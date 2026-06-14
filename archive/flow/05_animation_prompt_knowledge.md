# Coslient GPT Knowledge — Animation Prompt Development v4.0

## Purpose

This file defines how Coslient handles the animation stage after the image set is ready.

Turn approved images into video clips using VEO 3 — with a minimal-lock prompt applied to all clips.

> **v4.0 Update:** Triết lý mới — AI-inferred motion. Không dùng universal camera/motion directive nữa. VEO 3 tự đọc ảnh và nội suy tất cả: camera move, character motion, ambient physics. Chỉ khóa cứng audio rules + no-effect protection.

---

## Stage position

This stage begins only after the image direction or image set is approved.
Do not move to animation before the image stage is ready.

---

## Tool: VEO 3 — Điều cần biết

VEO 3 generates video and audio in a single pass via image-to-video mode.

**Những điều quan trọng nhất:**

- VEO đọc ảnh gốc trước khi đọc prompt. Nó đã biết nhân vật đang làm gì, ánh sáng đến từ đâu, không gian là gì
- **Prompt chi tiết về camera/motion = nhiễu.** Nó tạo ra xung đột với những gì VEO tự nội suy từ ảnh → character drift, ảnh vỡ
- Để VEO tự quyết định: camera move, character movement, ambient physics (seagrass sway, steam, fabric)
- Chỉ áp đặt những gì VEO không thể tự biết từ ảnh: **audio rules + no-effect lock**
- Image-to-video mode thường ra silent clip theo mặc định — đây là tốt cho music video vì mình có nhạc riêng
- Prompt length tối ưu: **càng ngắn càng tốt.** Mục tiêu: dưới 60 từ

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

---

## Prompt Duy Nhất — Paste vào TẤT CẢ clip (nguyên xi, không thêm gì)

```
Audio: Diegetic environmental sound only — soft ambient sounds natural to this scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.

No internal glow. No magical particles. No sparkles. No floating light effects. No added visual effects not present in the source image.
```

**Để VEO tự nội suy:** camera movement, character motion, ambient physics. Đừng can thiệp trừ khi clip bị sai rõ ràng.

---

## Quy tắc bắt buộc

### Rule 1 — Không mô tả lại nhân vật hay cảnh
VEO đã thấy ảnh gốc. Thêm description về visual sẽ khiến model re-interpret → character drift, ảnh vỡ.
**Chỉ paste nguyên prompt, không thêm gì.**

### Rule 2 — Không dùng dấu ngoặc kép `" "` ở bất kỳ đâu
VEO hiểu quotes = command generate dialogue + lip-sync. Kể cả trong audio section.

### Rule 3 — Clip length: 8 giây (default)

### Rule 4 — Frame bridging giữa các clip
Last frame của clip A → làm start frame của clip B.
Khi đổi location hoàn toàn: generate ảnh tĩnh mới làm anchor trước, rồi dùng làm start frame.

### Rule 5 — Strip audio nếu VEO gen sound lạ
```bash
ffmpeg -i input.mp4 -an output_no_audio.mp4
```
Sau đó overlay nhạc riêng trong editor.

---

## Fallback Protocol — Khi 1 clip cụ thể ra sai

Chỉ can thiệp khi clip bị VEO xử lý sai rõ ràng (ảnh vỡ, motion quá aggressive, camera lắc). Thêm đúng **1 cụm fix** vào đầu prompt — không viết lại cả đống.

| Triệu chứng | Thêm vào đầu prompt |
|:---|:---|
| Camera bị giật/lắc | `Tripod-stable framing.` |
| Nhân vật bị biến dạng | `Hold source image fidelity, subtle motion only.` |
| Cảnh bị zoom quá nhanh | `Slow gentle motion throughout.` |
| Motion quá nhiều / hỗn loạn | `Static or near-static, preserve composition.` |

Sau khi thêm cụm fix → vẫn giữ nguyên phần audio + no-effect lock phía dưới. Không thêm gì khác.

**Cấu trúc fallback:**
```
[1 cụm fix từ bảng trên].

Audio: Diegetic environmental sound only — soft ambient sounds natural to this scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.

No internal glow. No magical particles. No sparkles. No floating light effects. No added visual effects not present in the source image.
```

---

## Workflow thực tế

```
1. Có đủ ảnh gốc (đã qua Stage 4)
2. Copy prompt duy nhất → paste vào VEO cho từng ảnh (không thêm gì)
3. Clip length: 8 giây
4. Batch xong → review toàn bộ
5. Clip nào sai → thêm đúng 1 cụm fix từ bảng fallback
6. Strip audio VEO nếu cần: ffmpeg -i input.mp4 -an output.mp4
7. Overlay nhạc trong editor
8. Frame bridging khi edit: last frame A → start frame B
```

---

## Core rule

VEO 3 là một visual director. Ảnh tốt + để nó tự đọc = 90% công việc xong. Kiểm soát thật sự đến từ **chất lượng ảnh gốc** — prompt chỉ là lớp bảo vệ audio và no-effect. Đừng nghĩ mình thông minh hơn model khi nó đang nhìn thấy hình ảnh.

Mọi clip phải có thể chạm tay vào được.
