# The knowledge map: one living framework, with cards linked off it

What the learner keeps from studying is not a pile of per-session summaries. It is one
document that shows the whole subject, grows each session, and links out to the
details. Per-session summary tables fragment the subject by date; nobody rereads them,
and they never show how today's idea connects to last week's.

So the learner-facing record has exactly two kinds of files:

- **`map.md`** — the single overall framework. Edited every session, never duplicated.
- **Cards** — one file per concept, practice set, or worked case, linked from map nodes.

`progress.md` and `misconceptions.md` stay the tutor's internal notebook. The map is
what the learner sees and rereads.

## The map (`map.md`)

````markdown
# <Subject> · 总脉络
主线：<one sentence: what the whole subject is about>
来源：<source pack inputs> · 最近更新：<date>

```mermaid
graph LR
  A["镜像阶段"] --> B["自我 / 主体"]
  B --> C["大他者"]
  C --> D["欲望"]
  D --> E["对象 a"]
```

## 一、<part> ●
- **<concept>** ● <one or two sentences in plain words: what it is, how it connects>
  → [卡片](concepts/<concept>.md) · [练习 3 题](practice/<concept>.md) · [案例：…](cases/<case>.md)
  <!-- tutor: src S3,S4 · causal links: … · common misconceptions: … -->
- **<concept>** ◐ …（曾误解为「…」，已纠正；修订于 11-02）
- **<concept>** ⚠ … 目前理解为「…」，待纠正
- **<concept>** ○ （未学）<one line from the source so the shape is visible>

## 二、<part> ◐
…

## 学习日志
- 11-03 · 大他者、欲望 vs 要求（新增）· 镜像阶段（修订）
- 11-02 · 镜像阶段、自我 vs 主体
````

### Rules for the map

1. **Organised by concept, never by date.** Dates live only in the log at the bottom,
   one line per session, naming the nodes touched.
2. **Whole skeleton from day one.** When the map is first built (from the source pack,
   in workflow step 2), every part and concept goes in — unlearned ones marked ○ with a
   one-line preview. The learner sees the full shape of the subject and where they are
   in it from the first session.
3. **Merge, don't append.** Each session edits existing nodes or attaches new ones under
   the right parent. Never add a "today's summary" section or a new summary file.
4. **Revise, don't stack.** When understanding changes — a misconception repaired, a
   definition sharpened — rewrite the node and mark `（修订于 MM-DD）`. Do not keep the
   old wording next to the new one.
5. **Nodes stay short.** One or two sentences in the learner's own terms (reuse their
   teach-back phrasing when it was right). Quotes, examples, derivations and questions
   go to cards. The node's job is position and connection.
6. **Status marks, no due dates.** ● solid / durable · ◐ new, shaky or gap · ○ not yet
   studied · ⚠ open misconception (with the belief in a few words). Derived from
   `progress.md`; never shown as tasks or reminders.
7. **Size.** Keep `map.md` to about two screens. Past ~30 nodes, split by part into
   sub-maps (`maps/<part>.md`) and keep only the parts, their status and one line each
   on the main map. The Mermaid diagram shows parts and key relations, ~15 nodes max;
   labels short and in quotes.
8. **Provenance stays.** Each node's hidden tutor comment lists its source chunks
   (`src S3,S4`) so a card or answer can cite slide/page/minute.
9. **Tutor-only planning goes in the hidden comment** (`<!-- tutor: … -->`): the key
   causal links used to score teach-backs, the common misconceptions for the topic. It
   is invisible when the map is rendered and keeps the visible map clean.

The map's shape follows the subject: a theory (Lacan, Foucault) is a concept network
with relations between parts; a technical course (CS336) is closer to a tree of
modules → capabilities. Same rules either way.

## Cards

Create a card only when there is something to put in it. Each card starts with a back
link: `← [总脉络](../map.md) · 相关：[大他者](大他者.md) [欲望](欲望.md)`.

| Folder | One card per | Holds |
|---|---|---|
| `concepts/` | concept | source excerpts with citation · the learner's explanation · examples **and** a contrast case · how it differs from look-alikes · misconceptions met and how they were repaired |
| `practice/` | concept (not per day) | questions asked, the learner's answers, the feedback, newest at the top; generated questions labelled as generated |
| `cases/` | case or application | applying the subject to something concrete — for a theory, analysing a person, text or event; for a technical course, a worked problem or a piece of the learner's code |
| `exam/` | mock exam (only with an exam) | the mock, the learner's answers, the debrief by cause of lost points; the profile itself stays in `exam-profile.md` (see `exam-backsolve.md`) |

Domains can rename folders when it reads better (`derivations/` for a maths course,
`code/` for a coding course); say so once in the map header.

When a session adds to a card, add to the existing card. A second card for the same
concept is the same mistake as a second summary table.

## Link format — ask once

When the map is first created, ask in one line, alongside workflow step 2's questions:

> 笔记里的链接用哪种格式？① 标准 Markdown `[卡片](concepts/x.md)`，任何编辑器都能点开；
> ② Obsidian 双链 `[[x]]`，能看知识图谱，但离开 Obsidian 不好用。

Record the answer in `progress.md`'s header (`Link style: markdown | wikilink`) and use
it everywhere. No answer → standard Markdown. If they switch later, convert all files
in one pass.

## Updating at the end of a session

Part of every session close (`session.md` § Closing):

1. Update the nodes touched: status marks, revised wording, new links.
2. Add or extend the cards the session produced (practice answers, a new example, a
   case the learner analysed).
3. Add one log line.
4. Tell the learner in one line what changed, e.g. 「总脉络已更新：新增「欲望 vs 要求」，修订「镜像阶段」，练习 +3。」

## Where the map lives

| Environment | How |
|---|---|
| File access (Claude Code, Codex, Cursor, desktop with a connected folder, …) | Files in the study folder as above. For a coding course: `study/` inside the repo. |
| No files, but a document tool with tabs (e.g. Claude's Docs artifacts) | One document per subject. First tab = the map; one tab per card group (概念 / 练习 / 案例), each card a heading inside it. Link nodes to tabs or headings. Edit the same document every session — never create a new one. |
| Plain chat, nothing else | At session close, give the full updated `map.md` in one Markdown block for the learner to save over the old one (cards only when changed). Next session, ask them to paste it back. |

## Migrating existing summaries

If the learner already has per-session summary tables or notes from earlier sessions:

1. Read them all; build the map once from their combined content plus the source pack.
2. Move examples, quotes and questions into cards; keep the learner's own wording.
3. Ask before deleting or moving the old files. Default: move them to `archive/`
   untouched, so nothing is lost.
4. Show the new map and say what came from where in one or two lines.
