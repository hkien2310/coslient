# 04 — Phát triển Hình ảnh

> **Phiên bản V8** — Cải biên từ V7
> Lưu trữ V7: `flow_vn/archive/04a_image_scene_sequence_knowledge.md`

---

## Triết lý

Story first. Style second. Iterate, không plan.

Mục đích duy nhất của toàn bộ quy trình này: **tạo pool ảnh đủ đa dạng để editor chọn tự do.**

Không map ảnh với beat. Không plan 100 ảnh trước khi làm ảnh đầu tiên. Làm → xem → push tiếp. Mỗi batch dạy bạn điều mà planning không bao giờ dạy được.

---

## Bước 1 — Đọc câu chuyện

> Tự làm, ẩn, không output ra chat.

Đọc theo thứ tự:
- `projects/video_xxx/docs/01_idea.md` — hạt giống câu chuyện, ý định cảm xúc ban đầu
- `projects/video_xxx/docs/02_concept.md` — thế giới hình ảnh, nhân vật, bối cảnh đã duyệt
- `projects/video_xxx/docs/03_song.md` — cấu trúc bài hát, cảm xúc từng section

Extract 3 thứ vào working memory:

**A. LEITMOTIF** — Tìm vật thể symbol:
- Vật thể là gì? Xuất hiện mấy lần? Cảm xúc mỗi lần?
- Nếu không có trong file → tự đề xuất 1 vật thể phù hợp (đồ vật bình thường, gắn với nhân vật, có thể phát triển cảm xúc qua 4 lần). Không hỏi Boss.

**B. SONG SECTIONS** — Biết bài có những phần nào:
- Intro / Verse / Pre-Chorus / Chorus / Bridge / Final Chorus / Outro
- Cảm xúc chủ đạo của từng phần (không cần số %)

**C. VISUAL WORLD** — Từ `02_concept.md`:
- Bối cảnh, bầu không khí, nhân vật
- Dùng để đảm bảo consistency khi viết prompt

---

## Bước 2 — Chọn Style

Liệt kê tất cả file `04s_visual_style_*.md` trong `style/` → hỏi Boss chọn.

Style quyết định tất cả: rendering medium, palette, surreal logic, cách ánh sáng hoạt động, cảm xúc tổng thể. Không có Color Tone Lock riêng — style guide đã handle.

---

## Bước 3 — Story Arc

Không phải blueprint. Không có quota. Mỗi section: **câu chuyện đang làm gì ở đây?**

| Section | Câu chuyện làm gì | Hướng hình ảnh |
|---------|-------------------|----------------|
| **Intro** | Thế giới trước khi câu chuyện bắt đầu | Thưa, rộng, không người — chỉ dấu vết sự sống |
| **Verse** | Câu chuyện mở ra, nhân vật bước vào | Nhân vật + hành động nhẹ, moderate |
| **Pre-Chorus** | Cảm xúc dâng, nhịp tăng | Chuyển động, anticipation |
| **Chorus** | Peak cảm xúc — khoảnh khắc vỡ oà | Dense, hero shots, leitmotif |
| **Bridge** | Tạm dừng + ký ức — hơi thở giữa hai đỉnh | Still life, sparse, symbolic |
| **Final Chorus** | Giải phóng — lớn hơn mọi chorus trước | Densest, unusual angles, toàn hero shots |
| **Outro** | Dư âm — thế giới sau câu chuyện | Echo Intro, không người, chỉ dấu vết |

### Opening 3-shot (3 prompt đầu tiên của Intro)
- **Shot 1:** Wide establishing — thế giới, không người. Thưa.
- **Shot 2:** Environment + dấu vết nhân vật (ánh đèn từ cửa sổ, đôi giày, khói bếp). Không người.
- **Shot 3:** Nhân vật xuất hiện lần đầu — full shot, nhìn ra xa, không nhìn camera.

### Closure Bookend (2 prompt cuối của Outro)
Echo Shot 1 của Intro:
- Cùng location → khác thời điểm trong ngày
- Không người — chỉ dấu vết: ghế trống, cốc nguội, ánh đèn tắt
- Sparse. Không action. Chỉ still life.

---

## Bước 4 — Leitmotif Plan

Vật thể symbol xuất hiện **4 lần**, mỗi lần một cảm xúc khác. Mô tả vật thể thay đổi tinh tế qua từng lần — không clone prompt cũ.

| Lần | Section ưu tiên | Cảm xúc | Cách xuất hiện |
|-----|----------------|---------|----------------|
| **1** | Intro / Verse 1 | Trung tính — vật thể bình thường, chưa có subtext | Still life hoặc fragmented macro |
| **2** | Chorus 1 | Ấm áp — gắn với hành động có ý nghĩa, ai đó còn ở đây | Trong tay người, trong hành động |
| **3** | Bridge / Chorus 2 | U sầu — vật thể thay đổi trạng thái, vắng bóng ai đó | Đặt xuống, bị bỏ lại, ánh sáng khác |
| **4** | Final Chorus / Outro | Biến đổi — bối cảnh đảo ngược hoàn toàn, ý nghĩa mới | Cùng vật thể, thế giới hoàn toàn khác |

---

## Bước 5 — Viết Prompt (Iterative Batches)

### Câu hỏi trước mỗi prompt

> **Khoảnh khắc này đang nói gì?**

Không phải "cảnh này trông như thế nào" — mà là "cảnh này có nghĩa gì trong câu chuyện." Trả lời câu hỏi đó trước, rồi mới viết prompt.

### Format prompt

```
[shot size + camera angle], [location description], [character action + body language],
[foreground element] in the foreground, [main subject] in the mid-ground,
[background space] beyond, [style anchor], 16:9
```

Không người → bỏ phần character action.
Macro shot → chỉ foreground và chủ thể cận.

### Batch 1 — 10 ảnh sát câu chuyện

Đi thẳng vào những khoảnh khắc cốt lõi của video. Mỗi ảnh trả lời rõ câu hỏi "nói gì." Không cần unusual, không cần push. Chỉ cần đúng câu chuyện.

### Batch 2+ — Push sáng tạo hơn

Dựa trên những gì đã thấy từ batch trước:
- Góc máy bất thường hơn
- Khoảnh khắc cảm xúc sâu hơn
- Surreal elements mạnh hơn nếu câu chuyện cần
- Mở rộng location ra ngoài không gian quen thuộc

Repeat cho đến khi pool đủ đa dạng.

---

## Đảm bảo Đa dạng

Không fill quota. Nhưng nhìn lại mỗi batch — đảm bảo có sự mix tự nhiên của:

**Focus (mỗi 10 ảnh nên có đủ 4 loại):**
- **Character Action** — nhân vật tương tác, hành động rõ ràng
- **Environment** — cảnh vật, không người, thế giới tự kể
- **Traces & Still Life** — dấu vết, đồ vật, sự vắng mặt
- **Fragmented Macro** — tay, vai, vật thể cận — không bao giờ lấy mặt

**Chorus escalation:**
- Chorus 1 → Rich
- Chorus 2 → Rich+
- Final Chorus → Dense, toàn hero shots

Nếu một loại focus bị thiếu hoàn toàn trong batch → bổ sung trước khi chuyển batch tiếp.

---

## Kỹ thuật (Kiến thức nền)

### Shot-Size

Ưu tiên mặc định: medium / medium-wide / full shot — giữ được nhân vật và môi trường cùng lúc.

```
45–55%  medium / medium-wide / full — narrative chính
15–20%  wide / establishing — thiết lập thế giới, closure
10–15%  close — bàn tay, khoảnh khắc nhận thức, tenderness
10–15%  detail / object — leitmotif, anchors
5–10%   unusual framing — gia vị, không lạm dụng
```

### Camera Angle

Ưu tiên: eye-level, slightly low angle.

| Góc | Cảm xúc |
|-----|---------|
| Eye-level | Gần gũi, chân thực |
| Slightly low | Phẩm giá, wonder |
| Gentle high | Tenderness, fragility |
| Low ground-level | Hành trình, childlike wonder |
| Overhead | Ritual, intimacy |
| Over-the-shoulder | Shared perspective |
| Through-the-frame | Depth, cinematic distance |

Mỗi batch nên có ít nhất 2-3 góc bất thường (low-ground, overhead, through-obstruction).

### Depth & Composition

Mọi cảnh medium, wide, full cần **3 lớp:**
1. **Foreground** — vật thể gần camera: cành cây, góc bàn, rèm
2. **Mid-ground** — nhân vật hoặc hành động chính
3. **Background** — không gian có ý nghĩa: vườn ngoài cửa sổ, hành lang mờ, ánh sáng cuối phòng

**Hero shots** (ít nhất 2 mỗi batch) — ảnh khiến người xem dừng lại:
- Bố cục 3 lớp rõ ràng
- Ánh sáng nổi bật tại một điểm
- Góc máy khác thường
- Cảm xúc đọc được trong 1 giây

---

*V8 — Cải biên 2026-06-17*
