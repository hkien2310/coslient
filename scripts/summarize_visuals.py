#!/usr/bin/env python3
"""
summarize_visuals.py — Bước 3.5: Tổng hợp Visual Index từ 04_image_prompts.txt

Đọc docs/04_image_prompts.txt (dài 100KB+) → xuất docs/04_visual_index.txt (ngắn ~2KB)

04_visual_index.txt là file tham chiếu cô đọng:
  - Mỗi dòng: "# Tag | object1, object2, object3"
  - AI đọc TRƯỚC KHI search → biết palette hình ảnh chính xác của video
  - Không đọc file gốc 100KB — chỉ đọc index 2KB

Usage:
    python3 scripts/summarize_visuals.py --project projects/video_057

Output:
    projects/video_057/docs/04_visual_index.txt
"""

import re
import argparse
from pathlib import Path

_BOILERPLATE = {
    # camera / shot
    "wide", "medium", "full", "close", "macro", "overhead", "eye-level",
    "slightly", "low", "high", "angle", "shot", "ground-level", "through",
    "frame", "establishing", "fragmented", "low-ground", "close-up",
    "over-the-shoulder", "high-angle", "through-the-frame",
    # lighting / style
    "bright", "luminous", "warm", "soft", "lifted", "shadows", "daylight",
    "cream", "honey", "gold", "tones", "ambient", "glow", "indigo", "blue",
    "cozy", "golden", "amber", "dappled", "glittering", "darkness", "pitch",
    "black", "absolutely", "no",
    # style boilerplate
    "handcrafted", "miniature", "diorama", "photography", "tilt", "shift",
    "lens", "gentle", "loving", "atmosphere", "smooth", "hand", "painted",
    "character", "handsome", "gracefully", "aging", "face", "kind", "eyes",
    "wool", "like", "hair", "subtle", "fabric", "detail", "realistic", "adult",
    "body", "proportions", "correct", "head", "to", "ratio", "open", "airy",
    "composition", "generous", "negative", "space", "16", "9",
    # prepositions / filler
    "a", "an", "the", "of", "in", "on", "at", "by", "for", "and", "or",
    "with", "from", "into", "onto", "over", "under", "across", "through",
    "beyond", "seen", "is", "are", "was", "be", "been", "has", "have", "not",
    "each", "this", "that", "his", "her", "its", "their", "our", "man's",
    # action verbs (không cần trong index)
    "resting", "sitting", "standing", "leaning", "looking", "walking",
    "holding", "touching", "cradling", "filtering", "creating", "stretching",
    "filled", "broken", "fallen", "running", "sweeping", "kneeling", "wiping",
    "watering", "upward", "downward", "playfully", "peacefully", "calmly",
    "proudly", "gently", "heavily", "slowly", "warmly", "quietly",
    "next", "against", "behind", "above", "below", "dwarfed", "engulfed",
    "wrapping", "covering", "curving", "sprawling", "growing", "falling",
    # size / quantity adjectives (giữ lại nếu cần nhưng thường noise)
    "tiny", "small", "large", "giant", "massive", "enormous", "impossibly",
    "vast", "great", "old", "young", "single", "colossal", "wall-like",
    # body parts (không useful cho search)
    "brow", "sweat", "shoulder", "shoulders", "hands", "arms",
    # color adjectives phổ biến (giữ distinctive colors thôi)
    "rustic", "weathered", "sunbaked", "cracked", "muddy", "faded", "rich",
    "normal", "sized", "outdoors", "sunny", "sunlit", "evening", "night", "day",
    "background", "foreground", "mid", "ground", "mid-ground",
    # person descriptors
    "man", "woman", "boy", "girl", "child", "grandson", "people", "person",
    "elderly", "adult", "figure",
    # generic locations already in category
    "courtyard", "backyard", "porch", "farm",
    # other filler
    "completely", "deep", "rough", "strong", "wooden-like", "textured",
    "color", "natural", "style", "look", "feel", "kind",
}


def extract_objects(prompt_text: str) -> list[str]:
    """
    Extract 3-6 core visual objects/nouns from a full prompt string.
    Returns list of short noun phrases.
    """
    # Remove style boilerplate suffix (everything after "bright luminous" or "handcrafted")
    cutoffs = ["bright luminous", "handcrafted miniature", "warm gentle loving",
               "smooth hand-painted", "16:9", "tilt-shift"]
    for cutoff in cutoffs:
        idx = prompt_text.lower().find(cutoff)
        if idx > 0:
            prompt_text = prompt_text[:idx]

    # Tokenize to words, remove punctuation
    raw_words = re.findall(r"[a-zA-Z]+(?:[-'][a-zA-Z]+)*", prompt_text.lower())

    # Filter boilerplate
    meaningful = [w for w in raw_words if w not in _BOILERPLATE and len(w) > 2]

    # Deduplicate while preserving order
    seen, result = set(), []
    for w in meaningful:
        if w not in seen:
            seen.add(w)
            result.append(w)

    # Return top 6 most meaningful (first = most prominent in prompt)
    return result[:6]


def parse_prompts(filepath: Path) -> list[dict]:
    """Parse 04_image_prompts.txt into list of {tag, text}."""
    content = filepath.read_text(encoding="utf-8")
    entries = []

    # Split by prompt headers: "# Prompt N: ..." or "# BATCH ..."
    # Keep non-batch headers only
    lines = content.split("\n")
    current_tag = None
    current_lines = []

    for line in lines:
        # Detect prompt header: "# Prompt 1: Intro - ..."
        m = re.match(r"^#\s+Prompt\s+(\d+)[:\s]+(.+)", line)
        if m:
            # Save previous
            if current_tag and current_lines:
                entries.append({
                    "tag": current_tag,
                    "text": " ".join(current_lines).strip()
                })
            num = m.group(1)
            desc = m.group(2).strip()
            current_tag = f"P{num.zfill(3)} {desc}"
            current_lines = []
        elif line.startswith("#") or line.strip() == "---":
            # Batch header or separator — save if we have something
            if current_tag and current_lines:
                entries.append({
                    "tag": current_tag,
                    "text": " ".join(current_lines).strip()
                })
            current_tag = None
            current_lines = []
        elif current_tag and line.strip():
            current_lines.append(line.strip())

    # Last entry
    if current_tag and current_lines:
        entries.append({
            "tag": current_tag,
            "text": " ".join(current_lines).strip()
        })

    return entries


def main():
    parser = argparse.ArgumentParser(
        description="Rút gọn 04_image_prompts.txt → 04_visual_index.txt"
    )
    parser.add_argument("--project", required=True,
                        help="Project folder (e.g. projects/video_057)")
    parser.add_argument("--input", default=None,
                        help="Override input file path")
    args = parser.parse_args()

    project_dir = Path(args.project)
    docs_dir    = project_dir / "docs"
    input_file  = Path(args.input) if args.input else docs_dir / "04_image_prompts.txt"
    output_file = docs_dir / "04_visual_index.txt"

    if not input_file.exists():
        # Try clean version
        alt = docs_dir / "04_image_prompts_clean.txt"
        if alt.exists():
            input_file = alt
        else:
            print(f"❌ Không tìm thấy {input_file}")
            return

    print(f"📂 Đọc : {input_file}  ({input_file.stat().st_size // 1024}KB)")

    entries = parse_prompts(input_file)
    print(f"🎨 Tìm thấy: {len(entries)} prompts")

    if not entries:
        print("⚠️  Không parse được prompt nào. Kiểm tra format file.")
        return

    # Build output lines
    out_lines = []
    out_lines.append("# Visual Index — Tham chiếu hình ảnh cô đọng")
    out_lines.append("# Đọc file này trước khi search_media để biết visual palette của video")
    out_lines.append("# Format: Tag | object1, object2, object3, ...")
    out_lines.append("#" + "-" * 70)
    out_lines.append("")

    # Global palette (deduplicated across all prompts)
    all_objects: list[str] = []
    seen_global: set[str] = set()

    for entry in entries:
        objects = extract_objects(entry["text"])
        # Per-prompt line
        obj_str = ", ".join(objects) if objects else "(no objects extracted)"
        # Truncate tag to reasonable length
        tag = entry["tag"][:55]
        out_lines.append(f"{tag} | {obj_str}")

        # Accumulate global
        for o in objects:
            if o not in seen_global:
                seen_global.add(o)
                all_objects.append(o)

    # Summary section at top
    global_summary = ", ".join(all_objects[:40])  # top 40 most prominent
    summary_lines = [
        "",
        "#" + "=" * 70,
        "# GLOBAL VISUAL PALETTE (40 concepts nổi bật nhất — copy cho AI)",
        "#" + "=" * 70,
        global_summary,
        "#" + "=" * 70,
        "",
    ]

    final_lines = summary_lines + out_lines
    output_text = "\n".join(final_lines)
    output_file.write_text(output_text, encoding="utf-8")

    size_in  = input_file.stat().st_size
    size_out = output_file.stat().st_size
    reduction = (1 - size_out / size_in) * 100

    print(f"✅ Đã ghi: {output_file}")
    print(f"   {size_in:,} bytes → {size_out:,} bytes  ({reduction:.0f}% nhỏ hơn)")
    print()
    print("📋 Global palette (preview):")
    print("  " + global_summary[:180] + ("..." if len(global_summary) > 180 else ""))


if __name__ == "__main__":
    main()
