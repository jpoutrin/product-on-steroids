---
id: pestel-delta-monitor-happy
skill: pestel-delta-monitor
input:
  prompt: "Here's our PESTEL baseline from November 2025 for our EU B2B fintech and a batch of Q1 2026 signals — ECB held rates, a new EU instant-payments mandate took effect, the AI Act high-risk timeline firmed up, and consumer trust in fintech ticked up in a survey. What changed and what should we revisit?"
  context: "Baseline scan with dated per-factor states and impact/likelihood ratings is provided; new signals are attributed to sources; roadmap and pricing bets riding on the baseline are named."
expected:
  - "References the November 2025 baseline by name/date and frames output as a diff against it, not a fresh scan"
  - "Covers all six PESTEL factors, marking the unmoved ones explicitly as stable rather than omitting them"
  - "Assigns direction and magnitude to each moved factor and cites the specific signal/source for it"
  - "Restates impact/likelihood as before → after for the material shifts (e.g., instant-payments mandate, AI Act timeline)"
  - "Maps each material shift to a specific roadmap/pricing decision to revisit with an action and owner/trigger"
  - "Produces a watch list separating sub-threshold movers from material changes"
rubric:
  diff_discipline: 0.30
  correctness: 0.25
  decision_mapping: 0.25
  completeness: 0.20
weight: 1.0
---

Happy path: a real baseline plus clearly-sourced new signals and named bets.
Guards against the report collapsing into a fresh scan or a vague "things
changed" narrative instead of an anchored, decision-mapped diff.
