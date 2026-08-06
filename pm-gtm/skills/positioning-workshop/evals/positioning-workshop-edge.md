---
id: positioning-workshop-edge
skill: positioning-workshop
input:
  prompt: "Run a positioning workshop for Loopback, our B2B customer-feedback routing tool."
  context: |
    Loopback automatically routes customer feedback from support tickets, NPS surveys, and sales calls
    to the relevant product squad in real time.
    Team: PM, Head of Product, VP Sales, CX Director.
    Strong disagreement on Exercise 1: VP Sales insists the primary competitive alternative is
    "Salesforce + manual tagging by a RevOps analyst"; CX Director insists it is "Slack channels
    + spreadsheets maintained by CX." Both claim their alternative is what customers actually use.
expected:
  - "Does NOT silently pick one alternative and discard the other"
  - "Surfaces the disagreement in Exercise 1 as a flagged tension with both positions captured"
  - "Completes all remaining exercises using both alternatives as the comparison set, or explicitly notes which one is used and why"
  - "Exercise 2 attributes are evaluated against both alternatives, not just one"
  - "Positioning statement in Exercise 6 is internally consistent with whichever alternative set was used, and the tension is noted if unresolved"
  - "Summary recommends a validation step (e.g. customer interview) to resolve the alternative disagreement before finalising the statement"
rubric:
  tension_handling: 0.35
  correctness: 0.30
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge case: genuine team disagreement on the primary competitive alternative —
the most common point of failure in real positioning workshops. Guards against
the facilitator picking a side silently or producing a statement that only
satisfies one stakeholder's mental model. The skill must hold the tension and
still produce a usable summary.
