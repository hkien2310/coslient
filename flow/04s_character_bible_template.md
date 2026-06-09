# Character Bible Template — [Tên dự án]

> **Stage:** 4.1.5 — Ingredient Design (Google Flow)
> **Tool:** Google Flow (Nano Banana image gen + VEO 3 video gen)
> **Điều kiện:** Tạo file này trước Stage 4.2. Tất cả ingredients phải được Boss approve trước khi viết shot prompts.

---

## Nguyên tắc cốt lõi

> [!IMPORTANT]
> **Mọi thứ xuất hiện nhiều lần trong video → phải trở thành ingredient với @tag.**
> Không chỉ nhân vật — địa điểm, prop quan trọng, và style reference đều là ingredients.

### Quy tắc 2 Ảnh per Ingredient
- **Mỗi ingredient được define bằng tối đa 2 ảnh** trong Flow.
- Dùng tối đa thông tin trong 2 ảnh đó:
  - Ảnh 1: Multi-angle overview (front + 3/4 + side trong 1 frame)
  - Ảnh 2: Close-up detail (texture, face, key feature)
- Không cần nhiều hơn — Flow AI sẽ extract DNA từ 2 ảnh này.

### Quy tắc 3-Ingredient Budget per Prompt (Hard Limit của Flow)
- **Flow hard limit: tối đa 3 @tags per prompt.**
- Mỗi shot phải plan trước sẽ dùng 3 slots đó cho gì.
- **Budget template cho Coslient:**
  - Slot 1: `@Character` (nhân vật chính)
  - Slot 2: `@Environment` (địa điểm hiện tại)
  - Slot 3: `@StyleRef` (style anchor)
- **Exception:** DETAIL shot không có nhân vật → Slot 1 là `@Prop` hoặc `@DetailSubject`

### Quy tắc Naming Convention
- Tên @tag: PascalCase, không dấu, không space, không ký tự đặc biệt
- Ngắn gọn: `@OldMan`, `@GlassDome`, `@BrassHand`, `@StyleRef`
- Mô tả đủ để đọc prompt là hiểu ngay

---

## Story Type Check

```
STORY TYPE: [ A ] No Character / [ B ] Single Character / [ C ] Multi-Character
CHARACTER COUNT: [N]
TOTAL SHOTS: [N]
LOCATION COUNT: [N]

INGREDIENT COUNT DỰ KIẾN:
- Character ingredients: [N]
- Environment ingredients: [N]
- Prop ingredients (recurring): [N]
- Style ingredient: 1
TỔNG: [N] ingredients (phải upload tất cả trước khi bắt đầu generate)
```

---

## Tier A — CHARACTER Ingredients

> Character = bất kỳ "nhân vật" nào xuất hiện trong nhiều shots.
> Bao gồm cả con vật, nhân vật phụ thường xuyên xuất hiện.

### Ảnh 1 — Multi-Angle Sheet

```
@TagName: [@CharacterName]
STATUS: PENDING / GENERATED / UPLOADED TO FLOW

MỤC ĐÍCH: Overview toàn diện, Flow dùng để hiểu silhouette, proportions, costume.

PROMPT (Nano Banana):
Character reference sheet, [CHARACTER DESCRIPTION], shown from multiple angles:
front view, 3/4 view left, side profile, all on the same neutral background,
full body visible in each view, no overlapping,
[STYLE ANCHOR — ví dụ: stop-motion claymation, tactile textures, Laika aesthetic],
reference sheet layout, clean neutral background
```

---

### Ảnh 2 — Close-Up Detail

```
STATUS: PENDING / GENERATED / UPLOADED TO FLOW

MỤC ĐÍCH: Detail quan trọng mà ảnh 1 không capture được rõ.
Ví dụ: texture của costume, biểu cảm mặt, đôi tay đặc trưng.

PROMPT (Nano Banana):
Close-up detail of [CHARACTER NAME], showing [KEY DETAIL: face expression / hands / costume texture / signature feature],
extreme macro close-up, [MATERIAL DESCRIPTION],
[STYLE ANCHOR],
isolated on neutral background, no background clutter
```

---

### Flow Upload Info

```
@TagName: [@CharacterName]
Image 1 URL: [link sau khi upload lên Flow]
Image 2 URL: [link sau khi upload lên Flow]
Flow Ingredient Name: [tên đặt trong Flow]
Used in shot types: [STORY / DETAIL / ENV]
3-Slot position: Slot 1 (Character)
```

---

## Tier B — ENVIRONMENT Ingredients

> Environment = địa điểm xuất hiện trong nhiều shots.
> Địa điểm là "nhân vật" thứ 2 của mỗi scene — phải nhất quán như nhân vật.

### Template per Environment:

```
@TagName: [@EnvironmentName]
STATUS: PENDING / GENERATED / UPLOADED TO FLOW

SHOTS IN THIS ENVIRONMENT: [SB_xxx — SB_xxx]

### Ảnh 1 — Establishing Wide Shot
MỤC ĐÍCH: Flow hiểu tổng thể không gian, scale, màu sắc chủ đạo.

PROMPT (Nano Banana):
Wide establishing shot of [ENVIRONMENT DESCRIPTION], no characters present,
showing [KEY ARCHITECTURAL/NATURAL ELEMENTS],
[LIGHTING DESCRIPTION],
[ATMOSPHERE: particles / fog / underwater / etc.],
[COLOR PALETTE: 3-5 màu chính],
[STYLE ANCHOR], cinematic composition, 16:9

### Ảnh 2 — Key Atmosphere Detail
MỤC ĐÍCH: Capture đặc trưng không thể nhầm lẫn của địa điểm này.

PROMPT (Nano Banana):
Close-medium shot detail of [SIGNATURE ELEMENT of this environment],
[KEY TEXTURE / MATERIAL / LIGHT EFFECT],
[STYLE ANCHOR], macro photography, shallow depth of field

### Flow Upload Info
Image 1 URL: [establishing shot]
Image 2 URL: [detail shot]
Flow Ingredient Name: [@TagName]
3-Slot position: Slot 2 (Environment)

### Environment Pack Keywords (dùng trong mọi shot prompt của location này)
[Compact 20-30 word string mô tả environment — paste vào text prompt bổ sung cho @tag]
```

---

## Tier C — PROP Ingredients

> Prop ingredient = vật thể xuất hiện trong 3+ shots HOẶC có tương tác vật lý phức tạp.
> Prop ít xuất hiện hơn → mô tả trong text prompt, không cần ingredient.

### Template per Prop:

```
@TagName: [@PropName]
STATUS: PENDING / GENERATED / UPLOADED TO FLOW

SHOTS USING THIS PROP: [SB_xxx, SB_xxx...]
THRESHOLD CHECK: Xuất hiện [N] lần → Có/Không cần ingredient?

### Ảnh 1 — Prop Overview
PROMPT (Nano Banana):
Prop design sheet, [PROP DESCRIPTION], multiple views on same neutral background,
scale reference visible (compare to [human hand / common object]),
[MATERIAL, COLOR, TEXTURE DETAILS],
[STYLE ANCHOR], isolated, no background

### Ảnh 2 — Interaction Close-Up
PROMPT (Nano Banana):
Close-up of [PROP] in the context of interaction:
[HOW CHARACTER HOLDS/TOUCHES/USES IT],
[KEY INTERACTION DETAIL],
[STYLE ANCHOR], macro photography

### Flow Upload Info
Image 1 URL: [prop overview]
Image 2 URL: [interaction shot]
Flow Ingredient Name: [@TagName]
3-Slot position: Slot 1 (khi không có character) / varies
```

---

## Tier D — STYLE Ingredient

> Một style reference duy nhất, áp dụng cho toàn bộ video.
> Được cập nhật sau khi Boss approve 3-5 shots đầu tiên.

```
@TagName: @StyleRef
STATUS: PENDING — điền sau khi approve shots đầu tiên

### Ảnh 1 — Primary Style Frame
[URL shot đầu tiên được approve — đây là "bộ mặt" của video]
CHỌN: Shot có đầy đủ nhất: character + environment + lighting + texture

### Ảnh 2 — Secondary Style Frame (Optional)
[URL shot thứ 2 được approve — tăng variety cho style reading]
CHỌN: Shot với lighting hoặc environment khác để tăng style range

Flow Ingredient Name: @StyleRef
3-Slot position: Slot 3 (luôn luôn)
NOTE: Cập nhật @StyleRef URL sau mỗi batch nếu tìm được shot đẹp hơn.
```

---

## Ingredient Registry (Điền đầy đủ trước khi generate)

```
| @Tag | Type | Slot | Ảnh 1 | Ảnh 2 | Status | Shots |
|------|------|------|-------|-------|--------|-------|
| @[Char] | Character | 1 | — | — | PENDING | STORY shots |
| @[Env1] | Environment | 2 | — | — | PENDING | SB_xxx–SB_xxx |
| @[Env2] | Environment | 2 | — | — | PENDING | SB_xxx–SB_xxx |
| @[Prop] | Prop | varies | — | — | PENDING | SB_xxx, SB_xxx |
| @StyleRef | Style | 3 | — | — | PENDING | All |
```

---

## 3-Ingredient Budget Map

> Mỗi shot phải assign đủ 3 slots trước khi viết prompt.
> Điền bảng này trước khi viết `04_image_prompts.txt`.

| Shot Type | Slot 1 | Slot 2 | Slot 3 |
|-----------|--------|--------|--------|
| STORY (character + env) | `@Character` | `@Environment` | `@StyleRef` |
| DETAIL (prop/body part + env) | `@Prop/@Detail` | `@Environment` | `@StyleRef` |
| ENV only | `@Environment` | `@StyleRef` | — |
| Multi-character | `@Char1` | `@Char2` | `@Environment` *(StyleRef mô tả trong text)* |

---

## Flow Prompt Templates

### STORY Shot Template
```
[Shot size], @[Character] [action verb] [how], @[Environment] [brief context],
[camera movement — 1 move only],
[lighting keyword — 3-5 words],
Audio: [specific ambient sounds matching scene]. No music. No score. No dialogue. No voiceover.
```

**Ví dụ:**
```
Medium shot, @OldMan kneels slowly on sandy seafloor placing something gently down, @SandyBed quiet isolated,
static locked frame tilting down slightly,
soft blue-green underwater ambient light,
Audio: muffled underwater silence, faint sand displacement, distant water pressure hum. No music. No score. No dialogue. No voiceover.
```

### ENV Shot Template (không có character)
```
[Shot size] establishing shot, @[Environment] [atmosphere description],
[camera movement],
[lighting],
Audio: [ambient sounds of this environment]. No music. No score.
```

### DETAIL Shot Template (cận vật/tay)
```
Extreme close-up, @[Prop/Detail] [action/state],
[shot context — what surrounds it],
macro photography shallow depth of field,
[lighting],
Audio: [specific small sound — fabric rustle, water, metal creak]. No music.
```

---

## Flow Generation Workflow

```
Bước 1: Generate tất cả ingredient images trong Nano Banana (ảnh 1 + ảnh 2 per ingredient)
Bước 2: Boss approve từng ingredient
Bước 3: Upload approved images lên Flow → đặt @tag names
Bước 4: Điền URLs vào Ingredient Registry ở trên
Bước 5: Điền 3-Ingredient Budget Map
Bước 6: Viết shot prompts vào 04_image_prompts.txt (Stage 4.3)
Bước 7: Generate images qua Nano Banana trong Flow
Bước 8: Generate videos qua VEO 3 trong Flow (dùng "Add to Scene" cho continuity)
```

---

## Flow Continuity Protocol (Video Generation)

> [!IMPORTANT]
> **"Add to Scene"** là cơ chế chính để duy trì continuity trong Flow.
> KHÔNG generate từng clip hoàn toàn độc lập nếu tránh được.

| Transition Type | Cách xử lý trong Flow |
|----------------|----------------------|
| **Cùng location, shot tiếp theo** | "Add to Scene" → VEO maintain continuity |
| **Extend clip** | "Extend" feature → chain seamlessly |
| **Đổi location** | "Jump To" + ENV shot reference trước |
| **Time jump** | Generate DETAIL shot làm bridge, rồi "Add to Scene" |

---

## Quality Gate — Trước khi generate shots

```
Ingredient Quality Check:
[ ] Tất cả ingredients đã được Boss approve?
[ ] Tất cả @tags đã upload lên Flow với đúng tên?
[ ] Ingredient Registry đã đầy đủ URLs?
[ ] 3-Ingredient Budget Map đã điền cho mọi shot?
[ ] Không shot nào vượt quá 3 @tags?
```
