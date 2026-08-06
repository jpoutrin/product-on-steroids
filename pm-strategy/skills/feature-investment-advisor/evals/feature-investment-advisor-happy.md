---
id: feature-investment-advisor-happy
skill: feature-investment-advisor
input:
  prompt: "We have 5 product areas and 8 teams. Advise how to allocate them next year."
  context: >
    Areas (current teams): Core Platform (3, ROI med / fit high / risk low),
    Usage-Based Billing (1, ROI high / fit high / risk med),
    Mobile App (2, ROI med / fit med / risk low),
    Legacy Reporting (1.5, ROI low / fit low / risk low),
    AI Assistant (0.5, ROI unproven-high / fit med / risk high).
    Baseline is today's team split. No hard mandate.
expected:
  - "Assigns each of the 5 areas a disposition of invest, maintain, or divest"
  - "Recommends a % of capacity per area that sums to 100% and shows the delta vs the current 8-team baseline"
  - "Ties allocation to the stated 8-team capacity rather than floating numbers"
  - "Recommends an H1/H2/H3 horizon mix that sums to 100% with a justification"
  - "Divests or starves Legacy Reporting and redeploys the freed capacity explicitly"
  - "Gives an advisor-voice reason per disposition naming the ROI-vs-fit-vs-risk trade-off, not just a score"
rubric:
  correctness: 0.35
  completeness: 0.25
  allocation_discipline: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a real multi-area portfolio with ROI/fit/risk reads and a team
baseline. Guards against producing a ranked list instead of a summed, baselined
allocation with dispositions and a horizon mix.
