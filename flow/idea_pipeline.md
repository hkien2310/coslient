# 🗂️ IDEA PIPELINE — Active
> **Đây là file sống.** Coslient GPT tự update sau mỗi bước.  
> Boss không cần sửa tay — chỉ đọc và kéo Kanban card trên web theo đúng status ở đây.  
> Khi video publish xong → Coslient move entry sang `idea_archive.md`, xoá khỏi file này.

---

## 📥 INBOX — Ý tưởng thô chưa evaluate

> Đây là nơi paste idea list từ web vào. Coslient sẽ evaluate và chuyển xuống IN PROGRESS.

<!-- PASTE IDEAS TỪ WEB VÀO ĐÂY -->
<!-- Format mỗi dòng: - [idea text] | added: YYYY-MM-DD -->

*(Trống — đang chờ idea mới từ web)*

---

## 🔄 IN PROGRESS — Đang làm

> Mỗi idea đã được chọn và đang đi qua các bước production.

<!--
STAGE ORDER: inbox → brainstorm → selected → concept → research → song → image → animation → seo → published
KANBAN MAPPING:
  inbox/brainstorm/selected → cột "Ideas" trên web
  concept/research          → cột "Scripting" trên web  
  song/image/animation      → cột "Production" trên web
  seo                       → cột "Ready" trên web
  published                 → cột "Published" trên web (rồi archive)
-->

| ID | Title | Stage | Notes | Updated |
|---|---|---|---|---|
| v052 | The Ocean Keepers | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |
| v053 | The Unplayed Song | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |
| v054 | The Train to the Light | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |
| v055 | The Time Machine of Scents | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |
| v056 | The Wild Horse in the Quiet Room | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |
| v057 | The Pecan Tree's Legacy | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |
| v058 | The Biscuit Tin | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |
| v059 | Last Summer Together | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |
| v060 | The Message in the Margin | `song` | Có lyrics + music. Chưa có image prompts | 2026-06-10 |

---

## 📋 BACKLOG — Đã evaluate, chờ làm

> Idea đã qua Stage 1 (STRONG label), chờ được kéo vào production.

| ID | Title / Idea | Score | Notes | Added |
|---|---|---|---|---|
| — | — | — | *Chưa có idea trong backlog* | — |

---

## ❌ CUT — Đã loại

> Idea đã evaluate và loại. Giữ lại để không brainstorm lại.  
> **Không xoá.** Dùng để tránh lặp lại ý tưởng dở.

| Idea | Lý do loại | Date |
|---|---|---|
| — | — | — |

---

## 📝 HƯỚNG DẪN — Coslient GPT

### Khi Boss paste idea list từ web:
1. Move tất cả ideas vào section INBOX với format chuẩn
2. Chạy evaluate (Stage 1) cho từng idea
3. Gắn nhãn STRONG → move sang BACKLOG, RESHAPE → ghi note, CUT → move sang CUT
4. Báo cáo kết quả cho Boss

### Khi Boss chọn 1 idea để làm:
1. Move từ BACKLOG vào IN PROGRESS
2. Gán ID: `v[số video tiếp theo]` (xem concept_index.md để biết số tiếp theo)
3. Stage bắt đầu: `concept`
4. Update cột `Updated` sau mỗi bước

### Sau mỗi bước production:
Cập nhật cột `Stage` theo thứ tự:
`concept → research → song → image → animation → seo → published`

### Khi video published:
1. Copy toàn bộ row sang `idea_archive.md`
2. Xoá row khỏi IN PROGRESS ở file này
3. Cập nhật `concept_index.md` (add entry mới)

### Web sync workflow:
```
WEB → COSLIENT:  Boss copy ideas từ Kanban "Ideas" column → paste vào INBOX section
COSLIENT → WEB:  Boss đọc stage ở IN PROGRESS → kéo tay card trên web Kanban cho khớp
```

---

*Last updated: 2026-06-10*
