---
id: stakeholder-identification-adversarial
skill: stakeholder-identification
input:
  prompt: "Who are the stakeholders for our product?"
  context: "No initiative, no change described, no organizational context provided. User expects an immediate list."
expected:
  - "Does NOT produce a generic stakeholder list before scoping the initiative"
  - "Asks at minimum: what is the initiative and what will it change or decide?"
  - "Asks or infers: is the initiative internal-facing, customer-facing, or mixed?"
  - "Explains why producing a list without initiative scope would result in a low-value generic output"
  - "If the user refuses to provide scope and insists on a list, the skill produces one explicitly labelled as unscoped and provisional, with a prominent warning"
  - "Does not pad the response with a generic 'typical stakeholders include product, engineering, sales...' filler that adds no value"
rubric:
  scoping_discipline: 0.45
  correctness: 0.25
  completeness: 0.20
  actionability: 0.10
weight: 1.0
---

Adversarial: a maximally vague ask with no initiative scope and pressure for an
immediate answer. Guards against the most common failure mode — producing a
generic "product, engineering, sales, marketing, leadership" list that is useless
without initiative context. The skill must hold the scoping line before
proceeding, just as stakeholder mapping is meaningless without knowing what is
being mapped.
