# Coslient GPT Knowledge — Animation Prompt Development v4.0

## Purpose

This file defines how Coslient handles the animation stage using **Google Flow** (Nano Banana image gen + VEO 3 video gen).

Workflow: Generate ingredients → @tag trong Flow → generate image frames → animate với VEO 3 → assemble trong Scenebuilder.

> **v4.0 Update:** Google Flow native workflow. @tag character/environment system. Scenebuilder continuity protocol. Camera vocabulary for VEO 3. Universal audio control updated.

---

## Stage position

This stage begins only after the image direction or image set is approved.
Do not move to animation before the image stage is ready.

---

## Tool: VEO 3 — Điều cần biết

VEO 3 generates video and audio in a single pass via image-to-video mode.

**Những điều quan trọng nhất:**

- VEO đọc ảnh gốc trước khi đọc prompt. **Prompt không cần mô tả lại visual** — chỉ cần nói về camera, motion, style, audio
- VEO weight những từ đầu tiên của prompt mạnh hơn — front-load camera + motion
- **Audio cues trong VEO 3 không chỉ control sound — chúng còn là motion physics anchor.** Viết `"leaves responding gently to air"` trong prompt → VEO tự animate lá cây theo gió thật. Đây là behavior riêng của VEO 3
- Image-to-video mode thường ra silent clip theo mặc định — đây là tốt cho music video vì mày có nhạc riêng
- Prompt length tối ưu: **75–125 từ**. Quá 175 từ → conflicting instructions → chất lượng giảm

---

## Grounded Reality Rule (BẮT BUỘC — ZERO TOLERANCE)

> [!IMPORTANT]
> Áp dụng cho MỌI clip, dù cảnh đời thường hay siêu thực.

Cái làm video trông rẻ tiền không phải là con rồng hay không gian kỳ lạ — mà là **hiệu ứng không có thật trong tự nhiên**.

**Tuyệt đối cấm:**
- Internal glow từ nhân vật hoặc vật thể
- Magical particles, sparkles, stardust, light orbs
- Sợi ánh sáng từ tay / người
- Lơ lửng không có lý do vật lý
- Ethereal mist quanh nhân vật
- Bất kỳ hiệu ứng nào chỉ tồn tại trong video game hoặc cheap AI

**Test trước khi dùng bất kỳ motion nào:**
> "Cái này có tồn tại trong thế giới thật không?" → Không → Bỏ.

---

## Universal Prompt — Dùng cho TẤT CẢ clip

```
Slow, steady cinematic push-in, smooth and tripod-stable. Soft natural ambient 
motion in the scene — fabric, hair, leaves, or steam responding gently to air. 
Warm golden-hour lighting, long soft shadows, lifted warm tones. Rich warm 
cinematic color grading, preserve handcrafted miniature diorama style with 
tactile materials, smooth cinematic motion, fluid character movement, shallow 
depth of field. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — soft ambient sounds natural to this 
scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable 
sound can be generated, output silence rather than music.
```

### Lý do từng phần — để không vô tình sửa sai

| Phần | Lý do |
|------|-------|
| `Slow, steady cinematic push-in` | Motion verb cụ thể — "cinematic" alone là placebo, nhưng kết hợp với "push-in" thì có tác dụng thật |
| `smooth and tripod-stable` | Positive anchor, không dùng "no camera shake" vì VEO thường ignore negative instructions |
| `fabric, hair, leaves, or steam responding gently to air` | Physics anchor — trigger VEO animate đúng vật thể theo vật lý thật |
| `Warm golden-hour lighting` | Top-tier keyword — shift palette sang warm amber |
| `long soft shadows, lifted warm tones` | Ngăn vùng tối lạnh, giữ Coslient DNA |
| `rich warm cinematic color grading` | Color control — giữ tông ấm, không dùng aesthetic retro/film |
| `shallow depth of field` | Subject nổi, background blur tự nhiên — đây là tính chất quang học của ống kính, không phải retro look |
| `Serene, intimate, contemplative mood` | Cụ thể hơn "emotional" — VEO hiểu và apply đúng tone |
| `Diegetic environmental sound only` | Filmmaking term — VEO comply ~70% với cụm này |
| `soft ambient sounds natural to this scene` | Flexible nhưng grounded — VEO tự chọn sound phù hợp với ảnh |
| `No music. No score. No dialogue. No vocals. No voiceover.` | 5 exclusion riêng biệt — combine với diegetic → ~85-90% compliance |
| `If no suitable sound can be generated, output silence rather than music` | Fallback instruction — ngăn VEO default sang music khi confused |

---

## Quy tắc bắt buộc khi dùng Universal Prompt

### Rule 1 — Không mô tả lại nhân vật hay cảnh
VEO đã thấy ảnh gốc. Thêm description về visual sẽ khiến model re-interpret → character drift, ảnh vỡ.
**Chỉ paste nguyên prompt, không thêm gì.**

### Rule 2 — Không dùng dấu ngoặc kép `" "` ở bất kỳ đâu
VEO hiểu quotes = command generate dialogue + lip-sync. Kể cả trong audio section.

### Rule 3 — Clip length: 8 giây (default)
Đây là native output duration của VEO 3 image-to-video. Dùng parameter `"duration": 8` nếu qua API.

### Rule 4 — Frame bridging giữa các clip
Last frame của clip A → làm start frame của clip B.
Khi đổi location hoàn toàn: generate ảnh tĩnh mới làm anchor trước, rồi dùng làm start frame.

### Rule 5 — Strip audio nếu VEO gen sound lạ
```bash
ffmpeg -i input.mp4 -an output_no_audio.mp4
```
Sau đó overlay nhạc riêng trong editor. Đây là workflow chuẩn của professional.

---

## Shot Bridge Protocol (MỚI — Storyboard-Driven Workflow)

> [!IMPORTANT]
> Storyboard đã thiết kế sẵn tính liên tục giữa các clips. Khi animate theo storyboard, dùng bảng này để quyết định cách nối từng clip — thay vì phải sắp xếp thủ công trong editor.

### Ba loại Bridge:

| Loại | Khi nào dùng | Cách xử lý |
|------|-------------|-----------|
| **Direct Bridge** | Shot N+1 cùng không gian với Shot N | Last frame của Shot N → làm input image cho Shot N+1 |
| **Environmental Bridge** | Shot N+1 là `[NEW LOCATION]` | Tạo 1 ENV Shot (cảnh không người) làm "xả" trước khi vào location mới. **KHÔNG** dùng last frame của Shot N làm start frame cho Shot N+1 |
| **Detail Bridge** | Time jump (sáng → tối, ngày → năm sau) | Tạo 1 DETAIL Shot (cận vật thể) làm visual bridge — không cần match spatial anchor |

### Khi nào KHÔNG dùng last frame làm start frame:
- Shot N+1 là `[NEW LOCATION]` → KHÔNG dùng (AI sẽ bị confused về không gian)
- Shot N+1 là time-jump rõ ràng → KHÔNG dùng
- Hai shots có emotional contrast quá lớn (vui cực ↔ buồn sâu) → dùng Environmental Bridge xen giữa

### Checklist trước khi batch VEO (dùng cùng file `03_storyboard.md`):
- [ ] Mọi Shot ID đã có prompt tương ứng trong `04_image_prompts.txt`?
- [ ] Các Shot Bridge đã được đánh dấu (Direct / Environmental / Detail)?
- [ ] Mọi `[NEW LOCATION]` shot đã có Environmental Bridge trước đó?
- [ ] Không có 2 close-up liên tiếp cùng hướng nào sẽ gây jump cut?

---

## Keywords CẤM trong Animation Prompt

**Motion keywords nguy hiểm — gây distortion:**
- `zoom in fast` → face warping
- `orbit around subject` → face morphing (VEO phải hallucinate góc không có trong ảnh)
- `handheld shake` (không có "subtle/micro") → jitter không kiểm soát
- `pan while zooming` → horizon distortion
- `drone flyover` → unrealistic physics
- `dynamic movement` (vague) → AI tự chọn path ngẫu nhiên
- `scene changes` → trigger cut attempts, phá single-clip flow

**Cách dùng negative cho VEO 3:**
- ❌ "no camera shake" → VEO thường ignore
- ✅ "tripod-stable framing" → positive anchor, VEO hiểu

---

## Fallback Protocol — Khi 1 clip cụ thể ra sai

Sau khi batch toàn bộ, nếu 1 vài clip bị vỡ hoặc sound lạ, viết prompt riêng cho clip đó:

**Cấu trúc fallback:**
```
[Shot type]. [1 gentle action]. [Reinforcement của cảnh trong ảnh].
[Paste full style + audio block từ universal prompt]
```

**Ví dụ — cảnh bà ngồi bên cửa sổ:**
```
Static medium shot, subtle micro-movements, preserve facial expression and posture. 
Figure sits quietly by window, slight natural breathing motion, hands still. 
Warm golden-hour lighting, long soft shadows, lifted warm tones. Rich warm 
cinematic color grading, preserve handcrafted miniature diorama style with 
tactile materials, smooth cinematic motion, fluid character movement, shallow 
depth of field. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — distant birds through window glass, 
quiet house ambient, faint ceramic settle. No music. No score. No dialogue. 
No vocals. No voiceover. If no suitable sound can be generated, output silence 
rather than music.
```

**Ví dụ — cảnh ngoài vườn:**
```
Slow gentle parallax dolly-in, foreground-background depth separation. 
Figure moves slowly through garden, natural weight and gait. 
Warm golden-hour lighting, long soft shadows, lifted warm tones. Rich warm 
cinematic color grading, preserve handcrafted miniature diorama style with 
tactile materials, smooth cinematic motion, fluid character movement, shallow 
depth of field. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — birdsong from multiple directions, 
light wind through leaves, soft footsteps on grass. No music. No score. 
No dialogue. No vocals. No voiceover. If no suitable sound can be generated, 
output silence rather than music.
```

**Ví dụ — cảnh siêu thực (grounded):**
```
Static medium shot, hold still, preserve all elements exactly as in source image. 
Natural ambient motion only — no magical effects, no added light, no particles. 
Warm golden-hour lighting, long soft shadows, lifted warm tones. Rich warm 
cinematic color grading, preserve handcrafted miniature diorama style with 
tactile materials, smooth cinematic motion, fluid character movement, shallow 
depth of field. Serene, contemplative mood.

Audio: Diegetic environmental sound only — natural physical sounds matching the 
environment in the scene. No music. No score. No dialogue. No vocals. 
No voiceover. If no suitable sound can be generated, output silence rather than music.
```

---

## Google Flow Native Workflow (v4.0)

> [!IMPORTANT]
> **Đây là workflow chính thức.** Toàn bộ image generation và video generation xảy ra trong Google Flow.

### Bước 1 — Chuẩn bị Ingredients
```
Tất cả ingredients đã upload và approve (từ 04_character_bible.md)
@OldMan, @BrassHand, @GlassDome, @Seagrass, @SandyBed, @DeepAbyss,
@HermitCrab, @CoralSeed, @MantaRay, @StyleRef
```

### Bước 2 — Generate Source Frames (Nano Banana)
Generate source image cho mỗi shot theo storyboard.
Dùng Shot Prompt Template từ `04_character_bible.md`:
```
[Shot size], @[Character] [action] in @[Environment],
[1 camera movement intent — cho VEO đọc sau],
[lighting keywords]
```
Approve frames trước khi animate.

### Bước 3 — Animate với VEO 3
Paste Universal Prompt vào VEO 3 cho từng approved frame:
```
[Xem Universal Prompt section phía trên]
```
Dùng @tags trong VEO prompt để maintain character consistency:
```
Slow steady push-in, @OldMan kneeling gently, @DeepAbyss surrounding,
static almost-locked frame with micro-movements,
near-darkness with faint bioluminescent cyan light,
Audio: deep ocean pressure hum, distant water movement. No music. No score. No dialogue.
```

### Bước 4 — Scenebuilder Assembly

| Transition | Cách xử lý |
|-----------|------------|
| Cùng location, shot tiếp theo | **"Add to Scene"** → VEO tự maintain continuity |
| Extend clip dài hơn | **"Extend"** → chain seamlessly |
| Đổi location | **"Jump To"** + ENV bridge shot trước |
| Time jump | Generate DETAIL shot bridge → rồi "Add to Scene" |

> [!CAUTION]
> KHÔNG generate từng clip hoàn toàn độc lập nếu có thể tránh. Dùng "Add to Scene" để Flow giữ continuity tốt hơn.

### Bước 5 — Audio
- Review toàn bộ clips: audio VEO có phù hợp không?
- Strip audio nếu lạ: `ffmpeg -i input.mp4 -an output.mp4`
- Overlay nhạc trong editor

---

## Camera Vocabulary cho VEO 3 (Reference)

| Camera Move | Prompt Term tốt nhất | Tránh |
|-------------|---------------------|-------|
| Dolly in | `slow dolly-in` hoặc `slow steady push-in` | `zoom in` |
| Dolly out | `slow dolly-out revealing context` | `pull back fast` |
| Pan | `slow horizontal pan` | `pan while zooming` |
| Tilt | `tilt up slowly` / `tilt down` | — |
| Static | `static locked frame, no camera movement` | `no camera shake` |
| Tracking | `lateral tracking shot moving with subject` | `orbit around` |
| Low angle | `low ground-level angle looking up at figure` | — |
| Over-shoulder | `over-the-shoulder framing, camera behind figure` | — |

> [!NOTE]
> **1 camera movement per generation.** Không mix nhiều movements trong 1 clip.
> VEO weights đầu prompt → front-load camera movement + shot type.

---

## Workflow thực tế (updated)

```
1. Tất cả ingredients đã upload lên Flow (@tags ready)
2. Generate source frame với Nano Banana (dùng @tags + shot prompt)
3. Boss approve frame → animate với VEO 3
4. Paste Universal Prompt vào VEO → dùng @tags trong text
5. Dùng "Add to Scene" cho shot tiếp theo cùng location
6. Dùng "Jump To" khi đổi location (+ ENV bridge shot)
7. Clip sai → fallback protocol, viết prompt riêng
8. Strip audio VEO nếu lạ: ffmpeg -i input.mp4 -an output.mp4
9. Overlay nhạc trong Scenebuilder hoặc editor
```

---

## Core rule

Ảnh tốt + universal prompt đúng = 90% công việc xong. Kiểm soát thật sự đến từ **chất lượng ảnh gốc** — prompt chỉ là lớp hướng dẫn thêm về camera, style, audio.

Mọi clip phải có thể chạm tay vào được.
