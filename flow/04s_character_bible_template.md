# Character Bible Template — [Tên dự án]

> **Stage:** 4.1.5 — Character & Asset Reference Design
> **Điều kiện:** Chỉ tạo file này KHI story có nhân vật xuyên suốt nhiều shots (Story Type B hoặc C).
> **Tiếp theo:** Stage 4.2 (Test Prompts) chỉ bắt đầu sau khi Boss duyệt ít nhất C3 + E1.

---

## Story Type Check — Bắt buộc xác định trước

```
STORY TYPE: [ B ] Single Character Journey
             [ C ] Multi-Character (N nhân vật)
             [ A ] No Character → SKIP toàn bộ file này, chuyển sang Stage 4.2

CHARACTER COUNT: [số lượng]
TOTAL SHOTS: [N shots từ storyboard]
LOCATION COUNT: [số locations]
CHARACTER VISIBILITY: [% shots có nhân vật xuất hiện]
HAND/GESTURE MOTIF: [ YES / NO ]  ← nếu YES → O3 Hand Sheet là BẮT BUỘC
```

---

## Asset Generation Order (BẮT BUỘC tuân thủ thứ tự)

> [!IMPORTANT]
> Không được nhảy cóc thứ tự. Mỗi tier cần được Boss duyệt trước khi sang tier tiếp theo.

```
Bước 1 → [Style] 3 test prompts → Boss duyệt style fit
Bước 2 → [C3]   Fully Costumed character → Boss duyệt master character
Bước 3 → [O3]   Hand Detail (nếu tay là motif) → Boss duyệt hands
Bước 4 → [E1-EN] 1 establishing shot per location → Boss duyệt cross-environment color
Bước 5 → [Props] Chỉ props xuất hiện nhiều / visually complex
Bước 6 → Compile Master Frozen Character Block + Environment Packs
```

---

## Tier 1 — CHARACTER ASSETS

> [!IMPORTANT]
> **C3 (Fully Costumed) là asset quan trọng nhất.** Đây là image làm `--cref` cho 80-90% shots trong video. Phải generate và Boss duyệt trước tất cả assets khác.

### C1: Character Face Sheet

**Mục đích:** Lock facial identity. Dùng làm `--cref --cw 0` khi chỉ cần giữ mặt (không giữ costume).

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]
[MJ JOB ID: ...]

PROMPT:
character design sheet, multiple angles, turnaround, front view + 3/4 view + side profile + back view,
[MÔ TẢ MẶT NHÂN VẬT: tuổi, giới tính, đặc điểm nổi bật],
neutral expression, isolated on clean neutral background,
[STYLE ANCHOR],
character reference sheet layout, no background, 16:9
--stylize [N] --v 6.0
```

---

### C2: Character Full Body (Bare / Undressed)

**Mục đích:** Lock body proportions khi nhân vật không mặc costume đặc trưng.

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

PROMPT:
full body turnaround, front and back, [MÔ TẢ CƠ THỂ NHÂN VẬT: tỷ lệ, đặc trưng],
wearing [trang phục bình thường khi ở nhà],
isolated on neutral background,
[STYLE ANCHOR],
16:9
--stylize [N] --v 6.0
```

---

### C3: Character Fully Costumed ⭐ CRITICAL

**Mục đích:** Master reference dùng làm `--cref --cw 100` cho toàn bộ shots có nhân vật mặc costume đầy đủ. Đây là asset quan trọng nhất của toàn bộ video.

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]  ← URL này được dùng làm --cref cho mọi shot

PROMPT:
full body character design sheet, multiple angles (front / 3-quarter / side / back),
[MÔ TẢ NHÂN VẬT] wearing [MÔ TẢ CHI TIẾT TỪNG LAYER CỦA COSTUME],
isolated on neutral background,
[STYLE ANCHOR],
highly detailed costume, visible texture and material,
16:9
--stylize [N] --v 6.0
```

**Dùng với:**
- `--cref [C3_URL] --cw 100` → lock cả face + full costume
- `--cref [C3_URL] --cw 50` → lock costume shape, ít lock mặt hơn

---

### C4: Character Expression Sheet

**Mục đích:** Tham khảo khi viết prompts cần biểu cảm cụ thể, đặc biệt nếu face bị che khuất (qua kính, từ xa, góc nghiêng).

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

EXPRESSIONS CẦN COVER (theo emotional beats trong storyboard):
- [Biểu cảm 1]: [tên cảm xúc]
- [Biểu cảm 2]: [tên cảm xúc]
- [Biểu cảm 3]: [tên cảm xúc]
- [Biểu cảm 4]: [tên cảm xúc]
- [Biểu cảm 5]: [tên cảm xúc]

PROMPT:
expression sheet, [CHARACTER DESCRIPTION],
5 expressions side by side: [list expressions],
isolated on neutral background,
[STYLE ANCHOR],
16:9 --stylize [N] --v 6.0
```

---

### C5: Character Signature Pose Sheet

**Mục đích:** Tham khảo khi viết prompts cho STORY shots — poses mapping với actions trong storyboard.

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

POSES CẦN COVER (từ STORY shots trong storyboard):
- Pose A: [tên pose] — dùng ở shots [SB_XXX]
- Pose B: [tên pose] — dùng ở shots [SB_XXX]
- Pose C: [tên pose] — dùng ở shots [SB_XXX]

PROMPT:
action pose sheet, [CHARACTER DESCRIPTION],
[list poses] side by side on neutral background,
[STYLE ANCHOR],
full body visible, 16:9 --stylize [N] --v 6.0
```

---

## Tier 2 — COSTUME / OUTFIT ASSETS

### O1: Outfit Turnaround

**Mục đích:** Lock costume details độc lập với nhân vật. Dùng khi cần tham khảo texture/shape mà không cần nhân vật trong frame.

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

COSTUME NAME: [tên costume]

LAYER-BY-LAYER SPEC:
- Outer layer: [mô tả]
- Accessories: [mô tả]
- Material: [mô tả texture, màu sắc chính xác]
- Color code: [hex hoặc descriptive]
- Aging/weathering: [mô tả mức độ cũ/mới]

PROMPT:
prop design sheet, costume turnaround, front + side + back + 3-quarter,
[MÔ TẢ CHI TIẾT COSTUME], isolated on neutral background,
[STYLE ANCHOR], 16:9 --stylize [N] --v 6.0
```

---

### O2: Headwear / Helmet Detail Sheet

**Bắt buộc khi:** Costume có headwear đặc biệt hoặc che khuất mặt nhân vật.

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

PROMPT:
detailed prop sheet, [TÊN HEADWEAR], close-up detail views from multiple angles,
[MÔ TẢ CHI TIẾT: material, texture, key features],
isolated on neutral background,
[STYLE ANCHOR], 16:9 --stylize [N] --v 6.0
```

---

### O3: Hand Detail Sheet ⭐ (BẮT BUỘC nếu tay là visual motif)

**Bắt buộc khi:** Story có nhiều DETAIL shots về bàn tay, hoặc tay là visual motif trung tâm của câu chuyện.

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

HAND MOTIF ROLE: [mô tả tại sao tay quan trọng trong story này]
SHOTS USING HANDS: [list SB_IDs]

TEXTURE SPEC:
- Material: [mô tả]
- Color: [mô tả chính xác]
- Aging details: [mô tả chi tiết rust/wear pattern]
- Joint details: [mô tả]
- Finger proportions: [mô tả]

PROMPT:
detailed hand reference sheet, multiple views (palm facing up / palm facing down / side / gripping / open),
[MÔ TẢ CHI TIẾT BÀN TAY], isolated on neutral background,
[STYLE ANCHOR], extreme close-up macro photography, 16:9
--stylize [N] --v 6.0
```

---

### O4: Footwear Detail

```
[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

PROMPT:
detailed footwear prop sheet, [TÊN FOOTWEAR], front and side view,
[MÔ TẢ], isolated on neutral background, [STYLE ANCHOR],
16:9 --stylize [N] --v 6.0
```

---

## Tier 3 — PROP ASSETS

> [!NOTE]
> Chỉ tạo Prop Sheet cho props: (1) xuất hiện trong 3+ shots, HOẶC (2) visually complex, HOẶC (3) có tương tác vật lý rõ ràng với nhân vật.

### Template per prop:

```
### P[N]: [Tên prop]

[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

SHOTS USING THIS PROP: [list SB_IDs]

SPEC:
- Scale: [so sánh với character — ví dụ "bằng 1/3 chiều cao nhân vật"]
- Material: [mô tả]
- Color: [mô tả chính xác]
- Weight/Physics feel: [nặng / nhẹ / fragile / solid]
- Interaction type: [cách nhân vật cầm/đặt/sử dụng]

PROMPT:
prop design sheet, orthographic views (front / side / top),
[MÔ TẢ CHI TIẾT PROP], scale reference indicator,
isolated on neutral background, [STYLE ANCHOR],
16:9 --stylize [N] --v 6.0
```

---

## Tier 4 — ENVIRONMENT ASSETS

> [!IMPORTANT]
> **Bắt buộc tạo 1 establishing shot cho MỖI location** trước khi viết bất kỳ prompt nào trong location đó. Mục tiêu: verify màu brass của nhân vật vẫn đúng khi đặt vào các lighting environment khác nhau.

### Template per location:

```
### E[N]: [Tên location]

[STATUS: PENDING / GENERATED / APPROVED]
[GENERATED IMAGE URL: ...]

SHOTS IN THIS LOCATION: [list SB_IDs]

LOCATION SPEC:
- Không gian: [mô tả tổng quan]
- Scale indicator: [nhân vật chiếm bao nhiêu % frame]
- Key structural elements: [liệt kê 3-5 elements quan trọng nhất]

COLOR PALETTE (5 màu chính):
- Primary: [hex + descriptive name]
- Secondary: [hex + descriptive name]
- Accent: [hex + descriptive name]
- Shadow color: [hex + descriptive name]
- Highlight color: [hex + descriptive name]

LIGHTING:
- Direction: [từ đâu]
- Color temperature: [ấm/lạnh, Kelvin estimate]
- Intensity: [mô tả]
- Signature keyword: [1-2 từ khoá lighting cho prompt]

ATMOSPHERE:
- Particles/effects: [fog / dust / bubbles / none]
- Movement: [slow / fast / still]
- Depth cues: [mô tả cách tạo depth trong environment này]

TRANSITION POINTS:
- Entry: [nhân vật từ đâu đến]
- Exit: [nhân vật đi về đâu]
- Bridge shot type: [Direct / Environmental / Detail]

ENVIRONMENT PACK KEYWORD STRING (dùng trong mọi prompt trong location này):
[compact string 30-50 từ mô tả environment — copy-paste vào prompt]

PROMPT (establishing shot):
wide establishing shot, empty scene with no character,
[MÔ TẢ TOÀN CẢNH LOCATION], [LIGHTING], [ATMOSPHERE],
[STYLE ANCHOR], [COLOR_TONE],
16:9 --stylize [N] --v 6.0
```

---

## Tier 5 — LIGHTING SETUPS

```
## LIGHTING LIBRARY — [Tên dự án]

| Setup ID | Tên | Keyword String | Áp dụng shots |
|----------|-----|----------------|--------------|
| L1 | [Tên] | [compact lighting keywords] | [SB_IDs] |
| L2 | [Tên] | [compact lighting keywords] | [SB_IDs] |
| L3 | [Tên] | [compact lighting keywords] | [SB_IDs] |
| L4 | [Tên] | [compact lighting keywords] | [SB_IDs] |

Quy tắc: brass/metal color phải được verify dưới TỪNG lighting setup.
Nếu brass bị shift sang màu khác dưới lighting mới → thêm anchor màu cụ thể vào Environment Pack.
```

---

## Tier 6 — STYLE ANCHOR ASSETS

### S1: Approved Shot Gallery (Style Bank)

```
[Sau khi Boss approve 3-5 shots đầu tiên, điền URL vào đây]
Shot 1: [URL] — dùng làm --sref primary
Shot 2: [URL] — dùng làm --sref secondary
Shot 3: [URL] — ...

Cách dùng: --sref [URL1] [URL2] [URL3] (combine tối đa 3 URLs)
```

---

### S2: LOCKED COLOR TONE

```
[Copy từ Stage 4.1 Bước 3 — không thay đổi qua toàn bộ video]

LOCKED COLOR TONE: [color tone string]
```

---

### S3: LOCKED STYLE STRING

```
[Style anchor compact — dùng trong mọi prompt]

LOCKED STYLE STRING: [style anchor string]
```

---

### S4: Master Frozen Character Block ⭐

> [!IMPORTANT]
> **Đây là block văn bản KHÔNG ĐỔI qua toàn bộ 48 shots.** Copy-paste nguyên văn vào mọi prompt có nhân vật. Không paraphrase, không rút gọn.

```
MASTER FROZEN CHARACTER BLOCK:
[
  Viết đây sau khi đã approve C3.
  Block này mô tả: WHO + WEARING WHAT + MATERIAL DETAILS.
  Không bao gồm: location, action, camera, lighting.
  Độ dài mục tiêu: 40-60 từ.
]
```

---

## Master Prompt Architecture (Reference khi viết 04_image_prompts.txt)

```
# SB_[ID] | [Section] | [Timecode] | Type: [STORY/ENV/DETAIL]

[FROZEN_CHARACTER_BLOCK] (nếu shot có nhân vật)
[SHOT_SPECIFIC_ACTION] (hành động/cảnh cụ thể của shot này)
[CAMERA_ANGLE_AND_FRAMING]
[ENVIRONMENT_PACK_CURRENT] (thay đổi theo location)
[LIGHTING_SETUP_CURRENT] (từ Tier 5)
[LOCKED_STYLE_STRING]
[LOCKED_COLOR_TONE]
16:9 --ar 16:9 --cref [C3_URL] --cw 100 --sref [S1_URL] --stylize [N] --v 6.0
```

---

## Quality Gate — Kiểm tra mỗi shot trước khi approve

```
Per-Shot Quality Checklist:
[ ] Costume material/color matches O1 reference?
[ ] Hand proportions/texture match O3 reference? (nếu tay visible)
[ ] Helmet/headwear shape matches C3 reference?
[ ] Background color palette matches environment sheet?
[ ] Art style matches S1 style bank?

Nếu fail bất kỳ điểm nào → regenerate với tighter --cref --cw + targeted negative prompt.
```

---

## Regeneration Protocol (Khi shot bị drift)

```
CHARACTER FACE DRIFT:
→ Tăng --cw về 80-100
→ Thêm vào negative: [tên vật liệu không đúng], [màu sắc không đúng]
→ Confirm dùng đúng C3_URL làm --cref

COSTUME MATERIAL DRIFT:
→ Thêm material anchor vào prompt: "[vật liệu cụ thể] [màu hex-descriptive]"
→ Dùng O1 URL làm --sref phụ

ENVIRONMENT COLOR BLEED (màu environment bôi lên nhân vật):
→ Thêm materiality anchor: "[costume material] [color] [surface texture]" gắn trực tiếp vào tên chất liệu
→ Thêm negative: "no color bleed, [costume color] isolated to costume fabric only"

NGUYÊN TẮC TUYỆT ĐỐI:
KHÔNG bao giờ dùng output shot làm --cref cho shot tiếp theo.
LUÔN dùng master C3 sheet gốc làm --cref. (Tránh generational drift)
```

---

## Asset Status Summary (Cập nhật liên tục)

| Asset ID | Tên | Status | URL | Dùng cho |
|----------|-----|--------|-----|---------|
| C1 | Face Sheet | PENDING | — | --cref --cw 0 |
| C2 | Full Body Bare | PENDING | — | Body proportion ref |
| **C3** | **Fully Costumed** | **PENDING** | **—** | **--cref --cw 100 (critical)** |
| C4 | Expression Sheet | PENDING | — | Expression ref |
| C5 | Pose Sheet | PENDING | — | Pose ref |
| O1 | Outfit Turnaround | PENDING | — | Costume ref |
| O2 | Headwear Detail | PENDING | — | Headwear ref |
| O3 | Hand Detail | PENDING | — | --sref hands |
| O4 | Footwear Detail | PENDING | — | Footwear ref |
| P[N] | Props | PENDING | — | Per-shot |
| E[N] | Environments | PENDING | — | Environment packs |
| L[N] | Lighting Setups | PENDING | — | Per-location |
| S1 | Style Bank | PENDING | — | --sref |
| S2 | Color Token | PENDING | — | End of every prompt |
| S3 | Style String | PENDING | — | Every prompt |
| S4 | Frozen Char Block | PENDING | — | Character shots |
