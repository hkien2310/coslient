# Animation Prompts (Video 057)

Theo triết lý của Coslient GPT v7.0 đối với VEO 3: Sự đa dạng của chuyển động đến từ chính hình ảnh đầu vào. Do đó, chúng ta sẽ sử dụng **MỘT (01) prompt duy nhất** cho toàn bộ 140 ảnh để giữ sự đồng nhất về mood (cảm xúc) và style (phong cách).

## Universal Animation Prompt
Sử dụng dòng prompt ngắn gọn dưới đây cho **tất cả** các ảnh (copy-paste nguyên xi, KHÔNG có dấu ngoặc kép):

`warm nostalgic cinematic soft diorama surreal 4K`

---

## Các trường hợp Fallback (Xử lý sự cố)
Chỉ khi VEO 3 tạo ra video bị lỗi cho một bức ảnh cụ thể (camera quá giật, nhân vật méo mó, biến dạng), hãy thêm 1 cụm điều hướng vào đầu prompt. Dưới đây là các fallback tương ứng:

- **Nếu camera bị giật/lắc (Unstable camera):**
  `Tripod-stable framing. warm nostalgic cinematic soft diorama surreal 4K`

- **Nếu nhân vật hoặc đồ vật bị biến dạng/chảy lỏng (Morphing/Warping):**
  `Hold source image fidelity, subtle motion only. warm nostalgic cinematic soft diorama surreal 4K`

- **Nếu zoom hoặc lia máy quá nhanh (Excessive speed):**
  `Slow gentle motion throughout. warm nostalgic cinematic soft diorama surreal 4K`

- **Nếu các chi tiết bay lượn hỗn loạn:**
  `Static or near-static, preserve composition. warm nostalgic cinematic soft diorama surreal 4K`

---

## Lưu ý kỹ thuật cho quá trình render:
- **Độ dài mặc định:** Render 8 giây cho mỗi clip.
- **Không mô tả hành động:** Tuyệt đối không viết thêm các mô tả như "the boy runs", "the tree grows". VEO 3 sẽ tự "đọc" 140 bức ảnh tĩnh của chúng ta và tự động sinh ra chuyển động (ví dụ: khói bay, nước chảy, ông lão bước đi) phù hợp với bối cảnh siêu thực.
- **Không dùng dấu ngoặc kép (" ")** vì VEO sẽ hiểu nhầm đó là lệnh yêu cầu nhân vật mấp máy môi (lip-sync).
