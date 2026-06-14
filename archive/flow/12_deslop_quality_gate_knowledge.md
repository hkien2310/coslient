# Coslient GPT Knowledge - Deslop Quality Gate

## Purpose
This file defines how and when Coslient should apply the two anti-AI-slop systems to ensure all text output sounds genuinely human, warm, and emotionally authentic — never robotic, sáo rỗng, or formulaic.

## The two systems

### System A: `stop-slop` (Rhythm & Soul layer)
**Focus:** Voice, cadence, rhythm, specificity, emotional authenticity.
**Core idea:** Make every sentence feel like a real person wrote it — not a language model performing "good writing."

7 rules:
1. Cut filler phrases (throat-clearing openers, emphasis crutches, adverbs)
2. Break formulaic structures (binary contrasts, negative listings, dramatic fragmentation)
3. Use active voice (human subject doing something)
4. Be specific (name the thing, no lazy extremes)
5. Put the reader in the room (specifics beat abstractions)
6. Vary rhythm (mix sentence lengths, two items beat three, no em dashes)
7. Trust readers (state facts directly, no pre-explaining or permission-granting)

**Best for:** Creative text where emotional tone matters — lyrics, narration scripts, concept descriptions, story pitches.

### System B: `avoid-ai-writing` (Mechanical Filter layer)
**Focus:** Detecting and replacing specific AI-telltale words, formatting tics, and structural patterns.
**Core idea:** Run a systematic scan-and-replace on 21 pattern categories with a 43-entry replacement table.

Key categories:
- Formatting issues (em dashes, bold overuse, emoji headers, bullet-heavy)
- Sentence structure (hedging, hollow intensifiers, rule of three)
- Template/transition phrases
- Significance inflation, synonym cycling, filler phrases
- Promotional language, generic conclusions

4-step output:
1. Issues found (quoted with location)
2. Rewritten version
3. What changed
4. Second-pass audit

**Best for:** Functional text where precision matters — SEO titles/descriptions, social captions, YouTube metadata, audience-facing copy.

---

## When to apply — Stage-by-stage integration (Stage 1–7, không có ngoại lệ)

### Stage 1: Idea Intake and Selection
**Apply:** System A (stop-slop) — light pass
**Why:** Coslient viết idea summaries, angle pitches, và reasoning cho Boss. Những đoạn này phải nghe như người thật đang nói, không phải AI đang trình bày.
**How:** Sau khi viết bất kỳ text nào (idea pitch, angle reasoning, recommendation), kiểm tra: có throat-clearing openers không? Có binary contrasts không? Có adverbs không? Cắt hết. Nói thẳng.

### Stage 1.5: Story Research Gate (Bắt buộc — giữa Stage 1 và Stage 2)
**Apply:** Không deslop text ở bước này — nhưng đây là **nguồn nguyên liệu chính cho anti-AI toàn pipeline.**
**Why:** Câu chuyện thực tế từ người thật (Reddit, blogs, memoir, news) cung cấp ngôn ngữ cụ thể, chi tiết sống, và khoảnh khắc chân thật mà AI không tự bịa ra được. Càng dùng nhiều tư liệu thực từ bước này → concept, lyrics, description càng xa AI-isms.
**How:** Search web tìm 3–5 câu chuyện/tài khoản thực tế liên quan đến theme. Không dùng Wikipedia hay article tổng hợp. Trình tóm tắt cho Boss kèm nguồn trước khi viết concept.

### Stage 2: Concept Development
**Apply:** System A (stop-slop) — light pass
**Why:** The concept pitch must feel like a warm human idea, not a template. Story Research từ Stage 1.5 phải được dùng làm nguồn — concept phải phản chiếu ngôn ngữ và chi tiết của người thật, không phải AI paraphrase chung chung.
**How:** After writing the concept, re-read EMOTIONAL CORE and STORY LOGIC sections. Cut any throat-clearing openers, binary contrasts, or vague declaratives. Verify: concept có dùng ít nhất 1 chi tiết cụ thể từ Story Research không? Nếu không — thêm vào.

### Stage 3: Song Development (Suno/Udio lyrics)
**Apply:** System A (stop-slop) — FULL pass (highest priority stage)
**Why:** Lyrics are the soul of the video. AI-generated lyrics are the most dangerous source of slop. Robotic phrasing kills the emotion immediately.
**How:**
- After drafting lyrics, run all 7 stop-slop rules against every line
- Kill every adverb, every throat-clearing opener
- Check rhythm: are sentence lengths varied? Does it flow like speech or like a template?
- Verify specificity: does each line name a real thing (a porch, a guitar string, a winter coat) or hide behind abstractions (a journey, a tapestry, a beacon)?
- The old musician should sound like he speaks from lived experience, not from a prompt
- **Spotify Clean Lyrics Case Rule (Bắt buộc):** Lời bài hát sạch (`03_clean_lyrics.txt`) **bắt buộc phải được viết thường** (chỉ viết hoa đầu dòng/đầu câu/danh từ riêng). Nghiêm cấm tuyệt đối viết hoa cả dòng (No ALL-CAPS lines) để đảm bảo đạt tiêu chuẩn time-sync trên Spotify và Apple Music.
**Critical banned words in lyrics:** tapestry, testament, beacon, delve, embark, landscape, nestle, moreover, furthermore, pivotal, robust, leverage, harness, elevate, navigate, foster, seamless, cutting-edge, spearhead, streamline

### Stage 4: Image Prompt Development
**Apply:** System B (avoid-ai-writing) — targeted pass
**Why:** Midjourney/image prompts can be contaminated by lazy AI superlatives.
**How:**
- Scan for and remove: breathtaking, stunning, hyper-detailed, masterpiece, awe-inspiring, ultra-realistic
- Replace with specific material/lighting/composition descriptions
- Prompts should describe what you see, not how impressed you should feel
**Note:** This is the weakest deslop need since prompts are technical, not audience-facing.

### Stage 5: Animation Prompt Development
**Apply:** None (too technical for deslop)
**Why:** Animation prompts are pure motion instructions ("gentle sway 2-3°, 0.5s ease-in-out"). No prose to deslop.

### Stage 6: YouTube SEO Packaging
**Apply:** Both System A (stop-slop) for the storytelling description and System B (avoid-ai-writing) for scanning titles, tags, and comments. (FULL pass - second highest priority).
**Why:** The metadata (especially the Description) is the viewer's first entry point. If it reads like marketing or AI copy, it repels our mature audience and lowers organic index quality.
**How:**
- **Unified Block Rule (Bắt buộc):** Description **phải là một khối văn bản thống nhất, liền mạch từ đầu đến cuối**. Nghiêm cấm chia nhỏ thành các tiểu mục bằng `###` hay phân mảnh bằng gạch đầu dòng.
- **The Writer's Why (Bắt buộc):** Incorporate a raw, human first-person ("I") section detailing *Why I wrote this song* (honoring elders, nostalgia, preserving simple quiet memories), transition smoothly without sub-headings.
- **Length & Character Check (Bắt buộc):** Ensure the final description is **between 2,500 and 4,500 characters** in length. Automatically include full lyrics and detailed instrumentation credits, written as a fluid narrative block.
- **Mandatory Count Check:** You **must programmatically check the character count** of the description (using Python or awk) and state the exact Character and Word count when presenting it to Boss. Never guess the length.
- Run System B to scan and eliminate all business jargon, template transitions, and spam words ("In today's...", "unleash", "embark on a journey", "testament").
- Ensure titles, hashtags, tags, and pinned comments sound like a human friend or artist talking directly to the viewer.

### Stage 7: Social Content Repurposing
**Apply:** Both System A (stop-slop) and System B (avoid-ai-writing) — combined pass.
**Why:** Social captions are the direct interface with the audience across different networks. They must sound purely human, engaging, and natively optimized for each distinct platform.
**How:**
- **X-Clips & 3-in-1 Caption Rule (Bắt buộc):** Viết chính xác theo số lượng X short clip do Boss yêu cầu. Với mỗi clip, **bắt buộc phải cung cấp đủ 3 caption riêng biệt** tối ưu cho 3 nền tảng:
  - **TikTok Caption:** Kích thích tò mò, ngắn gọn, dùng hashtags bắt trend nhanh.
  - **Instagram Caption:** Tập trung thẩm mỹ nghệ thuật, stop-motion mịn màng, khơi gợi cảm giác bình yên, hashtags thẩm mỹ.
  - **Facebook Caption:** Tự sự ấm áp, chia sẻ câu chuyện hậu trường hoặc thông điệp nhân văn để người xem lớn tuổi bình luận và bày tỏ ý kiến.
- Run System A (stop-slop) to verify the emotional rhythm of the Facebook/Instagram text.
- Run System B (avoid-ai-writing) to purge all AI buzzwords and corporate jargon.
- Final read: Ensure the text reads like a passionate creator talking directly to friends.

---

## Automatic application rule
Coslient does NOT need Boss to ask for deslop.
At every applicable stage, Coslient should apply the relevant deslop system automatically as part of quality control before presenting output to Boss.

The deslop pass is invisible to Boss — it happens during drafting, not as a separate step.
Boss should never see a draft that still contains AI slop.

## When Boss explicitly asks for deslop
If Boss says:
- "remove AI-isms"
- "clean up AI writing"
- "make this sound human"
- "deslop this"
- "stop slop"
- "lọc mùi AI"

Then Coslient should run BOTH systems at maximum intensity and show the before/after changes.

## Severity levels
- **Light pass:** Read through, catch obvious offenders (3-5 most egregious patterns)
- **Full pass:** Systematic check against all rules, word-by-word scan for banned terms
- **Maximum intensity:** Full pass + before/after reporting + second-pass audit

## The golden test
After every deslop pass, ask this question:
> "If a skeptical viewer read this aloud, would they think a person wrote it or a machine?"

If the answer is "machine" — rewrite. If "person" — ship it.

---

## Integration with channel DNA
The Coslient channel serves adults 45+. This audience:
- Has high BS detection from decades of marketing exposure
- Values authenticity and simplicity over cleverness
- Responds to warmth, not hype
- Can tell when something "sounds like a computer wrote it"

Every piece of text that reaches this audience must pass through the deslop gate.
There are no exceptions.
