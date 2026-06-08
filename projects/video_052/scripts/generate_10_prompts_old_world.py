import random
import os

LYRICS_FILE = "../docs/03_clean_lyrics.txt"
OUTPUT_FILE = "../docs/04_test_10_prompts_old_world.txt"

# Updated Base Style from Old World Claymation (Anti-Goblin Drift)
BASE_STYLE = "stop-motion claymation puppet, handcrafted European village cinema, macro photography, tilt-shift lens, kind and expressive elderly human face with a long aquiline nose and large ears, smooth matte clay puppet skin with warm beige clay tone, warm gentle eyes with depth and life, soft natural character lines around eyes and mouth, wild wispy silver-white hair with fine natural strands, realistic adult human body proportions with correct head-to-body ratio, long expressive elderly puppet hands, chunky knit wool sweater or worn tweed coat, aged stone Mediterranean village setting, cobblestone streets, warm/cool lighting contrast, rich cinematic depth of field, 16:9"

# Updated Master Negative Block (Anti-Goblin Drift)
NEGATIVE_BLOCK = "--no goblin, troll, creature, monster, fantasy creature, rough matted fibrous skin, horror creature face, grotesque, chibi, oversized head, oversized cute eyes, cute anime proportions, smooth porcelain skin, warm_storybook aesthetic, plastic shine, glossy 3D, Pixar-style smooth animation, flat clean architecture, healing-cozy pastel palette, cream honey gold color palette, children, kids, magical floating elements, text, handwriting"

ACCENT_COLORS = [
    "a terracotta orange enamel kettle",
    "a terracotta orange woven scarf",
    "a rust orange backpack"
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
    "framed by an aged stone archway",
    "seen across a narrow cobblestone alley",
    "over-the-shoulder angle"
]

BASE_SCENES = [
    "An elderly village artisan inside a rustic stone workshop, looking at the warm amber fire crackling in a rough stone hearth",
    "Deep warm amber lantern light casting shadows against the weathered stone walls of the workshop",
    "A worn tweed coat resting peacefully on a rough wooden chair",
    "The elderly artisan stepping out of his stone cottage onto a cool overcast cobblestone street",
    "The artisan holding out his smooth matte clay hand with long expressive fingers",
    "A small felted wool sheep with dense curly cream-white wool walking faithfully at his feet",
    "The artisan standing peacefully on uneven stone steps, his chunky knit sweater absorbing the cool Mediterranean daylight",
    "The aged Mediterranean village stretching out with peeling teal-blue wooden doors and narrow atmospheric alleys",
    "A stray cat watching from a stone wall as the artisan walks past a weathered doorway",
    "The artisan gently touching the rough stone wall with his visibly aged clay hands"
]

prompts = []
for i in range(10):
    base_scene = BASE_SCENES[i]
    shot = SHOT_SIZES[i % len(SHOT_SIZES)]
    angle = ANGLES[i % len(ANGLES)]
    accent = ACCENT_COLORS[i % len(ACCENT_COLORS)]
    
    if i % 5 == 0:
        detail = f"cool daylight shaft through a small stone window, {accent} resting nearby"
    elif i % 5 == 1:
        detail = f"warm amber lantern glowing against cool blue dusk, {accent} in the background"
    elif i % 5 == 2:
        detail = f"steam rising slowly from a mismatched ceramic cup, {accent} placed thoughtfully"
    elif i % 5 == 3:
        detail = f"aged hands slowly turning the dial of a vintage wooden radio, {accent} draped nearby"
    else:
        detail = f"smooth clay fingers wrapped carefully around a walking stick, {accent} nearby"
        
    full_prompt = f"{base_scene}, {detail}, {shot}, {angle}, {BASE_STYLE} {NEGATIVE_BLOCK}"
    prompts.append(full_prompt)

with open(OUTPUT_FILE, "w") as f:
    for p in prompts:
        f.write(f"{p}\n\n")

print(f"Successfully generated {len(prompts)} test prompts in {OUTPUT_FILE}")
