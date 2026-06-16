# Visual Style Module: Warm Gentle Loving Handcrafted Storybook Miniature

> **Style ID:** `warm_storybook`
> **Status:** 🟢 Active Default
> **Version:** 1.0
> **Dùng cho:** Mọi video trừ khi Boss chỉ định style khác

---

## Cách sử dụng file này

File này chứa toàn bộ DNA thị giác cho **một style cụ thể**. Agent đọc file này tại Stage 4.1 để load phong cách hình ảnh.

Khi Boss muốn style mới, tạo file `04s_visual_style_[tên_style].md` theo cùng cấu trúc, không cần sửa file `04_image_prompt_development_knowledge.md`.

---

## 1. Style Identity & Feel

### Tên phong cách
**Warm Gentle Loving Handcrafted Storybook Miniature**

### Hình ảnh nên cảm nhận như:

- warm
- light and luminous
- soft and smooth
- loving
- gentle
- healing
- mature and elegant (beautiful elderly characters)
- welcoming
- emotionally clean
- bright and rực rỡ (even at night scenes, absolutely no pitch-black darkness)
- handcrafted but not rough or cracked
- storybook-like but **not childish, not cute/chibi**
- grounded in everyday domestic realism — real kitchens, real hands, real small gestures
- cinematic but not dark or overdramatic
- **PROPORTIONS: realistic adult human body proportions** — head size, limb length, and body scale must match a real adult person, not a doll or cartoon figure
- **OPEN & AIRY** — every frame breathes. Generous negative space, one clear subject, room for the eye to rest and wander

### Người xem nên cảm thấy:

- comfort
- memory
- tenderness
- quiet wonder
- being welcomed into a peaceful, bright place

### Hình ảnh KHÔNG được cảm nhận như:

- creepy or scary
- waxy
- muddy
- heavy
- horror-like
- overly textured or cracked
- plastic or glossy CGI
- distorted or deformed
- dark or pitch-black (no cold gloomy blue night tones)
- chaotic or noisy
- **cluttered, cramped, or suffocating** — khung hình bí bách khiến mắt bị kẹt, không có chỗ thở ← nguy cơ drift số 2
- **chibi, cute anime, oversized head, oversized eyes, toy-like anatomy** ← đây là nguy cơ drift số 1 của style này

---

## 2. Style Anchors

### Full style anchor (dùng cho prompt > 500 ký tự)

```
handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, handsome and gracefully aging elderly face, clean smooth features with minimal soft laugh lines, no deep-cut wrinkles, kind eyes, fluffy needle-felted wool hair with visible fine fibers, subtle fabric detail, smooth matte porcelain skin, realistic adult human body proportions, correct head-to-body ratio of a real adult person, bright and luminous color palette of soft cream, honey-gold, and light amber, warm natural daylight or radiant amber light with lifted soft warm shadows, absolutely no pitch-black darkness, open and airy composition, generous negative space, single clear subject, uncluttered background, peaceful everyday realism, airy and healing mood, 16:9, not photorealistic, not glossy 3D
```

### Short style anchor (dùng cho prompt ngắn hơn)

```
handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, handsome gracefully aging face, clean smooth features, kind eyes, soft wool-like hair, subtle fabric detail, realistic adult body proportions, correct head-to-body ratio, open and airy composition, generous negative space, bright luminous warm-gold daylight or amber night light, lifted soft warm shadows, 16:9
```

---

## 3. Style Migration Notes (từ style cũ)

Style cũ sử dụng ngôn ngữ nặng nề. Tránh dùng mặc định:

| ❌ Tránh | ✅ Thay bằng |
|----------|-------------|
| wax-clay skin | smooth hand-painted character, smooth matte porcelain skin |
| visible fibers | subtle fabric detail, soft woven detail, gentle knit detail |
| matte carved wood grain | smooth matte wood, warm matte wood, polished golden-oak table |
| aged paper texture | soft aged paper, warm old paper, folded paper flowers |
| cinematic semi-realistic handcrafted stop-motion puppet realism | handcrafted miniature diorama, macro photography, tilt-shift lens, cinematic handcrafted storybook softness |

---

## 4. Character Design (Style-Specific)

Characters nên cảm nhận như kind, handsome, and gracefully aging older humans trong thế giới storybook thủ công.

> [!IMPORTANT]
> **Anti-Chibi Proportion Lock:** Thế giới xung quanh là miniature diorama, nhưng nhân vật bên trong thế giới đó phải có tỉ lệ người thật. Đầu nhỏ so với thân người, tay chân dài đúng tỉ lệ. **Không bao giờ được để đầu lớn hơn 1/5 chiều cao cơ thể.** Mục tiêu: 80/100 ảnh giữ đúng tỉ lệ này.

### Đặc điểm bắt buộc

- handsome, gracefully aging elegant faces
- clean smooth facial features
- minimal soft laugh lines around eyes
- warm kind eyes
- **correct adult head-to-body ratio** — head is roughly 1/6 to 1/7 of total body height
- **realistic adult body proportions** — full-length torso, normal limb length
- **balanced facial proportions** — eyes are not oversized, not cartoonishly large
- calm body language, gentle posture, readable gestures
- smooth matte porcelain skin
- fluffy needle-felted wool hair with visible fine fibers, clear hairline
- subtle fabric detail
- mature emotional presence

### Đặc điểm CẤM

- children, kids, toddlers, babies (nghiêm cấm tuyệt đối)
- **chibi anatomy, oversized head, oversized eyes** ← nguy cơ drift số 1
- **cute anime proportions, doll-like toy body, toy-scale anatomy**
- **head larger than 1/5 of total body — tuyệt đối cấm**
- deep-cut wrinkles or harsh lines
- sunken cheeks or hollow eyes
- melted wax skin, muddy clay skin, cracked skin
- blob-like hair, hair fused into the face
- distorted faces, uncanny doll expressions
- extreme puppet anatomy
- horror mood
- plastic toy finish, overly shiny CGI skin

### Hair rule

Hair phải tách biệt khỏi da.

Dùng: `fluffy needle-felted wool hair with visible fine fibers, soft gray hair with clear hairline, gentle wool-like hair, not fused to the face`

Tránh: `blob-like hair, melted hair, hair fused with skin, solid clay hair mass`

Khi nhân vật close-up, luôn thêm: `clear hairline, soft separated curls`

### Face rule

Gương mặt phải đẹp, sạch, đọc được cảm xúc, không nhăn quá mức.

Dùng: `handsome and gracefully aging face, clean smooth features, minimal soft laugh lines, kind eyes, gentle expression, balanced facial proportions, smooth hand-painted character, smooth matte porcelain skin`

Tránh: `deep wrinkles, harsh facial lines, sunken cheeks, hollow eyes, cracked skin, waxy skin, creepy puppet face, photorealistic elderly skin`

### Hands rule

Cho close-up hoặc chi tiết, dùng: `clean elegant elderly hand shape, smooth skin with gentle fingers, no harsh veins or rough wrinkles, soft hand-painted hands, gentle hand pose, subtle sleeve detail`

Tránh: `deformed hands, fused fingers, lumpy fingers, over-wrinkled hands, muddy hand texture, harsh veins`

### Character Rendering Lock

Khi kịch bản mô tả nhân vật lớn tuổi, luôn áp dụng:
- **Từ khóa bắt buộc:** `smooth hand-painted character, handsome and gracefully aging elderly face, clean smooth features with minimal soft laugh lines, smooth matte porcelain skin, realistic adult body proportions, correct head-to-body ratio of a real adult person`
- **Tránh tuyệt đối:** deep wrinkles, hollow eyes, waxy skin, creepy puppet face, **chibi anatomy, oversized head, oversized eyes, toy body proportions**.
- **Trang phục:** Hoàn toàn mở theo bối cảnh kịch bản, luôn bổ sung cụm từ chất liệu: `subtle fabric detail` hoặc `thick chunky knit/tweed texture`.

---

## 5. Material Palette

Texture nên hỗ trợ cảm xúc, không nên chiếm trọng tâm hình ảnh.

### Vật liệu ưa thích

- soft aged paper, folded paper flowers
- smooth matte wood, porcelain cups, clay pots
- brass details, soft fabric, gentle knit detail
- warm painted walls, cream curtains
- handmade props

### Cảm giác vật liệu tốt nhất

soft, dry, clean, warm, slightly handmade, not melted, not muddy, not plastic

### Tactile Material Lock

Không bắt buộc vật thể phải xuất hiện trong mọi cảnh, nhưng **KHI** chúng xuất hiện:
- **Cừu:** `fluffy white felted-wool sheep with a thick beautifully textured felted wool coat, styled as a miniature stop-motion puppet`
- **Đồ gỗ:** `smooth matte wood` hoặc `polished golden-oak with subtle natural grain`
- **Giấy/sổ sách:** `soft aged paper, warm old paper texture`

---

## 6. Color DNA

### Bảng màu mặc định

cream, honey-gold, soft peach, warm beige, pale amber, gentle ivory, light brown, soft green garden accents, small old-gold details

### Tránh mặc định

dark blue, cold teal, muddy brown, harsh orange, neon colors, heavy black shadows, gothic palettes

### Cách dùng gold tự nhiên

Gold là chữ ký Coslient, nhưng phải tự nhiên. Gold có thể xuất hiện như:
morning sunlight, paper flower glow, window warmth, brass latch, cup rim, tiny lamp, honey-colored wood, soft flower center, warm thread, faint magical glow

Không ép gold một cách giả tạo.

---

## 6.5. Focal Accent Color System (Eye-Anchor Colors)

> [!IMPORTANT]
> Đây là hệ thống màu điểm neo mắt bắt buộc. Thiếu accent color → frame bị phẳng về tonal và mắt người xem không biết nhìn vào đâu → tone drift theo từng prompt. Mỗi prompt **phải** có ít nhất 1 accent color được đặt có chủ ý vào 1 object cụ thể.

### Định nghĩa

**Focal Accent Color** là màu sắc nhỏ, có tương phản đủ để mắt "đậu" vào, nhưng không đủ lớn để phá vỡ bảng màu ấm chủ đạo. Vai trò của nó: tạo điểm dừng cho mắt, ngăn frame bị nhòa vào nhau, giữ tone cảm xúc ổn định xuyên suốt.

### Ba màu accent được phép dùng

| Accent | Tên gọi trong prompt | Cảm xúc | Đặt vào object nào |
|--------|---------------------|---------|-------------------|
| 🌿 **Dusty Sage Green** | `muted sage green`, `dusty sage`, `faded sage-green` | Ký ức thiên nhiên, bình yên | Cây nhỏ, khăn bếp, tạp dề, áo khoác nhẹ, cốc men, rèm mỏng |
| 🫙 **Faded Cornflower Blue** | `faded cornflower blue`, `dusty soft blue`, `aged porcelain blue` | Hoài niệm, nhẹ nhàng, đồ gốm cũ | Cốc sứ, bình hoa, khăn bàn có sọc, áo ngủ, hộp thiếc cũ |
| 🌸 **Pale Terracotta Rose** | `pale dusty rose`, `muted terracotta pink`, `faded petal rose` | Yêu thương, ấm áp thầm lặng | Bông hoa nhỏ, ruy-băng cũ, gối sofa, khăn tay, tấm thêu |

### Quy tắc sử dụng (BẮT BUỘC)

1. **Diện tích tối đa 5–15% frame** — accent chỉ là điểm nhấn, không phải nền. Nếu accent lan rộng → bị vỡ palette.
2. **Chỉ đặt vào objects cụ thể** — không đặt accent vào background, bầu trời, tường, hay sàn nhà.
3. **Mỗi prompt chọn đúng 1 accent** — không dùng 2 accent cùng lúc trong 1 prompt.
4. **Xoay vòng accent qua các prompt** — không để cùng 1 accent xuất hiện quá 3 lần liên tiếp.
5. **Accent không được sáng hơn highlight chính** — nó phải hơi tối hơn hoặc desaturated để đứng yên trong palette ấm.

### Prompt language chuẩn

Đặt accent vào phần object description, trước style anchor:

```
..., a small sage-green ceramic pot on the windowsill, ...
..., she wears a faded cornflower-blue apron with soft worn edges, ...
..., a single pale dusty-rose flower in a glass bottle on the table, ...
..., a folded dusty sage-green cloth draped over the chair arm, ...
..., an aged porcelain-blue mug placed near her elbow, ...
```

### Vì sao không dùng màu khác

- **Đỏ / cam đậm:** Quá aggressive, phá tone healing.
- **Tím:** Có thể cảm giác gothic hoặc lạnh.
- **Vàng chanh / xanh lá tươi:** Trẻ trung quá, không khớp demographic 45-55+.
- **Trắng tinh:** Không phải accent — hòa vào base palette cream.
- **Đen:** Tuyệt đối cấm theo Lighting DNA.

### Ví dụ tích hợp đầy đủ vào prompt

```
An elderly woman standing by a sunlit kitchen window, medium shot framed through a doorway, her hands resting on the windowsill beside a small sage-green ceramic pot with a single dried stem, handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, handsome and gracefully aging elderly face, clean smooth features with minimal soft laugh lines, kind eyes, fluffy needle-felted wool hair with visible fine fibers, subtle apron detail, smooth matte porcelain skin, warm morning daylight streaming through, cream honey-gold palette with a small dusty sage-green accent on the pot, rich tonal depth, lifted soft warm shadows, tender and peaceful, 16:9
```

---

## 7. Lighting DNA

### Ưu tiên

- soft morning sunlight
- late-morning daylight, clear afternoon warmth
- gentle after-rain daylight
- warm window light, lifted shadows
- airy sunlit interiors, soft garden light
- honey-gold daylight, cream and peach ambient light

### Ánh sáng ban ngày

`bright and luminous daylight, soft warm morning/afternoon sun streaming through, soft cream and honey-gold tones`

### Ánh sáng ban đêm

Phải sử dụng bầu trời đêm sáng tự nhiên và ánh sáng ấm cúng:
`luminous indigo-blue night sky with glittering natural stars, cozy golden-amber ambient glow, lifted soft warm shadows, absolutely no pitch-black darkness`

### Tránh

- dark dusk, blue night
- harsh dramatic lighting, horror contrast
- heavy cinematic shadows, overly moody interiors
- extreme backlight that hides the character
- pitch-black darkness, cold gloomy blue tones, heavy black shadows, harsh dark contrast

Lighting nên cảm nhận như kindness entering the frame.

---

## 7.5. HDR & Tonal Richness Doctrine

> [!IMPORTANT]
> Warm Storybook images phải có **chiều sâu tonal thực sự** — không phải ảnh phẳng, không phải low-contrast watercolor wash. HDR trong context này là **pseudo-HDR aesthetic**: shadows vẫn có detail, highlights không bị clip, mid-tones được phân tầng rõ. Kết quả: ảnh trông có hồn, có chiều sâu, và visual richness khiến người xem dừng lại.

### Định nghĩa HDR cho Warm Storybook

Trong context AI image generation cho style này, "HDR" không có nghĩa là tone-mapping HDR cực đoan hay photo-realistic camera HDR. Nó có nghĩa:

- **Shadow retain detail:** Vùng tối không bị fill thành grey flat — có texture, có warmth, có màu sắc riêng
- **Highlight glow, không clip:** Vùng sáng (cửa sổ, bầu trời, ánh nến) rực rỡ nhưng vẫn có gradient, không cháy trắng
- **Rich mid-tone separation:** Màu trung tính được phân tầng rõ — honey vs gold vs amber vs cream là các giá trị khác nhau
- **Micro-contrast:** Các vật thể gần nhau vẫn tách biệt về tonal value, không bị merge thành mảng phẳng
- **Local contrast:** Mỗi vùng nhỏ trong frame có internal contrast riêng

### HDR Keywords cho Prompt (chọn 2-3 cụm phù hợp mỗi prompt)

**Tonal depth & richness:**
- `rich tonal depth with luminous highlights and warm shadow detail`
- `HDR-like tonal range, bright luminous highlights blending into warm shadow detail`
- `pseudo-HDR warm palette, deep rich shadows retaining texture and warmth`
- `high dynamic range warm lighting, bright areas glow without clipping, shadows full of honey-amber detail`

**Micro-contrast & separation:**
- `subtle micro-contrast between cream and gold and amber tones`
- `layered warm tonal values with clear separation between honey, amber, and cream`
- `rich local contrast, each surface has its own warm tonal identity`

**Luminosity & glow:**
- `luminous warm glow with deep rich background warmth`
- `backlit warm-golden light creating halo glow around subject without overexposure`
- `volumetric warm light rays with deep atmospheric depth`
- `radiant honey-amber light with rich tonal gradient from bright center to warm dark edges`

**Cinematic richness:**
- `cinematic warm tonal richness, not flat, not washed out`
- `filmic warm color grading with lifted blacks and rich warm highlights`
- `Vintage celluloid-inspired warm color science, rich shadow detail, creamy highlights`

### Vị trí đặt HDR keywords trong prompt

Đặt ngay sau phần ánh sáng (lighting description), trước phần emotional tone:

```
[scene + subject + action], [shot size + composition], [lighting description], [HDR/tonal richness keywords], [style anchor], [character + material], [emotion], 16:9
```

### Quy tắc kết hợp: HDR + Warm Storybook

| Tình huống | HDR keywords phù hợp |
|-----------|---------------------|
| Cảnh buổi sáng | `rich warm morning light with long golden shadows, luminous honey highlights, shadow detail in warm amber tones` |
| Cảnh bên cửa sổ | `backlit warm window glow creating soft halo, deep warm tonal richness behind the figure, cream-to-amber gradient` |
| Cảnh buổi tối ấm cúng | `luminous indigo-blue night sky, warm amber interior glow, rich tonal depth with detailed shadow warmth, no flat darkness` |
| Cảnh ngoài vườn | `bright layered outdoor light, rich green shadow detail, luminous warm-gold highlights on surfaces, volumetric depth` |
| Close-up tay/mặt/đồ vật | `rich close-up tonal richness, micro-contrast on skin texture, warm highlight with detailed shadow, tonal depth` |

### Full Style Anchor HDR-Enhanced (dùng thay cho anchor cũ khi cần độ sâu tonal cao nhất)

```
handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, handsome and gracefully aging elderly face, clean smooth features with minimal soft laugh lines, no deep-cut wrinkles, kind eyes, fluffy needle-felted wool hair with visible fine fibers, subtle fabric detail, smooth matte porcelain skin, bright and luminous color palette of soft cream, honey-gold, and light amber, warm natural daylight or radiant amber light with lifted soft warm shadows, rich tonal depth with luminous highlights and warm shadow detail, HDR-like warm tonal range, micro-contrast between honey and amber and cream tones, absolutely no pitch-black darkness, open and airy composition, generous negative space, single clear subject, uncluttered background, peaceful everyday realism, airy and healing mood, 16:9, not photorealistic, not glossy 3D
```

---

## 8. Emotional Doctrine

### Trung tâm cảm xúc

love, memory, gratitude, care, tenderness, quiet hope, healing, welcome, gentle reflection, peaceful closure

### Ngay cả khi chủ đề buồn

Hình ảnh không được cảm thấy tuyệt vọng. Nỗi buồn phải được sưởi ấm bởi sự chăm sóc.

### Cảm giác khung hình

someone is still loved, someone is remembered, something unsaid becomes beautiful, a small domestic moment becomes sacred, an ordinary place becomes gently magical

---

## 9. Everyday Detail Devices Library

Thay vì phép thuật hay chữ viết, hình ảnh quan trọng nên chứa **một chi tiết đời thường được quan sát cực kỳ cẩn thận** — loại chi tiết bình thường nhưng đẹp đến mức người xem dừng lại.

### ❌ Tuyệt đối cấm trong section này

- Không chữ viết, handwriting, letters, envelopes, ink lines
- Không phép thuật: không flowers blooming from objects, không paper transformations, không magical glow events
- Không surreal objects lơ lửng

### ✅ Thiết bị chi tiết đời thường cho style này

**Ánh sáng & bóng tối tự nhiên:**
- slanted morning sunlight casting long warm shadows across a wooden floor
- late afternoon sun catching the rim of a ceramic cup, making it glow like amber
- soft window light falling across an elderly person's hands at rest
- a patch of gold sunlight on a worn wooden chair seat
- steam rising slowly from a bowl of soup in morning light

**Hành động tay & cử chỉ nhỏ:**
- weathered hands carefully folding a cloth napkin
- an elderly hand resting on a wooden table, fingers slightly curled
- two cups of tea placed side by side on a tray, one slightly fuller than the other
- a hand smoothing down a bed quilt with quiet care
- fingers trailing along a garden fence rail while walking slowly

**Đồ vật & không gian sống:**
- a worn coat hanging on a hook beside a door, still shaped by the body that wore it
- a pair of old shoes placed neatly at the threshold
- a half-eaten bowl of soup beside a window, still steaming
- a garden chair left slightly turned, as if someone just stood up
- a kitchen shelf with three mismatched ceramic mugs
- a single flower in a small glass bottle on a windowsill
- laundry hanging still on a line in quiet afternoon air
- an open gate at the end of a garden path, soft light beyond it

**Khoảnh khắc chuyển tiếp nhẹ:**
- a door left slightly ajar, warm light leaking through the gap
- a figure pausing at the top of porch steps, looking out at the garden
- a person standing still at a window, light on one side of their face
- an empty doorway that still holds the shape of presence

> [!NOTE]
> Đây là các ví dụ mẫu. Mỗi dự án nên phát triển everyday detail devices riêng phù hợp với concept đã duyệt. Luôn ưu tiên chi tiết **quan sát được trong cuộc sống thực**, không phải hư cấu hay ẩn dụ thị giác.

### Cảm giác chi tiết đúng

clear, grounded, emotionally resonant, quietly beautiful, not magical, not decorative, not random

One beautifully observed real detail is stronger than ten invented magical events.

---

## 10. World Logic

### Thế giới mặc định Coslient

tiny old houses, cozy kitchens, warm sitting rooms, gentle bedrooms, front porches, garden paths, sunrooms, miniature town lanes, small village squares, garden gates, old mailboxes, wooden tables, windows, stairs, thresholds, quiet domestic spaces

### Cảm giác thế giới

handmade, safe, old but loved, lived-in, small but emotionally large, warm and welcoming

### Tránh

empty generic fantasy spaces, overdesigned magical kingdoms, futuristic CGI rooms, glossy dollhouses, cluttered AI-fantasy decoration, cold photorealistic suburbia

---

## 11. Prompt Templates (Style-Specific)

### Full template

```
[scene + subject + emotional action], [shot size / composition], [one specific grounded everyday detail — lighting, gesture, or object observed closely], open and airy composition, generous negative space, single clear focal point, uncluttered background, handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, handsome and gracefully aging elderly face, clean smooth features with minimal soft laugh lines, no deep-cut wrinkles, kind eyes, fluffy needle-felted wool hair with visible fine fibers, subtle fabric detail, smooth matte porcelain skin, realistic adult body proportions, correct head-to-body ratio of a real adult person, [key props/materials], warm natural daylight, airy cream honey peach palette, [emotion], 16:9
```

### Compressed template

```
[scene + subject + action], [shot size], [one grounded everyday detail], open and airy composition, generous negative space, handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, kind elderly face, realistic adult body proportions, correct head-to-body ratio, fluffy needle-felted wool hair with visible fine fibers, subtle fabric detail, smooth matte wood, warm natural daylight, cream honey peach palette, [emotion], 16:9
```

### Dynamic template chuẩn hóa

```
[Chủ thể + Hành động theo concept], [Góc máy & Bố cục động], [Chi tiết đời thường cụ thể quan sát được — ánh sáng / cử chỉ / đồ vật], [Vật thể & Bối cảnh theo kịch bản], handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, handsome and gracefully aging elderly face, clean smooth features with minimal soft laugh lines, no deep-cut wrinkles, kind eyes, fluffy needle-felted wool hair with visible fine fibers, subtle fabric detail, smooth matte porcelain skin, realistic adult body proportions, correct head-to-body ratio of a real adult person, [Ánh sáng & Màu sắc Luminous động theo ngày/đêm], 16:9
```

### Example prompt (ĐÃ SỬA — không chibi, không chữ viết, không phép thuật)

Cozy miniature kitchen in bright late-morning light, an elderly woman standing beside a wooden table with both hands resting lightly on its surface, medium shot framed through a doorway, slanted morning sunlight casting long warm shadows across the worn wooden floor, a single ceramic mug steaming gently near her elbow, handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, soft natural elderly face, kind eyes, fluffy needle-felted wool hair with visible fine fibers, subtle apron detail, smooth matte wood, realistic adult body proportions, correct head-to-body ratio of a real adult person, cream honey peach palette, tender and inviting, 16:9

---

## 12. Words to Prefer / Avoid

### Dùng nhiều

handsome, gracefully aging, elegant elderly face, clean smooth features, minimal soft laugh lines, kind eyes, smooth matte porcelain skin, fluffy needle-felted wool hair with visible fine fibers, clean elegant hands, soft, gentle, warm, loving, tender, welcoming, peaceful, healing, luminous and bright, warm-gold glow, luminous indigo-blue, light amber, cream, honey-gold, warm natural daylight, radiant amber light, lifted soft warm shadows, soft aged paper, smooth matte wood, calm body language, emotional clarity, slanted warm light, long soft shadows, steam rising gently, worn wooden surface, mismatched ceramic mugs, garden gate, open door, half-open window, laundry on a line, worn coat on a hook, a figure pausing at a threshold, **open and airy composition**, **generous negative space**, **single clear subject**, **uncluttered background**, **breathing room**, **minimalist foreground**, **clean empty sky**, **vast open field**, **wide empty corridor**, **solitary figure in open space**

### Tránh hoặc dùng rất ít

deep wrinkles, harsh facial lines, sunken cheeks, hollow eyes, cracked skin, waxy skin, creepy puppet face, pitch-black darkness, heavy black shadows, gloomy night, cold dark blue tones, moody dark atmosphere, harsh dark contrast, heavy texture, gritty, rough, hyper-detailed, visible fibers, lumpy, muddy, wet clay, horror puppet, glossy 3D, plastic toy, photorealistic skin, surreal chaos, fantasy clutter, **cluttered frame**, **busy background**, **cramped composition**, **too many objects competing for attention**, **no breathing room**, **frame feels suffocating**

---

## 13. Style Fingerprint (Compact Summary)

Soft handcrafted storybook miniature world, warm gentle loving atmosphere, **OPEN & AIRY COMPOSITION** — generous negative space, single clear subject, uncluttered background, every frame breathes (≥30% negative space target), **realistic adult human body proportions** (correct head-to-body ratio, no oversized head, no oversized eyes, no chibi anatomy), handsome and gracefully aging elderly characters with clean smooth features and minimal laugh lines, soft wool-like hair, clean elegant hands, smooth matte wood, bright and luminous color palette (cream, honey-gold, light amber, luminous indigo-blue), **one focal accent color per frame** (dusty sage green / faded cornflower blue / pale terracotta rose — max 15% frame area, placed on a specific object only), bright natural daylight or radiant amber light with lifted soft warm shadows (no pitch-black darkness), **grounded in everyday domestic realism** — real kitchens, real gestures, real quiet moments — emotionally readable body language, no deep wrinkles, no waxy skin, no creepy puppet face, no pitch-black gloomy night, **no chibi, no cute anime proportions, no oversized heads**, **no text, no handwriting, no magical transformations, no floating objects**, **no cluttered frames, no busy backgrounds, no cramped compositions**.

---

## 14. Revision Behavior (Style-Specific)

| Boss nói | Sửa |
|----------|-----|
| **Nhân vật bị chibi / đầu to / mắt to** | **ƯU TIÊN SỬA NGAY:** Thêm `realistic adult body proportions, correct head-to-body ratio of a real adult person` vào positive. Bỏ mọi cụm từ "cute", "adorable", "tiny character". |
| Thiếu accent / flat tone | Thêm 1 focal accent object vào prompt: `a small sage-green ceramic pot`, `an aged porcelain-blue mug`, hoặc `a pale dusty-rose flower in a glass bottle`. Đặt ngay sau phần action/object, trước style anchor. |
| Accent bị vỡ / quá sặc sỡ | Đổi sang shade nhạt hơn: `muted`, `faded`, `dusty`. |
| Quá nặng / heavy | Giảm texture language, bỏ "visible fibers", "wax-clay", "highly detailed texture". Thêm "smooth", "soft", "subtle", "airy", "warm gentle loving atmosphere" |
| Nhân vật creepy | Tăng "soft natural elderly face", "kind eyes", "balanced facial proportions", "avoid creepy puppet face". Bỏ "sculpted wrinkles", "puppet realism" |
| Tóc bệt / fused | Thêm "fluffy needle-felted wool hair with visible fine fibers", "clear hairline", "avoid fused hair and skin", "avoid blob-like hair" |
| Quá glossy | Thêm "not glossy 3D", "soft matte finish", "avoid plastic shine" |
| Thiếu ấm | Thêm "warm gentle loving atmosphere", "cream honey peach palette", "soft natural daylight", "tender cinematic softness" + thêm domestic/caring gesture |
| Nhàm chán / boring | Thêm một everyday detail được quan sát cực kỳ cẩn thận (ánh sáng, cử chỉ tay, đồ vật quen thuộc), composition rõ hơn, leading lines, emotional action, symbolic motif từ cuộc sống thực |
| Quá rối / busy | Giảm objects, focus 1 subject, dùng negative space, bỏ decorative fragments thừa, composition sạch hơn |
| Chữ viết / phép thuật xuất hiện | Xóa hoàn toàn: không handwriting, letters, envelopes, paper flowers, magical transformations. Thay bằng: chi tiết đời thường cụ thể (hơi nước bốc, tấm rèm, cốc sứ, cửa mở hé). Thêm vào prompt: "no text no handwriting no magical elements" |
| Ảnh phẳng / flat | Thêm 3 lớp không gian rõ: foreground object + mid character + background space. Đổi góc máy: "camera placed low", "seen through doorway", "through foreground foliage". Làm nổi bật ánh sáng có hướng (slanted rays, rim light, long shadows) |
| **Ảnh bí / cluttered / ngột ngạt** | **ƯU TIÊN SỬA NGAY:** Xóa bớt objects trong prompt. Thêm `open and airy composition, generous negative space, single clear focal point, uncluttered background`. Chọn wide shot hoặc medium-wide thay vì medium shot. Đặt nhân vật trong không gian mở (cánh đồng, góc phố rộng, hiên nhà thoáng). |

---

## 15. Color DNA Reference

> [!NOTE]
> Section này là **nguồn tham khảo bảng màu** của style `warm_storybook`. Coslient sử dụng đây khi xây dựng Color Tone String cho từng video (dựa trên câu chuyện). Không phải block cứng nhắc bắt buộc — tone màu thực tế của từng video do câu chuyện quyết định.

### Block chính (gắn vào cuối prompt)

```
storybook illustration style, vintage 35mm film look, warm golden-hour light, soft lifted blacks, amber split-tone highlights, gentle film halation, muted earthy ochre-sienna palette, subtle 35mm grain
```

### Ví dụ tích hợp đầy đủ

```
An elderly woman sitting quietly by the kitchen window, her hands resting on a warm honey-toned wooden table, a faded sage-green ceramic mug steaming gently beside her, soft morning light falling across her face, medium shot seen through a doorway, handcrafted miniature diorama, macro photography, tilt-shift lens, warm gentle loving atmosphere, smooth hand-painted character, handsome and gracefully aging elderly face, kind eyes, soft wool-like hair, subtle apron detail, storybook illustration style, vintage 35mm film look, warm golden-hour light, soft lifted blacks, amber split-tone highlights, gentle film halation, muted earthy ochre-sienna palette, subtle 35mm grain, 16:9
```

---

## 16. Open & Airy Composition Doctrine (Học thuyết Khung hình Thoáng)

> [!IMPORTANT]
> **Đây là nguyên tắc cốt lõi ảnh hưởng đến khả năng viral.** Khung hình thoáng giúp mắt người xem biết nhìn vào đâu ngay lập tức — tạo ra hiệu ứng "scroll stop" tự nhiên trên mọi nền tảng. Khung hình bí làm não mệt và ngón tay lướt tiếp.

### Định nghĩa "Thoáng"

Một khung hình **thoáng** không có nghĩa là trống rỗng — mà có nghĩa là:
- **Một chủ thể rõ ràng** — mắt người biết nhìn vào đâu ngay khi frame xuất hiện
- **Không gian âm đủ lớn** — ít nhất 30% diện tích frame không có chi tiết phức tạp
- **Hậu cảnh sạch** — không có objects cạnh tranh sự chú ý phía sau chủ thể
- **Ánh sáng có hướng rõ** — gradient sáng tối tự nhiên tạo chiều sâu mà không cần nhiều objects

### Kỹ thuật tạo khung hình thoáng

| Kỹ thuật | Mô tả | Keywords trong prompt |
|---------|-------|-----------------------|
| **Sky breathing** | Để phần bầu trời hoặc nền sáng chiếm ≥40% frame | `vast open sky, clean luminous background` |
| **Solitary figure** | Nhân vật đứng một mình trong không gian rộng, không objects cạnh tranh | `solitary figure in open space, empty surroundings` |
| **Negative space frame** | Nhân vật lệch sang 1/3, phần còn lại là không gian trống ấm áp | `asymmetrical composition, generous negative space on one side` |
| **Clean field/ground** | Mặt đất hoặc sàn nhà sạch, không lộn xộn đồ vật | `clean wooden floor, empty meadow ground, uncluttered path` |
| **Misty depth** | Hậu cảnh mờ dần tự nhiên (tilt-shift) tạo cảm giác thoáng sâu | `softly blurred background, tilt-shift depth, gentle bokeh` |
| **Open doorway** | Nhân vật ở ngưỡng cửa, phía sau là khoảng sáng mở | `figure at open doorway, bright open space beyond` |
| **Wide establishing** | Cảnh rộng, nhân vật nhỏ trong khung — tạo sự kính sợ và bình yên | `wide shot, small figure in vast setting` |

### Quy tắc bắt buộc (Mandatory Rules)

1. **Mỗi 5 prompt liên tiếp** phải có ít nhất 1 prompt với negative space ≥50%
2. **Không bao giờ** mô tả >3 objects riêng biệt trong cùng 1 prompt nếu không phải Still Life
3. **Intro và Outro** phải có ≥70% prompts là Wide hoặc Negative Space compositions
4. **Character Action shots**: nhân vật phải có ít nhất 1/3 frame trống xung quanh — không bị objects kẹp 2 bên
5. **Tránh danh sách objects dài** trong prompt — nhiều objects trong prompt = ảnh bí

### Prompt Language Chuẩn (Bắt buộc thêm vào mọi prompt)

```
open and airy composition, generous negative space, single clear focal point, uncluttered background
```

### Ví dụ So sánh

**❌ Bí / Cluttered:**
```
An elderly man sitting at a kitchen table surrounded by copper pots, a stack of books, three ceramic mugs, a wooden box, scattered papers, hanging herbs, and a steaming pot on the stove nearby
```

**✅ Thoáng / Airy:**
```
An elderly man sitting quietly at a plain wooden table, a single ceramic mug of tea beside him, open and airy composition, generous negative space, soft morning light streaming through a half-open window, uncluttered background
```

### Revision Rule

Khi Boss nói **"thoáng hơn"**, **"bớt đồ"**, **"nhìn mệt mắt quá"**, **"bí quá"**:
1. Xóa tất cả objects trong prompt, chỉ giữ lại 1-2 objects quan trọng nhất
2. Thêm `open and airy composition, generous negative space, single clear focal point, uncluttered background`
3. Đổi sang wide shot hoặc negative space composition
4. Thêm environmental openness: `open sky`, `empty field`, `clean floor`, `vast corridor`

*V7.1 — Cập nhật: Thêm Open & Airy Doctrine*
