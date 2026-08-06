---
id: pestel-delta-monitor-edge
skill: pestel-delta-monitor
input:
  prompt: "Refresh our PESTEL against the last quarter. Honestly not much happened except one thing: a new data-residency law just passed that forces EU customer data to stay in-region by year end. Baseline attached."
  context: "Five of six factors are genuinely unchanged since the baseline; only Legal has a sharp, material shift. Baseline provided with prior states and ratings."
expected:
  - "Reports the five unchanged factors explicitly as stable with a prior-state reference, rather than only surfacing the Legal mover"
  - "Flags the data-residency law as a Legal shift with direction (rising) and magnitude (major) and cites it as the signal"
  - "Restates Legal impact/likelihood as before then after against the baseline rating"
  - "Maps the residency law to the specific decisions it forces (e.g., data architecture / hosting region / roadmap) with an action and owner/trigger"
  - "Does not manufacture spurious movement in the stable factors to fill the report"
rubric:
  stable_factor_discipline: 0.35
  correctness: 0.25
  decision_mapping: 0.25
  no_fabrication: 0.15
weight: 1.0
---

Edge: mostly-stable environment with a single sharp mover. Guards against two
failures — dropping the unchanged factors (so it stops being a true diff) and
inventing motion in stable factors to pad the output.
