import argparse
import librosa
import json
import numpy as np
import os

def normalize(array):
    m = np.max(array)
    return array / m if m > 0 else array

def analyze_beats(audio_path, transcription_path, output_path, fps=60, min_duration=2.0, cut_style='normal'):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
    print(f"Loading audio from {audio_path}...")
    y, sr = librosa.load(audio_path, sr=None)
    
    segments = []
    if transcription_path and os.path.exists(transcription_path):
        print(f"Loading transcription from {transcription_path}...")
        with open(transcription_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Smart cleaning logic using word-level timestamps to fix ASR hallucinations (e.g. Whisper stretching intro words)
            if "segments" in data and "words" in data and len(data["words"]) > 0:
                print("Cleaning transcription using word-level timestamps...")
                words = data["words"]
                word_idx = 0
                for seg in data["segments"]:
                    # seg is [text, start, end]
                    seg_text = seg[0]
                    seg_words = []
                    # Find all words that belong to this segment
                    while word_idx < len(words) and words[word_idx][1] < seg[2]:
                        seg_words.append(words[word_idx])
                        word_idx += 1
                        
                    if seg_words:
                        # Check first word
                        first_w = seg_words[0]
                        first_start, first_end = first_w[1], first_w[2]
                        if first_end - first_start > 1.5:
                            # Stretched word, adjust segment start
                            seg[1] = max(0, first_end - 0.5)
                        else:
                            seg[1] = first_start
                            
                        # Check last word
                        last_w = seg_words[-1]
                        seg[2] = last_w[2]
                        
                    segments.append(seg)
            elif "segments" in data:
                segments = data["segments"]
            else:
                segments = data

    print("Extracting features using librosa...")
    # 1. Beat Grid
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    
    # 2. Novelty / Onset Strength
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onset_env = normalize(onset_env)
    
    # 3. RMS Energy
    rms = librosa.feature.rms(y=y)[0]
    rms = normalize(rms)

    # 4. Phrase Boundaries
    phrase_boundaries = []
    for seg in segments:
        if len(seg) >= 3:
            phrase_boundaries.append(seg[1]) # Start
            phrase_boundaries.append(seg[2]) # End

    duration = librosa.get_duration(y=y, sr=sr)
    
    # Calculate scores for all beats
    print("Calculating Scene Cut Priority Scores...")
    beat_scores = []
    for i, t in enumerate(beat_times):
        frame_idx = beat_frames[i]
        
        # Novelty Score (0 to 1)
        novelty_score = float(onset_env[frame_idx]) if frame_idx < len(onset_env) else 0.0
        
        # Energy Surge (0 to 1)
        energy_surge = 0.0
        if i > 0:
            prev_frame_idx = beat_frames[i-1]
            surge = float(rms[frame_idx] - rms[prev_frame_idx])
            energy_surge = max(0.0, surge)
            
        # Phrase Boundary Proximity
        phrase_score = 0.0
        boundary_dist = min([abs(t - pb) for pb in phrase_boundaries]) if phrase_boundaries else 999
        if boundary_dist < 0.5:
            phrase_score = 0.4  # High priority if very close
        elif boundary_dist < 1.0:
            phrase_score = 0.2
            
        # Downbeat Approximation (assuming 4/4 time, every 4th beat)
        downbeat_score = 0.1 if (i % 4 == 0) else 0.0
        
        # Final Score
        total_score = (novelty_score * 0.4) + (energy_surge * 0.3) + phrase_score + downbeat_score
        total_score = min(1.0, total_score) # Cap at 1.0
        
        # Find reasons
        reasons = []
        if phrase_score > 0:
            reasons.append("Phrase Boundary")
        if novelty_score > 0.6:
            reasons.append("Strong Onset/Novelty")
        if energy_surge > 0.2:
            reasons.append("Energy Surge")
        if downbeat_score > 0:
            reasons.append("Downbeat")
            
        beat_scores.append({
            "index": i,
            "time": t,
            "score": total_score,
            "reasons": reasons
        })

    # Filter Scene Cuts based on min_duration
    print("Selecting Scene Cuts...")
    scene_cuts = []
    last_cut_time = -999.0
    
    # Force the first cut at 0.0 to fix the black frame issue
    if len(beat_scores) > 0:
        first_beat = beat_scores[0]
        scene_cuts.append({
            "start_seconds": 0.0,
            "start_frame": 0,
            "score": 1.0,
            "reasons": ["Forced First Cut"]
        })
        last_cut_time = 0.0

    i = 0
    while i < len(beat_scores):
        b = beat_scores[i]
        
        # Look ahead window to find the best local peak
        if b["time"] - last_cut_time >= min_duration:
            # We can cut now. But let's check if there's a much better cut in the next 1 second.
            window_end_time = b["time"] + 1.0
            best_beat = b
            
            for j in range(i, len(beat_scores)):
                if beat_scores[j]["time"] > window_end_time:
                    break
                if beat_scores[j]["score"] > best_beat["score"]:
                    best_beat = beat_scores[j]
            
            cut_info = {
                "start_seconds": round(float(best_beat["time"]), 3),
                "start_frame": int(best_beat["time"] * fps),
                "score": round(float(best_beat["score"]), 3),
                "reasons": best_beat["reasons"]
            }
            scene_cuts.append(cut_info)
            last_cut_time = best_beat["time"]
            
            # Skip i to the beat we actually picked
            i = best_beat["index"]
        
        i += 1

    # ── Sparse Gap Fill ────────────────────────────────────────────────────────
    # Detect sections with no beat cuts (e.g. quiet outro, soft intro).
    # Any gap wider than min_duration × 2.5 gets subdivided with forced cuts
    # spaced min_duration apart — so the timeline is always fully covered.
    SPARSE_THRESHOLD = min_duration * 2.5
    forced_cuts = []

    # Build a list of all time boundaries to check gaps between
    all_cut_times = [c["start_seconds"] for c in scene_cuts] + [duration]

    for k in range(len(all_cut_times) - 1):
        gap_start = all_cut_times[k]
        gap_end   = all_cut_times[k + 1]
        gap_len   = gap_end - gap_start

        if gap_len > SPARSE_THRESHOLD:
            # Insert cuts every min_duration seconds inside this gap
            t = gap_start + min_duration
            while t < gap_end - (min_duration * 0.4):
                forced_cuts.append({
                    "start_seconds": round(t, 3),
                    "start_frame": int(t * fps),
                    "score": 0.0,
                    "reasons": ["Forced Gap Fill"]
                })
                t += min_duration

    if forced_cuts:
        scene_cuts.extend(forced_cuts)
        scene_cuts.sort(key=lambda c: c["start_seconds"])
        print(f"  → Inserted {len(forced_cuts)} forced gap-fill cuts (sparse sections covered).")
    # ──────────────────────────────────────────────────────────────────────────

    # Post-process to add end_frames, durations, and calculate lyric overlap weight
    for seg in segments:
        seg_start, seg_end = seg[1], seg[2]
        if len(seg) == 3:
            seg.append(seg_end - seg_start) # seg[3] is duration
            
    for idx in range(len(scene_cuts)):
        start_t = scene_cuts[idx]["start_seconds"]
        if idx + 1 < len(scene_cuts):
            end_t = scene_cuts[idx+1]["start_seconds"]
            end_frame = scene_cuts[idx+1]["start_frame"]
        else:
            end_t = duration
            end_frame = int(duration * fps)
            
        scene_cuts[idx]["end_seconds"] = round(float(end_t), 3)
        scene_cuts[idx]["end_frame"] = end_frame
        scene_cuts[idx]["duration_frames"] = end_frame - scene_cuts[idx]["start_frame"]
        
        # Calculate overlap with all lyric segments
        best_seg = None
        max_overlap_duration = 0.0
        
        for seg in segments:
            seg_text, seg_start, seg_end, seg_dur = seg[0], seg[1], seg[2], seg[3]
            overlap_start = max(start_t, seg_start)
            overlap_end = min(end_t, seg_end)
            overlap_dur = max(0, overlap_end - overlap_start)
            
            if overlap_dur > max_overlap_duration:
                max_overlap_duration = overlap_dur
                best_seg = seg
                
        # Determine the role of this scene
        has_vocals = False
        vocals = ""
        weight = 0.0
        
        if best_seg and max_overlap_duration > 0:
            seg_text, seg_start, seg_end, seg_dur = best_seg[0], best_seg[1], best_seg[2], best_seg[3]
            has_vocals = True
            vocals = seg_text
            weight = max_overlap_duration / seg_dur if seg_dur > 0 else 0
        
        # queryParams is intentionally left empty — will be filled by VisualPromptEngineer subagent (Step 3 of auto-edit pipeline).
        # lyric_context provides raw lyric hint for the subagent to interpret emotionally, not literally.
        scene_cuts[idx]["has_vocals"] = has_vocals
        scene_cuts[idx]["vocals_in_segment"] = vocals
        scene_cuts[idx]["lyric_context"] = vocals if vocals else ""
        scene_cuts[idx]["queryParams"] = ""  # Placeholder — filled by VisualPromptEngineer subagent
        scene_cuts[idx]["queryParamsSecondary"] = ""
        scene_cuts[idx]["queryParamsTertiary"] = ""
        scene_cuts[idx]["overlap_weight"] = round(weight, 2)

    output_data = {
        "song_name": os.path.basename(audio_path),
        "fps": fps,
        "duration_seconds": round(duration, 2),
        "total_frames": int(duration * fps),
        "min_duration_setting": min_duration,
        "cut_style": cut_style,
        "cuts_count": len(scene_cuts),
        "scene_cuts": scene_cuts
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(scene_cuts)} scene cuts to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart Scene Cut Detection using librosa.")
    parser.add_argument("--audio", required=True, help="Path to the WAV audio file")
    parser.add_argument("--transcription", required=False, help="Path to JSON transcription segments")
    parser.add_argument("--output", required=True, help="Path to save the output json")
    parser.add_argument("--fps", type=int, default=60, help="Timeline FPS (default: 60)")
    parser.add_argument("--min-duration", type=float, default=2.0, help="Minimum duration between cuts in seconds")
    parser.add_argument("--cut-style", type=str, default="normal", help="Cut style identifier")
    
    args = parser.parse_args()
    
    # Simple logic mapping cut-style to min_duration if user specifies style
    if args.cut_style == "fast":
        args.min_duration = 1.0
    elif args.cut_style == "slow":
        args.min_duration = 3.5
        
    analyze_beats(args.audio, args.transcription, args.output, args.fps, args.min_duration, args.cut_style)
