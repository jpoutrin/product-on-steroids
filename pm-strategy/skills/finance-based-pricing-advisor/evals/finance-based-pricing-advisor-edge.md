---
id: finance-based-pricing-advisor-edge
skill: finance-based-pricing-advisor
input:
  prompt: "Is €12/mo a defensible price for our new plan?"
  context: "Variable cost €3/mo per user. Target 75% gross margin. We don't track CAC or churn yet."
expected:
  - "Computes the price floor as 3 / (1 - 0.75) = €12/mo with the arithmetic shown"
  - "Verdicts on gross margin only: (12-3)/12 = 75%, exactly at the floor, PASS"
  - "Marks LTV:CAC and CAC-payback as N/A - needs CAC & lifetime rather than fabricating them"
  - "Notes €12 sits exactly at the floor with zero headroom and flags the risk if costs rise"
  - "Verdict is qualified and states the missing CAC/lifetime data needed for a full check"
rubric:
  correctness: 0.35
  completeness: 0.25
  assumptions_explicit: 0.25
  actionability: 0.15
weight: 1.0
---

Edge: CAC and lifetime are absent. The skill must verdict on gross margin alone, explicitly mark
the LTV:CAC and payback checks N/A, and not invent CAC numbers. Also catches the at-the-floor,
zero-headroom case.
