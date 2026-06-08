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

b1_actions = [
    ("A tired middle-aged city man parking his dusty car near the cliff edge", "wide shot, foreground car, background ocean", "slanted morning sunlight casting long warm shadows across the car hood"),
    ("The city man opening his car door in the cold dawn", "medium shot through the car window", "the soft glow of the dashboard illuminating his exhausted face"),
    ("Heavy boots stepping out onto the wet sand", "close up on the boots", "the exact moment the boot presses into the damp, cold sand"),
    ("The man standing by the car, looking out at the vast ocean", "medium wide shot from behind", "the gentle sea breeze rustling the edges of his heavy coat"),
    ("The man slowly taking off his heavy winter coat", "medium shot", "his shoulders dropping slightly as the weight comes off"),
    ("Dropping his heavy travel bag onto the sand", "low angle shot", "the soft thud of the bag displacing a small ridge of sand"),
    ("Sitting on a piece of driftwood, unlacing his boots", "medium close up", "his hands moving slowly, tired but deliberate"),
    ("Stepping onto the wet sand barefoot for the first time", "close up on the bare feet", "the contrast of his smooth skin against the textured sand"),
    ("Cold sea water gently touching his toes", "extreme close up", "the thin, silvery layer of water washing over the sand"),
    ("The man looking down at the water swirling around his feet", "high angle shot", "the reflection of the dawn sky in the shallow water"),
    ("Taking a deep, visible breath of the cold morning air", "medium close up on his face", "a faint puff of steam escaping his lips"),
    ("Looking up at the sky as the indigo begins to fade", "low angle shot on his face", "the first hints of warm amber light catching his eyes"),
    ("Wading ankle-deep into the calm surf", "medium wide shot", "the gentle ripples spreading out from his legs"),
    ("His heavy coat draped over the car hood in the background", "wide shot, foreground coat, background man", "the textures of the coat catching the early light"),
    ("Standing with hands in his pockets, shivering slightly", "medium shot", "his posture curled inward against the morning chill"),
    ("Holding a thermos with both hands to get warm", "close up on his hands", "steam rising slowly from the open thermos lid"),
    ("Closing his eyes against the salty wind", "close up on his face", "his expression shifting from tense to a soft release"),
    ("A trail of footprints starting at the car and leading to the water", "wide shot", "the deep impressions in the sand filled with shadows"),
    ("Dropping his shoulders, completely relaxing his posture", "medium shot", "the physical weight of the city visibly leaving his body"),
    ("Walking slowly further down the shoreline", "wide shot tracking", "his figure becoming a small silhouette against the vast ocean")
]

b2_actions = [
    ("An elderly fisherman arranging smooth stones to build a small fire", "close up on his hands", "his weathered fingers placing each stone with quiet precision"),
    ("Lighting the small beach fire", "medium close up", "the first spark catching the dry kindling, casting a warm glow"),
    ("Warming his hands over the crackling flames", "medium shot", "the amber firelight dancing across his calm, gracefully aging face"),
    ("Pulling out a damaged fishing net from a wooden crate", "medium wide shot", "the intricate, tangled knots of the net catching the firelight"),
    ("Threading a wooden needle to repair the net", "extreme close up", "the steady, practiced movement of the thick thread passing through"),
    ("Tying a strong, secure knot in the net", "close up on his hands", "the tension in the rope as the knot is pulled tight"),
    ("Looking up from his work toward the gentle waves", "medium shot", "the reflection of the ocean in his kind, peaceful eyes"),
    ("Sipping hot tea from a battered tin cup", "close up", "steam rising softly from the cup into the cold morning air"),
    ("Patting the side of his weathered wooden boat", "medium wide shot", "his hand resting affectionately on the smooth, worn wood"),
    ("Organizing colorful wooden floats along the sand", "high angle shot", "the neat arrangement of the floats beside the chaotic net"),
    ("Smoothing the repaired net out across his knees", "medium close up", "the soft, rhythmic motion of his hands checking the work"),
    ("The small fire crackling merrily beside him", "low angle shot", "the bright flames standing out against the indigo dawn sky"),
    ("His face beautifully illuminated by the firelight", "close up", "the warm glow highlighting his gentle features and soft hair"),
    ("His hands working with practiced, effortless ease", "medium shot", "a sense of total mastery and peace in his repetitive actions"),
    ("Placing a smooth piece of dry driftwood onto the fire", "close up", "the wood catching flame, sending up a tiny shower of sparks"),
    ("His wooden boat resting quietly on the sand behind him", "wide shot, foreground fisherman, background boat", "the boat acting as a sturdy, silent companion"),
    ("Tying the final, perfect knot on the fishing net", "close up on the knot", "the satisfaction of a job well done visible in the tight weave"),
    ("Folding the repaired net carefully into a neat pile", "medium shot", "the methodical, rhythmic folding motion"),
    ("Looking down the vast, empty beach", "medium wide shot", "his calm gaze scanning the horizon with deep familiarity"),
    ("Resting his hands on his knees, taking a break", "medium shot", "a moment of total stillness, his breath steady and calm")
]

b3_actions = [
    ("A vast view of the beach, the city man far away in the shallows, the fisherman by his fire", "extreme wide establishing shot", "the sweeping curve of the shoreline connecting the two tiny figures"),
    ("View from the water, showing both men in the distance", "low angle wide shot", "the gentle waves in the foreground leading the eye to the men"),
    ("The rhythmic waves breaking on the shore, both men visible in the background", "deep focus wide shot", "the water creating a visual bridge between their two separate worlds"),
    ("The fisherman's perspective, looking down the beach at the city man", "over the shoulder wide shot", "the fisherman's calm observation of the stranger"),
    ("The city man's perspective, noticing the distant glow of the fisherman's fire", "over the shoulder wide shot", "the warm amber dot of the fire against the cool indigo morning"),
    ("The vast empty space of sand between the two men", "wide shot, framing the space", "the peaceful emptiness that allows both men to be alone together"),
    ("A single seagull gliding smoothly between their two positions", "wide shot tracking the bird", "the bird's flight path drawing an invisible line between them"),
    ("The morning sun cresting the horizon exactly between their distant figures", "wide shot against the sunrise", "the brilliant burst of amber light uniting the composition"),
    ("Both men looking out at the exact same breaking wave", "split focus wide shot", "a shared moment of observation without any communication"),
    ("The gentle curve of the wet sand reflecting both their distant silhouettes", "low angle wide shot", "the mirror-like surface of the wet sand doubling the scene"),
    ("A trail of footprints leading halfway toward the fisherman's camp", "medium wide shot", "the footprints representing a silent, unfulfilled connection"),
    ("The city man pausing, his attention caught by the distant fire", "medium shot on the city man, deep background fire", "the subtle turn of his head toward the warmth"),
    ("The fisherman pausing his work, noticing the man in the water", "medium shot on fisherman, deep background city man", "his hands resting on the net as he watches peacefully"),
    ("Both men turning their gaze back to the endless sea at the same time", "wide shot", "a synchronized movement driven entirely by the ocean's rhythm"),
    ("The sky taking up most of the frame, the men as tiny details on the edge", "extreme wide shot, sky dominant", "the overwhelming scale of nature dwarfing their human concerns"),
    ("The visual contrast of the modern car and the ancient wooden boat", "wide shot capturing both objects", "the metallic sheen of the car versus the worn matte wood of the boat"),
    ("The contrast of the man's heavy city clothes and the fisherman's simple sweater", "split-screen style wide shot", "the different armors they wear against the cold"),
    ("A beautiful piece of sea-smoothed driftwood lying exactly between them", "low angle deep focus shot", "the driftwood acting as a silent centerpiece of the vast beach"),
    ("The waves gently washing the sand in the space between them", "medium wide shot on the water", "the water constantly erasing any lines between their territories"),
    ("The rich amber sunlight finally hitting both their faces simultaneously", "wide shot", "the warmth of the sun physically connecting their isolated moments")
]

b4_actions = [
    ("The ocean tide gently washing over the footprints left by the city man", "close up on the sand", "the water filling the deep impressions and smoothing them away"),
    ("The city man's face, now completely peaceful and relaxed", "close up", "the harsh lines of exhaustion replaced by a soft, quiet hope"),
    ("The fisherman's face, content and satisfied with his morning's work", "close up", "a faint, gentle smile playing at the corners of his mouth"),
    ("The sun fully rising above the horizon, flooding the scene", "wide establishing shot", "the entire beach bathed in a brilliant, luminous honey-gold light"),
    ("The rolling waves catching the sunlight and turning golden", "medium shot on the water", "the sparkling, radiant highlights on the crest of each wave"),
    ("The city man slowly putting his heavy boots back on", "medium close up", "his movements are no longer heavy, but light and purposeful"),
    ("The city man walking back to his car, his posture noticeably lighter", "medium wide shot from behind", "his silhouette moving smoothly, free from the invisible burden"),
    ("The fisherman carefully putting out his small beach fire with sand", "close up on his hands", "the gentle, respectful way he covers the embers"),
    ("The fisherman standing up slowly, stretching his back", "medium shot", "his silhouette against the bright morning sky, rooted and strong"),
    ("The empty stretch of wet sand where the city man had stood", "medium wide shot", "the perfect, pristine smoothness of the untouched sand"),
    ("The dusty car driving away slowly in the distance", "wide shot", "the car disappearing into the warm, hazy morning atmosphere"),
    ("The fisherman packing his repaired net into his wooden boat", "medium shot", "the neat, orderly arrangement of his simple tools"),
    ("A macro close up of the perfectly smooth, washed sand reflecting the sky", "extreme close up", "the microscopic grains of sand sparkling in the amber light"),
    ("The fisherman walking slowly towards his boat, ready for the day", "wide shot", "his figure perfectly at home in the vast landscape"),
    ("The city man's hand resting gently on his steering wheel", "close up inside the car", "his grip is relaxed, no longer tense or white-knuckled"),
    ("The fisherman's hand resting on the side of his boat", "close up", "the deep connection between the man and his worn wooden vessel"),
    ("The ocean waves continuing their gentle, rhythmic lapping", "medium shot on the surf", "the endless, indifferent, healing heartbeat of the sea"),
    ("The bright sun reflecting brilliantly on the thin film of water on the sand", "low angle shot", "a blindingly beautiful glow that signifies a clean slate"),
    ("The quiet, empty morning beach, peaceful and still", "wide establishing shot", "the landscape completely undisturbed, as if no one was ever there"),
    ("A final wide shot of the vast ocean holding the morning light", "extreme wide shot", "the majestic, unjudging ocean, perfectly calm and glowing")
]

beats = [b1_actions, b2_actions, b3_actions, b4_actions]
prompts = []

prompt_idx = 0
for b_idx, beat_actions in enumerate(beats):
    beat_num = b_idx + 1
    prompts.append(f"### Beat {beat_num} Prompts")
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
            if "city man" in action_text.lower():
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

print("Generated 80 prompts successfully.")
