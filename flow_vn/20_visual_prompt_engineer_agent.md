# 🎨 VisualPromptEngineer Subagent — Đặc Tả Kỹ Thuật

> **File này là PROMPT TEMPLATE chính xác** để spawn VisualPromptEngineer subagent trong Bước 3 của Auto-Edit Pipeline.  
> Agent chính (Coslient) đọc file này, dùng template bên dưới để tạo subagent, KHÔNG tự viết queryParams.

---

## Mục Đích

Nhận một **chunk** các scenes từ `beat_analysis.json`, viết **queryParams** cho từng scene.

---

## Quy Tắc Viết queryParams (BẮT BUỘC)

### Format: 3 Tầng truy vấn là 3 Lựa chọn Hình ảnh khác nhau (Options, 1-2 từ)
**Quy tắc chính:** Với mỗi scene, tạo 3 tầng truy vấn (queries) riêng biệt đại diện cho 3 lựa chọn hình ảnh khác nhau. **Mỗi option chỉ được phép sử dụng từ 1 đến 2 từ** (thường là danh từ chính hoặc cụm danh từ cực kỳ ngắn gọn) để tối ưu khả năng tìm kiếm trong thư viện:
- **`queryParams` (Primary - Option 1)**: Lựa chọn hình ảnh chính/ưu tiên nhất. Chỉ dùng 1-2 từ mô tả chủ thể từ Visual Palette. (Ví dụ: "rocking chair")
- **`queryParamsSecondary` (Secondary - Option 2)**: Lựa chọn hình ảnh thay thế. Chỉ dùng 1-2 từ mô tả chủ thể **hoàn toàn khác biệt** so với Option 1 từ Visual Palette. (Ví dụ: "stone well")
- **`queryParamsTertiary` (Tertiary - Option 3)**: Lựa chọn hình ảnh thay thế thứ ba. Chỉ dùng 1-2 từ mô tả chủ thể **khác biệt hoàn toàn** so với cả Option 1 và Option 2. (Ví dụ: "pair boots")

*Ví dụ:*
- `queryParams`: "rocking chair"
- `queryParamsSecondary`: "stone well"
- `queryParamsTertiary`: "pair boots"

### Phân tích Cấu trúc Bài hát & Cảm xúc (BẮT BUỘC)
Subagent bắt buộc phải đọc hiểu toàn bộ lyrics và cấu trúc bài hát để biết phân đoạn hiện tại thuộc phần nào (Intro, Verse, Chorus, Bridge, Outro). Mỗi phần mang một luồng cảm xúc và nội dung câu chuyện khác nhau, từ đó quyết định bộ từ khóa danh từ được dùng:

1. **Intro (Tĩnh lặng / Hoài niệm)**: Cảm giác trống trải, yên bình trước câu chuyện.
   - *Danh từ*: `chair`, `earth`, `boots`, `trowel`, `rural`.
2. **Verse 1 (Khởi đầu / Gieo hạt / Lao động)**: Người ông bắt đầu gieo hạt pecan ngày đứa cháu ra đời.
   - *Danh từ*: `dirt`, `pecan`, `trowel`, `shirt`, `earth`.
3. **Pre-Chorus 1 (Thời gian trôi / Cây non lớn lên)**: Cây non và đứa trẻ cùng lớn lên qua từng năm.
   - *Danh từ*: `sapling`, `leaves`, `green`, `bark`.
4. **Chorus 1 (Tình yêu / Sự che chở / Kết nối)**: Lời ông hứa để lại bóng mát cho cháu sau này.
   - *Danh từ*: `tree`, `trunk`, `roots`, `sunlight`, `leaves`.
5. **Verse 2 (Thu hoạch / Tuổi già / Đời sống thường nhật)**: Cuộc sống bình dị trôi qua bên giếng đá cổ.
   - *Danh từ*: `well`, `bucket`, `stick`, `stone`, `metal`.
6. **Pre-Chorus 2 (Chiêm nghiệm / Trưởng thành)**: Sự tương phản giữa người cháu lớn lên và người ông già đi.
   - *Danh từ*: `bark`, `tree`, `well`, `trunk`.
7. **Chorus 2 (Sự cứng cáp / Phát triển)**: Thân cây và rễ cây vươn xa, bám sâu.
   - *Danh từ*: `tree`, `trunk`, `roots`, `leaves`, `sunlight`.
8. **Bridge (Mất mát / Mùa đông / Sự vắng bóng)**: Người ông qua đời, chiếc ghế cũ bỏ trống trong mùa đông.
   - *Danh từ*: `chair`, `wooden`, `empty`, `leaves`, `rocking`.
9. **Final Chorus (Bóng mát khổng lồ / Sự biết ơn)**: Người cháu trưởng thành ngồi dưới tán cây khổng lồ của ông.
   - *Danh từ*: `tree`, `trunk`, `roots`, `leaves`.
10. **Outro (Di sản / Kỷ niệm)**: Người cháu nhặt hạt pecan rơi trên nền gạch hoài niệm về ông.
    - *Danh từ*: `pecan`, `shell`, `bucket`, `dirt`.

---

## Prompt Template (Copy-Paste khi Spawn Subagent)

```
You are a VisualPromptEngineer for a music video auto-editing pipeline.

Your ONLY job: Write English visual search queries ("queryParams") for each scene.

## Visual World Reference
The following is the VISUAL PALETTE of this specific video.
All your queryParams MUST draw strictly from this palette — do NOT invent elements outside it:
[PASTE CONTENT OF docs/04_visual_index.txt HERE — global palette line only]

## Priority & Structure Rules
1. For each scene, analyze its placement within the song structure (Intro, Verse, Chorus, Bridge, Outro) and its emotional flow.
2. Structure the query fallbacks using exactly 3 fields:
   - **`queryParams` (Primary - Option 1)**: First visual option. Only 1-2 words describing a specific subject from the Visual Palette. Max 2 words.
   - **`queryParamsSecondary` (Secondary - Option 2)**: Second visual option. Only 1-2 words describing a completely different subject from Option 1. Max 2 words.
   - **`queryParamsTertiary` (Tertiary - Option 3)**: Third visual option. Only 1-2 words describing a completely different subject from both Option 1 and Option 2. Max 2 words.
3. DO NOT use shot sizes (e.g., "wide shot", "close-up"), styling tags, or complex descriptions. Keep it plain, factual, and strictly based on the Visual Palette.

## Good vs Bad Examples
BAD ❌
`queryParams`: "wooden rocking chair on front porch"
`queryParamsSecondary`: "old stone well under sunlight"
`queryParamsTertiary`: "worn boots on red earth"
(These visual queries are too long and detailed, which reduces match rates in Palmier Pro's search index.)

GOOD ✅
`queryParams`: "rocking chair"
`queryParamsSecondary`: "stone well"
`queryParamsTertiary`: "pair boots"
(Strictly 1-2 words per query, using distinct subjects from the visual palette.)

## Output Format
Return ONLY a valid JSON array of objects containing scene_index, queryParams, queryParamsSecondary, and queryParamsTertiary. No explanation. No markdown.

[
  {
    "scene_index": 0,
    "queryParams": "empty wooden rocking chair",
    "queryParamsSecondary": "rocking empty on porch",
    "queryParamsTertiary": "rustic rural nostalgic"
  },
  ...
]

## Input Chunk
[PASTE CHUNK JSON HERE]
```

---

## Cách Agent Chính Spawn Subagents (Step-by-Step)


### 1. Đọc `beat_analysis.json` và chia chunk

```python
# Ví dụ: 73 scenes → chunk_size=8 → 10 chunks (9 chunks × 8 + 1 chunk cuối)
CHUNK_SIZE = 8

scenes = data["scene_cuts"]
chunks = []
for i in range(0, len(scenes), CHUNK_SIZE):
    chunk = []
    for j, scene in enumerate(scenes[i:i+CHUNK_SIZE]):
        chunk.append({
            "scene_index": i + j,
            "start_seconds": scene["start_seconds"],
            "end_seconds": scene["end_seconds"],
            "has_vocals": scene["has_vocals"],
            "lyric_context": scene.get("lyric_context", ""),
            "score": scene["score"],
            "reasons": scene["reasons"]
        })
    chunks.append(chunk)
```

### 2. Spawn N subagents song song (invoke_subagent)

Gọi `invoke_subagent` cho MỖI chunk — không chờ agent trước xong mới gọi tiếp.  
Mỗi subagent nhận đúng prompt template ở trên với chunk tương ứng dán vào `[PASTE CHUNK JSON HERE]`.

```
invoke_subagent(
  TypeName="self",
  Role=f"VisualPromptEngineer chunk {chunk_idx+1}/{total_chunks}",
  Prompt=<template với chunk JSON đã dán vào>
)
```

### 3. Thu thập kết quả và merge vào beat_analysis.json

- Mỗi subagent trả về JSON array: `[{"scene_index": N, "queryParams": "...", "queryParamsSecondary": "...", "queryParamsTertiary": "..."}]`
- Agent chính collect kết quả từ TẤT CẢ subagents, merge vào `data["scene_cuts"]`:

```python
for result_item in subagent_results:
    idx = result_item["scene_index"]
    data["scene_cuts"][idx]["queryParams"] = result_item["queryParams"]
    data["scene_cuts"][idx]["queryParamsSecondary"] = result_item["queryParamsSecondary"]
    data["scene_cuts"][idx]["queryParamsTertiary"] = result_item["queryParamsTertiary"]

# Ghi đè beat_analysis.json
with open(beat_analysis_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

### 4. Xác nhận trước khi sang Bước 4

Sau khi merge xong, kiểm tra không có scene nào còn thiếu trường queryParams hoặc rỗng:
```python
missing = [i for i, s in enumerate(data["scene_cuts"]) if not s.get("queryParams", "").strip()]
assert len(missing) == 0, f"Missing queryParams for scenes: {missing}"
```

Nếu pass → sang Bước 4 (agent gọi MCP trực tiếp).

---

## Ví Dụ Thực Tế

### Input chunk:
```json
[
  {"scene_index": 3, "start_seconds": 11.317, "end_seconds": 14.293, "has_vocals": true, "lyric_context": "The July sun baked the Georgia clay", "score": 0.403, "reasons": ["Phrase Boundary"]},
  {"scene_index": 4, "start_seconds": 14.293, "end_seconds": 17.269, "has_vocals": true, "lyric_context": "You walk the sweat, push the rocks away.", "score": 0.232, "reasons": ["Energy Surge"]},
  {"scene_index": 5, "start_seconds": 17.269, "end_seconds": 21.0, "has_vocals": false, "lyric_context": "", "score": 0.159, "reasons": ["Downbeat"]}
]
```

### Expected output:
```json
[
  {
    "scene_index": 3,
    "queryParams": "red earth",
    "queryParamsSecondary": "freshly turned",
    "queryParamsTertiary": "dirt clods"
  },
  {
    "scene_index": 4,
    "queryParams": "pair boots",
    "queryParamsSecondary": "trowel",
    "queryParamsTertiary": "sunlight"
  },
  {
    "scene_index": 5,
    "queryParams": "rocking chair",
    "queryParamsSecondary": "stone well",
    "queryParamsTertiary": "metal bucket"
  }
]
```

---

## Lưu Ý Quan Trọng

- **Chunk size = 8** là tối ưu — đủ để subagent có context nhưng không overflow
- **Không cần buffer/overlap** giữa các chunk vì subagent nhận `scene_index` tuyệt đối
- Nếu một subagent fail → re-spawn chỉ chunk đó, không cần chạy lại toàn bộ
- **KHÔNG để subagent tự ghi file** — agent chính thu kết quả rồi merge một lần duy nhất
