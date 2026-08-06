---
id: saas-revenue-growth-metrics-happy
skill: saas-revenue-growth-metrics
input:
  prompt: "Here are our monthly MRR movements — give me the revenue-retention and growth picture."
  context: "Mid-market B2B SaaS. Start MRR 100k. New 15k, expansion 12k, contraction 3k, churned 6k. End MRR 118k. Retention on a TTM basis."
expected:
  - "Builds an MRR bridge that reconciles: 100k + 15k + 12k - 3k - 6k = 118k"
  - "Computes NRR = (100 + 12 - 3 - 6) / 100 = 103% and GRR = (100 - 3 - 6) / 100 = 91%"
  - "Computes ARR growth from the movements and the SaaS quick ratio = (15 + 12) / (3 + 6) = 3.0"
  - "Attaches a good/median/weak benchmark band per metric matched to mid-market B2B"
  - "Interprets NRR against GRR and reads the quick ratio 3.0 as below the >=4 efficient-growth bar"
  - "States the retention basis (TTM) and does not report bare percentages"
rubric:
  correctness: 0.40
  completeness: 0.25
  benchmarking: 0.20
  interpretation: 0.15
weight: 1.0
---

Happy path: all four MRR movements plus start/end given, so the bridge, NRR, GRR,
ARR growth, and quick ratio are all computable. Guards against un-reconciled
bridges, missing GRR, and reporting values without benchmarks or basis.
