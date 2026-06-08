import os

filepath = "/Users/hoangkien/Youtube/coslient-video/projects/video_051/docs/04_image_prompts.txt"
os.makedirs(os.path.dirname(filepath), exist_ok=True)

accents = [
    "a muted sage-green",
    "a faded cornflower-blue",
    "a pale dusty-rose"
]

objects = [
    "thermos", "scarf", "travel bag", "ceramic mug", "cloth napkin", "jacket lining",
    "blanket", "fishing float", "tin cup", "rope", "towel", "boat flag"
]

locked_color = "cold indigo coastal dawn, muted sea-glass greys, rich warm amber morning light, lifted soft shadows, cinematic hazy atmosphere"
hdr_keywords = "rich tonal depth with luminous highlights and warm shadow detail, pseudo-HDR warm palette"
style_anchor_man = "soft handcrafted storybook miniature, warm gentle loving atmosphere, smooth hand-painted claymation character, handsome and tired middle-aged face, clean smooth features, kind exhausted eyes, soft wool-like hair with separated curls, subtle heavy coat fabric detail, smooth matte porcelain-clay skin"
style_anchor_fisher = "soft handcrafted storybook miniature, warm gentle loving atmosphere, smooth hand-painted claymation character, handsome and gracefully aging elderly face, clean smooth features with minimal soft laugh lines, no deep-cut wrinkles, kind eyes, soft wool-like hair with separated curls, subtle thick knitted sweater fabric detail, smooth matte porcelain-clay skin"
style_anchor_generic = "soft handcrafted storybook miniature, warm gentle loving atmosphere, smooth hand-painted claymation character, smooth matte porcelain-clay skin"
negatives = "no text no handwriting no magical elements, avoid oversaturated accent colors, avoid large areas of non-warm color, avoid waxy face, muddy skin, fused hair and skin, creepy puppet face, plastic shine, no children no kids, pitch-black darkness, avoid heavy texture"

b1_actions_new = [
    ("The city man sitting inside his parked car, staring blankly ahead", "medium shot through the windshield", "the dashboard lights casting a faint blue glow on his tired eyes"),
    ("Adjusting the rearview mirror slowly", "close up on the mirror", "his eyes looking heavy and worn out in the reflection"),
    ("Rolling down the car window to let the cold air in", "medium close up", "the sharp sea wind instantly blowing through his neatly styled hair"),
    ("Unbuttoning the stiff collar of his dress shirt", "close up on his neck", "his fingers clumsily pulling the tight fabric away"),
    ("Finding an crumpled coffee receipt in his coat pocket", "extreme close up on his hand", "the white paper contrasting with the dark heavy coat fabric"),
    ("Leaning against the side of the car, head tilted back toward the sky", "medium shot", "his eyes closed against the cool morning mist"),
    ("Wiping a thin layer of condensation off the side mirror", "close up", "the squeaky streak revealing the dark ocean behind him"),
    ("Watching a small sand crab scuttle over the toe of his boot", "low angle shot", "the fragile crab dwarfed by the heavy leather footwear"),
    ("Bending down to pick up a smooth piece of sea glass", "medium close up", "his pale fingers tracing the frosted edges of the glass"),
    ("Tossing a small pebble lazily into the shallow surf", "wide shot from behind", "the tiny splash disturbing the glassy surface of the water"),
    ("Rolling up the cuffs of his expensive trousers", "close up on his legs", "the fine fabric dragging slightly in the wet sand"),
    ("Splashing freezing seawater onto his face", "medium shot", "water droplets flying off his cheeks, instantly waking him up"),
    ("Drying his face with the rough sleeve of his heavy coat", "close up on his face", "the thick wool absorbing the moisture, his skin looking refreshed"),
    ("Letting out a long, shuddering sigh of relief", "medium close up", "a massive cloud of steam escaping his mouth in the cold air"),
    ("Closing the car trunk with a soft, definitive click", "medium wide shot", "the metallic sound echoing slightly across the empty beach"),
    ("Unlocking his smartphone, hesitating, then turning the power off completely", "close up on his hands", "the black screen reflecting his own tired face"),
    ("Staring down at his own faint reflection in a shallow tide pool", "high angle shot", "the water slightly distorting his sharp, tense features"),
    ("Feeling the rough texture of a barnacle-covered rock", "extreme close up", "his smooth skin contrasting against the sharp, jagged shells"),
    ("Kicking up a small, playful spray of water with his bare foot", "low angle close up", "the droplets catching the early morning light like tiny diamonds"),
    ("Standing perfectly motionless, letting the wind mess up his hair", "medium shot", "the formal grooming of the city completely undone by the ocean breeze")
]

b2_actions_new = [
    ("The elderly fisherman untangling a fishing line with incredible patience", "close up on his hands", "the thin transparent line weaving through his thick, calloused fingers"),
    ("Sharpening a small pocket knife on a smooth, flat whetstone", "medium close up", "the rhythmic, scraping motion creating tiny metal flakes"),
    ("Carving a tiny identification notch into a wooden float", "extreme close up", "the sharp blade lifting a neat curl of dry wood"),
    ("Wiping sea salt and mist from his forehead", "close up on his face", "the rough back of his hand rubbing against his gracefully aging skin"),
    ("Checking the distant sky for weather signs", "medium shot", "his kind eyes squinting slightly beneath his wool-like hair"),
    ("Adjusting a thick woolen scarf tighter around his neck", "medium close up", "the bulky fabric providing extra warmth against the coastal chill"),
    ("Pouring the very last dark drops of tea from his thermos", "close up on the cup", "a solitary drop hanging on the lip of the thermos"),
    ("Watching a hermit crab hide under a piece of wet seaweed", "low angle shot", "the fisherman's massive boot next to the tiny, fragile creature"),
    ("Patching a small, frayed hole in his heavy canvas bag", "medium close up", "a thick iron needle pushing forcefully through the tough fabric"),
    ("Running his hand affectionately over the worn gunwale of his wooden boat", "medium wide shot", "the wood deeply scarred and weathered from years at sea"),
    ("Tying down a loose tarpaulin over his fishing gear", "close up on the knot", "the heavy canvas snapping sharply in the sea breeze"),
    ("Arranging his freshly caught fish in an old wooden cooler", "high angle shot", "the silver scales of the fish shimmering in the dim dawn light"),
    ("Lighting an old, tarnished brass storm lantern", "medium close up", "the small yellow flame illuminating the intricate metalwork"),
    ("Cleaning his dirty hands with a rough, damp cloth", "close up on his hands", "the fabric scrubbing away the dark mud and fish scales"),
    ("Stretching his aching shoulders with a slow, deliberate movement", "medium wide shot", "his thick sweater shifting as his muscles stretch"),
    ("Humming a quiet tune to himself", "close up on his face", "his lips barely moving, a look of profound contentment in his eyes"),
    ("Examining a rusted iron hook before tossing it away", "extreme close up", "the orange rust contrasting with his pale, matte porcelain-clay skin"),
    ("Tossing a scrap of leftover bait to a lingering seagull", "medium wide shot", "the bird catching the morsel mid-air in the hazy atmosphere"),
    ("Tucking his hands deep into his thick sweater pockets to keep warm", "medium shot", "his shoulders hunched slightly against a sudden gust of wind"),
    ("Sitting quietly on an overturned wooden crate, watching the horizon", "wide shot", "a monument of stillness amidst the moving waves")
]

b3_actions_new = [
    ("The city man picking up a seashell while the fisherman works far away", "deep focus wide shot", "the foreground hand holding the shell, the background figure a tiny blur"),
    ("The physical distance between the two men feeling strangely intimate", "extreme wide establishing shot", "the vast sandy expanse linking them rather than separating them"),
    ("The city man's long morning shadow stretching almost all the way to the boat", "high angle wide shot", "the dark silhouette on the sand acting like a bridge"),
    ("A massive wave crashing exactly at the midpoint between the two men", "wide shot", "the dramatic spray of white water separating their two silent worlds"),
    ("Both men turning their heads simultaneously to watch a distant ship", "split-screen style wide shot", "their identical posture revealing an unspoken connection"),
    ("The thin wisp of smoke from the fire drifting across to the city man", "medium wide shot", "the hazy smoke interacting with the lifted soft shadows of the beach"),
    ("A jagged line of washed-up seaweed tracing a path between them", "low angle wide shot", "the dark green kelp leading the eye from the car to the boat"),
    ("The city man taking one slow, hesitant step toward the warmth of the fire", "medium shot", "his foot sinking into the sand as he pauses, unsure"),
    ("The fisherman nodding slightly to himself, sensing the stranger's presence", "close up on his face", "a wise, unseen acknowledgment of the man's silent burden"),
    ("The glowing golden hour light casting identical bright halos on both their heads", "wide shot", "the light treating both the exhausted man and the peaceful fisherman equally"),
    ("The reflection of the rising sun in the wet sand perfectly bridging the gap", "low angle wide shot", "a dazzling pathway of amber light connecting their positions"),
    ("Both men taking a deep, slow breath in perfect unison with the ocean swell", "split focus wide shot", "the subtle rise and fall of their chests matching the tide"),
    ("The city man's expensive coat lying on the sand near the fisherman's discarded net", "close up on the ground", "the contrast of luxurious wool and utilitarian rope"),
    ("The profound, quiet understanding filling the vast open space of the beach", "extreme wide shot", "the atmosphere heavy with peace rather than isolation"),
    ("A pair of white seabirds flying in perfect parallel formation overhead", "low angle wide shot tracking the birds", "the birds mirroring the two men on the ground below"),
    ("The incoming tide slowly creeping up, almost touching both their boots", "high angle wide shot", "the water acting as a great equalizer, claiming the beach"),
    ("The stark contrast between the man's smooth hands and the fisherman's calloused fingers", "split-screen close up", "the different lifetimes written into their skin"),
    ("The man holding his silver thermos, the fisherman holding his battered tin cup", "medium wide shot", "both taking a sip of warmth at the exact same moment"),
    ("The soundless wind carrying an unspoken sense of deep human kinship", "wide shot", "the grass on the dunes bending towards the two figures"),
    ("Both men closing their eyes simultaneously, absorbing the morning sun", "close up, split focus", "the identical expression of pure, unadulterated relief")
]

b4_actions_new = [
    ("The city man returning to his car, a small, genuine smile on his lips", "medium shot", "the heavy exhaustion completely replaced by a light, hopeful energy"),
    ("The fisherman stepping into the cold water to push his small boat out", "medium wide shot", "the effortless strength of his movements as the boat slides off the sand"),
    ("The man opening his car door, feeling entirely complete and rested", "close up on his face", "his eyes clear and bright, reflecting the morning sky"),
    ("The fisherman climbing nimbly over the side of his wooden boat", "medium shot", "his body moving with practiced, rhythmic grace"),
    ("The car engine starting up with a gentle, smooth hum", "low angle shot near the exhaust", "a small puff of exhaust dissipating quickly into the fresh air"),
    ("The boat's wooden oars slicing cleanly into the glowing, golden water", "close up on the oars", "the water fracturing into a million bright amber shards"),
    ("The man turning up the heat dial inside his comfortable car", "extreme close up on the dashboard", "his fingers moving quickly, eager for the drive home"),
    ("The fisherman gracefully casting his first fishing line of the day", "wide shot", "the thin line forming a perfect, elegant arc against the sky"),
    ("The dusty car turning around slowly on the sandy coastal road", "wide shot from above", "the tires kicking up a small cloud of golden dust"),
    ("The small wooden boat gliding silently away from the safe shore", "wide shot", "the boat becoming a tiny silhouette against the vast ocean"),
    ("The man taking one last appreciative look at the sea in his rearview mirror", "close up on the mirror", "the glowing horizon perfectly framed in the small rectangle"),
    ("The fisherman looking back at the beautifully empty stretch of beach", "over the shoulder shot", "the pristine sand holding nothing but a few scattered footprints"),
    ("The tire tracks of the car fading softly as the wind blows dry sand over them", "close up on the ground", "nature quickly reclaiming the brief mark of human presence"),
    ("The gentle wake of the boat slowly dispersing into calm, rhythmic ripples", "high angle shot on the water", "the V-shape widening until it disappears completely"),
    ("The empty parking spot near the cliff edge, looking peaceful and profoundly still", "wide establishing shot", "the landscape exactly as it was before the man arrived"),
    ("The remaining dark embers of the small fire slowly dying out on the sand", "close up on the fire pit", "a tiny, final wisp of smoke rising lazily into the air"),
    ("The morning sun casting pure, brilliant light over the entire coastal landscape", "extreme wide shot", "the shadows completely gone, replaced by vibrant, luminous clarity"),
    ("A single, pristine white seagull feather resting on the sand where the man stood", "extreme close up", "the delicate fibers of the feather blowing slightly in the breeze"),
    ("A small wave gently washing away the very last footprint on the shore", "medium close up on the water", "the sand left completely smooth, a perfect clean slate"),
    ("A magnificent final view of the ocean, indifferent, beautiful, and healing", "extreme wide establishing shot", "the endless horizon radiating a deep, eternal warmth")
]

beats = [b1_actions_new, b2_actions_new, b3_actions_new, b4_actions_new]
prompts = []

# Appending with a header to distinguish Part 2 if wanted, or just continue
prompts.append("\n### PART 2 PROMPTS (81-160) ###\n")

prompt_idx = 0
for b_idx, beat_actions in enumerate(beats):
    beat_num = b_idx + 1
    prompts.append(f"### Beat {beat_num} Prompts (Part 2)")
    for action_tuple in beat_actions:
        action_text, shot_text, detail_text = action_tuple
        accent = f"{accents[prompt_idx % 3]} {objects[prompt_idx % len(objects)]}"
        
        # Decide char anchor
        if beat_num == 1:
            char_anchor = style_anchor_man
        elif beat_num == 2:
            char_anchor = style_anchor_fisher
        elif beat_num == 3:
            char_anchor = style_anchor_generic
        elif beat_num == 4:
            if "city man" in action_text.lower() or "man" in action_text.lower():
                char_anchor = style_anchor_man
            elif "fisherman" in action_text.lower():
                char_anchor = style_anchor_fisher
            else:
                char_anchor = style_anchor_generic
                
        # Base Emotion
        if beat_num == 1: emotion = "quiet release, exhaustion turning to peace"
        elif beat_num == 2: emotion = "steady, grounded, peaceful acceptance"
        elif beat_num == 3: emotion = "a sense of shared human connection without words, vast peacefulness"
        elif beat_num == 4: emotion = "complete cleansing, quiet hope, a fresh start"

        prompt = f"{action_text}, {shot_text}, {detail_text}, with {accent} visible, {char_anchor}, {locked_color}, {hdr_keywords}, {emotion}, 16:9, {negatives}"
        prompts.append(prompt)
        prompts.append("") # blank line
        prompt_idx += 1

with open(filepath, "a") as f:
    for p in prompts:
        f.write(p + "\n")

print("Generated 80 new prompts successfully.")
