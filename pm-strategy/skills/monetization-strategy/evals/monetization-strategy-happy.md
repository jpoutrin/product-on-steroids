---
id: monetization-strategy-happy
skill: monetization-strategy
input:
  prompt: "How should we monetize our new text-to-speech API for developers?"
  context: "B2B, sold to engineers who embed it. Usage varies wildly per customer. Priority is revenue with land-and-expand. No pricing decided yet."
expected:
  - "Proposes 3-5 distinct revenue models (not near-duplicates of one model)"
  - "Each model names an explicit value metric and explains why it tracks delivered value"
  - "Surfaces usage-based / metered as a strong fit for the variable-usage B2B API context"
  - "Each model has audience fit, a unit-economics sketch, 1-2 risks, and a validation experiment with a go/no-go rule"
  - "Includes a comparison table and recommends 1-2 models to test first, considering a hybrid"
  - "Does NOT set price levels; refers price-setting to pricing-strategy"
rubric:
  correctness: 0.35
  completeness: 0.25
  value_metric_explicit: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a clean B2B API with an obvious usage signal. Guards against
single-model answers, models without a named value metric, and drifting into
price-level setting.
