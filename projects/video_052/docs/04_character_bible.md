# Character Bible — video_052: The Ocean Keepers (the rusted hand)

> **Stage:** 4.1.5 — Character & Asset Reference Design
> **Dự án:** video_052
> **Storyboard:** 48 shots / 4:00 / 4 locations

---

## Story Type Check

```
STORY TYPE:        [B] Single Character Journey
CHARACTER COUNT:   1 (ông lão thợ lặn)
TOTAL SHOTS:       48 shots
LOCATION COUNT:    4 locations (Glass Dome → Seagrass → Sandy Seabed → Deep Abyss → Glass Dome)
CHARACTER VISIBILITY: ~50% shots có nhân vật (23 STORY + đầu tay trong 13 DETAIL)
HAND/GESTURE MOTIF: [YES] ← bàn tay đồng là visual motif trung tâm → O3 BẮT BUỘC
STYLE:             Nostalgic Diorama (nostalgic_diorama)
PLATFORM:          Midjourney v6.0
```

---

## Asset Generation Order (Trạng thái hiện tại)

```
Bước 2a → [STYLE TEST]    3 prompts test style             → STATUS: PENDING
Bước 2b → [C3]            Character Fully Costumed         → STATUS: PENDING ← CRITICAL
Bước 2c → [O3]            Brass Hand Detail Sheet          → STATUS: PENDING
Bước 2d → [E1-E4]         4 establishing shots             → STATUS: PENDING
Bước 2e → [Props]         P2, P5, P7                       → STATUS: PENDING
Bước 2f → [Compile]       Frozen Block + Env Packs         → STATUS: PENDING
```

---

## Tier 1 — CHARACTER ASSETS

### C1: Character Face Sheet

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]

NHÂN VẬT: Ông lão — elderly male, deeply weathered face, tired but kind eyes,
           sunken cheeks, visible age lines, gentle and melancholic expression.
           Proportions: exaggerated spindly claymation style.

PROMPT:
character design sheet, multiple angles, front view + 3/4 view left + side profile + 3/4 view right,
kind elderly man with deeply weathered claymation face, tired but gentle warm eyes, sunken cheeks,
soft natural age lines, melancholic yet peaceful expression, naturally soft thin white hair,
exaggerated spindly claymation proportions, warm soft matte clay puppet skin,
isolated on clean neutral off-white background,
nostalgic stop-motion animation style, miniature diorama, macro photography,
extremely tactile hand-crafted textures, Laika studios claymation aesthetic,
character reference sheet layout, no background clutter,
16:9 --stylize 250 --v 6.0
```

---

### C2: Character Full Body (Bare — trong nhà, không mặc đồ lặn)

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]

DÙNG CHO: SB_047 (ngồi ghế bành trong nhà, đã tháo đồ lặn)

PROMPT:
full body character design sheet, front and back view,
kind elderly man with exaggerated spindly claymation proportions, deeply weathered face, gentle tired eyes,
wearing chunky knit wool sweater in muted navy blue, loose worn canvas trousers,
naturally soft thin white hair, warm soft matte clay puppet skin, long gentle expressive hands,
isolated on clean neutral background,
nostalgic stop-motion animation style, miniature diorama, Laika studios claymation aesthetic,
extremely tactile hand-crafted textures, earthy muted color palette,
16:9 --stylize 250 --v 6.0
```

---

### C3: Character Fully Costumed ⭐ CRITICAL

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate — đây là --cref cho 90% shots]

ĐÂY LÀ ASSET QUAN TRỌNG NHẤT. Phải generate trước tất cả shots.
Dùng: --cref [URL] --cw 100 cho mọi STORY shot có nhân vật mặc đồ lặn đầy đủ.

COSTUME LAYER-BY-LAYER SPEC:
- Outer shell: vintage brass diving suit, fully enclosing body
- Helmet: large round brass sphere, single circular porthole glass (foggy/slightly tinted),
          riveted construction, visible bolts around porthole rim
- Body suit: heavy brass plates, articulated at joints (shoulders, elbows, knees, hips),
             visible segmented construction, bulky and rigid-looking
- Gloves: articulated brass fingers, visible joint mechanisms at each knuckle
- Boots: thick flat-soled brass boots, heavily weighted appearance
- Color: dark amber-orange brass (#8B6914 equivalent) with teal-green oxidation
         (verdigris) concentrated at all joints, edges, and seams
- Aging: deep rust textures, scratches, dents, patina — NOT shiny, NOT new

PROPORTIONS: Spindly claymation body (thin limbs, slightly oversized helmet relative to body)
SILHOUETTE: Unmistakable — round helmet on thin body = instantly recognizable

PROMPT:
full body character design sheet, front view + 3/4 view + side view + back view,
kind elderly man completely enclosed in a heavy vintage brass diving suit,
large round brass sphere helmet with single circular foggy porthole glass window, riveted brass construction with visible bolts,
full body brass diving suit with segmented articulated plates at shoulders elbows hips knees,
articulated brass gloved fingers with visible joint mechanisms, thick flat-soled brass weighted boots,
dark amber-orange brass color with teal-green verdigris oxidation concentrated at joints and seams,
deeply rusted and weathered surface texture, visible scratches dents and heavy patina,
exaggerated spindly claymation proportions — thin limbs inside bulky suit,
isolated on clean neutral off-white background,
nostalgic stop-motion animation style, miniature diorama, macro photography,
extremely tactile hand-crafted textures, weathered and aged surfaces,
Laika studios claymation aesthetic, earthy muted color palette,
highly detailed, no background, full body visible,
16:9 --stylize 250 --v 6.0
```

**After generate — điền đây:**
```
APPROVED C3 URL: [URL]
--cref usage: --cref [URL] --cw 100
```

---

### C4: Character Expression Sheet (qua kính mũ)

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]

LƯU Ý ĐẶC BIỆT: Ông lão luôn đội mũ lặn khi ở ngoài biển.
Expressions phải đọc được QUA lớp kính porthole mờ.

EXPRESSIONS (map theo emotional beats trong storyboard):
- Yên tĩnh / Peaceful: SB_001, SB_006 (routine, hòa mình)
- Nâng niu / Tender: SB_008, SB_022, SB_025 (cho cá ăn, nhặt chai)
- Tập trung / Focused: SB_021, SB_029, SB_033 (nhìn thấy nhiệm vụ)
- Lưu luyến / Wistful: SB_037 (dõi theo cá đuối bay đi)
- Hài lòng / Content: SB_044, SB_047 (sau khi gieo mầm, về nhà)

PROMPT:
expression sheet, 5 expressions side by side,
kind elderly man wearing heavy brass diving suit helmet with circular foggy porthole glass,
expressions visible through porthole: peaceful / tender / focused / wistful / content,
visible slight differences in eye crinkles and posture per expression,
isolated on neutral background,
nostalgic stop-motion animation style, miniature diorama, Laika studios claymation aesthetic,
extremely tactile textures, dark amber brass with verdigris, earthy muted colors,
16:9 --stylize 250 --v 6.0
```

---

### C5: Character Signature Pose Sheet

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]

POSES (map theo STORY shots):
- Pose A: Xòe bàn tay ra (SB_007, SB_040) — open palm extended
- Pose B: Cúi xuống nhặt (SB_021, SB_039) — bending forward, reaching down
- Pose C: Gật đầu / nods (SB_025) — slight helmet nod
- Pose D: Đứng thẳng, nhìn lên (SB_037, SB_044) — standing straight, looking up
- Pose E: Quỳ một gối (SB_039, SB_041) — kneeling on one knee

PROMPT:
action pose sheet, 5 poses side by side,
kind elderly man in complete heavy brass vintage diving suit,
poses: (1) standing with open palm extended outward (2) bent forward reaching one arm down (3) standing with slight head tilt nod (4) standing straight looking upward (5) kneeling on one knee with arm extended down,
full body visible for each pose, isolated on neutral background,
nostalgic stop-motion animation style, miniature diorama, Laika studios claymation aesthetic,
dark amber brass with verdigris oxidation, extremely tactile aged surfaces,
earthy muted color palette, 16:9 --stylize 250 --v 6.0
```

---

## Tier 2 — COSTUME / OUTFIT ASSETS

### O1: Diving Suit Turnaround (Đã có trong 04_test_prompts.txt)

```
STATUS: PROMPT READY — cần generate
GENERATED IMAGE URL: [điền sau khi generate]

[Prompt đã có trong 04_test_prompts.txt — Asset 01]
Tham khảo file đó để copy prompt.
```

---

### O2: Helmet / Porthole Detail Sheet

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]

DÙNG CHO: DETAIL shots về mũ, phản chiếu ánh sáng qua kính

HELMET KEY DETAILS:
- Shape: Large sphere, brass
- Porthole: Single large circular window, foggy/tinted glass, riveted brass ring around it
- Surface: Dark amber-orange brass, heavy verdigris at all edges
- Top ring: Large hex bolt fitting at crown
- Back: Hose fitting connection point (air hose — can be omitted for atmosphere)

PROMPT:
detailed prop sheet, vintage brass diving helmet, multiple views and details:
front view (porthole facing camera) + 3/4 view + side view + back view + close-up of porthole rivets,
large round brass sphere with single circular foggy porthole glass, riveted brass ring frame around porthole,
hex bolt air fitting at crown, dark amber-orange brass surface with heavy teal-green verdigris at edges and rivets,
deeply rusted and aged, visible scratches and dents,
isolated on neutral background,
nostalgic stop-motion animation style, miniature diorama, Laika studios claymation aesthetic,
extremely tactile textures, earthy muted color palette,
16:9 --stylize 250 --v 6.0
```

---

### O3: Brass Hand Detail Sheet ⭐ (CRITICAL — bàn tay là visual motif)

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]

DÙNG CHO: 13 DETAIL shots về bàn tay (SB_008, SB_012, SB_015, SB_022, SB_024,
           SB_032, SB_034, SB_040, SB_042 và các shots cận tay khác)

HAND VISUAL MOTIF: Bàn tay kim loại KHỔNG LỒ, nặng nề, thực hiện những hành động
                   VÔ CÙNG nâng niu. Đây là emotional core của video.

TEXTURE SPEC:
- Material: Articulated brass, segmented finger plates
- Base color: Dark amber-orange (#8B6914 equivalent)
- Oxidation: Teal-green verdigris concentrated at finger joints, knuckle seams, palm edge
- Surface: Heavily weathered, visible tool marks, deep scratches
- Joints: Visible mechanical joint rings at each finger knuckle
- Palm: Large, flat, slightly cupped when open
- Weight feel: Must LOOK extremely heavy despite delicate actions

PROMPT:
detailed hand reference sheet, multiple views: palm facing up + palm facing down + side view + fingers spread + gentle gripping gesture,
heavy articulated brass diving glove hand, segmented brass finger plates with visible mechanical joint rings at each knuckle,
dark amber-orange brass color with teal-green verdigris oxidation concentrated at joints and seams,
deeply weathered rusted surface, visible scratches and aged patina,
extremely large and heavy-looking despite being shown in gentle gestures,
isolated on neutral off-white background,
nostalgic stop-motion animation style, miniature diorama, macro photography extreme close-up,
extremely tactile hand-crafted textures, Laika studios claymation aesthetic,
earthy muted color palette, 16:9 --stylize 300 --v 6.0
```

**After generate — điền đây:**
```
APPROVED O3 URL: [URL]
--sref usage for hand shots: --sref [URL]
```

---

### O4: Brass Boots Detail

```
STATUS: PENDING (low priority — generate cuối)
GENERATED IMAGE URL: [điền sau khi generate]
DÙNG CHO: SB_012 (cận bàn chân bước trên cát)

PROMPT:
detailed prop sheet, vintage brass diving boots, front and side view,
thick flat-soled heavy brass boots, dark amber-orange brass with teal-green verdigris at sole edges,
heavily weighted appearance, deeply aged rusted surface,
isolated on neutral background, nostalgic stop-motion animation style,
Laika studios claymation aesthetic, earthy muted colors,
16:9 --stylize 250 --v 6.0
```

---

## Tier 3 — PROP ASSETS

### P2: Hermit Crab + Glass Bottle ⭐

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]
SHOTS: SB_021 (nhặt chai), SB_023 (đặt chai), SB_024 (cua chui vào chai), SB_026 (cua đi xa)

SCALE: Chai ≈ 1/3 kích thước bàn tay brass. Cua ≈ 1/4 kích thước chai.

SPEC:
- Glass Bottle: Old green-tinted glass, bubbles in glass, barnacles on exterior,
                slightly foggy/opaque from years underwater, cork or broken neck
- Hermit Crab: Tiny, articulated claymation legs, soft shell-less abdomen visible,
               antennae, small dark eyes — innocent and cute

PROMPT:
prop design sheet, two items side by side with scale reference:
(1) old sunken glass bottle — green-tinted glass with visible bubbles in glass material, barnacle encrusted exterior, underwater-worn, foggy opacity,
(2) tiny hermit crab — small articulated claymation creature with delicate legs and antennae, soft vulnerable abdomen, small dark eyes, no shell,
scale indicator showing crab is 1/4 the size of bottle,
isolated on neutral background,
nostalgic stop-motion animation style, miniature diorama, macro photography,
extremely tactile hand-crafted textures, Laika studios claymation aesthetic,
earthy muted colors, deep oceanic teal and faded seagrass green palette,
16:9 --stylize 250 --v 6.0
```

---

### P5: Coral Seedling (Glowing)

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]
SHOTS: SB_040 (trong lòng bàn tay), SB_041 (cắm xuống cát), SB_042 (lan tỏa rễ),
       SB_043 (bừng sáng cả vùng), SB_045 (toàn cảnh)

LƯU Ý: Coral phải có glow nhưng theo Grounded Reality Rule → glow phải
        là bioluminescent ORGANIC light (như đom đóm), không phải magical particles.

SPEC:
- Size: Vừa lọt lòng bàn tay brass (nhỏ hơn nhiều so với bàn tay)
- Form: Small coral polyp, branching, fragile-looking
- Light: Soft bioluminescent cyan-teal emitting from within tissue (organic, like a firefly)
- Material: Semi-translucent organic tissue, soft claymation texture

PROMPT:
prop design sheet, tiny glowing coral seedling,
small branching coral polyp the size of a thumbnail, semi-translucent organic tissue,
soft internal bioluminescent cyan-teal light glowing from within like a firefly — organic luminescence not magical sparkles,
fragile delicate branching structure, few tiny visible polyp tips,
scale reference: shown next to a brass gloved hand — seedling fits in palm,
isolated on dark navy background to show bioluminescence,
nostalgic stop-motion animation style, miniature diorama, macro photography extreme close-up,
extremely tactile organic textures, Laika studios claymation aesthetic,
deep oceanic teal and soft bioluminescent cyan color palette,
16:9 --stylize 300 --v 6.0
```

---

### P7: Giant Manta Ray

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]
SHOTS: SB_030 (kẹt xích), SB_031 (ông lão tiếp cận), SB_032 (cận xích),
       SB_033 (cắt xích), SB_034 (xích đứt), SB_035 (bay lên), SB_036 (bóng dáng xa)

SCALE: Cá đuối PHẢI lớn hơn nhân vật nhiều lần — wing span ≥ 3x chiều cao nhân vật.
       Đây là cảnh chuyển từ "nhỏ bé" sang "vĩ đại" trong story arc.

SPEC:
- Size: Massive — wingspan 3-5x larger than the diving suit character
- Shape: Wide flat diamond/kite shape, two wing-like pectoral fins, long thin tail
- Skin: Dark grey-blue on top, pale white on belly, slightly textured claymation surface
- Eyes: Gentle, small, round — NOT predatory
- Entanglement: Heavy rusted iron chain wrapped around one wing edge (visible in P7 shot)
- Movement quality: Graceful, slow, flowing — despite size

PROMPT:
prop design sheet, giant manta ray, multiple views: top view + side view + front view facing camera,
massive manta ray with wingspan 5x larger than a human-sized figure (scale indicator included),
wide flat diamond-shaped body, two enormous pectoral fins like wings, long slender tapering tail,
dark slate-blue grey textured skin on top surface, pale cream-white smooth belly,
gentle small round dark eye (non-threatening), cephalic fin horns at front,
claymation stop-motion texture quality — tactile and hand-crafted,
isolated on neutral background,
nostalgic stop-motion animation style, miniature diorama, Laika studios claymation aesthetic,
deep oceanic teal muted color palette, 16:9 --stylize 250 --v 6.0
```

---

## Tier 4 — ENVIRONMENT ASSETS

### E1: Glass Dome Interior (Inside the Submarine House)

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]
SHOTS: SB_001, SB_002, SB_003 (intro), SB_047, SB_048 (outro)

SPEC:
- Space: Round glass dome structure, dry interior, warm and cozy
- Key elements: Stone fireplace with crackling fire, wooden table, worn armchair,
                brass diving helmet resting on stand/chair, steam teacup
- Glass: The dome walls are curved glass — outside (dark ocean) visible through walls
- Scale: Intimate, cottage-sized — not a big space
- Texture: Stone interior walls, aged wood, worn fabric

COLOR PALETTE:
- Primary: Warm amber (#C17A35) — firelight
- Secondary: Deep oceanic teal (#1A4A5E) — visible outside through glass
- Accent: Muted rusted brass (#7A5020) — helmet, fittings
- Shadow: Warm dark brown (#2A1A0A) — shadowed corners
- Highlight: Pale cream (#F5EDD8) — lamplight on surfaces

LIGHTING:
- Direction: Primarily from fireplace (left or center), secondarily from ambient glass dome glow
- Color temperature: Very warm (2800K equivalent) inside vs cool teal outside
- Intensity: Cozy dim interior — not bright, not dark
- Signature: "warm amber firelight, deep honey glow filling glass dome interior, cool oceanic teal visible beyond curved glass walls"

ATMOSPHERE: No particles, warm steam from teacup only, still air
SCALE: Character fills ~40% of frame height when standing

ENVIRONMENT PACK KEYWORD STRING (copy-paste vào mọi prompt trong E1):
warm amber firelight filling curved glass dome interior, cracked stone fireplace glowing, aged wooden furniture, muted rusted brass diving helmet resting nearby, deep oceanic teal visible through curved glass walls outside, warm deep honey glow, earthy warm interior vs cool exterior contrast

PROMPT (establishing shot — empty scene):
wide establishing shot, interior of a cozy underwater glass dome house, no character present,
warm amber firelight from stone fireplace illuminating aged wooden table and worn armchair,
muted rusted brass diving helmet resting on wooden stand beside the armchair,
steam rising from a ceramic cup on the table,
curved glass dome walls showing dark oceanic teal deep water outside with distant fish shadows,
warm deep honey amber glow filling interior, cool oceanic teal beyond the glass,
nostalgic stop-motion animation style, miniature diorama, macro photography,
extremely tactile hand-crafted textures, Laika studios claymation aesthetic,
deep oceanic teal and warm amber firelight color palette, muted rusted brass accent,
16:9 --stylize 250 --v 6.0
```

---

### E2: Shallow Seagrass Field

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]
SHOTS: SB_005–SB_013 (Verse 1, Pre-Chorus 1), SB_014–SB_019 (Chorus 1)

SPEC:
- Space: Open shallow seabed, seagrass meadow, small coral formations
- Key elements: Flowing seagrass, low coral reef patches, soft sandy bottom
- Overhead: Dappled light rays from water surface above
- Scale: Open space — character feels small but not overwhelmed

COLOR PALETTE:
- Primary: Faded seagrass green (#4A7A50) — seagrass
- Secondary: Muted oceanic teal (#2A5A6A) — water ambient
- Accent: Dappled pale blue (#A0C8D8) — light from above
- Shadow: Deep teal-navy (#1A3040) — shadowed areas
- Coral: Muted rust pink (#8A5050) — small coral patches

LIGHTING:
- Direction: From above (water surface) — god rays angling down
- Color temperature: Cool (underwater blue-green)
- Signature: "dappled underwater light rays from water surface above, soft blue-green ambient, gentle caustic light patterns on sandy floor"

ENVIRONMENT PACK KEYWORD STRING:
shallow underwater seagrass meadow, flowing seagrass in gentle current, small coral reef patches, dappled light rays from water surface above, soft blue-green ambient underwater light, gentle caustic patterns on sandy bottom, vast open oceanic space

PROMPT (establishing shot):
wide establishing shot, shallow underwater seagrass meadow, no character,
dense flowing seagrass in gentle ocean current, small coral reef formations scattered across sandy floor,
dappled sunlight rays angling down from water surface far above, soft blue-green ambient underwater light,
gentle caustic light patterns on the sandy seabed, faint silhouettes of fish near surface,
vast open feeling — enormous ocean space with small intimate seagrass details,
nostalgic stop-motion animation style, miniature diorama, macro photography,
extremely tactile hand-crafted textures, Laika studios claymation aesthetic,
deep oceanic teal and faded seagrass green color palette, dappled pale blue accent,
16:9 --stylize 250 --v 6.0
```

---

### E3: Sandy Seabed (with Debris)

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]
SHOTS: SB_020–SB_026 (Verse 2)

SPEC:
- Space: Open flat sandy seabed, slightly more cluttered than E2
- Key elements: Clean sand in some areas, debris in others (glass bottle, old objects)
- Atmosphere: Slightly more isolated feeling than seagrass

ENVIRONMENT PACK KEYWORD STRING:
sandy ocean floor with scattered debris, clean sand patches and cluttered areas with sunken objects, soft blue-green underwater ambient light, muted oceanic teal, isolated and quiet seabed atmosphere

PROMPT (establishing shot):
wide establishing shot, sandy ocean floor, no character,
flat sandy seabed stretching into blue-green distance, small scattered debris — old glass bottles, rusted fragments half-buried in sand,
clean sand areas contrasting with cluttered debris zones, soft blue-green underwater ambient light from above,
slightly darker and more isolated atmosphere than shallow reef areas,
nostalgic stop-motion animation style, miniature diorama, Laika studios claymation aesthetic,
extremely tactile textures, muted oceanic teal color palette, deep oceanic teal shadows,
16:9 --stylize 250 --v 6.0
```

---

### E4: Deep Abyss

```
STATUS: PENDING
GENERATED IMAGE URL: [điền sau khi generate]
SHOTS: SB_027–SB_046 (Pre-Chorus 2, Chorus 2, Bridge, Final Chorus)

SPEC:
- Space: Deep ocean trench, near-dark, dramatic scale contrast
- Key elements: Rocky formations, near-darkness with occasional bioluminescent light,
                distant whale silhouettes far above, massive sense of scale
- Character appears TINY (visual motif: small person in vast space)
- Scale: Character ≈ 2-3% of frame height at widest shots

COLOR PALETTE:
- Primary: Deep navy (#0A0F2C) — near-darkness
- Secondary: Bioluminescent cyan (#40E0D0 muted version) — coral/creature glow
- Accent: Distant pale blue (#6080A0) — faint distant light
- Shadow: Near-black (#050810) — deep shadows
- Rock: Dark charcoal (#252525) — rocky formations

LIGHTING:
- Direction: Near-zero ambient + point sources (bioluminescence, distant whale glow)
- Color temperature: Very cold, near-black
- Signature: "near-darkness deep ocean abyss, faint distant bioluminescent cyan points of light, vast dark rocky formations, character appears tiny against enormous dark space"

ATMOSPHERE: Suspended particles (barely visible), slow water drift, sense of immense pressure/depth

ENVIRONMENT PACK KEYWORD STRING:
deep ocean abyss near-darkness, massive dark rocky formations, faint bioluminescent cyan points of light, distant whale silhouette far above, character tiny against enormous dark space, deep navy and near-black shadows, vast crushing depth

PROMPT (establishing shot):
wide establishing shot, deep ocean abyss, no character,
massive dark rocky formations rising from near-black seafloor,
near-total darkness with only faint scattered bioluminescent cyan points of light from deep sea organisms,
enormous sense of scale — vast crushing depth visible,
distant giant whale silhouette barely visible far above as a shadow against slightly lighter dark blue,
slow suspended particles drifting in near-motionless water,
nostalgic stop-motion animation style, miniature diorama, macro photography,
extremely tactile hand-crafted textures, Laika studios claymation aesthetic,
deep navy and near-black color palette with faint bioluminescent cyan accent,
no internal glow no magical particles no sparkles,
16:9 --stylize 300 --v 6.0
```

---

## Tier 5 — LIGHTING SETUPS

| Setup ID | Tên | Keyword String | Shots |
|----------|-----|----------------|-------|
| L1 | Interior Warm | warm amber firelight, deep honey glow, cool oceanic teal beyond glass | SB_001–003, SB_047–048 |
| L2 | Shallow Sea Blue | dappled underwater light rays from above, soft blue-green ambient, gentle caustic patterns | SB_005–019 |
| L3 | Sandy Seabed Quiet | soft blue-green underwater ambient, slightly darker, isolated quiet | SB_020–026 |
| L4 | Deep Abyss Dark | near-darkness, faint bioluminescent cyan, vast crushing depth | SB_027–046 |

> [!IMPORTANT]
> **Cross-environment brass color test:** Khi approve E1-E4 establishing shots → verify màu brass
> của suit vẫn readable và nhất quán khi được đặt vào từng environment. Brass warm amber trong L1
> sẽ appear teal-shifted trong L4 — đây là normal và acceptable, nhưng SHAPE phải không đổi.

---

## Tier 6 — STYLE ANCHOR ASSETS

### S2: LOCKED COLOR TONE

```
LOCKED COLOR TONE: deep oceanic teal, warm amber firelight, muted rusted brass, faded seagrass green, soft bioluminescent cyan
```

### S3: LOCKED STYLE STRING

```
LOCKED STYLE STRING: nostalgic stop-motion animation style, miniature diorama, macro photography with shallow depth of field, extremely tactile hand-crafted textures, weathered and aged surfaces, earthy muted color palette, Laika studios claymation aesthetic
```

### S4: Master Frozen Character Block ⭐

> [!IMPORTANT]
> Điền block này SAU KHI Boss approve C3. Copy nguyên văn vào mọi prompt có nhân vật.

```
MASTER FROZEN CHARACTER BLOCK:
[ĐIỀN SAU KHI C3 APPROVED]

Draft (điền URL sau khi generate C3):
kind elderly man completely enclosed in a heavy vintage brass diving suit, large round brass sphere helmet with single circular foggy porthole glass window riveted brass ring, segmented articulated brass body suit at all joints, articulated brass gloved hands with visible knuckle joint mechanisms, thick flat-soled heavy brass boots, dark amber-orange brass with teal-green verdigris oxidation at joints and seams, deeply rusted aged patina, exaggerated spindly claymation proportions, extremely tactile stop-motion puppet texture
```

### S1: Approved Shot Gallery — Style Bank

```
[Điền sau khi Boss approve 3-5 shots đầu tiên từ Stage 4.2]
Shot A: [URL]
Shot B: [URL]
Shot C: [URL]

Usage: --sref [URL_A] [URL_B] [URL_C]
```

---

## Asset Status Summary

| Asset ID | Tên | Status | URL | Dùng cho |
|----------|-----|--------|-----|---------|
| C1 | Face Sheet | PENDING | — | --cref --cw 0 |
| C2 | Full Body Bare | PENDING | — | SB_047 nhà không đồ lặn |
| **C3** | **Fully Costumed** | **PENDING** | **—** | **--cref --cw 100 (critical)** |
| C4 | Expression Sheet | PENDING | — | Expression reference |
| C5 | Pose Sheet | PENDING | — | Pose reference |
| O1 | Suit Turnaround | PROMPT READY | — | Costume ref |
| O2 | Helmet Detail | PENDING | — | Headwear ref |
| **O3** | **Brass Hands** | **PENDING** | **—** | **--sref for 13 DETAIL hand shots** |
| O4 | Boots Detail | PENDING | — | SB_012 |
| P2 | Hermit Crab + Bottle | PENDING | — | SB_021–026 |
| P5 | Coral Seedling | PENDING | — | SB_040–045 |
| P7 | Giant Manta Ray | PENDING | — | SB_030–035 |
| **E1** | **Glass Dome** | **PENDING** | **—** | **SB_001–003, 047–048** |
| **E2** | **Seagrass Field** | **PENDING** | **—** | **SB_005–019** |
| E3 | Sandy Seabed | PENDING | — | SB_020–026 |
| **E4** | **Deep Abyss** | **PENDING** | **—** | **SB_027–046** |
| L1 | Interior Warm | LOCKED | — | Keyword string ready |
| L2 | Shallow Sea Blue | LOCKED | — | Keyword string ready |
| L3 | Sandy Seabed | LOCKED | — | Keyword string ready |
| L4 | Deep Abyss Dark | LOCKED | — | Keyword string ready |
| S1 | Style Bank | PENDING | — | --sref |
| **S2** | **Color Token** | **✅ LOCKED** | — | **"deep oceanic teal, warm amber firelight, muted rusted brass, faded seagrass green, soft bioluminescent cyan"** |
| **S3** | **Style String** | **✅ LOCKED** | — | **Every prompt** |
| S4 | Frozen Char Block | PENDING (draft ready) | — | After C3 approved |

**Priority generate order:**
1. C3 → O3 → E1 + E4 (kiểm tra cross-env color) → E2 + E3 → Props → Style Bank
