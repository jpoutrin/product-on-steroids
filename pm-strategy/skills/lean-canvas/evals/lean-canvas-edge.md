---
id: lean-canvas-edge
skill: lean-canvas
input:
  prompt: "I want to build an AI app that summarizes meetings. Make me a Lean Canvas."
  context: "Solution-first pitch. No customer segment named, no problem stated, no pricing or cost data provided."
expected:
  - "Does not accept the solution as-is; elicits or explicitly frames the underlying problem and the customer segment before or while drafting"
  - "Anchors the Problem block on a real problem (not a restated solution) with plausible existing alternatives"
  - "Labels every block filled without evidence as an explicit assumption rather than stating it as fact"
  - "Still produces all nine blocks plus a riskiest-assumptions list"
  - "Ranks problem/segment fit as a top riskiest assumption with a cheap test (e.g. customer interviews)"
rubric:
  correctness: 0.30
  problem_framing: 0.30
  assumptions_explicit: 0.25
  completeness: 0.15
weight: 1.0
---

Edge: a solution-first request with no problem or segment. Guards against the
canvas being solution-led, against inventing facts, and forces the skill to
restore Lean Canvas's problem-first ordering and flag unknowns as assumptions.
