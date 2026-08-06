---
id: market-sizing-adversarial
skill: market-sizing
input:
  prompt: "How big is the AI market? Just give me one number."
  context: "No product, segment, geography, or customer type specified. User is pushing for a single figure."
expected:
  - "Does NOT return a single unscoped number in response to the pressure"
  - "Asks for or proposes explicit market boundaries (problem space, customer type, geography) before sizing"
  - "Explains why one global 'AI market' number is not decision-useful and would be indefensible"
  - "If it proceeds, it sizes a scoped-down slice and reports TAM/SAM/SOM with the scope stated, not the whole undefined space"
  - "Surfaces assumptions and their confidence rather than presenting a figure as fact"
rubric:
  scoping_discipline: 0.40
  correctness: 0.25
  assumptions_explicit: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: a vague, oversized ask with pressure for a single number. Guards
against the most common failure mode — producing an authoritative-sounding
one-number market size for an undefined market.
