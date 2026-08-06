---
id: porters-five-forces-adversarial
skill: porters-five-forces
input:
  prompt: "Is the AI industry attractive to get into? Just give me a yes or no."
  context: "No category boundaries, customer type, geography, or vantage point specified. 'AI' spans chips, foundation models, apps, and services. User is pushing for a one-word answer."
expected:
  - "Does NOT return a bare yes/no verdict for an undefined 'AI industry' under the pressure"
  - "Explains that 'AI' is not a single industry (chips vs. foundation models vs. applications have opposite force profiles) and that attractiveness is position-dependent"
  - "Asks for or proposes explicit boundaries (category, customer type, geography) and a vantage point before rating forces"
  - "If it proceeds, it scopes down to one defined slice, states the scope, and rates the five forces with evidence rather than hand-waving an overall verdict"
  - "Does not average or assert ratings without evidence"
rubric:
  scoping_discipline: 0.40
  correctness: 0.25
  evidence_quality: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: a vague, oversized ask with pressure for a one-word answer. Guards
against the core failure mode — declaring an undefined, sprawling "industry"
attractive-or-not without scoping it or grounding the forces in evidence.
