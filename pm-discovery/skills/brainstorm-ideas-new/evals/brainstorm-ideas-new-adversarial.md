---
id: brainstorm-ideas-new-adversarial
skill: brainstorm-ideas-new
input:
  prompt: "We want to brainstorm a new product for improving productivity. We think there's a market opportunity with mobile-first working. Generate as many ideas as possible — we'll figure out the business model later."
  context: "Productivity, mobile, vague. No target segment identified. No specific customer problem articulated. Budget unconstrained. Time pressure: needs ideas by EOD."
expected:
  - "Skill does NOT produce a massive list of generic ideas (e.g., 'task management', 'note-taking', 'calendar sync', 'AI assistant')"
  - "Skill pushes back on vague opportunity statement and asks for segment + problem clarification before ideating"
  - "If skill proceeds despite vagueness, ideas are at least grounded in a narrowed assumption (e.g., 'assuming field service workers')"
  - "Quality Bar prevents shipping 50 mediocre ideas; skill prioritizes depth over volume"
  - "Assumptions acknowledge missing constraints (no business model, time pressure) but remain grounded in customer reality"
rubric:
  resistance_to_scope_creep: 0.3
  pushback_on_vagueness: 0.25
  depth_over_volume: 0.25
  assumption_discipline: 0.2
weight: 1.0
---

Adversarial: vague problem + unconstrained scope + time pressure. Guards
against shipping unfocused, generic ideation. Validates that the skill enforces
the Quality Bar and resists "generate 100 ideas" requests that produce noise
instead of signal. Tests whether the skill prioritizes clarity over speed.
