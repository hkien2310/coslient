"""
auto_edit_timeline.py — Stateful Timeline Assembly Script

Gọi MCP server trực tiếp qua HTTP (không cần mcp library).
Toàn bộ dedup logic chạy trong Python — reliable, stateful.

Features:
  - Chronological order (single pass)
  - Dedup bằng (mediaRef, trimStartFrame) pair + cooldown window
  - Multi-query fallback (5 cấp)
  - [--inventory] Pre-inventory mode: scan toàn bộ palette → build pool → assign tối ưu

Usage:
    python3 scripts/auto_edit_timeline.py --project projects/video_060
    python3 scripts/auto_edit_timeline.py --project projects/video_060 --dry-run
    python3 scripts/auto_edit_timeline.py --project projects/video_060 --inventory
    python3 scripts/auto_edit_timeline.py --project projects/video_060 --single-kw
"""

import json
import os
import sys
import time
import argparse
import urllib.request
import urllib.error
import threading
from collections import defaultdict, deque

# Minimum scene duration to add to timeline (shorter = likely a bad beat slice)
MIN_DURATION_FRAMES = 24  # 0.4s at 60fps — skip scenes shorter than this

# Minimum source clip content required to be usable (hard filter on search results)
MIN_MOMENT_DURATION_S = 1.0  # reject moments shorter than 1s

# Cooldown: don't reuse same mediaRef within this many scenes
# Prevents adjacent scenes from showing same video file
MEDIAREF_COOLDOWN = 15

# ── MCP Client (Direct HTTP POST JSON-RPC, no external deps) ──────────────────

class MCPClient:
    """Minimal MCP client over direct HTTP POST JSON-RPC using only stdlib."""

    def __init__(self, url: str, timeout: int = 120):
        self.url = url
        self.timeout = timeout
        self._req_id = 0

    def _next_id(self):
        self._req_id += 1
        return self._req_id

    def connect(self):
        """Stateless connection check (does nothing)."""
        pass

    def call(self, method: str, params: dict) -> dict:
        """Send a JSON-RPC request over POST and return result."""
        rid = self._next_id()
        payload = json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": rid
        }).encode("utf-8")

        req = urllib.request.Request(
            self.url,
            data=payload,
            method="POST"
        )
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                if "error" in res_data:
                    raise RuntimeError(f"MCP error: {res_data['error']}")
                return res_data.get("result", {})
        except Exception as e:
            raise RuntimeError(f"Failed to communicate with MCP server: {e}")

    def tool_call(self, tool_name: str, arguments: dict) -> dict:
        return self.call("tools/call", {"name": tool_name, "arguments": arguments})


# ── Scene Processor ───────────────────────────────────────────────────────────

def make_fallback_queries(q1: str, single_kw: bool = False, kw_words: int = None) -> list[str]:
    """Generate progressive fallback queries from q1.

    If q1 contains ',', it uses the comma-separated structure:
      - 3 parts: [Noun], [Verb], [Adjective]
      - Primary: Noun + Verb + Adjective
      - Secondary: Noun + Verb
      - Tertiary: Noun
      - Quaternary: Noun + Adjective

    If q1 contains '|', it uses the legacy pipe-separated formula:
      - 4 parts: [SHOT_SIZE_OR_CONTEXT] | [SUBJECT] | [ACTION_OR_STATE] | [COLOR_OR_MOOD]
      - 3 parts: [SHOT_SIZE_OR_CONTEXT] | [SUBJECT] | [ACTION_OR_STATE]

    Otherwise, it uses default legacy fallback:
      - Primary: full phrase
      - Secondary: first 3 words
      - Tertiary: core noun
    """
    q1 = q1.strip()
    if not q1:
        return []

    # 0. Comma-separated structure (Option 1, Option 2, Option 3)
    if "," in q1:
        parts = [p.strip() for p in q1.split(",") if p.strip()]
        if len(parts) == 3:
            opt1, opt2, opt3 = parts[0], parts[1], parts[2]
            queries_ordered = [opt1, opt2, opt3]
        elif len(parts) == 2:
            opt1, opt2 = parts[0], parts[1]
            queries_ordered = [opt1, opt2]
        else:
            queries_ordered = [parts[0]]

        # Deduplicate while preserving order
        seen, result = set(), []
        for qp in queries_ordered:
            qp_clean = " ".join([w for w in qp.split() if w]).strip()
            if qp_clean and qp_clean not in seen:
                seen.add(qp_clean)
                result.append(qp_clean)
        return result


    # 1. Pipe-separated formula
    if "|" in q1:
        parts = [p.strip() for p in q1.split("|") if p.strip()]
        
        camera_terms = {
            "close-up", "closeup", "close up", "cu", "ecu", "extreme close-up", 
            "wide shot", "wide", "establishing shot", "medium shot", "medium", 
            "low angle", "high angle", "macro", "extreme wide shot", "extreme wide"
        }
        
        if len(parts) == 4:
            context_or_shot, subject, action_or_state, color_or_mood = parts[0], parts[1], parts[2], parts[3]
            
            # Compile ordered queries with color/mood consistency
            qp1 = f"{context_or_shot} {subject} {action_or_state} {color_or_mood}"
            qp2 = f"{subject} {action_or_state} {color_or_mood}"
            qp3 = f"{subject} {color_or_mood}"
            qp4 = f"{action_or_state} {color_or_mood}"
            qp5 = color_or_mood
            
            # Context + Color focus (if context is not a standard camera term)
            qp6 = None
            if context_or_shot.lower() not in camera_terms:
                qp6 = f"{context_or_shot} {color_or_mood}"
                
            queries_ordered = [qp1, qp2, qp3, qp4, qp5]
            if qp6:
                queries_ordered.append(qp6)
                
        elif len(parts) == 3:
            context_or_shot, subject, action_or_state = parts[0], parts[1], parts[2]
            
            # Compile ordered queries (backwards compatible 3-part)
            qp1 = f"{context_or_shot} {subject} {action_or_state}"
            qp2 = f"{subject} {action_or_state}"
            qp3 = subject
            qp4 = action_or_state
            
            # Context focus (only if context is not a standard camera term)
            qp5 = None
            if context_or_shot.lower() not in camera_terms:
                qp5 = context_or_shot
                
            queries_ordered = [qp1, qp2, qp3, qp4]
            if qp5:
                queries_ordered.append(qp5)
                
        elif len(parts) == 2:
            subject, action_or_state = parts[0], parts[1]
            qp1 = f"{subject} {action_or_state}"
            qp2 = subject
            qp3 = action_or_state
            queries_ordered = [qp1, qp2, qp3]
        else:
            queries_ordered = [parts[0]]

        # Deduplicate while preserving order
        seen, result = set(), []
        for qp in queries_ordered:
            qp_clean = " ".join([w for w in qp.split() if w]).strip()
            if qp_clean and qp_clean not in seen:
                seen.add(qp_clean)
                result.append(qp_clean)
        return result

    # 2. Legacy fallback mode (no pipes)
    words = [w for w in q1.split() if w]
    if not words:
        return []

    # Extract core noun using the skip list
    _SKIP = {"still", "dry", "empty", "dark", "old", "young", "big", "small",
             "wide", "deep", "rough", "soft", "heavy", "slow", "fast", "quiet",
             "bright", "dim", "warm", "cold", "tall", "low", "long", "short",
             "red", "blue", "green", "black", "white", "grey", "gray", "golden",
             "dirty", "tired", "wet", "burning", "falling", "rising", "rolling",
             "open", "cracked", "worn", "massive", "under", "over",
             "through", "across", "into", "onto", "beside", "resting", "sitting",
             "standing", "walking", "gripping", "leaning", "baking", "hanging",
             "drifting", "stretching", "curling", "swaying", "casting", "blocking"}
    core_noun = next((w for w in words if w.lower() not in _SKIP), words[0])

    if kw_words and not single_kw:
        n = min(kw_words, len(words))
        q1_trimmed = " ".join(words[:n])
        queries_ordered = [q1_trimmed, q1, core_noun]
    elif single_kw:
        queries_ordered = [core_noun, q1]
    else:
        q1_effective = q1
        q2_effective = " ".join(words[:3]) if len(words) > 3 else q1
        queries_ordered = [q1_effective, q2_effective, core_noun]

    seen, result = set(), []
    for q in queries_ordered:
        q_clean = " ".join([w for w in q.split() if w]).strip()
        if q_clean and q_clean not in seen:
            seen.add(q_clean)
            result.append(q_clean)

    return result



def process_scene(scene: dict, used_media_refs: set, fps: float,
                  mcp: MCPClient, dry_run: bool, label: str, single_kw: bool = False, kw_words: int = None) -> tuple[str, dict | None, str | None]:
    """
    Search for a clip and return the timeline entry dict and dedup key.
    2-pass search over all queries to prioritize visual novelty:
      Pass 1 (Tier 1 preference): Check all queries in order, looking for a clip where mediaRef NOT in recent_media.
      Pass 2 (Tier 2 fallback): If Pass 1 fails, check all queries in order, looking for a clip where (mediaRef, trimStart) NOT in used_segments.
    Returns: (status, entry_dict, dedup_key)
    """
    q_primary = scene.get("queryParams", "").strip()
    q_secondary = (scene.get("queryParamsSecondary") or scene.get("queryParamsSecond") or "").strip()
    q_tertiary = (scene.get("queryParamsTertiary") or scene.get("queryParamsThirdary") or "").strip()

    if q_secondary or q_tertiary:
        raw_queries = []
        if q_primary:
            raw_queries.append(q_primary)
        if q_secondary:
            raw_queries.append(q_secondary)
        if q_tertiary:
            raw_queries.append(q_tertiary)
        seen, queries = set(), []
        for qp in raw_queries:
            qp_clean = " ".join([w for w in qp.split() if w]).strip()
            if qp_clean and qp_clean not in seen:
                seen.add(qp_clean)
                queries.append(qp_clean)
    else:
        if not q_primary:
            return "skip_no_query", None, None
        if "," in q_primary:
            parts = [p.strip() for p in q_primary.split(",") if p.strip()]
            seen, queries = set(), []
            for qp in parts:
                qp_clean = " ".join([w for w in qp.split() if w]).strip()
                if qp_clean and qp_clean not in seen:
                    seen.add(qp_clean)
                    queries.append(qp_clean)
        else:
            queries = make_fallback_queries(q_primary, single_kw=single_kw, kw_words=kw_words)
    
    if dry_run:
        for qi, q in enumerate(queries, 1):
            print(f"      [DRY] q{qi}: {q}")
        return "dry_run", None, None

    chosen_moment = None
    scene_dur_s = scene["duration_frames"] / fps

    for qi, q in enumerate(queries, 1):
        try:
            result = mcp.tool_call("search_media", {
                "query": q,
                "scope": "visual",
                "limit": 100
            })
        except Exception as e:
            print(f"      ⚠️  search_media error (q{qi}): {e}")
            continue

        content = result.get("content", [])
        result_text = ""
        for c in content:
            if isinstance(c, dict) and c.get("type") == "text":
                result_text += c.get("text", "")

        try:
            result_data = json.loads(result_text)
        except (json.JSONDecodeError, TypeError):
            continue

        moments = result_data.get("moments", [])
        if not moments:
            continue

        annotated = []
        rejected_short = 0
        for m in moments:
            media_ref = m.get("mediaRef", "")
            start_s = m.get("startSeconds", 0.0)
            end_s   = m.get("endSeconds", start_s + 3.0)
            avail_s = end_s - start_s

            if avail_s < MIN_MOMENT_DURATION_S:
                rejected_short += 1
                continue

            trim_start = round(start_s * fps)
            key = (media_ref, trim_start)
            has_enough = avail_s >= scene_dur_s
            annotated.append((m, media_ref, trim_start, key, has_enough, avail_s, end_s))

        if rejected_short:
            print(f"      🚫 q{qi}: {rejected_short}/{len(moments)} moments too short (<{MIN_MOMENT_DURATION_S}s) — filtered")

        if not annotated:
            continue

        # Sort: moments with enough duration first
        annotated.sort(key=lambda x: (not x[4],))

        # Check if any candidate has not been used yet
        for m, media_ref, trim_start, key, has_enough, avail_s, end_s in annotated:
            if media_ref not in used_media_refs:
                chosen_moment = m
                chosen_moment["_trim_start"] = trim_start
                chosen_moment["_end_s"] = end_s
                chosen_moment["_avail_s"] = avail_s
                chosen_moment["_key"] = key
                if not has_enough:
                    print(f"      ⚠️  Short match: {avail_s:.1f}s < {scene_dur_s:.1f}s beat — will shift trimStart")
                print(f"      ✅ q{qi}: \"{q}\" → {chosen_moment['mediaRef']} @{chosen_moment.get('startSeconds', 0):.1f}s")
                break

        if chosen_moment:
            break

    if not chosen_moment:
        return "skip_all_dupes", None, None

    # Compile clip entry
    avail_s    = chosen_moment.get("_avail_s", 999.0)
    end_s      = chosen_moment.get("_end_s", chosen_moment.get("endSeconds", 0.0))
    scene_dur_s = scene["duration_frames"] / fps

    if avail_s < scene_dur_s:
        adjusted_start_s = max(0.0, end_s - scene_dur_s)
        trim_start_f = round(adjusted_start_s * fps)
        print(f"      [SHIFT] Shift trimStart: {chosen_moment.get('startSeconds',0):.1f}s -> {adjusted_start_s:.1f}s (covers full {scene_dur_s:.1f}s beat)")
    else:
        trim_start_f = chosen_moment["_trim_start"]

    entry = {
        "mediaRef":       chosen_moment["mediaRef"],
        "startFrame":     scene["start_frame"],
        "durationFrames": scene["duration_frames"],
        "trimStartFrame": trim_start_f,
    }
    return "added", entry, chosen_moment["mediaRef"]


def clear_timeline(mcp: MCPClient):
    """Query get_timeline and remove all existing tracks."""
    print("🧹 Clearing existing timeline tracks...")
    try:
        timeline = mcp.tool_call("get_timeline", {})
        content = timeline.get("content", [])
        timeline_text = ""
        for c in content:
            if isinstance(c, dict) and c.get("type") == "text":
                timeline_text += c.get("text", "")
        timeline_data = json.loads(timeline_text)
        tracks = timeline_data.get("tracks", [])
        if tracks:
            # Pass all 0-based indexes to remove_tracks in one call
            mcp.tool_call("remove_tracks", {"trackIndexes": list(range(len(tracks)))})
            print(f"✅ Removed {len(tracks)} existing tracks.")
        else:
            print("Timeline is already empty.")
    except Exception as e:
        print(f"⚠️  Error clearing timeline: {e}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Auto-edit timeline assembly with stateful dedup")
    parser.add_argument("--project", required=True, help="Path to project folder (e.g. projects/video_060)")
    parser.add_argument("--mcp-url", default="http://127.0.0.1:19789/mcp", help="Palmier MCP server URL")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without adding clips")
    parser.add_argument("--inventory", action="store_true",
                        help="Pre-inventory mode: scan all palette terms first, then assign optimally")
    parser.add_argument("--single-kw", action="store_true",
                        help="Use single core noun as search query (broader pool, less specific)")
    parser.add_argument("--kw-words", type=int, default=None, metavar="N",
                        help="Use first N words of query as q1 (e.g. --kw-words 2 or 3)")
    args = parser.parse_args()

    # ── Load beat_analysis.json ──
    beat_path = os.path.join(args.project, "beat_analysis.json")
    if not os.path.exists(beat_path):
        print(f"❌ Not found: {beat_path}")
        sys.exit(1)

    with open(beat_path, encoding="utf-8") as f:
        data = json.load(f)

    scenes = data["scene_cuts"]
    fps = float(data.get("fps", 60))
    song = data.get("song_name", "unknown")
    duration = data.get("duration_seconds", 0)

    print(f"📂 Project : {args.project}")
    print(f"🎵 Song    : {song}  ({duration}s)")
    print(f"⚙️  FPS     : {fps}")
    print(f"✂️  Scenes  : {len(scenes)}")

    # ── Auto-sync Visual Index ──────────────────────────────────────────────────
    # Regenerate 04_visual_index.txt if:
    #   (a) it doesn't exist, OR
    #   (b) 04_image_prompts.txt is newer (AI added prompts but forgot to run script)
    _docs_dir    = os.path.join(args.project, "docs")
    _prompts_src = os.path.join(_docs_dir, "04_image_prompts.txt")
    _prompts_alt = os.path.join(_docs_dir, "04_image_prompts_clean.txt")
    _index_file  = os.path.join(_docs_dir, "04_visual_index.txt")
    _summarizer  = os.path.join(os.path.dirname(__file__), "summarize_visuals.py")

    _src = _prompts_src if os.path.exists(_prompts_src) else (_prompts_alt if os.path.exists(_prompts_alt) else None)

    if _src and os.path.exists(_summarizer):
        _index_exists = os.path.exists(_index_file)
        _index_stale  = _index_exists and os.path.getmtime(_src) > os.path.getmtime(_index_file)

        if not _index_exists:
            print("⚡ Visual index missing — auto-generating...")
            import subprocess
            subprocess.run([sys.executable, _summarizer, "--project", args.project], check=False)
        elif _index_stale:
            print("⚡ Visual index stale (prompts updated) — auto-regenerating...")
            import subprocess
            subprocess.run([sys.executable, _summarizer, "--project", args.project], check=False)
        else:
            print("✅ Visual index up-to-date")

        # Print palette preview for log context
        if os.path.exists(_index_file):
            with open(_index_file, encoding="utf-8") as _f:
                for _line in _f:
                    if _line.strip() and not _line.startswith("#"):
                        print(f"   🎨 Palette: {_line.strip()[:120]}")
                        break
    else:
        print("ℹ️  No image prompts file found — visual index skipped")
    # ────────────────────────────────────────────────────────────────────────────

    # ── Validate queryParams ──
    missing = [i for i, s in enumerate(scenes) if not s.get("queryParams", "").strip()]
    if missing:
        print(f"\n❌ STOP: {len(missing)} scenes missing queryParams: {missing}")
        print("   → Re-run VisualPromptEngineer subagents (Step 3) first.")
        sys.exit(1)
    print("✅ All scenes have queryParams")

    # ── Scene info (2-pass disabled — chronological order) ──
    # lyric_scenes   = [s for s in scenes if s.get("has_vocals") and s.get("queryParams","").strip()]
    # ambient_scenes = [s for s in scenes if not s.get("has_vocals") and s.get("queryParams","").strip()]
    # print(f"\n✔️ Pass 1 (lyric):   {len(lyric_scenes)} scenes")
    # print(f"   Pass 2 (ambient): {len(ambient_scenes)} scenes")
    lyric_count   = sum(1 for s in scenes if s.get("has_vocals"))
    ambient_count = sum(1 for s in scenes if not s.get("has_vocals"))
    print(f"\n📋 Scenes: {lyric_count} lyric + {ambient_count} ambient = {len(scenes)} total (chronological)")

    if args.dry_run:
        print("\n🔍 DRY RUN — no clips will be added\n")

    # ── Connect to MCP ──
    if not args.dry_run:
        print(f"\n🔌 Connecting to MCP: {args.mcp_url}")
        mcp = MCPClient(args.mcp_url, timeout=120)
        try:
            mcp.connect()
            print("✅ MCP connected\n")
        except Exception as e:
            print(f"❌ Cannot connect to MCP server: {e}")
            print("   → Make sure CapCut + Palmier Pro plugin are running.")
            sys.exit(1)
    else:
        mcp = None

    # ── Find main audio track mediaRef ──
    audio_ref = None
    if not args.dry_run:
        try:
            print("🔍 Listing media library to find main audio asset...")
            media_res = mcp.tool_call("get_media", {})
            content = media_res.get("content", [])
            media_text = ""
            for c in content:
                if isinstance(c, dict) and c.get("type") == "text":
                    media_text += c.get("text", "")
            media_data = json.loads(media_text)
            
            # Match by song name
            song_clean = song.replace(".wav", "").strip().lower()
            for entry in media_data.get("entries", []):
                if entry.get("type") == "audio" and song_clean in entry.get("name", "").lower():
                    audio_ref = entry.get("id")
                    break
            
            # Fallback: first audio entry
            if not audio_ref:
                for entry in media_data.get("entries", []):
                    if entry.get("type") == "audio":
                        audio_ref = entry.get("id")
                        break
            
            if audio_ref:
                print(f"✅ Found main audio mediaRef: {audio_ref}")
            else:
                print("⚠️ Main audio asset not found in CapCut media library.")
        except Exception as e:
            print(f"⚠️ Error retrieving media list to find audioRef: {e}")

    # ── State ──
    used_media_refs: set = set()          # mediaRef — hard block any reuse of the same clip
    stats = defaultdict(int)
    all_entries = []

    # Queue the audio track first if found
    if audio_ref and not args.dry_run:
        total_frames = int(data.get("total_frames", round(duration * fps)))
        print(f"🎵 Queueing main audio clip (mediaRef: {audio_ref}) for {total_frames} frames")
        all_entries.append({
            "mediaRef": audio_ref,
            "startFrame": 0,
            "durationFrames": total_frames,
            "trimStartFrame": 0
        })

    def run_pass(pass_scenes: list, pass_label: str):
        total = len(pass_scenes)
        for i, scene in enumerate(pass_scenes, 1):
            idx = scene.get("scene_index", "?")
            t = scene.get("start_seconds", 0)
            q = scene.get("queryParams", "")
            dur = scene.get("duration_frames", 0)

            # Skip scenes that are too short (would appear as black flash)
            if dur < MIN_DURATION_FRAMES:
                print(f"  [{pass_label} {i:3d}/{total}] scene {idx} @ {t:.1f}s | ⏭️  TOO SHORT ({dur}f < {MIN_DURATION_FRAMES}f) — skip")
                stats["skip_too_short"] += 1
                continue

            print(f"  [{pass_label} {i:3d}/{total}] scene {idx} @ {t:.1f}s | \"{q}\"")

            result, entry, key = process_scene(
                scene, used_media_refs, fps, mcp, args.dry_run, pass_label,
                single_kw=getattr(args, "single_kw", False),
                kw_words=getattr(args, "kw_words", None)
            )
            stats[result] += 1
            if result == "added":
                all_entries.append(entry)
                used_media_refs.add(key)
            elif result == "skip_all_dupes":
                print(f"      ⚠️  SKIP: all candidates exhausted for this scene")
            elif result == "skip_no_query":
                print(f"      ⏭️  SKIP: no queryParams")

            if not args.dry_run:
                time.sleep(0.05)

    # ════════════════════════════════════════════════════════════
    # CHOOSE MODE
    # ════════════════════════════════════════════════════════════
    if args.inventory and not args.dry_run:
        print("\n" + "═" * 60)
        print("PRE-INVENTORY MODE — Scanning palette terms first")
        print("═" * 60)

        # 1. Extract palette terms from visual index
        palette_terms = []
        if os.path.exists(_index_file):
            with open(_index_file, encoding="utf-8") as _pf:
                for _pl in _pf:
                    _pl = _pl.strip()
                    if _pl and not _pl.startswith("#"):
                        palette_terms = [t.strip() for t in _pl.split(",") if len(t.strip()) > 2]
                        break
        if not palette_terms:
            from collections import Counter as _Counter
            _wf: _Counter = _Counter()
            for _s in scenes:
                for _w in _s.get("queryParams", "").split():
                    if len(_w) > 3:
                        _wf[_w.lower()] += 1
            palette_terms = [w for w, _ in _wf.most_common(20)]

        print(f"📚 Palette terms ({len(palette_terms)}): {palette_terms[:20]}")

        # 2. Search each term → build segment pool
        pool: list = []
        _seen_keys: set = set()
        for _term in palette_terms[:20]:
            try:
                _res = mcp.tool_call("search_media", {"query": _term, "scope": "visual", "limit": 100})
                _content = _res.get("content", [])
                _rt = "".join(c.get("text", "") for c in _content if isinstance(c, dict))
                _rd = json.loads(_rt)
                _moments = _rd.get("moments", [])
                _added = 0
                for _m in _moments:
                    _ref   = _m.get("mediaRef", "")
                    _start = _m.get("startSeconds", 0.0)
                    _end   = _m.get("endSeconds", _start + 3.0)
                    _dur   = _end - _start
                    if _dur < MIN_MOMENT_DURATION_S:
                        continue
                    _key = (_ref, round(_start * fps))
                    if _key not in _seen_keys:
                        _seen_keys.add(_key)
                        pool.append({"mediaRef": _ref, "start_s": _start, "end_s": _end,
                                     "dur_s": _dur, "score": _m.get("score", 0.0), "term": _term})
                        _added += 1
                print(f"  {_term:15s} → {len(_moments):2d} hits | +{_added} new | pool={len(pool)}")
            except Exception as _e:
                print(f"  ⚠️  scan '{_term}': {_e}")
            time.sleep(0.05)

        pool.sort(key=lambda x: -x["score"])
        print(f"\n✅ Pool: {len(pool)} unique segments")

        # 3. Assign greedily: chronological, prefer high-score
        _inv_used: set  = set()

        print("\n" + "═" * 60)
        print("INVENTORY ASSIGN — Chronological")
        print("═" * 60)

        for _i, _scene in enumerate(scenes, 1):
            _idx   = _scene.get("scene_index", "?")
            _t     = _scene.get("start_seconds", 0)
            _q     = _scene.get("queryParams", "")
            _dur_f = _scene.get("duration_frames", 0)
            _dur_s = _dur_f / fps

            if _dur_f < MIN_DURATION_FRAMES:
                print(f"  [INV {_i:3d}/{len(scenes)}] scene {_idx} @ {_t:.1f}s | ⏭️  TOO SHORT — skip")
                stats["skip_too_short"] += 1
                continue

            print(f"  [INV {_i:3d}/{len(scenes)}] scene {_idx} @ {_t:.1f}s | \"{_q}\"")

            _chosen = None

            # Pass 1: enough duration and not used
            for _seg in pool:
                _ref = _seg["mediaRef"]
                if _ref in _inv_used:
                    continue
                if _seg["dur_s"] >= _dur_s:
                    _chosen = _seg
                    break

            # Pass 2: any segment not used (short OK, will shift)
            if not _chosen:
                for _seg in pool:
                    _ref = _seg["mediaRef"]
                    if _ref in _inv_used:
                        continue
                    _chosen = _seg
                    break

            if not _chosen:
                print(f"      ❌ Pool exhausted for this scene")
                stats["skip_all_dupes"] += 1
                continue

            _avail_s = _chosen["dur_s"]
            _end_s   = _chosen["end_s"]
            if _avail_s < _dur_s:
                _adj = max(0.0, _end_s - _dur_s)
                _trim_f = round(_adj * fps)
                print(f"      ⚠️  Short {_avail_s:.1f}s < {_dur_s:.1f}s — shift trimStart to {_adj:.1f}s")
            else:
                _trim_f = round(_chosen["start_s"] * fps)

            print(f"      ✅ {_chosen['mediaRef']} @{_chosen['start_s']:.1f}s  term={_chosen['term']}  score={_chosen['score']:.3f}")
            _inv_used.add(_chosen["mediaRef"])
            stats["added"] += 1
            all_entries.append({
                "mediaRef":       _chosen["mediaRef"],
                "startFrame":     _scene["start_frame"],
                "durationFrames": _dur_f,
                "trimStartFrame": _trim_f,
            })
            time.sleep(0.05)

    else:
        # ── Chronological Single Pass (default) ──
        print("═" * 60)
        print("CHRONOLOGICAL PASS — All scenes in order")
        print("═" * 60)
        run_pass(scenes, "CHRONO")

    # ── Clear existing timeline and Add batch ──
    if not args.dry_run:
        clear_timeline(mcp)
        if all_entries:
            # Split: audio first, video clips after (so audio is on its own track)
            audio_entries = [e for e in all_entries if e.get("mediaRef") == audio_ref]
            video_entries = [e for e in all_entries if e.get("mediaRef") != audio_ref]

            print(f"\n🚀 Adding {len(video_entries)} video clips to timeline...")
            try:
                result = mcp.tool_call("add_clips", {"entries": video_entries})
                stats["added"] = len(video_entries)

                # ── Mute all video clips ──
                print("🔇 Muting all video clip audio tracks...")
                try:
                    tl = mcp.tool_call("get_timeline", {})
                    tl_text = ""
                    for c in tl.get("content", []):
                        if isinstance(c, dict) and c.get("type") == "text":
                            tl_text += c.get("text", "")
                    tl_data = json.loads(tl_text)

                    # Collect clip IDs from all VIDEO tracks (not audio tracks)
                    clip_ids = []
                    for track in tl_data.get("tracks", []):
                        if track.get("type") == "video":
                            for clip in track.get("clips", []):
                                clip_ids.append(clip["id"])

                    if clip_ids:
                        mcp.tool_call("set_clip_properties", {
                            "clipIds": clip_ids,
                            "volume": 0.0
                        })
                        print(f"✅ Muted {len(clip_ids)} video clips.")
                    else:
                        print("⚠️ No video clip IDs found to mute.")
                except Exception as e:
                    print(f"⚠️ Mute step failed: {e}")

                # ── Add main audio track ──
                if audio_entries:
                    print(f"🎵 Adding main audio track...")
                    try:
                        mcp.tool_call("add_clips", {"entries": audio_entries})
                        print("✅ Audio track added.")
                    except Exception as e:
                        print(f"⚠️ Audio track add failed: {e}")

                print("\n✅ Timeline assembled successfully.")

            except Exception as e:
                print(f"❌ Failed to add video clips: {e}")
                sys.exit(1)

    # ── Summary ──
    total_added = stats["added"]
    total_skip_dupe = stats["skip_all_dupes"]
    total_skip_noq = stats["skip_no_query"]
    total_too_short = stats["skip_too_short"]
    total_dry = stats["dry_run"]
    print()
    print("═" * 60)
    print("✅ DONE")
    if args.dry_run:
        print(f"   Dry run:         {total_dry} scenes would be processed")
        print(f"   Skip (too short):{total_too_short}")
    else:
        print(f"   Added (visuals): {total_added}")
        print(f"   Skip (too short):{total_too_short}")
        print(f"   Skip (dupes):    {total_skip_dupe}")
        print(f"   Skip (no query): {total_skip_noq}")
        print(f"   Total scenes:    {len(scenes)}")
    print("═" * 60)


if __name__ == "__main__":
    main()
