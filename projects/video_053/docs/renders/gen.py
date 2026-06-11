import os
import random

target_file = "/Users/hoangkien/Youtube/coslient-video/projects/video_053/docs/renders/v7_part5.txt"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

shot_angles = [
    "Medium Shot, Eye Level", "Close-up, Low Angle", "Extreme Close-up, High Angle", 
    "Medium Wide Shot, Dutch Angle", "Over-the-Shoulder Shot, Eye Level",
    "Close-up, Dynamic Angle", "Medium Shot, Slight Low Angle", "Wide Shot, Low Angle"
]

locations = [
    "same small lived-in sitting room interior as established in asset bible",
    "same small quiet countryside cemetery exterior as established in asset bible",
    "rustic wooden porch overlooking an autumn meadow",
    "worn dirt road winding through bare trees"
]

character = "elderly man, approximately 72 years old, lean and weathered build with slightly stooped shoulders from decades of physical labor, wearing a simple flannel shirt with rolled-up sleeves and worn dark trousers, calm and dignified expression with a quiet sadness in his kind eyes, thick-fingered working hands with visible calluses, soft gray needle-felted wool hair, consistent character design"

prop = "small acoustic guitar, warm honey-brown spruce top with aged matte finish, steel strings slightly oxidized"
style = "handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted textures, Laika Studios claymation aesthetic, storybook illustration style"
color_tones = ["aged honey-amber", "dusty warm cream", "pale autumn gold", "muted morning mist", "soft iron-gray"]
negative = "16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting"

fc_actions = [
    "strumming the strings with intense cathartic energy",
    "singing powerfully with head tilted towards the light",
    "clutching the instrument tightly against his chest",
    "striking a resonant chord with fingers pressing hard",
    "standing tall while playing a sweeping melody",
    "closing eyes in profound emotional release",
    "gazing intensely forward while hands blur over the strings",
    "breathing deeply as a final triumphant note rings out",
    "leaning into the music with visible passion",
    "sweeping his calloused thumb across the steel strings",
    "looking up at a beam of light with a hopeful smile",
    "tapping the wooden body in a strong rhythmic beat",
    "holding a sustained chord while the world seems to pause",
    "pressing forehead to the wood in an overwhelming wave of memory",
    "plucking the strings with newfound strength and resolve"
]

fc_layers = [
    "falling golden autumn leaves in foreground -> character immersed in musical catharsis in mid-ground -> heavily textured stone wall with deep contrasting shadows in background",
    "intense beams of afternoon sun cutting through dust in foreground -> character striking guitar with passion in mid-ground -> shelves of blurred weathered books and trinkets in background",
    "swirling mist and soft glowing lamplight in foreground -> character standing firm with guitar in mid-ground -> silhouetted bare trees against a fading sky in background",
    "out-of-focus wooden porch railing in foreground -> character playing with profound emotion in mid-ground -> rolling hills bathed in amber light in background",
    "scattered sheet music catching the light in foreground -> character deeply focused on his performance in mid-ground -> warm glowing fireplace with dancing flames in background",
    "thick morning fog drifting slowly in foreground -> character looking up with musical intensity in mid-ground -> faded wooden cabin walls in background",
    "out-of-focus guitar neck in foreground -> character's expressive face caught in a moment of release in mid-ground -> softly lit sitting room corner in background",
    "warm glowing embers floating upward in foreground -> character holding a final powerful chord in mid-ground -> deep shadowy room interior with textured clay walls in background"
]

outro_actions = [
    "slowly lowering his hands from the instrument",
    "gazing softly into the distance in quiet contemplation",
    "resting his hands gently on his knees",
    "looking down at the worn wooden floor",
    "sitting perfectly still as the final note fades",
    "gently placing the instrument beside him",
    "taking a slow calming breath",
    "watching the dust motes settle in the quiet room"
]

outro_layers = [
    "empty space with a single dust mote in foreground -> character sitting quietly in mid-ground -> soft muted wall texture in background",
    "faint ray of cool light in foreground -> character resting in stillness in mid-ground -> blurred empty chair in background",
    "soft shadow stretching across the floor in foreground -> character looking peaceful in mid-ground -> plain wooden door in background",
    "barely visible window frame in foreground -> character exhaling slowly in mid-ground -> pale gray sky through the glass in background"
]

prompts = []

for i in range(50):
    loc = locations[i % len(locations)]
    action = fc_actions[i % len(fc_actions)]
    layer = fc_layers[i % len(fc_layers)]
    shot = shot_angles[i % len(shot_angles)]
    color = color_tones[i % len(color_tones)]
    
    prompt = f"{shot}, {loc}, {character}, {action}, {layer}, {prop}, {style}, {color}, {negative}"
    prompts.append(prompt)

for i in range(8):
    loc = locations[i % len(locations)]
    action = outro_actions[i % len(outro_actions)]
    layer = outro_layers[i % len(outro_layers)]
    shot = "Medium Shot, Eye Level" if i % 2 == 0 else "Wide Shot, Low Angle"
    color = color_tones[i % len(color_tones)]
    
    prompt = f"{shot}, {loc}, {character}, {action}, {layer}, {prop}, {style}, {color}, {negative}"
    prompts.append(prompt)

prompts.append(f"Extreme Wide Shot, High Angle, same small lived-in sitting room interior as established in asset bible, no character present, empty space waiting in absolute quiet, bare wooden floor in foreground -> empty armchair catching soft light in mid-ground -> dimly lit corner in background, no props present, {style}, muted morning mist, {negative}")

prompts.append(f"Extreme Wide Shot, Static Angle, same small lived-in sitting room interior as established in asset bible, no character present, dust settling slowly in the silent room, faint cool light on the floorboards in foreground -> empty center space in mid-ground -> window frame looking out to gray skies in background, no props present, {style}, soft iron-gray, {negative}")

output = "\n\n".join(prompts)
with open(target_file, "w") as f:
    f.write(output)

print(f"Generated {len(prompts)} prompts and saved to {target_file}")
