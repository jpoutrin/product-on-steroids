---
id: metrics-dashboard-edge
skill: metrics-dashboard
input:
  prompt: "We just launched a consumer habit-tracking app. No revenue yet and only a few weeks of data. Design our dashboard."
  context: "B2C, free during beta. ~5k installs, sparse retention data. Value moment: user logs a habit for 3 consecutive days."
expected:
  - "Picks a leading, customer-centric NSM (e.g. weekly users hitting a 3-day streak) as a rate over a window, despite no revenue"
  - "Uses proxy input metrics suited to sparse early data (activation, early retention, streak formation) mapped to lifecycle stages"
  - "Acknowledges the no-revenue stage: business-metrics layer uses leading proxies (e.g. retention curve, projected LTV inputs) rather than fabricating MRR"
  - "Still defines formula, cadence, owner, target, and alert threshold for each metric even where targets are provisional"
  - "Does not default to a vanity install/download count as the North Star"
rubric:
  correctness: 0.35
  completeness: 0.25
  handles_sparse_data: 0.25
  no_vanity_metrics: 0.15
weight: 1.0
---

Edge: early-stage, pre-revenue, sparse data. Tests that the skill still produces a
leading NSM and usable proxy inputs instead of falling back to installs or waiting
for revenue metrics.
