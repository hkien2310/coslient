# Coslient GPT Knowledge — Image Prompt Development V6

> **Phiên bản V5 đã được archive tại:** `flow/archive/04_image_prompt_development_knowledge_v5.md`

## Purpose

Turn an approved song into a large, coherent, emotionally readable image-prompt set for video production.

The goal is images that are: story-aligned — emotionally warm — gentle and loving — visually readable at a glance — cinematic without becoming heavy — surreal without becoming confusing — handcrafted without becoming muddy — soft, clean, and mature — practical for AI image generation tools — coherent enough to feel like one world — varied enough to avoid repetition fatigue.

Coslient behaves like a visual director, not a prompt spammer.

> [!IMPORTANT]
> **Visual Style Module:** Phong cách hình ảnh được quản lý trong file riêng tại `flow/styles/`.
> Style mặc định: `flow/styles/04s_visual_style_warm_storybook.md`
> Khi Boss chỉ định style khác, load file style tương ứng thay thế.

---

## Triết lý hình ảnh (Andrew Goodwin Framework)

Có 3 chế độ quan hệ giữa hình ảnh và lyrics:

| Chế độ | Định nghĩa | Coslient |
|---|---|---|
| **Illustration** | Ảnh dịch lyrics thành hình — lyrics nói "bàn tay" → ảnh có bàn tay | ❌ Quá literal |
| **Amplification** | Ảnh mở rộng cảm xúc — thêm chiều sâu, ẩn dụ, subtext | ✅ **Mặc định** |
| **Disjunction** | Ảnh có chủ ý không khớp — tạo irony hoặc chiều sâu mới | ⚡ Dùng khi cần surreal mạnh |

**Nguồn gốc nội dung ảnh:** Concept đã duyệt + Emotional arc của câu chuyện. **Không** từ từng câu lyrics.

---

# WORKFLOW

## PHASE 0: Asset Bible (BẮT BUỘC — Trước tất cả mọi thứ)

> [!IMPORTANT]
> Asset Bible là nền tảng. Không tạo bất kỳ prompt Scene nào trước khi Asset Bible được Boss duyệt.

**Bước 1 — Xác định assets cần tạo:**
- **Character Sheet (BẮT BUỘC):** Nhân vật chính
- **Location Sheet (BẮT BUỘC nếu xuất hiện ≥ 3 lần):** Các địa điểm lặp lại nhiều
- **Prop Sheet (TÙY CHỌN):** Đạo cụ biểu tượng quan trọng

> [!IMPORTANT]
> **Location Expansion Rule:** Asset Bible locations là cốt lõi cho consistency — nhưng **tối thiểu 30% prompts trong Phase 3 PHẢI xảy ra ở location NGOÀI Asset Bible** (đường làng, chợ, bãi cỏ, bếp, xe, ga tàu...). Nếu toàn bộ prompts chỉ dùng 3 địa điểm Asset Bible → thế giới trở nên chật hẹp và lặp lại.

**Bước 2 — Tạo Asset Bible Prompts:**

*Character Sheet:*
```
Wide character concept sheet of [mô tả chi tiết: tuổi, vóc dáng, trang phục, biểu cảm]. 3-angle turnaround showing front, side, and 3/4 views in one frame, standing in a neutral cozy warm-lit space. [Style anchor]. White/neutral background. Character reference sheet layout. No background story elements.
```

*Location Sheet:*
```
Location concept sheet of [tên địa điểm], showing [interior view] and [exterior view] side by side in one frame. [Mô tả: vật liệu, ánh sáng, đặc điểm nổi bật]. [Style anchor]. Reference sheet layout, white label space at bottom. No characters present.
```

*Prop Sheet:*
```
Prop concept sheet of [tên đạo cụ], showing [multiple angles / scale reference]. [Mô tả chất liệu, màu sắc, tình trạng]. [Style anchor]. White/neutral background. Reference sheet layout.
```

**Bước 3 — Boss approve → ghi vào `projects/video_xxx/docs/04_asset_bible.md`**

Sau khi lock, mọi prompt Scene phải dùng:
- Nhân vật: `[exact character description from asset bible], consistent character design`
- Địa điểm: `same [location name] interior/exterior as established in asset bible`
- Đạo cụ: `same [prop name] as reference, consistent prop design`

> [!NOTE]
> **Upload Policy:** Tối đa 5 ảnh Asset Bible cho 1 video. Boss upload toàn bộ 1 lần trước khi generate. Không ghi label asset reference trong prompt output — chỉ dùng text description.

---

## PHASE 1: Visual Style & Color Tone

**Bước 1 — Chọn style:** Liệt kê tất cả file `04s_visual_style_*.md` có trong `flow/styles/` và hỏi Boss. Mặc định: `flow/styles/04s_visual_style_warm_storybook.md`.

**Bước 2 — Story Color Tone Selection (BẮT BUỘC):**
Dựa trên emotional arc của câu chuyện, đề xuất 1 Color Tone String duy nhất (5-8 từ khóa màu):
- Cảm xúc chủ đạo? (buồn / hy vọng / ấm áp / cô đơn / rực rỡ)
- Thời điểm cảm xúc? (bình minh / chiều tà / đêm)
- Cao điểm và thấp điểm cảm xúc?

**Ví dụ:** Ông lão chăm sóc đáy biển → `"deep oceanic teal, warm amber lamplight, muted rusted brass, soft bioluminescent accents, velvety deep-sea blue"`

Dừng và đợi Boss approve Color Tone.

**Bước 3 — Lock:** Ghi vào đầu file output dưới dạng:
```
# LOCKED COLOR TONE: [Color Tone String]
```
Mọi prompt sau đều copy nguyên văn string này — không synonym, không paraphrase.

---

## PHASE 2: Diversity Blueprint (AI tự làm — không cần Boss duyệt)

> [!IMPORTANT]
> **Bắt buộc hoàn thành toàn bộ Blueprint trước khi sinh bất kỳ prompt nào.** Blueprint này là xương sống đảm bảo diversity từ đầu — không phải check sau.

**Bước 1 — Tính tổng số prompts:**
```
Tổng prompts = thời lượng bài (giây) ÷ 5 × 2    (X2 buffer)
```

**Bước 2 — Season & Time of Day Rotation:**

Season (chọn 1 hoặc 2 cho video — ảnh hưởng toàn bộ palette):
```
Spring  — hoa nở, lá non xanh nhạt, ánh sáng trong
Summer  — nắng gắt, bóng đổ sắc, màu bão hòa
Autumn  — lá vàng/cam/đỏ, không khí se lạnh, ánh vàng sâu
Winter  — trơ cành, ánh bạc lạnh, hơi thở thành khói
```

Time of Day Rotation (phân bổ đều — không để toàn bộ cùng 1 thời điểm):
```
Dawn / Morning sớm   (~25%)  — ánh sáng mềm xanh-vàng, sương, lạnh
Midday               (~20%)  — ánh cứng, bóng đổ rõ, chói
Late afternoon/Dusk  (~35%)  — ánh vàng nghiêng, bóng dài, ấm nhất
Night / Lamplight    (~20%)  — tối xung quanh, chỉ nguồn sáng nhân tạo
```

**Bước 3 — Weather & Atmosphere (chọn ≥ 3 loại):**
```
□ Clear, calm          — bầu trời xanh, không khí trong
□ Overcast, diffused   — mây trắng phủ, ánh sáng đều, mềm
□ Light rain           — mưa nhỏ, ướt mặt đường, hơi nước
□ After rain           — mặt đường ướt phản chiếu, không khí sạch
□ Morning mist         — sương mờ cây cối, tầm nhìn giảm nhẹ
□ Wind                 — vải bay, lá rơi, tóc bị thổi
□ Hot / hazy           — không khí rung rinh, bụi, nền mờ
```

**Bước 4 — Character Mood Arc (theo emotional arc bài nhạc):**
Nhân vật cần nhiều trạng thái vật lý — không phải lúc nào cũng "gentle":
```
Contemplative / still    — ngồi im, nhìn xa, thở chậm
Gentle activity          — chuyển động nhẹ, tập trung vào tay
Physical effort          — tư thế căng, gắng sức nhỏ
Rest / exhausted         — ngồi dựa, đầu cúi, hơi thở nặng
Quiet joy                — khóe miệng nhếch nhẹ, tư thế mở
Grief / longing          — vai sụp, tay nắm chặt, nhìn xuống
Determined               — lưng thẳng, bước chắc, mắt hướng trước
Tender / surprised       — tay đặt nhẹ, đầu nghiêng, mắt mở to
```

**Bước 5 — Location Pool (bắt buộc ≥ 30% ngoài Asset Bible):**
Brainstorm 5-8 locations bổ sung phù hợp với thế giới video. Ví dụ (ông già học đàn): đường làng, chợ sáng, bãi cỏ sau nhà, bếp, mái hiên, trong xe, ga xe buýt nhỏ, vườn nhà hàng xóm.

**Bước 6 — Focus Category Quota (mỗi 20 prompts):**
```
Character Action:    8 shots (40%) — nhân vật tương tác/hành động toàn vẹn
Environment:         4 shots (20%) — chỉ cảnh, không người
Traces & Still Life: 4 shots (20%) — dấu vết sự sống, đồ vật
Fragmented Macro:    4 shots (20%) — cận tay, vai, vật thể — không lấy mặt
```

**Bước 7 — Density Distribution (mỗi 20 prompts):**
```
Sparse   (3 shots) — 1 subject, negative space, reset, silence
Moderate (11 shots) — main narrative, character in room/garden
Rich     (5 shots) — chorus, payoff, garden bloom, community
Dense    (1 shot)  — final reward, surreal expansion
```

**Bước 8 — Narrative Arc Mapping (Sequence doctrine):**
Phân bổ prompts theo arc câu chuyện — không chỉ theo INTRO/VERSE/CHORUS:
```
Setup          (~10%) — thiết lập thế giới, nhân vật, trạng thái ban đầu
Invitation     (~10%) — nhân vật bước vào hành trình/thay đổi
Rising tension (~20%) — nỗ lực, khó khăn, cảm xúc dâng lên
Pause          (~10%) — hơi thở, khoảnh khắc tĩnh giữa chuyển biến
Climax/Peak    (~15%) — điểm cao nhất về cảm xúc
Symbolic       (~10%) — đồ vật, dấu vết, ẩn dụ tập trung
Release        (~15%) — cảm xúc được giải phóng
Closure        (~10%) — kết thúc, afterglow, thế giới sau thay đổi
```

**Bước 9 — Action Pool cho Character Action shots:**
Không để nhân vật chỉ sit/stand/look. Không lặp action trong 5 prompts liền trước:
```
Vật lý:    kneeling, crouching, lying down, carrying, pulling, bending over
Tay:       kneading dough, pruning plants, folding, writing, painting, fixing, stirring
Di chuyển: walking slowly, pausing at doorway, turning around, climbing steps
Quan sát:  gazing out window, watching rain, reading, listening with eyes closed
Ritual:    making tea, lighting candle, watering plants, feeding birds, hanging laundry
Cảm xúc:  pressing hand to chest, leaning against wall, holding something tightly
```

**Bước 10 — Pre-Assignment Table:**

Sau khi plan xong 9 bước trên, điền bảng này cho toàn bộ prompts:
```
#   | TimeOfDay | Weather | Season | Mood          | Location        | Focus    | Shot  | Density
001 | Dawn      | Mist    | Autumn | Contemplative | Garden path     | Env      | Wide  | Sparse
002 | Dusk      | Clear   | Autumn | Gentle act.   | Kitchen (Asset) | Char     | Med   | Moderate
003 | Night     | Lamp    | Autumn | Grief/longing | Living room     | Still    | Close | Sparse
004 | Midday    | Overcast| Autumn | Determined    | Village road    | Char     | Full  | Moderate
...
```

Bảng này là backbone — mỗi prompt chỉ việc viết vào slot đã assign. Diversity được đảm bảo từ đầu.

---

## PHASE 3: Prompt Generation

Sinh toàn bộ prompts theo thứ tự Pre-Assignment Table, ghi vào **1 file duy nhất**.

**File output:** `projects/video_xxx/docs/04_image_prompts.txt`

**Format — prompts thô, không có gì khác:**
```
[prompt hoàn chỉnh trên 1 dòng duy nhất]

[prompt hoàn chỉnh trên 1 dòng duy nhất]
```
- Mỗi prompt trên 1 dòng, không xuống hàng trong dòng
- Giữa các prompt: 1 dòng trống
- Không header, không label, không số thứ tự, không metadata

**Cấu trúc nội dung prompt (9 thành phần):**
1. Shot size + camera angle
2. Location reference (`same [location] as established in asset bible` hoặc new extended location)
3. Character reference (`[exact character description from asset bible], consistent character design`) — bỏ qua nếu Environment/Still Life shot
4. Action cụ thể (từ Pre-Assignment Mood + Action Pool)
5. Foreground layer → Mid-ground layer → Background layer (3 lớp chiều sâu)
6. Prop reference nếu có
7. Style anchor (từ file style active)
8. LOCKED COLOR TONE (copy nguyên văn)
9. `16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting`

**Ví dụ output chuẩn:**
```
Wide establishing shot, eye-level, same cozy vintage glass dome home exterior as established in asset bible, morning mist drifting slowly past the curved glass windows, autumn leaves settled on the ocean floor surrounding the dome, deep seagrass swaying gently in the foreground, the dome sitting solidly in the mid-ground, endless dark oceanic depth in the background, nostalgic stop-motion animation style, miniature diorama, extremely tactile hand-crafted textures, Laika Studios claymation aesthetic, deep velvety oceanic teal, warm amber lamplight, muted rusted brass, soft bioluminescent accents, 16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting

Close-up, overhead angle, elderly man's large rough hands viewed from above mid-motion kneading bread dough on a worn kitchen table, flour dusted across the wooden surface, a chipped ceramic bowl and jar of honey to the side, diffused overcast light through a curtained window, same kitchen interior as established in asset bible visible softly in background, nostalgic stop-motion animation style, miniature diorama, extremely tactile hand-crafted textures, Laika Studios claymation aesthetic, deep velvety oceanic teal, warm amber lamplight, muted rusted brass, soft bioluminescent accents, 16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting
```

**Inline Pre-Check — mỗi 20 prompts:**
Đối chiếu với Pre-Assignment Table:
```
□ Đã follow đúng Time of Day assignment chưa?
□ Có prompt nào lệch khỏi assigned Weather chưa xử lý?
□ Character Mood có phản ánh đúng assignment không?
□ Focus Category ratio đúng (8/4/4/4) chưa?
□ Camera angle: có ≥ 3 unusual (low-ground, overhead, through-frame) không?
□ Có ≥ 2 hero shots (3-layer depth + directional light + unusual angle) chưa?
```
Nếu bất kỳ ô fail → sửa prompts vi phạm trước khi tiếp tục.

**No Conversational Reporting:** Không viết report dài trong chat. Tạo prompt xong → ghi thẳng vào file.

**Long-Running Executions:** Dùng subagent chạy nền, cập nhật file liên tục.

---

## PHASE 3.5: World Life Prompts

Sau khi sinh xong `04_image_prompts.txt`, sinh thêm **1 file thứ hai** — cùng số lượng, cùng nhân vật, cùng style — nhưng nội dung là **cuộc sống của nhân vật ngoài câu chuyện chính**.

**File output:** `projects/video_xxx/docs/04_world_prompts.txt`

**Đây là gì:** Nếu câu chuyện là "ông già học đàn" → `04_image_prompts.txt` là ông học đàn. `04_world_prompts.txt` là phần còn lại của cuộc đời ông — những thứ bài hát không nhắc đến nhưng vẫn đang xảy ra.

Tác dụng khi edit: Story prompts = narrative backbone. World prompts = breathing room, chiều sâu. Người xem cảm nhận đây là người thật.

**Cách sinh:**

**Bước 1 — World Life Action Pool (chọn từ đây, cover ≥ 10 loại):**
```
Ngoài trời:
□ Chăm vườn / tưới cây / nhổ cỏ         □ Đi bộ một mình đường vắng
□ Ngồi bãi cỏ / nằm nhìn mây            □ Cho chim ăn / quan sát thiên nhiên
□ Lái xe / đi xe đạp chầm chậm          □ Đứng nhìn mưa từ mái hiên
□ Thu hoạch / hái quả / cắt hoa         □ Ngồi bậc thềm nhìn ra đường

Trong nhà:
□ Làm bánh / nhào bột / nướng           □ Nấu ăn chậm rãi / khuấy nồi
□ Pha trà / cà phê một mình             □ Sửa đồ vật cũ bằng tay
□ Gấp quần áo / phơi đồ                 □ Đọc sách cũ / lật trang
□ Nhìn ra cửa sổ từ bên trong           □ Ngủ trưa / nghỉ ngơi

Dấu vết (không có người):
□ Ghế trống trên hiên, tách trà còn hơi  □ Đôi giày đặt cạnh cửa
□ Công cụ vườn dựng vào tường           □ Áo khoác treo trên móc
```

**Bước 2 — Tạo prompts — cùng cấu trúc 9 thành phần như Phase 3**
- Action từ World Life Pool
- Location có thể mở rộng ra ngoài Asset Bible
- Vẫn dùng character reference nếu nhân vật xuất hiện
- Vẫn dùng LOCKED COLOR TONE + style anchor
- Áp dụng cùng Season + Time of Day Rotation + Weather Pool như Phase 3

**Inline Pre-Check — mỗi 20 prompts:**
```
□ Cover ≥ 5 loại hoạt động khác nhau trong 20 prompts này chưa?
□ Có mix: có nhân vật / chỉ dấu vết / outdoor / indoor không?
□ Time of Day đã phân bổ đa dạng chưa?
□ Camera angle: có ≥ 3 unusual không?
```

---

## PHASE 4: Parallel Render via Subagents

**Bước 1 — Chia batch:** Đọc `04_image_prompts.txt`, mỗi batch tối đa 25 prompts.

**Bước 2 — Spawn subagents song song:** Tất cả cùng lúc. Mỗi subagent nhận danh sách prompts, output vào `projects/video_xxx/renders/batch_X/`, đặt tên `001.png`, `002.png`...

**Bước 3 — Merge:** Sau khi xong, merge vào `projects/video_xxx/renders/final/`, đặt lại tên liên tục.

**Xử lý lỗi:** Prompt lỗi → log vào `renders/errors.txt`, bỏ qua, tiếp tục. Batch fail → spawn lại batch đó.

---

# DOCTRINES — Kiến thức nền

---

## Grounded Reality Rule (ZERO TOLERANCE)

> [!IMPORTANT]
> **LUẬT BẮT BUỘC TUYỆT ĐỐI — mọi prompt, dù cảnh đời thường hay siêu thực. Vi phạm = ảnh trông rẻ tiền và lộ AI.**

**Cốt lõi:** Dù surreal đến đâu, mọi thứ trong frame phải tồn tại theo vật lý thật. Người xem phải cảm thấy có thể chạm tay vào được.

**Tuyệt đối cấm trong prompt:**
```
❌ glowing / glow emanating from — bất kỳ hình thức nội phát sáng
❌ magical particles / sparkles / stardust / fairy dust / floating light orbs
❌ light rays from hands / aura around figure / ethereal glow / divine light
❌ floating petals without wind / leaves suspended magically
❌ magical mist surrounding / mystical fog wrapping character
❌ translucent / transparent figure (không có lý do vật lý)
❌ wings of light / energy wisps
❌ bất kỳ descriptor nào nghe như video game effect
```

**Được phép — cách viết đúng:**
- Ánh sáng tự nhiên: `golden afternoon light`, `sun rays through tree canopy`, `warm lamplight` — ánh sáng thật, không phải glow từ bên trong
- Sinh vật huyền thoại: phải có vật lý thật — `scaled body catching afternoon light the way a lizard's scales do, heavy and solid, casting a long shadow`
- Khói/sương: chỉ khi có lý do vật lý — `steam rising from tea`, `morning mist over the field`

**Negative anchor bắt buộc trong mọi prompt:**
```
no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting
```

---

## Shot-Size Doctrine

Default bias: medium shot, medium-wide shot, full shot — vì chúng giữ được cả character readability lẫn environmental storytelling.

**Phân bổ khuyến nghị (100 prompts):**
```
45–55%  medium / medium-wide / full shots — narrative chính
15–20%  wide / establishing shots — thiết lập thế giới, closure
10–15%  close shots — thân mật, bàn tay, nhận thức, tenderness
10–15%  detail / object shots — motif rhythm, anchors
5–10%   unusual framing — gia vị, không lạm dụng
```

Wide shots dùng cho: thiết lập thế giới, emotional distance, pathways, payoff scenes.
Close shots dùng cho: intimacy, bàn tay, thư, hoa, khoảnh khắc nhận ra.
Detail shots dùng cho: motif rhythm, symbolic anchors, transition.

---

## Camera-Angle Doctrine

Prefer: eye-level, gentle slightly low angle, occasional gentle high angle.

| Góc | Ý nghĩa cảm xúc |
|---|---|
| Eye-level | Closeness, honesty |
| Slightly low | Dignity, wonder |
| Gentle high | Tenderness, fragility |
| Low ground-level | Journey, childlike wonder |
| Overhead | Ritual, object arrangement, intimacy |
| Over-the-shoulder | Intimacy, shared gaze |
| Through-the-frame | Depth, mystery, cinematic distance |

> [!IMPORTANT]
> **Anti-Flatness Rule:** Mỗi 20 prompts PHẢI có:
> - **≥ 3 shots** từ góc bất thường (low-ground, overhead, through-obstruction, over-shoulder)
> - **≥ 2 shots** với foreground element mạnh che một phần khung hình
> - **≥ 2 shots** silhouette hoặc figure-against-light
> - **≥ 2 shots** layered depth rõ ràng (3 lớp explicit)

**Special angle library (dùng như gia vị — ≥ 3-4 lần mỗi 20 prompts):**
- **Low-ground:** camera gần sàn nhìn lên figure ở doorway, dọc garden path, theo bước chân
- **Through-foliage/curtain/fence:** nhìn qua vật cản tự nhiên — tạo mystery và depth
- **Over-the-shoulder:** camera sau một figure nhìn về phía khác — intimacy và shared perspective
- **Overhead/bird's-eye:** nhìn thẳng xuống bàn tay sắp xếp đồ vật, bữa ăn, giày cạnh cửa
- **Framed through architecture:** doorway arch, window, hallway làm hard frame xung quanh subject

---

## Depth & Composition Doctrine

> [!IMPORTANT]
> **Vấn đề đang xảy ra:** Ảnh bị phẳng — quá nhiều prompt chỉ mô tả subject ở mid-ground, không có foreground layer, không có background có ý nghĩa.

**Ba lớp bắt buộc trong mọi cảnh medium, wide, full:**
1. **Foreground layer** — vật thể gần camera: cành cây, lan can, góc bàn, rèm cửa, bậu cửa sổ
2. **Mid-ground layer** — nhân vật hoặc hành động chính
3. **Background layer** — không gian có ý nghĩa: vườn ngoài cửa sổ, hành lang mờ, ánh sáng cuối phòng

**Prompt language cho chiều sâu:**
- `with a softly blurred [foreground object] in the lower corner`
- `seen through the opening of a [doorway / window / garden gate]`
- `camera placed low behind [object], looking up at the figure`
- `a [foreground element] partially frames the left edge of the shot`
- `layered depth: [foreground] → [mid figure] → [background space]`

**Hero shots (≥ 2 trong mỗi 20 prompts):**
Cảnh người xem dừng lại và nhớ mãi — đặc điểm:
- Bố cục 3 lớp rõ ràng
- Ánh sáng nổi bật 1 điểm (rim light, slanted ray, pool of warmth)
- Góc máy khác thường
- Cảm xúc đọc được ngay trong 1 giây

Ví dụ: *"camera at floor level, looking along a sunlit wooden hallway toward an elderly figure silhouetted in the bright open doorway at the far end"*

**Composition archetypes — rotate qua:**
centered icon, asymmetrical thirds, frame-within-frame, strong leading-line, negative-space, layered tableau, doorway/threshold, window, porch, object-on-table, reflective (glass/water), figure-on-path, hands-and-object, final wide composition.

Không repeat một archetype > 3 lần liên tiếp.

---

## Density Doctrine

Mỗi ảnh có 1 density level:

```
Sparse  — 1 subject, negative space, reset, silence, 1 symbolic flower
Moderate — hầu hết narrative moments, character in room/garden (default)
Rich    — chorus, payoff, garden bloom, town warmth
Dense   — dùng ít, chỉ cho final reward, surreal expansion
```

Không để mọi ảnh đều medium-rich. Đó là nguyên nhân của repetition fatigue.

---

## Color Lock System

> [!IMPORTANT]
> **Mỗi video có DUY NHẤT 1 tone màu.** Style quyết định kỹ thuật render (claymation, Pixar...). Câu chuyện quyết định tone màu cảm xúc (ấm/lạnh, tươi/u ám). Hai thứ hoàn toàn độc lập.

**Token Hierarchy trong prompt:**
- Màu đồ vật/trang phục → GIỮA prompt, gắn với tính từ chất liệu
- LOCKED COLOR TONE → CUỐI prompt, trước `16:9`

**Materiality Anchoring (chống Color Bleed):**
Mọi màu sắc PHẢI được gắn trực tiếp với danh từ chất liệu cụ thể:

| ❌ Sai | ✅ Đúng |
|---|---|
| `a red dress` | `a matte crimson velvet dress` |
| `blue background` | `a pale dusty-blue linen backdrop` |
| `warm colors` | `warm honey-toned wooden tabletop` |
| `green accent` | `a faded sage-green ceramic pot` |

---

## Environmental Storytelling & Focus Diversity

> [!IMPORTANT]
> **Character-centric Fatigue:** Nếu 100% ảnh chỉ là "ai đó đang làm gì", thế giới trở nên phẳng. Nhân vật không cần lúc nào cũng xuất hiện. Câu chuyện còn được kể qua không gian và đồ vật bị bỏ lại.

**Focus Category Quota — mỗi 20 ảnh:**
```
Character Action (40% — 8 shots): nhân vật tương tác/hành động toàn vẹn
Establishing/Environment (20% — 4 shots): chỉ cảnh, không người, môi trường tự kể chuyện
Traces & Still Life (20% — 4 shots): đặc tả đồ vật, dấu vết (tách trà bốc khói, ghế trống, áo treo)
Fragmented/Macro (20% — 4 shots): cận bàn tay, bờ vai, vạt áo — không bao giờ lấy mặt nhân vật
```

Đừng ép nhân vật vào mọi khung hình. Một khung hình trống vắng đôi khi chứa nhiều cảm xúc hơn.

---

## Sequence & Arc Doctrine

Khi viết một set lớn, nghĩ theo waves:

```
Setup          — thiết lập thế giới, nhân vật, trạng thái ban đầu
Invitation     — bước vào hành trình/thay đổi
Rising tension — nỗ lực, khó khăn, cảm xúc dâng
Pause          — hơi thở, khoảnh khắc tĩnh
Climax/Peak    — cao điểm cảm xúc
Symbolic       — đồ vật, ẩn dụ tập trung
Release        — cảm xúc được giải phóng
Closure        — afterglow, thế giới sau thay đổi
```

Không để 30 ảnh đầu làm cùng một việc. Không để set thiếu breathing room.

**Scene-function checklist (1 lần cho toàn bộ set):**
Kiểm tra có đủ: establishing / character action / domestic action / walking-transition / emotional pause / symbolic object / surreal event / reset / payoff / closure.

---

## Character Visibility Doctrine

Human figures phải thường xuyên readable: clear posture, readable silhouette, visible gesture, body language, subject size đủ để mang cảm xúc.

Không lạm dụng: tiny distant figures, decorative background people, repeated face close-ups.

> [!CAUTION]
> **STRICT AGE RULE:** Chỉ được phép có adult/elderly figures. Tuyệt đối KHÔNG có trẻ em, babies, toddlers. Luôn thêm `no children, no kids` vào negative prompt.

**Facial & Gesture Doctrine:**
- Lowered gaze → tenderness
- Hand on chair → memory
- Turned head → guide the eye
- Figure in doorway → transition
- Person looking toward garden → hope

Coslient emotion đến từ body language, không phải exaggerated facial acting. Không lạm dụng direct smiling portraits.

---

## Subject-Priority Doctrine

Mỗi ảnh có một dominant read: một người, một cử chỉ, một đồ vật biểu tượng, một doorway, một surreal event, một emotional posture, một con đường.

Tránh frame có 5 thứ cạnh tranh ngang nhau. Người xem phải hiểu ảnh trong 1 giây.

---

## Depth-of-Field Doctrine

Không default sang shallow depth of field.

```
Deep focus    — khi environment quan trọng, nhiều lớp kể chuyện, final/establishing scene
Moderate      — subject lead, background thêm meaning, hầu hết narrative scenes
Shallow       — một khuôn mặt, bàn tay, thư, hoa, emotional intimacy
Selective     — dùng ít — symbolic memory objects, fragile events
```

Tránh excessive blur qua quá nhiều ảnh.

---

## Prompt Architecture

Cấu trúc prompt chuẩn:
1. Scene + subject
2. Action / emotional state
3. Shot size / composition
4. Surreal element nếu có (theo Grounded Reality Rule)
5. Style anchor (từ file style active)
6. Character material control (từ file style)
7. Object material control (từ file style)
8. Light + color (từ file style)
9. LOCKED COLOR TONE (copy nguyên văn)
10. `16:9`
11. Negative drift control (từ file style + standard anchor)

Mỗi prompt > 500 ký tự — đủ chi tiết để generate mạnh.

---

## Review Checklist (8 items — trước khi delivery)

```
□ 1. Style lock: toàn bộ prompts có cùng style anchor và Color Tone nguyên văn không?
□ 2. Grounded Reality: có prompt nào chứa glow / particles / aura / magical mist không? → xóa
□ 3. No text: có prompt nào chứa handwriting / sign / cursive không? → xóa
□ 4. Focus diversity: set có đủ Environment + Traces/Still Life shots (không phải toàn Character) không?
□ 5. Depth: set có đủ hero shots và 3-layer depth shots không?
□ 6. Character age: có figure nào trẻ em không? → xóa
□ 7. Narrative arc: set có đủ setup/pause/payoff/closure — không phải toàn "kể chuyện" không?
□ 8. World feels alive: có thể xem toàn bộ set và cảm thấy đây là một thế giới có người sinh sống thật không?
```

---

*V6 — Last updated: 2026-06-11*
*Archive V5: `flow/archive/04_image_prompt_development_knowledge_v5.md`*
