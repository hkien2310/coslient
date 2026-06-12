
# Kiến thức Coslient GPT - Kiểm tra A/B Tiêu đề & Hình thu nhỏ (Sau khi xuất bản)

## Mục đích
Tệp này định nghĩa quy trình kiểm tra và tối ưu tiêu đề/hình thu nhỏ **sau khi xuất bản (publish)** dựa trên dữ liệu thực tế từ YouTube Studio. Đây không phải là SEO một lần — đây là vòng lặp cải thiện liên tục dựa trên tín hiệu thật, không phải phỏng đoán.

Giai đoạn 6 chỉ là điểm bắt đầu. Tệp này là bước tiếp theo.

## Khi nào sử dụng
Kích hoạt **48–72 giờ sau mỗi lần xuất bản**. Boss mở YouTube Studio, chia sẻ số CTR và AVD, Coslient đọc dữ liệu và đề xuất hành động tiếp theo (hoặc không làm gì).

## Quy tắc Một Biến số (The One Variable Rule)

**Chỉ kiểm tra (test) 1 biến số tại một thời điểm.**

Không thay đổi tiêu đề VÀ hình thu nhỏ cùng lúc. Nếu thay cả hai, sẽ không biết cái nào gây ra sự thay đổi — mọi bài học rút ra đều vô nghĩa.

- Nếu quyết định test: chọn tiêu đề HOẶC hình thu nhỏ, không phải cả hai.
- Đợi ít nhất 7 ngày để có đủ dữ liệu trước khi đánh giá kết quả.
- Chỉ test 1 video tại một thời điểm — không chạy 3 video test song song.

## Định dạng Giả thuyết (Hypothesis Format)

Trước khi thay đổi bất cứ thứ gì, hãy viết giả thuyết ra. Không có giả thuyết → không thay đổi.

```
GIẢ THUYẾT:
Bởi vì [quan sát từ dữ liệu],
Tôi tin rằng việc thay đổi [tiêu đề HOẶC hình thu nhỏ — chọn một]
từ [phiên bản hiện tại]
thành [phiên bản mới]
sẽ làm tăng [CTR hoặc AVD]
bởi vì [lý do tâm lý].
Tôi sẽ biết điều đó hiệu quả nếu [chỉ số] cải thiện sau hơn 5 ngày.
```

**Ví dụ thực tế:**

```
GIẢ THUYẾT:
Bởi vì CTR là 2.1% (dưới mức chuẩn của thị trường ngách),
Tôi tin rằng việc thay đổi tiêu đề
từ "The Blue Cup | A Warm Song for Still Evenings"
thành "She Still Sets Two Cups Every Morning — A Warm Song | Coslient (4K)"
sẽ làm tăng CTR
bởi vì tiêu đề mới có điểm nhấn kể chuyện (tình huống cụ thể)
thay vì chỉ là một nhãn mô tả.
Tôi sẽ biết điều đó hiệu quả nếu CTR vượt mốc 3.5% sau 7 ngày.
```

## Các mốc chuẩn CTR trên YouTube — Ngách của Coslient

Thị trường ngách (Niche): video ca nhạc cảm xúc, khán giả 45+ tuổi, thiên về duyệt tự do (người xem không chủ động tìm kiếm — YouTube tự đề xuất).

| CTR | Đánh giá | Hành động |
|-----|----------|-----------|
| Dưới 2% | Tiêu đề hoặc hình thu nhỏ không kết nối — cần thay đổi | Test tiêu đề trước |
| 2–3.5% | Trung bình — có tiềm năng nhưng còn cải thiện được | Tùy chọn test, hoặc chờ thêm 2 tuần |
| 3.5–5% | Tốt — thuật toán đang quảng bá đúng | Không thay gì |
| 5%+ | Mạnh — bảo vệ mức này | Tuyệt đối không đụng vào |

## Các mốc chuẩn AVD trên YouTube — Video nhạc 3–5 phút

| AVD | Đánh giá | Hành động |
|-----|----------|-----------|
| Dưới 40% | Phần mở đầu (hook) thất bại hoặc nội dung lỗi — người xem bỏ sớm | Xem xét lại hook ở đầu video |
| 40–55% | Chấp nhận được đối với định dạng nhạc | Theo dõi, không cần hành động gấp |
| 55–70% | Tốt — âm nhạc và hình ảnh đang giữ chân tốt | Quảng bá video này nhiều hơn |
| 70%+ | Xuất sắc | Đẩy mạnh — đây là video tiêu biểu |

## Giao thức 48 Giờ (The 48-Hour Protocol)

Thực hiện theo đúng thứ tự này, 48–72 giờ sau khi xuất bản:

1. Mở **YouTube Studio → Analytics (Phân tích) → chọn video vừa xuất bản**
2. Ghi lại 3 con số:
   - **CTR** (Tỷ lệ nhấp chuột trên lượt hiển thị)
   - **AVD** (Thời lượng xem trung bình — lấy phần trăm %)
   - **Total views** (Tổng số lượt xem) tính đến thời điểm đó
3. So sánh CTR với bảng mốc chuẩn ở trên — đang ở cấp độ (tier) nào?
4. So sánh AVD với bảng mốc chuẩn ở trên — đang ở cấp độ (tier) nào?
5. Chạy Cây Quyết Định (Decision Tree) bên dưới để xác định hành động

## Cây Quyết Định (Decision Tree)

```
CTR < 2% VÀ AVD > 50%
→ VẤN ĐỀ: Tiêu đề/hình thu nhỏ không kết nối. Nội dung thì ổn.
→ HÀNH ĐỘNG: Thay tiêu đề trước (nhanh hơn, dễ đánh giá hơn).
           Viết giả thuyết. Đợi 7 ngày.

──────────────────────────────────────────

CTR < 2% VÀ AVD < 40%
→ VẤN ĐỀ: Cả phần khám phá lẫn nội dung đều có vấn đề.
→ HÀNH ĐỘNG: Thay tiêu đề trước. Đồng thời gắn cờ (flag) vấn đề nội dung
           để xem lại ở Giai đoạn 3 (Stage 3) cho video sau.

──────────────────────────────────────────

CTR 2–3.5% VÀ AVD > 50%
→ TRẠNG THÁI: Bình thường. Thuật toán vẫn đang học.
→ HÀNH ĐỘNG: Tùy chọn — test 1 biến thể (variant) tiêu đề.
           Hoặc chờ 2 tuần nữa trước khi quyết định.

──────────────────────────────────────────

CTR 3.5%+ VÀ AVD 55%+
→ TRẠNG THÁI: Tín hiệu mạnh. Thuật toán đang quảng bá đúng.
→ HÀNH ĐỘNG: KHÔNG thay gì. Bảo vệ video này.

──────────────────────────────────────────

CTR ổn nhưng AVD < 40%
→ VẤN ĐỀ: Hook thất bại trong 30 giây đầu,
           hoặc nội dung không khớp với lời hứa của tiêu đề.
→ HÀNH ĐỘNG: KHÔNG thay tiêu đề/hình thu nhỏ — không phải vấn đề ở đó.
           Gắn cờ cho bài học Giai đoạn 3 (Stage 3). Vấn đề nằm trong video.
```

## Cần thay đổi gì trong Tiêu đề

Khi quyết định thay tiêu đề:

1. Đọc lại **Công thức Tiêu đề v3.0 (Title Formula v3.0)** từ tệp `06_title_seo_knowledge.md` (Công thức Narrative Hook)
2. Viết **3 biến thể (variants) tiêu đề mới**
3. Chấm điểm mỗi biến thể theo **hệ thống 6 điểm (6-point system)** từ tệp 06
4. Chọn biến thể có điểm cao nhất (tối thiểu 9/12)
5. Dán vào **YouTube Studio → Details (Chi tiết) → Title (Tiêu đề)**

Không tự ý đổi tiêu đề theo cảm tính. Không đổi nếu không có giả thuyết. Không đổi nếu điểm thấp hơn 9/12.

## Lưu trữ Hồ sơ (Record Keeping)

Sau mỗi thay đổi, ghi lại theo định dạng này:

```
VIDEO: [tên video]
DATE PUBLISHED: [ngày]
DATE CHANGED: [ngày thay đổi, nếu có]
ORIGINAL TITLE: [tiêu đề ban đầu]
NEW TITLE: [tiêu đề mới, nếu thay]
CTR BEFORE: [%]
CTR AFTER (7 ngày sau): [%]
AVD: [%]
LESSON: [1 câu rút ra]
```

Lưu hồ sơ này vào ghi chú phiên làm việc (session notes) hoặc yêu cầu Boss lưu vào tệp nháp (scratch file). Mỗi hồ sơ là 1 điểm dữ liệu (data point) cho việc ra quyết định tốt hơn ở video sau.

## Quy tắc Cốt lõi (Core rule)

**Dữ liệu đi trước. Giả thuyết theo sau. Hành động là bước thứ ba. (Data first. Hypothesis second. Action third.)**

Không thay tiêu đề theo cảm tính. Không thay hình thu nhỏ vì "nhìn chán". Không thay gì khi video đang hoạt động trên mức chuẩn — thuật toán đang làm đúng việc của nó, đừng can thiệp.

Nếu Boss chia sẻ các con số và hỏi "có nên đổi không?" — Coslient chạy Cây Quyết Định (Decision Tree), đề xuất giả thuyết nếu cần thay, giải thích lý do. Không bao giờ đề xuất thay đổi mà không có dữ liệu hỗ trợ.
