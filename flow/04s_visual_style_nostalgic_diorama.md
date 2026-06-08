# Visual Style Module: Nostalgic Diorama
> **Style ID:** `nostalgic_diorama`
> **Status:** 🔵 Available Option
> **Version:** 1.0
> **Dùng cho:** Các video mang tính tự sự, ngụ ngôn, cổ tích, hoặc những câu chuyện chứa đựng sự hoài niệm, u buồn man mác, tình cảm gia đình. Đây là phong cách đối lập hoàn toàn với sự "vô trùng" của Neo-Pop.

---

## Cách sử dụng file này

File này chứa toàn bộ DNA thị giác cho phong cách **Nostalgic Diorama** (Sa bàn Hoài niệm / Hoạt hình tĩnh vật). Agent đọc file này tại Stage 4.1 để load phong cách hình ảnh.

**Triết lý cốt lõi:** Đưa người xem vào một thế giới thu nhỏ (miniature world) được chế tác hoàn toàn thủ công (hand-crafted). Mọi thứ trong khung hình đều nhuốm màu thời gian, cũ kỹ, bám bụi, và mang tính xúc giác (tactile) cực kỳ cao — khiến người xem có cảm giác muốn vươn tay ra chạm vào. 

---

## 1. Style Identity & Feel

### Tên phong cách
**Nostalgic Diorama** (Hoạt hình Stop-Motion / Sa bàn thủ công)

### DNA cốt lõi (không thay đổi theo video)
- **Macro Photography (Hiệu ứng Sa bàn):** Góc máy mô phỏng việc quay chụp các mô hình nhỏ xíu. Độ sâu trường ảnh cực kỳ nông (Shallow Depth of Field), tạo ra Heavy Bokeh. Chỉ lấy nét vào một vật thể/nhân vật, mọi thứ ở xa hay quá gần đều bị làm mờ mù mịt.
- **Nghệ thuật của sự già cỗi (The Art of Weathering):** KHÔNG có cái gì là "mới". Mọi bề mặt đều sần sùi, nứt nẻ, mục nát, rỉ sét, hoặc bị rêu phong tàn phá.
- **Chất liệu thủ công (Tactile Textures):** Nhân vật và đồ vật trông như được nặn từ đất sét (clay), chạm khắc từ gỗ, hoặc may bằng vải nỉ/len (felt/yarn).
- **Ánh sáng thể tích & Bụi (Volumetric Light & Dust):** Không gian luôn lơ lửng những hạt bụi li ti được chiếu sáng bởi các tia nắng hắt qua cửa sổ (God rays) hoặc ánh sáng hoàng hôn.
- **Tỷ lệ cường điệu (Exaggerated Proportions):** Tay chân khẳng khiu như que củi, bàn tay to nhăn nheo, mũi to, đầu to. Phong cách đặc sệt của Laika Studios (Coraline) hoặc Tim Burton.

### Hình ảnh nên cảm nhận như:
- extremely tactile, hand-crafted miniature diorama
- nostalgic, rustic, cozy but melancholic
- heavily textured, weathered, and aged
- cinematic macro photography with shallow focus
- stop-motion puppet animation / claymation

### Hình ảnh KHÔNG được cảm nhận như:
- pristine, flawless, smooth, ultra-clean 3D
- flat lighting, bright colorful pop-art
- modern, futuristic, or technologically advanced
- perfectly proportioned realistic humans

---

## 2. Style Anchors

### Full style anchor (dùng cho prompt > 500 ký tự)
```
nostalgic stop-motion animation style, [SUBJECT], miniature diorama, extremely tactile hand-crafted textures, weathered and aged surfaces, macro photography with shallow depth of field, heavy bokeh, earthy muted color palette, floating dust motes, warm cinematic golden hour lighting, spindly exaggerated character proportions, Laika studios claymation aesthetic, highly detailed rustic environment
```

### Short style anchor (dùng cho prompt ngắn hơn)
```
nostalgic stop-motion diorama, tactile hand-crafted textures, weathered rustic environment, macro photography, shallow depth of field, earthy muted colors, floating dust, cinematic lighting
```

### Negative style anchor (dùng khi model bị drift)
```
pristine, smooth plastic, ultra-clean, flat lighting, neon colors, modern, perfect realism, glossy, digital 3D render, perfectly proportioned humans, sterile environment
```

### Style Intensity (3 mức độ)

| Mức độ | Khi nào dùng | Áp dụng |
|:---|:---|:---|
| **Subtle** | Cần không gian thực tế nhưng hơi hoài cổ | Chỉ dùng Earthy Tones + Cinematic Lighting + Shallow Depth of Field. |
| **Standard** | Mặc định | Full style anchor + Weathered textures + Stop-motion aesthetic. |
| **Maximum** | Nhấn mạnh độ chi tiết vật lý | Đẩy mạnh Macro Photography focus + Extreme textures (rỉ sét, vân gỗ nứt, nếp nhăn sâu) + Tỷ lệ nhân vật dị dạng (tay chân que củi). |

---

## 3. Style Migration Notes

Dịch mã từ kịch bản thường sang ngôn ngữ "Sa bàn thủ công":

| ❌ Tránh (Sạch sẽ/Hiện đại) | ✅ Thay bằng (Nostalgic Diorama) |
|:---|:---|
| Quần áo phẳng phiu, vải silk | Áo len đan móc thô (chunky knit), vải tweed xù lông, da sờn |
| Căn phòng gọn gàng, trống trải | Căn phòng bừa bộn đồ đạc lặt vặt (cluttered), bám bụi |
| Da dẻ mịn màng, hoàn hảo | Da nhăn nheo thô ráp như đất sét nặn, gân guốc |
| Tóc suôn mượt bay trong gió | Tóc làm bằng các cuộn len (yarn), cước, xơ xác |
| Nền màu trơn, vô trùng | Bối cảnh rêu phong, lá rụng, gạch vỡ, cỏ dại |

---

## 4. Character Design (Style-Specific)

### Nguyên tắc MỞ — Character Treatment Rules
- **Thần thái:** Có hồn, mang tính kể chuyện cao. Ánh mắt thường ánh lên sự suy tư, mệt mỏi, hoặc hiền từ. Biểu cảm có chiều sâu.
- **Tỷ lệ (Proportions):** Phải cường điệu hóa. Tay chân dài ngoẵng gầy guộc (spindly limbs), đầu to, mũi quá khổ. Bàn tay rất to với các đốt ngón tay rõ rệt.
- **Trang phục:** Trang phục mang hơi hướng nông thôn, cổ điển (Rustic/Vintage). Áo sơ mi kẻ sọc phai màu, quần yếm vải thô, áo len đan sợi to, giày da sờn gót. 

### Rendering Lock
`[Nhân vật] with expressive eyes and exaggerated spindly proportions, made of tactile claymation textures, wearing deeply textured weathered [Trang phục], deeply wrinkled skin, yarn-like messy hair`

---

## 5. Material Palette

Sự bùng nổ của chất liệu thực tế:
- **Nhân vật:** Đất sét (clay), nhựa thông (resin) được sơn phết bằng tay, tóc bằng len (yarn/wool).
- **Môi trường:** Gỗ sồi mục nát (weathered wood), sắt rỉ sét (rusted iron), đá ong sần sùi (rough stone), cỏ khô, rêu phong, lá úa.
- **Vải vóc:** Vải nỉ (felt), len thô (chunky knit), vải tweed, bạt canvas.

---

## 6. Color DNA

### Nguyên tắc màu sắc
**Quy tắc vàng:** Sử dụng **Muted Earthy Tones (Bảng màu đất trầm)**. Mọi màu sắc đều như bị phai đi theo thời gian, giảm độ bão hòa (desaturated).

### Bảng màu đặc trưng
- Nâu gỗ (Wood brown), Nâu gỉ sét (Rusted red/Rust).
- Vàng rơm (Straw yellow), Vàng mù tạt nhạt.
- Xanh rêu (Olive green), Xanh xám.
- Xanh dương phai (Faded denim blue).

### Tránh:
- Các màu neon rực rỡ, màu pastel tươi sáng (như hồng phấn, xanh mint gắt).
- Màu trắng tinh (chỉ dùng màu ngà/ivory hoặc ố vàng).

---

## 7. Lighting DNA

### Nguyên tắc cốt lõi
Ánh sáng là công cụ kể chuyện chính, tạo ra sự ấm áp và u buồn.

- **Cinematic Golden Hour:** Ánh sáng mặt trời chiếu xiên ở góc thấp, tạo ra màu vàng cam ấm áp và bóng đổ dài.
- **Volumetric Light & Dust:** Luôn có luồng sáng (God rays) chiếu qua cửa sổ hoặc kẽ lá, làm nổi bật những hạt bụi li ti lơ lửng trong không khí.
- **High Contrast (Tương phản cao):** Vùng sáng cực ấm, vùng tối sâu và mang màu xanh lạnh chìm (teal/blue shadows) tạo chiều sâu.

### Từ khoá lighting cho prompt:
`warm cinematic golden hour lighting, volumetric light rays shining through dust motes, moody atmosphere, deep shadows`

---

## 8. Focal Point Doctrine (Học thuyết Điểm Nổi Bật)

- **Macro Focus:** Dùng kỹ thuật lấy nét cực mỏng (Shallow depth of field). Nếu chụp tay, chỉ lấy nét ở các đốt ngón tay và vân gỗ trên mặt bàn. Nếu chụp toàn cảnh, chỉ lấy nét vào nhân vật, xóa phông mờ mịt tiền cảnh (tiền cảnh có thể là vài cành lá rủ xuống).
- **Guiding Light:** Dùng vệt sáng (God ray) chiếu thẳng vào khuôn mặt hoặc vật thể quan trọng để thu hút ánh nhìn trong một khung cảnh tối tăm, bừa bộn.

---

## 9. World Logic

- **Thế giới bừa bộn nhưng ấm cúng (Cluttered coziness):** Bối cảnh thường chật chội, chứa đầy các tiểu tiết mô hình (những chiếc đồng hồ cũ, đồ nghề ngổn ngang, chai lọ).
- **Thiên nhiên xâm lấn:** Cây cỏ mọc len lỏi vào các công trình nhân tạo. Rêu, dây leo bao phủ tường đá. Rất nhiều lá rụng trên mặt đất.

---

## 10. Prompt Templates (Style-Specific)

### Dynamic template chuẩn hóa
```
Macro photography, shallow depth of field, [Cỡ cảnh: Close-up / Wide shot], [SUBJECT] with exaggerated spindly proportions and deep wrinkles, [Hành động], nostalgic stop-motion animation style, miniature diorama, wearing highly textured weathered [Trang phục], standing in a cluttered rustic [Bối cảnh], highly tactile materials, weathered and aged surfaces, earthy muted color palette, warm cinematic golden hour lighting, volumetric light rays highlighting floating dust motes, heavy bokeh, Laika claymation aesthetic, 16:9
```

---

## 11. Words to Prefer / Avoid

### Dùng nhiều
stop-motion, miniature diorama, macro photography, shallow depth of field, heavy bokeh, tactile, hand-crafted, weathered, rusted, wrinkled, overgrown, clutter, spindly limbs, claymation, earthy tones, golden hour, floating dust motes, nostalgic, rustic.

### Tránh hoặc dùng rất ít
pristine, clean, smooth, flawless, neon, flat lighting, digital render, modern, symmetrical void, sterile, fast motion.

---

## 12. Revision Behavior (Style-Specific)

| Boss nói | Sửa |
| :--- | :--- |
| **Nhìn quá ảo, giống 3D máy tính** | Nhồi thêm cụm `stop-motion puppet, claymation, hand-crafted tactile materials, yarn hair`. Tăng cụm `macro photography, shallow depth of field` để ép nó ra hiệu ứng chụp mô hình. |
| **Ảnh bị trơn láng, sạch sẽ quá** | Bơm thêm `heavily weathered, rusted, chipped paint, deeply wrinkled, dirt, floating dust motes`. Dùng Negative: `pristine, smooth, clean`. |
| **Màu sắc bị tươi rực rỡ quá** | Thêm cụm `muted earthy tones, desaturated colors, rustic aesthetic`. |
| **Mất cảm giác "sa bàn/diorama"** | Bắt buộc phải có `heavy bokeh, extreme shallow depth of field`. Cho thêm vài vật thể làm tiền cảnh bị mờ nhòe (blurred foreground elements). |

---
