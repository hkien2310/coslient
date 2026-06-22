# Kiến thức Coslient GPT — Phát triển Prompt Hoạt ảnh v7.0

## Triết lý cốt lõi

VEO 3 đọc ảnh trước khi đọc prompt. Nó đã biết nội dung, ánh sáng, không gian — và tự sinh chuyển động phù hợp với từng ảnh.

**Đa dạng đến từ ảnh, không phải từ prompt.**

---

## Prompt

Dùng **1 prompt ngắn (~8 từ) cố định cho toàn bộ batch.** Chỉ dùng keyword về style/mood — không chỉ định camera, không mô tả chuyển động.

```
surreal cinematic 4K atmospheric
```

```
warm cinematic nostalgic soft 4K
```

```
dramatic editorial cinematic filmic
```

> **Không dùng dấu ngoặc kép `" "` ở bất kỳ đâu** — VEO hiểu là lệnh tạo hội thoại + nhép môi.

---

## Fallback — Khi 1 clip cụ thể ra sai

Chỉ can thiệp khi clip bị VEO xử lý sai rõ ràng. Thêm đúng **1 cụm** vào đầu prompt:

| Triệu chứng | Thêm vào đầu |
|:---|:---|
| Camera bị giật/lắc | `Tripod-stable framing.` |
| Nhân vật bị biến dạng | `Hold source image fidelity, subtle motion only.` |
| Zoom quá nhanh | `Slow gentle motion throughout.` |
| Chuyển động hỗn loạn | `Static or near-static, preserve composition.` |

---

## Quy tắc kỹ thuật

**Độ dài clip:** 8 giây (mặc định).

**Frame bridging:** Khung hình cuối clip A → làm khung hình đầu clip B. Khi đổi hoàn toàn địa điểm: tạo ảnh tĩnh mới làm anchor trước.

**Strip audio** nếu VEO tạo ra âm thanh lạ:
```bash
ffmpeg -i input.mp4 -an output_no_audio.mp4
```

---

## Quy tắc cốt lõi

Ảnh tốt + prompt ngắn + edit theo cảm giác = đủ rồi.
