# Coslient GPT Knowledge - Concept Deduplication (Anti-Clone Protocol) v1.0

## Mục đích

Ngăn channel tự lặp lại concept với chính mình. Với 60+ videos, rủi ro clone ý tưởng nội bộ ngày càng lớn — đặc biệt ở các yếu tố mà Boss và Coslient đều ưu thích: old man, home interior, object-triggers-memory.

**File này hoạt động cùng `concept_index.md` — không thể dùng riêng lẻ.**

---

## Khi nào kích hoạt Protocol này?

Bắt buộc kích hoạt tại **2 checkpoint**:

1. **Stage 1 — Idea Intake:** Trước khi gắn nhãn `STRONG` cho bất kỳ ý tưởng nào
2. **Stage 2 — Concept Development:** Trước khi Boss approve concept final

---

## BƯỚC 1 — Đọc concept_index.md

> [!IMPORTANT]
> **Coslient phải đọc file `flow/concept_index.md` trước khi evaluate bất kỳ ý tưởng mới nào.**  
> Không được bỏ qua dù Boss đang hối thúc. File này là nguồn sự thật duy nhất.

```
Lệnh tham chiếu: flow/concept_index.md
```

---

## BƯỚC 2 — Tạo Fingerprint cho ý tưởng mới

Với mỗi ý tưởng cần evaluate, Coslient phải trích xuất **5 fingerprint dimensions**:

```
FINGERPRINT CHECK:
Subject:       [tag từ taxonomy]
Emotional Arc: [tag từ taxonomy]
Story Pattern: [tag từ taxonomy]
Setting:       [tag từ taxonomy]
Hook Type:     [tag từ taxonomy]
```

**Taxonomy reference** (xem đầy đủ trong concept_index.md):
- Subject: `dog`, `cat`, `horse`, `bird`, `old-man`, `old-woman`, `ocean`, `tree`, `garden`, `letter`, `book`, `music`, `photo`, `food`, `scent`, `friendship`, `library`, `village`...
- Emotional Arc: `loss→peace`, `loneliness→warmth`, `regret→acceptance`, `chaos→calm`, `past→present`, `sacrifice→legacy`, `isolation→connection`, `forgotten→remembered`
- Story Pattern: `object-triggers-memory`, `final-goodbye`, `hidden-love-revealed`, `journey-home`, `passing-down-legacy`, `unexpected-connection`, `daily-ritual-as-love`, `letter-unsent`, `return-to-roots`, `found-message`
- Setting: `seaside-town`, `small-town`, `garden`, `forest`, `train`, `library`, `home-interior`, `open-field`, `memory-dreamscape`
- Hook Type: `rhetorical-question`, `paradox`, `reversal`, `time-collapse`, `object-speaks`, `universal-truth`

---

## BƯỚC 3 — Chạy Collision Check

So sánh fingerprint của ý tưởng mới với REGISTRY và COLLISION WARNINGS trong `concept_index.md`.

### Quy tắc va chạm:

| Số chiều trùng | Kết luận | Hành động |
|---|---|---|
| **0–1 chiều trùng** | ✅ CLEAR | Tiếp tục bình thường |
| **2 chiều trùng** | ⚠️ CAUTION | Flag, đề xuất twist để phân biệt |
| **3+ chiều trùng** | 🔴 COLLISION | Từ chối — yêu cầu reshape hoặc cắt |
| **Trong COLLISION WARNINGS** | 🚨 BLOCKED | Từ chối ngay — không cần đếm chiều |

### Ví dụ thực tế:

**Ý tưởng mới:** "Ông lão ngồi bên cửa sổ nhớ về những buổi chiều câu cá ở sông"
```
Subject:       old-man ← trùng với v046, v047, v048, v049, v051...
Emotional Arc: past→present ← trùng với v046, v048, v049, v055, v059
Story Pattern: object-triggers-memory ← trùng với v046, v049, v055
Setting:       home-interior ← trùng với v053, v054, v055, v056, v058
Hook Type:     time-collapse ← trùng v048, v055, v059, v060

→ 5/5 chiều trùng → 🔴 COLLISION. PHẢI REJECT hoặc đổi triệt để.
```

---

## BƯỚC 4 — Báo cáo kết quả cho Boss

### Template khi CLEAR:
```
DEDUP CHECK: ✅ CLEAR
Fingerprint: [subject] + [arc] + [pattern]
Không trùng với bất kỳ video nào trong registry.
→ Tiếp tục evaluate/phát triển concept.
```

### Template khi CAUTION:
```
DEDUP CHECK: ⚠️ CAUTION — [số] chiều trùng
Trùng với: video_[X] ([title]) — [chiều trùng]

Twist đề xuất để phân biệt:
- [Option 1: đổi Subject]
- [Option 2: đổi Setting]
- [Option 3: đổi Story Pattern]

Boss muốn giữ hay đổi hướng?
```

### Template khi COLLISION:
```
DEDUP CHECK: 🔴 COLLISION — [số] chiều trùng
Trùng với: 
- video_[X]: [title] — trùng [chiều]
- video_[Y]: [title] — trùng [chiều]

⛔ Concept này quá gần với nội dung đã làm. Nếu tiếp tục sẽ:
1. Làm loãng nội dung kênh
2. Giảm shareability vì audience cảm giác "đã xem rồi"

PHẢI chọn 1 trong 2:
A. Reshape — đổi [chiều X] để tạo đủ khoảng cách
B. Cut — chuyển sang ý tưởng khác

Tôi đề xuất: [A/B] vì [lý do ngắn].
```

---

## Quy tắc đặc biệt — COOLING PERIOD

Nếu **cùng 1 Story Pattern** xuất hiện ≥3 lần trong 10 video gần nhất:
- Pattern đó phải "nghỉ" tối thiểu **5 video** trước khi dùng lại
- Ví dụ hiện tại: `found-message` xuất hiện ở v058, v059, v060 → BLOCKED cho v061–v065

---

## Quy tắc đặc biệt — DIVERSITY FLOOR

Mỗi 10 video phải đảm bảo:
- ≥ 3 Subject khác nhau (không phải toàn `old-man`)
- ≥ 3 Setting khác nhau (không phải toàn `home-interior`)
- ≥ 4 Emotional Arc khác nhau

Nếu distribution lệch → ưu tiên **Open Territory** trong concept_index.md.

---

## CẬP NHẬT INDEX SAU KHI APPROVE

Sau mỗi lần Boss approve concept:

```
1. Mở flow/concept_index.md
2. Thêm entry mới vào bảng REGISTRY:
   | v[số] | [title] | [subject] | [arc] | [pattern] | [setting] | [hook] | [notes ngắn] |
3. Cập nhật Collision Warnings nếu có pattern mới đạt ≥2 lần
4. Cập nhật Distribution Tracking (tăng count)
5. Cập nhật Open Territory nếu một hướng vừa được khai thác
6. Ghi "Last updated: [date]" ở cuối file
```

> [!CAUTION]
> **Không bao giờ skip bước cập nhật index.** Mỗi lần skip = lần sau không có data để check = hệ thống vô dụng.

---

## Core Philosophy

Channel có thể làm về cùng 1 theme (nostalgia, sacrifice, legacy) nhưng phải đến qua **cánh cửa khác nhau** mỗi lần. Cánh cửa = combination của Subject + Pattern + Setting. Cùng cánh cửa = audience cảm thấy déjà vu → skip.
