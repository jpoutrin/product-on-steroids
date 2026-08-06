---
id: metrics-dashboard-adversarial
skill: metrics-dashboard
input:
  prompt: "Just build me a dashboard with total signups, total pageviews, and cumulative downloads as the top KPIs. That's what the board wants."
  context: "B2C freemium app with a paid tier. Value moment: user completes a first project. Board is fixated on big up-and-to-the-right numbers."
expected:
  - "Refuses to make cumulative signups/pageviews/downloads the North Star, naming them as vanity metrics that don't change decisions"
  - "Substitutes a value-moment NSM expressed as a rate/ratio over a window (e.g. weekly users completing a first project)"
  - "Explains the swap using good-metric criteria (comparative, ratio/rate, behavior-changing) rather than just complying"
  - "Builds a proper metric tree with input, health, and business layers instead of a flat KPI list"
  - "May retain the requested counts only as clearly-labeled secondary/context metrics, not as the North Star"
rubric:
  correctness: 0.3
  rejects_vanity_metrics: 0.35
  completeness: 0.2
  actionability: 0.15
weight: 1.0
---

Adversarial: user explicitly demands vanity metrics as top KPIs. Tests that the
skill pushes back with the good-metric criteria and delivers an actionable
value-moment tree rather than rubber-stamping the request.
