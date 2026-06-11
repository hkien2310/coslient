# Cẩm Nang Kỹ Thuật Prompting Cho AI Tạo Ảnh
*(Tổng hợp từ các tài liệu chuẩn của Midjourney, OpenAI, Google Nano Banana, và Leonardo AI)*

Cẩm nang này cung cấp nền tảng tổng quát để bạn có thể kiểm soát và tạo ra hình ảnh chất lượng cao trên hầu hết các công cụ AI hiện nay (ChatGPT 4o, Midjourney, Leonardo AI, v.v.).

---

## 1. Hiểu Về "Tính Cách" Của Các Mô Hình AI
Mỗi AI tạo ảnh có một thế mạnh riêng, do đó cách chúng ta "nói chuyện" với chúng cũng cần linh hoạt:
- **Midjourney / Leonardo:** Rất nhạy bén với tính nghệ thuật, thẩm mỹ (aesthetics). Chúng thích các từ khóa (keywords) về phong cách nghệ thuật, tên họa sĩ, hoặc thông số máy ảnh cụ thể. 
- **ChatGPT 4o (DALL-E 3) / Google Nano Banana / Imagen:** Hiểu ngữ nghĩa và cấu trúc câu cực kỳ tốt. Bạn có thể viết prompt như đang kể một câu chuyện dài, mô tả chính xác vị trí của từng vật thể (trái/phải/tiền cảnh/hậu cảnh) và AI sẽ tuân thủ nghiêm ngặt.

---

## 2. Công Thức Prompt Chuẩn (The Core Formula)
Thay vì viết một mớ từ khóa lộn xộn, hãy cấu trúc prompt như một đạo diễn đang miêu tả cảnh quay:

> **[Chủ thể] + [Hành động] + [Bối cảnh] + [Góc máy & Bố cục] + [Ánh sáng & Phong cách]**

**Ví dụ:**
- **[Chủ thể]** Một người mẫu thời trang mặc chiếc váy tweed màu xanh navy và bốt da cao cổ.
- **[Hành động]** Đang tạo dáng tự tin, mắt nhìn thẳng ống kính, hơi nghiêng người.
- **[Bối cảnh]** Đứng giữa một studio có phông nền liền mạch (seamless backdrop) màu đỏ mận sẫm.
- **[Góc máy]** Cảnh trung toàn (medium-full shot), chủ thể ở trung tâm.
- **[Ánh sáng & Phong cách]** Ánh sáng cinematic, phong cách ảnh editorial trên tạp chí, chụp bằng phim analog medium-format, nhiễu hạt nhẹ, độ bão hòa màu cao.

---

## 3. Kỹ Thuật "Đạo Diễn Hình Ảnh" (Creative Director Mode)
Để ảnh bớt "giả" (mang hơi hướm AI) và đậm chất chuyên nghiệp, hãy bổ sung các thuật ngữ nhiếp ảnh:

### A. Góc máy & Bố cục (Camera Angles)
- **Low-angle shot:** Chụp từ dưới lên, tạo sự vĩ đại, quyền lực.
- **Aerial / Drone view:** Chụp từ trên không xuống, bao quát không gian.
- **Macro lens:** Cận cảnh siêu chi tiết (giọt nước, kết cấu bề mặt).
- **Wide-angle:** Góc rộng, phô diễn sự rộng lớn của môi trường xung quanh.

### B. Ống kính & Thiết bị (Hardware DNA)
Thay vì chỉ nói "ảnh chụp", hãy chỉ định thiết bị:
- **GoPro:** Tạo hiệu ứng action, méo góc viền, cảm giác nhập vai.
- **Disposable camera / Polaroid:** Ảnh raw, đèn flash gắt, hoài cổ, chân thực.
- **Shallow depth of field (f/1.8):** Xóa phông mù mịt, nổi bật chủ thể.

### C. Ánh sáng (Lighting)
Ánh sáng là linh hồn của bức ảnh:
- **Golden hour:** Ánh sáng mặt trời lúc bình minh/hoàng hôn, ấm áp, bóng đổ dài.
- **Chiaroscuro:** Tương phản sáng tối cực mạnh, kịch tính (phong cách tranh Phục Hưng).
- **Three-point softbox setup:** Ánh sáng studio chuẩn, chiếu sáng đều, thích hợp cho chụp sản phẩm/mockup.
- **Cinematic lighting với muted teal tones:** Ánh sáng điện ảnh với tông màu xanh lam mờ (rất hợp phong cách Cyberpunk hoặc Moody).

### D. Bề mặt & Chất liệu (Materiality)
Đừng dừng lại ở danh từ chung. Thay vì nói "áo khoác", hãy nói "áo khoác len dệt kim sợi to". Thay vì nói "cốc cà phê", hãy dùng "cốc sứ nhám tối giản". Điều này bắt buộc AI phải tính toán và render bề mặt (texture) một cách chân thực nhất.

---

## 4. Các Nguyên Tắc Vàng Khác
1. **Sử dụng ngôn ngữ khẳng định (Positive Framing):** Nói với AI những gì bạn *muốn thấy*, đừng nói những gì bạn *không muốn*.
   - Sai: `Đường phố không có ô tô` (AI có thể vẫn vẽ ô tô vì bị ám ảnh từ khóa).
   - Đúng: `Đường phố hoàn toàn trống vắng, vắng lặng`.
2. **Quy định tỷ lệ khung hình (Aspect Ratio):** Luôn ghi rõ tỷ lệ khung hình bạn muốn ở cuối prompt (VD: `16:9` cho YouTube, `9:16` cho Reels/Shorts, `1:1` cho Instagram). Nếu không, nhiều AI mặc định sẽ xuất ảnh vuông.
3. **Mô tả càng chi tiết càng tốt:** Bất cứ khoảng trống nào bạn không mô tả, AI sẽ tự điền vào (hallucination), và điều đó làm bạn mất đi sự kiểm soát.

---

## 5. Xử Lý Các Tác Vụ Nâng Cao

### Render Text (Chèn chữ vào ảnh)
Rất hiệu quả với ChatGPT 4o, Ideogram, Nano Banana.
- **Nguyên tắc:** Bọc từ cần chèn trong ngoặc kép (VD: `"HELLO WORLD"`).
- **Chỉ định Phông chữ (Font):** Mô tả rõ tính chất của phông chữ.
  - *Ví dụ:* `Một chiếc poster với dòng chữ "NEW YORK" viết bằng font sans-serif in đậm, to màu trắng.`

### Hình ảnh tham chiếu (Image-to-Image / Style Transfer)
Sử dụng ảnh có sẵn làm khuôn mẫu:
- **Biến đổi chất liệu:** Đưa vào một bản phác thảo (sketch) và yêu cầu: *"Dựa vào bức phác thảo này làm cấu trúc, hãy render nó thành một chiếc ghế bành 3D chân thực."*
- **Biến đổi phong cách:** Đưa vào ảnh thật và yêu cầu: *"Chuyển đổi toàn bộ nội dung bức ảnh này sang phong cách tranh sơn dầu của Van Gogh."*

### Inpainting (Sửa chi tiết)
Khi muốn sửa một phần (VD: đổi màu áo, xóa người thừa), hãy mô tả rõ cái cần xóa/thay đổi và **nhấn mạnh việc giữ nguyên phần còn lại**.
- *Ví dụ:* `Thay thế chiếc túi trên bàn thành một lọ hoa hồng đỏ, giữ nguyên hoàn toàn ánh sáng và không gian xung quanh.`

---

## 6. Quy Trình Làm Việc Thực Tế (Iterative Process)
- Hiếm khi có một prompt hoàn hảo ngay lần đầu tiên. Việc tạo ảnh là một quá trình hội thoại và tinh chỉnh liên tục.
- **Lưu ý với ChatGPT 4o:** Các ảnh tạo ra trong cùng một khung chat thường có xu hướng "nhớ" bối cảnh của ảnh trước đó (Consistency). Điều này tốt nếu bạn muốn sửa lỗi nhỏ. Nhưng nếu bức ảnh đã đi chệch hướng quá xa, hoặc bạn muốn sáng tạo cái mới, hãy **mở một cuộc trò chuyện mới** để tránh bị ảnh hưởng bởi dữ liệu cũ.
- Hãy yêu cầu LLM (như GPT, Claude) viết lại hoặc làm phong phú thêm prompt gốc của bạn dựa trên công thức trên trước khi đưa vào AI tạo ảnh. Mẹo: *"Hãy mở rộng ý tưởng 'một con mèo uống cà phê' thành 3 prompt ảnh tiếng Anh cực kỳ chi tiết theo chuẩn nhiếp ảnh cinematic."*
