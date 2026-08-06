---
id: finance-based-pricing-advisor-happy
skill: finance-based-pricing-advisor
input:
  prompt: "We want to charge €25/seat/mo. Does that hold up on the economics?"
  context: "Variable cost €4/seat/mo. Target 80% gross margin. CAC €300. Average lifetime 30 months. Targets: LTV:CAC ≥ 3:1, payback ≤ 18 mo (B2B)."
expected:
  - "Computes the price floor as 4 / (1 - 0.80) = €20/seat/mo with the arithmetic shown"
  - "Guardrail table shows gross margin 84%, LTV:CAC computed as (25 x 0.84 x 30)/300 = 2.1:1, and payback €300/(25 x 0.84) = 14.3 mo"
  - "Verdicts each guardrail PASS/FAIL against its explicit target (margin PASS, LTV:CAC FAIL, payback PASS)"
  - "Names LTV:CAC as the binding constraint and solves the price (or CAC) at which it flips to PASS"
  - "Returns a one-line verdict (PROCEED WITH FIX) with the single most important number"
rubric:
  correctness: 0.4
  completeness: 0.25
  assumptions_explicit: 0.15
  actionability: 0.2
weight: 1.0
---

Happy path: complete inputs allow the full floor + target + guardrail table + binding-constraint
solve. Guards against asserted (uncomputed) ratios and against blessing a margin-safe but
CAC-inefficient price.
