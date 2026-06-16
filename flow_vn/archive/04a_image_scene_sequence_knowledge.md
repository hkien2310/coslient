**Tóm tắt tác dụng của file:** File này cung cấp hướng dẫn và kỹ thuật để phát triển câu lệnh (prompt) tạo hình ảnh AI chất lượng cao, đồng nhất với phong cách và thẩm mỹ của dự án.

---

# Coslient GPT Knowledge — Phát triển Image Prompt V7

> **Phiên bản V6 đã được lưu trữ tại:** `flow/archive/04_image_prompt_development_knowledge_v6.md`



## Mục đích

Biến bài hát đã duyệt thành bộ image-prompt mạch lạc, đọc được cảm xúc để sản xuất video.

Coslient hoạt động như đạo diễn hình ảnh — không phải công cụ spam prompt.

> [!IMPORTANT]
> **Visual Style Module:** Phong Phong cách hình ảnh được quản lý trong file riêng tại `styles/`.
> Style mặc định: `styles/04s_visual_style_warm_storybook.md`
> Khi Boss chỉ định style khác, load file style tương ứng thay thế.

---

## Triết lý hình ảnh (Andrew Goodwin Framework)


| Chế độ | Định nghĩa | Coslient |
|---|---|---|
| **Illustration** | Ảnh dịch lyrics thành hình — lyrics nói "bàn tay" → ảnh có bàn tay | ❌ Quá sát nghĩa đen (literal) |
| **Amplification** | Ảnh mở rộng cảm xúc — thêm chiều sâu, ẩn dụ, ẩn ý (subtext) | ✅ **Mặc định** |
| **Disjunction** | Ảnh có chủ ý không khớp — tạo sự mỉa mai (irony) hoặc chiều sâu mới | ⚡ Dùng khi cần siêu thực (surreal) mạnh |

**Nguồn gốc nội dung ảnh:** Concept đã duyệt + Cung bậc cảm xúc (Emotional arc) của câu chuyện. **Không** từ từng câu lyrics.

---

# QUY TRÌNH LÀM VIỆC (WORKFLOW)

## GIAI ĐOẠN -1: Tiếp nhận Bài hát (Song Intake) (AI tự làm — ẩn, không báo Boss)

> [!IMPORTANT]
> Bước này chạy TRƯỚC mọi thứ khác. Hoàn toàn internal — không output ra chat, không hỏi Boss.

Khi Boss nói "làm ảnh video X":

**Bước 1 — Đọc 3 files theo thứ tự:**
- `projects/video_xxx/docs/01_idea.md` → hạt giống câu chuyện (story seed), ý định cảm xúc (emotional intent) ban đầu
- `projects/video_xxx/docs/02_concept.md` → THẾ GIỚI HÌNH ẢNH (VISUAL WORLD), nhân vật, bối cảnh (setting) đã duyệt
- `projects/video_xxx/docs/03_song.md` → cấu trúc nhạc, leitmotif, chế độ cảm xúc (emotional mode), bản đồ năng lượng (energy map)

**Bước 2 — Trích xuất 5 thứ vào bộ nhớ làm việc (working memory) (không output):**

**A. VẬT THỂ LEITMOTIF** — Tìm phần B5.6 trong file bài hát:
- Vật thể là gì? Xuất hiện mấy lần? Sức nặng cảm xúc (Emotional load) mỗi lần?
- **Nếu không có leitmotif trong file:** AI tự đề xuất 1 vật thể phù hợp với câu chuyện và concept (đồ vật bình thường, gắn với nhân vật chính, có thể phát triển bối cảnh cảm xúc qua 4 lần xuất hiện). Ghi vào bộ nhớ làm việc, không hỏi Boss.

**B. CHẾ độ CẢM XÚC (EMOTIONAL MODE)** — Tìm phần B2.5: A / B / C / D
- Nếu không có: AI tự suy luận từ lyrics và concept. Mặc định Mode A nếu không rõ.

| Mode | Tên | Thiên hướng hình ảnh (Visual Bias) |
|---|---|---|
| A | Trở về ngọt ngào xen lẫn cay đắng (Bittersweet Return) | Đồ vật ấm áp, góc máy ngưỡng cửa (threshold shots), ánh sáng vàng |
| B | Quan sát yên bình (Peaceful Observation) | Chú trọng môi trường, góc rộng + tĩnh vật, tươi sáng |
| C | Tiếc nuối + Kêu gọi hành động (Regret + CTA) | Ngôn ngữ cơ thể rõ ràng, hướng đến hành động, tone màu hơi lạnh |
| D | Nỗi đau được giải tỏa (Cathartic Grief) | Không gian trống trải, dấu vết, sự vắng mặt, chi tiết bóng tối |

**C. CẤU TRÚC BÀI HÀT + THỜI GIAN (SONG STRUCTURE + TIMING)** — Tìm F7:
- Mẫu (Pattern) đã chọn (Classic Pop / Evolving Chorus / 2-phút...)
- Thời gian ước lượng từng phần (giây)

**D. BẢN ĐỒ NĂNG LƯỢNG (ENERGY MAP)** — Tìm D1:
- % năng lượng từng phần (Intro 15-20%, Verse 25-35%, Chorus 75-85%, Bridge 25-40%, Final Chorus 95-100%)

**E. THẾ GIỚI HÌNH ẢNH (VISUAL WORLD)** — Từ 02_concept.md:
- Mô tả thế giới hình ảnh đã duyệt (bối cảnh, bầu không khí, bảng màu cảm xúc)
- Dùng để đảm bảo tính nhất quán (consistency) với câu chuyện gốc khi viết prompt

---

## GIAI ĐOẠN 1: Phong cách hình ảnh (Visual Style) & Tông màu (Color Tone)

**Bước 1 — Chọn style:** Liệt kê tất cả file `04s_visual_style_*.md` có trong `styles/` và hỏi Boss. Mặc định: `styles/04s_visual_style_warm_storybook.md`.

**Bước 2 — Lựa chọn Tông màu Câu chuyện (Story Color Tone Selection) (BẮT BUỘC):**
Dựa trên cung bậc cảm xúc của câu chuyện và Chế độ cảm xúc đã trích xuất từ Giai đoạn -1, đề xuất 1 Chuỗi Tông màu (Color Tone String) duy nhất (5-8 từ khóa màu):
- Cảm xúc chủ đạo? (buồn / hy vọng / ấm áp / cô đơn / rực rỡ)
- Thời điểm cảm xúc? (bình minh / chiều tà / đêm)
- Cao điểm và thấp điểm cảm xúc?

**Ví dụ:** Ông lão chăm sóc đáy biển → `"deep oceanic teal, warm amber lamplight, muted rusted brass, soft bioluminescent accents, velvety deep-sea blue"`

Dừng và đợi Boss duyệt Tông màu (Color Tone).

**Bước 3 — Chốt (Lock):** Ghi vào đầu file đầu ra (output) dưới dạng:
```
# LOCKED COLOR TONE: [Color Tone String]
```
Mọi prompt sau đều sao chép nguyên văn chuỗi này — không dùng từ đồng nghĩa (synonym), không diễn giải lại (paraphrase).

---

## GIAI ĐOẠN 2: Bản thiết kế đa dạng (Diversity Blueprint) (AI tự làm — không cần Boss duyệt)

> [!IMPORTANT]
> **Bắt buộc hoàn thành toàn bộ Bản thiết kế (Blueprint) trước khi sinh bất kỳ prompt nào.**

**Bước 1 — Tính tổng số prompts:**

```
Tổng prompts = song_duration_seconds ÷ 1.5
```

| Bài dài | Tổng prompts |
|---|---|
| 2 phút (120s) | 80 |
| 2.5 phút (150s) | 100 |
| 3 phút (180s) | 120 |
| 3.5 phút (210s) | 140 |
| 4 phút (240s) | 160 |

**Sau khi có tổng, phân bổ theo section bằng % cố định:**

| Phân đoạn (Section) | % của tổng |
|---|---|
| Intro | 7% |
| Verse 1 | 15% |
| Pre-Chorus 1 | 5% |
| Chorus 1 | 13% |
| Verse 2 | 11% |
| Pre-Chorus 2 | 4% |
| Chorus 2 | 13% |
| Bridge | 7% |
| Final Chorus | 17% |
| Outro | 8% |
| **Tổng** | **100%** |

> [!NOTE]
> Nếu bài không có đủ sections (không có Bridge, không có Pre-Chorus): phân bổ % thừa vào Verse và Final Chorus.
> Làm tròn xuống để không vượt tổng. Điều chỉnh ±1 ở Final Chorus nếu cộng lại lệch.


**Bước 2 — Season & Time of Day:** Chọn 1-2 mùa cho video. Phân bổ time of day đều — không để toàn bộ cùng 1 thời điểm:
```
Dawn (~25%) | Midday (~20%) | Late afternoon/Dusk (~35%) | Night/Lamplight (~20%)
```

**Bước 3 — Weather (chọn ≥ 3 loại):**
```
Clear / Overcast / Light rain / After rain / Morning mist / Wind / Hot-hazy
```

**Bước 4 — Cung bậc Cảm xúc Nhân vật (Character Mood Arc) (theo Emotional Mode + arc bài nhạc):**
Nhân vật cần nhiều trạng thái vật lý — không phải lúc nào cũng "nhẹ nhàng" (gentle):
```
Contemplative / still (Trầm tư / tĩnh lặng)    — ngồi im, nhìn xa, thở chậm
Gentle activity (Hoạt động nhẹ nhàng)          — chuyển động nhẹ, tập trung vào tay
Physical effort (Nỗ lực thể chất)          — tư thế căng, gắng sức nhỏ
Rest / exhausted (Nghỉ ngơi / kiệt sức)         — ngồi dựa, đầu cúi, hơi thở nặng
Quiet joy (Niềm vui tĩnh lặng)                — khóe miệng nhếch nhẹ, tư thế mở
Grief / longing (Đau buồn / khao khát)          — vai sụp, tay nắm chặt, nhìn xuống
Determined (Kiên định)               — lưng thẳng, bước chắc, mắt hướng trước
Tender / surprised (Dịu dàng / ngạc nhiên)       — tay đặt nhẹ, đầu nghiêng, mắt mở to
```

**Bước 5 — Tập hợp Địa điểm (Location Pool) (bắt buộc ≥ 30% ngoài Asset Bible):**
Lên ý tưởng (Brainstorm) 5-8 locations bổ sung phù hợp với thế giới video và Visual World đã extract từ Phase -1.

**Bước 6 — Chỉ tiêu Hạng mục Tập trung (Focus Category Quota) (mỗi 20 prompts):**
```
Character Action (Hành động Nhân vật):    8 shots (40%) — nhân vật tương tác/hành động toàn vẹn
Environment (Môi trường):         4 shots (20%) — chỉ cảnh, không người
Traces & Still Life (Dấu vết & Tĩnh vật): 4 shots (20%) — dấu vết sự sống, đồ vật
Fragmented Macro (Cận cảnh Chi tiết):    4 shots (20%) — cận tay, vai, vật thể — không lấy mặt
```

**Bước 7 — Phân bổ Mật độ (Density Distribution):**

**Ghi đè mật độ theo Phân đoạn (Density Override theo Section):**

| Phân đoạn (Section) | Sparse (Thưa thớt) | Moderate (Vừa phải) | Rich (Phong phú) | Dense (Dày đặc) |
|---|---|---|---|---|
| Intro | 60% | 30% | 10% | 0% |
| Verse | 20% | 60% | 15% | 5% |
| Pre-Chorus | 10% | 45% | 35% | 10% |
| Chorus | 5% | 30% | 45% | 20% |
| Bridge | 40% | 45% | 12% | 3% |
| Final Chorus | 0% | 15% | 45% | 40% |
| Outro | 65% | 30% | 5% | 0% |

**Bước 8 — Ánh xạ Cung bậc Kể chuyện (Narrative Arc Mapping) (theo Song Structure):**

| Phân đoạn Bài hát (Song Section) | Chức năng Kể chuyện (Narrative Function) | Tính chất Thị giác (Visual character) |
|---|---|---|
| Intro | Setup (Thiết lập) — thiết lập thế giới | Sparse (Thưa thớt), wide (rộng), không nhân vật |
| Verse 1 | Rising tension (Căng thẳng dâng trào) đầu — nhân vật bước vào | Moderate (Vừa phải), character introduced (giới thiệu nhân vật) |
| Pre-Chorus | Invitation (Lời mời) — cảm xúc dâng | Moderate-Rich (Vừa phải-Phong phú), movement (chuyển động) |
| Chorus 1 | Climax (Cao trào) mức 1 | Rich (Phong phú), dynamic (năng động), leitmotif (nhạc đề) lần 2 |
| Verse 2 | Deeper story (Câu chuyện sâu hơn) — đào sâu hơn V1 | Moderate (Vừa phải), new angle/location (góc/địa điểm mới) |
| Chorus 2 | Climax (Cao trào) mức 2 — lớn hơn C1 | Rich+ (Phong phú+), unusual angles (các góc bất thường) |
| Bridge | Pause (Tạm nghỉ) + Symbolic (Tính biểu tượng) | Sparse-Moderate (Thưa thớt-Vừa phải), still life heavy (nhiều tĩnh vật) |
| Final Chorus | Peak + Release (Đỉnh điểm + Giải tỏa) | Dense (Dày đặc), hero shots (cảnh quay đắt giá) tập trung |
| Outro | Closure (Kết thúc) — afterglow (dư âm) | Sparse (Thưa thớt), bookend (kết cấu tương ứng) với Intro |

> [!NOTE]
> Khi không có song structure rõ: dùng Narrative Arc cũ (Setup 10% / Invitation 10% / Rising tension 20% / Pause 10% / Climax 15% / Symbolic 10% / Release 15% / Closure 10%).

**Bước 8.5 — Chuỗi Mở đầu + Kết cấu Đầu cuối tương ứng (Opening Sequence + Closure Bookend):**

Làm NGAY SAU Bước 8, TRƯỚC khi viết Creative Brief.

**Opening Sequence (Chuỗi Mở đầu) — 3 prompts đầu tiên của INTRO:**
- **Prompt 1:** Wide establishing (Cảnh rộng thiết lập) — thế giới, mùa, không khí — KHÔNG nhân vật. Sparse (Thưa thớt).
- **Prompt 2:** Environmental (Môi trường) + dấu vết nhân vật (ánh đèn từ cửa sổ, khói bếp, đôi giày cạnh cửa). Không nhân vật.
- **Prompt 3:** Nhân vật xuất hiện lần đầu — Full shot (Cảnh toàn thân), nhìn ra xa, KHÔNG nhìn camera.

→ 3 prompts này là 3 prompts được viết kỹ nhất toàn bộ set. Assign HERO flag (Gắn cờ HERO) cho ít nhất 1 trong 3.

**Closure Bookend (Kết cấu Đầu cuối tương ứng) — 2 prompts cuối của OUTRO:**
Phải echo (lặp lại sự tương đồng) prompt đầu tiên (Prompt 1 của Intro):
- Cùng location → nhưng khác thời điểm trong ngày (thường chiều tà hoặc đêm)
- Cùng composition archetype (nguyên mẫu bố cục) → nhưng KHÔNG có nhân vật
- Dấu vết thay cho người: ghế trống, cốc nguội, cửa khép nhẹ, ánh đèn tắt
- Density: Sparse. Không action. Chỉ still life (tĩnh vật).

→ Ghi rõ vào Creative Brief của INTRO và OUTRO: slot #001 là BOOKEND-OPEN, slot #N là BOOKEND-CLOSE.

**Bước 9 — Tập hợp Hành động (Action Pool) cho Character Action shots:**
Không để nhân vật chỉ sit/stand/look. Không lặp action trong 5 prompts liền trước:
```
Vật lý:    kneeling (quỳ), crouching (cúi người), lying down (nằm), carrying (mang vác), pulling (kéo), bending over (cúi gập người)
Tay:       kneading dough (nhào bột), pruning plants (tỉa cây), folding (gấp), writing (viết), painting (vẽ), fixing (sửa chữa), stirring (khuấy)
Di chuyển: walking slowly (đi chậm), pausing at doorway (dừng ở cửa), turning around (quay lại), climbing steps (bước lên bậc thang)
Quan sát:  gazing out window (nhìn ra cửa sổ), watching rain (ngắm mưa), reading (đọc), listening with eyes closed (nhắm mắt lắng nghe)
Nghi thức: making tea (pha trà), lighting candle (thắp nến), watering plants (tưới cây), feeding birds (cho chim ăn), hanging laundry (phơi đồ)
Cảm xúc:   pressing hand to chest (đặt tay lên ngực), leaning against wall (dựa vào tường), holding something tightly (nắm chặt vật gì đó)
```

**Bước 10 — Creative Brief per Section:**

Tạo 1 Creative Brief ngắn cho mỗi section. LLM đọc rồi tự quyết định shot size, weather, time of day, action, composition — không điền trước.

```
## [SECTION NAME] — [N] prompts
Cảm xúc cốt lõi: [trạng thái cảm xúc của section — không phải thuộc tính kỹ thuật]
Hướng hình ảnh: [2-3 gợi ý mở, không bắt buộc]
Tránh: [1-2 bẫy lặp lại phổ biến]
Anchor bắt buộc: [leitmotif slot / bookend / opening sequence nếu có]
```

Ví dụ:
```
## INTRO — 8 prompts
Cảm xúc cốt lõi: Thế giới trước khi câu chuyện bắt đầu — yên tĩnh như đang giữ hơi thở. Không gian tự kể, chưa cần nhân vật.
Hướng hình ảnh: dấu hiệu mùa / dấu vết sinh sống (ánh đèn, khói, giày) / nhân vật xuất hiện lần đầu từ xa
Tránh: bắt đầu với nhân vật đang làm gì đó — thế giới phải "thở" trước
Anchor bắt buộc: Prompt 1 = Wide establishing, Sparse, HERO, BOOKEND-OPEN | Prompt 3 = Opening Sequence (Bước 8.5)
```

---

## Học thuyết về cỡ cảnh (Shot-Size Doctrine)

Ưu tiên mặc định (Default bias): cảnh trung (medium shot), cảnh trung rộng (medium-wide shot), cảnh toàn (full shot) — vì chúng giữ được cả khả năng nhận diện nhân vật (character readability) lẫn tính kể chuyện của môi trường (environmental storytelling).

**Phân bổ được khuyến nghị:**
```
45–55%  medium / medium-wide / full shots — câu chuyện (narrative) chính
15–20%  wide / establishing shots — cảnh thiết lập thế giới, sự kết thúc (closure)
10–15%  close shots — sự thân mật, bàn tay, khoảnh khắc nhận thức, sự dịu dàng (tenderness)
10–15%  detail / object shots — nhịp điệu chủ đề (motif rhythm), mỏ neo (anchors)
5–10%   unusual framing (khung hình bất thường) — làm gia vị, không lạm dụng
```



---

## Học thuyết về góc máy (Camera-Angle Doctrine)

Ưu tiên (Prefer): góc ngang tầm mắt (eye-level), góc hơi thấp nhẹ (gentle slightly low angle), thỉnh thoảng dùng góc hơi cao nhẹ (gentle high angle).

| Góc | Ý nghĩa cảm xúc |
|---|---|
| Eye-level | Sự gần gũi (Closeness), sự chân thực (honesty) |
| Slightly low | Sự trang nghiêm (Dignity), sự kinh ngạc (wonder) |
| Gentle high | Sự dịu dàng (Tenderness), sự mong manh (fragility) |
| Low ground-level | Hành trình (Journey), sự tò mò như trẻ nhỏ (childlike wonder) |
| Overhead | Nghi thức (Ritual), sự sắp đặt đồ vật, sự thân mật (intimacy) |
| Over-the-shoulder | Sự thân mật (Intimacy), góc nhìn chung (shared perspective) |
| Through-the-frame | Chiều sâu (Depth), sự bí ẩn (mystery), khoảng cách điện ảnh (cinematic distance) |

> [!IMPORTANT]
> **Quy tắc chống phẳng (Anti-Flatness Rule):** Mỗi 20 prompt PHẢI có:
> - **≥ 3 cảnh (shots)** từ các góc bất thường (low-ground, overhead, through-obstruction, over-shoulder)
> - **≥ 2 cảnh** với yếu tố tiền cảnh (foreground element) mạnh che khuất một phần khung hình
> - **≥ 2 cảnh** dạng bóng đen (silhouette) hoặc nhân vật ngược sáng (figure-against-light)
> - **≥ 2 cảnh** có chiều sâu phân lớp rõ ràng (layered depth - 3 lớp rõ rệt)

**Góc đặc biệt (≥ 3-4 lần mỗi 20 prompts):**
- **Low-ground:** sàn nhìn lên — doorway, garden path, bước chân
- **Through-foliage/curtain/fence:** nhìn qua vật cản — tạo mystery và depth
- **Over-the-shoulder:** camera sau nhân vật nhìn về phía khác
- **Overhead:** nhìn thẳng xuống — bàn tay, bữa ăn, đôi giày
- **Framed through architecture:** doorway arch, window, hallway làm hard frame

---

## Học thuyết về chiều sâu và bố cục (Depth & Composition Doctrine)

> [!IMPORTANT]
> **Vấn đề đang xảy ra:** Ảnh bị phẳng — quá nhiều prompt chỉ mô tả chủ thể (subject) ở trung cảnh (mid-ground), không có lớp tiền cảnh (foreground layer), không có hậu cảnh (background) có ý nghĩa.

**Ba lớp bắt buộc trong mọi cảnh medium, wide, full:**
1. **Lớp tiền cảnh (Foreground layer)** — vật thể gần camera: cành cây, lan can, góc bàn, rèm cửa, bậu cửa sổ.
2. **Lớp trung cảnh (Mid-ground layer)** — nhân vật hoặc hành động chính.
3. **Lớp hậu cảnh (Background layer)** — không gian có ý nghĩa: khu vườn ngoài cửa sổ, hành lang mờ ảo, ánh sáng cuối căn phòng.

**Ngôn ngữ prompt để tạo chiều sâu:**
- `with a softly blurred [foreground object] in the lower corner`
- `seen through the opening of a [doorway / window / garden gate]`
- `camera placed low behind [object], looking up at the figure`
- `a [foreground element] partially frames the left edge of the shot`
- `layered depth: [foreground] → [mid figure] → [background space]`

**Hero shots (Cảnh đắt giá - ≥ 2 trong mỗi 20 prompt):**
Là những cảnh khiến người xem phải dừng lại và nhớ mãi — với các đặc điểm:
- Bố cục 3 lớp rõ ràng
- Ánh sáng nổi bật tại một điểm (ánh sáng ven - rim light, tia sáng xiên - slanted ray, vũng sáng ấm áp - pool of warmth)
- Góc máy khác thường
- Cảm xúc có thể đọc được ngay trong 1 giây

Ví dụ: *"camera at floor level, looking along a sunlit wooden hallway toward an elderly figure silhouetted in the bright open doorway at the far end"*

**Các nguyên mẫu bố cục (Composition archetypes) — luôn luân phiên thay đổi:**
trung tâm (centered icon), tỷ lệ 1/3 bất đối xứng (asymmetrical thirds), khung trong khung (frame-within-frame), đường dẫn hướng mạnh mẽ (strong leading-line), không gian âm (negative-space), phân lớp tĩnh vật (layered tableau), ngưỡng cửa/lối vào (doorway/threshold), cửa sổ (window), hiên nhà (porch), vật thể trên bàn (object-on-table), phản chiếu (reflective - kính/nước), nhân vật trên con đường (figure-on-path), bàn tay và vật thể (hands-and-object), bố cục toàn cảnh kết thúc (final wide composition).

Không lặp lại (repeat) một nguyên mẫu bố cục quá 3 lần liên tiếp.

---

## Học thuyết về mật độ (Density Doctrine)

```
Sparse (Thưa thớt)  — 1 chủ thể, không gian âm (negative space), sự tái tạo (reset), sự tĩnh lặng (silence), 1 bông hoa biểu tượng.
Moderate (Vừa phải) — hầu hết các khoảnh khắc tự sự (narrative moments), nhân vật trong phòng/vườn (mặc định).
Rich (Phong phú)    — điệp khúc (chorus), sự gặt hái (payoff), khu vườn nở rộ, sự ấm áp của thị trấn.
Dense (Dày đặc)     — ít sử dụng, chỉ dành cho phần thưởng cuối cùng (final reward), sự mở rộng siêu thực (surreal expansion).
```

---

## Kể chuyện qua Môi trường & Đa dạng Tiêu điểm (Environmental Storytelling & Focus Diversity)

**Hạn mức hạng mục tiêu điểm (Focus Category Quota) — mỗi 20 ảnh:**
```
Hành động Nhân vật (Character Action) (40% — 8 ảnh): nhân vật tương tác/hành động toàn vẹn
Cảnh quan/Môi trường (Establishing/Environment) (20% — 4 ảnh): chỉ cảnh, không người, môi trường tự kể chuyện
Dấu vết & Tĩnh vật (Traces & Still Life) (20% — 4 ảnh): đặc tả đồ vật, dấu vết (tách trà bốc khói, ghế trống, áo treo)
Mảnh ghép/Cận cảnh (Fragmented/Macro) (20% — 4 ảnh): cận bàn tay, bờ vai, vạt áo — không bao giờ lấy mặt nhân vật
```

---


## Học thuyết Tiến hóa Hình ảnh Điệp khúc (Chorus Visual Evolution Doctrine)

> [!IMPORTANT]
> **Mỗi lần Điệp khúc (Chorus) là một bước leo thang (escalation) — không phải bản copy của Điệp khúc trước.**

Điệp khúc là đỉnh điểm cảm xúc (emotional peak). Nếu mọi Điệp khúc trông giống nhau → người xem mất cảm nhận về hành trình.

**3 mức Điệp khúc:**

| | Điệp khúc 1 (Chorus 1) | Điệp khúc 2 (Chorus 2) | Điệp khúc cuối (Final Chorus) |
|---|---|---|---|
| **Mật độ (Density)** | Phong phú (Rich) | Phong phú+ (Rich+) | Dày đặc (Dense) |
| **Bố cục khung hình (Shot composition)** | Phong phú tiêu chuẩn (Standard Rich) — nhân vật + môi trường | Tăng độ phức tạp — bắt buộc có góc máy khác thường (unusual angle) | Toàn bộ là ảnh chính (Hero shots) — mọi prompt phải đáng nhớ |
| **Máy ảnh (Camera)** | Ngang tầm mắt (Eye-level) hoặc hơi thấp | Ít nhất 2 góc máy khác thường | Sát đất (Low-ground) + Xuyên qua khung hình (Through-frame) là chủ đạo |
| **Tiền cảnh (Foreground)** | 1 lớp tiền cảnh OK | Tiền cảnh bắt buộc dày đặc/nhiều lớp | Tiền cảnh kép — 2 lớp trước chủ thể |
| **Nhân vật** | Hành động có ý nghĩa | Hành động mạnh hơn hoặc đỉnh điểm cảm xúc | Ngôn ngữ cơ thể rõ nhất, hình bóng (silhouette) hoặc nhòe do chuyển động (motion blur) |
| **Chủ đề lặp lại (Leitmotif)** | Lần 2 (Ấm áp) | Lần 3 (U sầu) | Lần 4 (Biến đổi) nếu thời gian phù hợp |
| **Địa điểm (Location)** | Địa điểm trong Asset Bible | Asset Bible + 1 địa điểm mở rộng (extended location) | Địa điểm mở rộng hoặc biến đổi siêu thực nhẹ |

**Các quy tắc chống lặp lại cho Điệp khúc:**
- Không dùng cùng nguyên mẫu bố cục giữa C1 và C2
- Không dùng cùng góc máy ảnh cho ảnh chính giữa C2 và Điệp khúc cuối
- Nếu C1 dùng ảnh chính Ngang tầm mắt → C2 phải Sát đất hoặc Xuyên qua khung hình
- Điệp khúc cuối: bắt buộc ít nhất 1 ảnh mà người xem chưa thấy trong toàn bộ video trước đó

---

## Học thuyết về Hiện diện của Nhân vật (Character Visibility Doctrine)

Hình dáng con người (Human figures) phải thường xuyên dễ nhìn (readable): tư thế rõ ràng, hình bóng dễ nhận diện, cử chỉ có thể nhìn thấy, ngôn ngữ cơ thể, kích thước chủ thể đủ để mang cảm xúc.

Không lạm dụng: những hình người nhỏ bé ở xa, người làm nền trang trí, những ảnh cận mặt lặp đi lặp lại.

> [!CAUTION]
> **QUY TẮC NGHIÊM NGẶT VỀ ĐỘ TUỔI:** Chỉ được phép có hình người lớn/người già. Tuyệt đối KHÔNG có trẻ em, em bé, trẻ mới biết đi. Luôn thêm `no children, no kids` vào prompt phủ định.

Cảm xúc đến từ ngôn ngữ cơ thể — không phải diễn xuất mặt thái quá. Không lạm dụng chân dung cười trực diện.

Gợi ý: lowered gaze → dịu dàng | hand on chair → ký ức | figure in doorway → chuyển tiếp | looking toward garden → hy vọng

---

## Danh sách Kiểm tra Đánh giá (Review Checklist) (12 mục — trước khi giao bài)

```
□ 1.  Khóa phong cách (Style lock): toàn bộ prompts có cùng mỏ neo phong cách và Tông màu nguyên văn không?
□ 2.  Thực tế Nền tảng (Grounded Reality): có prompt nào chứa ánh sáng rực rỡ / hạt / hào quang / sương mù ma thuật không? → xóa
□ 3.  Không văn bản (No text): có prompt nào chứa chữ viết tay / biển hiệu / chữ thảo không? → xóa
□ 4.  Đa dạng tiêu điểm (Focus diversity): set có đủ ảnh Môi trường + Dấu vết/Tĩnh vật (không phải toàn Nhân vật) không?
□ 5.  Độ sâu (Depth): set có đủ ảnh chính và ảnh có chiều sâu 3 lớp không?
□ 6.  Tuổi nhân vật (Character age): có hình bóng nào là trẻ em không? → xóa
□ 7.  Vòng cung câu chuyện (Narrative arc): set có đủ thiết lập/tạm nghỉ/kết quả/khép lại — không phải toàn "kể chuyện" không?
□ 8.  Thế giới sống động (World feels alive): có thể xem toàn bộ set và cảm thấy đây là một thế giới có người sinh sống thật không?
□ 9.  Cổng Chất lượng — Địa điểm: có ≥ 30% prompts dùng địa điểm mở rộng (ngoài Asset Bible) không?
□ 10. Cổng Chất lượng — Hành động: có hành động nào lặp lại > 3 lần trong toàn bộ set không? → thay thế
□ 11. Cổng Chất lượng — Điệp khúc: C1 / C2 / Final Chorus có mật độ và góc máy ảnh leo thang khác nhau không?
□ 12. Cổng Chất lượng — Chủ đề lặp lại (Leitmotif): 4 khe chủ đề lặp lại có bối cảnh cảm xúc khác nhau rõ rệt không? (Trung lập → Ấm áp → U sầu → Biến đổi)
```

---

*V7 — Cập nhật lần cuối: 2026-06-12*
