# Animation Prompts - Video 055 (The Architecture of Smoke)

Dựa trên **Quy trình Hoạt ảnh v5.0**, chúng ta sẽ chấm dứt việc dùng prompt rỗng để VEO tự bơi. Thay vào đó, áp dụng triết lý **Định hướng góc máy điện ảnh ngẫu nhiên có kiểm soát** thông qua Hệ thống 4 Preset vạn năng.

> **💡 Lời khuyên:** Boss hãy lưu 4 preset này vào Text Replacement (Gõ tắt) của MacOS (System Settings > Keyboard > Text Replacements) để bốc thuốc nhanh cho 160 ảnh mà không tốn công copy-paste nhé!

---

## Hệ thống 4 Preset Vạn Năng (Sử dụng cho VEO 3)

### 1. Preset Môi Trường/Toàn Cảnh (Gõ tắt gợi ý: `,,v1`)
**Dùng cho:** Những shot Wide Establishing (ví dụ cảnh đường phố mưa, không gian bếp, vườn cây), không có nhân vật hoặc nhân vật rất nhỏ.
```text
Slow cinematic pan or gentle forward push. Rich environmental physics (wind, water, moving light, atmospheric particles). Do not zoom. Audio: Diegetic environmental sound only. No music. No dialogue. No internal glow. No magical particles. No floating light effects.
```

### 2. Preset Hành Động Nhân Vật (Gõ tắt gợi ý: `,,v2`)
**Dùng cho:** Nhân vật ông lão đang bước đi, làm việc, tương tác với không gian (Medium / Full shot).
```text
Smooth tracking shot following the character's action. Natural character physics (hair, clothing) and environmental motion. Do not zoom. Audio: Diegetic environmental sound only. No music. No dialogue. No internal glow. No magical particles. No floating light effects.
```

### 3. Preset Cận Cảnh/Biểu Cảm (Gõ tắt gợi ý: `,,v3`)
**Dùng cho:** Cận mặt ông lão (nháy mắt, thở, rưng rưng), cận bàn tay (Macro shot).
```text
Subtle handheld camera feel. Intimate character micro-actions (breathing, blinking, gentle tactile movement). Do not zoom. Audio: Diegetic environmental sound only. No music. No dialogue. No internal glow. No magical particles. No floating light effects.
```

### 4. Preset Tĩnh Vật/Chiều Sâu (Gõ tắt gợi ý: `,,v4`)
**Dùng cho:** Bếp lò cháy đỏ, tách trà bốc khói, góc bếp tĩnh lặng, giọt sương, đốm than hồng (Still Life / Leitmotif).
```text
Static tripod camera. Cinematic rack focus (shifting depth of field) or very slow tilt. Gentle atmospheric motion (dust motes, light shifting). Do not zoom. Audio: Diegetic environmental sound only. No music. No dialogue. No internal glow. No magical particles. No floating light effects.
```

---

## Giao thức Dự phòng (Fallback Protocol)

**Lưu ý:** VEO đọc ảnh gốc trước, do đó chỉ can thiệp sửa lỗi nếu clip VEO tạo ra bị hỏng. Thêm **DUY NHẤT 1 cụm sửa lỗi** dưới đây vào ĐẦU preset:

| Triệu chứng lỗi của VEO | Cụm từ cần thêm vào đầu Preset |
|:---|:---|
| Camera bị giật/lắc | `Tripod-stable framing. ` |
| Khuôn mặt ông lão bị biến dạng | `Hold source image fidelity, subtle motion only. ` |
| Cảnh bị zoom quá nhanh | `Slow gentle motion throughout. ` |
| Chuyển động quá hỗn loạn | `Static or near-static, preserve composition. ` |

---

## Workflow Thực Hành cho Video 055
1. **Import:** Kéo hàng loạt ảnh (đã gen từ file `04_image_prompts_all.txt`) vào VEO 3.
2. **Bốc thuốc:** Liếc qua từng ảnh xem nó thuộc loại nào (Toàn cảnh / Hành động / Cận cảnh / Tĩnh vật) và gõ tắt preset tương ứng (`,,v1` -> `,,v4`).
3. **Độ dài clip:** Đặt mặc định là **8 giây**.
4. **No-Effect Lock:** Lưu ý mọi preset đều đã khóa các hiệu ứng giả (phát sáng trong, bụi phép thuật, lơ lửng) để giữ vững style "Everyday Detail" (Warm Storybook) chân thực nhất.
5. **Tách âm thanh (Nếu cần):** Nếu VEO tạo ra nhạc hoặc âm thanh lỗi, dùng lệnh:
   `ffmpeg -i input.mp4 -an output_no_audio.mp4`
6. **Nối khung hình (Frame bridging):** Khung hình cuối của clip trước dùng làm Start Frame cho clip sau để tạo luồng video mượt mà.
