# Quy Trình Dựng Phim Tự Động (Automated Editing Pipeline)

Tài liệu này là **nguồn sự thật duy nhất** cho toàn bộ pipeline dựng video tự động trên CapCut thông qua MCP Palmier Pro và các script hỗ trợ.

> **Đọc kỹ toàn bộ file này trước khi bắt đầu.** Pipeline có 5 bước **bắt buộc theo thứ tự**. Không được nhảy cóc.

---

## Sơ Đồ Tổng Quan

```
[Nhạc .wav]
     │
     ▼ Bước 1
[get_transcript]  ──→  transcription.json  (word-level timestamps)
     │
     ▼ Bước 2
[analyze_beats.py]  ──→  beat_analysis.json  (scenes, lyric_context, queryParams = "")
     │
     ▼ Bước 3
[N × VisualPromptEngineer subagents]  ──→  beat_analysis.json  (queryParams đã điền)
     │
     ▼ Bước 4
[auto_edit_timeline.py]  ──→  CapCut Timeline ✅
  • search_media × N scenes  (5-tier fallback, 2-pass lyric→ambient)
  • clear timeline  →  add_clips (1 batch call)  →  mute video tracks  →  add audio
```

---

## Bước 1: Trích Xuất Transcription

**Tool:** `call_mcp_tool` → server `palmier-pro`, tool `get_transcript`  
**Input:** `clipId` của file âm thanh (ví dụ: `"Chapter Five.wav"`)  
**Output:** Lưu thành `projects/video_xxx/transcription.json`

**Yêu cầu bắt buộc:**
- File JSON phải có mảng `words` với word-level timestamps (do Whisper tạo)
- Kiểm tra `words` tồn tại và không rỗng trước khi sang Bước 2
- Nếu không có `words` → báo lỗi, không tiếp tục

---

## Bước 2: Phân Tích Beat và Tạo Scenes

**Tool:** Chạy script Python

```bash
python3 scripts/analyze_beats.py \
  --audio "projects/video_xxx/SongName.wav" \
  --transcription "projects/video_xxx/transcription.json" \
  --output "projects/video_xxx/beat_analysis.json" \
  --fps 60 \
  --min-duration 2.5
```

**Tùy chọn `--cut-style`:**
| Style | `--min-duration` tương đương | Dùng khi |
|-------|------------------------------|---------|
| `fast` | 1.0s | Chorus bùng nổ, nhịp nhanh |
| `normal` | 2.5s (mặc định) | Phần lớn bài hát |
| `slow` | 3.5s | Intro/Outro/Bridge tĩnh lặng |

**Output — Cấu trúc mỗi scene trong `beat_analysis.json`:**
```json
{
  "start_seconds": 11.317,
  "start_frame": 679,
  "end_seconds": 14.293,
  "end_frame": 857,
  "duration_frames": 178,
  "score": 0.403,
  "reasons": ["Phrase Boundary"],
  "has_vocals": true,
  "vocals_in_segment": "The July sun baked the Georgia clay",
  "lyric_context": "The July sun baked the Georgia clay",
  "queryParams": "",
  "overlap_weight": 0.48
}
```

> ⚠️ `queryParams` LÚC NÀY LÀ CHUỖI RỖNG `""`. Đây là thiết kế đúng.  
> Subagents ở Bước 3 mới điền vào. Không được tự điền tay.

---

## Bước 3: Viết queryParams Bằng VisualPromptEngineer Subagents

**Đây là bước quan trọng nhất và hay bị bỏ qua nhất.**

> 📖 Đọc đầy đủ spec tại: `flow_vn/20_visual_prompt_engineer_agent.md`

### Tóm Tắt Cách Làm:

**1. Chia scenes thành chunks (8 scenes/chunk):**
```python
CHUNK_SIZE = 8
chunks = [scenes[i:i+CHUNK_SIZE] for i in range(0, len(scenes), CHUNK_SIZE)]
# Ví dụ: 73 scenes → 10 chunks
```

**2. Spawn TẤT CẢ subagents CÙNG LÚC (song song):**
```
invoke_subagent × N (một lần, không chờ tuần tự)
  TypeName: "self"
  Role: "VisualPromptEngineer chunk K/N"
  Prompt: [template từ file 20_visual_prompt_engineer_agent.md + chunk JSON]
```

**3. Thu kết quả — mỗi subagent trả về:**
```json
[
  {"scene_index": 0, "queryParams": "slow pan across empty wheat field"},
  {"scene_index": 1, "queryParams": "close-up of cracked dry earth"}
]
```

**4. Merge vào `beat_analysis.json` và ghi đè file:**
- Dùng `scene_index` để map đúng scene
- Sau khi merge: kiểm tra KHÔNG có scene nào còn `queryParams = ""`
- Nếu có scene trống → re-spawn subagent cho chunk đó

**Sau khi Bước 3 xong, `beat_analysis.json` đã có đầy đủ `queryParams` — sẵn sàng cho Bước 3.5 + 4.**

---

## Bước 3.5: Verify Visual Index

> Index được AI **tự duy trì inline** trong Bước 04 Image Development — mỗi prompt viết xong thì append condensed entry vào `04_visual_index.txt` ngay lúc đó.  
> `summarize_visuals.py` chỉ dùng 1 lần để **backfill** nếu index chưa tồn tại (ví dụ video 57 đã có prompts từ trước).

**Verify:**
```bash
# File phải tồn tại — nếu không có → chạy lần đầu:
python3 scripts/summarize_visuals.py --project projects/video_xxx
```

**File:** `projects/video_xxx/docs/04_visual_index.txt`

**Format:**
```
#======================================================================
# GLOBAL VISUAL PALETTE (40 concepts nổi bật nhất)
#======================================================================
dry, earth, wooden, chair, boots, pecan, sapling, roots, trunk, tree, well, bucket...

P001 Intro - Wide establishing | dry, red, earth, wooden, chair
P002 Intro - Environment + Traces | boots, trowel, pecan, seed
P006 Chorus 1 - Love and growth | trunk, tree, roots, smile, sunlight
...
```

**Ai đọc file này:**

| Bước | Ai đọc | Mục đích |
|------|--------|----------|
| Bước 3 — VisualPromptEngineer | Subagent | Cross-check queryParams với palette thực tế |
| Bước 4 — auto_edit_timeline | (Tham khảo nếu cần debug) | Hiểu visual world khi xem log |

> 📖 **Nguồn tham chiếu duy nhất.** Không đọc `04_image_prompts.txt` gốc (100KB+).

---

## Bước 4: Lắp Timeline — Script Python Stateful

**Không để agent tự làm bước này** — agent không thể duy trì state qua 70+ tool calls liên tiếp → bị lặp clip.

Dùng script Python có đầy đủ state management:

```bash
# Chạy bình thường:
python3 scripts/auto_edit_timeline.py --project projects/video_xxx

# Test trước khi add thật:
python3 scripts/auto_edit_timeline.py --project projects/video_xxx --dry-run

# Custom MCP URL (nếu khác port mặc định):
python3 scripts/auto_edit_timeline.py --project projects/video_xxx --mcp-url http://127.0.0.1:19789/mcp
```

**Yêu cầu:** CapCut đang mở + Palmier Pro plugin đang chạy.  
**Không cần install thêm gì** — script chỉ dùng Python stdlib.

**Validate trước khi chạy:**
```
missing = scenes có queryParams = "" → nếu có → dừng, re-spawn subagent chunk đó
```


---

### Lớp 1 — 2-Tier Dedup: cooldown window + hard block

`search_media` trả về **source-second ranges** (moments). Mỗi moment là đoạn cụ thể trong clip cụ thể.

```
moment = { mediaRef: "clip_xyz", startSeconds: 30.5, endSeconds: 33.5 }
→ trim_start_frame = round(30.5 × fps)
→ key = ("clip_xyz", 1830)
```

**Tier 1 — Cooldown window (ưu tiên):**
```
recent_media = deque(maxlen=15)  ← sliding window 15 scenes gần nhất
→ Không dùng clip nào nằm trong recent_media
→ Sau 15 scenes, clip cũ bị evict tự động → có thể reuse
```

**Tier 2 — Hard block (fallback):**
```
used_segments = set()  ← (mediaRef, trimStartFrame) pairs
→ Tuyệt đối không dùng cùng đoạn tại cùng timestamp
→ Chỉ fallback vào Tier2 khi Tier1 hết lựa chọn
```

**Ưu điểm so với dedup cũ:**
- `used_media_refs` permanent set → block clip tốt vĩnh viễn → Tier2 reuse ngay cạnh nhau
- `deque(maxlen=15)` → cùng clip có thể xuất hiện lại sau 15 scenes → không adjacent

---

### Lớp 2 — `limit=30` để có pool lựa chọn rộng hơn

Mặc định `search_media` trả 10 kết quả. Với library lớn, dùng `limit=30`:

```
search_media(query=q, scope="visual", limit=30)
```

---

### Lớp 3 — Fallback Query (3 Lựa chọn Hình ảnh độc lập)

Nếu query ban đầu không tìm thấy clip (hoặc tất cả clips của chủ thể này đã bị sử dụng do chính sách chống trùng lặp) → tự động thử các lựa chọn hình ảnh/chủ thể thay thế theo thứ tự để tìm được clip độc nhất phù hợp nhất:

```text
q1 = queryParams          ← Option 1 (Lựa chọn hình ảnh 1)
q2 = queryParamsSecondary ← Option 2 (Lựa chọn hình ảnh 2 - khác chủ thể của Option 1)
q3 = queryParamsTertiary  ← Option 3 (Lựa chọn hình ảnh 3 - khác chủ thể của Option 1 & 2)
```

Ví dụ với một cảnh quay có 3 tùy chọn:
  - `queryParams`: "rocking chair"
  - `queryParamsSecondary`: "stone well"
  - `queryParamsTertiary`: "pair boots"

Tự động chuyển từ q1 $\rightarrow$ q2 $\rightarrow$ q3 nếu không tìm thấy clip đáp ứng được yêu cầu hoặc clip tìm được bị loại bỏ vì chính sách chống trùng lặp.

**Hard filter:** Moment nào có `endSeconds - startSeconds < 1.0s` → reject ngay, không cho vào pool.
Nếu tất cả moments của 1 query đều quá ngắn → thử query tiếp theo.

---

### Lớp 4 — 2-Pass Execution: Lời trước, Nhạc nền sau

**Đây là fix quan trọng nhất cho vấn đề lặp clip.**

**Tại sao lặp xảy ra với 1-pass tuần tự:**  
Các scenes không lời (instrumental, outro gap-fill) nằm liên tiếp nhau, query đều chung chung (`fog over valley`, `still water reflecting sky`). Khi search cùng 1 loại query liên tục → cùng clips nổi lên top → clip trước claim → clip sau trùng → phải dùng fallback → nhanh hết pool.

**Fix 2-pass:**
- **Pass 1** — Scenes có lời (`has_vocals=true`): query cụ thể, unique → claim clip tốt nhất trước
- **Pass 2** — Scenes không lời (`has_vocals=false`): lấy phần còn lại — pool đã được "dọn" các clip dễ nhầm, buộc search đa dạng hơn

> `startFrame` vẫn đặt đúng vị trí timeline của từng scene — 2 pass chỉ thay đổi THỨ TỰ CLAIM, không thay đổi vị trí clip trên timeline.

---

### Lớp 5 — Shift trimStart khi source ngắn hơn beat

Palmier search trả về `startSeconds/endSeconds` của đoạn match, không phải toàn bộ source clip. Nếu `avail_s < beat_duration_s` → màn đen phần còn lại.

**Fix: tự động shift trimStart về trước:**
```
Ví dụ:
  Source clip: 0-8s
  Moment match: startSeconds=5, endSeconds=8 → avail=3s
  Beat duration: 4s

  adjusted_start = max(0, end_s - beat_duration_s) = max(0, 8-4) = 4s
  trimStartFrame = round(4s × fps) = 240
  → Clip plays 4-8s → đủ 4s, include semantic match ✅
```

**Không set `trimEndFrame`** — để clip chạy tự nhiên đến hết source, tránh black screen.

---

### Lớp 6 — Batch Add + Auto-mute + Min Duration Filter

**Min duration filter:**
```
MIN_DURATION_FRAMES = 24 (0.4s @ 60fps)
Scene nào ngắn hơn → skip, không tìm clip → không có black flash
```

**Batch Add — 1 call duy nhất:**
Thay vì `add_clips` 70+ lần (1 per scene), script:
1. Search và compile TẤT CẢ entries trong Python (dedup bằng state)
2. Clear timeline
3. Gọi `add_clips` 1 lần với tất cả video clips
4. Gọi `set_clip_properties(volume=0.0)` cho tất cả video clips → mute
5. Gọi `add_clips` 1 lần cho audio track

**Lợi ích:** Không bị state loss giữa các calls, nhanh hơn nhiều, dễ debug.

---

### Quy Trình Đầy Đủ Bước 4

```bash
# Test trước:
python3 scripts/auto_edit_timeline.py --project projects/video_xxx --dry-run

# Chạy thật:
python3 scripts/auto_edit_timeline.py --project projects/video_xxx
```

**Script tự động:**
1. Đọc `beat_analysis.json`
2. Pass 1: search lyric scenes → compile entries
3. Pass 2: search ambient scenes → compile entries  
4. Clear timeline
5. Batch add_clips (tất cả video)
6. Mute video clips
7. Add audio track


---

## Checklist Hoàn Chỉnh

```
[ ] 1. get_transcript → transcription.json (có mảng "words")
[ ] 2. analyze_beats.py → beat_analysis.json (queryParams = "" — bình thường)
[ ] 3. Spawn N VisualPromptEngineer subagents song song → điền queryParams
[ ]    └─ Verify: 0 scenes còn queryParams trống
[ ] 4. python3 scripts/auto_edit_timeline.py --project projects/video_xxx --dry-run  (kiểm tra)
[ ] 5. python3 scripts/auto_edit_timeline.py --project projects/video_xxx           (chạy thật)
```

---

## Lỗi Thường Gặp và Cách Sửa

| Triệu chứng | Nguyên nhân | Cách sửa |
|-------------|-------------|---------|
| Timeline toàn clip sai/không khớp | Bỏ qua Bước 3, dùng lyric thô làm query | Chạy lại từ Bước 3 |
| `queryParams` là lyrics nguyên văn | Ai đó tự điền tay thay vì dùng subagent | Xóa, spawn subagent lại |
| Subagent trả về text thay vì JSON | Prompt không rõ | Dùng đúng template từ file 20_ |
| Một số scenes `queryParams = ""` sau merge | Subagent chunk đó fail | Re-spawn đúng chunk bị thiếu |
| Clip bị lặp adjacent (scene 1 và 3 giống nhau) | Cooldown deque quá nhỏ hoặc library thiếu clip | Tăng `MEDIAREF_COOLDOWN` trong script |
| Quá nhiều scenes bị skip "all dupes" | Library clip ít, fallback query chưa đủ generic | Kiểm tra q4/q5 trong `make_fallback_queries` |
| Đoạn không lời (outro, bridge) toàn clip trùng | 1-pass tuần tự: ambient scenes liên tiếp claim cùng 1 pool | Đã fix bằng 2-pass (xem Lớp 4) |
| Màn đen cuối beat | Source clip ngắn hơn beat duration | Đã fix bằng shift trimStart (Lớp 5) |
| Màn đen — clip quá ngắn (<1s) | search_media trả moment ngắn, source chỉ vài frames | Đã fix bằng `MIN_MOMENT_DURATION_S=1.0` filter |
| Audio video chồng lên nhau | Video clip có audio track | Đã fix: auto-mute video clips sau add_clips |

---

## Constants Quan Trọng (trong `auto_edit_timeline.py`)

| Constant | Mặc định | Ý nghĩa |
|----------|----------|---------|
| `MIN_DURATION_FRAMES` | 24 (0.4s) | Beat ngắn hơn → skip |
| `MIN_MOMENT_DURATION_S` | 1.0s | Moment ngắn hơn → reject |
| `MEDIAREF_COOLDOWN` | 15 scenes | Cooldown trước khi reuse cùng clip |
| `MCP_URL` | `http://127.0.0.1:19789/mcp` | Địa chỉ Palmier Pro |

---

**Lưu ý:** Bất cứ khi nào được yêu cầu "Dựng video tự động", Agent phải thực hiện đúng các bước này theo thứ tự, sử dụng subagents ở Bước 3, và không bao giờ tự viết `queryParams` từ raw lyrics.
