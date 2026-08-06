---
id: opportunity-solution-tree-adversarial
skill: opportunity-solution-tree
input:
  prompt: "Here are our opportunities for the OST: (1) build a dark mode, (2) add Slack integration, (3) redesign the dashboard, (4) launch a mobile app. Now generate the solutions and experiments."
  context: "User is presenting a feature wishlist as 'opportunities' and wants the skill to skip straight to solutions and experiments without questioning the framing."
expected:
  - "Does NOT accept the feature list as valid opportunities and proceed directly to solutions"
  - "Explains that the items provided are solutions or features, not customer opportunities (needs/pains)"
  - "Asks for or proposes the underlying customer needs that motivate each feature — reframes at least one as a genuine opportunity (e.g., 'users struggle to use the app in low-light environments' rather than 'dark mode')"
  - "Asks for the desired outcome at the top of the tree before building anything — does not assume one"
  - "If the user insists on proceeding, the skill restructures the tree by inferring plausible customer opportunities behind each feature, labels them as hypotheses, and flags the reframing explicitly"
  - "Does not produce experiments that validate features directly — experiments test whether an underlying customer need is real or whether a solution addresses it"
rubric:
  reframing_discipline: 0.40
  correctness: 0.30
  completeness: 0.15
  actionability: 0.15
weight: 1.0
---

Adversarial: the user presents a classic solution-first, feature-list framing as
"opportunities" and pushes to skip straight to experiments. This is the most
common OST misuse — treating the Opportunities level as a backlog of features
rather than a map of customer needs. Guards against the skill rubber-stamping bad
OST structure and reinforcing the exact failure mode the framework was designed to
prevent (Teresa Torres's "jumping to solutions"). The skill must push back on the
framing while remaining helpful — the right answer is to reframe, not to refuse.
