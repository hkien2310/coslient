# Coslient GPT Knowledge — Image Prompt Development V7

> **Phiên bản V6 đã được archive tại:** `flow/archive/04_image_prompt_development_knowledge_v6.md`

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

## PHASE -1: Song Intake (AI tự làm — invisible, không báo Boss)

> [!IMPORTANT]
> Bước này chạy TRƯỚC mọi thứ khác. Hoàn toàn internal — không output ra chat, không hỏi Boss.
> Đây là bước AI "đọc kịch bản" trước khi bắt đầu làm việc.

Khi Boss nói "làm ảnh video X":

**Bước 1 — Đọc 3 files theo thứ tự:**
- `projects/video_xxx/docs/01_idea.md` → story seed, emotional intent ban đầu
- `projects/video_xxx/docs/02_concept.md` → VISUAL WORLD, nhân vật, setting đã approve
- `projects/video_xxx/docs/03_song.md` → cấu trúc nhạc, leitmotif, emotional mode, energy map

**Bước 2 — Extract 5 thứ vào working memory (không output):**

**A. LEITMOTIF OBJECT** — Tìm section B5.6 trong file bài hát:
- Vật thể là gì? Xuất hiện mấy lần? Emotional load mỗi lần?
- **Nếu không có leitmotif trong file:** AI tự đề xuất 1 vật thể phù hợp với câu chuyện và concept (đồ vật bình thường, gắn với nhân vật chính, có thể evolve emotional context qua 4 lần xuất hiện). Ghi vào working memory, không hỏi Boss.

**B. EMOTIONAL MODE** — Tìm section B2.5: A / B / C / D
- Nếu không có: AI tự suy luận từ lyrics và concept. Default Mode A nếu không rõ.

| Mode | Tên | Visual Bias |
|---|---|---|
| A | Bittersweet Return | Warm objects, threshold shots, golden light |
| B | Peaceful Observation | Environment-heavy, wide + still life, luminous |
| C | Regret + CTA | Body language rõ, action-forward, slightly cooler |
| D | Cathartic Grief | Empty spaces, traces, absence, shadow detail |

**C. SONG STRUCTURE + TIMING** — Tìm F7:
- Pattern đã chọn (Classic Pop / Evolving Chorus / 2-phút...)
- Timing ước lượng từng section (giây)

**D. ENERGY MAP** — Tìm D1:
- % energy từng section (Intro 15-20%, Verse 25-35%, Chorus 75-85%, Bridge 25-40%, Final Chorus 95-100%)

**E. VISUAL WORLD** — Từ 02_concept.md:
- Mô tả thế giới hình ảnh đã approve (setting, atmosphere, palette cảm xúc)
- Sẽ dùng để cross-check Asset Bible — nếu có drift → tự điều chỉnh, không báo Boss

---

## PHASE 0: Asset Bible (BẮT BUỘC — Trước tất cả mọi thứ)

> [!IMPORTANT]
> Asset Bible là nền tảng. Không tạo bất kỳ prompt Scene nào trước khi Asset Bible được Boss duyệt.

**Bước 1 — Xác định assets cần tạo:**
- **Character Sheet (BẮT BUỘC):** Nhân vật chính
- **Location Sheet (BẮT BUỘC nếu xuất hiện ≥ 3 lần):** Các địa điểm lặp lại nhiều
- **Prop Sheet (TÙY CHỌN):** Đạo cụ biểu tượng quan trọng
- **Leitmotif Prop Sheet (BẮT BUỘC nếu Song Intake tìm thấy hoặc tự đề xuất Leitmotif Object):**
  Dùng Prop Sheet template để tạo reference cho vật thể leitmotif.
  Sau khi lock, ghi vào Pre-Assignment Table 3-4 slots cố định với tag [LEITMOTIF]:

  | Lần | Section ưu tiên | Emotional context trong prompt |
  |---|---|---|
  | Lần 1 | Intro / Verse 1 | **Neutral** — vật thể bình thường, không có subtext |
  | Lần 2 | Chorus 1 / Verse 2 | **Warm** — gắn với hành động có ý nghĩa, ai đó còn ở đây |
  | Lần 3 | Bridge / Chorus 2 | **Melancholy** — vật thể thay đổi trạng thái, vắng bóng ai đó |
  | Lần 4 | Outro / Final Chorus | **Transformed** — context đảo ngược hoàn toàn, ý nghĩa mới |

  Prompt của leitmotif shots: Still Life hoặc Fragmented Macro.
  Mô tả vật thể phải thay đổi subtle qua từng lần — không clone prompt cũ.

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
Dựa trên emotional arc của câu chuyện và Emotional Mode đã extract từ Phase -1, đề xuất 1 Color Tone String duy nhất (5-8 từ khóa màu):
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

**Hard cap: tối đa 120 prompts cho 1 file `04_image_prompts.txt`.**

```
Tổng prompts = min(song_duration_seconds ÷ 1.5, 120)
```

| Bài dài | Tổng prompts |
|---|---|
| 2 phút (120s) | 80 |
| 2.5 phút (150s) | 100 |
| 3 phút (180s) | 120 (cap) |
| 3.5 phút+ | 120 (cap) |

**Sau khi có tổng, phân bổ theo section bằng % cố định:**

| Section | % của tổng | Ví dụ (120 prompts) |
|---|---|---|
| Intro | 7% | 8 |
| Verse 1 | 15% | 18 |
| Pre-Chorus 1 | 5% | 6 |
| Chorus 1 | 13% | 16 |
| Verse 2 | 11% | 13 |
| Pre-Chorus 2 | 4% | 5 |
| Chorus 2 | 13% | 16 |
| Bridge | 7% | 8 |
| Final Chorus | 17% | 20 |
| Outro | 8% | 10 |
| **Total** | **100%** | **120** |

> [!NOTE]
> Nếu bài không có đủ sections (không có Bridge, không có Pre-Chorus): phân bổ % thừa vào Verse và Final Chorus. Không được vượt cap 120.
> Làm tròn xuống để không vượt tổng. Điều chỉnh ±1 ở Final Chorus nếu cộng lại lệch.


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

**Bước 4 — Character Mood Arc (theo Emotional Mode + arc bài nhạc):**
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
Brainstorm 5-8 locations bổ sung phù hợp với thế giới video và Visual World đã extract từ Phase -1.

**Bước 6 — Focus Category Quota (mỗi 20 prompts):**
```
Character Action:    8 shots (40%) — nhân vật tương tác/hành động toàn vẹn
Environment:         4 shots (20%) — chỉ cảnh, không người
Traces & Still Life: 4 shots (20%) — dấu vết sự sống, đồ vật
Fragmented Macro:    4 shots (20%) — cận tay, vai, vật thể — không lấy mặt
```

**Bước 7 — Density Distribution:**

Default flat ratio (mỗi 20 prompts khi không có section data):
```
Sparse   (3 shots) — 1 subject, negative space, reset, silence
Moderate (11 shots) — main narrative, character in room/garden
Rich     (5 shots) — chorus, payoff, garden bloom, community
Dense    (1 shot)  — final reward, surreal expansion
```

**Density Override theo Section (ưu tiên hơn flat ratio khi có section data):**

| Section | Sparse | Moderate | Rich | Dense |
|---|---|---|---|---|
| Intro | 60% | 30% | 10% | 0% |
| Verse | 20% | 60% | 15% | 5% |
| Pre-Chorus | 10% | 45% | 35% | 10% |
| Chorus | 5% | 30% | 45% | 20% |
| Bridge | 40% | 45% | 12% | 3% |
| Final Chorus | 0% | 15% | 45% | 40% |
| Outro | 65% | 30% | 5% | 0% |

**Bước 8 — Narrative Arc Mapping (theo Song Structure):**

Map narrative arc lên trên song sections — không tạo arc độc lập:

| Song Section | Narrative Function | Visual character |
|---|---|---|
| Intro | Setup — thiết lập thế giới | Sparse, wide, không nhân vật |
| Verse 1 | Rising tension đầu — nhân vật bước vào | Moderate, character introduced |
| Pre-Chorus | Invitation — cảm xúc dâng | Moderate-Rich, movement |
| Chorus 1 | Climax mức 1 | Rich, dynamic, leitmotif lần 2 |
| Verse 2 | Deeper story — đào sâu hơn V1 | Moderate, new angle/location |
| Chorus 2 | Climax mức 2 — lớn hơn C1 | Rich+, unusual angles |
| Bridge | Pause + Symbolic | Sparse-Moderate, still life heavy |
| Final Chorus | Peak + Release | Dense, hero shots concentrated |
| Outro | Closure — afterglow | Sparse, bookend với Intro |

> [!NOTE]
> Khi không có song structure rõ: dùng Narrative Arc cũ (Setup 10% / Invitation 10% / Rising tension 20% / Pause 10% / Climax 15% / Symbolic 10% / Release 15% / Closure 10%).

**Bước 8.5 — Opening Sequence + Closure Bookend:**

Làm NGAY SAU Bước 8, TRƯỚC khi điền Pre-Assignment Table.

**Opening Sequence — 3 prompts đầu tiên của INTRO:**
- **Prompt 1:** Wide establishing — thế giới, mùa, không khí — KHÔNG nhân vật. Sparse.
- **Prompt 2:** Environmental + dấu vết nhân vật (ánh đèn từ cửa sổ, khói bếp, đôi giày cạnh cửa). Không nhân vật.
- **Prompt 3:** Nhân vật xuất hiện lần đầu — Full shot, nhìn ra xa, KHÔNG nhìn camera.

→ 3 prompts này là 3 prompts được viết kỹ nhất toàn bộ set. Assign HERO flag cho ít nhất 1 trong 3.

**Closure Bookend — 2 prompts cuối của OUTRO:**
Phải echo prompt đầu tiên (Prompt 1 của Intro):
- Cùng location → nhưng khác thời điểm trong ngày (thường chiều tà hoặc đêm)
- Cùng composition archetype → nhưng KHÔNG có nhân vật
- Dấu vết thay cho người: ghế trống, cốc nguội, cửa khép nhẹ, ánh đèn tắt
- Density: Sparse. Không action. Chỉ still life.

→ Ghi rõ trong Pre-Assignment Table: **#001 (INTRO-OPEN)** và **#N (OUTRO-CLOSE)** là cặp bookend.

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

Điền bảng này cho toàn bộ prompts, có thêm cột SECTION và LEITMOTIF tracking:
```
#   | SECTION       | TimeOfDay | Weather  | Season | Mood          | Location        | Focus | Shot  | Density  | Special
001 | INTRO         | Dawn      | Mist     | Autumn | -             | Garden path     | Env   | Wide  | Sparse   | HERO, BOOKEND-OPEN
002 | INTRO         | Dawn      | Mist     | Autumn | -             | Kitchen window  | Trace | Wide  | Sparse   | -
003 | INTRO         | Dawn      | Mist     | Autumn | Contemplative | Garden path     | Char  | Full  | Moderate | -
004 | VERSE-1       | Dusk      | Clear    | Autumn | Gentle act.   | Kitchen (Asset) | Char  | Med   | Moderate | LEITMOTIF-1
...
N   | OUTRO         | Night     | Lamplight| Autumn | -             | Garden path     | Trace | Wide  | Sparse   | BOOKEND-CLOSE
```

Cột SECTION dùng để tracking nội bộ — không xuất hiện trong output file.
Bảng này là backbone — mỗi prompt chỉ việc viết vào slot đã assign.

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

**Cấu trúc nội dung prompt — Reference-Optimized (7 thành phần):**

> [!IMPORTANT]
> **Chúng ta dùng 1 character ref image duy nhất.** Model AI đã thấy hình nhân vật — không cần mô tả lại ngoại hình. Thay thế toàn bộ character physical description bằng **short identifier** (2-4 từ). Nếu không có nhân vật trong shot — bỏ qua hẳn.

1. Shot size + camera angle
2. Location (`same [location name] interior/exterior as established in asset bible` hoặc extended location mới)
3. **Character short ID** — **Bỏ qua nếu là Environment / Still Life / Trace shot**
   - Dùng: `the old man`, `he`, `the woman`, `her`, `the craftsman`... — không mô tả ngoại hình
   - Chỉ viết action + tư thế: `the old man kneeling slowly`, `he reaches toward the shelf`
4. Action cụ thể (từ Pre-Assignment Mood + Action Pool)
5. Foreground layer → Mid-ground layer → Background layer (3 lớp chiều sâu)
6. Style anchor (từ file style active)
7. LOCKED COLOR TONE (copy nguyên văn) + `16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting`

**Prop reference:** Nếu có prop sheet — dùng `same [prop name] as reference`. Nếu không có prop sheet — mô tả ngắn gọn.

---

**So sánh độ dài trước / sau ref optimization:**

```
❌ KHÔNG REF — 520 chờ:
Medium shot, low-ground angle, elderly man with silver hair and weathered calloused hands wearing a faded linen shirt and worn brown suspenders, consistent character design, sitting at same workshop interior as established in asset bible, slowly running his hands along the grain of a half-carved wooden boat on the workbench, woodshavings scattered in the foreground, his hands and torso in mid-ground, soft amber lamplight through dusty window in background, warm storybook illustration style, handcrafted texture, aged paper, soft amber and sage green, 16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting

✅ CÓ REF — 290 chờ:
Medium shot, low-ground angle, same workshop interior as established in asset bible, the old man sitting at the workbench slowly running his hands along the grain of a half-carved wooden boat, woodshavings scattered in the foreground, his hands and torso in mid-ground, soft amber lamplight through dusty window in background, warm storybook illustration style, handcrafted texture, aged paper, soft amber and sage green, 16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting
```

**Điều không bỏ được dù có ref:**
- Action cụ thể (model không đoán được)
- Tư thế / body language rõ ràng
- 3 lớp chiều sâu
- Style anchor + Color Tone
- Negative anchor

**Những gì cắt được khi có ref:**
- Toàn bộ mô tả vật lý (tóc, da, mắt, quần áo, tuổi...)
- `consistent character design` (ref đã handle)
- `exact character description from asset bible` (ref đã handle)

---

**Ví dụ output chuẩn (ref-optimized):**
```
Wide establishing shot, eye-level, same cozy vintage glass dome home exterior as established in asset bible, morning mist drifting past the curved glass windows, autumn leaves on the ocean floor in the foreground, the dome solid in the mid-ground, endless dark oceanic depth in the background, nostalgic stop-motion animation style, miniature diorama, extremely tactile hand-crafted textures, Laika Studios claymation aesthetic, deep velvety oceanic teal, warm amber lamplight, muted rusted brass, 16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting

Overhead close-up, same kitchen interior as established in asset bible, the old man's hands mid-motion kneading bread dough on a worn table, flour dusted across the wooden surface, a chipped ceramic bowl and jar of honey beside him, diffused morning light through a curtained window, nostalgic stop-motion animation style, miniature diorama, extremely tactile hand-crafted textures, Laika Studios claymation aesthetic, deep velvety oceanic teal, warm amber lamplight, muted rusted brass, 16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting

Medium shot, through-doorway framing, village road at dusk, the old man walking slowly with hands in pockets, long shadow stretching ahead on gravel in the foreground, his unhurried figure in the mid-ground, autumn trees lining the road curving out of sight in the background, nostalgic stop-motion animation style, miniature diorama, extremely tactile hand-crafted textures, Laika Studios claymation aesthetic, deep velvety oceanic teal, warm amber lamplight, muted rusted brass, 16:9, no internal glow, no magical particles, no sparkles, no children, no kids, no aura, no text, no handwriting
```


**Quality Gate — MANDATORY — chạy mỗi 20 prompts:**

Sau khi viết mỗi batch 20 prompts, dừng lại và chạy Deduplication Check:

```
DEDUPLICATION CHECK — Batch [X]:

Dimension 1 — Shot Type:
□ Kiểm tra 5 prompts trước có cùng Shot Size không? (all Wide, all Close, all Medium...)
□ Nếu có 4+ prompts cùng shot size liên tiếp → bắt buộc thay đổi 2 prompts đó

Dimension 2 — Location:
□ Liệt kê locations dùng trong batch này
□ Có location nào xuất hiện > 5 lần trong batch không? → phân bổ lại
□ Asset Bible locations: không vượt quá 70% của batch (30% phải là extended locations)

Dimension 3 — Action:
□ Liệt kê tất cả Character Action shots trong batch
□ Có action nào lặp lại trong 5 prompts liên tiếp không? → thay thế bằng action khác từ Action Pool

Dimension 4 — Time of Day:
□ So sánh phân bổ thực tế với target ratio (Dawn 25% / Midday 20% / Dusk 35% / Night 20%)
□ Nếu lệch > 15% từ target → điều chỉnh 3 prompts tiếp theo

Dimension 5 — Camera Angle:
□ Đếm unusual angles (low-ground, overhead, through-frame, over-shoulder)
□ Phải có ≥ 3 unusual angles trong mỗi 20 prompts
□ Eye-level không được vượt quá 50% của batch

Dimension 6 — Density:
□ So sánh Sparse/Moderate/Rich/Dense ratio với Density Override của section đang gen
□ Nếu có > 4 Moderate liên tiếp → insert 1 Sparse và 1 Rich

Fail bất kỳ ô nào → sửa prompts vi phạm TRƯỚC KHI tiếp tục gen batch tiếp theo.
```

**No Conversational Reporting:** Không viết report dài trong chat. Tạo prompt xong → ghi thẳng vào file.

**Long-Running Executions:** Dùng subagent chạy nền, cập nhật file liên tục.




## PHASE 4: Parallel Render via Subagents

> [!CAUTION]
> **NGHIÊM CẤM dùng Python script để generate ảnh.** Lý do: script crash giữa chừng không biết bao nhiêu ảnh đã xong, không có per-prompt retry, không có visibility, lỗi 1 prompt có thể drop cả batch.
>
> **BẮT BUỘC:** Dùng `invoke_subagent` native. Mỗi subagent nhận 1 batch, gọi image generation tool trực tiếp từng prompt một — không bọc trong script.

**Bước 1 — Đọc và chia batch:**
- Đọc `projects/video_xxx/docs/04_image_prompts.txt`
- Mỗi batch: tối đa **20 prompts** (không phải 25 — để subagent có headroom xử lý retry)
- Đánh số batch: `batch_01`, `batch_02`...

**Bước 2 — Spawn subagents song song (invoke_subagent):**

Spawn tất cả batch cùng lúc. Mỗi subagent nhận prompt sau:

```
Bạn là image generation agent cho batch [X].
Nhiệm vụ: Generate lần lượt từng prompt trong danh sách sau.
Output folder: projects/video_xxx/renders/batch_X/
Đặt tên file: [số thứ tự 3 chữ số].png (001.png, 002.png...)

Quy tắc:
- Generate từng prompt một, KHÔNG batch cùng lúc
- Nếu 1 prompt lỗi → log vào renders/errors.txt (ghi số thứ tự + prompt + lý do), bỏ qua, tiếp tục prompt tiếp theo
- Sau mỗi 5 prompts → update file renders/batch_X/progress.txt với số đã xong
- Không dùng Python script để call image gen API — dùng native tool trực tiếp
- Khi xong toàn bộ batch → báo cáo: tổng số xong / tổng số assign / số lỗi

[Danh sách prompts batch X]
```

**Bước 3 — Monitor:**
- Không poll liên tục. Hệ thống tự notify khi subagent xong.
- Kiểm tra `renders/batch_X/progress.txt` nếu cần biết tiến độ.

**Bước 4 — Merge sau khi tất cả batch xong:**
- Merge toàn bộ ảnh từ `renders/batch_X/` vào `renders/final/`
- Đặt lại tên liên tục: `001.png`, `002.png`...
- Dùng `run_command` với `cp` hoặc `mv` — không script

**Bước 5 — Xử lý lỗi:**
- Đọc `renders/errors.txt`
- Re-spawn subagent chỉ cho các prompts lỗi (không re-gen toàn bộ batch)
- Log final: tổng prompts / thành công / fail

---

# DOCTRINES — Kiến thức nền

---

## Render Safety Rule — Banned Words (ZERO TOLERANCE)

> [!CAUTION]
> **Một số từ/cụm từ kích hoạt content filter của image gen AI → prompt bị từ chối hoặc render ra ảnh sai hoàn toàn.** Kiểm tra toàn bộ prompts trước khi ghi file.

**Danh sách cấm tuyệt đối — và cách thay thế:**

| ❌ Cấm | ✅ Thay bằng |
|---|---|
| `dead leaves` | `fallen leaves`, `dried leaves`, `withered autumn leaves` |
| `dead of winter` | `deep winter`, `mid-winter stillness` |
| `dead calm` | `still air`, `motionless surface`, `windless morning` |
| `dying light` | `fading light`, `last light of evening`, `amber dusk glow` |
| `dying embers` | `glowing embers`, `fading coals`, `last warmth of the fire` |
| `dying` (bất kỳ) | `fading`, `aging`, `waning`, `last` |
| `dead` (bất kỳ) | `still`, `bare`, `quiet`, `empty`, `dried` |
| `death` | xóa khỏi prompt — không cần thiết trong Coslient |
| `corpse` / `body` | không dùng trong Coslient |
| `ghost` / `ghostly` | `faint`, `soft`, `barely visible`, `translucent shadow` |
| `haunted` / `haunting` | `evocative`, `stirring`, `deeply moving` |
| `decay` / `decaying` | `weathered`, `aged`, `time-worn`, `worn by years` |
| `rotting` / `rotten` | `aged wood`, `weathered timber`, `mossy old` |
| `withering` | `aging gracefully`, `worn at the edges` |
| `kill` / `killing` | không dùng — kể cả `killing light` → dùng `brilliant light` |
| `blood` | không dùng trong Coslient |
| `violence` / `violent` | không dùng trong Coslient |
| `nude` / `naked` | không dùng trong Coslient |
| `drug` / `drugs` | không dùng trong Coslient |
| `suicide` / `self-harm` | không dùng trong Coslient |
| `weapon` | không dùng trong Coslient |
| `real person name` | không tag tên người thật (celeb, politician...) |
| `brand name` | không tag thương hiệu có bản quyền |
| `child` / `children` / `kid` / `baby` | đã có trong negative anchor — không để trong body prompt |

**Cụm từ thường vô tình xuất hiện trong Coslient context — cần đặc biệt chú ý:**
```
"dead leaves blowing"   → "fallen leaves drifting"
"dying afternoon light" → "late afternoon amber light"
"ghost of a smile"     → "a faint smile", "the faintest curve of a smile"
"haunting melody"      → xóa — không cần descriptor âm nhạc trong image prompt
"decay of time"        → "marks of time", "weathered by years"
"withered hand"        → "aged hand", "time-worn hand", "gnarled and worn hand"
```

**Khi nào check:** Sau khi viết mỗi batch 20 prompts, scan nhanh toàn bộ từ trong batch.
Nếu phát hiện từ cấm → sửa ngay trước khi ghi vào file.

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

**Phân bổ khuyến nghị (120 prompts):**
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

## Chorus Visual Evolution Doctrine

> [!IMPORTANT]
> **Mỗi lần Chorus là một bước escalation — không phải bản copy của Chorus trước.**

Chorus là emotional peak. Nếu mọi Chorus trông giống nhau → người xem mất cảm nhận về hành trình.

**3 mức Chorus:**

| | Chorus 1 | Chorus 2 | Final Chorus |
|---|---|---|---|
| **Density** | Rich | Rich+ | Dense |
| **Shot composition** | Standard Rich — nhân vật + environment | Tăng complexity — unusual angle bắt buộc | Toàn Hero shots — mọi prompt phải memorable |
| **Camera** | Eye-level hoặc slightly low | At least 2 unusual angles | Low-ground + Through-frame dominant |
| **Foreground** | 1 foreground layer OK | Foreground bắt buộc dense/layered | Double foreground — 2 lớp trước subject |
| **Nhân vật** | Action có ý nghĩa | Action mạnh hơn hoặc emotional peak | Body language rõ nhất, silhouette hoặc motion blur |
| **Leitmotif** | Lần 2 (Warm) | Lần 3 (Melancholy) | Lần 4 (Transformed) nếu timing phù hợp |
| **Location** | Asset Bible location | Asset Bible + 1 extended location | Extended location hoặc surreal transformation nhẹ |

**Anti-repetition rules cho Chorus:**
- Không dùng cùng composition archetype giữa C1 và C2
- Không dùng cùng camera angle cho hero shot giữa C2 và Final Chorus
- Nếu C1 dùng Eye-level hero → C2 phải Low-ground hoặc Through-frame
- Final Chorus: bắt buộc ít nhất 1 shot mà người xem chưa thấy trong toàn bộ video trước đó

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

## Review Checklist (12 items — trước khi delivery)

```
□ 1.  Style lock: toàn bộ prompts có cùng style anchor và Color Tone nguyên văn không?
□ 2.  Grounded Reality: có prompt nào chứa glow / particles / aura / magical mist không? → xóa
□ 3.  No text: có prompt nào chứa handwriting / sign / cursive không? → xóa
□ 4.  Focus diversity: set có đủ Environment + Traces/Still Life shots (không phải toàn Character) không?
□ 5.  Depth: set có đủ hero shots và 3-layer depth shots không?
□ 6.  Character age: có figure nào trẻ em không? → xóa
□ 7.  Narrative arc: set có đủ setup/pause/payoff/closure — không phải toàn "kể chuyện" không?
□ 8.  World feels alive: có thể xem toàn bộ set và cảm thấy đây là một thế giới có người sinh sống thật không?
□ 9.  Quality Gate — Location: có ≥ 30% prompts dùng extended location (ngoài Asset Bible) không?
□ 10. Quality Gate — Action: có action nào lặp lại > 3 lần trong toàn bộ set không? → thay thế
□ 11. Quality Gate — Chorus: C1 / C2 / Final Chorus có density và camera angle escalate khác nhau không?
□ 12. Quality Gate — Leitmotif: 4 leitmotif slots có emotional context khác nhau rõ rệt không? (Neutral → Warm → Melancholy → Transformed)
```

---

*V7 — Last updated: 2026-06-11*
*Archive V6: `flow/archive/04_image_prompt_development_knowledge_v6.md`*
