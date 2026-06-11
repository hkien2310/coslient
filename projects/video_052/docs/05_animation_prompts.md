# STAGE 5: ANIMATION PROMPTS
**Project:** Video 52 — The Ocean Keepers
**Tool:** VEO 3 (Image-to-Video Mode)
**Duration:** 8 seconds per clip
**Version:** 2.0 — Minimal Lock / AI-Inferred Motion

---

## TRIẾT LÝ TIẾP CẬN

VEO 3 đọc hình ảnh gốc trước, prompt sau. Nó đã thấy nhân vật đang làm gì, không gian là gì, ánh sáng đến từ đâu. Prompt chi tiết quá sẽ tạo **xung đột** giữa những gì VEO thấy và những gì ta nói → ảnh bị vỡ, nhân vật bị drift.

**Quy tắc vận hành:**
- Để VEO tự nội suy: chuyển động camera, hành động nhân vật, nhịp điệu cảnh
- Chỉ áp đặt những gì VEO không thể tự biết từ ảnh: audio rules + style protection

---

## PROMPT DUY NHẤT (Paste vào tất cả clip)

```
Audio: Diegetic environmental sound only — soft underwater ambient, quiet ocean currents, faint bubbling, or interior warmth depending on the scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.

No internal glow. No magical particles. No sparkles. No floating light effects. No added visual effects not present in the source image.
```

---

## HƯỚNG DẪN SỬ DỤNG

**Bước 1:** Upload ảnh gốc vào VEO 3 (image-to-video mode)

**Bước 2:** Paste prompt trên vào — không thêm gì khác

**Bước 3:** Clip length: 8 giây

**Bước 4:** Xem VEO tự quyết định:
- Camera move (push-in, drift, static, parallax)
- Chuyển động nhân vật (breathing, reaching, turning)
- Ambient physics (seagrass sway, bubble rise, steam drift)

---

## XỬ LÝ AUDIO SAU KHI RENDER

VEO 3 đôi khi tự chế nhạc bất chấp lệnh cấm. Nếu clip bị dính nhạc lạ — bóc audio ra:

```bash
ffmpeg -i input.mp4 -an output_no_audio.mp4
```

Sau đó overlay nhạc gốc trong phần mềm edit như bình thường.

---

## KHI NÀO CẦN CAN THIỆP THÊM

Chỉ thêm instruction khi clip bị VEO xử lý sai rõ ràng (ảnh vỡ, nhân vật biến dạng, motion quá aggressive). Khi đó thêm đúng 1 cụm vào đầu prompt:

| Triệu chứng | Thêm vào đầu prompt |
|:---|:---|
| Camera bị giật/lắc | `Tripod-stable framing.` |
| Nhân vật bị biến dạng | `Hold source image fidelity, subtle motion only.` |
| Cảnh bị zoom quá nhanh | `Slow gentle motion throughout.` |
| Motion quá nhiều / hỗn loạn | `Static or near-static, preserve composition.` |

Sau khi thêm cụm fix → vẫn giữ nguyên phần audio + no-effect lock phía dưới. Không thêm gì khác.

---

## FALLBACK AN TOÀN — Lỗi "third-party content providers"

**Nguyên nhân:** VEO 3 phát hiện ảnh gốc có thể dính bản quyền — thường do keyword **"Laika Studios"**, **"Pixar"**, **"Disney"** hoặc tên studio bất kỳ xuất hiện trong metadata hoặc trong prompt gốc khi gen ảnh. VEO 3 không cho phép animate ảnh mà nó nghi là IP của bên thứ ba.

**Cách xử lý:** Dùng prompt dưới đây thay thế hoàn toàn. Prompt này không mention bất kỳ studio, style reference, hay brand nào. Hoàn toàn trung lập.

```
An original handcrafted clay animation scene. Animate naturally based on what is visible in the image.

Audio: Diegetic environmental sound only — soft ambient sounds natural to this scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.

No internal glow. No magical particles. No sparkles. No floating light effects. No added visual effects not present in the source image.
```

**Lưu ý thêm nếu vẫn bị lỗi:**
- Thử re-export lại ảnh gốc (Save As PNG mới) để xóa metadata cũ trước khi upload lại
- Nếu vẫn lỗi, ảnh đó bị VEO block hoàn toàn — skip qua, gen ảnh thay thế với prompt ảnh không có reference tên studio
