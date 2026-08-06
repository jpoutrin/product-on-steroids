---
id: saas-economics-efficiency-metrics-happy
skill: saas-economics-efficiency-metrics
input:
  prompt: "Assess our SaaS unit economics and efficiency and tell me whether we should spend more on sales. Last quarter: S&M €600k, 40 new logos, ARPA €500/mo, gross margin 78%, monthly logo churn 1.5%, net new ARR €900k annualized, net cash burn €1.2M, YoY growth 60%, operating margin −20%."
  context: "B2B SaaS, mid-market. Founder wants a spend decision backed by the numbers."
expected:
  - "Computes CAC (€600k / 40 = €15k) and shows the formula with the numbers plugged in"
  - "Computes gross-margin-adjusted LTV and CAC payback (payback = CAC / (ARPA × GM) = 15000 / (500×0.78) ≈ 38 months) and LTV:CAC"
  - "Computes burn multiple (~1.33), magic number, and Rule of 40 (60 + (−20) = 40) with named benchmarks and healthy/watch/unhealthy verdicts"
  - "Delivers a scorecard table plus a read that names the driving metrics and a concrete accelerate/fix/extend decision"
  - "States whether CAC is blended or new-logo and flags at least one pitfall"
rubric:
  correctness: 0.35
  completeness: 0.25
  benchmark_grounding: 0.20
  actionability: 0.20
weight: 1.0
---

Happy path: a full input set. Guards against skipping formulas, omitting the
gross-margin adjustment, or giving a verdict without benchmarks or a decision.
