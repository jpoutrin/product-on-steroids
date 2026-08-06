---
id: prioritization-frameworks-happy
skill: prioritization-frameworks
input:
  prompt: "We have ~40 backlog features and our leadership wants defensible math on what we build next quarter. Which prioritization framework should we use?"
  context: "Squad of 6. We have reach data from product analytics and can estimate effort in person-months. Exec stakeholders need to see the reasoning."
expected:
  - "Names RICE as the primary framework with a fit rationale tied to the ~40-item scale, available reach/effort data, and the exec audience"
  - "Gives the RICE mechanic: (Reach x Impact x Confidence) / Effort, with the scale for each factor"
  - "Names a fallback (e.g. ICE) for items lacking reach data rather than fabricating a Reach number"
  - "Includes a comparison table listing inputs needed and a tradeoff/failure mode per candidate framework"
  - "States at least one RICE-specific watch-out such as tiny-effort items inflating the score, with a guardrail"
rubric:
  correctness: 0.35
  fit_justification: 0.30
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: the inputs (scale, reach + effort data, exec buy-in) point cleanly at
RICE. Guards against naming a framework without justifying fit, and against
omitting the fallback and the effort-denominator watch-out.
