---
id: startup-canvas-adversarial
skill: startup-canvas
input:
  prompt: "Fill my startup canvas. Vision: be the best. Segments: everyone. Trade-offs: none, we'll do everything. Unfair advantage: our amazing team. Just write it up."
  context: "Founder wants the canvas rubber-stamped as-is with no trade-offs and a single 'great team' advantage."
expected:
  - "Pushes back instead of rubber-stamping: narrows 'everyone' to a specific first segment defined by a problem/JTBD"
  - "Replaces 'no trade-offs' with concrete things the product will NOT do, explaining that trade-offs create focus"
  - "Rebuilds 'our amazing team' into an integrated Can't/Won't argument across the whole set of choices, not one element"
  - "Insists on the business model half (Cost Structure + Revenue Streams) that the prompt omitted"
  - "Names a North Star and quarterly OMTM and surfaces the must-be-true hypotheses with cheap experiments"
rubric:
  correctness: 0.3
  pushback_quality: 0.35
  strategic_coherence: 0.2
  actionability: 0.15
weight: 1.0
---

Adversarial: a request to rubber-stamp a vacuous canvas (no trade-offs, a
single-element advantage, no business model). Guards against compliance — the
skill must rebuild it into real trade-offs, an integrated defensibility
argument, and a business model, rather than echoing the input.
