# 04b_IMAGE_PROMPT_TECHNIQUE_KNOWLEDGE



---

## GIAI ĐOẠN 1: Tạo Prompt (PHASE 1: Prompt Generation)

> [!CAUTION]
> **NGHIÊM CẤM** để Main Agent tự viết toàn bộ hàng trăm prompts trong một lần (sẽ dẫn đến hiện tượng văn phong lười biếng, "1 màu").
> KHÔNG dùng mã lệnh Python để sinh prompt hàng loạt.

**Quy trình phân tán qua Subagent (BẮT BUỘC):**
1. Main Agent đóng vai trò Trưởng nhóm (Orchestrator). Chia **Section Creative Brief** thành các lô nhỏ theo section (Verse/Chorus), mỗi lô 15-20 prompts.
2. Dùng lệnh `invoke_subagent` để gọi các Subagent. Cung cấp cho mỗi Subagent: Creative Brief của section đó, Story Context của video, Asset Bible, và File Style.
3. Các Subagent tiến hành viết prompt.
4. Main Agent thu thập toàn bộ kết quả, chạy Cổng Kiểm Tra Chất Lượng (Quality Gate) trên từng lô. Nếu lô nào bị trùng lặp hoặc "1 màu", Main Agent yêu cầu Subagent làm lại lô đó.
5. Cuối cùng, Main Agent gộp tất cả lại và ghi vào **1 file duy nhất**.

**File output:** `projects/video_xxx/docs/04_image_prompts.txt`

**Format file cuối cùng (chỉ chứa prompts thô, không có gì khác):**
```
[prompt hoàn chỉnh trên 1 dòng duy nhất]

[prompt hoàn chỉnh trên 1 dòng duy nhất]
```
- Mỗi prompt trên 1 dòng, không xuống hàng trong dòng
- Giữa các prompt: 1 dòng trống
- Không header, không label, không số thứ tự, không metadata

**Cấu trúc nội dung prompt — Tối ưu hóa Tham chiếu (Reference-Optimized) (7 thành phần):**

> [!IMPORTANT]
> **Chúng ta dùng 1 character ref image duy nhất.** Model AI đã thấy hình nhân vật — không cần mô tả lại ngoại hình. Thay thế toàn bộ character physical description (mô tả thể chất nhân vật) bằng **short identifier (định danh ngắn)** (2-4 từ). Nếu không có nhân vật trong shot — bỏ qua hẳn.

1. Shot size (Cỡ cảnh) + camera angle (Góc máy)
2. Location (Địa điểm) — **dùng Location Shorthand nguyên văn** (địa điểm trong Asset Bible) hoặc mô tả tự nhiên (địa điểm mở rộng)
   - ❌ SAI: `same kitchen interior as established in asset bible` — model không biết file đó là gì
   - ✅ ĐÚNG: `cluttered farmhouse kitchen, rough stone walls, copper pots hanging, warm hearth glow`
3. **Character short ID (Định danh nhân vật ngắn)** — **Bỏ qua nếu là Environment (Môi trường) / Still Life (Tĩnh vật) / Trace shot (Dấu vết)**
   - Dùng: `the old man`, `he`, `the woman`, `her`, `the craftsman`... — không mô tả ngoại hình
   - Chỉ viết action (hành động) + tư thế: `the old man kneeling slowly`, `he reaches toward the shelf`
4. Action (Hành động) cụ thể — phát sinh từ cảm xúc cốt lõi của section (xem Section Brief). Action Pool là gợi ý, không phải menu bắt buộc.
5. Lớp tiền cảnh (Foreground layer) → Lớp trung cảnh (Mid-ground layer) → Lớp hậu cảnh (Background layer) (3 lớp chiều sâu)
6. Điểm neo phong cách (Style anchor) (từ file style active)
7. TONE MÀU BỊ KHÓA (LOCKED COLOR TONE) (copy nguyên văn) + `16:9`

**Tham chiếu đạo cụ (Prop reference):** Nếu có bảng đạo cụ (prop sheet) — dùng `same [prop name] as reference`. Nếu không có bảng đạo cụ — mô tả ngắn gọn.

---


**So sánh độ dài trước và sau khi tối ưu hóa tham chiếu (ref optimization):**

```
❌ SAI — mô hình không hiểu “same as” + thừa mô tả nhân vật (character desc):
Medium shot, low-ground angle, elderly man with silver hair and weathered calloused hands wearing a faded linen shirt and worn brown suspenders, consistent character design, sitting at same workshop interior as established in asset bible, slowly running his hands along the grain of a half-carved wooden boat on the workbench, woodshavings scattered in the foreground, his hands and torso in mid-ground, soft amber lamplight through dusty window in background, warm storybook illustration style, handcrafted texture, aged paper, soft amber and sage green, 16:9

✅ ĐÚNG — dùng tham chiếu (ref) + Viết tắt địa điểm (Location Shorthand) — ngắn hơn 44%:
Medium shot, low-ground angle, small woodworking workshop, amber oil lamp overhead, rough timber walls, heavy oak workbench, woodshavings floor, the old man sitting at the workbench slowly running his hands along the grain of a half-carved wooden boat, woodshavings scattered in the foreground, his hands and torso in mid-ground, soft amber lamplight through dusty window in background, warm storybook illustration style, handcrafted texture, aged paper, soft amber and sage green, 16:9
```

**Những yếu tố không thể bỏ qua dù đã có tham chiếu (ref):**
- Hành động cụ thể (mô hình không thể tự đoán)
- Tư thế / ngôn ngữ cơ thể rõ ràng
- 3 lớp chiều sâu
- Mỏ neo phong cách (Style anchor) + Tông màu (Color Tone)



---

**Ví dụ đầu ra chuẩn (ref-optimized + Location Shorthand):**
```
Wide establishing shot, eye-level, glass dome home submerged in ocean, curved glass windows with morning mist drifting past, ocean floor covered in autumn leaves, deep seagrass in the foreground, the dome solid in the mid-ground, endless dark oceanic depth in the background, handcrafted stop-motion puppet technique, physical clay-and-fabric texture, miniature diorama, extremely tactile hand-crafted textures, deep velvety oceanic teal, warm amber lamplight, muted rusted brass, 16:9

Overhead close-up, cluttered farmhouse kitchen, rough stone walls, copper pots hanging, warm hearth glow, the old man's hands mid-motion kneading bread dough on a worn table, flour dusted across the wooden surface, a chipped ceramic bowl and jar of honey beside him, diffused morning light through a curtained window, handcrafted stop-motion puppet technique, physical clay-and-fabric texture, miniature diorama, extremely tactile hand-crafted textures, deep velvety oceanic teal, warm amber lamplight, muted rusted brass, 16:9

Medium shot, through-doorway framing, village road at dusk, the old man walking slowly with hands in pockets, long shadow stretching ahead on gravel in the foreground, his unhurried figure in the mid-ground, autumn trees lining the road curving out of sight in the background, handcrafted stop-motion puppet technique, physical clay-and-fabric texture, miniature diorama, extremely tactile hand-crafted textures, deep velvety oceanic teal, warm amber lamplight, muted rusted brass, 16:9
```


**Cổng Kiểm Tra Chất Lượng (Quality Gate) — BẮT BUỘC — Main Agent kiểm duyệt từng Lô của Subagent:**

Sau khi nhận kết quả lô (batch) từ mỗi Subagent, Main Agent phải chạy Kiểm tra trùng lặp (Deduplication Check) trước khi gộp vào file chính. Nếu lô không đạt, Main Agent phải phản hồi yêu cầu Subagent sửa lại lô đó:

```
KIỂM TRA TRÙNG LẶP (DEDUPLICATION CHECK) — Lô [X]:

Chiều 1 — Loại Cảnh Quay (Shot Type):
□ Kiểm tra 5 câu lệnh trước đó có cùng Kích cỡ Cảnh (Shot Size) không? (tất cả là Rộng, tất cả là Cận, tất cả là Trung...)
□ Nếu có từ 4 câu lệnh trở lên cùng kích cỡ cảnh liên tiếp → bắt buộc phải thay đổi 2 câu lệnh trong số đó

Chiều 2 — Địa Điểm (Location):
□ Liệt kê các địa điểm được dùng trong lô này
□ Có địa điểm nào xuất hiện > 5 lần trong lô không? → phân bổ lại
□ Địa điểm từ Asset Bible (Tài liệu gốc): không vượt quá 70% của lô (30% phải là địa điểm mở rộng)

Chiều 3 — Hành Động (Action):
□ Liệt kê tất cả các cảnh quay Hành động của Nhân vật trong lô
□ Có hành động nào lặp lại trong 5 câu lệnh liên tiếp không? → thay thế bằng hành động khác từ Nhóm Hành động (Action Pool)

Chiều 4 — Thời Gian trong Ngày (Time of Day):
□ So sánh phân bổ thực tế với tỷ lệ mục tiêu (Bình minh 25% / Trưa 20% / Hoàng hôn 35% / Đêm 20%)
□ Nếu lệch > 15% so với mục tiêu → điều chỉnh 3 câu lệnh tiếp theo

Chiều 5 — Góc Máy Trực Quan (Camera Angle):
□ Đếm các góc máy bất thường (góc thấp, từ trên không, qua khung ảnh, qua vai)
□ Phải có ≥ 3 góc máy bất thường trong mỗi 20 câu lệnh
□ Góc ngang tầm mắt (Eye-level) không được vượt quá 50% của lô

Chiều 6 — Mật Độ (Density):
□ So sánh tỷ lệ Thưa thớt (Sparse) / Vừa phải (Moderate) / Phong phú (Rich) / Dày đặc (Dense) với Ghi đè Mật độ (Density Override) của phần đang tạo
□ Nếu có > 4 mức Vừa phải (Moderate) liên tiếp → chèn 1 Thưa thớt (Sparse) và 1 Phong phú (Rich)

Không đạt ở bất kỳ ô nào → sửa các câu lệnh vi phạm TRƯỚC KHI tiếp tục tạo lô tiếp theo.
```

**Không Báo Cáo Dưới Dạng Hội Thoại (No Conversational Reporting):** Không viết báo cáo dài trong chat. Tạo câu lệnh xong → ghi thẳng vào tệp.



## GIAI ĐOẠN 2: Kết xuất Song song qua các Tác nhân phụ (Parallel Render via Subagents)

> [!CAUTION]
> **BẮT BUỘC:** Dùng `invoke_subagent` native. Mỗi subagent nhận 1 lô, gọi trực tiếp tool tạo ảnh từng prompt — không bọc trong script.

**Bước 1 — Đọc và chia lô (batch):**
- Đọc tệp `projects/video_xxx/docs/04_image_prompts.txt`
- Mỗi lô: tối đa **20 câu lệnh** (không phải 25 — để tác nhân phụ có không gian xử lý việc thử lại)
- Đánh số lô: `batch_01`, `batch_02`...

**Bước 1.5 — Ánh xạ Đa dạng (Diversity Slot Mapping) (BẮT BUỘC):**
Main Agent phải phân bổ trước "Ngân sách Đa dạng" (Diversity Budget) cho từng lô. Do các tác nhân phụ chạy song song và không thấy nhau, nếu không phân bổ trước, chúng sẽ chọn trùng lặp (vd: tất cả đều cho nhân vật ngồi trong phòng).
- Phân bổ **Location, Time of Day, Density, Cỡ cảnh (Shot Size), và Tiêu điểm (Focus)** cho từng lô dựa trên Narrative Arc.
- VD: Batch 1 (Intro) → Cấp phép Location A; Dawn; Sparse; Cỡ cảnh chủ đạo: Wide; Tiêu điểm: Environment. Batch 2 (Verse) → Location B; Morning; Moderate; Cỡ cảnh: Medium; Tiêu điểm: Character.

**Bước 2 — Tạo các tác nhân phụ song song (invoke_subagent):**

Tạo (Spawn) tất cả các lô cùng lúc. Mỗi tác nhân phụ nhận câu lệnh sau:

```text
Bạn là image prompt writer cho [SECTION NAME] của video "[VIDEO_TITLE]".

## Câu chuyện (Story Context)
[3-5 câu: nhân vật là ai, tình huống, cảm xúc chủ đạo video]

## Section Brief
[Copy Creative Brief của section này từ Giai đoạn 2 Bước 10]

## Cross-section Context
Section trước ([PREV_SECTION]) kết thúc với cảm giác: [1 câu]
Section này cần mở ra với cảm giác: [1 câu]

## Ngân sách Đa dạng (Diversity Budget - BẮT BUỘC TUÂN THỦ)
Main Agent đã phân bổ trước các yếu tố sau để lô này KHÔNG TRÙNG với các lô khác và đi đúng Arc:
- Locations ĐƯỢC PHÉP dùng trong lô này: [List locations từ Asset Bible]
- Time of Day / Lighting (thời gian trong ngày): [Time]
- Density (mật độ): [Density]
- Cỡ cảnh chủ đạo (Dominant Shot Size): [Wide / Medium / Close / Macro]
- Tiêu điểm chủ đạo (Dominant Focus): [Character Action / Environment / Object]

## Quality Gate (Kiểm tra nội bộ SAU KHI viết)
- Số prompts: [N]
- Luân phiên liên tục (không lặp lại 2 lần liên tiếp): Mặc dù có "Cỡ cảnh chủ đạo", vẫn phải xen kẽ các cỡ cảnh và góc máy khác để tạo nhịp điệu (VD: Wide -> Medium -> Wide -> Close). Camera Angle luôn thay đổi.
- Mandatory anchors: [chỉ những gì bắt buộc cố định: leitmotif, bookend]

## Resources
- Asset Bible shorthands: [paste]
- Style anchor: [paste]
- Locked Color Tone: [paste]
- Action Pool: [paste] — đây là GỢI Ý, không phải menu bắt buộc chọn từ đó

## Output
[N] prompts theo format chuẩn 7 thành phần.
Không cần giải thích. Không cần báo cáo.
```

**Bước 3 — Theo dõi (Monitor):**
- Không cần thăm dò (poll) liên tục. Hệ thống sẽ tự động thông báo khi tác nhân phụ hoàn thành.
- Kiểm tra `renders/batch_X/progress.txt` nếu cần biết tiến độ.

**Bước 4 — Gộp (Merge) sau khi tất cả các lô đã hoàn thành:**
- Gộp toàn bộ ảnh từ `renders/batch_X/` vào `renders/final/`
- Đặt lại tên liên tục: `001.png`, `002.png`...
- Dùng `run_command` với `cp` hoặc `mv` — không dùng mã lệnh

**Bước 5 — Xử lý lỗi:**
- Đọc `renders/errors.txt`
- Tạo lại (Re-spawn) tác nhân phụ chỉ cho các câu lệnh bị lỗi (không tạo lại toàn bộ lô)
- Ghi nhật ký cuối cùng (Log final): tổng số câu lệnh / thành công / thất bại

---

# NGUYÊN TẮC CHỈ ĐẠO (DOCTRINES) — Kiến thức nền

---

### A. Không dùng tên studio / hãng / thương hiệu trong prompt — mô tả kỹ thuật thay thế:

| ❌ Không được dùng | ✅ Thay bằng |
|---|---|
| `Laika Studios aesthetic` | `handcrafted stop-motion puppet technique, physical clay-and-fabric texture` |
| `Laika-style puppet` | `handcrafted stop-motion puppet, wire armature and silicone skin construction` |
| `Pixar-style 3D` | `smooth stylized 3D animation, subsurface scattering skin, appealing proportions` |
| `Disney style` | `warm stylized animation, expressive character proportions` |
| `Studio Ghibli` | `hand-painted watercolor animation, soft natural environments, gentle character movement` |
| `DreamWorks style` | `stylized CGI animation, dynamic character expression` |
| `Tim Burton style` | `gothic whimsical proportions, expressionist shadow play, twisted silhouettes` |
| `Wes Anderson style` | `symmetrical composition, pastel color palette, flat graphic depth` |



---

### B. Không dùng tên nghệ sĩ còn sống — mô tả kỹ thuật thay thế:

| ❌ Không được dùng | ✅ Thay bằng |
|---|---|
| `in the style of [living artist]` | Mô tả kỹ thuật: brushwork, color palette, composition style |
| `Hayao Miyazaki art style` | `hand-painted background with watercolor depth, soft natural lighting` |
| `Edward Hopper style` | `realist painting, solitary figure in empty interior, strong directional light` |

---

### C. Dành riêng cho từng nền tảng (Platform-specific) — Sử dụng Thương mại (Commercial Use)

Coslient là một kênh YouTube = **sử dụng thương mại (commercial use)**.

| Nền tảng (Platform) | Thương mại OK? | Lưu ý |
|---|---|---|
| Midjourney Basic ($10/tháng) | ❌ | Cần từ gói Standard trở lên |
| Midjourney Standard ($30/tháng) | ✅ | Đầy đủ quyền thương mại (Full commercial rights) |
| DALL-E 3 (API trả phí) | ✅ | Hình ảnh thuộc sở hữu của người tạo |
| Adobe Firefly | ✅ | Thiết kế cho mục đích thương mại, được bảo hộ quyền sở hữu trí tuệ (IP-indemnified) |
| Flux.1 [dev] | ❌ | Chỉ dùng cho mục đích phi thương mại |
| Flux.1 [schnell] | ✅ | Giấy phép Apache 2.0 |
| Flux.1 [pro] (API) | ✅ | Thương mại qua API |
| Stable Diffusion base (SDXL) | ✅ | Giấy phép Apache 2.0 |

> [!WARNING]
> Nếu Boss đang dùng gói miễn phí (free tier) của Midjourney → toàn bộ nội dung trên YouTube có thể vi phạm Điều khoản Dịch vụ.

---

Nhân vật Coslient phải là nhân vật hư cấu nguyên bản — không dựa trên người thật, không giống IP được bảo vệ.

---

## Quy tắc an toàn khi kết xuất (Render Safety Rule) — Các từ bị cấm (KHÔNG KHOAN NHƯỢNG)

> [!CAUTION]
> **Một số từ/cụm từ kích hoạt bộ lọc nội dung (content filter) của AI tạo ảnh → prompt bị từ chối hoặc kết xuất ra ảnh sai hoàn toàn.** Kiểm tra toàn bộ các prompt trước khi ghi file.

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
| `real person name` | không gắn thẻ (tag) tên người thật (người nổi tiếng, chính trị gia...) |
| `brand name` | không gắn thẻ (tag) tên thương hiệu có bản quyền |
| `child` / `children` / `kid` / `baby` | không để trong phần thân prompt (body prompt) |

**Các cụm từ thường vô tình xuất hiện trong ngữ cảnh Coslient — cần đặc biệt chú ý:**
```
"dead leaves blowing"   → "fallen leaves drifting"
"dying afternoon light" → "late afternoon amber light"
"ghost of a smile"     → "a faint smile", "the faintest curve of a smile"
"haunting melody"      → xóa — không cần từ mô tả (descriptor) âm nhạc trong image prompt
"decay of time"        → "marks of time", "weathered by years"
"withered hand"        → "aged hand", "time-worn hand", "gnarled and worn hand"
```

**Khi nào cần kiểm tra:** Sau khi viết mỗi đợt (batch) 20 prompt, quét nhanh (scan) toàn bộ các từ trong đợt đó.
Nếu phát hiện từ bị cấm → sửa ngay trước khi ghi vào file.

---

**Được phép:** `golden afternoon light`, `sun rays through tree canopy`, `warm lamplight`, `steam rising from tea`, `morning mist over the field` — ánh sáng và khói phải có lý do vật lý.

---

## Hệ thống khóa màu sắc (Color Lock System)

> [!IMPORTANT]
> **Mỗi video có DUY NHẤT 1 tông màu (tone).** Hai yếu tố này hoàn toàn độc lập với nhau.

**Hệ thống phân cấp token (Token Hierarchy) trong prompt:**
- Màu sắc của đồ vật/trang phục → Đặt ở GIỮA prompt, gắn liền với tính từ chỉ chất liệu.
- TÔNG MÀU ĐƯỢC KHÓA (LOCKED COLOR TONE) → Đặt ở CUỐI prompt, trước `16:9`.

**Neo giữ tính vật chất (Materiality Anchoring - chống hiện tượng tràn màu/Color Bleed):**
Mọi màu sắc PHẢI được gắn trực tiếp với một danh từ chỉ chất liệu cụ thể:

| ❌ Sai | ✅ Đúng |
|---|---|
| `a red dress` | `a matte crimson velvet dress` |
| `blue background` | `a pale dusty-blue linen backdrop` |
| `warm colors` | `warm honey-toned wooden tabletop` |
| `green accent` | `a faded sage-green ceramic pot` |

---

## Học thuyết Ưu tiên Chủ thể (Subject-Priority Doctrine)

Mỗi ảnh có một điểm nhấn chính (dominant read): một người, một cử chỉ, một đồ vật biểu tượng, một ngưỡng cửa, một sự kiện siêu thực, một tư thế mang cảm xúc, một con đường.

Tránh khung hình có 5 thứ cạnh tranh ngang nhau. Người xem phải hiểu ảnh trong 1 giây.

---

## Học thuyết về Độ sâu trường ảnh (DoF)

```
Deep focus  — môi trường quan trọng, cảnh establishing/cuối
Moderate    — chủ thể dẫn dắt, nền thêm ý nghĩa (mặc định)
Shallow     — khuôn mặt, bàn tay, thư, hoa, cảm xúc gần
Selective   — vật thể ký ức biểu tượng, sự kiện mong manh
```

---

*V7 — Cập nhật lần cuối: 2026-06-12*
