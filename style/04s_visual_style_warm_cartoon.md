# Visual Style Module: Warm Golden Hour Cartoon Cinema

> **Style ID:** `warm_cartoon`
> **Status:** 🔵 Available Option
> **Version:** 1.0
> **Dùng cho:** Video cần phong cách hoạt hình 3D mượt mà, ấm áp kiểu smooth stylized 3D CGI — nhân vật đa dạng tuổi, cảm xúc rõ ràng, ánh sáng golden hour cinematic, sắc nét và rực rỡ.

---

## Cách sử dụng file này

File này chứa toàn bộ DNA thị giác cho **Warm Golden Hour Cartoon Cinema**. Agent đọc file này tại Stage 4.1 để load phong cách hình ảnh.

Khi Boss muốn style này, chỉ định `style: warm_cartoon` trong brief. Style này hoạt động song song với `warm_storybook` — không thay thế, không cạnh tranh. Chúng là hai phong cách riêng biệt trên cùng một kênh.

**Điểm phân biệt cốt lõi so với warm_storybook:**

| warm_storybook | warm_cartoon |
|----------------|-------------|
| Claymation / stop-motion puppet feel | Smooth smooth stylized 3D CGI render |
| Matte porcelain-clay skin | Subsurface scattering, soft luminous skin |
| Handcrafted tactile texture | Polished digital smoothness |
| Elderly characters mặc định | Mọi lứa tuổi — linh hoạt |
| Indoor domestic realism | Outdoor cinematic + indoor đều mạnh |
| Paper, wood, fabric props | Clean stylized props với warm color pop |

---

## 1. Style Identity & Feel

### Tên phong cách
**Warm Golden Hour Cartoon Cinema**

### Hình ảnh nên cảm nhận như:

- warm và luminous — ánh vàng golden hour bao phủ mọi khung hình
- smooth và polished — bề mặt sạch bóng, không có handcraft imperfection
- joyful và emotionally expressive — nhân vật truyền cảm xúc qua ánh mắt và nét mặt
- cinematic — chiều sâu không gian thực, bokeh đẹp, ánh sáng có hướng rõ
- wholesome và inviting — ai nhìn cũng muốn bước vào thế giới đó
- vibrant nhưng không neon — màu rực nhưng ấm, không chói, không lạnh
- có chiều sâu tonal — không phẳng, không cartoon 2D flat
- outdoor-friendly — thiên nhiên, bầu trời, ánh nắng là bối cảnh tự nhiên
- emotional và readable — mỗi frame kể được một cảm xúc không cần chữ

---

## 2. Style Anchors

### Full style anchor (dùng cho prompt > 500 ký tự)

```
warm golden hour smooth stylized 3D animation cinema, smooth stylized 3D character with expressive proportions, soft subsurface scattering on luminous warm skin, vibrant warm color palette of honey-gold, soft amber, peachy cream, and sky blue, cinematic golden hour outdoor lighting with warm rim light wrapping the subject, rich tonal depth with glowing highlights and warm shadow detail, shallow depth of field with warm soft bokeh, emotionally readable expressive face and body language, clean stylized world with natural outdoor warmth, 16:9, not claymation, not flat cartoon, not photorealistic, not waxy plastic
```

### Short style anchor (dùng cho prompt ngắn hơn)

```
warm golden hour smooth stylized 3D cartoon, smooth stylized character, soft subsurface scattering, honey-gold warm lighting, expressive proportions, shallow depth of field, warm soft bokeh, vibrant warm palette, 16:9
```

### Nguyên tắc MỞ — Character Treatment Rules

Style này **không khóa vào một lứa tuổi cụ thể**. Trẻ em, thanh niên, người già đều có thể là nhân vật chính. Tuy nhiên character phải luôn:

- **Proportions:** Stylized cartoon proportions — đầu hơi lớn hơn thực tế, mắt expressive, tổng thể appealing không uncanny
- **Skin:** Soft luminous với subsurface scattering — ánh sáng xuyên nhẹ qua da tạo warmth tự nhiên
- **Expression:** Readable và emotional — người xem biết nhân vật đang cảm thấy gì trong 0.3 giây
- **Body language:** Calm, natural, gestural — không stiff, không over-animated
- **Clothing:** Warm-toned, có fabric detail nhẹ, không quá elaborate

### Đặc điểm bắt buộc

- expressive oversized eyes with warm catch lights
- smooth stylized facial features, no harsh lines
- soft rounded cartoon proportions — appealing, not creepy
- warm peach-amber skin tone với subtle subsurface glow
- hair với volume và shape rõ ràng, separated strands hoặc curls
- emotionally readable micro-expressions
- calm natural body posture

### Đặc điểm CẤM

- photorealistic human proportions và skin texture
- deep wrinkles hoặc harsh aging lines (nếu nhân vật già: stylized gracefully, không hyper-realistic)
- blob-like hair fused với skin
- dead eyes hoặc blank expression (uncanny valley)
- waxy or overly glossy skin
- skeletal or sunken facial features
- aggressive or unsettling proportions

### Hair rule

Tóc phải có volume, shape, và separation — không phải solid mass.

Dùng: `soft voluminous curly hair with clearly separated spiral locks, warm honey-gold or amber-brown hair catching golden light, natural hairline, wind-subtle movement`

Tránh: `flat solid hair mass, blob-like hair fused to head, hair without shading or depth`

Khi close-up: luôn thêm `separated hair strands catching warm backlight, clear hairline`

### Face rule

Gương mặt phải beautiful, readable, và stylized — không photorealistic, không uncanny.

Dùng: `smooth stylized smooth stylized face, expressive warm eyes with soft catch light, appealing cartoon proportions, emotionally readable expression, soft rounded features, luminous warm skin with gentle subsurface glow`

Tránh: `photorealistic skin texture, harsh facial lines, sunken cheeks, dead blank eyes, waxy plastic skin, uncanny valley proportions`

### Hands rule

Cho close-up: `clean smooth stylized hands, soft rounded fingers, appealing simplified anatomy, no harsh veins or wrinkles, warm skin tone, natural relaxed pose`

Tránh: `deformed hands, fused fingers, overly detailed realistic hands, lumpy knuckles`

### Character Rendering Lock

Khi render nhân vật, luôn áp dụng:
- **Bắt buộc:** `smooth stylized smooth stylized 3D character, expressive appealing proportions, soft subsurface scattering on warm skin, emotionally readable face`
- **Tránh tuyệt đối:** photorealistic skin, claymation texture, waxy shine, uncanny valley, dead eyes
- **Trang phục:** Warm-toned, clean fabric, luôn thêm: `soft warm-toned clothing with clean fabric detail`

---

## 5. Material Palette

Texture nên hỗ trợ cảm xúc và warmth — clean, smooth, inviting.

### Vật liệu ưa thích

- smooth warm fabric — soft cotton, gentle knit, clean linen
- natural wood với warm grain (không rough, không distressed)
- ceramic và pottery với warm glaze
- grass, leaves, flowers với vibrant but warm-toned color
- stone với smooth natural surface
- sky và cloud với soft painterly quality
- water với warm reflective surface

### Cảm giác vật liệu tốt nhất

smooth, warm, clean, slightly stylized, luminous — không muddy, không rough, không photorealistic hyper-detail

### Tactile Material Lock

Khi các vật thể sau xuất hiện:
- **Cây cối / thiên nhiên:** `stylized lush green foliage with warm sunlight filtering through, golden rim light on leaf edges`
- **Đồ gỗ:** `smooth warm wooden surface with gentle grain, honey-amber tone`
- **Bầu trời:** `painterly warm sky with soft peach-amber clouds, cinematic golden hour atmosphere`
- **Nước:** `warm reflective water surface, catching golden hour light`

---

## 6. Color DNA

### Bảng màu mặc định

honey-gold, warm amber, soft peach, cream, sky blue (cool accent), sage green (natural accent), dusty rose, warm ivory, golden ochre

### Tránh mặc định

cold neon colors, harsh electric blue, pure white (too sterile), pure black (too harsh), muddy brown, desaturated gray, cold purple, clinical white backgrounds

### Cách dùng màu chủ đạo

**Honey-gold** là màu chủ đạo của style này — không phải từ filter mà từ ánh sáng thực trong khung hình:
- golden hour sun trên skin và hair
- warm rim light wrapping around subject
- warm bokeh background glow
- warm-toned shadows (không bao giờ là cold gray shadows)

**Sky blue** là màu contrast tự nhiên — xuất hiện trong:
- bầu trời nền
- eye color nếu phù hợp
- bokeh cloud background

**Quy tắc shadow:** Shadow trong style này luôn là warm-toned — amber, honey, soft burnt sienna. Không bao giờ là neutral gray hoặc cold blue shadow.

### Color Balance

- 60% warm tones (honey, amber, peach, cream) — nền và nhân vật
- 25% natural accents (green, sky blue) — thiên nhiên và bầu trời
- 15% highlight glow (golden white, bright honey) — ánh sáng rim và highlight

---

## 7. Lighting DNA

### Nguyên tắc cốt lõi

Ánh sáng là **linh hồn của style này**. Golden hour lighting không phải filter sau — nó phải là ánh sáng thực có hướng rõ ràng, tạo rim light ấm trên nhân vật, warm bokeh trong background, và shadow ấm phía đối diện.

### Ưu tiên

- late afternoon golden sun từ một phía — rim light ấm bao quanh tóc và vai
- soft subsurface fill light từ phía đối diện — skin glow từ trong ra
- warm bokeh background với soft cloud hoặc foliage
- shallow depth of field — subject sắc nét, background mềm ấm
- low camera angle nhìn lên nhẹ — cinematic portrait feel

### Ánh sáng ban ngày (outdoor — mạnh nhất cho style này)

`cinematic late afternoon golden hour light from one side, warm amber rim light wrapping around hair and shoulders, soft subsurface fill from opposite side, shallow depth of field with warm honey-gold bokeh, painterly sky background`

### Ánh sáng indoor

`warm window light or golden interior lamp, soft warm ambient fill, honey-amber shadows, no harsh cool overhead light, cozy luminous indoor atmosphere`

### Ánh sáng ban đêm

`warm amber interior glow, soft candlelight or lamp warmth, luminous honey-colored light sources, lifted warm shadows, no pitch-black darkness, cozy nighttime atmosphere`

### Tránh

- flat frontal lighting (no shadow, no depth)
- cold studio strobe look
- harsh overhead light (too dramatic, loses warmth)
- overly saturated HDR extreme look
- pitch-black shadows
- pure white blown-out highlights
- cold blue-hour lighting

Lighting nên cảm nhận như: standing in the warmest moment of the day, just before sunset.

---

## 7.5. HDR & Tonal Richness Doctrine

> [!IMPORTANT]
> Warm Cartoon images phải có **chiều sâu tonal thực sự** — không phải flat cartoon với shading đồng đều. Mỗi khung hình cần có: shadow ấm có detail, highlight rực nhưng không cháy, mid-tone được phân tầng rõ giữa honey, amber, peach, và cream.

### Định nghĩa HDR cho Warm Cartoon

Trong context này, "HDR" không phải tone-mapping cực đoan. Nó có nghĩa:

- **Warm shadow detail:** Vùng tối không phải flat gray — có màu amber/honey ấm, có texture nhẹ
- **Glowing highlight:** Vùng rim light và highlight rực nhưng gradient mượt, không cháy trắng
- **Rich mid-tone separation:** Honey vs amber vs peach vs cream là các giá trị rõ ràng, không merge
- **Subsurface glow:** Skin có internal luminosity — ánh sáng từ trong da tỏa ra nhẹ
- **Bokeh warmth:** Background bokeh không phải white blur — phải có warm honey-amber toning

### HDR Keywords cho Prompt (chọn 2-3 cụm phù hợp mỗi prompt)

**Tonal depth & richness:**
- `rich cinematic tonal depth, warm glowing highlights, honey-amber shadow detail`
- `HDR-like warm color range, bright rim light blending into warm amber shadow`
- `deep rich warm tonal gradient from glowing highlight to honey-amber shadow`

**Subsurface & skin glow:**
- `soft subsurface scattering creating warm internal skin glow`
- `luminous warm skin with gentle subsurface light from within`
- `peach-warm skin luminosity, soft inner glow`

**Bokeh & atmospheric depth:**
- `warm honey-gold bokeh background with soft out-of-focus warmth`
- `shallow depth of field with warm amber atmospheric bokeh`
- `layered depth: sharp subject against warm soft background glow`

**Cinematic richness:**
- `cinematic warm color grading, not flat, not washed out`
- `filmic warm color science, rich shadow warmth, glowing rim highlight`
- `cinematic lighting richness with tonal identity on every surface, subsurface scattering warmth`

### Full Style Anchor HDR-Enhanced

```
warm golden hour smooth stylized 3D animation cinema, smooth stylized 3D character with expressive appealing proportions, soft subsurface scattering creating warm internal skin glow, luminous warm skin with gentle peach subsurface luminosity, vibrant warm color palette of honey-gold, soft amber, peachy cream, and sky blue, cinematic golden hour directional light from one side with warm amber rim light wrapping subject, rich cinematic tonal depth with glowing highlights and honey-amber shadow detail, warm honey-gold bokeh background, shallow depth of field, emotionally readable expressive face, clean stylized outdoor world, 16:9, not claymation, not flat cartoon, not photorealistic, not waxy plastic
```

## 11. Prompt Templates (Style-Specific)

### Full template

```
[scene + subject + emotional action], [shot size / composition], [one specific natural light detail — rim light, bokeh, shadow, sky], warm golden hour smooth stylized 3D animation cinema, smooth stylized 3D character with expressive appealing proportions, soft subsurface scattering on warm luminous skin, [key environment / props], vibrant warm palette of honey-gold and amber and peach and sky blue, cinematic golden hour light with warm rim and soft bokeh, shallow depth of field, [emotion], 16:9, not claymation, not flat cartoon, not photorealistic
```

### Compressed template

```
[scene + subject + action], [shot size], [one natural light detail], warm golden hour smooth stylized 3D animation cinema, smooth stylized character, soft subsurface scattering, expressive proportions, warm amber rim light, honey-gold bokeh, shallow depth of field, [emotion], 16:9
```

### Dynamic template chuẩn hóa

```
[Chủ thể + Hành động theo concept], [Góc máy & Bố cục động], [Chi tiết ánh sáng tự nhiên cụ thể — rim light / bokeh / shadow / sky], [Môi trường & Props theo kịch bản], warm golden hour smooth stylized 3D animation cinema, smooth stylized 3D character with expressive appealing proportions, soft subsurface scattering creating warm internal skin glow, [Màu sắc & Ánh sáng Golden Hour theo bối cảnh], shallow depth of field with warm honey-gold bokeh, 16:9, not claymation not flat cartoon not photorealistic
```

### Example prompt (outdoor portrait — loại mạnh nhất cho style này)

A young curly-haired child looking upward with a gentle curious smile, low camera angle looking up at the subject, late afternoon golden sun from behind creating warm amber rim light wrapping around curly hair like a halo, warm golden hour smooth stylized 3D animation cinema, smooth stylized 3D character with expressive appealing proportions, soft subsurface scattering on warm peach-luminous skin, expressive warm eyes catching soft afternoon light, soft warm-toned clothing, painterly sky background with warm peach-amber clouds slightly out of focus, shallow depth of field with honey-gold bokeh, joyful wonder, 16:9, not claymation, not flat cartoon, not photorealistic

---

## 12. Words to Prefer / Avoid

### Dùng nhiều

warm golden hour smooth stylized 3D cartoon, smooth stylized 3D character, expressive appealing proportions, soft subsurface scattering, warm luminous skin, internal skin glow, honey-gold, amber, peach, cream, sky blue, cinematic golden hour, warm rim light wrapping, shallow depth of field, warm honey-gold bokeh, expressive warm eyes, emotionally readable expression, soft voluminous hair with separated curls, clean warm-toned fabric, natural outdoor setting, warm shadow detail, dappled sunlight, late afternoon glow, painterly warm sky, joyful wonder, wholesome delight, emotionally alive, warm internal glow, cinematic tonal richness, not flat not washed out

### Tránh hoặc dùng rất ít

claymation, stop-motion puppet, clay texture, matte porcelain, handcrafted imperfection, photorealistic skin, hyper-detailed wrinkles, cold blue CGI, dark moody shadows, pitch-black darkness, waxy glossy shine, plastic toy finish, flat cartoon shading, mobile game graphic, generic 3D illustration, dead eyes, blob hair, creepy proportions, uncanny valley, cold steel, dark urban, gothic atmosphere

---

## 13. Style Fingerprint (Compact Summary)

Warm Golden Hour Cartoon Cinema. Smooth smooth stylized 3D animation with expressive appealing character proportions, soft subsurface scattering on luminous warm skin, and cinematic golden hour lighting as the visual signature. Vibrant warm palette (honey-gold, amber, peach, cream, sky blue) — no cold tones, no dark shadows, no claymation texture. Characters of any age rendered with emotional clarity and cartoon warmth. Outdoor-strong: golden hour rim light wrapping subjects, warm bokeh backgrounds, shallow depth of field, painterly sky. Rich tonal depth: warm shadow detail, glowing highlights, subsurface skin glow. Single natural everyday detail in each frame — observed from real light, real warmth, real outdoor moments. No text, no magical elements, no handcraft imperfection. **The world is familiar but lit like the most beautiful afternoon you've ever seen.**

---

## 14. Revision Behavior (Style-Specific)

| Boss nói | Sửa |
|----------|-----|
| Trông như claymation / handcraft | Tăng `smooth smooth stylized 3D`, `soft subsurface scattering`, `polished stylized render`. Bỏ `matte clay`, `handcrafted`, `textured surface`. |
| Skin trông waxy / plastic | Thêm `soft subsurface scattering`, `warm internal skin glow`, `luminous peach skin tone`. Bỏ `glossy`, `waxy`, `plastic finish`. Điều chỉnh ánh sáng: tránh highlight quá mạnh trực tiếp. |
| Thiếu ấm / quá lạnh | Thêm `warm golden hour lighting`, `honey-amber rim light`, `warm shadow detail`, `honey-gold bokeh`. Kiểm tra shadow color — phải warm, không phải cold gray. |
| Ảnh phẳng / thiếu chiều sâu | Thêm `shallow depth of field`, `warm bokeh background`, `cinematic tonal depth`, `rich warm tonal gradient`. Đổi camera angle: `low camera angle looking up`, `shot through foreground foliage`. |
| Nhân vật trông uncanny / creepy | Tăng `expressive appealing proportions`, `smooth stylized smooth stylized face`, `emotionally readable expression`. Bỏ bất cứ gì về realistic proportions, photorealistic detail. |
| Thiếu cảm xúc / nhân vật cold | Tăng `expressive warm eyes`, `emotionally readable micro-expression`, `clear body language`. Thêm gesture hoặc action cụ thể. |
| Tóc bệt / fused | Thêm `soft voluminous hair with clearly separated curls/strands`, `hair catching warm backlight`, `clear hairline`. Bỏ `blob hair`, `solid hair mass`. |
| Quá tối | Thêm `warm golden hour lighting`, `lifted warm shadows`, `no pitch-black darkness`. Chuyển setting sang outdoor golden hour hoặc cozy indoor warm lamp light. |
| Nhàm chán / boring | Thêm một chi tiết ánh sáng tự nhiên cụ thể (rim light trên tóc, bokeh lá cây, dappled shadow trên mặt đất). Đổi camera angle thấp hơn. Thêm emotional action rõ hơn. |
| Trông quá giống smooth CGI generic / thiếu identity riêng | Tăng warm palette cụ thể của Coslient: `honey-gold dominant`, `peach-cream skin`, `amber shadow`. Giảm generic smooth CGI blue-teal shadows. Style này là **Coslient warm** không phải generic smooth CGI. |

---

## 15. Color DNA Reference

> [!NOTE]
> Section này là **nguồn tham khảo bảng màu** của style `warm_cartoon`. Coslient sử dụng đây khi xây dựng Color Tone String cho từng video (dựa trên câu chuyện). Không phải block cứng nhắc bắt buộc — tone màu thực tế của từng video do câu chuyện quyết định.

### Block chính (gắn vào cuối prompt)

```
warm golden hour smooth stylized 3D cartoon color grading, honey-gold and amber split-tone, soft warm subsurface skin glow, luminous peach-cream highlights, warm amber shadow floor with no cold gray, vibrant warm palette of honey-gold and soft amber and peachy cream, warm honey-gold bokeh atmosphere
```

### Ví dụ tích hợp đầy đủ

```
A young curly-haired child crouching down to examine a glowing firefly cupped in both hands, low camera angle looking up slightly, late afternoon golden sun from behind creating warm amber rim light wrapping through curly hair, warm honey-toned meadow grass in foreground, painterly peach-amber sky with soft clouds slightly out of focus in background, smooth stylized 3D character with expressive appealing proportions, soft subsurface scattering on luminous warm peach skin, joyful quiet wonder, warm golden hour smooth stylized 3D cartoon color grading, honey-gold and amber split-tone, soft warm subsurface skin glow, luminous peach-cream highlights, warm amber shadow floor with no cold gray, vibrant warm palette of honey-gold and soft amber and peachy cream, warm honey-gold bokeh atmosphere, 16:9, not claymation, not flat cartoon, not photorealistic
```
