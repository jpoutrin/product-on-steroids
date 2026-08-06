---
id: business-model-happy
skill: business-model
input:
  prompt: "Build a Business Model Canvas for an on-demand ride-hailing app."
  context: "Two-sided: urban riders wanting fast, cashless rides; drivers wanting flexible income. Monetization via a take rate per ride. Proposed business."
expected:
  - "Populates all 9 blocks with no empty or TBD block"
  - "Treats it as multi-sided: distinct rider and driver customer segments each with its own value proposition"
  - "Revenue Streams name a concrete capture mechanism (take rate per ride) and pricing logic, not 'figure out later'"
  - "Cost Structure separates fixed vs variable and identifies the model as value-/network-driven"
  - "Includes a coherence note showing the create-side (drivers/supply) enables the rider value prop, and a viability check (revenue > cost at scale, LTV vs CAC)"
  - "Labels inferred blocks as assumptions and names the key risk (e.g. driver retention)"
rubric:
  correctness: 0.35
  completeness: 0.3
  coherence: 0.2
  actionability: 0.15
weight: 1.0
---

Happy path: a clear two-sided marketplace with obvious segments and a stated
monetization mechanism. Guards against empty/TBD blocks, an "everyone" segment,
and a canvas whose blocks do not reinforce each other or get an economics check.
