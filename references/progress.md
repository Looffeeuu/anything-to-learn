# Progress tracking (silent), warm-ups, and sprint mode

`progress.md` is the tutor's notebook, not the learner's to-do list. Keep it precise;
never present it to the learner as tasks or reminders. If they ask to see it, show it.

## Format

```markdown
# Progress — <course>
Last session: 2026-10-28 · Sessions: 4
Where we are: learning-map capability 3 (multi-head attention), lesson half done
Learner notes: knows PyTorch well; prefers code over equations; exam? none set

## Items
| id | item | src | status | last seen | evidence |
|----|------|-----|--------|-----------|----------|
| a1 | softmax scaling by √d | S4 | solid | 10-26 | derived it unprompted |
| a2 | causal mask shape | S6 | misconception | 10-28 | thought mask is applied after softmax, confidently |
| a3 | KV-cache memory formula | S9 | shaky | 10-21 | needed hint rung 3 |
```

**Item** = one thing that can be tested on its own (a fact, a step, a distinction, a
derivation). Keep items small enough that one question can probe one.

**Status** values, from evidence (see `session.md` § Inferring confidence):

| status | meaning |
|---|---|
| `new` | taught, not yet tested |
| `misconception` | wrong and confident — top priority |
| `gap` | wrong or unknown, no false belief |
| `shaky` | right but needed hint rung ≥3, or right with wrong/missing reasoning, or hedged |
| `solid` | right, reasoned, no hints |
| `durable` | solid on two occasions at least a few days apart, in different surface forms |

A `durable` item that is later missed drops back to `shaky`.

## Picking warm-up questions

Pick 1–2 items, in this priority:

1. `misconception` (and open entries in `misconceptions.md`, asked from a new angle)
2. `gap` / `shaky` last seen ≥1 day ago
3. `new` from the previous session
4. `solid` not seen for the longest time (≥ about a week)
5. `durable` items only occasionally, mostly when sprint mode is on

Prefer items that the session's new material builds on — the warm-up then doubles as the
lead-in. Always change the surface form from the last time the item was asked.

That's the whole spacing mechanism: intervals grow naturally because solid items drop
down the priority list, and weak items come back sooner. No dates are ever shown to
the learner.

## Sprint mode

Turn on only when the learner names an exam, quiz, or deadline. Record it in the header.

1. **Build or refresh the exam profile** (`exam-backsolve.md` Steps 1–2): past papers,
   homework, the teacher's hints, scope.
2. **Points-per-minute plan** (Step 3): rank by exam value × gap ÷ time to fix. Show
   the top of the list against the learner's time budget; say what's deprioritized.
3. **Sessions become isomorphic practice** (Step 4) in exam format and notation,
   interleaving topics — on an exam, choosing the method is part of the test.
4. **One mock** under timed conditions near the end, if the learner wants it, debriefed
   by cause of lost points (Step 5).
5. The day before: a light pass over the highest-weight items, not new material.

Sprint mode ends after the exam date; mention once, after it, that weak items remain in
the notebook if they ever want to continue.

## When there's no file system

Keep the same table in the conversation. At the end of a session, offer a compact
version (header + items that aren't `durable`) for the learner to paste next time, or
save it to the platform's memory if available and the learner wants that.
