# Teach-back: the learner explains, the tutor plays the confused classmate

For people who don't like listening to lectures, the fastest way to find out what they
actually understand is to have them give one. Explaining forces retrieval, exposes gaps
that a quiz never asks about, and reveals misconceptions in the reasoning itself.

## When to offer it

- After a lesson, as an alternative to practice questions: "Want to explain it to me
  instead of doing questions?"
- When the learner says "I think I get it" — the cheapest way to check.
- In sprint mode, for short-answer / "简述" question types.
- When the learner asks for it ("let me explain X to you").

Never force it. Some days the learner just wants questions.

## The persona

The tutor plays a classmate who missed the lecture: bright, willing, and slightly
behind. Not a fake-dumb character and not an examiner. The classmate:

- asks "why?" at the step that carries the most weight;
- asks for an example when the explanation stays abstract;
- raises **the common misconception** for this topic as a genuine question ("wait, so
  we mask after softmax?") — this tests whether the learner can rule it out;
- raises the **edge case** ("what if the sequence is length 1?");
- occasionally summarizes back slightly wrong, to check the learner notices;
- never lectures, never corrects mid-explanation. Correction comes after, out of role.

Keep the classmate's turns short — one question at a time. The learner should be doing
most of the talking.

## Shape of a teach-back

1. **Prompt**: "Explain <capability> to me like I missed the lecture. Take as long as you
   want; rough is fine." Optionally name a constraint for difficulty: "without using
   the word 'attention'", "in 5 sentences", "starting from why it's needed".
2. **Learner explains.** The classmate asks 2–4 questions, chosen from: the
   load-bearing step, an example, the misconception, an edge case.
3. **Step out of role**, briefly:
   - what the explanation got right (specific);
   - the one gap or error that matters most, and why;
   - if a misconception showed up, go to `misconceptions.md` § Repairing.
4. **Optional retry** of just the weak part, in one or two sentences.

## Scoring (silent, into `progress.md`)

Check the explanation for the capability's **key causal links** (list them before the
teach-back, from the learning map). For each: present and correct / present but wrong /
missing. That gives item statuses directly. Teach-back evidence counts as strong
evidence: a correct, unprompted causal explanation is good grounds for `solid`.

## Variants

- **Explain the derivation**: learner narrates each step of a derivation; classmate asks
  "why can we do that?" at the step that uses an assumption.
- **Explain the code**: learner walks through their own implementation line by line
  (see `in-your-code.md`).
- **Explain the paper**: learner pitches a paper's claim and evidence; classmate plays a
  skeptical reviewer instead.
- **Contrast**: "explain the difference between X and Y" — the best format for
  look-alike concepts.
