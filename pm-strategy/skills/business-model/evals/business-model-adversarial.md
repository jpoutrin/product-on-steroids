---
id: business-model-adversarial
skill: business-model
input:
  prompt: "We have an app. Make me a business model canvas."
  context: "No description of what the app does, who it serves, or how it makes money."
expected:
  - "Refuses to fabricate all 9 blocks from nothing"
  - "Elicits the required inputs first: what the business sells and to whom"
  - "Does not invent a value proposition, customer segments, or revenue mechanism out of thin air"
  - "Explains that a canvas whose blocks are guessed is worse than no canvas, since it hides the missing information"
  - "Optionally offers to draft a scaffold once the offer and target customer are provided, labeling any inference as an assumption"
rubric:
  correctness: 0.4
  input_discipline: 0.35
  actionability: 0.25
weight: 1.0
---

Adversarial: a near-empty ask. The skill must not hand-wave a full 9-block canvas;
it must elicit the offer and the customer before drafting, and refuse to pass off
guessed blocks as a business model.
