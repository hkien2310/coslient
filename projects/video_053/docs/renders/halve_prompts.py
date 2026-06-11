import os

files = [
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/04_image_prompts.txt",
    "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/04_world_prompts.txt"
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read().strip()
        
        # Split by empty lines
        prompts = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        # Keep only even prompts (index 1, 3, 5... which correspond to prompt 2, 4, 6...)
        kept_prompts = [prompts[i] for i in range(len(prompts)) if i % 2 != 0]
        
        with open(filepath, 'w') as f:
            for p in kept_prompts:
                f.write(p + "\n\n")
                
        print(f"Processed {filepath}: Reduced from {len(prompts)} to {len(kept_prompts)} prompts.")
