---
id: sprint-plan-adversarial
skill: sprint-plan
input:
  prompt: "We need a sprint plan NOW. What stories should we do?"
  context: "Team: unclear size and availability. Backlog: mostly unestimated, no AC, 2 stories blocked by 'engineering review'. No velocity data. Multiple departments want different priorities. External: payment provider upgrade must land this sprint but timeline is TBD. CEO wants 'more features.'"
expected:
  - "Skill acknowledges missing Definition of Ready and **asks for the required inputs** (team roster + availability, story estimates, blockers, priorities)."
  - "Does not guess capacity or commit stories without reasoning (refuses empty / round-number commits)."
  - "Flags blocked stories as unplannable until blockers are resolved."
  - "Escalates the external payment provider upgrade as a critical dependency — makes it explicit that the sprint cannot finalize until the timeline is locked."
  - "Asks for a single sprint goal if priorities conflict; does not try to do everything."
  - "Does not produce a full plan in this case — instead produces a **pre-plan checklist** (team size, story estimates, blocker resolution, priority alignment) that must be complete before sprint kickoff."
rubric:
  correctness: 0.25
  risk_identification: 0.25
  when_to_refuse: 0.3
  actionability: 0.2
weight: 1.0
---

Vague ask, missing inputs (team, estimates, blockers, priorities), conflicting signals, external blocker with unknown timeline. Guards against committing a sprint plan on incomplete information or false confidence in unresolved risks.

