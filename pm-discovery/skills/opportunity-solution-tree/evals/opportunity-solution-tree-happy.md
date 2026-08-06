---
id: opportunity-solution-tree-happy
skill: opportunity-solution-tree
input:
  prompt: "Build an OST for our mobile fitness app. Our desired outcome is to increase D30 retention from 28% to 40% this quarter."
  context: "Research signal: 10 user interviews conducted. Key themes: (1) users lose motivation after day 3 when they don't see progress — 8/10 mentioned this; (2) workout plans feel too generic and don't adapt to the user's fitness level — 6/10; (3) users forget to open the app — 5/10 reported missing planned sessions; (4) social accountability features are absent — 4/10 mentioned working out with friends as motivating. Analytics: D7 retention is 52%, D30 drops to 28% — the cliff is between D7 and D30."
expected:
  - "Desired Outcome section states the single metric (D30 retention), baseline (28%), and target (40%)"
  - "Opportunities are framed from the customer's perspective (needs/pains), not as features or solutions"
  - "Each opportunity has an evidence anchor (interview count or analytics observation)"
  - "Opportunities are ranked by priority using Opportunity Score or qualitative rating with stated rationale"
  - "Top 2-3 opportunities each have at least 3 candidate solutions tagged with generative lens (PM/Designer/Engineer)"
  - "Each experiment includes hypothesis, method, primary metric, and success threshold — not just a vague 'test it'"
  - "No opportunity is secretly a feature or solution in disguise"
rubric:
  correctness: 0.35
  completeness: 0.30
  format_adherence: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: rich research signal, a clear desired outcome with baseline and
target, and four distinct opportunity themes. Guards against collapsing
opportunities into features and against vague experiment specs ("let's A/B test
it" with no hypothesis or success threshold). Also guards against ranking without
stated rationale.
