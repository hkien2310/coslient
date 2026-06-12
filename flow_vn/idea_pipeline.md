**Tóm tắt tác dụng của file:** File này đóng vai trò là một quy trình quản lý (pipeline) trực tiếp để theo dõi vòng đời của các ý tưởng video, từ lúc là ý tưởng thô (Inbox), đang thực hiện (In Progress), chờ xử lý (Backlog) cho đến khi bị loại bỏ (Cut). Nó được tự động cập nhật bởi Coslient GPT sau mỗi bước tiến độ và hỗ trợ đồng bộ trạng thái với bảng Kanban trên web.

# 🗂️ QUY TRÌNH Ý TƯỞNG (IDEA PIPELINE) — Đang hoạt động
> **Đây là file sống.** Coslient GPT tự cập nhật sau mỗi bước.  
> Sếp không cần sửa tay — chỉ đọc và kéo thẻ Kanban trên web theo đúng trạng thái ở đây.  
> Khi video xuất bản (publish) xong → Coslient chuyển mục này sang `idea_archive.md`, xoá khỏi file này.

---

## 📥 HỘP THƯ ĐẾN (INBOX) — Ý tưởng thô chưa đánh giá

> Đây là nơi dán danh sách ý tưởng từ web vào. Coslient sẽ đánh giá (evaluate) và chuyển xuống ĐANG LÀM (IN PROGRESS).

<!-- DÁN Ý TƯỞNG TỪ WEB VÀO ĐÂY -->
<!-- Định dạng mỗi dòng: - [nội dung ý tưởng] | ngày thêm: YYYY-MM-DD -->

*(Trống — đang chờ ý tưởng mới từ web)*

---

## 🔄 ĐANG LÀM (IN PROGRESS) — Đang tiến hành

> Mỗi ý tưởng đã được chọn và đang đi qua các bước sản xuất (production).

<!--
THỨ TỰ GIAI ĐOẠN: inbox → brainstorm → selected → concept → research → song → image → animation → seo → published
ÁNH XẠ KANBAN:
  inbox/brainstorm/selected → cột "Ideas" trên web
  concept/research          → cột "Scripting" trên web  
  song/image/animation      → cột "Production" trên web
  seo                       → cột "Ready" trên web
  published                 → cột "Published" trên web (rồi archive)
-->

| ID | Tiêu đề | Giai đoạn | Ghi chú | Đã cập nhật |
|---|---|---|---|---|
| v052 | The Ocean Keepers (Những Người Canh Giữ Đại Dương) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |
| v053 | The Unplayed Song (Bài Hát Chưa Từng Được Phát) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |
| v054 | The Train to the Light (Chuyến Tàu Đến Ánh Sáng) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |
| v055 | The Time Machine of Scents (Cỗ Máy Thời Gian Của Những Mùi Hương) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |
| v056 | The Wild Horse in the Quiet Room (Chú Ngựa Hoang Trong Căn Phòng Tĩnh Lặng) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |
| v057 | The Pecan Tree's Legacy (Di Sản Của Cây Hồ Đào) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |
| v058 | The Biscuit Tin (Hộp Bánh Quy) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |
| v059 | Last Summer Together (Mùa Hè Cuối Cùng Bên Nhau) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |
| v060 | The Message in the Margin (Lời Nhắn Cạnh Lề) | `song` | Có lời bài hát + nhạc. Chưa có câu lệnh tạo ảnh (image prompts) | 2026-06-10 |

---

## 📋 TỒN ĐỌNG (BACKLOG) — Đã đánh giá, chờ làm

> Ý tưởng đã qua Giai đoạn 1 (nhãn MẠNH - STRONG), chờ được kéo vào khâu sản xuất.

| ID | Tiêu đề / Ý tưởng | Điểm số | Ghi chú | Đã thêm |
|---|---|---|---|---|
| — | — | — | *Chưa có ý tưởng trong danh sách tồn đọng* | — |

---

## ❌ LOẠI BỎ (CUT) — Đã loại

> Ý tưởng đã được đánh giá và loại bỏ. Giữ lại để không mất công lên ý tưởng (brainstorm) lại.  
> **Không xoá.** Dùng để tránh lặp lại những ý tưởng dở.

| Ý tưởng | Lý do loại | Ngày |
|---|---|---|
| — | — | — |

---

## 📝 HƯỚNG DẪN — Coslient GPT

### Khi Sếp dán danh sách ý tưởng từ web:
1. Chuyển tất cả ý tưởng vào phần HỘP THƯ ĐẾN (INBOX) với định dạng chuẩn
2. Chạy đánh giá (Giai đoạn 1) cho từng ý tưởng
3. Gắn nhãn MẠNH (STRONG) → chuyển sang TỒN ĐỌNG (BACKLOG), ĐỊNH HÌNH LẠI (RESHAPE) → ghi chú, LOẠI BỎ (CUT) → chuyển sang LOẠI BỎ (CUT)
4. Báo cáo kết quả cho Sếp

### Khi Sếp chọn 1 ý tưởng để làm:
1. Chuyển từ TỒN ĐỌNG (BACKLOG) vào ĐANG LÀM (IN PROGRESS)
2. Gán ID: `v[số video tiếp theo]` (xem file `concept_index.md` để biết số tiếp theo)
3. Giai đoạn bắt đầu: `concept`
4. Cập nhật cột `Đã cập nhật` sau mỗi bước

### Sau mỗi bước sản xuất (production):
Cập nhật cột `Giai đoạn` theo thứ tự:
`concept → research → song → image → animation → seo → published`

### Khi video được xuất bản (published):
1. Sao chép toàn bộ hàng sang `idea_archive.md`
2. Xoá hàng khỏi phần ĐANG LÀM (IN PROGRESS) ở file này
3. Cập nhật `concept_index.md` (thêm mục mới)

### Quy trình đồng bộ Web:
```
WEB → COSLIENT:  Sếp sao chép các ý tưởng từ cột Kanban "Ideas" → dán vào phần HỘP THƯ ĐẾN (INBOX)
COSLIENT → WEB:  Sếp đọc giai đoạn ở ĐANG LÀM (IN PROGRESS) → kéo tay thẻ trên web Kanban cho khớp
```

---

*Cập nhật lần cuối: 2026-06-10*
