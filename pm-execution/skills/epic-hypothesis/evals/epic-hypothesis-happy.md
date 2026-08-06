---
id: epic-hypothesis-happy
skill: epic-hypothesis
input:
  prompt: "Write an epic hypothesis for our onboarding checklist epic."
  context: "B2B SaaS product. Target users: first-time workspace admins. Epic: add an in-app guided onboarding checklist for new accounts. Current 30-day feature activation rate: 34%. Team OKR: increase activation to ≥ 50% this quarter. Next release cycle is 8 weeks."
expected:
  - "Produces a hypothesis statement following the canonical form: We believe [X] for [user] will [outcome], measured by [metric]. We'll know in [timeframe]."
  - "Fills every bracket with a specific, non-generic value — no placeholders remain"
  - "Names 'first-time workspace admins' (or equivalent specific segment), not generic 'users'"
  - "States 30-day feature activation as the metric with 34% baseline and a directional target"
  - "Sets the timeframe to 8 weeks or a specific date"
  - "Lists at least one leading indicator and one lagging indicator in the success criteria table"
  - "Surfaces at least one low- or med-confidence assumption with a suggested validation method"
  - "Includes anti-goals that guard against metric gaming"
rubric:
  correctness: 0.35
  completeness: 0.30
  assumptions_explicit: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: a well-scoped epic with a named user segment, an existing baseline
metric, and a team OKR. Guards against vague statement form, missing baselines,
and forgotten leading indicators.
