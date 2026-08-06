---
id: pre-mortem-adversarial
skill: pre-mortem
input:
  prompt: "Our product is basically 'we're going to disrupt the entire industry.' Can you do a pre-mortem?"
  context: "Vague vision statement. No defined customer segment. No competitive positioning. 'We'll figure out the business model later.' Team is excited but unfocused. Launch 'soon.'"
expected:
  - "Refuses to produce a speculative pre-mortem and asks for boundary-setting first (product definition, customer segment, timeline)"
  - "Points out that risks can't be identified without knowing what the product is or who it's for"
  - "Suggests narrowing scope (e.g., 'What's the first customer segment?' 'When do you actually launch?') before running the exercise"
  - "Does NOT produce a generic risk list that could apply to any startup"
  - "If a pre-mortem is attempted, it focuses on risks inherent to vagueness (e.g., unfocused features, undefined GTM, misaligned incentives)"
rubric:
  scope_discipline: 0.4
  boundary_setting: 0.3
  refusal_quality: 0.2
  helpfulness: 0.1
weight: 1.0
---

Adversarial: intentionally vague ask without boundaries. Skill must resist the temptation to fill in gaps and instead enforce that pre-mortem needs a defined product scope. Guards against producing noise when input is too abstract, and against false confidence in risks when the product itself is undefined.
