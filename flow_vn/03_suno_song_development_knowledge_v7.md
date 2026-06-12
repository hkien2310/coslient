# Coslient — Kiến thức Phát triển Bài hát Suno v7.0 "Trí tuệ Ngách"

## Mục đích

Tài liệu này hướng dẫn Coslient biến một **concept đã được Boss duyệt** thành một **song package Suno-ready** hoàn chỉnh, và sau khi Boss chốt nhạc, xuất ra một **file lời bài hát sạch chuẩn Spotify**.

> Bài hát phải khiến người nghe **phiêu theo từ câu đầu tiên** — không phải chỉ đọc lời hay, mà phải NGHE hay. Melody bắt tai, nhịp cuốn chân, dynamics dâng trào, và hook đọng lại trong đầu cả ngày.

---

## PHẦN A — QUY TRÌNH VẬN HÀNH (PIPELINE)

### A1. Điều kiện tiên quyết

Stage này **chỉ bắt đầu** khi Boss đã duyệt concept (`02_concept.md`). Nếu concept còn yếu, quay lại Stage 2 để tinh chỉnh trước.

> [!IMPORTANT]
> **BƯỚC ĐẦU TIÊN — HỎI BOSS CHỌN ĐỘ DÀI BÀI HÁT:**
>
> ```
> Bài hát lần này làm theo độ dài nào?
>
> [1] 2 phút  → Cấu trúc cô đọng, đi thẳng vào hook, phù hợp test retention
> [2] 4 phút  → Cấu trúc đầy đủ như hiện tại, khai thác trọn vẹn câu chuyện
> ```
>
> **Chờ Boss trả lời trước khi bắt đầu Pass 1.** Câu trả lời sẽ quyết định cấu trúc bài hát (xem F7), số lượng section, và target lyrics length (xem bên dưới).
>
> | Chọn | Target lyrics | Target sections | Ghi chú |
> | :--- | :--- | :--- | :--- |
> | **2 phút** | **20-30 dòng** | Tối đa 5 sections (Intro + V1 + Chorus + V2 + Chorus/Outro) | Không Bridge, không Final Chorus riêng |
> | **4 phút** | **40-60 dòng** | 7-9 sections đầy đủ | Như hiện tại |

---

### A2. Quy trình viết 4 Lượt (4-Pass Writing Process)

| Lượt | Tên gọi | Trọng tâm |
| :--- | :--- | :--- |
| **Pass 1** | Story & Melody Skeleton | Câu chuyện, cảm xúc, tiêu đề, hook — VÀ xác định melodic direction (melody lên/xuống ở đâu, nốt cao nhất rơi vào từ nào). |
| **Pass 2** | Groove & Dynamics | Xác định energy map toàn bài, groove feel, nhịp điệu drive. Đảm bảo contrast giữa verse/chorus. Chọn cấu trúc bài hát. |
| **Pass 3** | Craft & Deslop | Kiểm tra singability, cân bằng meter, near rhymes, tiêu diệt mọi từ AI slop. |
| **Pass 4** | Suno Technical Layer | Gắn structural metatags `[]`, backing vocals `()`, dấu ba chấm `...`, vocal cues, finalize style prompt. |

### A3. Đầu ra bắt buộc — Song Package (Bản nháp)

Khi trình Boss, song package **phải** có đầy đủ các mục sau:

```
STAGE: Song Development
STATUS: draft

SONG DURATION: [2 phút / 4 phút — ghi rõ Boss đã chọn]

MUSIC DIRECTION:
- [thể loại/pha trộn, nhịp điệu, nhạc cụ, hình mẫu giọng hát, giai điệu đặc trưng]

EMOTIONAL DIRECTION:
- [cung bậc cảm xúc: từ đâu → đến đâu]

MELODY DIRECTION:
- [đường nét giai điệu: giai điệu verse thấp/trung, giai điệu chorus vút cao/hùng tráng]
- [loại hook: lời / giai điệu / nhịp điệu — mục tiêu ≥ 2/3]
- [nốt cao nhất rơi vào từ nào trong chorus]

DYNAMIC ARC:
- [bản đồ năng lượng: Intro X% → Verse X% → Pre-Chorus X% → Chorus X% → Bridge X% → Final Chorus X%]
- [tỷ lệ tương phản: phần mạnh nhất gấp bao nhiêu lần phần nhẹ nhất]

GROOVE STRATEGY:
- [cảm giác nhịp điệu: thẳng/swung/đảo phách/cuộn]
- [cách tiếp cận bộ gõ]
- [điều gì khiến người nghe nhịp chân/gật đầu]

STORY ANGLE:
- [câu chuyện con người, hình ảnh cụ thể, yếu tố siêu thực nếu có]

STRUCTURE:
- [cấu trúc đã chọn từ Thư viện Cấu trúc, lý do — xem F7 cho cấu trúc 2 phút]

HOOK STRATEGY:
- [hook lời: cụm từ trung tâm, tại sao dễ nhớ]
- [hook giai điệu: đường nét giai điệu của hook, nguyên âm nào ở nốt cao]
- [hook nhịp điệu: pattern nhịp đặc trưng nếu có]
- [chorus cuối sâu hơn như thế nào — BẮT BUỘC thay đổi ≥ 1 yếu tố]

VOCAL PERFORMANCE STRATEGY:
- [các công cụ biểu diễn sử dụng, lý do]

ORIGINALITY NOTE:
- [điều gì khiến bài hát này khác biệt — phải nêu được ≥ 1 yếu tố chưa bao giờ làm]

SONG TITLE:
[tên bài hát]

STYLE:
[Suno style prompt, 120-200 ký tự tối ưu, tối đa 800 ký tự, chỉ mô tả nhạc]

LYRICS:
[toàn bộ lời tiếng Anh kèm section labels và performance markup]

SUNO TESTING NOTE:
Tạo 3-5 phiên bản. Chọn take có vocal melody mạnh nhất, groove bắt tai nhất, dynamic lift rõ ràng nhất, và chorus đọng lại lâu nhất.

NEXT STEP:
Chờ Boss duyệt hoặc feedback để tôi chỉnh tiếp.
```

### A4. Đầu ra cuối cùng — Clean Lyrics File (`03_clean_lyrics.txt`)

> [!IMPORTANT]
> **Chỉ tạo SAU KHI Boss chốt nhạc cuối cùng.** Không tạo trong giai đoạn draft.

**Quy cách chuẩn Spotify (Spotify-Ready Format):**
*   **Viết hoa chữ cái đầu tiên của mỗi dòng** — (Sentence case per line), convert mọi từ ALL CAPS về chữ thường (trừ tên riêng).
*   **Không đưa tên bài hát vào đây** — Bắt đầu ngay bằng câu hát đầu tiên.
*   **Không metatags** — xóa sạch tất cả `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`, `[Outro]` v.v.
*   **Không ghi chú nhạc cụ** — xóa sạch `[Guitar solo]`, `[Piano fill]` v.v.
*   **Không dấu ngoặc vuông `[]`** — xóa tất cả.
*   **Không dấu ngoặc đơn `()`** — xóa tất cả backing vocals, ad-libs, hums.
*   **Không dấu ba chấm `...`** — xóa tất cả.
*   **Không viết số** — viết bằng chữ (ví dụ: `1982` → `nineteen eighty-two`).
*   **Giữ nguyên ngắt dòng tự nhiên** — mỗi câu hát một dòng, dòng trống giữa các phân đoạn.

---

## PHẦN B — BẢN SẮC ÂM NHẠC COSLIENT (CREATIVE IDENTITY)

### B1. Core Music Identity — Theme-Driven, Genre-Free

Coslient **không bị khóa vào bất kỳ genre nào**. Bản sắc Coslient là một **chuẩn chất lượng cảm xúc**, không phải một thể loại nhạc:

*   **Trưởng thành, nhân văn, kể chuyện, cảm xúc rõ ràng, phù hợp người lớn 45+.**
*   **Nhạc phải có CHIỀU SÂU** — không bao giờ phẳng lỳ, không bao giờ generic.

**Quy tắc "Đưa chủ đề vào → Ra phong cách phù hợp":**

Khi nhận concept, Coslient phải tự xác định phong cách nhạc tối ưu cho concept đó. Không mặc định bất kỳ genre nào. Ví dụ:

| Concept | Genre tự nhiên | Lý do |
| :--- | :--- | :--- |
| Ông lão nhớ vợ qua chiếc cốc cà phê | Acoustic folk-blues, fingerpicked | Sự thân mật, ấm áp, giản dị |
| Thị trấn nhỏ trôi vào vũ trụ | Cinematic space-folk, orchestral swells | Quy mô sử thi, sự kỳ diệu |
| Đại dương ôm giữ ký ức | Celtic pop, rolling 6/8 waltz | Nhịp điệu đại dương, cảm giác cổ kính |
| Người thợ rèn già và ngọn lửa cuối cùng | Delta blues, slide guitar, raw | Sự gai góc, sức nóng, lao động |
| Khu vườn mùa thu tự kể chuyện | Chamber pop, strings + piano | Sự thanh lịch, các mùa |
| Cô đơn giữa thành phố đêm | Jazz noir, smoky saxophone | Nỗi u buồn thành thị, sự tinh tế |
| Ngọn hải đăng cuối cùng | Post-rock ambient, crescendo walls | Sự cô lập, đại dương bao la |
| Lá thư không gửi | Bossa nova, nylon guitar | Sự nuối tiếc nhẹ nhàng, cơn gió ấm |
| Chuyến tàu đêm xuyên nước Nga | Cinematic orchestral, Russian folk elements | Cuộc hành trình, cảnh quan rộng lớn |
| Người làm vườn và bầy ong | Pastoral folk-pop, mandolin, accordion | Vùng nông thôn, cuộc sống nhộn nhịp |

**Palette thể loại mở rộng (không giới hạn, đây chỉ là gợi ý):**
`acoustic folk` · `indie folk-pop` · `Americana` · `chamber orchestral pop` · `vintage gospel-soul` · `Celtic pop` · `delta blues` · `jazz noir` · `bossa nova` · `post-rock ambient` · `cinematic orchestral` · `country ballad` · `R&B soul` · `baroque pop` · `art rock` · `progressive folk` · `flamenco fusion` · `tango nuevo` · `Nordic noir folk` · `desert rock` · `Appalachian bluegrass` · `French chanson` · `African highlife` · `reggae acoustic` · `psychedelic folk`

### B2. Emotional Arc — Cozy Healing Gate + Emotional Mode Selector

**Mặc định:** Luôn đi từ buồn nhẹ/hoài niệm → ấm áp/chữa lành. **Không** kết thúc trong bóng tối tuyệt đối.

**Cấm tông chủ đạo hoặc kết thúc:** Bóng tối đen kịt, nỗi đau không thể chữa lành, sự ảm đạm, sự cay đắng, sự tuyệt vọng.

**Nhưng KHÔNG cấm:**
*   Đau đớn thực sự (grief) — miễn là có ánh sáng ở cuối.
*   Căng thẳng kịch tính (tension) — miễn là có giải quyết (resolution).
*   Sự cô đơn sâu sắc — miễn là kết thúc với sự kết nối hoặc sự chấp nhận.
*   Gai góc, nguyên bản, thô ráp — miễn là có nhân văn.

**Đạt tối thiểu ≥ 2/4 tiêu chí:**
1.  **Comfort in simple things** — Sự an ủi trong những điều giản dị.
2.  **The internal home** — Mái ấm bên trong tâm hồn.
3.  **Cozy nature** — Thiên nhiên ấm cúng.
4.  **Gentle nostalgia** — Hoài niệm dịu êm.

#### B2.5. Emotional Mode Selector (MỚI — v7.0)

> [!IMPORTANT]
> Trước khi viết lyrics, Boss và Agent **phải chọn 1 trong 4 Emotional Mode** dưới đây. Mode quyết định lyric strategy, bridge function, và ending type. Mỗi mode có engagement profile khác nhau — chọn dựa trên content strategy goal.

| Mode | Tên | Cảm xúc cốt lõi | Comment Engagement | Watch Time |
| :--- | :--- | :--- | :--- | :--- |
| **A** | **Bittersweet Return** | Quay về một nơi/người trong ký ức, vừa đau vừa ấm | Trung bình — bình luận hoài niệm | Cao |
| **B** | **Peaceful Observation** | Quan sát cảnh đẹp bình yên, không cần nhân vật cụ thể | Thấp hơn — mang tính trị liệu/làm nền | Rất Cao (xem lại) |
| **C** | **Regret + Call to Action** | Tiếc nuối điều chưa nói/làm → thúc đẩy hành động ngay hôm nay | **Cao nhất** — "Tôi đã gọi cho mẹ" | Cao |
| **D** | **Cathartic Grief** | Đau mất mát thực sự (người thân, thú cưng) → được phép khóc | **Cao nhất** — khóc + chia sẻ | Cao |

**Chiến lược chọn Mode:**
- Muốn nhiều bình luận → chọn Mode C hoặc D
- Muốn nhiều lượt xem lại / nghe làm nền → chọn Mode B
- Muốn cân bằng giữa bình luận và thời gian xem → chọn Mode A
- Muốn chia sẻ lan truyền (tag bạn bè) → Mode C hoặc D

**Mode ảnh hưởng đến Bridge và Ending:**

| Mode | Chức năng Bridge | Loại Ending |
| :--- | :--- | :--- |
| **A** | Khoảnh khắc hiển linh — hiểu ra điều gì đó | Tiếng guitar nhỏ dần + tiếng thì thầm/nói |
| **B** | Đỉnh điểm giác quan — khoảnh khắc đẹp nhất của ngày | Lời ca đứt đoạn/không trọn vẹn → cảm giác vương vấn |
| **C** | Lời tuyên bố — triết lý trung tâm của bài | Lời kêu gọi hành động trực tiếp + tiếng piano bước vào |
| **D** | Bước nhảy thời gian (trẻ → già → chết) | Hát không lời + nhạc cụ đặc biệt → sự im lặng |

### B3. Tiêu đề bài hát — Khung đặt tên Coslient (Thẩm mỹ Indie "Chống sến")

> [!IMPORTANT]
> **QUY TẮC BẮT BUỘC (Quy tắc tối cao — ghi đè mọi gợi ý bên dưới):**
> - **Tối đa 3 từ** — không được dài hơn.
> - **Ngắn gọn nhưng đầy đủ nghĩa** — người đọc xong phải cảm nhận được hồn của bài hát, dù chưa nghe.
> - **Hoặc kỳ lạ** — từ ngữ gây tò mò, khó đoán, buộc người ta phải bấm nghe để hiểu.
> - Nếu đề xuất tên bài, luôn đưa ra **3–5 phương án** kèm phân tích ngắn gọn (nghĩa kép, cảm giác gợi ra, lý do chọn).

Tiêu đề là **điểm chạm đầu tiên (Khoảng trống tò mò)**. Tên bài hát phải đóng vai trò như một tác phẩm nghệ thuật (Art-house/Indie), tuyệt đối không dùng để "tóm tắt" hay "kể lể" trần trụi nội dung. MỤC TIÊU LÀ TIẾNG ANH.

> [!WARNING]
> **BỘ LỌC CHỐNG "CHEESY" (Chống Sến/Chống Kịch tính thái quá)**
> - ❌ **Cấm từ ngữ cường điệu, khóc lóc:** *Agony, Shattered, Bleeding Heart, Tears, Sorrow, Weeping.*
> - ❌ **Cấm công thức sáo rỗng (Bẫy "Of The"):** `[Danh từ Trừu tượng] of the [Khái niệm Vĩ mô]` (VD: *Echoes of the Heart*, *Symphony of the Soul*, *Whispers of Time*).
> - ❌ **Cấm câu hỏi tu từ sến súa:** *Why Did You Leave?, Where Did Our Love Go?*

**5 Trụ Cột Đặt Tên "Sang" (Dựa trên Nghiên cứu Nhạc Indie/Alt-Rock/Pop Hiện Đại):**

**1. Sự Trừu Tượng Hóa & Hiện Tượng Học (Lâm sàng & Trừu tượng)**
Thay vì kể lể cảm xúc, hãy dùng các khái niệm y tế, khoa học, hoặc địa lý để ám chỉ sự việc. Tạo sự lạnh lùng, khách quan cho một nỗi đau.
- ✅ *Blood Bank* (Bon Iver), *Chinese Satellite* (Phoebe Bridgers), *First Breath After Coma* (Explosions in the Sky), *Holocene*.
- ❌ *The Hospital of Sadness*, *Stars in the Sky*.

**2. Vật Thể Hóa & Không Gian Cụ Thể (Điểm neo Siêu cụ thể)**
Dùng một vật thể cực kỳ đời thường hoặc một địa danh/địa chỉ chính xác làm đại diện cho toàn bộ câu chuyện (Tương quan khách quan).
- ✅ *Casimir Pulaski Day* (Sufjan Stevens), *Stoned at the Nail Salon* (Lorde), *Fake Plastic Trees* (Radiohead), *Needle in the Hay*.
- ❌ *The Town of Memories*, *Tears in the Rain*.

**3. Phá Vỡ Ngữ Pháp & Xung Đột Hình Ảnh (Sự đặt cạnh nhau)**
Kết hợp những từ không liên quan hoặc đối lập nhau kịch liệt (bạo lực vs mỏng manh, tự nhiên vs nhân tạo) để tạo ra cảm giác Siêu thực.
- ✅ *Bullet With Butterfly Wings* (Smashing Pumpkins), *Crying Lightning* (Arctic Monkeys), *Flightless Bird, American Mouth* (Iron & Wine).
- ❌ *Sad Winter*, *Lonely Night*.

**4. Chữ Thường & Lời Nói Đời Thường (Lời tự thú bằng chữ thường)**
Cắt một mảnh hội thoại cực kỳ tự nhiên, hoặc định dạng toàn bộ bằng **chữ viết thường (lowercase)** để tạo cảm giác riêng tư, thì thầm, giống như một tin nhắn lúc 2h sáng.
- ✅ *when the party's over* (Billie Eilish), *Why'd You Only Call Me When You're High?* (Arctic Monkeys), *hope is a dangerous thing...* (Lana Del Rey).
- ❌ *I Will Always Love You*, *Please Come Back*.

**5. Câu Hỏi Bỏ Ngỏ & Nghịch Lý (Khoảng trống tò mò)**
Đặt tên tạo ra một sự mâu thuẫn hoặc câu hỏi khiến người ta BẮT BUỘC phải bấm vào nghe để hiểu tại sao.
- ✅ *The System Only Dreams in Total Darkness* (The National), *How to Disappear Completely* (Radiohead), *The Predatory Wasp of the Palisades Is Out to Get Us!*
- ❌ *A Song About Depression*, *The Sad Love Story*.

**Kiểm tra tiêu đề (Bài kiểm tra 4 điểm):**
1. **Kiểm tra độ sến:** Có từ nào đọc lên nghe giống nhạc Pop thập niên 90 hay do AI tạo ra không (Echoes, Whispers...)? Nếu có → Đổi.
2. **Kiểm tra hình ảnh:** Tiêu đề có gợi ra một BỨC TRANH cụ thể không (VD: *Nail Salon*, *Plastic Trees*) hay chỉ là KHÁI NIỆM (*Sorrow*)? Phải là bức tranh.
3. **Kiểm tra sự tò mò:** Đọc lên có thấy tò mò, kỳ quặc, muốn bấm nghe không?
4. **Kiểm tra định dạng:** Cân nhắc dùng *toàn bộ chữ thường (lowercase)* để tăng tính tự sự, lofi, indie.

### B4. DNA Câu chuyện Coslient — Hồn cốt câu chuyện

**"Một ký ức nhỏ hóa thành âm nhạc"** — Câu chuyện phải đủ giản dị, dễ hiểu và gần gũi với khán giả lớn tuổi (45+) ngay từ những câu hát đầu tiên.

**5 Tiêu chí Vàng:**
1. **Sự thật nhân loại phổ quát:** Ai cũng từng trải qua. Tránh quá kỳ lạ hay triết lý cao siêu.
2. **Quy tắc "Một":** Một nhân vật chính, một vật thể trọng tâm, một khoảnh khắc cụ thể.
3. **Hiểu ngay từ Verse 1:** Không cần bối cảnh hay giải thích.
4. **Giản dị hóa:** Đẹp ở sự chân phương. Một ấm trà nguội có sức nặng hơn vạn lời thề.
5. **Bài kiểm tra "Kể cho bà ngoại nghe":** Bà ngoại 70 tuổi nghe xong Verse 1 mà hỏi "Bài này nói về cái gì?" → quá phức tạp, viết lại.

### B5. Lời bài hát — Thể hiện, Đừng kể (Show, Don't Tell)

Cảm xúc phải gắn vào **vật thể, địa điểm, hành động hoặc chi tiết giác quan cụ thể**.

| ❌ Yếu (Trừu tượng) | ✅ Mạnh (Giác quan) |
| :--- | :--- |
| *I was sad. I miss the past.* | *Your coat still hangs behind the kitchen door.* |
| *Love is in my heart.* | *The blue cup caught the morning on my windowsill.* |
| *Memories shine forever.* | *The chair by the window still knows your shape.* |

**Sự tách biệt giữa Lời bài hát và Video (QUAN TRỌNG):** Lời bài hát = cảm xúc, chất liệu giác quan, thế giới nội tâm. Video = hiệu ứng thị giác, phép thuật siêu thực. **KHÔNG BAO GIỜ** kể lại các hiệu ứng video trong lời hát.

**Các thủ pháp Lời bài hát Siêu thực (Phép thuật Coslient được nhúng vào):**
*   **Xung đột Thời gian:** *The clock on the wall ticks backwards, bringing 1982 to the kitchen door.*
*   **Sự biến đổi Vật chất:** *I planted tea leaves in your cup, and a tiny forest grew from the porcelain rim.*
*   **Kiến trúc Sống:** *The floorboards hum the song you used to play.*

### B5.5. Tính Thơ & Các Mối Quan Hệ (Sự thân mật đầy chất thơ)

1. **Dùng Ẩn dụ Vật lý:** Biến nỗi đau trừu tượng thành thực thể vật lý. Đừng viết "I miss you."
2. **Kể chuyện phi tuyến tính:** Ném người nghe vào mảnh ký ức lộn xộn đan xen quá khứ và hiện tại.
3. **Tôn vinh sự đời thường:** Tình yêu sâu sắc nhất nằm ở sự bình dị: *"Tell me about your day."*

### B5.6. Giao thức Nhạc đề Vật thể (MỚI — v7.0)

> [!IMPORTANT]
> Đây là kỹ thuật tạo ra sự đền đáp cảm xúc lớn nhất trong ngách folk/indie. Chọn 1 vật thể bình thường TRƯỚC KHI viết bài → lên kế hoạch cách nó xuất hiện nhiều lần → lần cuối cùng phải gây chấn động.

**3 bước bắt buộc:**

**Bước 1 — Chọn Vật thể:** Vật thể phải:
- Cực kỳ bình thường (không phải "trái tim", "bầu trời", "ngọn gió")
- Gắn với nhân vật cụ thể (chiếc cốc của bà, cái chăn của con mèo, chiếc ghế của ông)
- Có thể được nhìn/chạm/ngửi/nghe → không phải khái niệm

**Bước 2 — Lên kế hoạch Xuất hiện (tối thiểu 3 lần):**

| Lần xuất hiện | Ngữ cảnh | Mức độ cảm xúc |
| :--- | :--- | :--- |
| **Lần 1** (Verse 1/Verse 2) | Giới thiệu vật thể — bình thường, trung tính | 0% — chỉ là vật |
| **Lần 2** (Chorus/Verse 3) | Vật thể gắn với hành động/kỷ niệm | 40% — bắt đầu mang ý nghĩa |
| **Lần 3** (Bridge/Verse 4) | Vật thể thể hiện sự thay đổi (ai đó già đi, sức khỏe kém, v.v.) | 70% — người nghe bắt đầu lo |
| **Lần 4** (Outro/Final) | Vật thể lần cuối cùng — ngữ cảnh đã hoàn toàn thay đổi | 100% — sự đền đáp |

**Bước 3 — Quy tắc Đền đáp Cuối cùng:**
Lần xuất hiện cuối của vật thể phải có ít nhất 1 trong các yếu tố:
- Ngữ cảnh đã đảo ngược hoàn toàn (vật thể từ vui → buồn, từ đầy → vắng)
- Hành động đi kèm đã thay đổi (ai đó đặt nó xuống lần cuối)
- Câu lời bài hát có cùng từ nhưng nghĩa đã khác hoàn toàn

**Ví dụ từ kho dữ liệu:**
- ✅ "The faded blue blanket" (bài Cat): Verse 1=ấm áp, Verse 2=gối đầu, Chorus=bảo vệ, Verse 5=**"You climb to the blanket one final time"** → gây chấn động
- ✅ "Tuesday" (bài Last Time): xuất hiện 2 lần trong post-chorus → neo giữ toàn bộ thông điệp của bài hát

**Lưu ý:** Nhạc đề Vật thể có thể kết hợp với Tiêu đề Coslient (B3) — đặt tên bài theo chính vật thể đó.

### B6. Ràng buộc cho Ngách Folk Chữa lành (MỚI — v7.0)

> [!NOTE]
> Phần này áp dụng **khi ý tưởng thuộc ngách acoustic folk / indie folk chữa lành** — loại nhạc được nghiên cứu từ 5 bài gây sốt (Three-Quarter Town, loạt phim Siêu thực AI). Khi Sếp xác nhận ý tưởng thuộc ngách này, agent BẮT BUỘC tuân theo các ràng buộc bên dưới thay vì tự do lựa chọn.

**Các quy tắc về Kết cấu Acoustic (cứng):**
- ✅ Acoustic guitar gảy ngón HOẶC strum acoustic đánh nốt móc đơn (8th-note) đều đặn — không bao giờ dùng tiếng lead điện/chói tai
- ✅ Upright bass HOẶC acoustic bass — **không dùng bass điện** (mất đi tính nguyên bản của folk)
- ✅ Trống snare quét chổi mềm, shaker, kick nhẹ — không bao giờ dùng trống rock nặng
- ✅ 1 Nhạc cụ Đặc biệt (xem D2.5) — piano, glockenspiel, cello, đàn dây, hoặc guitar thứ hai
- ❌ Cấm: biến dạng guitar điện, synths, trống lập trình, bass nặng

**Các quy tắc về Nhịp độ & Tông nhạc:**
- Nhịp độ (BPM): **74–120** (điểm hoàn hảo: **78–82 BPM** cho ballad, 110–115 cho folk nhịp nhanh)
- Tông (Key): **Sol Trưởng (G Major)** hoặc Rê Trưởng (D Major) chiếm ưu thế — tạo các hợp âm guitar ấm áp, vang vọng
- Nhịp (Time): **4/4** mặc định — 3/4 chỉ khi ý tưởng cần cảm giác nhịp waltz (điệu valse)

**Triết lý Phối khí — "Chỉ Thêm vào":**
- Intro (Mở đầu): guitar solo (1 nhạc cụ) hoặc guitar + nhịp thở
- Mỗi phần THÊM tối đa 1 nhạc cụ mới
- Không loại bỏ nhạc cụ giữa bài (trừ khi giảm bớt (strip-back) ở Bridge có chủ đích)
- Nhạc cụ Đặc biệt **không có từ đầu** — chỉ vào tại đỉnh điểm cảm xúc
- Outro (Kết bài): giảm bớt dần chỉ còn guitar → mờ dần

**Cấu trúc Thanh nhạc:**
Chọn 1 trong 2:
- **Song ca (Nam/Nữ):** Hát đối đáp ở các verse → hát bè ở chorus → đồng thanh ở đỉnh điểm cảm xúc. *Đồng thanh = hai người cùng sống trong một khoảnh khắc.*
- **Giọng Nam trung (Baritone) Solo:** Sự tổn thương nam tính + độ khàn nhẹ. Giọng người kể chuyện trưởng thành. Thu âm sát micro.

**Cách tiếp cận Lời bài hát:**
Chọn 1 trong 3:
- **Cá nhân Cụ thể:** Người kể chuyện xưng "Tôi" + các chi tiết siêu cụ thể ("bậc thang gỗ thứ ba")
- **Vô danh Phổ quát:** Người quan sát "Ai đó" — người nghe tự liên hệ bản thân vào
- **Góc nhìn Nhân chứng Báo chí:** Quan sát miêu tả như họa sĩ — các cảnh xếp chồng lên nhau mà không gọi tên nhân vật

---

## PHẦN C — TRÍ TUỆ VỀ GIAI ĐIỆU & TÍNH NHẠC (MỚI)

> [!IMPORTANT]
> **Đây là phần quan trọng nhất của phiên bản 6.0.** Lời hay mà giai điệu dở = bài hát dở. Giai điệu hay mà lời trung bình = bài hát vẫn có thể thành hit. GIAI ĐIỆU LÀ VUA.

### C1. Đường cong Giai điệu

Giai điệu không phải ngẫu nhiên — nó có hình dạng, và hình dạng đó tạo ra cảm xúc:

| Hình dạng Giai điệu | Cảm xúc tạo ra | Khi nào dùng |
| :--- | :--- | :--- |
| **Đi lên (Ascending)** | Hy vọng, năng lượng, mở rộng | Pre-Chorus → Chorus, xây dựng cao trào |
| **Đi xuống (Descending)** | Buồn, thư giãn, kết thúc, chấp nhận | Verse, outro, sự giải quyết |
| **Hình vòm (Arch - lên rồi xuống)** | Kể chuyện hoàn chỉnh, trọn vẹn | Các dòng của Verse, bridge |
| **Nhảy quãng rồi bước (Leap then step)** | Bất ngờ, kịch tính, đáng nhớ | Dòng hook, dòng mở đầu chorus |
| **Bằng phẳng (Plateau)** | Căng thẳng, chờ đợi, thôi miên | Pre-chorus, các đoạn nói |
| **Zic-zắc (Zigzag - lên xuống liên tục)** | Tinh nghịch, tràn đầy năng lượng, bồn chồn | Các bài hát nhịp nhanh, các verse năng lượng |

**Quy tắc Đường cong Giai điệu BẮT BUỘC:**
1. **Giai điệu của verse phải THẤP hơn giai điệu của chorus.** Nếu verse đã hát cao → chorus không còn khoảng trống để "bay cao".
2. **Chorus phải có ít nhất 1 cú nhảy quãng giai điệu** — đây là yếu tố tạo ra "khoảnh khắc vỡ òa" (wow moment).
3. **Dòng hook phải chứa nốt CAO NHẤT của bài hát** — đó là lý do nó đọng lại trong tâm trí.
4. **Bridge nên đi vào vùng giai điệu CHƯA TỪNG XUẤT HIỆN** — tạo sự bất ngờ trước Chorus cuối cùng.

### C2. Hook Giai điệu vs Hook Lời bài hát vs Hook Nhịp điệu

**BẮT BUỘC: Mỗi bài hát phải hướng tới (target) ít nhất 2/3 loại hook (đoạn nhạc bắt tai).**

| Loại Hook | Định nghĩa | Cách tạo trong Suno |
| :--- | :--- | :--- |
| **Lyrical Hook** (Hook lời hát) | Cụm từ bắt tai, đáng nhớ (quotable), đọng lại | Viết lời hay, dễ nhớ (memorable), đơn giản |
| **Melodic Hook** (Hook giai điệu) | Chuỗi nốt nhạc bắt tai — người ta lẩm nhẩm (hum) mà không cần nhớ lời | Đặt nguyên âm mở ở nốt cao, tạo bước nhảy giai điệu (melodic leap), để không gian (space) cho Suno tạo vòng cung giai điệu (melody arc) |
| **Rhythmic Hook** (Hook nhịp điệu) | Mẫu nhịp điệu (pattern) đặc trưng — thứ khiến người nghe gõ tay theo | Viết lời (lyrics) theo mẫu nhịp điệu lặp lại, đảo phách (syncopation) |

**Cách viết lời (lyrics) để Suno tạo melodic hook:**
1. **Cho giai điệu (melody) có không gian bay bổng:** Dòng hook cần ≥ 7 từ để giai điệu có đủ nốt tạo vòng cung (arc). Dòng 2-3 từ → giai điệu bị phẳng.
2. **Đặt từ quan trọng nhất ở phách mạnh (beat):** Suno nhấn nốt ở phách 1 và phách 3. Đặt từ cảm xúc nhất vào đó.
3. **Lặp lại mẫu giai điệu (melodic pattern):** Khi 2 dòng điệp khúc (chorus) có cùng số âm tiết (syllable count) và quy luật nhấn âm (stress pattern), Suno sẽ lặp lại giai điệu → tạo ra sự ám ảnh (earworm).
4. **Tạo sự tương phản (contrast):** Nếu giai điệu đoạn verse thấp và đều → điệp khúc (chorus) phải nhảy lên cao và mở rộng.

### C4. Style Prompt — Từ khóa (Keywords) cho Tính nhạc (Musicality)

Ngoài thể loại/nhạc cụ/giọng hát (genre/instrument/vocal), style prompt (câu lệnh phong cách) **phải** chứa các từ khóa điều khiển **chất lượng âm nhạc**:

**Từ khóa cho Chất lượng Giai điệu (Melody Quality - chọn phù hợp):**
`soaring memorable melody` · `catchy singalong chorus` · `earworm hook` · `anthemic melody` · `haunting unforgettable melody` · `hummable tune` · `sweeping melodic lines` · `lyrical flowing melody`

**Từ khóa cho Độ phong phú của Hòa âm (Harmonic Richness - chọn phù hợp):**
`rich emotional chord changes` · `unexpected harmonic shifts` · `bittersweet major-minor transitions` · `lush jazz-influenced harmonies` · `dramatic chord progression` · `emotionally complex chords` · `suspended chords resolving`

**Từ khóa cho Nhịp điệu/Sự nhún nhảy (Groove/Rhythm - chọn phù hợp):**
`infectious groove` · `driving rhythmic pulse` · `syncopated rhythm` · `head-nodding beat` · `foot-tapping groove` · `rolling rhythmic momentum` · `hypnotic pulse` · `body-moving rhythm`

**Từ khóa cho Chất lượng Sản xuất (Production Quality - chọn phù hợp):**
`lush layered production` · `wide stereo soundscape` · `punchy compressed drums` · `warm analog tape saturation` · `crystal clear high fidelity` · `rich textured arrangement` · `cinematic wide-screen production` · `intimate studio quality`

---

## PHẦN D — VÒNG CUNG SỰ BIẾN ĐỔI (DYNAMIC ARC) & PHỐI KHÍ (ARRANGEMENT) (MỚI)

> [!IMPORTANT]
> Bài hát phẳng lỳ = bài hát chết. Mỗi bài PHẢI có hành trình năng lượng (energy journey) rõ ràng — người nghe phải cảm nhận được sự dâng trào, lắng xuống, rồi bùng nổ.

### D1. Bản thiết kế Bản đồ Năng lượng (Energy Map Blueprint)

**BẮT BUỘC:** Mỗi bài hát phải có Bản đồ Năng lượng (Energy Map) được xác định TRƯỚC KHI viết lời.

**Mẫu Bản đồ Năng lượng chuẩn (điều chỉnh theo concept):**

```
Intro (Mở đầu):               ██░░░░░░░░  15-20%  (gợi mở, lôi cuốn sự chú ý)
Verse 1 (Phiên khúc 1):       ███░░░░░░░  25-35%  (kể chuyện, gần gũi/intimate)
Pre-Chorus (Tiền điệp khúc):  █████░░░░░  45-55%  (tăng độ căng thẳng, sự mong đợi)
Chorus 1 (Điệp khúc 1):       ████████░░  75-85%  (giải phóng, bay bổng, tung ra hook)
Verse 2 (Phiên khúc 2):       ████░░░░░░  30-40%  (câu chuyện sâu hơn, năng lượng cao hơn V1 một chút)
Chorus 2 (Điệp khúc 2):       █████████░  80-90%  (lớn hơn C1 — thêm nhạc cụ/bè/cường độ)
Bridge (Đoạn nối):            ███░░░░░░░  25-40%  (tối giản lại, sự yếu đuối, yếu tố bất ngờ)
Final Chorus (Điệp khúc cuối):██████████  95-100% (bung hết tất cả, tác động cảm xúc tối đa)
Outro (Kết thúc):             ██░░░░░░░░  10-20%  (sự giải quyết, tiếng thở, hạ cánh)
```

**Quy tắc Năng lượng Cứng:**
1. **Tỷ lệ Tương phản (Contrast Ratio) ≥ 2x:** Chorus phải có năng lượng tối thiểu **gấp đôi** verse. Nếu verse = 30%, chorus phải ≥ 60%.
2. **Không bao giờ phẳng (Never Flat):** Hai phần liên tiếp **KHÔNG ĐƯỢC** cùng mức năng lượng. Mỗi phần phải khác phần trước/sau ít nhất 15%.
3. **Verse 2 > Verse 1:** Verse 2 luôn phải có chút năng lượng nhiều hơn Verse 1 (thêm 1 nhạc cụ, hoặc giọng hát mạnh hơn chút).
4. **Final Chorus > Chorus 2 > Chorus 1:** Mỗi lần chorus xuất hiện phải LỚN HƠN lần trước.

### D2. Chiến lược Phân lớp Nhạc cụ (Instrumentation Layering Strategy)

Đừng vứt tất cả nhạc cụ vào từ đầu. Phân lớp (layer) thông minh:

| Phần (Section) | Nhạc cụ điển hình | Nguyên tắc |
| :--- | :--- | :--- |
| **Intro** | 1-2 nhạc cụ (guitar/piano + 1 âm sắc/texture) | Thưa thớt (Sparse), gợi mở |
| **Verse 1** | 2-3 nhạc cụ (nền tảng + nhịp điệu nhẹ) | Gần gũi (Intimate), chừa chỗ cho giọng hát |
| **Pre-Chorus** | Thêm 1-2 lớp (bass xuất hiện, dàn dây dâng trào/strings swell) | Xây dựng sự căng thẳng (Building tension) |
| **Chorus 1** | 4-6 nhạc cụ (đầy đủ nhịp + hòa âm + giai điệu chính) | Rộng mở (Wide), mạnh mẽ, nhưng vẫn còn dư địa để phát triển |
| **Verse 2** | 3-4 nhạc cụ (V1 + 1 yếu tố mới) | Phong phú hơn V1 một chút |
| **Chorus 2** | 5-7 nhạc cụ (C1 + hát bè/backing vocals + lớp phụ) | Lớn hơn, dày hơn |
| **Bridge** | 2-3 nhạc cụ (tối giản lại, nhạc cụ khác biệt) | Bất ngờ, dễ tổn thương (vulnerability) |
| **Final Chorus** | Tất cả (dàn nhạc/ban nhạc đầy đủ + dàn đồng ca + hiệu ứng) | Độ bão hòa tối đa (Maximum saturation) |
| **Outro** | 1-2 nhạc cụ (phản chiếu intro hoặc chỉ 1 giọng hát) | Giải quyết (Resolution), khép lại (bookend) |

### D2.5. Giao thức Nhạc cụ Đặc biệt (Special Instrument Protocol) (MỚI — v7.0)

> [!IMPORTANT]
> Mẫu (Pattern) quan sát từ 5 bài viral: **1 nhạc cụ đặc biệt không có từ đầu, chỉ xuất hiện tại 1 đỉnh điểm cảm xúc (emotional peak) duy nhất** → tạo "dấu ấn cảm xúc" (emotional timestamp) mạnh nhất của bài. Đây không phải phân lớp nhạc cụ thông thường — đây là cột mốc cảm xúc.

**Quy tắc:**
1. Mỗi bài chỉ có **tối đa 1** Nhạc cụ Đặc biệt (Special Instrument)
2. Nhạc cụ này **KHÔNG xuất hiện** trong Intro, V1, V2
3. Chỉ xuất hiện (enter) tại **1 điểm duy nhất** — Chorus, Bridge, hoặc Outro — tùy Chế độ Cảm xúc (Emotional Mode)
4. Khi xuất hiện: phải được ghi chú rõ trong style prompt (thành phần thứ 8) VÀ trong thẻ `[]` của lyrics

**Menu Nhạc cụ Đặc biệt (chọn 1):**

| Nhạc cụ (Instrument) | Phẩm chất cảm xúc (Emotional quality) | Xuất hiện tại | Phù hợp Mode |
| :--- | :--- | :--- | :--- |
| **Piano** (rải ngón âm vực cao / high-register arpeggios) | Hy vọng, nâng tầm, giải quyết | Chorus hoặc Outro | A, C |
| **Glockenspiel** (Đàn phiến kim loại) | Phép màu, sự kỳ diệu, như trẻ thơ | Post-Chorus | B |
| **Cello** (Đàn hồ cầm) | Nỗi đau sâu sắc, sự gần gũi, sự ấm áp | Chorus | D |
| **String pads** (Dàn dây ngân dài) | Sự vĩ đại, dâng trào cảm xúc | Bridge | A, B, D |
| **Second acoustic guitar** (Guitar thùng thứ hai - chạy nốt lấp trống / melodic fills) | Sự đồng hành, đối thoại | Từ V2 trở đi | A, B |
| **Clean electric** (Guitar điện tiếng mộc - dâng trào không gian / ambient swells) | Khoảng cách, ký ức, sự mong mỏi | Xuyên suốt nhưng tinh tế | A, C |

**Cách viết vào Style Prompt (Thành phần 8 mới):**
```
[Component 8 — Special Instrument]
A [cello/piano/glockenspiel] enters only at [section], providing [emotional description].
Ví dụ: "A solo cello enters only at the chorus, providing deep melodic counterpoint and emotional warmth."
```

**Cách viết vào Lời (Lyrics):**
```
[Chorus]
[cello enters]
The faded blue blanket is warm in the night...
```

### D3. Nghệ thuật Tương phản — 7 Loại Tương phản (The Art of Contrast)

Mỗi bài hát phải sử dụng **ít nhất 3/7 loại tương phản** sau:

1. **Tương phản âm lượng (Volume contrast):** Verse nhỏ nhẹ (Quiet verse) → chorus lớn tiếng (loud chorus)
2. **Tương phản mật độ (Density contrast):** Nhạc cụ thưa thớt (Sparse instrumentation) → âm thanh phân lớp dày đặc (dense layered sound)
3. **Tương phản nhịp điệu (Rhythmic contrast):** Verse nhịp tự do/chậm (Slow rubato verse) → chorus nhịp điệu dồn dập (driving rhythmic chorus)
4. **Tương phản âm vực (Register contrast):** Verse hát ở quãng trầm (Low vocal range verse) → chorus bay bổng ở quãng cao (high soaring chorus)
5. **Tương phản âm sắc/không gian (Texture contrast):** Thu âm khô/gần (Dry close-mic) → không gian vang dội, ướt át (wet spacious reverb)
6. **Tương phản điệu thức (Tonal contrast):** Verse giọng thứ/tối (Minor/dark verse) → chorus giọng trưởng/sáng (major/bright chorus) (hoặc ngược lại)
7. **Tương phản giọng hát (Vocal contrast):** Giọng hát solo (Solo voice) → Dàn đồng ca/hát bè đầy đủ (full choir/harmonies)

---

## PHẦN E — LÀM CHỦ NHỊP ĐIỆU & SỰ NHÚN NHẢY (GROOVE & RHYTHM MASTERY) (MỚI)

> Groove là thứ khiến người nghe GÕ TAY, LẮC ĐẦU, PHIÊU THEO. Không có groove = nhạc nền, không phải bài hát.

### E1. Các mẫu Cảm giác Nhịp điệu (Rhythmic Feel Templates)

Chọn cảm giác nhịp điệu (rhythmic feel) phù hợp concept:

| Cảm giác Nhịp điệu (Rhythmic Feel) | Đặc tính | Phù hợp concept |
| :--- | :--- | :--- |
| **Straight 4/4** (Nhịp 4/4 đều) | Ổn định, vững chãi, mạnh mẽ | Rock, pop, nhạc hùng ca (anthemic) |
| **Swung/Shuffle** (Nhịp nảy) | Bluesy, thư giãn, ấm áp | Blues, jazz, soul, country |
| **Rolling 6/8** (Nhịp 6/8 cuộn trào) | Sóng nước, waltz, trôi chảy | Celtic, nhạc đại dương, đồng quê (pastoral) |
| **Syncopated** (Đảo phách) | Lệch phách (off-beat), bất ngờ, bắt tai (groovy) | R&B, funk, modern folk-pop |
| **March/Military** (Nhịp hành khúc) | Kiên định, sử thi, tiến về phía trước | Điện ảnh (Cinematic), hùng ca, câu chuyện chiến tranh |
| **Rubato/Free** (Nhịp tự do) | Bồng bềnh, như giấc mơ, gần gũi | Art songs, đọc thơ (spoken word), các đoạn bridge |
| **Driving 8th notes** (Nốt móc đơn dồn dập) | Khẩn trương, không ngừng nghỉ, dâng trào | Post-rock, indie, các phần build-up |
| **Waltz 3/4** (Nhịp điệu Valse 3/4) | Thanh lịch, hoài niệm, khiêu vũ | Châu Âu, thế giới cũ, lãng mạn |
| **Reggae/Half-time** (Nhịp giảm nửa) | Thong thả, không gian rộng, ấm áp | Câu chuyện đảo nhiệt đới, cảm giác thư giãn |

### E2. Chiến lược Bộ gõ (Percussion Strategy)

Bộ gõ không chỉ là "brush snare" hay "bodhrán." Nó phải THÚC ĐẨY (DRIVE) bài hát:

**Thẻ phong cách (Style tags) cho bộ gõ:**
*   Tinh tế (Subtle): `soft brushed snare`, `gentle finger percussion`, `light hand claps`
*   Trung bình (Medium): `steady rim clicks`, `warm kick drum`, `brushed hi-hat groove`
*   Dồn dập (Driving): `driving drum groove`, `punchy kick and snare`, `relentless bodhrán beat`
*   Sử thi (Epic): `thundering tribal drums`, `massive cinematic percussion`, `pounding floor toms`

### E3. Cách viết Lời (Lyrics) tạo Groove

Lời hát **tự chúng nó** có nhịp. Chọn từ và sắp xếp từ đúng cách → Suno sẽ tạo groove tự nhiên:

1. **Tính nhất quán của quy luật nhấn âm (Stress pattern consistency):** Giữ cùng một mẫu nhấn âm qua nhiều dòng.
   *   ✅ `The WINdow KNOWS your SHAPE` / `The GARden KEEPS your NAME` (da-DA-da-DA-da-DA)
   *   ❌ `Window shape` / `The old garden still remembers keeping names` (không có quy luật)

2. **Lựa chọn từ có tính gõ (Percussive word choice):** Dùng từ có phụ âm mạnh khi cần thúc đẩy (drive).
   *   Từ mạnh: *break, kick, tap, crack, click, stomp, clap, beat, cut, strike*
   *   Từ mềm: *flow, sway, melt, hum, breathe, drift, float, sweep*

3. **Lặp lại nhịp điệu (Rhythmic repetition):** Lặp cùng một motif nhịp điệu để tạo groove.
   *   `Brick by brick, the wall came down` → `Stone by stone, the road was found` (cùng mẫu/pattern)

---

## PHẦN F — KIỂM SOÁT KỸ THUẬT SUNO (SUNO TECHNICAL CONTROL)

### F1. Style Prompt — Quy tắc & Công thức

Style prompt **chỉ mô tả âm nhạc** (không kể video/story).

**Quy chuẩn mới (Suno Native Format):**
Không dùng các thẻ tags rời rạc (cách nhau bằng dấu phẩy). Hãy viết thành các **câu văn xuôi hoàn chỉnh (Natural Language)**, tập trung 100% vào chuyên môn âm nhạc (musicology). Phân tích cấu trúc chuẩn của Suno gồm **8 thành phần** (thành phần 8 là mới từ v7.0):

1. **Thể loại & Các yếu tố cốt lõi (Genre & Core Elements):** Liệt kê thể loại, các nhạc cụ chính và loại giọng hát. (VD: *Indie folk ballad, Acoustic guitar, upright bass, drums, piano, and male vocals,*)
2. **Nhịp điệu & Nền tảng nhịp (Tempo & Rhythm Foundation):** Chỉ định nhịp điệu, Số chỉ nhịp (Time signature), BPM và Tông (Key) thông qua một nhạc cụ giữ nhịp chính. (VD: *The acoustic guitar plays a steady fingerstyle pattern in 4/4 time at 82 BPM in the key of G major,*)
3. **Bass / Dải âm trầm (Bass / Lower Register):** Mô tả hành vi và âm sắc của dải trầm. (VD: *The upright bass provides melodic counterpoint with a warm, woody tone,*)
4. **Chi tiết bộ gõ (Percussion Details):** Chi tiết hóa bộ gõ. (VD: *Drums feature a light, shuffling snare played with brushes and a soft kick on beats 1 and 3,*)
5. **Nhạc cụ hòa âm/màu sắc (Harmonic/Color Instruments):** Mô tả cách các nhạc cụ giai điệu/hòa âm hoạt động. (VD: *A clean piano enters with sparse, high-register chords,*)
6. **Phần thể hiện giọng hát & Bè phối (Vocal Performance & Harmonies):** Mô tả âm sắc giọng hát chính và cách bè. (VD: *The male lead vocal is intimate and breathy, occasionally layering into three-part folk harmonies during the chorus,*)
7. **Tổng thể bản phối/Cường độ (Overall Arrangement/Dynamics):** Mô tả tổng thể bản phối. (VD: *The arrangement is organic and dynamic, with instruments entering and exiting to build texture.*)
8. **Sự xuất hiện của nhạc cụ đặc biệt (Special Instrument Entry - MỚI v7.0):** *[Tùy chọn nhưng ĐƯỢC KHUYẾN NGHỊ MẠNH MẼ cho thể loại folk]* Mô tả 1 nhạc cụ duy nhất tham gia vào muộn để đánh dấu đỉnh điểm cảm xúc. (VD: *A solo cello enters only at the chorus, providing deep melodic warmth and emotional counterpoint.* HOẶC *A piano enters only in the final outro, signaling the pivot from grief to hope.*)

**Công thức tổng quát:**
Viết thành một đoạn văn (khoảng 500-800 ký tự) nối tiếp nhau mô tả lần lượt 7-8 yếu tố trên.

**Ví dụ Câu lệnh Phong cách v7.0 (Style Prompt - Định dạng gốc của Suno — với thành phần thứ 8):**
```
Indie folk ballad, Acoustic guitar, upright bass, drums, piano, and male vocals, The acoustic guitar plays a steady fingerstyle pattern in 4/4 time at 82 BPM in the key of G major, The upright bass provides melodic counterpoint with a warm, woody tone, Drums feature a light, shuffling snare played with brushes and a soft kick on beats 1 and 3, A clean piano enters with sparse, high-register chords, The male lead vocal is intimate and breathy, occasionally layering into three-part folk harmonies during the chorus, The arrangement is organic and dynamic, with instruments entering and exiting to build texture, A solo cello enters only at the final chorus, providing deep melodic warmth as the emotional peak.
```

### F2. Tính cách giọng hát & Mô típ âm thanh đặc trưng (Vocal Persona & Signature Sound Motif)

*   **Tính cách giọng hát (Vocal Persona):** Xây dựng **nhân cách giọng hát** cụ thể. Tránh giọng pop teen, gào thét (belting) cực đoan, hoặc giọng robot.
    *   *Ví dụ tốt:* mature male baritone with a warm, weathered tone; older male storyteller vocal, sincere and close-mic'd; gentle female alto (intimate and nostalgic); old-radio crooner voice; crystalline soprano layered in harmony.
*   **Mô típ âm thanh đặc trưng (Signature Sound Motif):** Khi phù hợp, thêm 1 âm thanh đặc trưng tinh tế.
    *   *Ví dụ:* tiếng leng keng của cốc cà phê (coffee cup ping), tiếng đồng hồ cũ tích tắc (old clock tick), tiếng sột soạt của giấy (paper rustle), tiếng kéo ghế gỗ (wooden chair scrape), tiếng chuông nhà thờ nhẹ nhàng (soft church bell), tiếng cọt kẹt của cửa lưới từ xa (distant screen door creak), tiếng gió thổi qua lá trong vườn (wind through garden leaves), tiếng sóng biển vỗ (ocean wave crash), tiếng búa đập vào đe (hammer on anvil), tiếng lách cách của máy đánh chữ (typewriter click).

### F3. LỜI BÀI HÁT LÀ YẾU TỐ ĐIỀU KHIỂN CHÍNH (LYRICS LÀ CẦN GẠT SỐ 1)

> [!IMPORTANT]
> Câu lệnh Phong cách (Style Prompt) chỉ định hình "khung cảnh" (thể loại, tâm trạng, giọng hát). **Lời bài hát (Lyrics)** mới là thứ quyết định **100% cách Suno hát**: nhịp nhanh hay chậm, nhấn vào từ nào, ngắt hơi ở đâu, bè phối ra sao, cảm xúc như thế nào.

#### Bảng tra cứu nhanh: "Muốn X → Làm Y trong Lời bài hát"

| Muốn đạt hiệu ứng gì? | Kỹ thuật trong Lời bài hát | Ví dụ |
| :--- | :--- | :--- |
| **Hát chậm lại, nhấn từng từ** | Tách dòng ngắn (5-7 từ/dòng) + dấu ba chấm | `The old road... still remembers` |
| **Hát nhanh, dồn dập** | Gộp dòng dài liền mạch (10-14 từ) | `The house and all its memories are thrive under my restless care` |
| **Tạo nhịp thở, ngập ngừng** | Dấu ba chấm `...` | `I almost called your name...` |
| **Nhấn mạnh 1 từ cảm xúc** | VIẾT HOA chỉ 1 từ | `I am STILL here` |
| **Kéo dài ngân giọng** | Lặp nguyên âm cuối từ | `mineeeee`, `hoooome` |
| **Thêm bè nhẹ / vọng lại** | Ngoặc đơn `()` | `The garden kept your name (kept your name)` |
| **Giọng nghẹn ngào** | Thẻ cảm xúc `[]` trước dòng | `[crying voice]` |
| **Tiếng thở** | Thẻ nhịp thở (Breath tag) `[]` | `[sigh]`, `[deep breath]` |
| **Chuyển giọng (song ca)** | Thẻ tên nhân vật `[]` | `[John]` ... `[Jane]` ... `[Both]` |
| **Solo nhạc cụ** | Thẻ nhạc cụ trên dòng riêng | `[instrumental break, saxophone]` |
| **Đổi nhịp điệu (rhythm)** | Thay đổi kiểu khoảng cách (spacing) giữa các đoạn | Verse: dòng dài → Chorus: dòng ngắn hơn, nhịp điệu rõ ràng hơn |
| **Đặc tả phong cách đoạn nhạc** | Dấu hai chấm `:` trong `[]` | `[Bridge: haunting, slow, cello only]` |
| **Hát ngẫu hứng (Ad-lib) / tiếng đệm** | `()` với nguyên âm | `(Ohhh-ohhh)`, `(Mmm-hmm)` |

#### Quy tắc Đánh dấu (Markup) tuyệt đối

*   `()` = hát lót (backing vocals), hát ngẫu hứng (ad-libs), tiếng ngân nga (hums). **KHÔNG** để trống toàn bài — thiếu `()` = bài hát phẳng lỳ.
*   `[]` = thẻ cấu trúc (structural tags) + thẻ biểu diễn (performance tags). **KHÔNG** viết chỉ dẫn quá mơ hồ.
*   **KHÔNG** dùng `{}` hoặc `<>`.

#### Quy tắc Khoảng cách (Spacing) & Dấu câu — BẮT BUỘC

*   **Dấu phẩy `,`** = hát liền, cùng nhóm nhạc.
*   **Dấu chấm `.`** = kết thúc ý, ngắt hơi rõ ràng.
*   **Dòng trống** giữa 2 đoạn = Suno tự động thay đổi nhịp/beat.

> [!WARNING]
> **Thiếu thay đổi về khoảng cách = bài hát phẳng lỳ, đều đều (monotone) từ đầu đến cuối.** Mỗi bài hát BẮT BUỘC phải có ít nhất 2-3 kiểu khoảng cách khác nhau giữa các phân đoạn.

### F4. Nhịp thơ, Trọng âm & Khả năng hát (Singability) — Quy tắc Độ dài Dòng (CẬP NHẬT)

> [!IMPORTANT]
> **Thay đổi lớn so với v5.0:** Bỏ quy tắc câu Verse 2-3 từ/dòng. Dòng quá ngắn sẽ phá hỏng giai điệu (melody).

**Quy tắc Độ dài Dòng BẮT BUỘC:**

| Phân đoạn (Section) | Số từ/dòng | Lý do |
| :--- | :--- | :--- |
| **Verse** | **5-10 từ** (trung bình 7) | Đủ dài để giai điệu phát triển vòng cung, đủ ngắn để tạo sự gần gũi (intimate) |
| **Pre-Chorus** | **6-12 từ** (trung bình 8) | Dài hơn một chút để tạo đà (momentum building) |
| **Chorus** | **6-10 từ** (trung bình 8) | Đủ dài cho phần điệp khúc bắt tai (melodic hook), đủ ngắn để dễ nhớ (memorable) |
| **Bridge** | **5-10 từ** (tự do hơn) | Được phép đổi cấu trúc (pattern) hoàn toàn |
| **Hook line (Dòng chủ đạo)** | **≥ 7 từ** | BẮT BUỘC: giai điệu cần đủ nốt để tạo vòng cung gây nghiện (earworm arc) |

**Các dòng điệp khúc (chorus) song song phải có số âm tiết và mẫu trọng âm tương đương:**

| ❌ Nhịp điệu tệ (Suno sẽ vấp) | ✅ Nhịp điệu tốt (Suno hát mượt) |
| :--- | :--- |
| *I looked at the old photo on the wooden table and cried* (14 âm tiết) | *The dusty photo whispers from the floor* (8 âm tiết) |
| *Cold* (1 âm tiết) | *The fading light behind the door* (8 âm tiết) |

**Nguyên tắc "Xen kẽ Dài-Ngắn" (Long-Short Alternation):**
Xen kẽ dòng dài và dòng ngắn hơn trong verse để tạo nhịp thở tự nhiên. Không phải tất cả dòng cùng độ dài.

```
The morning caught your cup again          (8 âm tiết — dài)
a circle where the coffee dried            (8 âm tiết — dài)
I traced the rim                           (4 âm tiết — ngắn, lấy hơi)
and felt your hand still warm              (6 âm tiết — trung bình, giải quyết)
```

**Nguyên tắc "Breathing Room" (Khoảng không để thở):**
Cứ mỗi 4-6 dòng trong verse nên có 1 dòng ngắn hơn, hoặc theo sau bởi `[instrumental fill]`.

**Quy tắc Độ mở của Nguyên âm (Vowel Openness Rule - BẮT BUỘC — mới v8.0):**

Nốt cao của giai điệu (cao trào của dòng, cuối đoạn điệp khúc) PHẢI rơi vào nguyên âm MỞ (Open vowel). Nếu rơi vào nguyên âm ĐÓNG → Suno hát sẽ bị gắt, nghẹt giọng, mất cảm xúc.

| Loại | Nguyên âm | Âm thanh | Dùng ở nốt cao? |
|---|---|---|---|
| **Mở (open)** | AH, OH, AY, OW, AW | Vang xa, dễ kéo dài | ✅ TỐT NHẤT |
| **Nửa mở** | EH, UH, EE, OO | Được, nhưng kém hơn | ⚠ CHỈ DÙNG NẾU CẦN |
| **ĐÓNG (closed)** | IH, IM, IN, IT, IG, -NK | Nghẹn, bị ngắt | ❌ TRÁNH Ở NỐT CAO |

**Ví dụ:**
```
❌  "I still think of him"    → nốt cao rơi vào "him" (đóng -IM) → Suno ngắt nghẹn
✅  "I still call his name"   → nốt cao rơi vào "name" (mở AY) → Suno kéo dài vang vọng

❌  "the garden in the dark" → nốt cao rơi vào "dark" (đóng -RK) → Suno bị nghẹt giọng
✅  "the garden full of light" → nốt cao rơi vào "light" (mở AY/I) → bay bổng
```

**Tự kiểm tra khả năng hát (Singability Self-Test - chạy trước khi gửi đi):**

Hát thử từng dòng chorus theo giai điệu dự định. Đánh dấu bất kỳ chỗ nào:

```
☐ Miệng cảm giác gượng ép khi hát → cụm phụ âm (consonant cluster) quá dày (VD: "strengths", "sixths")
☐ Giọng bị ép xuống cuối dòng → nguyên âm đóng, đổi sang từ có nguyên âm mở
☐ Phải ngắt hơi giữa chừng mà không có dấu câu nào → dòng quá dài, cần cắt ngắn
☐ Đoạn nào khó nhớ sau 1 lần đọc → không có điểm neo nhịp điệu (rhythmic anchor), viết lại
☐ Hai dòng liền có cùng điểm ngắt hơi (cùng số âm tiết và cùng nguyên âm) → đều đều (monotone), đổi 1 trong 2
```

> [!CAUTION]
> Nếu bất kỳ ô nào bị đánh dấu → phải sửa trước khi tiếp tục. Không gửi lời bài hát chưa qua Kiểm tra Khả năng hát (Singability Test) cho Suno.

### F5. Quy tắc Gieo vần (Rhyme Rules) — Chống máy móc (Anti-Mechanical)

> [!IMPORTANT]
> **VẦN = ÂM THANH, KHÔNG PHẢI CHỮ VIẾT**
> Đây là nguyên tắc nền tảng. AI hay nhầm vần theo mắt (cùng chữ cuối) thay vì vần theo tai (cùng âm cuối). Khi hát, người nghe nghe âm — không đọc chữ.

**Định nghĩa đúng của vần:**
Hai từ vần với nhau khi **âm nguyên âm nhấn + mọi thứ sau đó** nghe giống nhau.

```
"rain" / "pain"   → cùng âm /AYN/  → ✅ vần
"love" / "move"   → tận -ove giống nhau NHƯNG âm khác (/ʌV/ vs /uːV/) → ❌ KHÔNG vần
"home" / "alone"  → âm /OHM/ vs /OHN/ — gần giống → ✅ vần gần (near rhyme)
"light" / "write" → âm /AYT/ vs /AYT/ → ✅ vần (dù chữ khác hoàn toàn)
"word"  / "heard" → âm /ɜːRD/ vs /ɜːRD/ → ✅ vần (dù cách đánh vần khác)
```

**Bẫy phổ biến nhất của AI khi viết lời bài hát:**

| Cặp từ | Nhìn thì vần? | Nghe thì vần? | Ghi chú |
|---|---|---|---|
| `love / move` | ✅ (cùng -ove) | ❌ | Âm khác nhau: /ʌv/ vs /uːv/ |
| `blood / food` | ✅ (cùng -ood) | ❌ | Âm khác nhau: /ʌd/ vs /uːd/ |
| `word / lord` | ❌ (chữ khác) | ✅ | Âm giống nhau: /ɜːrd/ ≈ /ɔːrd/ (vần gần) |
| `night / white` | ❌ (chữ khác) | ✅ | Âm giống nhau: /AYT/ = /AYT/ |
| `said / dead` | ❌ (chữ khác) | ✅ | Âm giống nhau: /ɛd/ = /ɛd/ |
| `gone / bone` | ✅ (cùng -one) | ❌ | Âm khác nhau: /ɒn/ vs /oʊn/ |

**Cách AI kiểm tra vần — So sánh IPA:**
Với mỗi cặp từ nghi ngờ, tra ngữ âm IPA của cả 2 từ, sau đó so sánh **phần từ nguyên âm nhấn trở về sau**:

```
Bước 1: Xác định nguyên âm nhấn của mỗi từ
Bước 2: Lấy âm từ đó đến hết từ (ký hiệu IPA)
Bước 3: So sánh 2 chuỗi âm đó

→ Giống nhau hoàn toàn = vần hoàn hảo (perfect rhyme)
→ Gần giống (cùng nguyên âm, khác phụ âm cuối 1 chút) = vần gần (near rhyme)
→ Khác = KHÔNG vần, dù chữ viết trông giống nhau
```

**Ví dụ áp dụng:**
```
"love"  → IPA: /lʌv/ → phần vần: /ʌv/
"move"  → IPA: /muːv/ → phần vần: /uːv/
→ /ʌv/ ≠ /uːv/ → KHÔNG vần ❌

"light" → IPA: /laɪt/ → phần vần: /aɪt/
"write" → IPA: /raɪt/ → phần vần: /aɪt/
→ /aɪt/ = /aɪt/ → VẦN ✅

"stone" → IPA: /stoʊn/ → phần vần: /oʊn/
"road"  → IPA: /roʊd/ → phần vần: /oʊd/
→ /oʊn/ ≈ /oʊd/ (cùng nguyên âm, khác phụ âm cuối) → VẦN GẦN (NEAR RHYME) ✅
```

---

Trộn lẫn **vần chính xác** với **vần gần đúng** để tránh cảm giác thơ trẻ con.

*   **Vần gần (Near Rhymes):** *home / alone*, *stone / road*, *wind / skin*, *rise / light* — âm cuối gần giống nhau, không đồng nhất hoàn toàn.
*   **Vần trong dòng (Internal Rhyming):** *The **cup** was chipped, the tea was **hot**, I sat upon the porch and **thought*** — vần xuất hiện giữa dòng, không chỉ cuối dòng.

**Bản đồ Cấu trúc Gieo vần (Rhyme Scheme Map - BẮT BUỘC chọn trước khi viết):**

Không viết thiếu cấu trúc (scheme). Chọn 1 cấu trúc cho Verse và 1 cấu trúc cho Chorus trước, rồi viết dựa theo đó.

| Cấu trúc (Scheme) | Hình mẫu (Pattern) | Cảm giác | Dùng khi nào |
|---|---|---|---|
| **ABAB** | dòng 1↔dòng 3, dòng 2↔dòng 4 | Cân bằng, folk cổ điển | Verse có 4 dòng, tính tự sự rõ ràng |
| **ABCB** | chỉ dòng 2↔dòng 4 vần, dòng 1&3 tự do | Tự nhiên, không gượng | Mặc định cho verse (dễ viết nhất, ít máy móc nhất) |
| **AABB** | cặp dòng vần liền nhau | Vui, dứt khoát | Chorus nghe trực tiếp, câu hook bắt tai |
| **AAAA** | tất cả cùng vần | Mạnh, ám ảnh | Bridge nhấn mạnh, lặp vần (dùng tiết kiệm) |
| **ABA** (3 dòng) | dòng 1↔dòng 3, dòng 2 tự do | Lấp lửng, hé mở | Pre-chorus ngắn, cầu nối cảm xúc |
| **Không vần** | không vần chút nào | Thơ tự do, đọc thơ (spoken-word) | Bridge nội tâm rất sâu, phải đặc biệt có chủ ý |

**Quy tắc phối cấu trúc (scheme):**
- Verse (Phiên khúc): dùng ABCB (tự nhiên) hoặc ABAB (cân bằng)
- Chorus (Điệp khúc): dùng AABB hoặc ABAB — nếu chorus là 4 dòng
- Bridge (Đoạn chuyển): thường ABA hoặc không vần hẳn
- **Không đổi cấu trúc giữa Chorus 1 và Chorus 2** — bị mất cảm giác quen thuộc

**Quy tắc Hạ cánh Phụ âm (Consonant Landing Rule) (BẮT BUỘC — mới v8.0):**

Suno xử lý phụ âm cuối dòng khác nhau. Nếu dòng kết bằng phụ âm cứng (hard stop) → Suno cắt đứt, mất vần khi nghe dù văn bản trông có vần.

| Phụ âm cuối | Loại | Nhận xét | Dùng cuối dòng vần? |
|---|---|---|---|
| -N, -M, -L, -NG | Âm mũi/âm lỏng mềm (Soft nasal/liquid) | Vang rơi, Suno kéo ra được | ✅ TỐT |
| -R | Âm lỏng (Liquid - US English) | Mờ, giai điệu vẫn được | ✅ ĐƯỢC |
| -D, -Z, -V | Âm ngắt mềm (Soft stop) | Chấp nhận được | ⚠️ OK |
| **-T, -K, -P, -CK** | Âm ngắt cứng (Hard stop) | Cắt đứt giai điệu (melody) | ❌ HẠN CHẾ CUỐI DÒNG VẦN |
| **-ST, -XT, -NK, -ND** | Cụm phụ âm (Cluster) | Ngắt giọng, mất vang | ❌ KHÔNG DÙNG CUỐI DÒNG |

**Ví dụ:**
```
❌  "...the porch in the dark"  → cuối -RK = hard (cứng), Suno cắt đứt
✅  "...the porch in the rain"  → cuối -N = nasal (âm mũi), Suno vang rơi tự nhiên

❌  "...we built"              → cuối -LT = cluster (cụm phụ âm), gượng
✅  "...we made"              → cuối -D = soft (mềm), mượt hơn
```

**Bài kiểm tra Chống vần máy móc (Anti-Mechanical Rhyme Test) (BẮT BUỘC):**
1.  Đọc to chorus — đoán được 100% từ vần tiếp theo → quá máy móc, sửa lại.
2.  >60% là vần hoàn hảo (perfect rhymes) → bẻ một nửa sang vần gần giống (near rhymes).
3.  Từ đó được chọn CHỈ VÌ nó vần? → Xóa và viết lại.
4.  Cùng cặp vần xuất hiện ở cả Verse và Chorus? → Đổi một bên.

### F6. Quy tắc Hook & Chorus (CẬP NHẬT)

**Tiêu chí Hook (đã mở rộng):**
*   **Về lời (Lyrical):** Dễ hát, bắt tai (sticky), chứa đựng cảm xúc, dễ trích dẫn, độc đáo.
*   **Về giai điệu (Melodic):** Có bước nhảy giai điệu (melodic leap) hoặc đường nét (contour) đặc biệt, nguyên âm mở ở nốt cao.
*   **Về nhịp điệu (Rhythmic):** Có mẫu nhịp điệu (rhythmic pattern) bắt tai, đảo phách (syncopation), hoặc mẫu lặp lại.

**Vị trí đặt Hook:** Dòng đầu chorus, dòng cuối chorus, hoặc cả hai. Có thể vang nhẹ trong outro.

**Quy tắc Chorus — KHÔNG LẶP NGUYÊN SI (CẬP NHẬT QUAN TRỌNG):**

> [!WARNING]
> **Chorus KHÔNG ĐƯỢC lặp nguyên si quá 2 lần.** Mỗi lần chorus xuất hiện lại phải thay đổi ≥ 1 trong các yếu tố sau:

| Lần lặp | Thay đổi bắt buộc |
| :--- | :--- |
| **Chorus 1** | Cơ bản (Baseline) — lời, phối khí (arrangement), cường độ (intensity) gốc |
| **Chorus 2** | Thay ≥ 1: (a) 1-2 dòng lyrics mới, HOẶC (b) thêm nhạc cụ/bè, HOẶC (c) tăng cường độ giọng hát (vocal intensity) |
| **Final Chorus (Chorus cuối)** | Thay ≥ 2: (a) 2-4 dòng lyrics sâu hơn, VÀ (b) phối khí đầy đủ nhất, VÀ/HOẶC (c) lên tông/chuyển điệu (key change/modulation), VÀ/HOẶC (d) giọng hát đạt đỉnh điểm cảm xúc (emotional peak vocal) |

### F6.5. Học thuyết Chống lặp lại (Anti-Repetition Doctrine) — Không Lặp Lại Lời Nguyên Si

> [!IMPORTANT]
> **Lặp lại lời nguyên si = Kẻ hủy diệt tỷ lệ giữ chân (retention killer).** Người nghe 45+ nhận ra ngay khi bài hát "tái chế" chính nó. Một khi họ cảm thấy "đã nghe rồi" → họ bỏ qua, bỏ qua (skip), hoặc rời đi. Quy tắc này áp dụng cho **toàn bộ bài hát**, không chỉ chorus.

#### Quy tắc tổng quát: Mỗi lần lặp = phải trả giá bằng 1 thay đổi

Bất kỳ phân đoạn (section) nào xuất hiện lần 2 trở đi **BẮT BUỘC phải khác** phiên bản đầu tiên theo ít nhất 1 trong các cách sau:

| Cách thay đổi | Ví dụ cụ thể |
|---|---|
| **Thay ≥ 1 dòng lyrics** | Verse 2 giữ melody nhưng đổi hình ảnh, đổi vật thể, đổi góc nhìn |
| **Thay sắc thái cảm xúc (emotional register)** | Verse 1 hát như hỏi → Verse 2 hát như nhớ lại / chấp nhận |
| **Thay góc nhìn (perspective)** | Từ "tôi" sang "anh/cô ấy" hoặc "chúng ta" |
| **Thay thời gian** | Verse 1 = hiện tại → Verse 2 = quá khứ cụ thể |
| **Thay 1 chi tiết giác quan trọng tâm** | Verse 1: mùi cà phê → Verse 2: tiếng ghế kéo |
| **Thay 1 vật thể (object)** | Verse 1: chiếc cốc → Verse 2: chiếc áo khoác trên móc |

#### Bảng quy tắc chi tiết theo phân đoạn (section)

| Phân đoạn | Quy tắc |
|---|---|
| **Verse 1 → Verse 2** | **KHÔNG được lặp nguyên bất kỳ dòng nào**. Phải thay ≥ 50% số dòng bằng hình ảnh/góc nhìn mới. Verse 2 phải đào sâu hơn câu chuyện, không phải kể lại. |
| **Pre-Chorus 1 → Pre-Chorus 2** | Có thể giữ cùng cấu trúc (structure), nhưng phải thay ≥ 1 dòng cuối để tạo cảm giác leo thang (escalation). |
| **Chorus 1 → Chorus 2 → Final Chorus** | Xem F6 — mỗi lần phải thay ≥ 1 yếu tố, Final Chorus thay ≥ 2. |
| **Giọng hát bè (Backing vocals) `()`** | Cùng 1 cụm backing vocal không được xuất hiện quá 3 lần nguyên si trong cả bài. Xoay vòng giữa `(ohhh)`, `(mmm-hmm)`, `(yeah)`, hoặc bè theo hook. |
| **Bridge** | **KHÔNG BAO GIỜ** lặp lại nội dung đã có ở Verse hoặc Chorus. Bridge phải mở ra góc nhìn mới hoặc khoảnh khắc (moment) của sự thay đổi nội tâm. |

#### Cách viết Verse 2 không lặp (quan trọng nhất)

Verse 2 là nơi bài hát dễ "lười" nhất. Hai cách sai phổ biến:
- ❌ **Lặp nguyên**: Copy Verse 1, chỉ đổi 1-2 từ.
- ❌ **Diễn giải lại (Paraphrase)**: Nói lại cùng ý bằng từ khác. Người nghe vẫn cảm thấy "đã nghe rồi."

Verse 2 đúng phải:
- ✅ **Phóng to (Zoom in)** — Verse 1 thấy ngôi nhà → Verse 2 thấy cụ thể góc bếp, chiếc ghế, đôi tay.
- ✅ **Lật ngược thời gian (Flip time)** — Verse 1 = hôm nay → Verse 2 = ngày xưa cụ thể.
- ✅ **Nhân chứng mới (New witness)** — Verse 1 = tôi nhớ → Verse 2 = căn phòng nhớ thay cho tôi.
- ✅ **Thêm cái giá phải trả (Add cost)** — Verse 1 = mô tả sự vắng mặt → Verse 2 = mô tả hậu quả của sự vắng mặt đó.

#### Quy tắc Tác động Giữ chân (Retention Impact Rule)

> Người nghe trung bình (45+) trên YouTube quyết định ở lại hay rời đi trong **40–90 giây đầu** và tại **mỗi điểm lặp lại**. Bất kỳ lần nào họ cảm thấy "bài này đang lặp lại rồi" → xác suất thoát (drop-off) tăng 30–50%.

---

### F7. Thư viện Cấu trúc Bài hát (Song Structure Library) (CẬP NHẬT v7.0)

**BƯỚC 0 — Lựa chọn Phạm vi Thời gian (Time Scope Selection) (MỚI):** Xác định khung thời gian câu chuyện TRƯỚC KHI chọn cấu trúc.

| Phạm vi Thời gian | Mô tả | Ảnh hưởng đến cấu trúc |
| :--- | :--- | :--- |
| **Khoảnh khắc đơn (Single Moment)** | Một khoảnh khắc duy nhất (buổi sáng, một buổi chiều) | Verse đi sâu vào chi tiết, không cần nhiều verses |
| **Chuỗi sự kiện một ngày (Single Day Arc)** | Từ sáng đến tối — 3 chorus = 3 mốc thời gian | Lời Chorus phải tiến triển (evolve) theo thời gian (xem Evolving Chorus) |
| **Phổ quát "Bất kỳ lúc nào" (Universal "Any Moment")** | Không gắn thời điểm cụ thể — luôn luôn đúng | Hook phải neo (anchor) bằng 1 vật thể/sự thật phổ quát |
| **Toàn bộ cuộc đời (Entire Lifespan)** | Từ trẻ đến già, từ sinh đến chết | Nhiều verses = các chương (chapters), phải có bước nhảy thời gian (time jump) rõ ràng |

**KHÔNG mặc định dùng cùng 1 cấu trúc.** Chọn cấu trúc phù hợp concept VÀ độ dài đã chọn ở A1.

#### 🕐 Cấu trúc 4 PHÚT (Phiên bản Đầy đủ — như hiện tại)

| Cấu trúc | Pattern (Mẫu) | Khi nào dùng |
| :--- | :--- | :--- |
| **Pop Cổ điển (Classic Pop)** | V-PC-C-V-PC-C-B-C | Bài hát cần hook mạnh, hấp dẫn đại chúng (mainstream appeal) |
| **Kể chuyện (Storyteller)** | V-V-C-V-V-C-B-C | Khi câu chuyện dài, cần nhiều verse để kể |
| **Chorus Ưu tiên (Chorus-First)** | C-V-C-V-B-C | Khi hook cực mạnh, muốn đánh thẳng ngay |
| **AABA** | V-V-B-V | Ballad cổ điển, tiêu chuẩn jazz, tập trung vào câu chuyện (story-driven) |
| **Điểm đỉnh Điệp khúc đôi (Double Chorus Climax)** | V-C-V-C-B-C-C | Đỉnh điểm (Climax) bùng nổ với double chorus cuối |
| **Sáng tác Xuyên suốt (Through-Composed)** | A-B-C-D-E | Mỗi đoạn mới hoàn toàn — mang tính điện ảnh (cinematic), tiến triển (progressive) |
| **Xây dựng & Giải phóng (Build & Release)** | V-V-V-BUILD-DROP-V-OUTRO | Post-rock, không gian điện ảnh (cinematic ambient), bùng nổ cảm xúc |
| **Phiên khúc-Điệp khúc phụ (Verse-Refrain)** | V(+R)-V(+R)-B-V(+R) | Folk truyền thống, đoạn refrain ngắn thay vì chorus đầy đủ |
| **Điệp khúc Tiến triển (Evolving Chorus)** | V-C1-V-C2-B-C3-OUTRO | **MỚI** — 3 chorus có lời khác nhau hoàn toàn, cùng melody |

**Cấu trúc Điệp khúc Tiến triển (Evolving Chorus) — Hướng dẫn chi tiết (MỚI v7.0):**

> Dùng khi Phạm vi Thời gian = **Chuỗi sự kiện một ngày** hoặc **Toàn bộ cuộc đời**. Melody của chorus giữ nguyên, chỉ lời (lyrics) thay đổi để kể câu chuyện (narrative) tiến triển qua thời gian.

| Chorus | Thời điểm | Nhiệm vụ của lời (lyrics) |
| :--- | :--- | :--- |
| **C1** | Bình minh / Trẻ / Bắt đầu | Thiết lập thế giới — ai, ở đâu, cảm giác gì |
| **C2** | Giữa trưa / Trưởng thành / Giữa chặng | Đào sâu (Deepening) — đi sâu hơn vào mối quan hệ/nơi chốn |
| **C3** | Chạng vạng / Già / Kết thúc | Điểm rơi cảm xúc (Emotional payoff) — giải quyết (resolution), chấp nhận, nói lời tạm biệt |

*Ví dụ từ kho dữ liệu: Bài "Old Farm Day" — 3 chorus kể hành trình từ bình minh → trưa → hoàng hôn qua cùng 1 trang trại.*

#### ⚡ Cấu trúc 2 PHÚT (Phiên bản Ngắn — cô đọng, thử nghiệm tỷ lệ giữ chân)

> [!IMPORTANT]
> **Nguyên tắc 2 phút:** Đi thẳng vào hook nhanh nhất có thể. Không Bridge. Không Final Chorus riêng. Mỗi phân đoạn PHẢI kiếm được chỗ đứng của nó — nếu cắt ra vẫn OK thì đừng có để vào.

| Cấu trúc | Pattern (Mẫu) | Khi nào dùng |
| :--- | :--- | :--- |
| **Hook Trước Ngắn gọn (Hook-First Short)** | C-V-C-V-C-OUTRO | Hook cực mạnh, muốn cắm vào tai ngay giây đầu |
| **Ballad Chặt chẽ (Tight Ballad)** | V-C-V-C-OUTRO | Câu chuyện đơn giản, 1 hình ảnh trung tâm, cảm xúc (emotional) đơn |
| **Vòng lặp Verse-Chorus** | V-PC-C-V-C-OUTRO | Cần pre-chorus tạo độ căng (tension), vẫn giữ được nhịp gọn |
| **Kể chuyện Tối giản (Stripped Storyteller)** | V-V-C-C-OUTRO | Kể xong câu chuyện, rồi hit chorus 2 lần liên tiếp để đọng lại |

**Ràng buộc cứng cho 2 phút:**
- Số dòng lời mục tiêu (Target lyrics): **20-30 dòng** (không phải 40-60)
- Số phân đoạn (sections): **tối đa 5** (không tính Intro)
- Intro: **4-8 giây** (thẻ `[Short Intro]` hoặc không có Intro)
- Chorus: **xuất hiện lần đầu trong 45 giây đầu** — không được để người nghe chờ quá lâu
- Không Bridge (Bridge chiếm ~30-45 giây — quá xa xỉ với bài 2 phút)
- Không Final Chorus riêng biệt — Chorus 2 là điểm đỉnh, Outro là đủ
- **Verse 2 PHẢI ngắn hơn hoặc bằng Verse 1** (không mở rộng câu chuyện ở đây)

**Sửa đổi từ bài 4 phút → 2 phút (nếu cần rút gọn):**
1. Bỏ Bridge
2. Gộp Pre-Chorus vào Chorus (nếu có PC)
3. Rút Verse 1 và Verse 2 xuống còn 4-6 dòng mỗi verse thay vì 8-10
4. Chorus chỉ 4-6 dòng, cực kỳ đáng nhớ (memorable)
5. Outro ngắn: 2-4 dòng hoặc `[instrumental fade]`

---

**Quy tắc "Yếu tố Bất ngờ" (Surprise Element) (áp dụng cho cả 2 phiên bản):**
Mỗi bài phải có **≥ 1 khoảnh khắc bất ngờ về cấu trúc (structural)** — ví dụ: solo nhạc cụ bất ngờ, chuyển điệu (key change), thay đổi hoàn toàn kết cấu âm thanh (texture shift), khoảng lặng (silence) trước đoạn đỉnh điểm (climax), hoặc đoạn kết (coda) không ai ngờ tới.

### F8. Kỹ thuật Điện ảnh Nâng cao (Advanced Cinematic Techniques)

1. **Pha trộn thể loại (Genre Fusion):** Kết hợp hai không gian đối lập (ví dụ: Acoustic Folk + Sub-bass Electronic → "Ma sát nhịp điệu (Rhythmic friction)").
2. **Khoảng thở:** Chủ động nhồi `[Pause]`, `[Beat Breakdown]`, hoặc `[Silence]` trước chuyển đoạn.
3. **Kỹ thuật Anti-Drop (Chống Drop):** Thay đoạn cao trào (build-up) ồn ào → `[Music abruptly stops]` (Nhạc dừng đột ngột) → chorus chỉ bằng giọng và sub-bass.
4. **Chỉ dẫn biểu diễn (Performance Cues):** `[Sigh]` (Thở dài), `[Breathless]` (Hụt hơi), `[Spoken]` (Nói), `[voice crack]` (Lạc giọng) — làm AI "con người" hơn.
5. **Nhịp điệu tự do (Rubato):** Dấu ba chấm `...` và ngắt dòng để ép AI hát lơi nhịp.

### F8.5. Thư viện Dấu ấn Kết thúc (Ending Signature Library) (MỚI — v7.0)

> [!IMPORTANT]
> Ending là khoảnh khắc người nghe quyết định **comment, share, hay replay**. YouTube đo tỷ lệ hoàn thành (completion rate) — bài có ending mạnh = người nghe nghe đến giây cuối = tín hiệu thuật toán (algorithmic signal). Chọn 1 trong 4 kiểu ending dưới đây dựa trên Trạng thái Cảm xúc (Emotional Mode) đã chọn ở B2.5.

| Loại kết thúc (Ending Type) | Cấu trúc | Hiệu ứng cảm xúc (Emotional Effect) | Dùng với Mode |
| :--- | :--- | :--- | :--- |
| **Whispered Coda** | Guitar mờ dần → 1 dòng thì thầm/nói cuối cùng | Cảm giác khép lại gần gũi, "ngả người lắng nghe" | A, B |
| **CTA Outro** | Piano xuất hiện → lời bài hát là chỉ dẫn trực tiếp ("sit a little longer") | Trăn trở → hành động → bình luận "tôi đã làm điều này" | C |
| **Incomplete Fragment** | Guitar mờ dần → 1-2 dòng lời bài hát không hoàn chỉnh, không dấu chấm | Vấn vương, ám ảnh, bài hát tiếp tục trong đầu | B |
| **Wordless Resolution** | Luyến láy (mmm, ooh) → Solo nhạc cụ đặc biệt → im lặng | Giải tỏa cảm xúc, vượt ngoài ngôn từ | D |

**Chi tiết từng Loại kết thúc (Ending Type):**

**Type 1 — Whispered Coda:**
```
[acoustic guitar fades]
[whispered]
This is home
```
- Nói/thì thầm sau khi nhạc mờ dần = sự gần gũi tột cùng
- Cảm giác như người hát đang nói thẳng vào tai người nghe
- KHÔNG hát — phải là nói hoặc thì thầm

**Type 2 — CTA Outro:**
```
[soft piano enters]
So sit a little longer at the table
Let the phone call run a little long
Look back once more when you are leaving
Say the thing that won't wait till you're strong
[final acoustic guitar strum]
That the last time could be today
```
- Piano xuất hiện để báo hiệu sự chuyển hướng từ suy ngẫm → hành động
- Lời bài hát phải là câu mệnh lệnh ("sit", "let", "look", "say")
- Kết thúc bằng 1 dòng khẳng định neo giữ lại thông điệp chính

**Type 3 — Incomplete Fragment:**
```
[acoustic guitar fades out]
Safer than lantern glow
Where the kind fields grow
```
- KHÔNG có dấu chấm ở cuối
- Câu không hoàn chỉnh về ngữ pháp → giai điệu tiếp tục vang vọng trong đầu người nghe
- Chỉ 2-4 dòng — không giải thích

**Type 4 — Wordless Resolution:**
```
[vocalizing melodies, cello, acoustic guitar fades out]
(Mmm-hmm-hmm)
(Ohhh-ohhh)
[cello solo]
[silence]
```
- Sau cái chết / sự mất mát lớn — ngôn ngữ không đủ diễn tả
- Chỉ có âm thanh, không lời
- Cello hoặc Nhạc cụ đặc biệt có đoạn solo cuối
- Kết thúc bằng sự im lặng thực sự (không mờ dần — CẮT)

### F9. Dàn dựng & Phối khí

**Song ca (Duets):**
1.  Hộp Style (Style Box): nhập `duet` hoặc `male and female vocal duet`.
2.  Hộp Lyrics (Lyrics Box) ở đầu bài: `[Duet: John (male) and Jane (female)]`.
3.  Chia đoạn: `[John]`, `[Jane]`, `[Both]`. Mỗi giọng hát hát nguyên cả verse/chorus.

**Dàn đồng ca:** `[Multiple voice chorus, SATB]` trước điệp khúc.

**Solo nhạc cụ:** Đặt thẻ trên dòng độc lập: `[instrumental break, saxophone]`.

**Cao trào (EDM):** `[buildup]` → `[drop]`.

### F10. Giới hạn ký tự & Mẹo Kéo dài (Extend Hack)

**Quy tắc khoảng đệm (Buffer Rule):** Viết lời ngắn hơn giới hạn tối đa ít nhất **500 ký tự** để chừa chỗ cho các thẻ.

**Mẹo Kéo dài (Extend Hack):**
1.  Chọn điểm cắt tại khoảng lặng hoặc cuối câu hát.
2.  Hộp Style khi kéo dài: giữ các thể loại cốt lõi, bỏ `[Intro]`, thêm `[Bridge]`/`[Outro]`.
3.  Hộp Lyrics: chỉ để phần lời bài hát còn lại, bắt đầu bằng nhãn phân đoạn hiện tại.

### F11. Khắc phục sự cố (Troubleshooting)

| Vấn đề | Giải pháp |
| :--- | :--- |
| Ca sĩ hát quá nhanh/vấp | Quá nhiều âm tiết/dòng → viết lại ngắn hơn, thêm `...` hoặc ngắt dòng |
| Âm thanh bùng nhùng/méo | Hộp Style có quá nhiều nhạc cụ → bỏ bớt, thêm `high fidelity`, `intimate close-mic` |
| Suno phát âm sai từ | Viết theo cách phát âm: `sewing` → `sowing`, `AI` → `A-I` |
| Suno đọc to siêu dữ liệu (metatag) | Chỉ dẫn trong `[]` quá dài → giữ ngắn gọn |
| Nhạc cụ (Instrumental) có giọng hát | Viết `Instrumental` ở CẢ HAI ô: Lyrics + Style Box |
| Giai điệu phẳng, không bắt tai | Thêm `soaring memorable melody`, `earworm hook` vào style. Đặt nguyên âm mở ở câu hook. |
| Bài hát đơn điệu (monotone) | Thiếu sự tương phản → kiểm tra Bản đồ Năng lượng, đảm bảo có ≥ 3/7 loại tương phản |
| Điệp khúc (Chorus) không đọng lại | Dòng hook quá ngắn (< 7 từ) → viết dài hơn. Thiếu bước nhảy giai điệu (melodic leap). |

### F12. Sửa lỗi phát âm & Dịch thuật

*   **Mẹo viết phiên âm (Phonetic Spelling Hack):** Viết phiên âm thay vì viết đúng chính tả. `mine` → `mineeeee` để kéo dài ngân giọng.
*   **Bảo vệ vần khi dịch (Translation Rhyme Guard):** Khi dịch, thay đổi từ vựng nếu cần để duy trì cấu trúc vần và số lượng âm tiết gốc.

---

## PHẦN G — KIỂM SOÁT CHẤT LƯỢNG (QUALITY GATES)

### G1. Chống văn rác AI (Anti-AI Slop) — Không khoan nhượng (SỬ DỤNG SKILLS)

Agent **BẮT BUỘC PHẢI CHẠY** 2 skills cho mọi bản nháp:
1. **`avoid-ai-writing`**
2. **`stop-slop`**

### G2. Cấp độ 1 — Cổng Kỹ thuật (Danh sách kiểm tra)

- [ ] **Tuân thủ Học thuyết Chống lặp lại (Anti-Repetition Doctrine)?** Verse 2 không lặp lại nguyên xi Verse 1? Hát bè `()` không lặp lại quá 3 lần? Bridge có góc nhìn mới?
- [ ] Câu chuyện đơn giản & nhân văn? Vật thể mang cảm xúc rõ ràng?
- [ ] Vượt qua Cổng Cozy Healing (≥ 2/4 tiêu chí)?
- [ ] **Thể loại phù hợp concept?** (không mặc định là folk)
- [ ] STYLE 120-200 ký tự? Có từ khóa chất lượng giai điệu? Có từ khóa nhịp điệu (groove)? Hình tượng giọng hát rõ ràng?
- [ ] **Bản đồ Năng lượng (Energy Map) đã được xác định?** Tỷ lệ tương phản ≥ 2x?
- [ ] **≥ 3/7 loại tương phản được sử dụng?**
- [ ] Lời bài hát 100% tiếng Anh? **Hook vượt qua cả 3 bài kiểm tra (lời ca + giai điệu + nhịp điệu)?** Đạt ≥ 2/3?
- [ ] **Độ dài dòng đúng quy tắc?** Verse 5-10 từ/dòng, hook ≥ 7 từ?
- [ ] **Nguyên âm mở ở nốt cao trong hook/chorus?**
- [ ] Nhịp điệu (Meter) tự nhiên? Hình ảnh cụ thể?
- [ ] Bridge có ý nghĩa? **Giai điệu Bridge chuyển sang một vùng mới?**
- [ ] **Chorus không lặp lại nguyên si quá 2 lần?** Final chorus sâu sắc hơn?
- [ ] Vượt qua bài kiểm tra vần chống máy móc? Tuân thủ phân tách lyrics-vs-video?
- [ ] 40-60 dòng lời bài hát? Các số được viết bằng chữ?
- [ ] Phù hợp với người lớn 45+? Ấm áp? Vượt qua quá trình quét chống văn rác (Anti-slop passed)?
- [ ] **Cấu trúc bài hát được chọn có chủ đích?** (không mặc định cùng 1 khuôn mẫu)
- [ ] **≥ 1 yếu tố bất ngờ về mặt cấu trúc?**

### G3. Cấp độ 2 — Bài kiểm tra tàn bạo (BẮT BUỘC — không bỏ qua)

1.  **Bài kiểm tra John Prine / Leonard Cohen:** Họ đọc điệp khúc này có thấy xấu hổ không? Có → viết lại cho chân chất hơn.
2.  **Bài kiểm tra Thơ vs Bài hát (Poem vs Song Test):** Đọc không có nhạc nghe giống một bài thơ hay bài hát thực sự? Giống thơ → viết lại cho dễ hát.
3.  **Sức nặng trên giấy:** Bỏ giai điệu đi, đọc lời có thấy cảm động không? Trôi tuột → viết lại.
4.  **Phản ứng của người lạ (Stranger Reaction Test):** Đọc Verse 1 cho người lạ nghe, họ cảm thấy gì? Nhún vai → viết lại.
5.  **Dòng lấp vần:** Dòng nào viết ra CHỈ để đủ nhịp/vần? → Tiêu diệt.
6.  **Mật độ giác quan:** Tối thiểu ≥ 3 chi tiết ngửi/chạm/nhiệt độ cụ thể. < 3 → quá trừu tượng.
7.  **Bài kiểm tra Bình luận (Comment Test):** Người xem có tự động gõ câu hook làm bình luận trên YouTube không? Không → chưa phải là hook.

### G4. Cấp độ 3 — Cổng Tính Nhạc (MỚI — BẮT BUỘC)

> [!IMPORTANT]
> Cổng này kiểm tra **NHẠC**, không chỉ lời. Đây là cổng quyết định bài hát có bắt tai không.

1.  **Bài kiểm tra Ngân nga (Hum Test):** Bỏ lời đi, chỉ ngân nga giai điệu điệp khúc — có bắt tai không? Nếu không ngân nga được → giai điệu quá phẳng.
2.  **Bài kiểm tra Gõ nhịp (Tap Test):** Đọc lời bài hát theo nhịp — có tự động gõ tay/lắc đầu không? Nếu không → thiếu nhịp điệu (groove).
3.  **Bài kiểm tra Nổi da gà (Goosebump Test):** Đọc đến đoạn chuyển giao pre-chorus/chorus — có cảm giác "dâng trào" không? Nếu không → thiếu độ tương phản động (dynamic contrast).
4.  **Bài kiểm tra 10 Giây Đầu (First 10 Seconds Test):** 10 giây đầu tiên có đủ thú vị để giữ chân người nghe không? Nếu nhàm chán → intro quá dài hoặc quá chung chung.
5.  **Bài kiểm tra Hát theo (Singalong Test):** Điệp khúc có đủ đơn giản và bắt tai để người nghe hát theo từ lần 2? Nếu không → quá phức tạp hoặc giai điệu không đáng nhớ.

### G5. Danh sách kiểm tra định dạng Lời bài hát (BẮT BUỘC)

- [ ] Dùng `...` và `()` hợp lý để tạo chiều sâu?
- [ ] Có ≥ 1 thẻ lấy hơi (breath tag) `[sigh]` / `[deep breath]`?
- [ ] Có ≥ 1 từ VIẾT HOA để nhấn mạnh?
- [ ] Có ≥ 1 nguyên âm kéo dài (`ohhh`, `hoooome`)?
- [ ] Bridge hoặc Final Chorus có thẻ cảm xúc (emotion tag)?
- [ ] Khoảng cách (Spacing) giữa Verse và Chorus **khác nhau rõ ràng**?
- [ ] Mọi thẻ `[]` đều ngắn gọn?
- [ ] Có ≥ 1 đoạn `[instrumental break]` tạo không gian thở (breathing room)?

---

## PHỤ LỤC — THƯ VIỆN THUẬT NGỮ ÂM NHẠC CHO SUNO

### Nhịp độ & Nhịp điệu
*   **Tempo**: Tốc độ bản nhạc (BPM). **Adagio**: 66-76 BPM. **Andante**: 76-108 BPM. **Allegro**: 120-168 BPM. **Presto**: 168-200 BPM.
*   **Rubato**: Nhịp độ tự do. **Syncopation**: Nhấn nhịp yếu/lệch nhịp. **Polyrhythm**: Đa nhịp điệu.
*   **Groove**: Cảm giác nhịp bắt tai. **Downbeat**: Nhịp mạnh ở đầu ô nhịp. **Upbeat**: Nhịp nhẹ trước downbeat.

### Sắc thái & Biểu cảm
*   **Crescendo**: To dần. **Diminuendo**: Nhỏ dần. **Forte**: Mạnh. **Piano**: Nhẹ. **Fortissimo**: Rất mạnh. **Pianissimo**: Rất nhẹ.
*   **Staccato**: Ngắt âm. **Legato**: Liên âm. **Vibrato**: Ngân rung. **Tremolo**: Rung giật nốt.

### Cấu trúc bài hát
*   **Verse** (Phiên khúc) → **Pre-Chorus** (Tiền điệp khúc) → **Chorus** (Điệp khúc) → **Bridge** (Đoạn nối) → **Outro** (Phần kết).
*   **Hook**: Cụm từ/giai điệu bắt tai. **Refrain**: Câu lặp. **Break**: Tạm dừng. **Drop**: Bùng nổ (EDM).

### Giai điệu & Hòa âm
*   **Chord Progression**: Chuỗi hợp âm. **Major**: Trưởng (Tươi sáng). **Minor**: Thứ (Tối, buồn).
*   **Arpeggio**: Rải hợp âm. **Counterpoint**: Đối âm. **Dissonance → Resolution**: Căng thẳng → Giải quyết.
*   **Melodic Contour**: Hình dáng giai điệu (đi lên/đi xuống/hình vòm/nhảy quãng).
*   **Interval**: Khoảng cách giữa 2 nốt (Quãng). **Leap**: Nhảy quãng rộng. **Step**: Bước đi liền bậc.

### Nhạc cụ & Chất liệu
*   **Monophonic**: Đơn âm. **Homophonic**: Chủ âm. **Polyphonic**: Đa âm.
*   **Timbre**: Âm sắc. **Layering**: Chồng lớp. **Sparse**: Tinh giản/Thưa thớt. **Dense**: Dày đặc.

### Kỹ thuật giọng hát
*   **Falsetto**: Giọng giả thanh. **Belt**: Hát giọng ngực nội lực. **Melisma**: Luyến láy. **Crooning**: Hát thủ thỉ.
*   **Call and Response**: Xướng đáp/Đối đáp. **A Cappella**: Hát chay (không nhạc đệm). **Scat**: Hát ngẫu hứng Jazz.

### Sản xuất & Hiệu ứng
*   **Reverb**: Độ vang không gian. **Delay/Echo**: Tiếng vọng. **Compression**: Nén tiếng. **Distortion**: Méo tiếng.
*   **EQ**: Cân bằng tần số. **Panning**: Định vị âm thanh nổi. **Fade In/Out**: Lớn/nhỏ dần.

### Khái niệm nâng cao
*   **Modulation (Key Change)**: Chuyển giọng/Chuyển tone. **Time Signature**: Số chỉ nhịp (4/4, 3/4, 6/8).
*   **Cadence**: Kết đoạn. **Ostinato**: Mô-típ lặp lại. **Pedal Point**: Nốt nền ngân dài.
*   **Suspension**: Giữ nốt tạo căng thẳng. **Anacrusis**: Nhịp lấy đà. **Coda**: Đoạn vĩ thanh.

---

*Bản cập nhật: 2026-06-07 | Kiến thức Phát triển Bài hát Coslient v7.0 "Niche Intelligence"*

