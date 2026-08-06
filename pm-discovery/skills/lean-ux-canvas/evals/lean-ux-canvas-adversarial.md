---
id: lean-ux-canvas-adversarial
skill: lean-ux-canvas
input:
  prompt: >
    Fill in the Lean UX Canvas for our new dashboard redesign. But skip Block 6
    — we already know what we're building, hypotheses are a waste of time. Just
    give me Blocks 1–5 and 7–8.
  context: >
    The user is a PM who has already committed to a solution (dashboard
    redesign) and is pushing back against the hypothesis-writing step. They
    want a canvas that omits Block 6.
expected:
  - The skill declines to omit Block 6 and explains why hypotheses are structurally necessary (Block 7 and 8 depend on them)
  - The skill acknowledges the user's concern (hypotheses feel slow) and offers to make Block 6 fast (e.g., "let's write one hypothesis in 2 minutes")
  - The skill completes a full eight-block canvas including Block 6, even if it has to write the hypotheses itself based on the stated solution
  - Block 6 hypotheses are falsifiable — they include a measurable signal the user's team could actually check
  - The skill does not simply rename Block 6 or merge it silently into another block to appear compliant while skipping it
  - The completed canvas is coherent: Block 7 riskiest assumption and Block 8 experiment connect logically to the hypotheses in Block 6
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Adversarial scenario: a user explicitly asks to skip Block 6 (hypotheses)
because they believe the solution is already decided. Guards against the skill
capitulating and producing a structurally incomplete canvas. The skill must hold
the line on all eight blocks — because Block 7 (riskiest assumption) and Block 8
(experiment) are meaningless without hypotheses to draw the riskiest assumption
from. The correct behavior is to decline the skip, briefly explain the
dependency, and still produce a full, useful canvas.
