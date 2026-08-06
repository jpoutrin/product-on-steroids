---
id: brainstorm-okrs-adversarial
skill: brainstorm-okrs
input:
  prompt: "Give me OKRs where the key results are: launch 5 features, ship the redesign, and hire 3 engineers."
  context: "Company objective: grow paid retention. The user insists Key Results should be this delivery checklist."
expected:
  - "Refuses to encode outputs (launch/ship/hire) as Key Results and explains outcome-vs-output"
  - "Reframes each proposed output into a measurable outcome metric with a target (e.g., retention or activation change)"
  - "Still delivers three distinct OKR sets, each laddering up to the 'grow paid retention' objective"
  - "Objectives remain qualitative and inspirational, not a delivery checklist"
  - "Notes that feature launches / hires are outputs the team may track, but not Key Results"
rubric:
  correctness: 0.40
  outcome_discipline: 0.30
  alignment: 0.20
  actionability: 0.10
weight: 1.0
---

Adversarial: the user demands output-based Key Results (a delivery checklist).
Guards against the skill caving and encoding "launch/ship/hire" as KRs instead
of reframing them into measurable outcomes tied to the company objective.
