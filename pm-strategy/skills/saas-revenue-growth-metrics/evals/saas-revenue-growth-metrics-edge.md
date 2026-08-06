---
id: saas-revenue-growth-metrics-edge
skill: saas-revenue-growth-metrics
input:
  prompt: "Our ARR went from 1.2M to 1.5M this year. What's our retention?"
  context: "Enterprise SaaS, annual prepaid contracts. Only the start/end ARR snapshot is available; no breakdown of new/expansion/contraction/churned."
expected:
  - "Computes ARR growth rate = (1.5 - 1.2) / 1.2 = 25% and reports it with its basis"
  - "States that NRR and GRR CANNOT be computed from a start/end snapshot alone and requests the new/expansion/contraction/churned movements"
  - "Does not fabricate an MRR bridge or invent movement figures to force a retention number"
  - "Flags the annual-prepay pitfall: MRR-based monthly metrics are distorted by lumpy annual billing"
  - "Names what input is needed (the MRR/ARR movements, ideally on a cohort/TTM basis) to produce retention"
rubric:
  correctness: 0.30
  refuses_to_fabricate: 0.35
  pitfall_awareness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge: only a single start/end ARR pair with annual-prepay billing. The skill can
report growth but must decline to compute NRR/GRR, ask for the movements, and
flag prepay lumpiness rather than manufacture a bridge.
