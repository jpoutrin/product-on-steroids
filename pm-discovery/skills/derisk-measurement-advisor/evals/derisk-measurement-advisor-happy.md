---
id: derisk-measurement-advisor-happy
skill: derisk-measurement-advisor
input:
  prompt: "We're running an A/B test on our SaaS freemium product to test this assumption: 'At least 5 % of free users will upgrade to a paid plan within 14 days when shown a redesigned pricing modal.' Our current upgrade rate is 3.2 % (90-day average, ~200 signups/day). Please design the measurement plan."
  context: "B2B SaaS, freemium tier. Experiment type: server-side A/B test. Billing data available in Stripe. No hard deadline but the team would like to ship within 30 days. MDE: any absolute lift ≥ 1.5 pp is business-meaningful."
expected:
  - "States the assumption in falsifiable form with a null hypothesis"
  - "Names free-to-paid conversion rate (or equivalent) as the primary metric with its definition, data source (Stripe or billing system), and 14-day measurement window"
  - "Provides at least two leading indicators (e.g., modal open rate, plan-page dwell time, checkout-initiation rate) with the earliest time each is readable"
  - "Lists at least two guardrail metrics (e.g., D7 retention, support ticket rate) with explicit floors or ceilings"
  - "Shows baseline (3.2 %), success threshold (≥ 5 %), and derives minimum sample size from power/alpha/MDE inputs — inputs are visible, not just the conclusion"
  - "Converts sample size to a run-duration estimate using the ~200 signups/day traffic figure"
  - "Includes an inconclusive protocol covering extend, pivot, and accept-uncertainty branches"
rubric:
  correctness: 0.40
  completeness: 0.30
  statistical_rigor: 0.20
  actionability: 0.10
weight: 1.0
---

Happy path: the PM provides a quantitative assumption and a chosen experiment
type with enough anchors (baseline rate, traffic volume, MDE) to produce a
full, statistically grounded measurement plan. Guards against output that
declares a threshold without showing the power calculation, or that skips
guardrails and the inconclusive protocol.
