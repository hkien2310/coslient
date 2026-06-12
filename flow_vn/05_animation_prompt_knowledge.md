# Kiến thức Coslient GPT — Phát triển Prompt Hoạt ảnh v4.0

## Mục đích

File này xác định cách Coslient xử lý giai đoạn hoạt ảnh sau khi bộ ảnh đã sẵn sàng.

Biến các hình ảnh đã được duyệt thành video clip sử dụng VEO 3 — với một prompt khóa tối thiểu áp dụng cho tất cả các clip.

> **Cập nhật v4.0:** Triết lý mới — Chuyển động do AI tự suy luận (AI-inferred motion). Không dùng các chỉ thị camera/chuyển động chung (universal camera/motion directive) nữa. VEO 3 tự đọc ảnh và nội suy tất cả: camera move (di chuyển máy ảnh), character motion (chuyển động nhân vật), ambient physics (vật lý môi trường xung quanh). Chỉ khóa cứng audio rules (quy tắc âm thanh) + no-effect protection (bảo vệ không hiệu ứng giả tạo).

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

## Prompt Duy Nhất — Dán vào TẤT CẢ clip (nguyên xi, không thêm gì)

```
Audio: Diegetic environmental sound only — soft ambient sounds natural to this scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.

No internal glow. No magical particles. No sparkles. No floating light effects. No added visual effects not present in the source image.
```

**Để VEO tự nội suy:** di chuyển máy ảnh, chuyển động nhân vật, vật lý môi trường xung quanh. Đừng can thiệp trừ khi clip bị sai rõ ràng.

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
2. Copy prompt duy nhất → dán vào VEO cho từng ảnh (không thêm gì)
3. Độ dài clip: 8 giây
4. Xử lý hàng loạt (Batch) xong → đánh giá (review) toàn bộ
5. Clip nào sai → thêm đúng 1 cụm sửa lỗi (fix) từ bảng giao thức dự phòng
6. Tách âm thanh (Strip audio) VEO nếu cần: ffmpeg -i input.mp4 -an output.mp4
7. Chèn nhạc (Overlay nhạc) trong trình chỉnh sửa (editor)
8. Nối khung hình (Frame bridging) khi chỉnh sửa (edit): last frame A → start frame B
```

---

## Quy tắc cốt lõi

VEO 3 là một đạo diễn hình ảnh (visual director). Ảnh tốt + để nó tự đọc = 90% công việc xong. Kiểm soát thật sự đến từ **chất lượng ảnh gốc** — prompt chỉ là lớp bảo vệ âm thanh (audio) và chống hiệu ứng giả (no-effect). Đừng nghĩ mình thông minh hơn model khi nó đang nhìn thấy hình ảnh.

Mọi clip phải có thể chạm tay vào được.
