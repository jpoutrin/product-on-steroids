---
id: roadmap-communication-happy
skill: roadmap-communication
input:
  prompt: "Turn our H1 roadmap into a brief for the exec team ahead of the quarterly review. I need them to approve two engineers for the activation work."
  context: "Roadmap themes: Activation (guided onboarding — targeting GA end of Q2, high confidence; in-app checklist — Q2, medium), Retention (usage insights dashboard — Q3, medium), and an AI setup assistant we've only prototyped (no date). Audience is the exec team; decision is headcount approval."
expected:
  - "States the audience (exec team) and the single decision it drives (approve two engineers for activation) up top"
  - "Leads with a headline (<= 2 sentences) at outcome altitude — activation as the lever, not a feature list"
  - "Presents an explicit commitments-vs-directional split: guided onboarding (Q2, high) and checklist (Q2, med) as committed with confidence levels; the AI setup assistant as directional with no date"
  - "Frames the message hierarchy in exec terms (outcomes, trade-offs, the headcount ask) rather than dumping every item"
  - "Includes an FAQ that pre-empts a hard question, e.g. why the AI assistant is not dated"
rubric:
  audience_framing: 0.30
  commitment_discipline: 0.30
  completeness: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a well-specified roadmap plus a named audience and clear intent.
Guards that the skill produces an audience-framed brief with a real
commitments/directional split and confidence levels, not a flattened dump.
