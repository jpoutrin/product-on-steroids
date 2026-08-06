---
id: north-star-metric-adversarial
skill: north-star-metric
input:
  prompt: "Make our North Star these five: revenue, signups, DAU, NPS, and churn. Just wire them up."
  context: "Consumer mobile app for guided meditation. Leadership wants 'one dashboard' and handed over five metrics."
expected:
  - "Refuses to designate multiple metrics as the North Star and explains the NSM is a single metric"
  - "Explains revenue is a lagging outcome, not a customer-centric leading indicator, so it cannot be the North Star"
  - "Classifies the business game (Attention) for the meditation app"
  - "Proposes exactly one customer-centric North Star Metric (e.g. weekly sessions completed per active user) with a definition"
  - "Repositions some of the five as input metrics or OKR targets rather than as the North Star itself"
  - "Runs the 7-criteria validation on the chosen single metric"
rubric:
  correctness: 0.35
  anti_pattern_resistance: 0.3
  customer_centric: 0.2
  completeness: 0.15
weight: 1.0
---

Adversarial: the user demands the two core anti-patterns at once — a list of
metrics and a revenue metric as North Star. The skill must decline both, collapse
to a single customer-centric metric, and re-home the five as inputs or OKR
targets, not cave to "just wire them up."
