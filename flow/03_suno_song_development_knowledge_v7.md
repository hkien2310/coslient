# Coslient — Suno Song Development Knowledge v7.0 "Niche Intelligence"

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

### A3. Đầu ra bắt buộc — Song Package (Draft)

Khi trình Boss, song package **phải** có đầy đủ các mục sau:

```
STAGE: Song Development
STATUS: draft

SONG DURATION: [2 phút / 4 phút — ghi rõ Boss đã chọn]

MUSIC DIRECTION:
- [genre/fusion, tempo, instruments, vocal persona, signature motif]

EMOTIONAL DIRECTION:
- [arc: từ đâu → đến đâu]

MELODY DIRECTION:
- [melodic contour: verse melody thấp/trung, chorus melody soaring/anthemic]
- [hook type: lyrical / melodic / rhythmic — target ≥ 2/3]
- [nốt cao nhất rơi vào từ nào trong chorus]

DYNAMIC ARC:
- [energy map: Intro X% → Verse X% → Pre-Chorus X% → Chorus X% → Bridge X% → Final Chorus X%]
- [contrast ratio: phần mạnh nhất gấp bao nhiêu lần phần nhẹ nhất]

GROOVE STRATEGY:
- [rhythmic feel: straight/swung/syncopated/rolling]
- [percussion approach]
- [what makes listener tap foot/nod head]

STORY ANGLE:
- [câu chuyện con người, hình ảnh cụ thể, yếu tố siêu thực nếu có]

STRUCTURE:
- [cấu trúc đã chọn từ Structure Library, lý do — xem F7 cho cấu trúc 2 phút]

HOOK STRATEGY:
- [lyrical hook: cụm từ trung tâm, tại sao dễ nhớ]
- [melodic hook: melodic contour của hook, vowel nào ở nốt cao]
- [rhythmic hook: pattern nhịp đặc trưng nếu có]
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
Generate 3-5 versions. Chọn take có vocal melody mạnh nhất, groove bắt tai nhất, dynamic lift rõ ràng nhất, và chorus đọng lại lâu nhất.

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
| Ông lão nhớ vợ qua chiếc cốc cà phê | Acoustic folk-blues, fingerpicked | Intimacy, warmth, simplicity |
| Thị trấn nhỏ trôi vào vũ trụ | Cinematic space-folk, orchestral swells | Epic scale, wonder |
| Đại dương ôm giữ ký ức | Celtic pop, rolling 6/8 waltz | Oceanic rhythm, ancient feel |
| Người thợ rèn già và ngọn lửa cuối cùng | Delta blues, slide guitar, raw | Grit, heat, labor |
| Khu vườn mùa thu tự kể chuyện | Chamber pop, strings + piano | Elegance, seasons |
| Cô đơn giữa thành phố đêm | Jazz noir, smoky saxophone | Urban melancholy, sophistication |
| Ngọn hải đăng cuối cùng | Post-rock ambient, crescendo walls | Isolation, vast ocean |
| Lá thư không gửi | Bossa nova, nylon guitar | Gentle regret, warm breeze |
| Chuyến tàu đêm xuyên nước Nga | Cinematic orchestral, Russian folk elements | Journey, vast landscape |
| Người làm vườn và bầy ong | Pastoral folk-pop, mandolin, accordion | Countryside, buzzing life |

**Palette thể loại mở rộng (không giới hạn, đây chỉ là gợi ý):**
`acoustic folk` · `indie folk-pop` · `Americana` · `chamber orchestral pop` · `vintage gospel-soul` · `Celtic pop` · `delta blues` · `jazz noir` · `bossa nova` · `post-rock ambient` · `cinematic orchestral` · `country ballad` · `R&B soul` · `baroque pop` · `art rock` · `progressive folk` · `flamenco fusion` · `tango nuevo` · `Nordic noir folk` · `desert rock` · `Appalachian bluegrass` · `French chanson` · `African highlife` · `reggae acoustic` · `psychedelic folk`

### B2. Emotional Arc — Cozy Healing Gate + Emotional Mode Selector

**Mặc định:** Luôn đi từ buồn nhẹ/hoài niệm → ấm áp/chữa lành. **Không** kết thúc trong bóng tối tuyệt đối.

**Cấm tông chủ đạo hoặc kết thúc:** Pitch-black darkness, unhealed grief, bleakness, bitterness, despair.

**Nhưng KHÔNG cấm:**
*   Đau đớn thực sự (grief) — miễn là có ánh sáng ở cuối.
*   Căng thẳng kịch tính (tension) — miễn là có resolution.
*   Sự cô đơn sâu sắc — miễn là kết thúc với connection hoặc acceptance.
*   Gritty, raw, thô ráp — miễn là có nhân văn.

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
| **A** | **Bittersweet Return** | Quay về một nơi/người trong ký ức, vừa đau vừa ấm | Medium — nostalgia comments | High |
| **B** | **Peaceful Observation** | Quan sát cảnh đẹp bình yên, không cần nhân vật cụ thể | Lower — therapeutic/background | Very High (rewatch) |
| **C** | **Regret + Call to Action** | Tiếc nuối điều chưa nói/làm → thúc đẩy hành động ngay hôm nay | **Highest** — "I called my mom" | High |
| **D** | **Cathartic Grief** | Đau mất mát thực sự (người thân, thú cưng) → được phép khóc | **Highest** — crying + sharing | High |

**Chiến lược chọn Mode:**
- Muốn nhiều comment → chọn Mode C hoặc D
- Muốn nhiều rewatch / background listening → chọn Mode B
- Muốn cân bằng giữa comment và watch time → chọn Mode A
- Muốn viral sharing (tag bạn bè) → Mode C hoặc D

**Mode ảnh hưởng đến Bridge và Ending:**

| Mode | Bridge function | Ending type |
| :--- | :--- | :--- |
| **A** | Khoảnh khắc epiphany — hiểu ra điều gì đó | Guitar fade + whisper/spoken coda |
| **B** | Sensory peak — moment đẹp nhất của ngày | Fragment/incomplete lyric → lingering feel |
| **C** | Thesis statement — triết lý trung tâm của bài | Direct CTA lyrics + piano enters |
| **D** | Time jump — bước nhảy timeline (trẻ → già → chết) | Wordless vocalizing + special instrument → silence |

### B3. Song Title — Coslient Naming Framework (The "Anti-Cheesy" Indie Aesthetic)

> [!IMPORTANT]
> **QUY TẮC BẮT BUỘC (Boss rule — override mọi gợi ý bên dưới):**
> - **Tối đa 3 từ** — không được dài hơn.
> - **Ngắn gọn nhưng đầy đủ nghĩa** — người đọc xong phải cảm nhận được hồn của bài hát, dù chưa nghe.
> - **Hoặc kỳ lạ** — từ ngữ gây tò mò, khó đoán, buộc người ta phải bấm nghe để hiểu.
> - Nếu đề xuất tên bài, luôn đưa ra **3–5 phương án** kèm phân tích ngắn gọn (double meaning, cảm giác gợi ra, lý do chọn).

Tiêu đề là **điểm chạm đầu tiên (Curiosity Gap)**. Tên bài hát phải đóng vai trò như một tác phẩm nghệ thuật (Art-house/Indie), tuyệt đối không dùng để "tóm tắt" hay "kể lể" trần trụi nội dung. MỤC TIÊU LÀ TIẾNG ANH.

> [!WARNING]
> **BỘ LỌC CHỐNG "CHEESY" (Anti-Sến/Anti-Melodrama)**
> - ❌ **Cấm từ ngữ cường điệu, khóc lóc:** *Agony, Shattered, Bleeding Heart, Tears, Sorrow, Weeping.*
> - ❌ **Cấm công thức sáo rỗng (The "Of The" trap):** `[Abstract Noun] of the [Macro Concept]` (VD: *Echoes of the Heart*, *Symphony of the Soul*, *Whispers of Time*).
> - ❌ **Cấm câu hỏi tu từ sến súa:** *Why Did You Leave?, Where Did Our Love Go?*

**5 Trụ Cột Đặt Tên "Sang" (Dựa trên Research Nhạc Indie/Alt-Rock/Pop Hiện Đại):**

**1. Sự Trừu Tượng Hóa & Hiện Tượng Học (Clinical & Abstract)**
Thay vì kể lể cảm xúc, hãy dùng các khái niệm y tế, khoa học, hoặc địa lý để ám chỉ sự việc. Tạo sự lạnh lùng, khách quan cho một nỗi đau.
- ✅ *Blood Bank* (Bon Iver), *Chinese Satellite* (Phoebe Bridgers), *First Breath After Coma* (Explosions in the Sky), *Holocene*.
- ❌ *The Hospital of Sadness*, *Stars in the Sky*.

**2. Vật Thể Hóa & Không Gian Cụ Thể (Hyper-Specific Anchors)**
Dùng một vật thể cực kỳ đời thường hoặc một địa danh/địa chỉ chính xác làm đại diện cho toàn bộ câu chuyện (Objective Correlative).
- ✅ *Casimir Pulaski Day* (Sufjan Stevens), *Stoned at the Nail Salon* (Lorde), *Fake Plastic Trees* (Radiohead), *Needle in the Hay*.
- ❌ *The Town of Memories*, *Tears in the Rain*.

**3. Phá Vỡ Ngữ Pháp & Xung Đột Hình Ảnh (Juxtaposition)**
Kết hợp những từ không liên quan hoặc đối lập nhau kịch liệt (bạo lực vs mỏng manh, tự nhiên vs nhân tạo) để tạo ra cảm giác Surreal.
- ✅ *Bullet With Butterfly Wings* (Smashing Pumpkins), *Crying Lightning* (Arctic Monkeys), *Flightless Bird, American Mouth* (Iron & Wine).
- ❌ *Sad Winter*, *Lonely Night*.

**4. Chữ Thường & Lời Nói Đời Thường (The Lowercase Confessional)**
Cắt một mảnh hội thoại cực kỳ tự nhiên, hoặc định dạng toàn bộ bằng **chữ viết thường (lowercase)** để tạo cảm giác riêng tư, thì thầm, giống như một tin nhắn lúc 2h sáng.
- ✅ *when the party's over* (Billie Eilish), *Why'd You Only Call Me When You're High?* (Arctic Monkeys), *hope is a dangerous thing...* (Lana Del Rey).
- ❌ *I Will Always Love You*, *Please Come Back*.

**5. Câu Hỏi Bỏ Ngỏ & Nghịch Lý (The Curiosity Gap)**
Đặt tên tạo ra một sự mâu thuẫn hoặc câu hỏi khiến người ta BẮT BUỘC phải bấm vào nghe để hiểu tại sao.
- ✅ *The System Only Dreams in Total Darkness* (The National), *How to Disappear Completely* (Radiohead), *The Predatory Wasp of the Palisades Is Out to Get Us!*
- ❌ *A Song About Depression*, *The Sad Love Story*.

**Kiểm tra tiêu đề (4-Point Test):**
1. **Cheesy Test:** Có từ nào đọc lên nghe giống nhạc Pop thập niên 90 hay AI generate không (Echoes, Whispers...)? Nếu có → Đổi.
2. **Visual Test:** Tiêu đề có gợi ra một BỨC TRANH cụ thể không (VD: *Nail Salon*, *Plastic Trees*) hay chỉ là KHÁI NIỆM (*Sorrow*)? Phải là bức tranh.
3. **Curiosity Test:** Đọc lên có thấy tò mò, kỳ quặc, muốn bấm nghe không?
4. **Formatting Test:** Cân nhắc dùng *toàn bộ chữ thường (lowercase)* để tăng tính tự sự, lofi, indie.

### B4. Coslient Story DNA — Hồn cốt câu chuyện

**"Một ký ức nhỏ hóa thành âm nhạc"** — Câu chuyện phải đủ giản dị, dễ hiểu và gần gũi với khán giả lớn tuổi (45+) ngay từ những câu hát đầu tiên.

**5 Tiêu chí Vàng:**
1. **Sự thật nhân loại phổ quát:** Ai cũng từng trải qua. Tránh quá kỳ lạ hay triết lý cao siêu.
2. **Quy tắc "Một":** Một nhân vật chính, một vật thể trọng tâm, một khoảnh khắc cụ thể.
3. **Hiểu ngay từ Verse 1:** Không cần background hay giải thích.
4. **Giản dị hóa:** Đẹp ở sự chân phương. Một ấm trà nguội có sức nặng hơn vạn lời thề.
5. **Bài test "Kể cho bà ngoại nghe":** Bà ngoại 70 tuổi nghe xong Verse 1 mà hỏi "Bài này nói về cái gì?" → quá phức tạp, viết lại.

### B5. Lyrics — Show, Don't Tell

Cảm xúc phải gắn vào **vật thể, địa điểm, hành động hoặc chi tiết giác quan cụ thể**.

| ❌ Yếu (Trừu tượng) | ✅ Mạnh (Giác quan) |
| :--- | :--- |
| *I was sad. I miss the past.* | *Your coat still hangs behind the kitchen door.* |
| *Love is in my heart.* | *The blue cup caught the morning on my windowsill.* |
| *Memories shine forever.* | *The chair by the window still knows your shape.* |

**Lyrics vs Video Separation (CRITICAL):** Lyrics = cảm xúc, chất liệu giác quan, thế giới nội tâm. Video = hiệu ứng thị giác, phép thuật siêu thực. **KHÔNG BAO GIỜ** kể lại các hiệu ứng video trong lời hát.

**Surreal Lyric Devices (Embedded Coslient Magic):**
*   **Temporal Juxtaposition:** *The clock on the wall ticks backwards, bringing 1982 to the kitchen door.*
*   **Material Metamorphosis:** *I planted tea leaves in your cup, and a tiny forest grew from the porcelain rim.*
*   **Living Architecture:** *The floorboards hum the song you used to play.*

### B5.5. Tính Thơ & Các Mối Quan Hệ (Poetic Intimacy)

1. **Dùng Ẩn dụ Vật lý:** Biến nỗi đau trừu tượng thành thực thể vật lý. Đừng viết "I miss you."
2. **Kể chuyện phi tuyến tính:** Ném người nghe vào mảnh ký ức lộn xộn đan xen quá khứ và hiện tại.
3. **Tôn vinh sự đời thường:** Tình yêu sâu sắc nhất nằm ở sự bình dị: *"Tell me about your day."*

### B5.6. Object Leitmotif Protocol (MỚI — v7.0)

> [!IMPORTANT]
> Đây là kỹ thuật tạo ra emotional payoff lớn nhất trong folk/indie niche. Chọn 1 vật thể bình thường TRƯỚC KHI viết bài → plan cách nó xuất hiện nhiều lần → lần cuối cùng phải devastating.

**3 bước bắt buộc:**

**Bước 1 — Chọn Object:** Vật thể phải:
- Cực kỳ ordinary (không phải "trái tim", "bầu trời", "ngọn gió")
- Gắn với nhân vật cụ thể (chiếc cốc của bà, cái chăn của con mèo, chiếc ghế của ông)
- Có thể được nhìn/chạm/ngửi/nghe → không phải khái niệm

**Bước 2 — Plan Appearances (tối thiểu 3 lần):**

| Lần xuất hiện | Context | Emotional load |
| :--- | :--- | :--- |
| **Lần 1** (V1/V2) | Giới thiệu vật thể — bình thường, neutral | 0% — chỉ là vật |
| **Lần 2** (Chorus/V3) | Vật thể gắn với hành động/kỷ niệm | 40% — bắt đầu load meaning |
| **Lần 3** (Bridge/V4) | Vật thể thể hiện sự thay đổi (ai đó già đi, sức khỏe kém, v.v.) | 70% — người nghe bắt đầu lo |
| **Lần 4** (Outro/Final) | Vật thể lần cuối cùng — context đã hoàn toàn thay đổi | 100% — payoff |

**Bước 3 — Final Payoff Rule:**
Lần xuất hiện cuối của object phải có ít nhất 1 trong các yếu tố:
- Context đã đảo ngược hoàn toàn (vật thể từ vui → buồn, từ đầy → vắng)
- Hành động đi kèm đã thay đổi (ai đó đặt nó xuống lần cuối)
- Câu lyrics có cùng từ nhưng nghĩa đã khác hoàn toàn

**Ví dụ từ corpus:**
- ✅ "The faded blue blanket" (bài Cat): V1=ấm áp, V2=gối đầu, Chorus=bảo vệ, V5=**"You climb to the blanket one final time"** → devastating
- ✅ "Tuesday" (bài Last Time): xuất hiện 2x trong post-chorus → anchors the entire thesis của bài

**Lưu ý:** Object Leitmotif có thể kết hợp với Coslient Title (B3) — đặt tên bài theo chính object đó.

### B6. Folk Healing Niche Constraints (MỚI — v7.0)

> [!NOTE]
> Section này apply **khi concept thuộc niche acoustic folk / indie folk healing** — loại nhạc được research từ 5 bài viral (Three-Quarter Town, Surreal AI Film series). Khi Boss confirm concept thuộc niche này, agent BẮT BUỘC tuân theo constraints bên dưới thay vì free-choice.

**Acoustic Texture Rules (cứng):**
- ✅ Fingerpicked acoustic guitar HOẶC steady 8th-note acoustic strum — không bao giờ distorted/electric lead
- ✅ Upright bass HOẶC acoustic bass — **không electric bass** (mất folk authenticity)
- ✅ Soft brushed snare, shaker, light kick — không bao giờ heavy rock drums
- ✅ 1 Special Instrument (xem D2.5) — piano, glockenspiel, cello, strings, hoặc second guitar
- ❌ Cấm: electric guitar distortion, synths, programmed drums, heavy bass

**Tempo & Key Rules:**
- BPM: **74–120** (sweet spot: **78–82 BPM** cho ballad, 110–115 cho uptempo folk)
- Key: **G Major** hoặc D Major chiếm ưu thế — tạo warm, resonant guitar voicings
- Time: **4/4** mặc định — 3/4 chỉ khi concept cần waltz feel

**Arrangement Philosophy — "Addition Only":**
- Intro: guitar solo (1 nhạc cụ) hoặc guitar + breathe
- Mỗi section THÊM tối đa 1 nhạc cụ mới
- Không remove instrument giữa bài (trừ Bridge strip-back có chủ đích)
- Special Instrument **không có từ đầu** — chỉ enter tại emotional peak
- Outro: strip back về guitar → fade

**Vocal Architecture:**
Chọn 1 trong 2:
- **Duet (M/F):** Trade verses → harmony at chorus → unison at emotional peak. *Unison = hai người cùng sống một khoảnh khắc.*
- **Solo Baritone:** Masculine vulnerability + slight rasp. Mature storyteller tone. Close-mic'd.

**Lyric Approach:**
Chọn 1 trong 3:
- **Personal Specific:** "I" narrator + hyper-specific details ("the third wooden step")
- **Anonymous Universal:** "Someone" observer — người nghe tự project vào
- **Journalistic Witness:** Painterly observation — scenes layered without named character

---

## PHẦN C — MELODY & MUSICALITY INTELLIGENCE (MỚI)

> [!IMPORTANT]
> **Đây là phần quan trọng nhất của v6.0.** Lời hay mà melody dở = bài hát dở. Melody hay mà lời trung bình = bài hát vẫn có thể hit. MELODY LÀ VUA.

### C1. Melodic Contour — Đường cong giai điệu

Melody không phải random — nó có hình dạng, và hình dạng đó tạo cảm xúc:

| Melodic Shape | Cảm xúc tạo ra | Khi nào dùng |
| :--- | :--- | :--- |
| **Ascending (đi lên)** | Hy vọng, năng lượng, mở rộng | Pre-Chorus → Chorus, build-up |
| **Descending (đi xuống)** | Buồn, thư giãn, kết thúc, chấp nhận | Verse, outro, resolution |
| **Arch (lên rồi xuống)** | Kể chuyện hoàn chỉnh, trọn vẹn | Verse lines, bridge |
| **Leap then step (nhảy rồi bước)** | Bất ngờ, kịch tính, memorable | Hook line, chorus opener |
| **Plateau (bằng phẳng)** | Tension, chờ đợi, hypnotic | Pre-chorus, spoken sections |
| **Zigzag (lên xuống liên tục)** | Playful, energetic, restless | Uptempo songs, energetic verses |

**Quy tắc Melodic Contour BẮT BUỘC:**
1. **Verse melody phải THẤP hơn chorus melody.** Nếu verse đã hát cao → chorus không có chỗ để "soar."
2. **Chorus phải có ít nhất 1 melodic leap** (nhảy quãng) — đây là cái tạo "wow moment."
3. **Hook line phải chứa nốt CAO NHẤT của bài hát** — đó là lý do nó đọng lại.
4. **Bridge nên đi vào vùng melody CHƯA TỪNG XUẤT HIỆN** — tạo bất ngờ trước Final Chorus.

### C2. Vowel Placement — Đặt nguyên âm cho melody

Suno tạo melody dựa trên nguyên âm trong lyrics. Nguyên âm mở (open vowels) ở nốt cao = Suno hát đẹp hơn, ngân hơn, ấn tượng hơn.

**Bảng nguyên âm cho melody:**

| Nguyên âm | Đặc tính | Dùng ở đâu |
| :--- | :--- | :--- |
| **AH** (heart, star, far) | Mở nhất, ngân to nhất, powerful | Nốt cao nhất trong chorus, climax |
| **OH** (home, know, gold) | Ấm, tròn, sâu | Chorus hook, emotional peaks |
| **OO** (moon, blue, you) | Mềm, dreamy, kéo dài được | Outro, gentle moments, sustain |
| **EE** (see, free, me) | Sáng, penetrating, cutting | Nốt cao khi cần edge/clarity |
| **AY** (day, way, stay) | Tươi, forward, bright | Uplifting moments |
| **EH** (bed, said, red) | Ngắn, closed, khó ngân | TRÁNH ở nốt cao/sustain |
| **IH** (sit, bit, this) | Đóng nhất, yếu nhất | TRÁNH ở hook/climax |

**Quy tắc BẮT BUỘC:**
*   Từ cuối dòng hook/chorus **phải có nguyên âm mở** (AH, OH, OO, AY). **Cấm** kết hook bằng nguyên âm đóng (EH, IH, UH).
*   Ví dụ: ✅ `The water is WARM` (AH) — Suno ngân đẹp. ❌ `The water is WET` (EH) — Suno ngắt cụt.

### C3. Melodic Hook vs Lyrical Hook vs Rhythmic Hook

**BẮT BUỘC: Mỗi bài hát phải target ít nhất 2/3 loại hook.**

| Loại Hook | Định nghĩa | Cách tạo trong Suno |
| :--- | :--- | :--- |
| **Lyrical Hook** | Cụm từ bắt tai, quotable, đọng lại | Viết lời hay, memorable, đơn giản |
| **Melodic Hook** | Chuỗi nốt nhạc bắt tai — người ta hum mà không cần nhớ lời | Đặt nguyên âm mở ở nốt cao, tạo melodic leap, để Suno space để tạo melody arc |
| **Rhythmic Hook** | Pattern nhịp đặc trưng — cái khiến người ta gõ tay | Viết lyrics theo rhythmic pattern lặp lại, syncopation |

**Cách viết lyrics để Suno tạo melodic hook:**
1. **Cho melody chỗ để bay:** Dòng hook cần ≥ 7 từ để melody có đủ nốt tạo arc. Dòng 2-3 từ → melody phẳng.
2. **Đặt từ quan trọng nhất ở beat mạnh:** Suno nhấn nốt ở beat 1 và beat 3. Đặt từ cảm xúc nhất vào đó.
3. **Lặp melodic pattern:** Khi 2 dòng chorus có cùng syllable count và stress pattern, Suno sẽ lặp melody → tạo "earworm."
4. **Tạo contrast:** Nếu verse melody thấp và đều → chorus phải nhảy lên cao và rộng.

**Cách tạo rhythmic hook:**
1. **Syncopated lyrics:** Đặt từ quan trọng ở off-beat (nhịp yếu). Ví dụ: thay vì `I am walking home tonight` (straight) → `I'm walk-ing HOME to-NIGHT` (syncopated emphasis).
2. **Rhythmic repetition:** Lặp cùng pattern nhịp qua nhiều dòng. Ví dụ: `DA-da-da-DA` × 4 dòng liên tục.
3. **Percussive consonants:** Dùng nhiều phụ âm mạnh (T, K, P, D, B) để tạo nhịp percussion trong chính lời hát.

### C4. Style Prompt — Keywords cho Musicality

Ngoài genre/instrument/vocal, style prompt **phải** chứa keywords điều khiển **chất lượng nhạc**:

**Keywords cho Melody Quality (chọn phù hợp):**
`soaring memorable melody` · `catchy singalong chorus` · `earworm hook` · `anthemic melody` · `haunting unforgettable melody` · `hummable tune` · `sweeping melodic lines` · `lyrical flowing melody`

**Keywords cho Harmonic Richness (chọn phù hợp):**
`rich emotional chord changes` · `unexpected harmonic shifts` · `bittersweet major-minor transitions` · `lush jazz-influenced harmonies` · `dramatic chord progression` · `emotionally complex chords` · `suspended chords resolving`

**Keywords cho Groove/Rhythm (chọn phù hợp):**
`infectious groove` · `driving rhythmic pulse` · `syncopated rhythm` · `head-nodding beat` · `foot-tapping groove` · `rolling rhythmic momentum` · `hypnotic pulse` · `body-moving rhythm`

**Keywords cho Production Quality (chọn phù hợp):**
`lush layered production` · `wide stereo soundscape` · `punchy compressed drums` · `warm analog tape saturation` · `crystal clear high fidelity` · `rich textured arrangement` · `cinematic wide-screen production` · `intimate studio quality`

---

## PHẦN D — DYNAMIC ARC & ARRANGEMENT (MỚI)

> [!IMPORTANT]
> Bài hát phẳng lỳ = bài hát chết. Mỗi bài PHẢI có energy journey rõ ràng — người nghe phải cảm nhận được sự dâng trào, lắng xuống, rồi bùng nổ.

### D1. Energy Map Blueprint

**BẮT BUỘC:** Mỗi bài hát phải có Energy Map được xác định TRƯỚC KHI viết lyrics.

**Template Energy Map chuẩn (điều chỉnh theo concept):**

```
Intro:        ██░░░░░░░░  15-20%  (gợi mở, kéo tai vào)
Verse 1:      ███░░░░░░░  25-35%  (kể chuyện, intimate)
Pre-Chorus:   █████░░░░░  45-55%  (tension rising, anticipation)
Chorus 1:     ████████░░  75-85%  (release, soaring, hook delivery)
Verse 2:      ████░░░░░░  30-40%  (deeper story, slightly more energy than V1)
Chorus 2:     █████████░  80-90%  (bigger than C1 — thêm nhạc cụ/bè/intensity)
Bridge:       ███░░░░░░░  25-40%  (strip back, vulnerability, surprise territory)
Final Chorus: ██████████  95-100% (everything, maximum emotional impact)
Outro:        ██░░░░░░░░  10-20%  (resolution, breath, landing)
```

**Quy tắc Energy Cứng:**
1. **Contrast Ratio ≥ 2x:** Chorus phải có năng lượng tối thiểu **gấp đôi** verse. Nếu verse = 30%, chorus phải ≥ 60%.
2. **Never Flat:** Hai section liên tiếp **KHÔNG ĐƯỢC** cùng energy level. Mỗi section phải khác section trước/sau ít nhất 15%.
3. **Verse 2 > Verse 1:** Verse 2 luôn phải có chút energy nhiều hơn Verse 1 (thêm 1 nhạc cụ, hoặc giọng hát mạnh hơn chút).
4. **Final Chorus > Chorus 2 > Chorus 1:** Mỗi lần chorus xuất hiện phải LỚN HƠN lần trước.

### D2. Instrumentation Layering Strategy

Đừng vứt tất cả nhạc cụ vào từ đầu. Layer thông minh:

| Section | Nhạc cụ điển hình | Nguyên tắc |
| :--- | :--- | :--- |
| **Intro** | 1-2 nhạc cụ (guitar/piano + 1 texture) | Sparse, gợi mở |
| **Verse 1** | 2-3 nhạc cụ (foundation + light rhythm) | Intimate, chừa chỗ cho giọng hát |
| **Pre-Chorus** | Thêm 1-2 layers (bass enters, strings swell) | Building tension |
| **Chorus 1** | 4-6 nhạc cụ (full rhythm + harmonies + lead) | Wide, powerful, but still room to grow |
| **Verse 2** | 3-4 nhạc cụ (V1 + 1 new element) | Slightly richer than V1 |
| **Chorus 2** | 5-7 nhạc cụ (C1 + backing vocals + extra layer) | Bigger, thicker |
| **Bridge** | 2-3 nhạc cụ (strip back, different instrument) | Surprise, vulnerability |
| **Final Chorus** | Everything (full orchestra/band + choir + effects) | Maximum saturation |
| **Outro** | 1-2 nhạc cụ (mirror intro or single voice) | Resolution, bookend |

**Cách điều khiển trong Suno:**
*   Dùng thẻ `[]` để chỉ nhạc cụ mỗi section: `[Verse 1: fingerpicked guitar, soft upright bass]`
*   Dùng `[Instrumental break]` để chừa breathing room
*   Dùng `[stripped back, voice and piano only]` để strip down
*   Dùng `[full band, sweeping strings, choir]` để build up

### D2.5. Special Instrument Protocol (MỚI — v7.0)

> [!IMPORTANT]
> Pattern quan sát từ 5 bài viral: **1 instrument đặc biệt không có từ đầu, chỉ xuất hiện tại 1 emotional peak duy nhất** → tạo "emotional timestamp" mạnh nhất của bài. Đây không phải instrumentation layering thông thường — đây là cột mốc cảm xúc.

**Quy tắc:**
1. Mỗi bài chỉ có **tối đa 1** Special Instrument
2. Instrument này **KHÔNG xuất hiện** trong Intro, V1, V2
3. Chỉ enter tại **1 điểm duy nhất** — Chorus, Bridge, hoặc Outro — tùy Emotional Mode
4. Khi enters: phải được note rõ trong style prompt (component 8) VÀ trong `[]` tag của lyrics

**Special Instrument Menu (chọn 1):**

| Instrument | Emotional quality | Enter tại | Phù hợp Mode |
| :--- | :--- | :--- | :--- |
| **Piano** (high-register arpeggios) | Hope, elevation, resolution | Chorus hoặc Outro | A, C |
| **Glockenspiel** | Magic, wonder, childlike | Post-Chorus | B |
| **Cello** | Deep grief, intimacy, warmth | Chorus | D |
| **String pads** (sustained) | Grandeur, emotional swell | Bridge | A, B, D |
| **Second acoustic guitar** (melodic fills) | Companionship, dialogue | V2 onwards | A, B |
| **Clean electric** (ambient swells) | Distance, memory, longing | Throughout but subtle | A, C |

**Cách viết vào Style Prompt (component 8 mới):**
```
[Component 8 — Special Instrument]
A [cello/piano/glockenspiel] enters only at [section], providing [emotional description].
Example: "A solo cello enters only at the chorus, providing deep melodic counterpoint and emotional warmth."
```

**Cách viết vào Lyrics:**
```
[Chorus]
[cello enters]
The faded blue blanket is warm in the night...
```

### D3. The Art of Contrast — 7 Loại Contrast

Mỗi bài hát phải sử dụng **ít nhất 3/7 loại contrast** sau:

1. **Volume contrast:** Quiet verse → loud chorus
2. **Density contrast:** Sparse instrumentation → dense layered sound
3. **Rhythmic contrast:** Slow rubato verse → driving rhythmic chorus
4. **Register contrast:** Low vocal range verse → high soaring chorus
5. **Texture contrast:** Dry close-mic → wet spacious reverb
6. **Tonal contrast:** Minor/dark verse → major/bright chorus (hoặc ngược lại)
7. **Vocal contrast:** Solo voice → full choir/harmonies

---

## PHẦN E — GROOVE & RHYTHM MASTERY (MỚI)

> Groove là cái khiến người nghe GÕ TAY, LẮC ĐẦU, PHIÊU THEO. Không có groove = nhạc nền, không phải bài hát.

### E1. Rhythmic Feel Templates

Chọn rhythmic feel phù hợp concept:

| Rhythmic Feel | Đặc tính | Phù hợp concept |
| :--- | :--- | :--- |
| **Straight 4/4** | Ổn định, vững chãi, powerful | Rock, pop, anthemic |
| **Swung/Shuffle** | Bluesy, relaxed, warm | Blues, jazz, soul, country |
| **Rolling 6/8** | Sóng, waltz, flowing | Celtic, oceanic, pastoral |
| **Syncopated** | Off-beat, unexpected, groovy | R&B, funk, modern folk-pop |
| **March/Military** | Determined, epic, forward | Cinematic, anthemic, war stories |
| **Rubato/Free** | Floating, dreamlike, intimate | Art songs, spoken word, bridges |
| **Driving 8th notes** | Urgent, relentless, building | Post-rock, indie, build-up sections |
| **Waltz 3/4** | Elegant, nostalgic, dancing | European, old-world, romance |
| **Reggae/Half-time** | Laid-back, spacious, warm | Island stories, relaxed vibes |

### E2. Percussion Strategy

Percussion không chỉ là "brush snare" hay "bodhrán." Nó phải DRIVE bài hát:

**Quy tắc:**
1. **Intro/Verse 1:** Percussion minimal hoặc không có → tạo expectation.
2. **Pre-Chorus:** Percussion enters hoặc intensifies → build anticipation.
3. **Chorus:** Full percussion locks in → groove đỉnh điểm.
4. **Bridge:** Strip percussion xuống hoặc đổi pattern hoàn toàn → surprise.
5. **Final Chorus:** Percussion ở mức mạnh nhất + thêm fills/flourishes.

**Style tags cho percussion:**
*   Subtle: `soft brushed snare`, `gentle finger percussion`, `light hand claps`
*   Medium: `steady rim clicks`, `warm kick drum`, `brushed hi-hat groove`
*   Driving: `driving drum groove`, `punchy kick and snare`, `relentless bodhrán beat`
*   Epic: `thundering tribal drums`, `massive cinematic percussion`, `pounding floor toms`

### E3. Cách viết Lyrics tạo Groove

Lyrics **tự chúng nó** có nhịp. Chọn từ và sắp xếp từ đúng cách → Suno sẽ tạo groove tự nhiên:

1. **Stress pattern consistency:** Giữ cùng pattern nhấn qua nhiều dòng.
   *   ✅ `The WINdow KNOWS your SHAPE` / `The GARden KEEPS your NAME` (da-DA-da-DA-da-DA)
   *   ❌ `Window shape` / `The old garden still remembers keeping names` (không pattern)

2. **Percussive word choice:** Dùng từ có phụ âm mạnh khi cần drive.
   *   Từ mạnh: *break, kick, tap, crack, click, stomp, clap, beat, cut, strike*
   *   Từ mềm: *flow, sway, melt, hum, breathe, drift, float, sweep*

3. **Rhythmic repetition:** Lặp cùng rhythmic motif tạo groove.
   *   `Brick by brick, the wall came down` → `Stone by stone, the road was found` (cùng pattern)

---

## PHẦN F — KIỂM SOÁT KỸ THUẬT SUNO (SUNO TECHNICAL CONTROL)

### F1. Style Prompt — Quy tắc & Công thức

Style prompt **chỉ mô tả âm nhạc** (không kể video/story).

**Quy chuẩn mới (Suno Native Format):**
Không dùng các thẻ tags rời rạc (comma-separated). Hãy viết thành các **câu văn xuôi hoàn chỉnh (Natural Language)**, tập trung 100% vào chuyên môn âm nhạc (musicology). Phân tích cấu trúc chuẩn của Suno gồm **8 thành phần** (component 8 là mới từ v7.0):

1. **Genre & Core Elements:** Liệt kê thể loại, các nhạc cụ chính và loại giọng hát. (VD: *Indie folk ballad, Acoustic guitar, upright bass, drums, piano, and male vocals,*)
2. **Tempo & Rhythm Foundation:** Chỉ định nhịp điệu, Time signature, BPM và Key thông qua một nhạc cụ giữ nhịp chính. (VD: *The acoustic guitar plays a steady fingerstyle pattern in 4/4 time at 82 BPM in the key of G major,*)
3. **Bass / Lower Register:** Mô tả hành vi và âm sắc của dải trầm. (VD: *The upright bass provides melodic counterpoint with a warm, woody tone,*)
4. **Percussion Details:** Chi tiết hóa bộ gõ. (VD: *Drums feature a light, shuffling snare played with brushes and a soft kick on beats 1 and 3,*)
5. **Harmonic/Color Instruments:** Mô tả cách các nhạc cụ giai điệu/hòa âm hoạt động. (VD: *A clean piano enters with sparse, high-register chords,*)
6. **Vocal Performance & Harmonies:** Mô tả âm sắc giọng hát chính và cách bè. (VD: *The male lead vocal is intimate and breathy, occasionally layering into three-part folk harmonies during the chorus,*)
7. **Overall Arrangement/Dynamics:** Mô tả tổng thể bản phối. (VD: *The arrangement is organic and dynamic, with instruments entering and exiting to build texture.*)
8. **Special Instrument Entry (MỚI v7.0):** *[Optional nhưng STRONGLY RECOMMENDED cho folk niche]* Mô tả 1 instrument duy nhất enter muộn để đánh dấu emotional peak. (VD: *A solo cello enters only at the chorus, providing deep melodic warmth and emotional counterpoint.* HOẶC *A piano enters only in the final outro, signaling the pivot from grief to hope.*)

**Công thức tổng quát:**
Viết thành một đoạn văn (khoảng 500-800 ký tự) nối tiếp nhau mô tả lần lượt 7-8 yếu tố trên.

**Ví dụ Style Prompt v7.0 (Suno Native Format — với component 8):**
```
Indie folk ballad, Acoustic guitar, upright bass, drums, piano, and male vocals, The acoustic guitar plays a steady fingerstyle pattern in 4/4 time at 82 BPM in the key of G major, The upright bass provides melodic counterpoint with a warm, woody tone, Drums feature a light, shuffling snare played with brushes and a soft kick on beats 1 and 3, A clean piano enters with sparse, high-register chords, The male lead vocal is intimate and breathy, occasionally layering into three-part folk harmonies during the chorus, The arrangement is organic and dynamic, with instruments entering and exiting to build texture, A solo cello enters only at the final chorus, providing deep melodic warmth as the emotional peak.
```

### F2. Vocal Persona & Signature Sound Motif

*   **Vocal Persona:** Xây dựng **nhân cách giọng hát** cụ thể. Tránh giọng pop teen, belting cực đoan, hoặc robot.
    *   *Ví dụ tốt:* mature male baritone with a warm, weathered tone; older male storyteller vocal, sincere and close-mic'd; gentle female alto (intimate and nostalgic); old-radio crooner voice; crystalline soprano layered in harmony.
*   **Signature Sound Motif:** Khi phù hợp, thêm 1 âm thanh đặc trưng tinh tế.
    *   *Ví dụ:* coffee cup ping, old clock tick, paper rustle, wooden chair scrape, soft church bell, distant screen door creak, wind through garden leaves, ocean wave crash, hammer on anvil, typewriter click.

### F3. LYRICS LÀ CẦN GẠT SỐ 1 (LYRICS IS THE PRIMARY CONTROL)

> [!IMPORTANT]
> Style Prompt chỉ đặt "khung trời" (genre, mood, vocal). **Lyrics** mới là thứ quyết định **100% cách Suno hát**: nhịp nhanh/chậm, nhấn từ nào, ngắt hơi ở đâu, bè ra sao, cảm xúc thế nào.

#### Bảng tra cứu nhanh: "Muốn X → Làm Y trong Lyrics"

| Muốn đạt hiệu ứng gì? | Kỹ thuật trong Lyrics | Ví dụ |
| :--- | :--- | :--- |
| **Hát chậm lại, nhấn từng từ** | Tách dòng ngắn (5-7 từ/dòng) + dấu ba chấm | `The old road... still remembers` |
| **Hát nhanh, dồn dập** | Gộp dòng dài liền mạch (10-14 từ) | `The house and all its memories are thrive under my restless care` |
| **Tạo nhịp thở, ngập ngừng** | Dấu ba chấm `...` | `I almost called your name...` |
| **Nhấn mạnh 1 từ cảm xúc** | VIẾT HOA chỉ 1 từ | `I am STILL here` |
| **Kéo dài ngân giọng** | Lặp nguyên âm cuối từ | `mineeeee`, `hoooome` |
| **Thêm bè nhẹ / vọng lại** | Ngoặc đơn `()` | `The garden kept your name (kept your name)` |
| **Giọng nghẹn ngào** | Thẻ cảm xúc `[]` trước dòng | `[crying voice]` |
| **Tiếng thở** | Breath tag `[]` | `[sigh]`, `[deep breath]` |
| **Chuyển giọng (duet)** | Thẻ tên nhân vật `[]` | `[John]` ... `[Jane]` ... `[Both]` |
| **Solo nhạc cụ** | Thẻ nhạc cụ trên dòng riêng | `[instrumental break, saxophone]` |
| **Đổi rhythm** | Thay đổi kiểu spacing giữa sections | Verse: dòng dài → Chorus: dòng ngắn hơn, rhythmic |
| **Đặc tả phong cách đoạn nhạc** | Dấu hai chấm `:` trong `[]` | `[Bridge: haunting, slow, cello only]` |
| **Ad-lib / tiếng đệm** | `()` với nguyên âm | `(Ohhh-ohhh)`, `(Mmm-hmm)` |

#### Quy tắc Markup tuyệt đối

*   `()` = backing vocals, ad-libs, hums. **KHÔNG** để trống toàn bài — thiếu `()` = bài hát phẳng lỳ.
*   `[]` = structural tags + performance tags. **KHÔNG** viết chỉ dẫn quá mơ hồ.
*   **KHÔNG** dùng `{}` hoặc `<>`.

#### Quy tắc Spacing & Dấu câu — BẮT BUỘC

*   **Dấu phẩy `,`** = hát liền, cùng nhóm nhạc.
*   **Dấu chấm `.`** = kết thúc ý, ngắt hơi rõ ràng.
*   **Dòng trống** giữa 2 đoạn = Suno tự động thay đổi beat/rhythm.

> [!WARNING]
> **Thiếu spacing thay đổi = bài hát phẳng lỳ, monotone từ đầu đến cuối.** Mỗi bài hát BẮT BUỘC phải có ít nhất 2-3 kiểu spacing khác nhau giữa các phân đoạn.

### F4. Meter, Stress & Singability — Line Length Rules (CẬP NHẬT)

> [!IMPORTANT]
> **Thay đổi lớn so với v5.0:** Bỏ quy tắc verse 2-3 từ/dòng. Dòng quá ngắn giết melody.

**Quy tắc Line Length BẮT BUỘC:**

| Section | Số từ/dòng | Lý do |
| :--- | :--- | :--- |
| **Verse** | **5-10 từ** (trung bình 7) | Đủ dài để melody phát triển arc, đủ ngắn để intimate |
| **Pre-Chorus** | **6-12 từ** (trung bình 8) | Dài hơn chút để tạo momentum building |
| **Chorus** | **6-10 từ** (trung bình 8) | Đủ dài cho melodic hook, đủ ngắn để memorable |
| **Bridge** | **5-10 từ** (tự do hơn) | Được phép đổi pattern hoàn toàn |
| **Hook line** | **≥ 7 từ** | BẮT BUỘC: melody cần đủ nốt để tạo earworm arc |

**Các dòng chorus song song phải có số âm tiết và mẫu nhấn tương đương:**

| ❌ Bad Meter (Suno sẽ vấp) | ✅ Good Meter (Suno hát mượt) |
| :--- | :--- |
| *I looked at the old photo on the wooden table and cried* (14 syl) | *The dusty photo whispers from the floor* (8 syl) |
| *Cold* (1 syl) | *The fading light behind the door* (8 syl) |

**Nguyên tắc "Long-Short Alternation":**
Xen kẽ dòng dài và dòng ngắn hơn trong verse để tạo nhịp thở tự nhiên. Không phải tất cả dòng cùng độ dài.

```
The morning caught your cup again          (8 syl — long)
a circle where the coffee dried            (8 syl — long)
I traced the rim                           (4 syl — short, breathing)
and felt your hand still warm              (6 syl — medium, resolve)
```

**Nguyên tắc "Breathing Room":**
Cứ mỗi 4-6 dòng trong verse nên có 1 dòng ngắn hơn, hoặc theo sau bởi `[instrumental fill]`.

**Vowel Openness Rule (BẮT BUỘC — mới v8.0):**

Nốt cao của melody (climax dòng, cuối chorus) PHẢI rơi vào nguyên âm Mửe. Nếu rơi vào nguyên âm đÓNG → Suno hát vẻ, ngoẹo giọng, mất cảm xúc.

| Loại | Nguyên âm | Âm thanh | Dùng ở nốt cao? |
|---|---|---|---|
| **Mửe (open)** | AH, OH, AY, OW, AW | Mườn gào, dễ kéo dài | ✅ THỢI ĐIỂM |
| **Nửa mửe** | EH, UH, EE, OO | Được, nhưng kém hơn | ⚠໵ ĐƯỢC NẺu CẦN |
| **ĐÓNG (closed)** | IH, IM, IN, IT, IG, -NK | Nghẹt, bị cắt | ❌ TRÁNH Ở NốT CAO |

**Ví dụ:**
```
❌  "I still think of him"    → nốt cao rơi vào "him" (closed -IM) → Suno cắt đuột
✅  "I still call his name"   → nốt cao rơi vào "name" (open AY) → Suno kéo dài mườn

❌  "the garden in the dark" → nốt cao rơi vào "dark" (closed -RK) → Suno đương ngoẹo
✅  "the garden full of light" → nốt cao rơi vào "light" (open AY/I) → bay len
```

**Singability Self-Test (chạy trước khi submit):**

Hát thử từng dòng chorus theo giai điệu dự định. Đánh dấu bất kỳ chỗ nào:

```
☐ Miệng cảm giác gưƣng té khi hát → consonant cluster quá dày (VD: "strengths", "sixths")
☐ Giọng bị nhặt xuống cuối dòng → nguyên âm đóng, đổi sang từ có nguyên âm mửe
☐ Phải nghế hơi giữa chừng mà không có dấu câu nào → dòng quá dài, cắt
☐ Đoạn nào khó nhớ sau 1 lần đọc → không có rhythmic anchor, viết lại
☐ Hai dòng liền có cùng điểm ngắng hơi (cùng syllable count và cùng vowel) → mónótone, đổi 1 trong 2
```

> [!CAUTION]
> Nếu bất kỳ ô nào bị check → sửa trước khi tiếp tục. Không submit lyrics chưa qua Singability Test cho Suno.

### F5. Rhyme Rules — Anti-Mechanical

> [!IMPORTANT]
> **VẦN = ÂM THANH, KHÔNG PHẢI CHỮ VIẾT**
> Đây là nguyên tắc nền tảng. AI hay nhầm vần theo mắt (cùng chữ cuối) thay vì vần theo tai (cùng âm cuối). Khi hát, người nghe nghe âm — không đọc chữ.

**Định nghĩa đúng của vần:**
Hai từ vần với nhau khi **âm nguyên âm nhấn + mọi thứ sau đó** nghe giống nhau.

```
"rain" / "pain"   → cùng âm /AYN/  → ✅ vần
"love" / "move"   → tận -ove giống nhau NHƯNG âm khác (/ʌV/ vs /uːV/) → ❌ KHÔNG vần
"home" / "alone"  → âm /OHM/ vs /OHN/ — gần giống → ✅ near rhyme (vần gần)
"light" / "write" → âm /AYT/ vs /AYT/ → ✅ vần (dù chữ khác hoàn toàn)
"word"  / "heard" → âm /ɜːRD/ vs /ɜːRD/ → ✅ vần (dù cách đánh vần khác)
```

**Bẫy phổ biến nhất của AI khi viết lyrics:**

| Cặp từ | Nhìn thì vần? | Nghe thì vần? | Ghi chú |
|---|---|---|---|
| `love / move` | ✅ (cùng -ove) | ❌ | Âm khác: /ʌv/ vs /uːv/ |
| `blood / food` | ✅ (cùng -ood) | ❌ | Âm khác: /ʌd/ vs /uːd/ |
| `word / lord` | ❌ (chữ khác) | ✅ | Âm giống: /ɜːrd/ ≈ /ɔːrd/ (near rhyme) |
| `night / white` | ❌ (chữ khác) | ✅ | Âm giống: /AYT/ = /AYT/ |
| `said / dead` | ❌ (chữ khác) | ✅ | Âm giống: /ɛd/ = /ɛd/ |
| `gone / bone` | ✅ (cùng -one) | ❌ | Âm khác: /ɒn/ vs /oʊn/ |

**Cách AI kiểm tra vần — So sánh IPA:**
Với mỗi cặp từ nghi ngờ, tra IPA phonetic của cả 2 từ, sau đó so sánh **phần từ nguyên âm nhấn trở về sau**:

```
Bước 1: Xác định nguyên âm nhấn của mỗi từ
Bước 2: Lấy âm từ đó đến hết từ (ký hiệu IPA)
Bước 3: So sánh 2 chuỗi âm đó

→ Giống nhau hoàn toàn = perfect rhyme
→ Gần giống (cùng nguyên âm, khác phụ âm cuối 1 chút) = near rhyme
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
→ /oʊn/ ≈ /oʊd/ (cùng nguyên âm, khác phụ âm cuối) → NEAR RHYME ✅
```


---

Trộn lẫn **vần chính xác** với **vần gần đúng** để tránh cảm giác thơ trẻ con.

*   **Near Rhymes (vần gần):** *home / alone*, *stone / road*, *wind / skin*, *rise / light* — âm cuối gần giống nhau, không đồng nhất hoàn toàn.
*   **Internal Rhyming (vần trong dòng):** *The **cup** was chipped, the tea was **hot**, I sat upon the porch and **thought*** — vần xuất hiện giữa dòng, không chỉ cuối dòng.


**Rhyme Scheme Map (BẮT BUỘC chọn trước khi viết):**

Không viết thiếu scheme. Chọn 1 scheme cho Verse và 1 scheme cho Chorus trước, rồi viết dồn theo.

| Scheme | Pattern | Cảm giác | Dùng khi nào |
|---|---|---|---|
| **ABAB** | dòng 1↔dòng 3, dòng 2↔dòng 4 | Cân bằng, folk classic | Verse có 4 dòng, narrative rõ ràng |
| **ABCB** | chỉ dòng 2↔dòng 4 vần, dòng 1&3 tự do | Tự nhiên, không gượng | Mặc định cho verse (dễ viết nhất, ít máy móc nhất) |
| **AABB** | cặp dòng vần liền nhau | Vui, dứt khoát | Chorus nghe trực tiếp, hook bắt tai |
| **AAAA** | tất cả cùng vần | Mạnh, ám ảnh | Bridge nhấn mạnh, lầu vựng (dùng tiết kiệm) |
| **ABA** (3 dòng) | dòng 1↔dòng 3, dòng 2 tự do | Âm ư, hé mở | Pre-chorus ngắn, cầu nối cảm xúc |
| **Không vần** | không vần chút nào | Thơ tự do, spoken-word | Bridge nội tâm rất sâu, phải đặc biệt chủ ý |

**Quy tắc phối scheme:**
- Verse: dùng ABCB (tự nhiên) hoặc ABAB (cân bằng)
- Chorus: dùng AABB hoặc ABAB — nếu chorus là 4 dòng
- Bridge: thường ABA hoặc không vần hẳn
- **Không đổi scheme giữa Chorus 1 và Chorus 2** — bị mất cảm giác quen thuộc

**Consonant Landing Rule (BẮT BUỘC — mới v8.0):**

Suno xử lý phụ âm cuối dòng khác nhau. Nếu dòng kết bằng phụ âm cứng (hard stop) → Suno cắt đuột, mất vần khi nghe dù bảng chữ trông có vần.

| Phụ âm cuối | Loại | Nhạn xét | Dùng cuối dòng vần? |
|---|---|---|---|
| -N, -M, -L, -NG | Soft nasal/liquid | Vang rơi, Suno kéo ra được | ✅ TỐT |
| -R | Liquid (US English) | Mờ, giai điệu vẫn được | ✅ ĐƯỢC |
| -D, -Z, -V | Soft stop | Chấp nhận được | ⚠໵ OK |
| **-T, -K, -P, -CK** | Hard stop | Cắt đứt melody | ❌ HẠN CHừe CUỐI DÒNG VẦN |
| **-ST, -XT, -NK, -ND** | Cluster | Ngặt giọng, mất vang | ❌ KHÔNG DÙNG CUỐI DÒNG |

**Ví dụ:**
```
❌  "...the porch in the dark"  → cuối -RK = hard, Suno cắt đứt
✅  "...the porch in the rain"  → cuối -N = nasal, Suno vang rơi tự nhiên

❌  "...we built"              → cuối -LT = cluster, gượng
✅  "...we made"              → cuối -D = soft, mườn hơn
```

**Anti-Mechanical Rhyme Test (BẮT BUỘC):**
1.  Đọc to chorus — đoán được 100% từ vần tiếp theo → quá máy móc, sửa lại.
2.  >60% là perfect rhymes → bẻ một nửa sang near rhymes.
3.  Từ đó được chọn CHỈ VÌ nó vần? → Xóa và viết lại.
4.  Cùng cặp vần xuất hiện ở cả Verse và Chorus? → Đổi một bên.

### F6. Hook & Chorus Rules (CẬP NHẬT)

**Hook criteria (đã mở rộng):**
*   **Lyrical:** Singable, sticky, emotionally loaded, quotable, unique.
*   **Melodic:** Có melodic leap hoặc contour đặc biệt, nguyên âm mở ở nốt cao.
*   **Rhythmic:** Có rhythmic pattern bắt tai, syncopation, hoặc repetition pattern.

**Hook placement:** Dòng đầu chorus, dòng cuối chorus, hoặc cả hai. Có thể vang nhẹ trong outro.

**Quy tắc Chorus — KHÔNG LẶP NGUYÊN SI (CẬP NHẬT QUAN TRỌNG):**

> [!WARNING]
> **Chorus KHÔNG ĐƯỢC lặp nguyên si quá 2 lần.** Mỗi lần chorus xuất hiện lại phải thay đổi ≥ 1 trong các yếu tố sau:

| Lần lặp | Thay đổi bắt buộc |
| :--- | :--- |
| **Chorus 1** | Baseline — lyrics, arrangement, intensity gốc |
| **Chorus 2** | Thay ≥ 1: (a) 1-2 dòng lyrics mới, HOẶC (b) thêm nhạc cụ/bè, HOẶC (c) vocal intensity tăng |
| **Final Chorus** | Thay ≥ 2: (a) 2-4 dòng lyrics sâu hơn, VÀ (b) arrangement đầy đủ nhất, VÀ/HOẶC (c) key change/modulation, VÀ/HOẶC (d) emotional peak vocal |

**Final Chorus Deepening (BẮT BUỘC):**
*   Chorus 1: Vật gợi lại ký ức.
*   Chorus 2: Vật tiết lộ tình yêu thực sự có ý nghĩa gì.
*   Final Chorus: Vật đưa người đã mất trở lại gần bên — hoặc chuyển hóa ý nghĩa hoàn toàn.

### F6.5. Anti-Repetition Doctrine — Không Lặp Lại Lời Nguyên Si

> [!IMPORTANT]
> **Lặp lại lời nguyên si = retention killer.** Người nghe 45+ nhận ra ngay khi bài hát "tái chế" chính nó. Một khi họ cảm thấy "đã nghe rồi" → họ bỏ qua, skip, hoặc rời đi. Rule này áp dụng cho **toàn bộ bài hát**, không chỉ chorus.

#### Quy tắc tổng quát: Mỗi lần lặp = phải trả giá bằng 1 thay đổi

Bất kỳ section nào xuất hiện lần 2 trở đi **BẮT BUỘC phải khác** version đầu tiên theo ít nhất 1 trong các cách sau:

| Cách thay đổi | Ví dụ cụ thể |
|---|---|
| **Thay ≥ 1 dòng lyrics** | Verse 2 giữ melody nhưng đổi hình ảnh, đổi vật thể, đổi góc nhìn |
| **Thay emotional register** | Verse 1 hát như hỏi → Verse 2 hát như nhớ lại / chấp nhận |
| **Thay perspective** | Từ "tôi" sang "anh/cô ấy" hoặc "chúng ta" |
| **Thay thời gian** | Verse 1 = hiện tại → Verse 2 = quá khứ cụ thể |
| **Thay 1 chi tiết giác quan trọng tâm** | Verse 1: mùi cà phê → Verse 2: tiếng ghế kéo |
| **Thay 1 object** | Verse 1: chiếc cốc → Verse 2: chiếc áo khoác trên móc |

#### Bảng quy tắc chi tiết theo section

| Section | Rule |
|---|---|
| **Verse 1 → Verse 2** | **KHÔNG được lặp nguyên bất kỳ dòng nào**. Phải thay ≥ 50% số dòng bằng hình ảnh/góc nhìn mới. Verse 2 phải đào sâu hơn câu chuyện, không phải kể lại. |
| **Pre-Chorus 1 → Pre-Chorus 2** | Có thể giữ cùng structure, nhưng phải thay ≥ 1 dòng cuối để tạo cảm giác escalation. |
| **Chorus 1 → Chorus 2 → Final Chorus** | Xem F6 — mỗi lần phải thay ≥ 1 yếu tố, Final Chorus thay ≥ 2. |
| **Backing vocals `()`** | Cùng 1 cụm backing vocal không được xuất hiện quá 3 lần nguyên si trong cả bài. Xoay vòng giữa `(ohhh)`, `(mmm-hmm)`, `(yeah)`, hoặc bè theo hook. |
| **Bridge** | **KHÔNG BAO GIỜ** lặp lại nội dung đã có ở Verse hoặc Chorus. Bridge phải mở ra góc nhìn mới hoặc moment của sự thay đổi nội tâm. |

#### Cách viết Verse 2 không lặp (quan trọng nhất)

Verse 2 là nơi bài hát dễ "lười" nhất. Hai cách sai phổ biến:
- ❌ **Lặp nguyên**: Copy Verse 1, chỉ đổi 1-2 từ.
- ❌ **Paraphrase**: Nói lại cùng ý bằng từ khác. Người nghe vẫn cảm thấy "đã nghe rồi."

Verse 2 đúng phải:
- ✅ **Zoom in** — Verse 1 thấy ngôi nhà → Verse 2 thấy cụ thể góc bếp, chiếc ghế, đôi tay.
- ✅ **Flip time** — Verse 1 = hôm nay → Verse 2 = ngày xưa cụ thể.
- ✅ **New witness** — Verse 1 = tôi nhớ → Verse 2 = căn phòng nhớ thay cho tôi.
- ✅ **Add cost** — Verse 1 = mô tả sự vắng mặt → Verse 2 = mô tả hậu quả của sự vắng mặt đó.

#### Retention Impact Rule

> Người nghe trung bình (45+) trên YouTube quyết định ở lại hay rời đi trong **40–90 giây đầu** và tại **mỗi điểm lặp lại**. Bất kỳ lần nào họ cảm thấy "bài này đang lặp lại rồi" → xác suất drop-off tăng 30–50%.

Vì vậy: **Mỗi lần lặp về cấu trúc phải được "trả giá" bằng sự đào sâu về nội dung.** Cấu trúc lặp = OK. Lời lặp = không bao giờ.

---

### F7. Song Structure Library (CẬP NHẬT v7.0)

**BƯỚC 0 — Time Scope Selection (MỚI):** Xác định khung thời gian câu chuyện TRƯỚC KHI chọn structure.

| Time Scope | Mô tả | Ảnh hưởng đến structure |
| :--- | :--- | :--- |
| **Single Moment** | Một khoảnh khắc duy nhất (buổi sáng, một buổi chiều) | Verse đi sâu vào chi tiết, không cần nhiều verses |
| **Single Day Arc** | Từ sáng đến tối — 3 chorus = 3 mốc thời gian | Chorus lyrics phải evolve theo thời gian (xem Evolving Chorus) |
| **Universal "Any Moment"** | Không gắn thời điểm cụ thể — luôn luôn đúng | Hook phải anchor bằng 1 object/truth phổ quát |
| **Entire Lifespan** | Từ trẻ đến già, từ sinh đến chết | Nhiều verses = chapters, phải có time jump rõ ràng |

**KHÔNG mặc định dùng cùng 1 cấu trúc.** Chọn cấu trúc phù hợp concept VÀ độ dài đã chọn ở A1.

#### 🕐 Cấu trúc 4 PHÚT (Full Version — như hiện tại)

| Cấu trúc | Pattern | Khi nào dùng |
| :--- | :--- | :--- |
| **Classic Pop** | V-PC-C-V-PC-C-B-C | Bài hát cần hook mạnh, mainstream appeal |
| **Storyteller** | V-V-C-V-V-C-B-C | Khi câu chuyện dài, cần nhiều verse để kể |
| **Chorus-First** | C-V-C-V-B-C | Khi hook cực mạnh, muốn đánh thẳng ngay |
| **AABA** | V-V-B-V | Ballad cổ điển, jazz standard, story-driven |
| **Double Chorus Climax** | V-C-V-C-B-C-C | Climax bùng nổ với double chorus cuối |
| **Through-Composed** | A-B-C-D-E | Mỗi đoạn mới hoàn toàn — cinematic, progressive |
| **Build & Release** | V-V-V-BUILD-DROP-V-OUTRO | Post-rock, cinematic ambient, emotional explosion |
| **Verse-Refrain** | V(+R)-V(+R)-B-V(+R) | Folk truyền thống, refrain ngắn thay vì chorus đầy đủ |
| **Evolving Chorus** | V-C1-V-C2-B-C3-OUTRO | **MỚI** — 3 chorus có lyrics khác nhau hoàn toàn, cùng melody |

**Evolving Chorus Structure — Hướng dẫn chi tiết (MỚI v7.0):**

> Dùng khi Time Scope = **Single Day Arc** hoặc **Entire Lifespan**. Melody chorus giữ nguyên, chỉ lyrics thay đổi để kể narrative tiến triển qua thời gian.

| Chorus | Thời điểm | Nhiệm vụ lyrics |
| :--- | :--- | :--- |
| **C1** | Dawn / Trẻ / Bắt đầu | Thiết lập thế giới — ai, ở đâu, cảm giác gì |
| **C2** | Midday / Trưởng thành / Giữa chặng | Deepening — đào sâu hơn vào relationship/place |
| **C3** | Dusk / Già / Kết thúc | Emotional payoff — resolution, acceptance, goodbye |

*Ví dụ từ corpus: Bài "Old Farm Day" — 3 chorus kể hành trình từ bình minh → trưa → hoàng hôn qua cùng 1 trang trại.*

#### ⚡ Cấu trúc 2 PHÚT (Short Version — cô đọng, test retention)

> [!IMPORTANT]
> **Nguyên tắc 2 phút:** Đi thẳng vào hook nhanh nhất có thể. Không Bridge. Không Final Chorus riêng. Mỗi section PHẢI kiếm được chỗ đứng của nó — nếu cắt ra vẫn OK thì đừng có để vào.

| Cấu trúc | Pattern | Khi nào dùng |
| :--- | :--- | :--- |
| **Hook-First Short** | C-V-C-V-C-OUTRO | Hook cực mạnh, muốn cắm vào tai ngay giây đầu |
| **Tight Ballad** | V-C-V-C-OUTRO | Câu chuyện đơn giản, 1 hình ảnh trung tâm, emotional đơn |
| **Verse-Chorus Loop** | V-PC-C-V-C-OUTRO | Cần pre-chorus tạo tension, vẫn giữ được nhịp gọn |
| **Stripped Storyteller** | V-V-C-C-OUTRO | Kể xong câu chuyện, rồi hit chorus 2 lần liên tiếp để đọng |

**Ràng buộc cứng cho 2 phút:**
- Target lyrics: **20-30 dòng** (không phải 40-60)
- Số sections: **tối đa 5** (không tính Intro)
- Intro: **4-8 giây** (thẻ `[Short Intro]` hoặc không có Intro)
- Chorus: **xuất hiện lần đầu trong 45 giây đầu** — không được để người nghe chờ quá lâu
- Không Bridge (Bridge chiếm ~30-45 giây — quá xa xỉ với bài 2 phút)
- Không Final Chorus riêng biệt — Chorus 2 là điểm đỉnh, Outro là đủ
- **Verse 2 PHẢI ngắn hơn hoặc bằng Verse 1** (không mở rộng story ở đây)

**Adaptation từ bài 4 phút → 2 phút (nếu cần rút gọn):**
1. Bỏ Bridge
2. Gộp Pre-Chorus vào Chorus (nếu có PC)
3. Rút Verse 1 và Verse 2 xuống còn 4-6 dòng mỗi verse thay vì 8-10
4. Chorus chỉ 4-6 dòng, cực kỳ memorable
5. Outro ngắn: 2-4 dòng hoặc `[instrumental fade]`

---

**Quy tắc "Surprise Element" (áp dụng cho cả 2 phiên bản):**
Mỗi bài phải có **≥ 1 moment bất ngờ structural** — ví dụ: instrumental solo bất ngờ, key change, texture shift hoàn toàn, silence trước climax, hoặc coda không ai ngờ tới.

### F8. Advanced Cinematic Techniques

1. **Genre Fusion:** Kết hợp hai không gian đối lập (ví dụ: Acoustic Folk + Sub-bass Electronic → "Rhythmic friction").
2. **Khoảng thở:** Chủ động nhồi `[Pause]`, `[Beat Breakdown]`, hoặc `[Silence]` trước chuyển đoạn.
3. **The Anti-Drop:** Thay build-up ồn ào → `[Music abruptly stops]` → chorus chỉ bằng giọng và sub-bass.
4. **Performance Cues:** `[Sigh]`, `[Breathless]`, `[Spoken]`, `[voice crack]` — làm AI "con người" hơn.
5. **Rubato:** Dấu ba chấm `...` và ngắt dòng để ép AI hát lơi nhịp.

### F8.5. Ending Signature Library (MỚI — v7.0)

> [!IMPORTANT]
> Ending là khoảnh khắc người nghe quyết định **comment, share, hay replay**. YouTube đo completion rate — bài có ending mạnh = người nghe nghe đến giây cuối = algorithmic signal. Chọn 1 trong 4 kiểu ending dưới đây dựa trên Emotional Mode đã chọn ở B2.5.

| Ending Type | Cấu trúc | Emotional Effect | Dùng với Mode |
| :--- | :--- | :--- | :--- |
| **Whispered Coda** | Guitar fade → 1 dòng whisper/spoken cuối | Intimate closure, "leaning in" feeling | A, B |
| **CTA Outro** | Piano enters → lyrics là instructions trực tiếp ("sit a little longer") | Disturbing → action → "I did this" comments | C |
| **Incomplete Fragment** | Guitar fade → 1-2 dòng lyrics không hoàn chỉnh, không dấu chấm | Lingering, haunting, bài tiếp tục trong đầu | B |
| **Wordless Resolution** | Vocalizing (mmm, ooh) → Special Instrument solo → silence | Cathartic release, beyond words | D |

**Chi tiết từng Ending Type:**

**Type 1 — Whispered Coda:**
```
[acoustic guitar fades]
[whispered]
This is home
```
- Spoken/whispered sau khi nhạc fade = intimacy tột cùng
- Cảm giác như người hát đang nói thẳng vào tai người nghe
- KHÔNG hát — phải spoken hoặc whispered

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
- Piano enters để signal pivot từ reflection → action
- Lyrics phải là imperative sentences ("sit", "let", "look", "say")
- Kết bằng 1 dòng declarative anchoring thesis

**Type 3 — Incomplete Fragment:**
```
[acoustic guitar fades out]
Safer than lantern glow
Where the kind fields grow
```
- KHÔNG có dấu chấm ở cuối
- Câu không hoàn chỉnh về ngữ pháp → melody tiếp tục trong đầu người nghe
- Chỉ 2-4 dòng — không giải thích

**Type 4 — Wordless Resolution:**
```
[vocalizing melodies, cello, acoustic guitar fades out]
(Mmm-hmm-hmm)
(Ohhh-ohhh)
[cello solo]
[silence]
```
- Sau cái chết / mất mát lớn — ngôn ngữ không đủ
- Chỉ âm thanh, không lời
- Cello hoặc Special Instrument có solo cuối
- Kết bằng silence thực sự (không fade — CUT)

### F9. Dàn dựng & Phối khí

**Song ca (Duets):**
1.  Style Box: nhập `duet` hoặc `male and female vocal duet`.
2.  Lyrics Box đầu bài: `[Duet: John (male) and Jane (female)]`.
3.  Chia đoạn: `[John]`, `[Jane]`, `[Both]`. Mỗi giọng hát nguyên cả verse/chorus.

**Dàn đồng ca:** `[Multiple voice chorus, SATB]` trước điệp khúc.

**Solo nhạc cụ:** Đặt tag trên dòng độc lập: `[instrumental break, saxophone]`.

**Cao trào (EDM):** `[buildup]` → `[drop]`.

### F10. Giới hạn ký tự & Extend Hack

**Buffer Rule:** Viết lời ngắn hơn giới hạn tối đa ít nhất **500 ký tự** để chừa đất cho tags.

**Extend Hack:**
1.  Chọn điểm cắt tại khoảng lặng hoặc cuối câu hát.
2.  Style Box khi extend: giữ core genres, bỏ `[Intro]`, thêm `[Bridge]`/`[Outro]`.
3.  Lyrics Box: chỉ lyrics còn lại, bắt đầu bằng section label hiện tại.

### F11. Troubleshooting

| Vấn đề | Giải pháp |
| :--- | :--- |
| Ca sĩ hát quá nhanh/vấp | Quá nhiều syllables/dòng → viết lại ngắn hơn, thêm `...` hoặc ngắt dòng |
| Âm thanh bùng nhùng/méo | Style box quá nhiều nhạc cụ → bỏ bớt, thêm `high fidelity`, `intimate close-mic` |
| Suno phát âm sai từ | Viết phiên âm: `sewing` → `sowing`, `AI` → `A-I` |
| Suno đọc to metatag | Chỉ dẫn trong `[]` quá dài → giữ ngắn gọn |
| Instrumental có giọng hát | Viết `Instrumental` ở CẢ HAI ô: Lyrics + Style Box |
| Melody phẳng, không bắt tai | Thêm `soaring memorable melody`, `earworm hook` vào style. Đặt nguyên âm mở ở hook. |
| Bài hát monotone | Thiếu contrast → kiểm tra Energy Map, đảm bảo ≥ 3/7 loại contrast |
| Chorus không đọng | Hook line quá ngắn (< 7 từ) → viết dài hơn. Thiếu melodic leap. |

### F12. Sửa lỗi phát âm & Dịch thuật

*   **Phonetic Spelling Hack:** Viết phiên âm thay vì chính tả. `mine` → `mineeeee` để kéo dài ngân.
*   **Translation Rhyme Guard:** Khi dịch, thay đổi từ vựng nếu cần để duy trì rhyme scheme và syllable counts gốc.

---

## PHẦN G — KIỂM SOÁT CHẤT LƯỢNG (QUALITY GATES)

### G1. Anti-AI Slop — Zero Tolerance (SỬ DỤNG SKILLS)

Agent **BẮT BUỘC PHẢI CHẠY** 2 skills cho mọi bản draft:
1. **`avoid-ai-writing`**
2. **`stop-slop`**

**Quy tắc duy nhất cần nhớ:** Cấm cấu trúc 4 dòng AABB máy móc. Chủ động bẻ vần và thay đổi số dòng.

### G2. Tier 1 — Technical Gate (Checklist)

- [ ] **Anti-Repetition Doctrine tuân thủ?** Verse 2 không lặp nguyên Verse 1? Backing vocals `()` không lặp quá 3 lần? Bridge có góc nhìn mới?
- [ ] Câu chuyện đơn giản & nhân văn? Vật thể cảm xúc rõ ràng?
- [ ] Pass Cozy Healing Gate (≥ 2/4 tiêu chí)?
- [ ] **Genre phù hợp concept?** (không mặc định folk)
- [ ] STYLE 120-200 chars? Có melody quality keywords? Có groove keywords? Vocal persona rõ ràng?
- [ ] **Energy Map defined?** Contrast ratio ≥ 2x?
- [ ] **≥ 3/7 loại contrast được sử dụng?**
- [ ] Lyrics 100% tiếng Anh? **Hook pass cả 3 loại (lyrical + melodic + rhythmic)?** ≥ 2/3 đạt?
- [ ] **Line length đúng quy tắc?** Verse 5-10 từ/dòng, hook ≥ 7 từ?
- [ ] **Nguyên âm mở ở hook/chorus nốt cao?**
- [ ] Meter tự nhiên? Hình ảnh cụ thể?
- [ ] Bridge có ý nghĩa? **Bridge melody vào vùng mới?**
- [ ] **Chorus không lặp nguyên si quá 2 lần?** Final chorus deepens?
- [ ] Anti-mechanical rhyme test passed? Lyrics-vs-video separation tuân thủ?
- [ ] 40-60 dòng lyrics? Số viết bằng chữ?
- [ ] Phù hợp người lớn 45+? Ấm áp? Anti-slop scan passed?
- [ ] **Cấu trúc bài hát được chọn có chủ đích?** (không mặc định cùng 1 pattern)
- [ ] **≥ 1 surprise element structural?**

### G3. Tier 2 — Adversarial Brutality Test (BẮT BUỘC — không skip)

1.  **John Prine / Leonard Cohen Test:** Họ đọc chorus này có xấu hổ không? Có → viết lại chân chất hơn.
2.  **Poem vs Song Test:** Đọc không nhạc nghe giống thơ hay bài hát thật? Giống thơ → viết lại cho dễ hát.
3.  **Sức nặng trên giấy:** Bỏ giai điệu, đọc lời có cảm động không? Trôi tuột → rewrite.
4.  **Stranger Reaction Test:** Đọc Verse 1 cho người lạ, họ cảm thấy gì? Nhún vai → viết lại.
5.  **Dòng lấp vần:** Dòng nào viết ra CHỈ để đủ nhịp/vần? → Tiêu diệt.
6.  **Mật độ giác quan:** Tối thiểu ≥ 3 chi tiết ngửi/chạm/nhiệt độ cụ thể. < 3 → quá trừu tượng.
7.  **Comment Test:** Viewer có tự động gõ câu hook làm YouTube comment không? Không → chưa phải hook.

### G4. Tier 3 — Musicality Gate (MỚI — BẮT BUỘC)

> [!IMPORTANT]
> Gate mới này kiểm tra **NHẠC**, không chỉ lời. Đây là gate quyết định bài hát có bắt tai không.

1.  **Hum Test:** Bỏ lời đi, chỉ hum melody chorus — có bắt tai không? Nếu không hum được → melody quá phẳng.
2.  **Tap Test:** Đọc lyrics theo nhịp — có tự động gõ tay/lắc đầu không? Nếu không → thiếu groove.
3.  **Goosebump Test:** Đọc đến pre-chorus/chorus transition — có cảm giác "dâng trào" không? Nếu không → thiếu dynamic contrast.
4.  **First 10 Seconds Test:** 10 giây đầu tiên có đủ interesting để giữ người nghe không? Nếu boring → intro quá dài hoặc quá generic.
5.  **Singalong Test:** Chorus có đủ đơn giản và catchy để người nghe hát theo từ lần 2? Nếu không → quá phức tạp hoặc melody không memorable.

### G5. Lyrics Formatting Checklist (BẮT BUỘC)

- [ ] Dùng `...` và `()` hợp lý để tạo chiều sâu?
- [ ] Có ≥ 1 breath tag `[sigh]` / `[deep breath]`?
- [ ] Có ≥ 1 từ VIẾT HOA nhấn mạnh?
- [ ] Có ≥ 1 nguyên âm kéo dài (`ohhh`, `hoooome`)?
- [ ] Bridge hoặc Final Chorus có thẻ cảm xúc?
- [ ] Spacing giữa Verse và Chorus **khác nhau rõ ràng**?
- [ ] Mọi `[]` tag đều ngắn gọn?
- [ ] Có ≥ 1 đoạn `[instrumental break]` tạo breathing room?

---

## PHỤ LỤC — THƯ VIỆN THUẬT NGỮ ÂM NHẠC CHO SUNO (MUSIC GLOSSARY)

### Nhịp độ & Nhịp điệu (Tempo & Rhythm)
*   **Tempo**: Tốc độ bản nhạc (BPM). **Adagio**: 66-76 BPM. **Andante**: 76-108 BPM. **Allegro**: 120-168 BPM. **Presto**: 168-200 BPM.
*   **Rubato**: Nhịp độ tự do. **Syncopation**: Nhấn nhịp yếu/off-beat. **Polyrhythm**: Đa nhịp điệu.
*   **Groove**: Cảm giác nhịp bắt tai. **Downbeat**: Nhịp mạnh đầu ô nhịp. **Upbeat**: Nhịp trước downbeat.

### Sắc thái & Biểu cảm (Dynamics & Expression)
*   **Crescendo**: To dần. **Diminuendo**: Nhỏ dần. **Forte**: Mạnh. **Piano**: Nhẹ. **Fortissimo**: Rất mạnh. **Pianissimo**: Rất nhẹ.
*   **Staccato**: Ngắt âm. **Legato**: Liên âm. **Vibrato**: Ngân rung. **Tremolo**: Rung giật nốt.

### Cấu trúc bài hát (Song Structure)
*   **Verse** → **Pre-Chorus** → **Chorus** → **Bridge** → **Outro**.
*   **Hook**: Cụm từ/giai điệu bắt tai. **Refrain**: Câu lặp. **Break**: Tạm dừng. **Drop**: Bùng nổ (EDM).

### Giai điệu & Hòa âm (Melody & Harmony)
*   **Chord Progression**: Chuỗi hợp âm. **Major**: Tươi sáng. **Minor**: Tối, buồn.
*   **Arpeggio**: Rải hợp âm. **Counterpoint**: Đối âm. **Dissonance → Resolution**: Căng thẳng → Giải quyết.
*   **Melodic Contour**: Hình dạng giai điệu (ascending/descending/arch/leap).
*   **Interval**: Khoảng cách giữa 2 nốt. **Leap**: Nhảy quãng rộng. **Step**: Bước đi liền bậc.

### Nhạc cụ & Chất liệu (Instrumentation & Texture)
*   **Monophonic**: Đơn âm. **Homophonic**: Chủ âm. **Polyphonic**: Đa âm.
*   **Timbre**: Âm sắc. **Layering**: Chồng lớp. **Sparse**: Tinh giản. **Dense**: Dày đặc.

### Kỹ thuật giọng hát (Vocal Techniques)
*   **Falsetto**: Giọng giả thanh. **Belt**: Hát giọng ngực nội lực. **Melisma**: Luyến láy. **Crooning**: Hát thủ thỉ.
*   **Call and Response**: Đối đáp. **A Cappella**: Hát chay. **Scat**: Hát ngẫu hứng Jazz.

### Sản xuất & Hiệu ứng (Production & Effects)
*   **Reverb**: Độ vang không gian. **Delay/Echo**: Tiếng vọng. **Compression**: Nén tiếng. **Distortion**: Méo tiếng.
*   **EQ**: Cân bằng tần số. **Panning**: Định vị stereo. **Fade In/Out**: To/nhỏ dần.

### Khái niệm nâng cao (Advanced Concepts)
*   **Modulation (Key Change)**: Chuyển giọng. **Time Signature**: Số chỉ nhịp (4/4, 3/4, 6/8).
*   **Cadence**: Kết đoạn. **Ostinato**: Mô-típ lặp. **Pedal Point**: Nốt nền ngân dài.
*   **Suspension**: Giữ nốt tạo căng thẳng. **Anacrusis**: Nhịp lấy đà. **Coda**: Đoạn vĩ thanh.

---

*Bản cập nhật: 2026-06-07 | Coslient Song Development Knowledge v7.0 "Niche Intelligence"*
