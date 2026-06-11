import os
import re

def check_banned_words(content):
    banned_words = [
        r'\bdead\b', r'\bdying\b', r'\bdeath\b', r'\bghost\b', r'\bhaunted\b', r'\bhaunting\b',
        r'\bdecay\b', r'\brotting\b', r'\brotten\b', r'\bkill\b', r'\bkilling\b', r'\bblood\b', 
        r'\bviolence\b', r'\bviolent\b', r'\bnude\b', r'\bnaked\b', r'\bsuicide\b', r'\bweapon\b'
    ]
    leaks = []
    lines = [line for line in content.split('\n') if line.strip()]
    for idx, line in enumerate(lines):
        for pattern in banned_words:
            if re.search(pattern, line.lower()):
                leaks.append(f"Line {idx+1}: {line}")
                break
    return leaks

def merge_files(parts, output_file):
    final_content = []
    for part in parts:
        if os.path.exists(part):
            with open(part, 'r') as infile:
                content = infile.read().strip()
                if content:
                    final_content.append(content)
                    
    full_text = "\n\n".join(final_content)
    with open(output_file, 'w') as outfile:
        outfile.write(full_text)
    
    print(f"Merged {len(parts)} parts into {output_file}")
    
    lines = [line.strip() for line in full_text.split('\n') if line.strip()]
    print(f"Total valid prompt lines in {output_file}: {len(lines)}")
    
    leaks = check_banned_words(full_text)
    if leaks:
        print(f"WARNING: Found {len(leaks)} banned words leaks in {output_file}:")
        for leak in leaks:
            print(f"  -> {leak[:100]}...")
    else:
        print(f"SUCCESS: Zero Banned Words found in {output_file}.")

story_parts = [
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7.1_story_part1.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7.1_story_part2.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7.1_story_part3.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7.1_story_part4.txt"
]

world_parts = [
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7.1_world_part1.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7.1_world_part2.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7.1_world_part3.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7.1_world_part4.txt"
]

merge_files(story_parts, "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/04_image_prompts.txt")
merge_files(world_parts, "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/04_world_prompts.txt")
