---
id: brainstorm-okrs-happy
skill: brainstorm-okrs
input:
  prompt: "Brainstorm Q3 OKRs for our onboarding team."
  context: "Company objective: double net-new active teams this year. Baselines: onboarding CSAT 61%, 2-day completion 41%, median time-to-value 55 min."
expected:
  - "Produces exactly three OKR sets, presented with equal weight, none pre-declared the winner"
  - "Each Objective is qualitative, inspirational, and time-bound (not a metric or a task)"
  - "Each set has ~3 Key Results that are measurable outcomes with numeric targets, using the given baselines"
  - "Every set's rationale ladders up to the 'double net-new active teams' company objective"
  - "The three sets are genuinely distinct strategic bets, not reworded versions of one"
  - "Includes a How-to-Choose section with trade-offs for the team to converge"
rubric:
  correctness: 0.35
  completeness: 0.25
  alignment: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a clear company objective and real baselines, so the skill can set
credible targets and ladder every set up to strategy. Guards against fewer than
three sets, output-based KRs, and near-duplicate options.
