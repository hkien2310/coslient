# Kiến thức Coslient GPT — Phát triển Prompt Hoạt ảnh v5.0

## Mục đích

File này xác định cách Coslient xử lý giai đoạn hoạt ảnh sau khi bộ ảnh đã sẵn sàng.

Biến các hình ảnh đã được duyệt thành video clip sử dụng VEO 3 — với hệ thống Preset vạn năng để tối ưu đa dạng góc máy mà vẫn duy trì tốc độ sản xuất (workflow efficiency).

> **Cập nhật v5.0:** Triết lý mới — Định hướng góc máy điện ảnh ngẫu nhiên có kiểm soát (Controlled Cinematic Direction). Chấm dứt việc dùng prompt rỗng để VEO tự bơi (gây ra tình trạng lạm dụng zoom chậm tẻ nhạt). Sử dụng hệ thống 4 Preset vạn năng tích hợp vào Text Replacement (Gõ tắt) của MacOS để bốc thuốc nhanh cho từng ảnh mà không tốn công copy-paste.

---

## Vị trí giai đoạn

Giai đoạn này chỉ bắt đầu sau khi định hướng hình ảnh hoặc bộ ảnh đã được phê duyệt.
Không chuyển sang làm hoạt ảnh trước khi giai đoạn hình ảnh đã sẵn sàng.

---

## Công cụ: VEO 3 — Điều cần biết

VEO 3 tạo ra video và âm thanh trong cùng một lần xử lý thông qua chế độ từ-ảnh-sang-video (image-to-video).

**Những điều quan trọng nhất:**

- VEO đọc ảnh gốc trước khi đọc prompt. Nó đã biết nhân vật đang làm gì, ánh sáng đến từ đâu, không gian là gì
- **Prompt chi tiết về camera/chuyển động = nhiễu.** Nó tạo ra xung đột với những gì VEO tự nội suy từ ảnh → character drift (nhân vật bị lệch/biến dạng), ảnh vỡ
- Để VEO tự quyết định: camera move (di chuyển máy ảnh), character movement (chuyển động nhân vật), ambient physics (vật lý môi trường xung quanh như cỏ biển đung đưa, khói, vải vóc)
- Chỉ áp đặt những gì VEO không thể tự biết từ ảnh: **audio rules (quy tắc âm thanh) + no-effect lock (khóa hiệu ứng giả)**
- Chế độ image-to-video thường tạo ra clip không lời (silent clip) theo mặc định — điều này là tốt cho video âm nhạc (music video) vì mình đã có nhạc riêng
- Độ dài prompt (prompt length) tối ưu: **càng ngắn càng tốt.** Mục tiêu: dưới 60 từ

---

## Quy tắc Thực tế Bám sát (BẮT BUỘC — KHÔNG NHƯỢNG BỘ)

> [!IMPORTANT]
> Áp dụng cho MỌI clip, dù cảnh đời thường hay siêu thực.

Cái làm video trông rẻ tiền không phải là con rồng hay không gian kỳ lạ — mà là **hiệu ứng không có thật trong tự nhiên**.

**Tuyệt đối cấm:**
- Internal glow (phát sáng từ bên trong) từ nhân vật hoặc vật thể
- Magical particles (hạt phép thuật), sparkles (tia lấp lánh), stardust (bụi sao), light orbs (quả cầu ánh sáng)
- Sợi ánh sáng từ tay / người
- Lơ lửng không có lý do vật lý
- Ethereal mist (sương mù huyền ảo) quanh nhân vật
- Bất kỳ hiệu ứng nào chỉ tồn tại trong video game hoặc AI rẻ tiền (cheap AI)

---

## Hệ thống Preset Gõ Tắt (BẮT BUỘC SỬ DỤNG)

**Cài đặt 1 LẦN DUY NHẤT trên Mac:**
- Vào `System Settings` > `Keyboard` > `Text Replacements`
- Thêm 4 mục gõ tắt dưới đây (sử dụng dấu phẩy kép để tránh trùng lặp gõ phím thông thường).
- **Hệ thống 4 Preset này được thiết kế để bao phủ 100% mọi trường hợp ảnh (Mapping trực tiếp 1-1 với 4 loại Tiêu điểm Hình ảnh trong Giai đoạn 4).**

### 1. Preset Môi Trường/Toàn Cảnh (`,,v1`)
**Dùng cho:** Ảnh Establishing, phong cảnh, kiến trúc rộng (Không có người hoặc người rất nhỏ).
```
Slow cinematic pan or gentle forward push. Rich environmental physics (wind, water, moving light, atmospheric particles). Do not zoom. Audio: Diegetic environmental sound only. No music. No dialogue. No internal glow. No magical particles. No floating light effects.
```

### 2. Preset Hành Động Nhân Vật (`,,v2`)
**Dùng cho:** Nhân vật đang đi lại, làm việc, tương tác với đồ vật (Medium / Full shot).
```
Smooth tracking shot following the character's action. Natural character physics (hair, clothing) and environmental motion. Do not zoom. Audio: Diegetic environmental sound only. No music. No dialogue. No internal glow. No magical particles. No floating light effects.
```

### 3. Preset Cận Cảnh/Biểu Cảm (`,,v3`)
**Dùng cho:** Cận mặt (chớp mắt, thở), cận bàn tay (Macro), góc nhìn qua vai.
```
Subtle handheld camera feel. Intimate character micro-actions (breathing, blinking, gentle tactile movement). Do not zoom. Audio: Diegetic environmental sound only. No music. No dialogue. No internal glow. No magical particles. No floating light effects.
```

### 4. Preset Tĩnh Vật/Chiều Sâu (`,,v4`)
**Dùng cho:** Đồ vật mỏ neo (leitmotif), vệt nắng, tách trà, góc phòng tĩnh lặng (Still Life / Traces).
```
Static tripod camera. Cinematic rack focus (shifting depth of field) or very slow tilt. Gentle atmospheric motion (dust motes, light shifting). Do not zoom. Audio: Diegetic environmental sound only. No music. No dialogue. No internal glow. No magical particles. No floating light effects.
```


---

## Quy tắc bắt buộc

### Quy tắc 1 — Không mô tả lại nhân vật hay cảnh
VEO đã thấy ảnh gốc. Thêm mô tả (description) về hình ảnh (visual) sẽ khiến model hiểu lại (re-interpret) → nhân vật bị lệch/biến dạng (character drift), ảnh vỡ.
**Chỉ dán nguyên prompt, không thêm gì.**

### Quy tắc 2 — Không dùng dấu ngoặc kép `" "` ở bất kỳ đâu
VEO hiểu dấu ngoặc kép (quotes) = lệnh tạo hội thoại (command generate dialogue) + nhép môi (lip-sync). Kể cả trong phần âm thanh (audio section).

### Quy tắc 3 — Độ dài clip: 8 giây (mặc định)

### Quy tắc 4 — Nối khung hình (Frame bridging) giữa các clip
Khung hình cuối (Last frame) của clip A → làm khung hình bắt đầu (start frame) của clip B.
Khi đổi hoàn toàn địa điểm (location): tạo ảnh tĩnh mới làm mỏ neo (anchor) trước, rồi dùng làm khung hình bắt đầu.

### Quy tắc 5 — Tách âm thanh (Strip audio) nếu VEO tạo ra âm thanh lạ
```bash
ffmpeg -i input.mp4 -an output_no_audio.mp4
```
Sau đó chèn nhạc (overlay nhạc) riêng trong trình chỉnh sửa (editor).

---

## Giao thức Dự phòng (Fallback Protocol) — Khi 1 clip cụ thể ra sai

Chỉ can thiệp khi clip bị VEO xử lý sai rõ ràng (ảnh vỡ, chuyển động quá mạnh bạo, camera lắc). Thêm đúng **1 cụm sửa lỗi (fix)** vào đầu prompt — không viết lại cả đống.

| Triệu chứng | Thêm vào đầu prompt |
|:---|:---|
| Camera bị giật/lắc | `Tripod-stable framing.` |
| Nhân vật bị biến dạng | `Hold source image fidelity, subtle motion only.` |
| Cảnh bị zoom quá nhanh | `Slow gentle motion throughout.` |
| Chuyển động quá nhiều / hỗn loạn | `Static or near-static, preserve composition.` |

Sau khi thêm cụm sửa lỗi → vẫn giữ nguyên phần quy tắc âm thanh (audio) + khóa hiệu ứng giả (no-effect lock) phía dưới. Không thêm gì khác.

**Cấu trúc dự phòng (fallback):**
```
[1 cụm sửa lỗi từ bảng trên].

Audio: Diegetic environmental sound only — soft ambient sounds natural to this scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.

No internal glow. No magical particles. No sparkles. No floating light effects. No added visual effects not present in the source image.
```

---

## Quy trình làm việc (Workflow) thực tế

```
1. Có đủ ảnh gốc (đã qua Giai đoạn 4)
2. Nhập hàng loạt ảnh vào VEO 3
3. Liếc qua từng ảnh, phân loại nó vào 1 trong 4 nhóm (v1, v2, v3, v4)
4. Dùng tính năng gõ tắt (vd: gõ `,,v1` rồi Enter) để dán preset tương ứng
5. Độ dài clip: 8 giây
6. Xử lý hàng loạt (Batch) xong → đánh giá (review) toàn bộ
5. Clip nào sai → thêm đúng 1 cụm sửa lỗi (fix) từ bảng giao thức dự phòng
6. Tách âm thanh (Strip audio) VEO nếu cần: ffmpeg -i input.mp4 -an output.mp4
7. Chèn nhạc (Overlay nhạc) trong trình chỉnh sửa (editor)
8. Nối khung hình (Frame bridging) khi chỉnh sửa (edit): last frame A → start frame B
```

---

## Quy tắc cốt lõi

VEO 3 là một đạo diễn hình ảnh (visual director). Ảnh tốt + để nó tự đọc = 90% công việc xong. Kiểm soát thật sự đến từ **chất lượng ảnh gốc** — prompt chỉ là lớp bảo vệ âm thanh (audio) và chống hiệu ứng giả (no-effect). Đừng nghĩ mình thông minh hơn model khi nó đang nhìn thấy hình ảnh.

Mọi clip phải có thể chạm tay vào được.
