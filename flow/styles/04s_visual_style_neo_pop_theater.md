# Visual Style Module: Neo-Pop Theater
> **Style ID:** `neo_pop_theater`
> **Status:** 🔵 Available Option
> **Version:** 2.1 (Generalized & Video Consistency Lock)
> **Dùng cho:** Bất kỳ video siêu thực nào mang tính trình diễn nghệ thuật, yêu cầu sự hoàn mỹ, sạch sẽ, màu sắc bắt mắt (color-blocking) và mang đậm tính hình học, hài hước ngầm (quirky). Thích hợp để "sân khấu hóa" các cốt truyện mang tính chất thời trang, trừu tượng. Tuyệt đối không dùng cho bối cảnh thực tế bụi bặm.

---

## Cách sử dụng file này

File này chứa toàn bộ DNA thị giác cho phong cách **Neo-Pop Theater** (Sân khấu Pop-Art Tân thời). Agent đọc file này tại Stage 4.1 để load phong cách hình ảnh.

**Triết lý cốt lõi:** Biến toàn bộ video thành MỘT sân khấu nghệ thuật trình diễn (Performance Art) duy nhất. Bối cảnh bị tước bỏ mọi chi tiết thực tế, chỉ giữ lại một "bức tường" màu trơn tĩnh lặng (Solid Color Void). Sự siêu thực đến từ việc sắp đặt hình học, sự đồng bộ tuyệt đối giữa các cảnh quay, và sự phi lý có chủ đích.

---

## 1. Style Identity & Feel

### Tên phong cách
**Neo-Pop Theater** (Sân khấu Pop-Art Tân thời / Clean Quirky)

### DNA cốt lõi (không thay đổi theo video)
- **Luật Đồng Nhất Tuyệt Đối (Video Consistency Lock):** Sự "lạ" của phong cách này đến từ việc duy trì một bối cảnh tĩnh xuyên suốt. **Màu nền (Background Color) phải cố định 100% từ đầu đến cuối video.** (Ví dụ: Đã chọn nền màu Xanh Mint ở cảnh 1 thì toàn bộ video phải là phông nền Xanh Mint).
- **Sạch sẽ tuyệt đối (Pristine Clean):** Bề mặt cực mịn, ánh sáng hoàn hảo. TUYỆT ĐỐI KHÔNG có nhiễu hạt (film grain), xước, bụi, hay filter camera cũ. Mọi thứ sắc nét như đồ họa 3D render cao cấp.
- **Hình học hóa (Geometric Obsession):** Mọi thứ đều quy về hình khối cơ bản. Quần áo có họa tiết lặp lại (kẻ sọc, chấm bi, caro). Phụ kiện được phóng to mang tính hình học (hình tròn, khối cầu).
- **Tương phản khối màu (Color Blocking):** Trang phục phối những mảng màu nóng/nổi bật, đối lập gay gắt với một phông nền tĩnh lặng.
- **Bố cục đối xứng tuyệt đối (Symmetry):** Giống như phim của Wes Anderson, khung hình canh chính diện (dead-center), hai bên cân bằng.

### Hình ảnh nên cảm nhận như:
- pristine, flawless 3D/editorial quality
- visually striking pop-art minimalism
- quirky, theatrical, and performative
- symmetrical and meticulously arranged
- avant-garde fashion and retro-futuristic shapes

### Hình ảnh KHÔNG được cảm nhận như:
- grainy, vintage, retro camera effects, film dust
- realistic natural environments (no trees, streets, messy rooms)
- cluttered backgrounds

---

## 2. Style Anchors

### Full style anchor (dùng cho prompt > 500 ký tự)
```
vibrant neo-pop theater style, [SUBJECT] wearing avant-garde oversized couture with bold geometric patterns, giant signature geometric accessories, synchronized quirky movement, standing in dead-center of frame, perfectly symmetrical composition, pristine flat solid [BACKGROUND COLOR] background, bright soft studio lighting, crisp and flawless textures, hyper-detailed pop-surrealism editorial, 16:9, absolute zero film grain, pristine clean, avoid noisy retro filter, avoid messy clutter
```

### Short style anchor (dùng cho prompt ngắn hơn)
```
symmetrical neo-pop theater, avant-garde fashion, bold color-blocking, oversized geometric accessories, pristine solid [BACKGROUND COLOR] background, crisp soft lighting, flawless texture, zero grain, 16:9
```

### Negative style anchor (dùng khi model bị drift)
```
children, kids, film grain, noise, vintage filter, retro camera damage, dirt, dust, messy realistic background, casual clothes, smiling, natural expressive faces, asymmetrical, gloomy heavy shadows, realistic landscape, cluttered details
```

---

## 3. Character Design (Style-Specific)

### Quy tắc CHỌN MẶT GỬI VÀNG (Faces & Identities Lock)
Để tạo ra sự siêu thực và cảm giác "trình diễn nghệ thuật", biểu cảm con người thông thường bị loại bỏ. Tùy thuộc vào kịch bản của từng Video, hãy **CHỌN ĐÚNG 1 LOẠI NHÂN VẬT DƯỚI ĐÂY** và áp dụng xuyên suốt từ đầu đến cuối video:

1. **Deadpan Human (Mặt lạnh vô cảm):** Mắt mở to nhìn thẳng ống kính, cơ mặt hoàn toàn tê liệt, không biểu lộ cảm xúc dù đang làm hành động kỳ quặc.
2. **Masked/Obscured (Giấu mặt / Mặt nạ):** Khuôn mặt bị che kín hoàn toàn một cách đầy tính nghệ thuật (ví dụ: đội một bông hoa khổng lồ che kín đầu, mặt nạ chấm bi che kín mặt, đeo khăn voan lưới che mặt).
3. **Surreal / Non-human (Siêu thực / Không phải người):** Người ngoài hành tinh, mannequin, robot có hình dáng người nhưng nước da dị thường (trắng bệch, sơn màu, hoặc trong suốt).

### Đặc điểm CẤM (áp dụng mọi nhân vật)
- **CẤM TRẺ EM (No Children / No Kids):** Phong cách này yêu cầu sự kiểm soát cơ thể và tỷ lệ thời trang của người trưởng thành. Không sử dụng trẻ em.
- Không có biểu cảm tự nhiên (Cấm cười đùa, tức giận, buồn bã bộc lộ ra mặt).
- Cấm quần áo thường ngày ôm sát (phải dùng Avant-Garde Oversized).

---

## 4. Material Palette & Lighting DNA

- **Trang phục:** Len đan sợi to (chunky knit), nỉ cứng giữ form (structured wool), lanh thô dệt. Phụ kiện làm từ nhựa đúc khối (molded plastic), nhựa resin trơn bóng.
- **Background (Void Stage):** Bề mặt phẳng lì tuyệt đối không có texture hạt/grain.
- **Soft Studio Lighting:** Ánh sáng tản đều, phẳng nhưng vẫn giữ được khối. Bóng đổ cực kỳ nhạt (lifted shadows) để phông nền luôn sạch sẽ. Không có nhiễu (noise) trong vùng tối.

---

## 5. Color DNA & Consistency

### LUẬT ĐỒNG NHẤT MÀU SẮC (Video-level Consistency)
- **Background Color:** Phải được chốt ở cảnh đầu tiên và **KHÔNG THAY ĐỔI** trong toàn bộ các shot tiếp theo của video đó. Bức tường nền đó chính là sân khấu cố định.
- **Color Blocking:** Trang phục dùng màu nổi bật đối lập với màu nền. Nên lặp lại một bảng màu nhất định cho quần áo xuyên suốt video để tạo tính "đồng phục" (Uniformity).

---

## 6. Surreal Devices Library (Neo-Pop specific)

Sự siêu thực ở đây cần phong phú, không chỉ là "to nhỏ". Dưới đây là các phương pháp tạo sự siêu thực mang tính nghệ thuật Pop-Art:

1. **2D Graphic Intrusion (Đồ họa 2D xâm nhập 3D):** Các khối hình học phẳng (Flat shapes) trôi lơ lửng trong không gian 3D một cách vô lý.
   *Ví dụ:* `a massive perfectly flat solid orange circle hovering behind the characters`
2. **Material Illusion / Camouflage (Ảo giác chất liệu):** Đồ vật hoặc cơ thể hòa quyện một cách phi lý.
   *Ví dụ:* Khuôn mặt nhân vật được sơn cùng họa tiết caro đen trắng y hệt như áo khoác đang mặc. Bông hoa khổng lồ mọc ra thay cho phần đầu. 
3. **Absurd Interaction (Tương tác vô nghĩa/Phi lý):** Nhân vật làm hành động không hợp logic vật lý hoặc logic đời sống bằng một thái độ cực kỳ nghiêm túc.
   *Ví dụ:* Dắt một khối lập phương đi dạo bằng dây xích chó, hay dùng búa đập vào một đám mây nhựa.
4. **Prop Hyper-scaling (Đạo cụ sai tỷ lệ):** Đồ vật thường ngày bị biến dạng kích thước cực đại và bị tối giản hóa thành hình khối.
   *Ví dụ:* Cái túi xách hình quả trứng ốp la siêu to, cây đàn Cello khổng lồ mang màu pastel.

---

## 7. Focal Point & World Logic

- **Bối cảnh là một Căn phòng/Sân khấu đóng:** Không có bầu trời thực sự, không mây, không có mặt trời. Không có gió tạt mạnh (chỉ có gió nhẹ làm bay áo nếu cần). Mọi thứ tĩnh lặng tuyệt đối để nhường chỗ cho chuyển động cơ thể nhân vật.
- **Symmetry & Repetition:** Đặt chủ thể ở ngay chính giữa. Nhân bản nhân vật (Hai người mặc đồ giống nhau nhưng ngược màu, làm cùng một động tác).

---

## 8. Prompt Templates (Style-Specific)

### Dynamic template chuẩn hóa
```
Wide symmetrical shot, [Số lượng nhân vật trưởng thành], [Chọn 1: deadpan stoic expressions / wearing artistic geometric masks], [Hành động/Tạo dáng], vibrant neo-pop theater style, wearing avant-garde oversized [Loại trang phục] featuring bold [Họa tiết caro/sọc], wearing giant signature [Hình khối] accessories, standing against a pristine seamless flat [CỐ ĐỊNH 1 BACKGROUND COLOR] solid color background, [Surreal Device từ Thư viện], bright soft studio lighting, flawless pristine texture, hyper-detailed pop-art editorial, 16:9, absolute zero film grain, avoid messy background, no children
```

---

## 9. Revision Behavior (Style-Specific)

| Boss nói | Sửa |
| :--- | :--- |
| **Video bị nhảy màu nền liên tục** | Ép cứng `[Background Color]` giống hệt nhau cho mọi câu prompt trong video đó. Khóa góc máy (Static camera). |
| **Nhân vật không đúng "Vibe" / Dính trẻ em** | Thêm cường độ negative prompt `NO children, NO kids`. Bắt buộc gài keyword: `deadpan stoic expression, motionless face, quirky performative stance` HOẶC `face entirely obscured by geometric mask`. |
| **Siêu thực còn nghèo nàn** | Áp dụng 1 trong 4 quy tắc ở Section 6. Ví dụ thêm: `holding a surreal impossible oversized object` hoặc `massive flat geometric shape hovering`. |
| **Ảnh dính hạt/grain giống phim cũ** | Tăng cụm `pristine, flawless, ultra-clean, 3D smooth texture`. |
