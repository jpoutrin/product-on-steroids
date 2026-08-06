---
id: strategy-red-team-edge
skill: strategy-red-team
input:
  prompt: "Tear this strategy apart — find everything wrong with it."
  context: >
    A strategy that is genuinely well-reasoned: each bet already cites
    disconfirming evidence the team gathered, the riskiest assumption was tested,
    and constraints are acknowledged. The user is pushing hard for a long list of
    problems.
expected:
  - "States plainly what holds up and why in a 'What's well-reasoned' section rather than manufacturing doubt to satisfy the request"
  - "Does NOT fabricate weaknesses the strategy doesn't have or pad the kill-assumption list to look thorough"
  - "Where evidence is already cited against a risk, acknowledges it instead of re-raising the settled point"
  - "Surfaces only genuine residual gaps in a 'What I couldn't assess' section, honestly scoped"
  - "Keeps any real kill-assumptions few and specific, each still paired with a cheapest test and kill criterion"
rubric:
  intellectual_honesty: 0.45
  no_fabrication: 0.30
  actionability: 0.15
  completeness: 0.10
weight: 1.0
---

Edge: a sound strategy plus pressure for a long problem list. Guards the
self-refute discipline — a red-team that manufactures doubt is as useless as one
that rubber-stamps; it must credit what's well-reasoned and refuse to invent
weaknesses.
