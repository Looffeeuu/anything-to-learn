# Lesson modes

Generate each lesson when the learner reaches it, in the mode that fits the material
and what they already know. A lesson is short: one capability, a handful of new ideas.

## Choosing attempt-first vs. example-first

- **Example-first** when the procedure or idea is genuinely new and the learner has
  little to build on. Asking a novice to "try first" on something they have no handle
  on produces frustration, not productive struggle.
- **Attempt-first** when they have prior knowledge that connects (a related method, the
  previous lesson, intuition from their field). A 1–2 minute prediction before the
  explanation then helps.
- Unsure? Ask one quick question that doubles as a diagnostic ("Have you seen X before?
  How would you guess Y works?"), and choose from the answer.

Whichever comes first, the shape converges: explanation → worked example with the *why*
of each step → a contrast (a look-alike case where it does NOT apply) → the learner
does one on their own → one variation.

## Modes by material type

### Procedural (algorithms, SQL, derivation recipes, tool usage)
Worked example → completion task (part done, they finish) → independent task → task
where the method isn't named. Fade the support quickly for capable learners.

### Conceptual (theory, definitions, "why does X work")
Concrete instance → general principle → contrast case → learner explains it in their
own words ("explain to a classmate who missed the lecture"). Check the explanation for
the key causal link, not the wording.

### Mathematical / proofs
Show the proof's *plan* before its steps ("we'll bound A, then show B dominates").
Then the learner fills in one step; then reconstructs the plan from memory; then a
variant with one hypothesis changed — "what breaks?".

### Reading a paper or technical report
Questions before reading: what problem, what claim, what evidence would convince you.
Learner skims → states the claim in one sentence → tutor and learner go through the
method and the key figure/table → "what's the weakest point of this evidence?" →
connect to something they already know.

### Code / implementation
Read before write: predict what a snippet outputs or where it breaks. Then implement a
small piece with tests as the judge. When the code is graded coursework, guide with
questions and hints only; don't write the submittable solution.

### Memorization-heavy (terminology, facts, vocabulary)
Short retrieval rounds in mixed order, each item in a slightly different prompt form;
build connections (mnemonics, grouping by structure) rather than repeating lists.

## Explaining well

- Define every term the learner hasn't seen before it carries any weight, in plain
  words: what it is, what distinguishes it from its neighbors, why it matters here.
- One name per concept. If the course uses two names, say so once and pick one.
- Cite the source chunk when teaching course content ("slide 14 / [S7]") so the learner
  can go back to it.
- Prefer the representation that fits: diagram for structure, table for comparison,
  code for procedure, equation for relationships. Don't decorate.
