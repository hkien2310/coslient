# Storyboard Template — [Tên dự án]

> **Stage:** 3.5 — Storyboard Planning
> **Điều kiện:** Chỉ tạo file này SAU KHI Boss đã duyệt bài hát (Stage 3).
> **Tiếp theo:** Stage 4.1 chỉ bắt đầu sau khi Boss duyệt bảng storyboard bên dưới.

---

## Thông số bài hát

- **Song title:** [...]
- **Duration:** [phút:giây] → [tổng giây]
- **BPM:** [...]
- **Song structure:**

| Section | Thời lượng (giây) | Số shots (÷5, làm tròn lên) |
|---------|-----------------|---------------------------|
| Intro | | |
| Verse 1 | | |
| Pre-Chorus | | |
| Chorus 1 | | |
| Verse 2 | | |
| Pre-Chorus 2 | | |
| Chorus 2 | | |
| Bridge | | |
| Final Chorus | | |
| Outro | | |
| **TỔNG** | **[tổng giây]s** | **[tổng shots] shots** |

> **Cách tính:** Tổng giây ÷ 5 = tổng shots cần tạo (làm tròn lên).
> Ví dụ: bài 4:10 = 250 giây ÷ 5 ≈ **50 shots**.

---

## Locked Settings (Điền sau khi hoàn thành Stage 4.1)

```
LOCKED COLOR TONE: [copy nguyên văn từ Stage 4.1 Bước 3]
ACTIVE STYLE: [tên file style đang dùng]
```

**Locked Spatial World** (thế giới của video này):
- Không gian chính: [VD: ngôi nhà nhỏ ven đồi, bếp gỗ, hành lang, vườn sau nhà]
- Ánh sáng chủ đạo: [VD: sáng sớm — ánh sáng từ cửa sổ đông, vàng nhạt ấm]
- Visual motif lặp lại: [VD: chiếc cốc sứ xanh nhạt — xuất hiện ở Intro, Chorus, Outro]

---

## Storyboard

> **Cột Spatial Anchor:** Mô tả ngắn vị trí nhân vật + hướng ánh sáng + đồ vật chính trong frame.
> Shot N+1 cùng không gian với Shot N → **phải kế thừa Spatial Anchor**.
> Shot N+1 đổi location → ghi **[NEW LOCATION]** và đặt lại Spatial Anchor.

| Shot ID | Section | Timecode | Type | Spatial Anchor | Camera | Action / Scene | Emotional Beat | → Next |
|---------|---------|----------|------|---------------|--------|---------------|----------------|--------|
| SB_001 | Intro | 0:00–0:05 | ENV | [bối cảnh] | Wide, eye-level | [cảnh gì] | [cảm xúc] | → SB_002 |
| SB_002 | Intro | 0:05–0:10 | STORY | [kế thừa SB_001] | Medium | [cảnh gì] | [cảm xúc] | → SB_003 |
| SB_003 | Intro | 0:10–0:18 | DETAIL | [cận vật thể] | Close | [cảnh gì] | [cảm xúc] | → SB_004 |
| | | | | | | | | |

> **Type legend:**
> - **STORY** — Nhân vật hành động / cảm xúc dẫn dắt (mục tiêu ~50%)
> - **ENV** — Bối cảnh không người, môi trường kể chuyện (mục tiêu ~25%)
> - **DETAIL** — Cận vật thể / tay / ánh sáng / texture (mục tiêu ~25%)

---

## Shot Continuity Rules (Agent tự kiểm tra khi viết storyboard)

1. **Spatial Lock** — Shot N+1 cùng không gian với Shot N: giữ nguyên vị trí nhân vật và hướng ánh sáng.
2. **Light Direction Lock** — Hướng sáng không đổi trong cùng không gian. Chỉ đổi khi chuyển scene hoặc time-jump.
3. **Camera Jump Rule** — Không cắt trực tiếp close-up → close-up cùng hướng. Phải có medium/wide xen giữa.
4. **Emotional Flow** — Emotional Beat của Shot N+1 là tiếp nối hoặc đối nghịch có chủ ý từ Shot N.
5. **Shot Type Rotation** — Không xếp liên tiếp quá 3 STORY shots. Phải xen ENV hoặc DETAIL.

---

## Shot Type Distribution (tự kiểm tra trước khi trình Boss)

- STORY shots: [ ] / [tổng] = [ ]%  (mục tiêu ~50%)
- ENV shots:   [ ] / [tổng] = [ ]%  (mục tiêu ~25%)
- DETAIL shots: [ ] / [tổng] = [ ]% (mục tiêu ~25%)

---

## VEO Bridge Map (Điền sau khi storyboard được duyệt — dùng khi animate)

| Từ Shot | Sang Shot | Bridge Type | Ghi chú |
|---------|----------|------------|---------|
| SB_001 | SB_002 | Direct | Cùng không gian, last frame → start frame |
| SB_003 | SB_004 | Environmental | Đổi location — insert ENV shot |
| SB_010 | SB_011 | Detail | Time jump — dùng cận vật thể |

> **Bridge Types:**
> - **Direct** — Cùng không gian, góc máy khác → last frame A làm start frame B
> - **Environmental** — Đổi location → tạo ENV shot làm "xả" trước khi vào location mới
> - **Detail** — Time jump → tạo DETAIL shot (cận vật thể) — không cần match spatial anchor
