---
id: north-star-metric-happy
skill: north-star-metric
input:
  prompt: "Help us pick a North Star Metric for our team wiki / docs product."
  context: "B2B SaaS. Customers are software teams; core value is capturing and finding knowledge fast. Vision: 'the shared brain for every team.' We track signups and MRR today."
expected:
  - "Classifies the business game as Productivity with a one-line justification"
  - "Proposes exactly one customer-centric North Star Metric with a precise definition (unit and time window)"
  - "Scores the candidate against all seven criteria, each pass/fail with a reason"
  - "Gives 3-5 input metrics, each with a definition and its causal link to the NSM"
  - "Does not use MRR/revenue as the North Star and explains it is a lagging outcome"
rubric:
  correctness: 0.35
  completeness: 0.3
  customer_centric: 0.2
  actionability: 0.15
weight: 1.0
---

Happy path: a clear productivity product with a stated vision and a value action,
so the skill can classify the game, define one customer-centric NSM, run the
7-criteria check, and derive a real input-metric constellation. Guards against
defaulting to the tracked revenue metric.
