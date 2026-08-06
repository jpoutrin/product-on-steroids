---
id: brainstorm-experiments-existing-adversarial
skill: brainstorm-experiments-existing
input:
  prompt: "Just test if this works. Does the new feature work? How do we know?"
  context: "No context on what 'it' is, what success looks like, who users are, or what constraints exist."
expected:
  - "Refuses to generate vague experiments; instead, asks clarifying questions about the feature, assumptions, and constraints"
  - "Explicitly names what is missing (hypothesis, success metric, method, cost estimate) before proceeding"
  - "Either provides a template or example of what a well-formed experiment request looks like"
  - "Demonstrates that undefined 'success' cannot be tested and offers to help once the user clarifies"
  - "Does NOT output a table with placeholder experiments or opinion-based metrics like 'Users like it'"
rubric:
  refusal_rigor: 0.4
  clarification_quality: 0.35
  guidance_helpfulness: 0.25
weight: 1.0
---

Adversarial: vague, untestable input; missing all context. Guards against generating pseudo-experiments that look rigorous but rest on undefined assumptions, and validates that the skill demands measurable hypotheses and concrete constraints before proceeding.
