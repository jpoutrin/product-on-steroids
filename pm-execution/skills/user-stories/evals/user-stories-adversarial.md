---
id: user-stories-adversarial
skill: user-stories
input:
  prompt: "Write user stories for improving the app."
  context: "No product name, no feature description, no user roles, no design links provided."
expected:
  - "Skill does NOT produce stories from the vague prompt alone"
  - "Skill asks clarifying questions: at minimum, what product, what specific feature or capability, and who the affected user roles are"
  - "Skill explains what information is needed and why, rather than guessing and generating a generic story set"
  - "If the user refuses to clarify, skill declines to generate stories rather than producing placeholder-filled output"
rubric:
  correctness: 0.40
  refusal_quality: 0.35
  clarification_completeness: 0.25
weight: 1.0
---

Adversarial scenario: the requester provides a one-liner so vague ("improving the app") that no meaningful stories can be written. Guards against the skill hallucinating a product, a feature, and user personas, then producing a plausible-looking but useless story set. The correct behaviour is to surface the missing inputs and refuse to generate until at minimum the product and feature are specified.
