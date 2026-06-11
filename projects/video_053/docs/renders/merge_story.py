import os

parts = [
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7_part1.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7_part2.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7_part3.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7_part4.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7_part5.txt"
]

output_file = "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/04_image_prompts.txt"

with open(output_file, 'w') as outfile:
    for part in parts:
        if os.path.exists(part):
            with open(part, 'r') as infile:
                outfile.write(infile.read().strip() + "\n\n")

print(f"Merged {len(parts)} parts into {output_file}")
