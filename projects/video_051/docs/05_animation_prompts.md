# Video 051 — Animation Prompts (VEO 3)

STAGE: Animation Generation
STATUS: ready

## QUY TẮC BẮT BUỘC (VEO 3)
1. **Không mô tả lại nhân vật/bối cảnh:** VEO 3 dùng chế độ Image-to-Video, nó đã nhìn thấy ảnh gốc. Nhồi thêm chi tiết hình ảnh vào prompt sẽ làm video bị vỡ nát hoặc thay đổi khuôn mặt.
2. **Audio là Physics Anchor:** Đừng tắt Audio. Các từ khóa âm thanh như "ocean waves", "crackling fire" giúp VEO hiểu vật lý của nước và lửa để animate cho đúng. Sau khi tải về mới dùng phần mềm dựng phim để tắt tiếng.
3. **Clip Length:** 8 giây mặc định.

---

## 1. UNIVERSAL PROMPT (DÙNG CHO 90% CÁC CLIP)
> Dán nguyên văn đoạn này vào VEO 3 cho tất cả các bức ảnh rộng, cảnh toàn, và cảnh nhân vật đứng im/đi bộ chậm. Không cần sửa chữ nào.

```text
Slow, steady cinematic push-in, smooth and tripod-stable. Soft natural ambient motion in the scene — fabric, hair, ocean water, or fire responding gently to air. Cold indigo coastal dawn, muted sea-glass greys, rich warm amber morning light, lifted soft shadows. Shot on 35mm film, vintage celluloid film aesthetic, cinematic hazy atmosphere, preserve handcrafted storybook miniature style and smooth claymation feel, fine natural grain, soft halation around highlights, shallow depth of field. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — soft ambient sounds natural to this coastal morning scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.
```

---

## 2. FALLBACK PROMPTS (CỨU HỘ CHO CÁC CLIP KHÓ)
Chỉ dùng các prompt dưới đây nếu chạy Universal Prompt bị hỏng (ví dụ: bị biến dạng mặt, nước chảy ngược, hoặc lửa cháy sai vật lý).

### Fallback A: Dành cho Cận Cảnh Khuôn Mặt (Chống biến dạng)
```text
Static medium shot, hold still, subtle micro-movements, preserve facial expression and posture exactly as in source image. Figure sits quietly, slight natural breathing motion, hands still, eyes blinking softly. Cold indigo coastal dawn, rich warm amber morning light, lifted soft shadows. Shot on 35mm film, vintage celluloid film aesthetic, preserve handcrafted storybook miniature style and smooth claymation feel, fine natural grain. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — distant ocean waves, gentle morning breeze. No music. No score. No dialogue. No vocals. If no suitable sound can be generated, output silence rather than music.
```

### Fallback B: Dành cho Sóng Biển & Bàn Chân Chạm Nước (Ưu tiên vật lý chất lỏng)
```text
Slow gentle tilt down, tripod-stable. Fluid, realistic natural ambient motion — ocean waves rolling gently onto the wet sand, water reflecting the sky. Cold indigo coastal dawn, muted sea-glass greys, rich warm amber morning light, lifted soft shadows. Shot on 35mm film, vintage celluloid film aesthetic, cinematic hazy atmosphere, preserve handcrafted storybook miniature style, fine natural grain, shallow depth of field. Serene, peaceful mood.

Audio: Diegetic environmental sound only — rhythmic ocean waves crashing softly, water washing over wet sand. No music. No score. No dialogue. No vocals. If no suitable sound can be generated, output silence rather than music.
```

### Fallback C: Dành cho Bếp Lửa Lão Ngư & Các Đồ Vật Nhỏ (Macro)
```text
Static macro close-up, extreme shallow depth of field. Natural ambient motion only — gentle fire flickering, sparks rising slowly, or steam curling gently into the cold air. Rich warm amber morning light, lifted soft shadows. Shot on 35mm film, vintage celluloid film aesthetic, preserve handcrafted storybook miniature style and smooth claymation feel, fine natural grain, soft halation around glowing highlights. Serene, intimate, contemplative mood.

Audio: Diegetic environmental sound only — dry wood crackling softly, quiet beach ambient. No music. No score. No dialogue. No vocals. If no suitable sound can be generated, output silence rather than music.
```

---
**NEXT STEP:** 
Giai đoạn sản xuất hình/chuyển động coi như đã có bộ khung đầy đủ. Boss có thể tiến hành render VEO 3/Runway Gen 3. 
Trong thời gian đó, Boss có muốn em chạy **Stage 6: Lên bộ Tiêu đề, Mô tả và Chiến lược SEO YouTube** cho Video 051 này không?
