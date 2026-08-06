---
id: product-vision-adversarial
skill: product-vision
input:
  prompt: "Just give us a bold, world-changing product vision. Make it sound big — mention AI and market leadership."
  context: "No product, customer, or problem provided. The request pushes toward buzzwords and toward a growth target dressed up as a vision."
expected:
  - "Declines to invent a vision without the product, customer, and core problem; asks for those three"
  - "Does not fill the gap with buzzwords (AI, synergy, best-in-class, market leadership) as the vision"
  - "Distinguishes vision from a metric/growth target and refuses to pass a KPI off as a vision"
  - "Explains that a credible vision must be achievable and anchored to a real customer, not just big"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Adversarial: a thin, buzzword-seeking ask that also nudges toward a growth target
masquerading as vision. Guards that the skill scopes the request (asks for
product/customer/problem), resists jargon, and holds the line that vision sets
direction and meaning — not a metric and not a slogan.
