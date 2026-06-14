# Clean Lyrics Rules — Coslient Project

> **Dùng khi:** Upload lyrics lên DistroKid, Bandcamp, hoặc bất kỳ platform nào yêu cầu clean lyrics.
> **Áp dụng cho:** Mọi bài nhạc từ video 41 trở đi.

---

## Quy tắc (9 rules)

| # | Rule | Ví dụ sai | Ví dụ đúng |
|---|------|-----------|-----------|
| 1 | **Chỉ viết lyrics. Không có thông tin khác.** | `Song title, artist name, genre…` | _(bỏ hết)_ |
| 2 | **Không ghi tên vocalist.** | `[Coslient]: When love walks tall` | `When love walks tall` |
| 3 | **Không có extra text (intro, chorus, social links…).** | `[Verse 1]`, `[Chorus 2x]`, `fb.com/coslient` | _(xóa hết)_ |
| 4 | **Viết ra đầy đủ các dòng lặp. Không ghi "Chorus 2x".** | `[Repeat chorus x3]` | _(chép lại 3 lần đầy đủ)_ |
| 5 | **Đầu mỗi dòng viết hoa chữ cái đầu.** | `when love walks tall` | `When love walks tall` |
| 6 | **Không dùng dấu câu cuối dòng.** | `When love walks tall.` hoặc `tall,` hoặc `tall...` | `When love walks tall` |
| 7 | **Dòng trắng chỉ dùng để phân cách verse / chorus. Không để nhiều hơn 1 dòng trắng.** | `[blank][blank]` giữa 2 câu | 1 dòng trắng duy nhất |
| 8 | **Mỗi dòng = 1 ý. Không ghi dòng quá dài.** | `The water holds your weight without asking for your name` | `The water holds your weight` / `Without asking for your name` |
| 9 | **Không kiểm duyệt từ nhạy cảm trừ khi bị bleep trong bản thu.** | `F***` | `F***` chỉ khi bị bleep; nếu không bleep thì viết thẳng |

---

## Các lỗi phổ biến cần tránh

### ❌ Section markers
```
[Verse 1]
[Pre-Chorus]
[Bridge]
[Intro: acoustic guitar...]
[Piano enters softly]
```
→ Xóa hết.

### ❌ Dấu câu cuối dòng
```
When love walks tall...    ← xóa "..."
And the years slipped away.  ← xóa "."
But look at how they PLAY!   ← xóa "!"
```
→ Dấu câu bên trong dòng (dấu phẩy, dấu nháy) thì giữ nguyên.

### ❌ Ellipsis kéo dài âm tiết
```
The waaater hooollds your weeeight   ← Suno notation
```
→ Chuẩn hóa: `The water holds your weight`

### ❌ Ký hiệu lặp
```
Chorus (x3)
Repeat verse
```
→ Viết ra đầy đủ 3 lần.

### ❌ Stage directions
```
[spoken, soft]
[sigh]
[fade out]
(mmm-hmm)
```
→ Xóa hết. Nếu "mmm-hmm" thực sự được hát thì giữ, nhưng bỏ dấu ngoặc.

### ❌ Parenthetical backing vocals
```
It takes the heavy things away (for your name)
```
→ Quyết định: nếu đó là backing vocal chính thì giữ và viết thành dòng riêng. Nếu là ghi chú thì xóa.

---

## Cấu trúc file chuẩn

**Đường dẫn:** `projects/[video_folder]/docs/03_clean_lyrics.txt`

**Format:**
```
[Dòng 1 của verse 1]
[Dòng 2 của verse 1]
[Dòng 3 của verse 1]
[Dòng 4 của verse 1]
                        ← 1 dòng trắng
[Dòng 1 của chorus]
[Dòng 2 của chorus]
                        ← 1 dòng trắng
[Dòng 1 của verse 2]
...
```

---

## Áp dụng cho project Coslient

Tất cả các file `03_clean_lyrics.txt` từ video 41–53 đã được chuẩn hóa theo rules này.

| Video | Song Title | File |
|-------|-----------|------|
| 41 | The Blue Cup by the Window | `projects/41/docs/03_clean_lyrics.txt` |
| 42a | That's How Big Love Can Be | `projects/42/docs/03_clean_lyrics_thats_how_big_love.txt` |
| 42b | When Love Walks Tall | `projects/42/docs/03_clean_lyrics_when_love_walks_tall.txt` |
| 43 | The Warmest Place in Winter | `projects/43/docs/03_clean_lyrics.txt` |
| 44 | The Summer Glass | `projects/44/docs/03_clean_lyrics.txt` |
| 45 | The Porch Paw Syndicate | `projects/45/docs/03_clean_lyrics.txt` |
| 46 | The Stars Still Sing My Name | `projects/video_046/docs/03_clean_lyrics.txt` |
| 47 | The Water Remembers | `projects/video_047/docs/03_clean_lyrics.txt` |
| 48 | Close the Door Lightly | `projects/video_048/docs/03_clean_lyrics.txt` |
| 49 | Until the Streetlights Came On | `projects/video_049/docs/03_clean_lyrics.txt` |
| 50 | Dirt on Her Hands | `projects/video_050/docs/03_clean_lyrics.txt` |
| 51 | The Water Doesn't Ask | `projects/video_051/docs/03_clean_lyrics.txt` |
| 52 | Gardeners of the Deep | `projects/video_052/docs/03_clean_lyrics.txt` |
| 53 | The Unplayed Song | `projects/video_053/docs/03_clean_lyrics.txt` |
