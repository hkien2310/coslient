# Visual Style Module: Old World European Stop-Motion Puppet

> **Style ID:** `old_world_claymation`
> **Status:** 🟢 Active
> **Version:** 2.0
> **Nguồn gốc:** Được xây dựng từ reference images thực tế — không phải lý thuyết
> **Dùng cho:** Khi Boss chỉ định style này thay vì `warm_storybook`

---

## Cách sử dụng file này

File này chứa toàn bộ DNA thị giác cho **Old World European Stop-Motion Puppet**. Agent đọc file này tại Stage 4.1 để load phong cách hình ảnh.

Style này **khác biệt hoàn toàn** với `warm_storybook`:
- `warm_storybook` = mịn màng, sứ trắng, healing, ấm áp nhẹ nhàng
- `old_world_claymation` = clay puppet mịn đẹp, nhân vật hiền hậu đẹp lão, làng đá cổ Châu Âu, melancholic-tender

> [!CAUTION]
> **NGUY CƠ DRIFT SỐ 1: GOBLIN/TROLL/CREATURE.** Tuyệt đối KHÔNG dùng các keyword exaggerated cho khuôn mặt (mũi khoằm, tai to, nếp nhăn sâu). Nhân vật phải là một người ông đẹp lão, hiền hậu, được nặn bằng clay — không phải sinh vật fantasy.

---

## 1. Style Identity & Feel

### Tên phong cách
**Old World European Stop-Motion Puppet — Village Puppet Cinema**

### Hình ảnh nên cảm nhận như:

- stop-motion puppet film từ một xưởng phim Châu Âu độc lập
- thế giới nhỏ bé nhưng emotionally vast
- nhân vật được nặn bằng clay có hồn — hiền hậu, đẹp lão, ấm áp
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
- **goblin, troll, creature, monster** ← ĐÂY LÀ NGUY CƠ DRIFT SỐ 1
- dark fantasy hay gothic horror
- rough matted fibrous creature skin
- glossy 3D animation (Pixar-like)
- đơn giản hoặc generic

---

## 2. Style Anchors

### Full style anchor (dùng cho prompt > 500 ký tự)

```
Laika-style stop-motion puppet, handcrafted European village cinema, macro photography, tilt-shift lens, [CHARACTER: kind naturally beautiful [age/gender per story] human face, warm gentle eyes, [expression per story]], warm soft silicone puppet skin with warm natural skin tone, naturally soft fine hair with gentle movement and clean silhouette, realistic human body proportions with correct head-to-body ratio, long gentle expressive hands, [clothing per story and setting], aged stone Mediterranean village setting, cobblestone streets, warm amber lantern glow against cool blue-gray stone, terracotta orange accent object, felted wool sheep companion, rich cinematic depth of field, 16:9
```

### Short style anchor (dùng cho prompt ngắn hơn)

```
Laika-style stop-motion puppet, European village cinema, tilt-shift macro, [CHARACTER per story], warm soft silicone puppet skin, warm natural skin tone, naturally soft fine hair with clean silhouette, realistic human proportions, [clothing per story], stone village cobblestone setting, warm amber lantern against cool stone, cinematic depth of field, 16:9
```

### Negative style anchor (dùng khi model bị drift)

```
avoid goblin, avoid troll, avoid creature, avoid monster, avoid exaggerated nose, avoid oversized ears, avoid grotesque features, avoid rough matted fibrous skin, avoid horror creature face, avoid chibi, avoid oversized head, avoid oversized cute eyes, avoid smooth porcelain skin, avoid warm_storybook aesthetic, avoid plastic shine, avoid glossy 3D, avoid Pixar-style smooth animation, avoid flat clean architecture, avoid healing-cozy pastel palette, avoid cream honey gold color palette, avoid children no kids, avoid magical floating elements, avoid text handwriting
```

---

## 3. So sánh với warm_storybook (BẮT BUỘC đọc)

> [!IMPORTANT]
> Hai style này là đối cực nhau. Đừng trộn lẫn keyword của chúng.

| Yếu tố | `warm_storybook` | `old_world_claymation` |
|--------|-----------------|----------------------|
| **Da nhân vật** | Smooth matte porcelain skin | Smooth matte clay skin — warm beige, natural, aged beautifully |
| **Nếp nhăn** | Chỉ laugh lines nhẹ | Soft laugh lines — đẹp lão, không horror |
| **Bàn tay** | Clean elegant elderly hands | Long gentle expressive hands — có warmth |
| **Khuôn mặt** | Balanced, clean | **Đẹp lão tự nhiên** — có chiều sâu, hiền hậu |
| **Tóc** | Fluffy needle-felted wool hair | Naturally soft fine hair, clean silhouette, theo nhân vật |
| **Palette** | Cream, honey-gold, amber | Stone gray, dusty olive, terracotta orange |
| **Kiến trúc** | Cozy kitchens, warm interiors | Weathered stone village, cobblestone streets |
| **Lighting** | Soft warm daylight | Strong amber/cool contrast |
| **Mood** | Healing, welcoming, gentle | Literary, melancholic-tender — NOT horror or dark |
| **Sheep** | Soft felted props (nếu có) | COMPANION MOTIF xuyên suốt |

---

## 4. Character Design

### Nguyên tắc cốt lõi

> [!IMPORTANT]
> **Proportion Lock:** Nhân vật phải có tỉ lệ người thật. Đầu chiếm 1/6 đến 1/7 chiều cao cơ thể. **TUYỆT ĐỐI KHÔNG chibi, không đầu to, không mắt anime oversized.**

### Khuôn mặt — THEO NHÂN VẬT của câu chuyện

> [!IMPORTANT]
> **Nhân vật KHÔNG bị khóa ở độ tuổi hay giới tính nào.** Tuổi, giới tính, biểu cảm — tất cả theo concept và story. Style chỉ định nghĩa CHẤT LƯỢNG của puppet (Laika-style, silicone skin, warm eyes) — không định nghĩa nhân vật cụ thể.

**Công thức mặt theo story:**
- `[tuổi: young / middle-aged / elderly] [giới tính: man / woman / person]`
- `kind naturally beautiful [age] [gender] face` — luôn giữ "kind" và "naturally beautiful"
- **Mắt:** `warm gentle eyes` — không oversized, không anime, luôn có soul
- **Mũi, tai:** Tự nhiên, proportional — **không exaggerated**
- **Nếp nhăn:** Phù hợp với độ tuổi nhân vật — không horror, không quá sâu
- **Biểu cảm:** Theo cảm xúc của scene — `thoughtful`, `melancholic`, `peaceful`, `determined`, `tender`

**Keyword đúng:** `kind naturally beautiful [age+gender] face, warm gentle eyes, [expression per scene], warm soft silicone puppet skin`

**Keyword SAI — tuyệt đối không dùng:** `hooked nose`, `large protruding ears`, `exaggerated features`, `visible wrinkles`, `creature`, `goblin`, `horror`

### Da nhân vật — WARM SOFT SILICONE PUPPET SKIN (BẮT BUỘC)

- **Chất liệu:** `warm soft silicone puppet skin` — mịn, ấm, matte (không bóng, không plastic)
- **Màu:** `warm natural skin tone` — theo độ tuổi nhân vật, không quá trắng sứ
- **Bề mặt:** Smooth, ấm, có hơi thở — `clean warm puppet skin with natural softness`
- **Tuyệt đối TRÁNH:** rough texture, fibrous surface, matted skin, creature skin, plastic shine

### Tóc — THEO NHÂN VẬT, thanh lịch và tự nhiên

> [!IMPORTANT]
> **Tóc phải thanh lịch.** Không dùng `wild`, `wispy`, `disheveled` — những từ này tạo ra tóc rối/xù. Tóc phải có silhouette rõ ràng, gọn gàng tự nhiên, phù hợp với nhân vật.

- **Màu:** Theo nhân vật và tuổi — trắng/bạc cho người già, nâu/đen cho trung niên, vàng/nâu cho trẻ hơn
- **Chất lượng:** `naturally soft fine hair with gentle movement` — mềm mại, tơi nhẹ, không xù
- **Silhouette:** `clean hair silhouette, neatly shaped` — có form rõ ràng, không rối
- **Tránh tuyệt đối:** `wild hair`, `wispy`, `disheveled`, `frizzy`, `matted`, `straw-like`

**Keyword đúng:** `naturally soft fine hair with gentle movement and clean silhouette, [màu sắc theo nhân vật]`

**Keyword SAI:** `wild wispy hair`, `disheveled hair`, `frizzy hair`, `matted hair`

### Bàn tay — Storytelling device

- Dài, ngón nhẹ nhàng biểu cảm — theo độ tuổi nhân vật
- `warm soft silicone puppet hands` — có warmth, tự nhiên, **không claw-like, không horror**
- Dùng cho close-up gesture shots: cầm đồ vật, chạm cừu, rót trà

**Keyword đúng:** `long gentle expressive puppet hands, warm soft silicone, natural graceful gesture`

### Trang phục — Vintage European Village Artisan

**Ưu tiên hàng đầu:**
- Chunky knit wool sweater (đan thô, rõ vân, màu trung tính xám/nâu/olive)
- Worn tweed coat (houndstooth hoặc herringbone, màu charcoal/dark gray/brown)
- Flat cap (tweed, herringbone) — đây là headwear signature
- Sage green beret (beret thợ thủ công)
- Dungarees / overalls (vải canvas thô, màu olive/beige)
- Scarf (len đan thô, thường màu terracotta cam đất đỏ)

### Companion Motif — Cừu len nỉ (Felted Wool Sheep)

> [!NOTE]
> Cừu là companion motif lặp lại của style này. Không bắt buộc xuất hiện trong mọi cảnh, nhưng khi có mặt phải đúng spec:

- `small felted wool sheep with dense curly cream-white wool coat, small black stick legs, tiny black bead eyes, stop-motion puppet scale`
- Cừu nhỏ hơn nhân vật đáng kể — scale miniature
- Thường 2-5 con trong cảnh ngoài trời, 1 con trong cảnh trong nhà

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
**Nhân vật (da, tóc, tay):** warm soft silicone puppet quality — sạch, có character nhưng KHÔNG rough/fibrous/creature-like

> [!IMPORTANT]
> **Phân biệt rõ:** World materials (đá, gỗ, vải) = rough và textured. Character skin = warm soft silicone. Đừng để texture của thế giới "lây" sang da nhân vật.

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
- Xuất hiện trong: scarves, backpacks, enamel kettles, mailboxes, hats
- Tone: `terracotta orange`, `rust red`, `burnt sienna`, `clay orange`
- KHÔNG phải orange tươi — phải muted, dusty, aged

**Secondary Accent: SAGE GREEN / DUSTY GREEN** 🌿
- Xuất hiện trong: berets, plant pots, weathered doors, moss on stone
- Tone: `dusty sage green`, `muted olive green`, `aged verdigris`

### Lighting Colors

- **Interior warm:** `deep amber`, `honey lamp glow`, `warm orange candlelight`
- **Exterior cool:** `cool blue-gray daylight`, `slate sky`, `muted overcast Mediterranean`
- **Golden hour:** `deep burnt orange sunset casting long shadows across stone`

---

## 7. Lighting DNA

### Quy tắc Lighting cốt lõi

> [!IMPORTANT]
> **Warm/Cool Contrast là defining characteristic của style này.** Mọi cảnh phải có sự tương phản rõ ràng giữa nguồn sáng ấm (amber) và không khí lạnh (stone gray blue).

### Cảnh ngoài trời — Ban ngày

- `cool overcast Mediterranean daylight, soft blue-gray ambient light on stone surfaces, dusty atmospheric haze`
- Ánh sáng chiều: `warm golden hour sunset casting long amber shadows across cobblestone`

### Cảnh ngoài trời — Chiều tối / Đêm

- `warm amber lantern light mounted on stone wall, glowing against cool blue dusk`
- `soft teal-blue door illuminated by a single warm lantern, golden amber pool of light on cobblestone below`

### Cảnh trong nhà — Buổi tối / Ấm cúng

- `warm amber table lamp with fabric shade, deep honey glow filling stone cottage interior`
- `fireplace glow, warm orange embers, dramatic warm/cool split on character's face`

### Không bao giờ dùng

- Flat uniform lighting
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

**Interior:**
- Stone cottage với low ceilings
- Rough stone walls, simple wooden furniture
- Workshop với tools và workbench
- Rustic kitchen với stone fireplace

---

## 9. Props Vocabulary

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

---

## 10. Emotional Doctrine

### Trung tâm cảm xúc

wonder, philosophical melancholy, quiet tenderness, the weight and beauty of a life fully lived, connection between beings (man and sheep, man and stranger), solitary dignity

### Khi chủ đề buồn

Buồn được phép ở đây — nhưng không bi thảm. Như một nhân vật ngồi một mình trước tách trà nguội, nhìn ra cửa sổ. Buồn như trong văn học.

---

## 11. Composition & Camera

### Tilt-shift / Depth of Field

- **BẮT BUỘC:** Tilt-shift effect tạo ra miniature world feeling
- Foreground objects thường bị blur nhẹ
- Background always atmospheric blur

### 3 lớp không gian

1. Foreground: một object gần camera (cừu, tảng đá, cái cốc)
2. Mid: nhân vật — đây là điểm focus chính
3. Background: kiến trúc đá blur, atmospheric haze

---

## 12. Prompt Templates

### Full template

```
[scene + subject + emotional action], [shot size / composition], [one specific grounded physical detail — light, gesture, or object], Laika-style stop-motion puppet, handcrafted European village cinema, macro photography, tilt-shift lens, kind naturally beautiful elderly human face with warm gentle eyes full of wisdom, gracefully aging with soft laugh lines, warm soft silicone puppet skin with warm natural skin tone, wild wispy silver-white hair, realistic adult human body proportions with correct head-to-body ratio, long gentle expressive puppet hands, [clothing from vintage European artisan wardrobe], [one terracotta orange accent object], [stone village setting detail], [lighting: warm amber interior OR golden hour sunset OR cool overcast exterior], rich cinematic depth of field with atmospheric background blur, 16:9, avoid goblin, avoid troll, avoid creature, avoid exaggerated nose or ears, avoid rough matted skin, avoid chibi, avoid glossy 3D, no text no handwriting no magical elements, no children
```

### Compressed template

```
[scene + subject + action], [shot size], Laika-style stop-motion puppet, European village cinema, tilt-shift macro, kind beautiful elderly human face, warm gentle eyes, gracefully aging, warm soft silicone puppet skin, soft laugh lines, realistic adult proportions, wild white hair, chunky knit or tweed clothing, [terracotta orange accent], stone village cobblestone setting, warm amber lantern against cool stone, cinematic depth of field, 16:9, avoid goblin avoid creature, avoid chibi, no children
```

### Dynamic template chuẩn hóa

```
[Chủ thể + Hành động theo concept], [Góc máy & Bố cục — framing qua arch/door/alley], [Một chi tiết vật lý cụ thể], [Props cụ thể theo kịch bản], Laika-style stop-motion puppet, handcrafted European village cinema, macro photography, tilt-shift lens, kind naturally beautiful elderly human face, warm gentle eyes full of life and wisdom, gracefully aging with soft natural laugh lines, warm soft silicone puppet skin with warm natural skin tone (clean surface not rough not fibrous), wild wispy silver-white hair, realistic adult human body proportions with correct head-to-body ratio, long gentle expressive puppet hands, [trang phục vintage artisan: chunky knit sweater / worn tweed coat / flat cap / sage green beret], [terracotta orange accent object cụ thể], [stone village bối cảnh cụ thể], [lighting contrast: warm amber source + cool stone ambient], rich cinematic depth of field, 16:9, avoid goblin, avoid troll, avoid creature, avoid exaggerated nose or ears, avoid rough matted fibrous skin, avoid chibi, avoid oversized head, avoid glossy 3D, no text no handwriting, no children
```

### Example prompts

**Ví dụ 1 — Shepherd on stone steps:**
```
A kind elderly shepherd gently hunched forward climbing ancient cobblestone steps, wide shot from side profile, small felted wool sheep walking alongside him at his feet, woven terracotta-orange backpack on his back, walking stick in hand, Laika-style stop-motion puppet, handcrafted European village cinema, macro photography, tilt-shift lens, kind naturally beautiful elderly human face with warm gentle eyes and soft laugh lines, gracefully aging, warm soft silicone puppet skin with warm natural skin tone, wild wispy silver-white hair, realistic adult body proportions, chunky sage-green knit jacket and olive trousers, rough stone village steps with Mediterranean stone buildings blurred in background, cool overcast blue-gray daylight, rich cinematic depth of field, 16:9, avoid goblin, avoid creature, avoid exaggerated features, avoid chibi, no text
```

**Ví dụ 2 — Indoor tea scene:**
```
A kind elderly man sitting at a rustic wooden table pouring tea from a terracotta orange enamel kettle, medium shot from slight side angle, steam rising gently from a ceramic cup, a small felted wool sheep resting quietly beside him on the table, a vintage wooden radio glowing amber in the background, Laika-style stop-motion puppet, handcrafted European village cinema, tilt-shift macro, kind naturally beautiful elderly human face with warm gentle eyes full of wisdom and quiet peace, gracefully aging with soft natural laugh lines, warm soft silicone puppet skin, wild wispy white hair, worn dark tweed jacket, rough stone cottage interior, deep warm amber lamp light, 16:9, avoid goblin, avoid creature, avoid exaggerated features, avoid chibi, no text
```

**Ví dụ 3 — Sunset shepherd with lantern:**
```
A kind elderly shepherd bending gently to pet a small sheep on a cobblestone street at dusk, medium shot, a warm amber lantern glowing on the stone wall beside a weathered teal-blue wooden door, Laika-style stop-motion puppet, handcrafted European village cinema, tilt-shift macro, kind naturally beautiful elderly human face, warm eyes catching the golden lantern light, gracefully aging, warm soft silicone puppet skin, wild wispy white hair, dark tweed coat and gray flat cap, cobblestone street with blurred flock of sheep in background, deep golden hour sunset casting warm orange light against cool stone walls, cinematic depth of field, 16:9, avoid goblin, avoid creature, avoid chibi
```

---

## 13. Words to Prefer / Avoid

### Dùng nhiều ✅

Laika-style stop-motion puppet, handcrafted European village cinema, macro photography, tilt-shift lens, **warm soft silicone puppet skin**, warm natural skin tone, **kind naturally beautiful elderly human face**, **warm gentle eyes full of life and wisdom**, **gracefully aging with soft natural laugh lines**, **wild wispy silver-white hair**, realistic adult body proportions, correct head-to-body ratio, long gentle expressive puppet hands, chunky knit wool sweater, worn tweed coat, flat cap, sage green beret, woven backpack, felted wool sheep, cobblestone street, weathered stone wall, aged wooden door (teal-blue), warm amber lantern, terracotta orange enamel kettle, vintage radio, mismatched ceramic teacups, stone cottage interior, atmospheric blur, cinematic depth of field, warm/cool lighting contrast, golden hour sunset over stone village

### Tránh hoặc không bao giờ dùng ❌

**goblin, troll, creature, monster** (drift #1), **exaggerated nose, large protruding ears, hooked nose, aquiline nose** (dễ drift creature), **rough matted fibrous skin, horror wrinkles, claw-like hands, creature face, grotesque**, textured clay skin (dùng warm soft silicone thay thế), chibi, oversized head, oversized cute eyes, anime proportions, smooth porcelain skin (quá warm_storybook), cream honey gold palette, healing cozy atmosphere, pitch-black darkness, magical elements, floating objects, text, handwriting, children, kids, Pixar-style, glossy 3D, modern architecture, clean interiors

---

## 14. Style Fingerprint (Compact Summary)

Old World European Stop-Motion Puppet village world — **kind, melancholic, beautiful**. Characters are stop-motion puppets with **realistic adult human proportions** (never chibi), **naturally beautiful elderly faces** — gracefully aging, warm eyes, soft laugh lines — rendered in **warm soft silicone puppet skin**. Like a master puppet maker's finest work: a dignified, kind old man, NOT a goblin, NOT a creature. Wild wispy white hair, long gentle hands. World is weathered Mediterranean stone — cobblestone streets, aged teal-blue wooden doors. **Terracotta orange** is the signature accent. **Felted wool sheep** are the companion motif. Lighting: **warm amber interior vs cool blue-gray stone exterior**. Mood: literary, melancholic-tender — "a life fully lived, observed with love." **No goblin. No creature. No exaggerated features. No chibi. No children.**

---

## 15. Revision Behavior (Style-Specific)

| Boss nói | Sửa |
|----------|-----|
| **Nhân vật trông như goblin / creature / kỳ dị** | **SỬA NGAY:** Xóa mọi keyword exaggerated. Dùng: `kind naturally beautiful elderly human face, gracefully aging with soft laugh lines, warm gentle eyes, warm soft silicone puppet skin`. Negative: `avoid goblin, avoid creature, avoid exaggerated nose or ears, avoid horror wrinkles`. |
| **Mặt không đẹp / thiếu warmth** | Thêm: `kind and naturally beautiful, warm gentle eyes full of wisdom and quiet joy, dignified gracefully aging face, peaceful melancholic expression`. |
| **Da quá rough / fibrous** | Dùng: `warm soft silicone puppet skin, warm natural skin tone, clean smooth surface`. Negative: `avoid rough texture, avoid fibrous skin`. |
| **Tóc trông như rơm / matted** | Dùng: `wild wispy silver-white hair, natural fluffy strands, softly disheveled`. Negative: `avoid matted hair, avoid straw-like texture`. |
| **Nhân vật bị chibi / đầu to** | Thêm: `realistic adult body proportions, correct head-to-body ratio`. Negative: `avoid chibi, avoid oversized head`. |
| **Thiếu terracotta orange** | Thêm 1 orange accent: `terracotta orange enamel kettle`, `rust-orange woven scarf`, `terracotta-orange backpack`. |
| **Lighting quá phẳng** | Thêm: `warm amber lantern glow against cool blue-gray stone`, `deep amber interior vs cool stone exterior`. |
| **Thiếu cừu** | Thêm: `small felted wool sheep with dense curly cream-white wool coat, small black stick legs, stop-motion puppet scale`. |
| **Bối cảnh không đúng** | Thêm: `weathered stone Mediterranean village, cobblestone street, aged limestone walls, teal-blue wooden door`. |
| **Quá dark / thiếu warmth** | Thêm: `melancholic but tender, kind human expression, warm amber light source`. |
| **Ảnh phẳng / no depth** | Thêm 3 lớp: foreground prop + mid character + background stone blur. `cinematic depth of field, tilt-shift atmospheric perspective`. |
