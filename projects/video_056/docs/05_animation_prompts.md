# Animation Prompts (VEO 3) - Video 056

## Triết lý cốt lõi
VEO 3 đọc ảnh trước khi đọc prompt. Đa dạng chuyển động và ánh sáng đến từ chất lượng của 40 ảnh Midjourney đã gen ở Stage 4. Chúng ta chỉ cần cung cấp từ khóa về mood/style. **Tuyệt đối KHÔNG dùng dấu ngoặc kép.**

## Global Prompts theo Batch (Sáng tạo theo cảm xúc)
Để "sáng tạo hơn" như Boss yêu cầu nhưng vẫn tuân thủ đúng luật VEO 3 (1 prompt ngắn cố định cho mỗi batch), em đã thiết kế 4 global prompts khác nhau, tương ứng với biểu đồ cảm xúc của từng giai đoạn trong bài hát:

### Batch 1: Intro & Verse 1 (Sự tĩnh lặng, chậm rãi, cũ kỹ)
`warm cinematic nostalgic soft quiet 4K`

### Batch 2: Chorus 1 & Verse 2 (Bùng nổ, rực rỡ khi chú ngựa xuất hiện)
`radiant cinematic glowing amber energetic 4K`

### Batch 3: Chorus 2 & Bridge (Sự buông bỏ, u sầu nhưng sâu thẳm)
`melancholic cinematic gentle soft profound 4K`

### Batch 4: Final Chorus & Outro (Giải thoát, rộng lớn & tĩnh lặng cuối cùng)
`majestic cinematic bright expansive free 4K`

## Quy tắc Fallback (Xử lý lỗi VEO 3)
Chỉ can thiệp khi VEO 3 phá hỏng bức ảnh gốc. Nếu gặp lỗi, thêm đúng 1 cụm vào **trước** các prompt phía trên:

- **Camera bị giật/lắc:** `Tripod-stable framing.`
- **Nhân vật biến dạng (Morphing):** `Hold source image fidelity, subtle motion only.`
- **Chuyển động quá hỗn loạn:** `Static or near-static, preserve composition.`
- **Zoom quá gắt/chóng mặt:** `Slow gentle motion throughout.`

*Lưu ý kỹ thuật: Độ dài clip mặc định 8s. Khi nối clip chuyển cảnh (ví dụ từ căn phòng ra thung lũng tuyết ở Batch 4), cân nhắc tạo ảnh tĩnh làm anchor. Nếu VEO tự chèn tiếng động lạ, phải mute/strip audio khi edit.*
