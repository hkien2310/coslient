import random
import os

LYRICS_FILE = "../docs/03_clean_lyrics.txt"
OUTPUT_FILE = "../docs/04_full_200_prompts_warm.txt"

LOCKED_COLOR_TONE = "rich tonal depth with luminous highlights and warm shadow detail, bright and luminous color palette of soft cream, honey-gold, and light amber"

# Base Style from Version 1.0 (Porcelain skin, needle-felted wool hair, adult proportions)
BASE_STYLE = "handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, handsome and gracefully aging elderly face, clean smooth features with minimal soft laugh lines, no deep-cut wrinkles, kind eyes, fluffy needle-felted wool hair with visible fine fibers, subtle fabric detail, smooth matte porcelain skin, realistic adult human body proportions, correct head-to-body ratio of a real adult person, warm natural daylight or radiant amber light with lifted soft warm shadows, absolutely no pitch-black darkness, peaceful everyday realism, airy and healing mood, 16:9, not photorealistic, not glossy 3D"

# Master Negative Block from Version 1.0
NEGATIVE_BLOCK = "--no chibi, oversized head, oversized eyes, cute anime proportions, doll-like toy body, solid clay hair, chunky sculpted hair mass, melted texture, blob-like hair, plastic finish, heavy claymation look, deep wrinkles, harsh facial lines, sunken cheeks, hollow eyes, cracked skin, waxy skin, creepy puppet face, pitch-black darkness, heavy black shadows, gloomy night, cold dark blue tones, muddy colors, harsh dark contrast, glossy plastic shine, glossy 3D, deformed hands, children, kids, toddlers, babies, text, handwriting"

ACCENT_COLORS = [
    "a vivid orange enamel kettle",
    "a faded cornflower-blue cup",
    "a muted sage-green cloth"
]

SHOT_SIZES = [
    "Wide establishing shot",
    "Medium-wide shot",
    "Medium shot",
    "Close intimate shot",
    "Macro detail shot"
]

ANGLES = [
    "eye-level intimate angle",
    "slightly low dignity angle",
    "gentle high tenderness angle",
    "ground-level path angle",
    "over-the-shoulder angle"
]

BASE_SCENES = [
    "An elderly deep-sea gardener inside a cozy bright underwater cottage, looking at the warm fire crackling in a smooth ceramic stove",
    "Giant gentle shadows cast by the fire dancing against the smooth matte wooden walls of the underwater cabin",
    "A beautifully crafted smooth matte copper diving suit with subtle fabric details resting peacefully on a wooden stand",
    "The elderly gardener stepping out of the glass dome onto a lush meadow of soft swaying ocean grass",
    "The gardener holding out his smooth, clean, elegant hand into the gentle underwater current",
    "Tiny silver-and-gold fishes swimming playfully around his outstretched gentle fingers",
    "The gardener standing peacefully as a gentle underwater current flows past his copper suit without resistance",
    "The deep ocean floor transformed into a peaceful, welcoming garden with carefully tended sand paths",
    "Friendly fish swimming past the gardener's window like neighbors passing by a countryside home",
    "The gardener gently pruning a soft kelp plant with his clean hands, tending to the underwater flora",
    "Warm light glowing from carefully arranged coral beds as the gardener smooths the sand around them",
    "The underwater cottage sitting peacefully on the sand, needing no anchor or harbor",
    "Every drop of the ocean surrounding the cottage feeling warm, safe, and exactly like home",
    "The gardener standing proudly among his blooming coral beds, holding a smooth wooden tending stick",
    "A small sunken glass bottle resting half-buried in the soft pristine ocean sand",
    "The gardener carefully and gently lifting the glass bottle with both hands, inspecting it with kind eyes",
    "His elegant hands brushing away the soft sand to reveal the clear, smooth glass of the bottle",
    "The gardener placing the clean glass bottle carefully down in a safe spot for a small creature",
    "A tiny hermit crab approaching the freshly cleaned glass bottle to use as a safe, quiet little house",
    "The tiny crab crawling inside the bottle, safe from the gentle ocean tide",
    "The gardener sitting on a smooth wooden bench outside his cottage, watching the calm currents",
    "The ocean floor stretching out like a peaceful, well-tended terrestrial countryside",
    "A massive, gentle whale swimming peacefully overhead, singing a soothing lullaby",
    "The gardener softly sweeping a garden path of white sand using a smooth wooden broom",
    "Tending to a cluster of luminous, warm-glowing coral that lights up the deep sea garden",
    "The peaceful glass-dome cottage radiating warm amber light into the blue water",
    "The gardener sitting quietly by his window, feeling completely at home in the deep sea",
    "The gardener walking slowly through his glowing underwater garden, inspecting his beautiful work",
    "A giant, gentle manta ray resting on the sand, tangled in a heavy rusted iron chain",
    "The gardener patiently and gently untangling the iron chain using only his smooth, bare hands",
    "The manta ray bowing its massive, smooth wings in a gesture of gratitude and goodbye",
    "The manta gliding gracefully away into the luminous, peaceful upper ocean waters",
    "The gardener watching the manta leave, a warm, gentle smile on his gracefully aging face",
    "The gardener carefully planting a small, glowing coral seed into a perfectly prepared mound of sand",
    "The cottage sitting quietly, a beacon of safety and warmth in the vast peaceful ocean",
    "The gardener looking around his perfect underwater home, filled with quiet gratitude",
    "The gardener standing tall and peaceful among his thriving, luminous deep-sea plants",
    "His smooth matte copper diving helmet resting neatly on a wooden chair inside the warm cottage",
    "The gardener sitting in his armchair, breathing in the warm, clean air of his sanctuary",
    "The gardener looking out the window at his beautiful underwater garden, finally truly home"
]

with open(LYRICS_FILE, "r") as f:
    lyrics = [line.strip() for line in f if line.strip()]

if len(lyrics) > len(BASE_SCENES):
    BASE_SCENES.extend([BASE_SCENES[-1]] * (len(lyrics) - len(BASE_SCENES)))
lyrics = lyrics[:len(BASE_SCENES)]

prompts = []
for i, lyric in enumerate(lyrics):
    base_scene = BASE_SCENES[i]
    
    for j in range(5):
        shot = SHOT_SIZES[j % len(SHOT_SIZES)]
        angle = ANGLES[(i + j) % len(ANGLES)]
        accent = ACCENT_COLORS[(i + j) % len(ACCENT_COLORS)]
        
        if j == 0:
            detail = f"slanted morning sunlight casting long warm shadows across a smooth wooden floor, {accent} resting nearby"
        elif j == 1:
            detail = f"a patch of gold sunlight on a polished golden-oak table, {accent} in the background"
        elif j == 2:
            detail = f"steam rising slowly from a porcelain cup in morning light, {accent} on the table"
        elif j == 3:
            detail = f"soft window light falling across the elderly character's smooth porcelain hands, {accent} nearby"
        else:
            detail = f"late afternoon sun catching the rim of a ceramic cup, making it glow like amber, {accent} placed thoughtfully"
            
        full_prompt = f"{base_scene}, {detail}, {shot}, {angle}, {LOCKED_COLOR_TONE}, {BASE_STYLE} {NEGATIVE_BLOCK}"
        prompts.append(full_prompt)

with open(OUTPUT_FILE, "w") as f:
    for p in prompts:
        f.write(f"{p}\n\n")

print(f"Successfully generated {len(prompts)} prompts in {OUTPUT_FILE}")
