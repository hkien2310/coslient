# Animation Prompts - Video 054 (The Wooden Floor)

Dựa trên **Quy trình Hoạt ảnh v4.0**, VEO 3 sẽ tự nội suy toàn bộ chuyển động từ hình ảnh gốc (camera move, nhân vật, physics). Boss **chỉ cần dùng 1 Prompt Khóa (Lock Prompt)** duy nhất cho TẤT CẢ các cảnh trong video này.

## Prompt Duy Nhất (Copy & Paste cho TẤT CẢ các clip)

```text
Audio: Diegetic environmental sound only — soft ambient sounds natural to this scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.

No internal glow. No magical particles. No sparkles. No floating light effects. No added visual effects not present in the source image.
```

---

## Giao thức Sửa lỗi (Fallback Protocol)
*Lưu ý: Chỉ thêm 1 dòng sửa lỗi này lên đầu prompt nếu clip bị lỗi rõ ràng (vỡ ảnh, camera giật, chuyển động quá mạnh). Nếu không lỗi, KHÔNG thêm gì cả.*

### 1. Nếu Camera bị giật/lắc:
```text
Tripod-stable framing.
```

### 2. Nếu Nhân vật (ông lão/chú chó) bị biến dạng:
```text
Hold source image fidelity, subtle motion only.
```

### 3. Nếu Cảnh bị zoom quá nhanh:
```text
Slow gentle motion throughout.
```

### 4. Nếu Chuyển động bị hỗn loạn / lộn xộn:
```text
Static or near-static, preserve composition.
```

---

## Workflow Nhắc nhở cho Video 054
1. **Độ dài clip VEO:** Set mặc định là **8 giây**.
2. **Nối cảnh (Frame bridging):** Lấy frame cuối của clip trước làm frame đầu cho clip sau để giữ sự liền mạch. Khi chuyển hẳn sang địa điểm mới (từ Ga Tàu sang Ngôi Nhà Gỗ), dùng ảnh tĩnh mới làm anchor.
3. **Âm thanh:** Nếu VEO nhét nhầm nhạc hoặc âm thanh lạ vào clip, Boss hãy dùng lệnh sau để tách bỏ audio:
   `ffmpeg -i input.mp4 -an output_no_audio.mp4`
   Sau đó chèn audio thật trong lúc edit.
