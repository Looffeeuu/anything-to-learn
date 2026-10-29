# The misconception map: track what the learner believes, not just what they got wrong

A quiz app knows *that* you got question 7 wrong. A good teacher knows *why*: what
false model in your head produced that answer, and which other questions that same
model will break. This module keeps that second kind of knowledge.

## What a misconception is (and isn't)

- **Misconception** — a specific, coherent false belief that predicts wrong answers
  ("the causal mask is applied after softmax", "a larger learning rate always trains
  faster", "Adam's bias correction matters only at the end of training").
- **Not a misconception**: a forgotten fact (that's a `gap`), a slip in arithmetic, or
  not having learned the topic yet.

The test: can you state the belief as a sentence the learner would agree with? If yes,
it's a misconception. Write it down that way.

## Detecting one

Signals, strongest first:

1. A wrong answer stated confidently with reasoning — the reasoning *is* the belief.
2. The same kind of wrong answer on two differently-worded questions.
3. A correct answer with reasoning that would fail on a variant ("right for the wrong
   reason").
4. In teach-back (see `teach-back.md`), an explanation that contains the false step.

When you suspect one, **confirm before correcting**: ask one question designed so the
belief predicts a specific wrong answer. If they give that answer, it's confirmed.
Correcting a belief they don't hold wastes time and plants the idea.

## Repairing one

Telling someone the right answer rarely dislodges a coherent false model; it gets
filed next to it. Instead:

1. **Surface it.** State the belief back in their words: "So the idea is: we compute
   softmax, then zero out the future positions?" Let them agree.
2. **Make it predict.** Pick a case where the belief gives a clearly checkable
   consequence ("then do the rows still sum to 1?").
3. **Let the prediction fail.** They work it out, or run it in code if there is code.
4. **Replace, don't just delete.** Give the correct model and show it explains both the
   original case and the one that broke the old belief.
5. **Say why the wrong one was tempting.** Usually it's a reasonable generalization
   from something true. This keeps the learner from feeling stupid and helps them spot
   the pattern next time.
6. **Recheck later** with a different surface form (the warm-up picks it up first).

## The map (`misconceptions.md` in the study folder)

```markdown
# Misconceptions — <course>

## M1 · causal mask after softmax                     status: repairing
belief: "softmax first, then zero the future positions"
evidence: 10-28 Q3 (confident, with reasoning); 10-28 teach-back step 4
breaks: any question about row normalization; KV-cache correctness; FlashAttention tiling
why tempting: masking "after" feels natural if you think of mask as filtering outputs
repair: 10-28 showed rows no longer sum to 1 → learner fixed it in code
recheck: next warm-up, ask via a different angle (gradient of masked positions)
links: progress a2
```

Statuses: `suspected` → `confirmed` → `repairing` → `resolved` (passed a recheck in a
new form, days later) or `recurred` (back to `confirmed`, try a different repair).

The **breaks** line is what makes this a map rather than a list: it says which other
topics are at risk. When the learner reaches one of those topics, check the
misconception first.

## Across courses

Some misconceptions are about thinking, not content (always stopping at the formula
without interpreting; treating correlation in an ablation as causation). When the same
one shows up in a second course, note it in the learner notes of both `progress.md`
files — that's a pattern worth naming to the learner once.

## Telling the learner

Don't show the map unprompted. Do tell them, once, when a misconception is resolved:
"That mask-after-softmax idea is gone — you just reasoned it correctly from a new
angle." It's the most useful kind of progress feedback there is, because it's specific
and evidence-based.
