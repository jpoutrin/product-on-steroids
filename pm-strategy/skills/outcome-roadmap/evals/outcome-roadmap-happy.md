---
id: outcome-roadmap-happy
skill: outcome-roadmap
input:
  prompt: "Turn this into an outcome roadmap. Q2: build advanced search filters, add AI recommendations, redesign the dashboard. Q3: add saved carts, one-click reorder."
  context: "E-commerce marketplace. Objective: grow repeat-purchase revenue. Baselines available: search-to-purchase 4.1 min, repeat-order rate 22%, search-session conversion 6%."
expected:
  - "Restates each output as an Enable [segment] to [outcome] so that [business impact] statement"
  - "Collapses related outputs (search filters + AI recommendations) into a shared discovery outcome where they serve one result"
  - "Attaches a success metric with baseline to target using the provided baselines (e.g., search-to-purchase 4.1 min to a target)"
  - "Maps outcomes to the stated objective of growing repeat-purchase revenue"
  - "Expresses release windows as quarters/ranges rather than hard calendar dates"
  - "States the customer-need assumptions each outcome rests on"
rubric:
  correctness: 0.35
  completeness: 0.25
  measurability: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a real feature-list roadmap with objectives and baselines. Guards
against leaving outputs as features and against unmeasurable outcome rows.
