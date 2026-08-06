---
id: feature-investment-advisor-edge
skill: feature-investment-advisor
input:
  prompt: "Allocate our 6 teams across these areas, but the CEO mandate is: protect the core AND put at least 15% of capacity into new bets this year."
  context: >
    Areas: Core Platform (ROI med / fit high / risk low), Payments (ROI high /
    fit high / risk med), Integrations (ROI med / fit med / risk low),
    New Vertical Bet (ROI unproven / fit med / risk high). Core is currently ~55%
    of capacity. New bets are currently ~5%.
expected:
  - "Treats the mandate as binding: keeps the core protected (maintain/invest, not starved) while raising new-bet capacity to >= 15%"
  - "Reflects the >= 15% new-bet floor in both the allocation table and the H3 (explore) share of the horizon mix"
  - "Names at least one area to divest or starve to fund the mandated increase, with freed capacity redeployed"
  - "Allocation sums to 100% and horizon mix sums to 100%"
  - "Explicitly reconciles the recommendation against the mandate rather than ignoring the >= 15% constraint"
rubric:
  correctness: 0.35
  constraint_adherence: 0.35
  allocation_discipline: 0.2
  actionability: 0.1
weight: 1.0
---

Edge: an explicit mandate (protect core, >=15% to new bets) that must bind the
horizon mix and force a funding trade-off. Guards against unconstrained
allocation that ignores the leadership floor.
