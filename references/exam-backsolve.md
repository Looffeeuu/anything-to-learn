# Exam back-solving: study what the exam asks, in the order that buys the most points

The headline feature. Most AI study tools teach the whole course and then quiz you.
This module starts from the other end: **what does this exam actually test, and what is
the fastest path from where the learner is now to those points?**

Turn it on when the learner gives an exam/quiz and any of: past papers, problem sets,
homework, a scope statement ("第3–6讲"), or what the teacher said will be on it. It also
powers sprint mode (`progress.md` § Sprint).

## Step 1 — Collect evidence about the exam

Ask once, in one message, for whatever exists. Don't block on missing pieces.

| Evidence | Weight | Notes |
|---|---|---|
| Past exams from this course/teacher | highest | the single best predictor; note year and whether the teacher changed |
| Teacher's explicit statements ("重点", "必考", review-session slides) | high | record verbatim with source |
| Homework / problem sets | high | teachers reuse their own problem shapes |
| Scope statement / syllabus | medium | defines the boundary, not the weights |
| Time spent in lecture per topic (from slides/transcript length) | low | rough prior when nothing else exists |
| Nothing at all | — | say so; fall back to the learning map and label the plan as a guess |

Never invent past-exam content. If the learner describes a question from memory, record
it as `source: learner recollection`.

## Step 2 — Build the exam profile (`exam-profile.md`)

Tag every past question with: topic (→ learning-map capability), question type, points,
and the *skill it actually demands* (recall a definition / run a procedure / derive /
choose a method / explain / debug / design).

```markdown
# Exam profile — <course> <exam name>
Date: 2026-11-06 · Duration: 120 min · Format: closed book, 6 questions
Evidence: 2023 + 2024 finals, HW1–5, teacher's review slides (2026-10-30)

## Question types
| type | share of points (past) | typical shape | example |
|---|---|---|---|
| derivation | 35% | "derive X under assumption Y, then interpret" | 2024 Q3 |
| computation | 30% | numbers given, compute and explain one step | 2023 Q2 |
| short concept | 20% | 3–5 lines, "why does X" | 2024 Q1(a–d) |
| design / open | 15% | small scenario, choose and justify | 2023 Q6 |

## Topics
| capability | appeared in | points (avg) | trend | notes |
|---|---|---|---|---|
| C3 attention complexity | 2023 Q2, 2024 Q3 | 18 | every year | always asks memory, not just FLOPs |
| C5 KV cache | 2024 Q5 | 10 | new in 2024 | teacher said "重点" in review slides |

## Recurring patterns
- Every derivation question ends with "interpret the result in one sentence" — 2–4 pts
  lost by students who stop at the formula.
- Notation: uses d_model, not d; batch first.
```

Show the learner a short version: top 5 topics by points, question-type split, and one
or two patterns worth knowing. That alone is useful to them.

## Step 3 — The points-per-minute plan

For each capability, estimate:

- **Exam value** `V` — expected points, from the profile
- **Gap** `G` — from `progress.md` status (`durable` 0 … `misconception` 1); unknown
  items get a quick 1-question probe rather than a guess
- **Cost** `T` — rough minutes to bring it to `solid` (small fact: 5; procedure: 20–40;
  derivation the learner has never seen: 60+)

Rank by `V × G / T`. Show the learner the top of the list with the time budget:

```
5 days, ~2 h/day you said. Where the points are:
1. KV-cache memory (10 pts, you're shaky, ~25 min)          ← start here
2. "Interpret the result" habit (2–4 pts × 3 questions, ~10 min of practice)
3. Attention complexity derivation (18 pts, you know half, ~40 min)
...
Low priority for this exam: positional encoding variants (0 pts in 2 years).
```

Say what you're skipping and why — the learner decides. Low-value topics aren't
forbidden, just ordered last.

## Step 4 — Isomorphic practice

Generate practice that matches the exam's **form**, not just its topics:

- Same question types in the same proportions; same notation and conventions; same
  phrasing style ("证明…", "简述…", "设计…").
- **Isomorphic variants** of past questions: keep the structure and the skill it tests,
  change the surface (numbers, names, which variable is unknown, one added constraint).
  Label each with the past question it mirrors, so the learner sees the pattern.
- Include the recurring traps found in Step 2 on purpose ("interpret the result").
- Grade with the point split a teacher would use; show where partial credit is won or
  lost, because that is what changes the score.

Never present a generated question as a real past question.

## Step 5 — Mock and debrief (optional)

Near the exam, offer one timed mock in the real format and length. Debrief by points
lost, grouped by *cause* (didn't know / knew but misapplied / ran out of time / lost
partial credit on presentation) — each cause has a different fix. Update `progress.md`.

## Boundaries

- Past exams for this course might be restricted by the teacher; if the learner says so,
  don't push for them.
- Scoring predictions are estimates; say so, and never promise a grade.
