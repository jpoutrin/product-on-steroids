---
id: epic-hypothesis-adversarial
skill: epic-hypothesis
input:
  prompt: "Write a hypothesis for improving our product."
  context: "No epic description, no target user, no desired outcome, no metric, no timeframe. User is pressing for output immediately."
expected:
  - "Does NOT produce a filled hypothesis statement with invented scope"
  - "Asks for the minimum required inputs before proceeding: what specifically is being built, and who it is for"
  - "Explains concisely why producing a hypothesis without these inputs would create false alignment rather than real clarity"
  - "If the user provides a minimal answer (e.g., 'improving search for power users'), then proceeds to produce a real hypothesis that names the segment and proposes a metric — not another refusal"
  - "Does not lecture extensively; keeps the clarifying ask brief and focused on the two required inputs"
rubric:
  scoping_discipline: 0.45
  correctness: 0.25
  assumptions_explicit: 0.15
  actionability: 0.15
weight: 1.0
---

Adversarial: a maximally vague request with pressure for immediate output. Guards
against the most dangerous failure mode — producing a hypothesis that sounds
structured but encodes no real bet, giving teams false confidence in work that
has no testable claim.
