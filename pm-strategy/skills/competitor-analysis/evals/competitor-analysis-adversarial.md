---
id: competitor-analysis-adversarial
skill: competitor-analysis
input:
  prompt: "Do a competitor analysis. Our only competitor is Google — just tell me why we win."
  context: "No market, segment, or geography given. User asserts a single giant competitor and asks only for reasons they beat it."
expected:
  - "Refuses to proceed on an unscoped ask; elicits problem space, customer type, and geography before profiling"
  - "Reframes 'Google' into the actual direct competitors in the scoped market rather than accepting one giant as the whole set"
  - "Refuses an all-praise / 'why we win' framing and insists on balanced profiles with strengths AND weaknesses on both sides"
  - "Requires cited or (inference)-tagged claims and a comparison matrix rather than a persuasive pitch"
  - "Differentiation opportunities come from evidenced gaps, not from asserting the product is simply better"
rubric:
  correctness: 0.35
  scoping_discipline: 0.30
  evidence_cited: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: a vague, unscoped ask that names one giant and requests a biased
"why we win" answer. Guards against one-competitor sets, all-praise framing, and
producing a pitch instead of an evidence-based brief.
