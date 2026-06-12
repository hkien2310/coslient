
# Kiến thức Coslient GPT - Khử trùng lặp Concept (Giao thức Anti-Clone) v1.0

## Mục đích

Ngăn channel tự lặp lại concept với chính mình. Với 60+ videos, rủi ro clone ý tưởng nội bộ ngày càng lớn — đặc biệt ở các yếu tố mà Boss và Coslient đều ưa thích: old man (ông lão), home interior (nội thất trong nhà), object-triggers-memory (đồ vật gợi nhớ kỷ niệm).

**File này hoạt động cùng `concept_index.md` — không thể dùng riêng lẻ.**

---

## Khi nào kích hoạt Protocol này?

Bắt buộc kích hoạt tại **2 checkpoint**:

1. **Stage 1 — Idea Intake (Tiếp nhận ý tưởng):** Trước khi gắn nhãn `STRONG` cho bất kỳ ý tưởng nào
2. **Stage 2 — Concept Development (Phát triển Concept):** Trước khi Boss approve (phê duyệt) concept final

---

## BƯỚC 1 — Đọc concept_index.md

> [!IMPORTANT]
> **Coslient phải đọc file `flow/concept_index.md` trước khi evaluate (đánh giá) bất kỳ ý tưởng mới nào.**  
> Không được bỏ qua dù Boss đang hối thúc. File này là nguồn sự thật duy nhất.

```
Lệnh tham chiếu: flow/concept_index.md
```

---

## BƯỚC 2 — Tạo Fingerprint (Dấu vân tay) cho ý tưởng mới

Với mỗi ý tưởng cần evaluate, Coslient phải trích xuất **5 fingerprint dimensions (chiều vân tay)**:

```
FINGERPRINT CHECK:
Subject:       [tag từ taxonomy]
Emotional Arc: [tag từ taxonomy]
Story Pattern: [tag từ taxonomy]
Setting:       [tag từ taxonomy]
Hook Type:     [tag từ taxonomy]
```

**Taxonomy reference (Tham chiếu phân loại)** (xem đầy đủ trong concept_index.md):
- Subject (Chủ thể): `dog`, `cat`, `horse`, `bird`, `old-man`, `old-woman`, `ocean`, `tree`, `garden`, `letter`, `book`, `music`, `photo`, `food`, `scent`, `friendship`, `library`, `village`...
- Emotional Arc (Cung bậc cảm xúc): `loss→peace`, `loneliness→warmth`, `regret→acceptance`, `chaos→calm`, `past→present`, `sacrifice→legacy`, `isolation→connection`, `forgotten→remembered`
- Story Pattern (Mô típ câu chuyện): `object-triggers-memory`, `final-goodbye`, `hidden-love-revealed`, `journey-home`, `passing-down-legacy`, `unexpected-connection`, `daily-ritual-as-love`, `letter-unsent`, `return-to-roots`, `found-message`
- Setting (Bối cảnh): `seaside-town`, `small-town`, `garden`, `forest`, `train`, `library`, `home-interior`, `open-field`, `memory-dreamscape`
- Hook Type (Loại mồi nhử): `rhetorical-question`, `paradox`, `reversal`, `time-collapse`, `object-speaks`, `universal-truth`

---

## BƯỚC 3 — Chạy Collision Check (Kiểm tra va chạm)

So sánh fingerprint của ý tưởng mới với REGISTRY và COLLISION WARNINGS (Cảnh báo va chạm) trong `concept_index.md`.

### Quy tắc va chạm:

| Số chiều trùng | Kết luận | Hành động |
|---|---|---|
| **0–1 chiều trùng** | ✅ CLEAR (An toàn) | Tiếp tục bình thường |
| **2 chiều trùng** | ⚠️ CAUTION (Cảnh báo) | Đánh dấu, đề xuất twist (điểm nhấn khác biệt) để phân biệt |
| **3+ chiều trùng** | 🔴 COLLISION (Va chạm) | Từ chối — yêu cầu định hình lại hoặc cắt bỏ |
| **Trong COLLISION WARNINGS** | 🚨 BLOCKED (Bị chặn) | Từ chối ngay — không cần đếm chiều |

### Ví dụ thực tế:

**Ý tưởng mới:** "Ông lão ngồi bên cửa sổ nhớ về những buổi chiều câu cá ở sông"
```
Subject:       old-man ← trùng với v046, v047, v048, v049, v051...
Emotional Arc: past→present ← trùng với v046, v048, v049, v055, v059
Story Pattern: object-triggers-memory ← trùng với v046, v049, v055
Setting:       home-interior ← trùng với v053, v054, v055, v056, v058
Hook Type:     time-collapse ← trùng v048, v055, v059, v060

→ 5/5 chiều trùng → 🔴 COLLISION. PHẢI REJECT (Từ chối) hoặc đổi triệt để.
```

---

## BƯỚC 4 — Báo cáo kết quả cho Boss

### Template khi CLEAR (An toàn):
```
DEDUP CHECK: ✅ CLEAR
Fingerprint: [subject] + [arc] + [pattern]
Không trùng với bất kỳ video nào trong registry.
→ Tiếp tục evaluate/phát triển concept.
```

### Template khi CAUTION (Cẩn thận):
```
DEDUP CHECK: ⚠️ CAUTION — [số] chiều trùng
Trùng với: video_[X] ([title]) — [chiều trùng]

Twist đề xuất để phân biệt:
- [Option 1: đổi Subject]
- [Option 2: đổi Setting]
- [Option 3: đổi Story Pattern]

Boss muốn giữ hay đổi hướng?
```

### Template khi COLLISION (Va chạm):
```
DEDUP CHECK: 🔴 COLLISION — [số] chiều trùng
Trùng với: 
- video_[X]: [title] — trùng [chiều]
- video_[Y]: [title] — trùng [chiều]

⛔ Concept này quá gần với nội dung đã làm. Nếu tiếp tục sẽ:
1. Làm loãng nội dung kênh
2. Giảm shareability (khả năng chia sẻ) vì audience (khán giả) cảm giác "đã xem rồi"

PHẢI chọn 1 trong 2:
A. Reshape (Định hình lại) — đổi [chiều X] để tạo đủ khoảng cách
B. Cut (Cắt) — chuyển sang ý tưởng khác

Tôi đề xuất: [A/B] vì [lý do ngắn].
```

---

## Quy tắc đặc biệt — COOLING PERIOD (Thời gian làm nguội)

Nếu **cùng 1 Story Pattern** xuất hiện ≥3 lần trong 10 video gần nhất:
- Pattern đó phải "nghỉ" tối thiểu **5 video** trước khi dùng lại
- Ví dụ hiện tại: `found-message` xuất hiện ở v058, v059, v060 → BLOCKED cho v061–v065

---

## Quy tắc đặc biệt — DIVERSITY FLOOR (Ngưỡng đa dạng)

Mỗi 10 video phải đảm bảo:
- ≥ 3 Subject khác nhau (không phải toàn `old-man`)
- ≥ 3 Setting khác nhau (không phải toàn `home-interior`)
- ≥ 4 Emotional Arc khác nhau

Nếu distribution (sự phân bổ) lệch → ưu tiên **Open Territory (Vùng đất mở)** trong concept_index.md.

---

## CẬP NHẬT INDEX SAU KHI APPROVE (Phê duyệt)

Sau mỗi lần Boss approve concept:

```
1. Mở flow/concept_index.md
2. Thêm entry mới vào bảng REGISTRY:
   | v[số] | [title] | [subject] | [arc] | [pattern] | [setting] | [hook] | [notes ngắn] |
3. Cập nhật Collision Warnings nếu có pattern mới đạt ≥2 lần
4. Cập nhật Distribution Tracking (Theo dõi phân bổ) (tăng count)
5. Cập nhật Open Territory nếu một hướng vừa được khai thác
6. Ghi "Last updated: [date]" ở cuối file
```

> [!CAUTION]
> **Không bao giờ skip (bỏ qua) bước cập nhật index.** Mỗi lần skip = lần sau không có data để check = hệ thống vô dụng.

---

## Core Philosophy (Triết lý cốt lõi)

Channel có thể làm về cùng 1 theme (chủ đề) (nostalgia, sacrifice, legacy) nhưng phải đến qua **cánh cửa khác nhau** mỗi lần. Cánh cửa = combination (sự kết hợp) của Subject + Pattern + Setting. Cùng cánh cửa = audience cảm thấy déjà vu (quen thuộc) → skip (bỏ qua).
