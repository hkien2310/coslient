# Visual Style Module: Old World European Claymation

> **Style ID:** `old_world_claymation`
> **Status:** 🟢 Active
> **Version:** 1.0
> **Nguồn gốc:** Được xây dựng từ reference images thực tế — không phải lý thuyết
> **Dùng cho:** Khi Boss chỉ định style này thay vì `warm_storybook`

---

## Cách sử dụng file này

File này chứa toàn bộ DNA thị giác cho **Old World European Claymation**. Agent đọc file này tại Stage 4.1 để load phong cách hình ảnh.

Style này **khác biệt hoàn toàn** với `warm_storybook`:
- `warm_storybook` = mịn màng, sứ trắng, healing, ấm áp nhẹ nhàng
- `old_world_claymation` = clay puppet mịn đẹp với khuôn mặt character-driven, literary, melancholic-tender, làng đá cổ Châu Âu

> [!CAUTION]
> **NGUY CƠ DRIFT SỐ 1: GOBLIN/TROLL/CREATURE.** Các keyword như "textured clay skin", "hooked nose", "large protruding ears", "visible wrinkles" nếu dùng sai sẽ khiến AI tạo ra quái vật. **Exaggeration trong style này nằm ở HÌNH DẠNG, không phải BỀ MẶT DA.** Da phải mịn, sạch như clay puppet chuyên nghiệp — không phải da cóc, da rắn, da goblin.

---

## 1. Style Identity & Feel

### Tên phong cách
**Old World European Claymation — Village Puppet Cinema**

### Hình ảnh nên cảm nhận như:

- stop-motion puppet film từ một xưởng phim Châu Âu độc lập
- thế giới nhỏ bé nhưng emotionally vast
- nhân vật được nặn bằng đất sét có hồn — từng nếp nhăn là một câu chuyện
- bối cảnh đá cổ Mediterranean / Đông Âu — sờn mòn, cũ kỹ, nhưng được yêu thương
- lighting theatrical: amber ấm bên trong ↔ xám lạnh bên ngoài
- melancholic nhưng không tuyệt vọng — "một cuộc đời đã sống trọn vẹn"
- cinematic như phim hoạt hình nghệ thuật Châu Âu — có chiều sâu văn học
- artisanal: mọi thứ trông như được làm bằng tay thật sự

### Người xem nên cảm thấy:

- bất ngờ vì nó đẹp theo cách không ngờ tới
- connected với một nhân vật lạ nhưng quen
- nostalgia cho một thế giới chưa bao giờ tồn tại nhưng cảm thấy thật
- wonder — kiểu wonder của người lớn, không phải trẻ con

### Hình ảnh KHÔNG được cảm nhận như:

- chibi hay cute anime (tuyệt đối không)
- warm_storybook (mịn, sứ, kem mật ong)
- **goblin, troll, creature, monster, fantasy creature** ← ĐÂY LÀ NGUY CƠ DRIFT SỐ 1
- dark fantasy hay gothic horror
- glossy 3D animation (Pixar-like)
- rough matted fibrous creature skin
- plastic toy photography
- đơn giản hoặc generic

---

## 2. Style Anchors

### Full style anchor (dùng cho prompt > 500 ký tự)

```
stop-motion claymation puppet, handcrafted European village cinema, macro photography, tilt-shift lens, kind and expressive elderly human face with a long aquiline nose and large ears, smooth matte clay puppet skin (clean surface, not rough or fibrous), warm beige clay tone, soft natural character lines around the eyes and mouth (not horror wrinkles), wild wispy silver-white hair, warm gentle eyes with depth and life, realistic adult human body proportions with correct head-to-body ratio, long expressive fingers, chunky knit wool sweater or worn tweed coat, aged stone Mediterranean village setting, cobblestone streets, warm amber lantern glow against cool blue-gray stone, terracotta orange accent object, felted wool sheep companion, rich cinematic depth of field, 16:9
```

### Short style anchor (dùng cho prompt ngắn hơn)

```
stop-motion claymation puppet, European village cinema, macro photography, tilt-shift lens, kind expressive elderly human face, long aquiline nose, smooth matte clay skin, soft character lines, warm gentle eyes, realistic adult proportions, wild white hair, tweed or knit clothing, stone village setting, amber lantern warm glow, terracotta orange accent, 16:9
```

### Negative style anchor (dùng khi model bị drift)

```
avoid goblin, avoid troll, avoid creature, avoid monster, avoid fantasy creature, avoid rough matted fibrous skin, avoid horror creature face, avoid grotesque, avoid chibi, avoid oversized head, avoid oversized cute eyes, avoid smooth porcelain skin, avoid warm_storybook aesthetic, avoid plastic shine, avoid glossy 3D, avoid Pixar-style smooth animation, avoid flat clean architecture, avoid healing-cozy pastel palette, avoid cream honey gold color palette, avoid children no kids, avoid magical floating elements, avoid text handwriting
```

---

## 3. So sánh với warm_storybook (BẮT BUỘC đọc)

> [!IMPORTANT]
> Hai style này là đối cực nhau. Đừng trộn lẫn keyword của chúng.

| Yếu tố | `warm_storybook` | `old_world_claymation` |
|--------|-----------------|----------------------|
| **Da nhân vật** | Smooth matte porcelain skin | **Smooth matte clay skin** — sạch, không fibrous, không rough |
| **Nếp nhăn** | Chỉ laugh lines nhẹ | Soft character lines — có thể sâu hơn nhưng **không horror** |
| **Bàn tay** | Clean elegant elderly hands | Long expressive fingers, matte clay — **không claw-like** |
| **Khuôn mặt** | Balanced, clean | Shape-exaggerated (mũi dài, tai to) nhưng **HUMAN và KIND** |
| **Tóc** | Fluffy needle-felted wool hair | Wild wispy white hair — **không matted/fibrous** |
| **Palette** | Cream, honey-gold, amber | Stone gray, dusty olive, terracotta orange |
| **Kiến trúc** | Cozy kitchens, warm interiors | Weathered stone village, cobblestone streets |
| **Lighting** | Soft warm daylight | Strong amber/cool contrast |
| **Mood** | Healing, welcoming, gentle | Literary, melancholic-tender — **NOT horror or dark** |
| **Sheep** | Soft felted props (nếu có) | COMPANION MOTIF xuyên suốt |

---

## 4. Character Design

### Nguyên tắc cốt lõi

> [!IMPORTANT]
> **Proportion Lock:** Nhân vật phải có tỉ lệ người thật. Đầu chiếm 1/6 đến 1/7 chiều cao cơ thể. Thân dài, chân dài, dáng hơi còng theo tuổi. **TUYỆT ĐỐI KHÔNG chibi, không đầu to, không mắt anime oversized.**

### Khuôn mặt — Quy tắc VÀNG: SHAPE exaggeration, SURFACE clean

> [!IMPORTANT]
> **Exaggeration nằm ở HÌNH DẠNG — không phải BỀ MẶT DA.** Mũi dài thì được, nhưng da mũi phải mịn. Tai to thì được, nhưng da tai phải clean. Khuôn mặt phải trông như một NGƯỜI THẬT ĐÃ GIÀ đẹp lão, được nặn bằng clay — không phải goblin, không phải troll, không phải sinh vật fantasy.

- **Mũi:** Dài và aquiline (mũi cao, sống mũi rõ) — đây là signature. **KHÔNG phải mũi khoằm quái dị như phù thủy.**
- **Tai:** To, hơi nhô ra — **da tai mịn, KHÔNG có sợi lông xù xì.**
- **Mắt:** Sâu, ấm, có soul — `warm gentle eyes with depth and kindness`. **Không oversized, không anime.**
- **Trán:** Cao, forehead rõ — character nhưng không quái.
- **Nếp nhăn:** Soft character lines — **chỉ quanh mắt và khóe miệng, như người già đẹp lão thật sự.** KHÔNG phải wrinkles trên toàn bộ da mặt theo kiểu horror.
- **Râu:** Stubble ngắn nhẹ hoặc râu bạc thưa — optional.
- **Biểu cảm:** `kind, thoughtful, melancholic-tender` — KHÔNG bao giờ là expressionless hay menacing.

### Da nhân vật — SMOOTH MATTE CLAY (BẮT BUỘC)

> [!CAUTION]
> **Da PHẢI MỊN.** Đây là điểm bị hiểu sai nhiều nhất. Reference images có da nhân vật khá mịn và sạch như clay puppet chuyên nghiệp. KHÔNG phải da thô ráp, fibrous, matted, hay rough như creature/monster.

- **Chất liệu:** `smooth matte clay puppet skin` — mịn, sạch, matte (không bóng)
- **Màu:** Warm beige clay — `warm beige clay tone, slightly aged` — không quá trắng sứ, không quá nâu
- **Bề mặt:** SMOOTH với gentle aging — `smooth clay surface with soft natural aging, not rough or fibrous`
- **Tuyệt đối TRÁNH:** rough texture, fibrous surface, matted skin, creature skin, monster texture

**Keyword đúng cho da:** `smooth matte clay puppet skin, warm beige clay tone, clean puppet surface with gentle aging quality, not rough not fibrous`

**Keyword SAI (gây drift goblin):** `textured clay skin`, `visible pores`, `rough surface`, `organic surface variation`

### Tóc — Đặc điểm bắt buộc

- **Màu chủ đạo:** Silver-white, wispy white
- **Kiểu:** Wild, fluffy, natural — tóc bồng tự nhiên, không sculpted cứng
- **Chất liệu:** Trông như tóc người thật (fine strands) hoặc sợi mỏng nhẹ được tạo hình
- **TRÁNH tuyệt đối:** Matted hair, fibrous clumped hair, hay tóc trông như rơm/cỏ khô — đây là nguyên nhân chính gây creature drift

**Keyword đúng:** `wild wispy silver-white hair, natural fluffy strands, fine hair texture`

**Keyword SAI:** `matted hair`, `fibrous hair`, `straw-like hair`, `rough hair texture`

### Bàn tay — Storytelling device

- Dài, ngón biểu cảm, hơi cong tự nhiên theo tuổi
- **Smooth matte clay** — có aging quality nhưng KHÔNG claw-like, KHÔNG horror
- Dùng cho close-up gesture shots: cầm đồ vật, chạm cừu, rót trà

**Keyword đúng:** `long expressive elderly puppet hands, smooth matte clay, gentle aged fingers, natural puppet hand pose`

**Keyword SAI:** `claw-like fingers`, `deeply wrinkled hands`, `rough aged texture`, `gnarled hands`

### Trang phục — Vintage European Village Artisan

**Ưu tiên hàng đầu:**
- Chunky knit wool sweater (đan thô, rõ vân, màu trung tính xám/nâu/olive)
- Worn tweed coat (houndstooth hoặc herringbone, màu charcoal/dark gray/brown)
- Flat cap (tweed, herringbone) — đây là headwear signature
- Sage green beret (beret thợ thủ công)
- Dungarees / overalls (vải canvas thô, màu olive/beige)
- Scarf (len đan thô, thường màu terracotta cam đất đỏ)

**Trang phục TRÁNH:**
- Clean modern clothes
- Anything too fancy or pristine
- Warm_storybook-style smooth fabric

### Companion Motif — Cừu len nỉ (Felted Wool Sheep)

> [!NOTE]
> Cừu là companion motif lặp lại của style này. Không bắt buộc xuất hiện trong mọi cảnh, nhưng khi có mặt phải đúng spec:

- `small felted wool sheep with dense curly cream-white wool coat, small black stick legs, tiny black bead eyes, stop-motion puppet scale`
- Cừu nhỏ hơn nhân vật đáng kể — scale miniature
- Thường 2-5 con trong cảnh ngoài trời, 1 con trong cảnh trong nhà (như thú cưng/bạn đồng hành)
- Không phải magical — chỉ đơn giản là có mặt, như thú cưng thật

---

## 5. Material Palette

### Vật liệu thế giới — Rough & Lived-In

Mọi thứ trong thế giới này trông như đã được dùng nhiều năm:

**Đá & Xây dựng:**
- Rough limestone blocks với rõ joint mortar
- Aged plaster tường (peeling, stained, weathered)
- Cobblestone đường (smooth from centuries of foot traffic)
- Stone steps (worn uneven)

**Gỗ:**
- Rough-hewn weathered wood — grain rõ, khoang mắt gỗ, cracked
- Aged wooden doors (teal-blue hoặc gray-blue, peeling paint)
- Old wooden furniture (chairs, tables, shelves)

**Vải & Sợi:**
- Chunky tweed and knit textures — visible individual fibers
- Burlap và canvas thô
- Plaid cloth (plaid tablecloth)
- Felted wool (cho cừu)

**Kim loại & Gốm:**
- **Enamel objects (orange) — signature:** kettle, mailbox, lamp shade
- Aged cast iron
- Hand-blown glass jars
- Ceramic cups (mismatched, simple, cream-white)

### Cảm giác vật liệu đúng

**Thế giới (đá, gỗ, vải):** rough, tactile, aged, organic, handmade, imperfect, well-loved
**Nhân vật (da, tóc, tay):** smooth matte clay puppet quality — sạch, có character nhưng KHÔNG rough/fibrous/creature-like

> [!IMPORTANT]
> **Phân biệt rõ:** World materials (đá, gỗ, vải) = rough và textured. Character skin = smooth matte clay. Đừng để texture của thế giới "lây" sang da nhân vật.

---

## 6. Color DNA

### Bảng màu nền (Base Palette)

- **Stone gray:** #8A8A80 — tường đá, đường phố, nền bầu trời
- **Dusty limestone:** #C4B99A — tường thô, nền đất
- **Aged clay beige:** #D4C4A0 — skin tone nhân vật
- **Dusty olive:** #7A8A60 — quần áo, cây cối
- **Charcoal tweed:** #4A4040 — áo khoác, cap
- **Warm shadow brown:** #5A4030 — bóng tối ấm

### Accent Màu — Bắt buộc

**Primary Accent: TERRACOTTA ORANGE / RUST ORANGE** 🔶
- Đây là chữ ký màu sắc quan trọng nhất của style
- Xuất hiện trong: scarves, backpacks, enamel kettles, mailboxes, hats, mushrooms
- Tone: `terracotta orange`, `rust red`, `burnt sienna`, `clay orange`
- KHÔNG phải orange tươi — phải muted, dusty, aged

**Secondary Accent: SAGE GREEN / DUSTY GREEN** 🌿
- Xuất hiện trong: berets, plant pots, weathered doors, moss on stone
- Tone: `dusty sage green`, `muted olive green`, `aged verdigris`

### Lighting Colors

- **Interior warm:** `deep amber`, `honey lamp glow`, `warm orange candlelight`
- **Exterior cool:** `cool blue-gray daylight`, `slate sky`, `muted overcast Mediterranean`
- **Golden hour:** `deep burnt orange sunset casting long shadows across stone`

### Tránh

- Cream và honey-gold của warm_storybook
- Pastel colors
- Neon hoặc high-saturation colors
- Cold blue tones (ngoại trừ exterior daylight)
- Black là fine cho bóng — không phải flat pitch-black

---

## 7. Lighting DNA

### Quy tắc Lighting cốt lõi

> [!IMPORTANT]
> **Warm/Cool Contrast là defining characteristic của style này.** Mọi cảnh phải có sự tương phản rõ ràng giữa nguồn sáng ấm (amber) và không khí lạnh (stone gray blue). Đây là điều tạo nên chiều sâu cinematic.

### Cảnh ngoài trời — Ban ngày

- `cool overcast Mediterranean daylight, soft blue-gray ambient light on stone surfaces, dusty atmospheric haze`
- Không phải gloomy — chỉ là "ngày trong làng đá cũ, trời mây nhẹ"
- Ánh sáng chiều: `warm golden hour sunset casting long amber shadows across cobblestone`

### Cảnh ngoài trời — Chiều tối / Đêm

- `warm amber lantern light mounted on stone wall, glowing against cool blue dusk`
- `soft teal-blue door illuminated by a single warm lantern, golden amber pool of light on cobblestone below`

### Cảnh trong nhà — Ban ngày

- Ánh sáng từ cửa sổ nhỏ: `cool daylight shaft through small stone window, warm amber cast from lamp`
- Workshop: `single overhead amber bulb casting warm cone of light, tools in warm shadow`

### Cảnh trong nhà — Buổi tối / Ấm cúng

- `warm amber table lamp with fabric shade, deep honey glow filling stone cottage interior`
- `fireplace glow, warm orange embers, dramatic warm/cool split on character's face`

### Không bao giờ dùng

- Flat uniform lighting
- Harsh studio lighting
- Cold fluorescent / cool white light
- Pitch-black darkness với không có detail

---

## 8. World Logic

### Bối cảnh mặc định

**Exterior:**
- Làng đá cổ Mediterranean / Đông Âu
- Cobblestone streets và stone steps (uneven, worn)
- Stone walls (rough limestone blocks)
- Aged wooden doors (teal-blue, gray-blue, peeling)
- Narrow alleys with atmospheric depth
- Stone archways và doorways
- Gas lanterns mounted on walls
- Stone courtyards với pots, benches, clotheslines

**Interior:**
- Stone cottage với low ceilings
- Rough stone walls, simple wooden furniture
- Workshop với tools và workbench
- Rustic kitchen với stone fireplace
- Market stall (covered, wooden structure)
- Bedroom với aged textiles

### Cảm giác thế giới

old, lived-in, slightly worn, full of character, every surface tells a story, imperfect but beautiful

### Tránh

- Modern architecture
- Clean interiors
- Fantasy/magical kingdoms
- Generic suburban settings
- Warm_storybook-style cozy kitchens (tránh overlap)
- Bright open spaces

---

## 9. Props Vocabulary

Props là storytelling devices trong style này. Mỗi prop mang lịch sử.

### Props Signature (Xuất hiện nhiều nhất trong reference)

| Prop | Mô tả | Màu |
|------|--------|-----|
| **Enamel kettle** | Vừa, hình tròn, có tay cầm | Orange/terracotta — signature |
| **Flat cap** | Tweed, herringbone, slightly worn | Charcoal gray, dark brown |
| **Walking stick/cane** | Gỗ thô, hơi cong tự nhiên | Dark brown wood |
| **Vintage radio** | Wooden cabinet, fabric speaker grill | Warm brown wood |
| **Glass jars** | Hand-blown, mismatched | Amber, clear |
| **Woven backpack/basket** | Rattan hoặc woven fiber | Terracotta orange |
| **Mismatched teacups** | Ceramic, simple, cream-white | Cream white |
| **Wooden crates** | Rough slat wood | Weathered brown |
| **Clothespins** | Simple wooden pegs | Natural wood |
| **Stone mailbox/post box** | Mounted on wall hoặc freestanding | Terracotta orange |
| **Vintage bellows camera** | Leather and metal | Dark brown/black |
| **Knit hats** | Pom-pom, ribbed | Terracotta orange, cream, gray |

### Props TRÁNH

- Modern objects
- Clean or new-looking items
- Magical objects
- Floating elements
- Text/handwriting trên objects

---

## 10. Emotional Doctrine

### Trung tâm cảm xúc

wonder, philosophical melancholy, quiet tenderness, the weight and beauty of a life fully lived, connection between beings (man and sheep, man and stranger), solitary dignity

### Cảm giác khung hình

someone has been walking these stones for 60 years and still notices one beautiful mushroom, two old men share a bench and nothing needs to be said, a small gesture of care is more meaningful than any grand statement

### Khác với warm_storybook

- **warm_storybook:** "someone is still loved, someone is remembered"
- **old_world_claymation:** "someone is still curious, still noticing, still here — and that itself is enough"

### Khi chủ đề buồn

Buồn được phép ở đây — nhưng không bi thảm. Như một nhân vật ngồi một mình trước tách trà nguội, nhìn ra cửa sổ. Buồn như trong văn học.

---

## 11. Composition & Camera

### Tilt-shift / Depth of Field

- **BẮT BUỘC:** Tilt-shift effect tạo ra miniature world feeling
- Foreground objects thường bị blur nhẹ
- Background always atmospheric blur
- Sharp focus vào nhân vật (mid-ground) hoặc một object cụ thể

### Composition Rules

**3 lớp không gian:**
1. Foreground: một object gần camera (cừu, tảng đá, cái cốc, nấm)
2. Mid: nhân vật — đây là điểm focus chính
3. Background: kiến trúc đá blur, atmospheric haze

**Shot sizes được dùng nhiều:**
- **Wide shot:** Nhân vật trong bối cảnh làng (nhân vật nhỏ trong không gian lớn)
- **Medium shot:** Từ đầu đến đùi, thấy full upper body và gesture
- **Close-up:** Khuôn mặt (thấy rõ clay texture và expression)
- **Extreme close-up:** Bàn tay + object (cầm nấm, rót trà, chạm cừu)

**Framing techniques:**
- `seen through a stone archway`
- `framed by aged wooden doorframe`
- `camera low, looking up slightly at character against sky`
- `seen from across a narrow cobblestone alley`

---

## 12. Prompt Templates

### Full template

```
[scene + subject + emotional action], [shot size / composition], [one specific grounded physical detail — light, gesture, or object], stop-motion claymation puppet, handcrafted European village cinema, macro photography, tilt-shift lens, kind expressive elderly human face with a long aquiline nose and large ears, smooth matte clay puppet skin with warm beige clay tone, warm gentle eyes with depth and life, soft natural character lines around eyes and mouth, wild wispy silver-white hair with fine natural strands, realistic adult human body proportions with correct head-to-body ratio, long expressive elderly puppet hands, [clothing from vintage European artisan wardrobe], [one terracotta orange accent object], [stone village setting detail], [lighting: warm amber interior OR golden hour sunset OR cool overcast exterior], rich cinematic depth of field with atmospheric background blur, 16:9, avoid goblin, avoid troll, avoid creature, avoid rough matted skin, avoid horror face, avoid chibi, avoid glossy 3D, no text no handwriting no magical elements, no children
```

### Compressed template

```
[scene + subject + action], [shot size], stop-motion claymation puppet, European village cinema, tilt-shift macro, kind expressive elderly human face, long aquiline nose, smooth matte clay skin, warm gentle eyes, wild wispy white hair, realistic adult proportions, chunky knit or tweed clothing, [terracotta orange accent], stone village cobblestone setting, warm amber lantern against cool stone, cinematic depth of field, 16:9, avoid goblin avoid troll avoid creature, avoid chibi, no children
```

### Dynamic template chuẩn hóa

```
[Chủ thể + Hành động theo concept], [Góc máy & Bố cục — framing qua arch/door/alley], [Một chi tiết vật lý cụ thể — ánh sáng, cử chỉ, đồ vật], [Props cụ thể theo kịch bản], stop-motion claymation puppet, handcrafted European village cinema, macro photography, tilt-shift lens, kind and expressive elderly human face with a long aquiline nose and large ears, smooth matte clay puppet skin with warm beige clay tone (not rough not fibrous), warm gentle eyes with depth, soft natural character lines (not horror wrinkles), wild wispy silver-white hair with fine natural strands, realistic adult human body proportions with correct head-to-body ratio, long expressive elderly puppet hands, [trang phục vintage artisan: chunky knit sweater / worn tweed coat / flat cap / sage green beret], [terracotta orange accent object cụ thể], [stone village bối cảnh cụ thể], [lighting contrast: warm amber source + cool stone ambient], rich cinematic depth of field, 16:9, avoid goblin, avoid troll, avoid creature, avoid rough matted fibrous skin, avoid horror wrinkles, avoid chibi, avoid oversized head, avoid glossy 3D, no text no handwriting, no children
```

### Example prompts (đã được sửa để tránh creature drift)

**Ví dụ 1 — Shepherd on stone steps:**
```
An elderly village shepherd hunched gently forward climbing ancient stone steps, wide shot from side profile, small felted wool sheep walking alongside him at his feet, woven terracotta-orange backpack strapped to his back, walking stick in hand, stop-motion claymation puppet, handcrafted European village cinema, macro photography, tilt-shift lens, kind expressive elderly human face with long aquiline nose, smooth matte clay puppet skin with warm beige clay tone, warm gentle eyes, wild wispy white hair with fine natural strands, realistic adult body proportions, chunky sage-green knit jacket and olive trousers, rough stone village steps with Mediterranean stone buildings blurred in background, cool overcast blue-gray daylight, cinematic atmospheric depth, 16:9, avoid goblin, avoid troll, avoid creature, avoid rough matted skin, avoid chibi, no text
```

**Ví dụ 2 — Indoor tea scene:**
```
An elderly man sitting at a rustic wooden table pouring tea from a terracotta orange enamel kettle, medium shot from slight side angle, steam rising gently from a ceramic cup, a small felted wool sheep resting quietly on the table beside him, a vintage wooden radio glowing amber in the background, stop-motion claymation puppet, handcrafted European village cinema, tilt-shift macro, kind expressive elderly human face with long aquiline nose and large ears, smooth matte clay puppet skin, warm gentle eyes with quiet contemplation, soft natural character lines, wild wispy white hair, worn dark tweed jacket, rough stone cottage interior, deep warm amber lamp light, 16:9, avoid goblin, avoid creature, avoid rough matted skin, avoid chibi, no text
```

**Ví dụ 3 — Sunset shepherd with lantern:**
```
An elderly shepherd bending gently to pet a small sheep on a cobblestone street at dusk, medium shot, a warm amber lantern glowing on the stone wall beside a weathered teal-blue wooden door, stop-motion claymation puppet, handcrafted European village cinema, tilt-shift macro, kind melancholic elderly human face with long aquiline nose, smooth matte clay puppet skin, warm eyes catching the lantern light, wild wispy white hair, dark tweed coat and gray flat cap, cobblestone street with blurred flock of sheep in background, deep golden hour sunset casting warm orange light against cool stone walls, cinematic depth of field, 16:9, avoid goblin, avoid creature, avoid rough skin, avoid chibi
```

---

## 13. Words to Prefer / Avoid

### Dùng nhiều ✅

stop-motion claymation puppet, handcrafted European village cinema, macro photography, tilt-shift lens, **smooth matte clay puppet skin**, warm beige clay tone, **kind expressive elderly human face**, **long aquiline nose**, large ears, **warm gentle eyes with depth and life**, soft natural character lines, **wild wispy silver-white hair with fine natural strands**, realistic adult body proportions, correct head-to-body ratio, long expressive elderly puppet hands, chunky knit wool sweater, worn tweed coat, flat cap, sage green beret, woven backpack, felted wool sheep, cobblestone street, weathered stone wall, aged wooden door (teal-blue), warm amber lantern, terracotta orange enamel kettle, vintage radio, mismatched ceramic teacups, stone cottage interior, atmospheric blur, cinematic depth of field, warm/cool lighting contrast, golden hour sunset over stone village

### Tránh hoặc không bao giờ dùng ❌

**goblin, troll, creature, monster, fantasy creature** (nguy cơ drift #1), **rough matted fibrous skin, horror wrinkles, claw-like hands, creature face**, textured clay skin (dễ gây creature drift — dùng "smooth matte clay" thay thế), prominent hooked nose (dùng "long aquiline nose" thay thế), large protruding ears (dùng "large ears" thay thế), chibi, oversized head, oversized cute eyes, anime proportions, smooth porcelain skin (quá warm_storybook), cream honey gold palette, healing cozy atmosphere, pitch-black darkness, magical elements, floating objects, text, handwriting, children, kids, Pixar-style, glossy 3D, modern architecture, clean interiors

---

## 14. Style Fingerprint (Compact Summary)

Old World European Claymation village world — **kind, melancholic, human**. Characters are stop-motion clay puppets with **realistic adult proportions** (never chibi), shaped-exaggerated faces (**long aquiline nose, large ears, wild white hair**) but **smooth matte clay puppet skin** — like a master puppet maker's finest work, NOT a goblin, NOT a troll. Faces are **warm, human, and emotionally readable**. World is weathered Mediterranean stone — cobblestone streets, aged teal-blue wooden doors, narrow atmospheric alleys. **Terracotta orange** is the signature accent (enamel kettle, scarves, backpacks). **Felted wool sheep** are the companion motif. Lighting: **warm amber interior / lantern glow vs cool blue-gray stone exterior**. Mood: literary, melancholic-tender — "a life fully lived, observed with love." **No goblin. No creature. No chibi. No horror wrinkles. No magical elements. No children.**

---

## 15. Revision Behavior (Style-Specific)

| Boss nói | Sửa |
|----------|-----|
| **Nhân vật trông như goblin / troll / creature** | **SỬA NGAY — ĐÂY LÀ DRIFT NGUY HIỂM NHẤT:** Xóa toàn bộ `textured clay skin`, `hooked nose`, `protruding ears`, `visible wrinkles`. Thay bằng: `kind expressive elderly human face, smooth matte clay puppet skin with warm beige clay tone, long aquiline nose, large ears, warm gentle eyes`. Thêm negative: `avoid goblin, avoid troll, avoid creature, avoid rough matted fibrous skin, avoid horror face`. |
| **Da quá rough / fibrous / thô** | Thay `textured clay skin` bằng `smooth matte clay puppet skin, warm beige clay tone, clean puppet surface with gentle aging quality`. Thêm negative: `avoid rough texture, avoid fibrous skin, avoid matted surface`. |
| **Tóc trông như rơm / matted** | Thay bằng `wild wispy silver-white hair with fine natural strands, fluffy and light`. Thêm negative: `avoid matted hair, avoid fibrous clumped hair, avoid straw-like texture`. |
| **Nhân vật bị chibi / đầu to** | Thêm `realistic adult body proportions, correct head-to-body ratio, elongated adult figure`. Negative: `avoid chibi, avoid oversized head`. |
| **Khuôn mặt thiếu character** | Thêm `long aquiline nose with strong profile, large expressive ears, warm deep-set eyes, melancholic kind expression, strong character silhouette`. KHÔNG thêm `hooked nose` hay `protruding ears` vì sẽ gây creature drift. |
| **Thiếu terracotta orange** | Thêm 1 orange accent object: `terracotta orange enamel kettle`, `rust-orange woven scarf`, `terracotta-orange woven backpack`. |
| **Lighting quá phẳng** | Thêm: `warm amber lantern glow against cool blue-gray stone`, `deep amber interior vs cool stone exterior daylight`. |
| **Thiếu cừu** | Thêm: `small felted wool sheep with dense curly cream-white wool coat, small black stick legs, stop-motion puppet scale`. |
| **Bối cảnh không đúng** | Thêm: `weathered stone Mediterranean village, cobblestone street, aged limestone walls, teal-blue wooden door, stone archway`. |
| **Quá dark / horror** | Thêm: `melancholic but tender atmosphere, kind human expression, warm amber light source, not dark or threatening`. |
| **Ảnh phẳng / no depth** | Thêm 3 lớp: foreground prop + mid character + background stone blur. Thêm `cinematic depth of field, tilt-shift atmospheric perspective`. |
