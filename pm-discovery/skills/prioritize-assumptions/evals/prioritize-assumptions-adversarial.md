---
id: prioritize-assumptions-adversarial
skill: prioritize-assumptions
input:
  prompt: "Prioritize assumptions. Here's what we think: the market is huge, everyone will want this, AI will solve everything."
  context: |
    No structured list provided. The user has given three vague, high-confidence assertions (not testable assumptions).
    No confidence levels, no impact scoring guidance, no discovery evidence.
expected:
  - "Skill asks for clarification: testable assumption format (specific claim, metric, customer segment)"
  - "Refuses to prioritize vague statements ('everyone will want this', 'huge market')"
  - "Asks the user to reframe as testable hypotheses (e.g., 'At least 20% of X will pay Y for Z')"
  - "Does not output a false matrix based on hand-wavy input"
  - "Either declines gracefully OR provides a structured elicitation that turns input into prioritizable assumptions"
rubric:
  correctness: 0.35
  completeness: 0.25
  boundary_defense: 0.25
  teaching: 0.15
weight: 1.0
---

Adversarial case: vague, over-confident input that does not meet the skill's requirement for "testable assumptions with confidence levels." Skill must detect this and either decline or ask clarifying questions to convert hand-waving into ranked assumptions. Guards against: garbage-in-garbage-out (outputting a fake matrix), false precision (treating vague ideas as equally ranked), or silently accepting bad input. Tests whether the skill enforces its input contract and educates the user.
