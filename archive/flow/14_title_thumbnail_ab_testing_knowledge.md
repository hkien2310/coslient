# Coslient GPT Knowledge - Title & Thumbnail A/B Testing (Post-Publish)

## Purpose
File này định nghĩa quy trình kiểm tra và tối ưu title/thumbnail **sau khi publish** dựa trên dữ liệu thực tế từ YouTube Studio. Đây không phải là SEO một lần — đây là vòng lặp cải thiện liên tục dựa trên signal thật, không phải phỏng đoán.

Stage 6 chỉ là điểm bắt đầu. File này là bước tiếp theo.

## When to use
Kích hoạt **48–72 giờ sau mỗi lần publish**. Boss mở YouTube Studio, chia sẻ số CTR và AVD, Coslient đọc dữ liệu và đề xuất hành động tiếp theo (hoặc không làm gì).

## The One Variable Rule

**Chỉ test 1 biến tại một thời điểm.**

Không thay title VÀ thumbnail cùng lúc. Nếu thay cả 2, không biết cái nào gây ra thay đổi — tất cả learning đều vô nghĩa.

- Nếu quyết định test: chọn title HOẶC thumbnail, không phải cả hai.
- Đợi ít nhất 7 ngày để có đủ data trước khi đánh giá kết quả.
- Chỉ test 1 video tại một thời điểm — không chạy 3 video test song song.

## Hypothesis Format

Trước khi thay đổi bất cứ thứ gì, viết hypothesis ra. Không có hypothesis → không thay đổi.

```
HYPOTHESIS:
Because [observation from data],
I believe changing [title OR thumbnail — pick one]
from [current version]
to [new version]
will increase [CTR or AVD]
because [psychology reason].
I'll know it worked if [metric] improves after 5+ days.
```

**Ví dụ thực tế:**

```
HYPOTHESIS:
Because CTR is 2.1% (below benchmark for our niche),
I believe changing the title
from "The Blue Cup | A Warm Song for Still Evenings"
to "She Still Sets Two Cups Every Morning — A Warm Song | Coslient (4K)"
will increase CTR
because the new title has a narrative hook (specific situation)
instead of a descriptive label.
I'll know it worked if CTR exceeds 3.5% after 7 days.
```

## YouTube CTR Benchmarks — Coslient's Niche

Niche: emotional music video, 45+ audience, browse-heavy (viewer không chủ động tìm — YouTube đề xuất).

| CTR | Đánh giá | Hành động |
|-----|----------|-----------|
| Dưới 2% | Title hoặc thumbnail không kết nối — cần thay đổi | Test title trước |
| 2–3.5% | Trung bình — có tiềm năng nhưng còn cải thiện được | Optional test, hoặc chờ thêm 2 tuần |
| 3.5–5% | Tốt — algorithm đang promote đúng | Không thay gì |
| 5%+ | Mạnh — protect this | Tuyệt đối không đụng vào |

## YouTube AVD Benchmarks — Video nhạc 3–5 phút

| AVD | Đánh giá | Hành động |
|-----|----------|-----------|
| Dưới 40% | Hook thất bại hoặc content lỗi — người xem bỏ sớm | Xem xét hook đầu video |
| 40–55% | Acceptable cho format nhạc | Theo dõi, không cần hành động gấp |
| 55–70% | Tốt — âm nhạc và hình ảnh đang landing | Promote video này nhiều hơn |
| 70%+ | Exceptional | Đẩy mạnh — đây là video tiêu biểu |

## The 48-Hour Protocol

Thực hiện theo đúng thứ tự này, 48–72h sau khi publish:

1. Mở **YouTube Studio → Analytics → chọn video vừa publish**
2. Ghi lại 3 số:
   - **CTR** (Impressions click-through rate)
   - **AVD** (Average view duration — lấy %)
   - **Total views** tính đến thời điểm đó
3. So CTR với bảng benchmark trên — đang ở tier nào?
4. So AVD với bảng benchmark trên — đang ở tier nào?
5. Chạy Decision Tree bên dưới để xác định hành động

## Decision Tree

```
CTR < 2% VÀ AVD > 50%
→ PROBLEM: Title/thumbnail không kết nối. Content thì ổn.
→ ACTION: Thay title trước (nhanh hơn, dễ đánh giá hơn).
           Viết hypothesis. Đợi 7 ngày.

──────────────────────────────────────────

CTR < 2% VÀ AVD < 40%
→ PROBLEM: Cả discovery lẫn content đều có vấn đề.
→ ACTION: Thay title trước. Đồng thời flag content problem
           để xem lại ở Stage 3 cho video sau.

──────────────────────────────────────────

CTR 2–3.5% VÀ AVD > 50%
→ STATUS: Bình thường. Algorithm vẫn đang học.
→ ACTION: Optional — test 1 title variant.
           Hoặc chờ 2 tuần nữa trước khi quyết định.

──────────────────────────────────────────

CTR 3.5%+ VÀ AVD 55%+
→ STATUS: Signal mạnh. Algorithm đang promote đúng.
→ ACTION: KHÔNG thay gì. Protect this video.

──────────────────────────────────────────

CTR ổn nhưng AVD < 40%
→ PROBLEM: Hook thất bại trong 30 giây đầu,
           hoặc content không khớp với promise của title.
→ ACTION: KHÔNG thay title/thumbnail — không phải vấn đề ở đó.
           Flag cho Stage 3 learning. Vấn đề nằm trong video.
```

## What to Change in a Title

Khi quyết định thay title:

1. Đọc lại **Title Formula v3.0** từ file `06_title_seo_knowledge.md` (Narrative Hook formula)
2. Viết **3 title variants mới**
3. Chấm điểm mỗi variant theo **hệ thống 6-point** từ file 06
4. Chọn variant có điểm cao nhất (tối thiểu 9/12)
5. Paste vào **YouTube Studio → Details → Title**

Không tự ý đổi title theo cảm tính. Không đổi nếu không có hypothesis. Không đổi nếu điểm thấp hơn 9/12.

## Record Keeping

Sau mỗi thay đổi, ghi lại theo format này:

```
VIDEO: [tên video]
DATE PUBLISHED: [ngày]
DATE CHANGED: [ngày thay đổi, nếu có]
ORIGINAL TITLE: [title ban đầu]
NEW TITLE: [title mới, nếu thay]
CTR BEFORE: [%]
CTR AFTER (7 ngày sau): [%]
AVD: [%]
LESSON: [1 câu rút ra]
```

Lưu record này vào session notes hoặc yêu cầu Boss lưu vào scratch file. Mỗi record là 1 data point cho việc ra quyết định tốt hơn ở video sau.

## Core rule

**Data first. Hypothesis second. Action third.**

Không thay title theo cảm tính. Không thay thumbnail vì "nhìn chán". Không thay gì khi video đang perform trên benchmark — algorithm đang làm đúng việc của nó, đừng can thiệp.

Nếu Boss chia sẻ số và hỏi "có nên đổi không?" — Coslient chạy Decision Tree, đề xuất hypothesis nếu cần thay, giải thích lý do. Không bao giờ đề xuất thay đổi mà không có data support.
