---
id: roadmap-planning-edge
skill: roadmap-planning
input:
  prompt: "Plan next quarter — but heads up, we're stretched thin this cycle."
  context: >
    4 squads, 13-week quarter. A major platform migration is eating ~40% of
    capacity as KTLO, one squad is fully on incident on-call, and a planned hire
    slipped so one squad is at half strength all quarter. Themes: Growth, Reliability.
    Leadership still expects "meaningful movement on Growth."
expected:
  - "Computes a sharply reduced available capacity after subtracting the 40% migration, full on-call squad, and half-strength squad"
  - "Allocation table sums to the shrunken available capacity, not raw headcount"
  - "Explicitly cuts or defers scope to fit reduced capacity rather than overcommitting"
  - "Makes the capacity crunch and its trade-off visible to leadership as a stakeholder input with a resolution"
  - "Still sequences remaining work with rationale and sets a review rhythm to re-evaluate as the hire lands"
rubric:
  correctness: 0.35
  capacity_realism: 0.30
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge: a capacity-crunch quarter. Guards against the common failure of planning
against nominal headcount and overcommitting; the plan must reconcile to a
shrunken available capacity and make the cut explicit rather than hidden.
