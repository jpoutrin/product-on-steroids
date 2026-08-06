---
id: decision-memo-adversarial
skill: decision-memo
input:
  prompt: "Write a decision memo about our go-to-market strategy."
  context: "No options specified. No decision owner named. No deadline. No specific choice framed."
expected:
  - "Does NOT produce a memo around a vague topic; refuses to draft until the decision question is specific"
  - "Asks the user to sharpen the question into a specific, bounded choice (e.g., which channel, which segment, which timing)"
  - "Asks who the decision owner is and what the response deadline is before drafting"
  - "Explains briefly why a memo without a specific question and owner would not drive a decision"
  - "If it proceeds after scoping, the subject line frames a specific question, not a topic"
  - "Does not invent a decision owner, options, or deadline that were not provided"
rubric:
  scoping_discipline: 0.45
  correctness: 0.25
  actionability: 0.20
  completeness: 0.10
weight: 1.0
---

Adversarial: the user asks for a "decision memo" but provides a vague topic with
no decision question, no options, no owner, and no deadline — the four inputs
that make a memo functional. Guards against the skill drafting a generic strategy
document dressed up as a memo, which would give the appearance of driving a
decision without actually doing so.
