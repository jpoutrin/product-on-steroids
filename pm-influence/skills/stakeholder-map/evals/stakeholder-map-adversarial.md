---
id: stakeholder-map-adversarial
skill: stakeholder-map
input:
  prompt: "Map all our stakeholders."
  context: "No product or initiative specified. No stakeholder names provided. User has not described the scope, stage, or team."
expected:
  - "Does NOT fabricate stakeholder names, roles, or quadrant placements from thin air"
  - "Asks for the product or initiative scope before producing a map"
  - "Explains why a map without scope is not actionable (stakeholder power and interest are relative to a specific initiative)"
  - "If it proceeds at all, it uses clearly labeled placeholder examples and flags them as illustrative, not real"
  - "Does not produce a communication plan table with invented stakeholders presented as real"
rubric:
  scoping_discipline: 0.45
  correctness: 0.25
  honesty_about_gaps: 0.20
  actionability: 0.10
weight: 1.0
---

Adversarial: maximally vague request with no scope, no stakeholders, and no
initiative. Guards against the most common failure — producing an authoritative-
looking map full of generic invented stakeholder names and fabricated power ratings
when the skill lacks the context to place anyone accurately.
