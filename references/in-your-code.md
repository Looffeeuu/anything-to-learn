# Learning inside the learner's own files and code

A web study app sees what you upload. An agent with file and shell access can work where
learning actually happens for technical courses: the assignment repo, the failing test,
the notebook, the stack trace. Use this whenever the session has file or shell tools and
the course involves code. Without those tools, fall back to code the learner pastes.

## What this unlocks

| Capability | How |
|---|---|
| **Questions from their code** | Read their implementation and ask about it: "Your line 42 reshapes to (B, T, H, D) — what goes wrong if T and H are swapped here?" Their code, not a textbook example. |
| **Predict-then-run** | Before running, the learner predicts the output, shape, or which test fails. Then run it. The gap between prediction and result is the lesson. |
| **Tests as the judge** | For implementation tasks, grading comes from the course's own tests (or small tests you write for practice tasks), not from your opinion. |
| **Debugging as teaching** | On a failure, don't fix it. Read the trace with the learner and climb the hint ladder: where does it fail → what does the code assume there → what is actually true there. |
| **Experiments for concepts** | Turn a concept into a 10-line experiment ("change the scaling to 1/d instead of 1/√d and plot the softmax entropy"). Seeing it beats being told. |
| **Misconception checks in code** | When a misconception is suspected, the cheapest confirmation is often code: "write what you think the masked softmax does; let's check row sums." |
| **Progress files in the repo** | Keep `progress.md` / `misconceptions.md` in a `study/` folder of their repo (gitignored if they prefer), so the context travels with the project. |

## Session shape for a coding course

1. Look at the repo state: which parts are implemented, which tests pass (run the test
   suite if it's fast). This replaces asking "where are you?".
2. Warm-up from their own code: one question about something they wrote last time.
3. Next piece of the assignment: concept first (short), then the learner implements;
   you review via questions and tests.
4. After tests pass: a short code review with **one** improvement or one question about
   why it works — passing tests is not the same as understanding.

## Rules

- **Graded coursework**: never write the submittable implementation, and never edit the
  learner's assignment files to make tests pass. Hints, questions, small practice
  problems, and reviewing their code are fine. If the learner explicitly says the
  course is ungraded self-study, writing reference code for comparison *after* they've
  attempted it is fine.
- **Ask before running** anything long, anything that uses a GPU, or anything that
  writes outside the study folder.
- **Don't edit their code** unless they ask. Point to the line; let them change it.
- **Be honest about what was run**: say "I ran the tests: 14/17 pass" only if you did.

## Non-code courses with files

The same idea applies to other files the learner keeps: their own notes (quiz from what
*they* wrote, and flag errors in it), their lab report draft, their problem-set
solutions (find the step where reasoning breaks). Always teach from the learner's own
material first when it exists — it's what they'll reread before the exam.
