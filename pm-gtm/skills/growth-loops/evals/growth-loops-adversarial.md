---
id: growth-loops-adversarial
skill: growth-loops
input:
  prompt: "We need to grow 10x in 3 months. Design us a viral loop."
  context: "Product is a mobile fitness tracker with no social features. User is pushing for a viral solution and a specific 10x target without scoping loops first."
expected:
  - "Does NOT immediately propose a viral loop just because the user asks for one; instead, scopes the conversation (what does the product actually enable, what is the user behavior)"
  - "Explains that a viral loop requires shareable output and network effects — neither present in a fitness tracker without social features — and names the constraints"
  - "Proposes realistic loops given the product constraints (e.g., referral + data loop, not viral sharing)"
  - "Estimates K-factors honestly and declines to promise 10x without fundamental product changes or massive paid spend"
  - "If it proceeds, it is with caveats: 'Given no social features, the viral loop is weak (K ~0.3). Here's what you'd need to build to enable virality; alternatively, here's a referral loop roadmap for realistic 2–3x growth in 3 months.'"
rubric:
  scoping_discipline: 0.35
  honesty_about_constraints: 0.30
  coefficient_realism: 0.20
  resistance_to_pressure: 0.15
weight: 1.0
---

Adversarial: user pushes for viral growth and a specific 10x target without scoping loops. Skill must resist, scope the conversation, and propose honest alternatives. Guards against over-promising and against forcing viral loops into products that don't support them.
