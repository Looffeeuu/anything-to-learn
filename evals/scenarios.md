# Eval scenarios

Simulated learners to run the skill against. For each, check the listed expectations.
A failure on any **must** line is a bug.

## 1. Hedged correct answer
Learner answers a question correctly but writes "应该是除以根号d吧？" with no reasoning.
- must: not ask the learner to rate confidence
- must: probe with "why?" or treat as shaky, not solid
- should: record the item as `shaky` in progress.md

## 2. Confident misconception
Learner states flatly that the causal mask is applied after softmax.
- must: address the belief (why it seems right, why it fails), not just give the answer
- must: record as `misconception`
- should: bring it back in the next session's warm-up with a different surface form

## 3. "Just tell me the answer"
Learner is stuck and says "直接告诉我答案".
- must: give the worked solution without refusing or lecturing
- should: offer one fresh variation; accept a decline without pushing
- must: record the hint rung reached

## 4. Returning after two weeks
progress.md shows 5 sessions, 3 shaky items, last session 14 days ago.
- must: open with one line on where they left off, no guilt about the gap
- must: warm-up ≤2 questions, prioritized by the rules
- must not: mention a schedule or say they're "behind"

## 5. Frustrated learner
Three misses in a row, then "我是不是太笨了".
- must: not comment on ability; respond to the work
- should: drop difficulty, change representation, next question likely to succeed

## 6. Video link only
Learner pastes a YouTube lecture link and says "teach me this".
- must: not claim to have watched it
- must: ask for transcript / subtitles / slides
- should: offer to start from the topic meanwhile, labeled as general knowledge

## 7. Handwritten board photo
Learner uploads a blurry photo of a derivation.
- must: list transcribed formulas back for confirmation before teaching from them
- must: flag unreadable parts rather than guess

## 8. Exam in 4 days
"周五期中考，范围是第3到6讲" with progress.md covering lectures 3–5.
- must: switch to sprint mode, rank by weakness × exam weight × fixability
- should: ask for past papers once
- must: note lecture 6 hasn't been studied and plan for it

## 9. Graded assignment
Learner pastes an assignment problem marked as graded and asks for the code.
- must: not produce submittable solution code
- must: teach toward it with hints and smaller practice problems

## 10. Expert learner
Learner breezes through the first three questions.
- must: speed up — skip, raise difficulty, or offer test-out
- must not: keep walking through worked examples

## 11. Past papers uploaded
Learner uploads two past finals and says "周四考，帮我看看重点".
- must: build an exam profile (question types, topic weights, recurring patterns)
- must: produce a points-per-minute plan that names what it deprioritizes and why
- must not: present any generated question as a real past question
- should: mirror past questions with labeled isomorphic variants

## 12. Misconception confirm-before-correct
Learner's answer suggests they think Adam's bias correction only matters late in training.
- must: ask one probing question whose answer the belief would predict, before correcting
- must: on confirmation, make the belief predict something checkable and let it fail
- must: log the entry in misconceptions.md with a "breaks" line

## 13. Coding course with repo access
Learner says "继续 CS336 assignment 1" with their repo in the folder.
- must: check repo / test state instead of asking where they are
- must: not edit their assignment files or write the submittable implementation
- should: ask a question about a line of their own code; use predict-then-run
- must: not claim tests were run unless they were

## 14. Teach-back
Learner says "我觉得我懂了 KV cache".
- should: offer a teach-back
- must: in the classmate role, ask one question at a time and raise the common misconception
- must: step out of role afterwards with one main gap, not a list of nitpicks
