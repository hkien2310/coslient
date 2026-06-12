# Giai đoạn 5: Phát triển Prompt Hoạt ảnh (VEO 3)

Theo quy tắc V4.0 (AI-inferred motion), bạn không cần các prompt mô tả chuyển động camera hay hành động phức tạp. VEO 3 sẽ tự động đọc hình ảnh và nội suy chuyển động (nhân vật, camera, vật lý môi trường).

**Chỉ copy và dán PROMPT DUY NHẤT này cho TẤT CẢ các clip trong VEO 3:**

```text
Audio: Diegetic environmental sound only — soft ambient sounds natural to this scene. No music. No score. No dialogue. No vocals. No voiceover. If no suitable sound can be generated, output silence rather than music.

No internal glow. No magical particles. No sparkles. No floating light effects. No added visual effects not present in the source image.
```

## Các Quy tắc Bắt buộc:
1. **Không mô tả lại nhân vật hay cảnh** (VEO sẽ tự hiểu).
2. **Không dùng dấu ngoặc kép `" "`** để tránh việc VEO tạo ra giọng nói / nhép môi.
3. Độ dài clip mặc định: **8 giây**.
4. Nối khung hình (Frame bridging): Dùng khung hình cuối của clip trước làm khung hình đầu của clip sau (nếu cùng một không gian/hành động).

## Giao thức Dự phòng (Chỉ dùng khi VEO bị lỗi trên 1 clip cụ thể)
Nếu clip ra bị giật lắc, biến dạng hoặc sai chuyển động, hãy ghép **đúng 1 cụm sửa lỗi** vào **đầu** của prompt duy nhất ở trên:

- **Camera bị giật/lắc:** Thêm `Tripod-stable framing.`
- **Nhân vật bị biến dạng:** Thêm `Hold source image fidelity, subtle motion only.`
- **Cảnh bị zoom quá nhanh:** Thêm `Slow gentle motion throughout.`
- **Chuyển động hỗn loạn:** Thêm `Static or near-static, preserve composition.`

*(Sau khi có toàn bộ video clip, bạn có thể chuyển sang Giai đoạn 6 - SEO)*
