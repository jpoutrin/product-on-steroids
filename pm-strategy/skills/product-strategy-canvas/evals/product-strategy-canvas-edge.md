---
id: product-strategy-canvas-edge
skill: product-strategy-canvas
input:
  prompt: "I have an early idea: an AI tutor for kids. Can you make a product strategy canvas? I don't have metrics, competitors mapped, or a growth plan yet."
  context: "Sparse inputs — early-stage idea, no metrics, no competitive data, no defined growth motion. Only a rough concept and audience are given."
expected:
  - "Still produces all 9 sections rather than refusing, but explicitly labels thin cells (metrics, growth, defensibility) as HYPOTHESES rather than presenting them as fact"
  - "Proposes candidate North Star / OMTM as hypotheses to validate, not fabricated numbers"
  - "Narrows the vague audience into 1–2 problem/JTBD-defined segments and names a plausible first segment"
  - "Surfaces the critical unknowns (competition, willingness to pay, safety/trust) as numbered hypotheses with low-effort experiments"
  - "Flags where more input is needed instead of inventing competitive or metric data"
rubric:
  handles_sparse_input: 0.35
  hypotheses_labeled: 0.30
  segment_focus: 0.20
  actionability: 0.15
weight: 1.0
---

Edge: sparse inputs from an early-stage idea. The skill must complete the canvas
by labeling under-supported cells as hypotheses with validation steps, rather
than either refusing or fabricating metrics and competitive data.
