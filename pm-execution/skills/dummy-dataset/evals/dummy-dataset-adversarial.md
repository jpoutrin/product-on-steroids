---
id: dummy-dataset-adversarial
skill: dummy-dataset
input:
  prompt: "Generate customer data."
  context: ""
expected:
  - "Skill asks clarifying questions before proceeding (domain, volume, format, constraints)"
  - "Skill does NOT proceed with a guess or generic 'customer' dataset"
  - "Skill explicitly lists the missing required inputs and why they matter"
  - "Skill provides concrete examples of what 'customer data' could mean (e-commerce, SaaS, financial, etc.)"
  - "After clarification, the output follows all other expectations (structured, constrained, sample rows, quick-start)"
rubric:
  clarity_request: 0.4
  scope_handling: 0.3
  guidance_quality: 0.2
  no_guessing: 0.1
weight: 1.0
---

Adversarial vague ask testing that the skill scopes down and refuses to guess. Prevents
outputting a generic "customer records" dataset without understanding use case, ensuring
the skill clarifies domain, format, and constraints before generating.

