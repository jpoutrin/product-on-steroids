---
id: alignment-narrative-edge
skill: alignment-narrative
input:
  prompt: "Write an alignment narrative to get the leadership team behind refactoring our data pipeline before we build any new features."
  context: |
    Product: internal analytics platform for a mid-size e-commerce company.
    Situation: the PM knows the pipeline is slow and unreliable but has no
    single dramatic incident — just ongoing low-grade pain (reports take 4-8
    hours to refresh, two minor data errors in the past 90 days that were
    caught before reaching customers). No competing product. Audience: VP
    Product and VP Engineering, both focused on new feature delivery. The PM
    has no NPS or revenue data directly tied to pipeline failures. Internal
    teams have different opinions on severity; data engineering says "urgent,"
    product says "manageable."
expected:
  - "Acknowledges that evidence is thin upfront rather than overstating urgency"
  - "Constructs the Complication from available signals (refresh time, two data errors, internal disagreement) without fabricating a crisis"
  - "Key Question addresses the tradeoff the audience actually cares about: new features vs. foundation stability"
  - "Strategic Direction makes the case for refactoring first with explicit reasoning, not just asserting it is necessary"
  - "Flags the internal disagreement and resolves it rather than papering over it"
  - "Does not invent evidence or fabricate a dramatic Complication the PM did not supply"
rubric:
  scqa_structure: 0.30
  evidence_honesty: 0.30
  audience_tuning: 0.25
  call_to_action_concreteness: 0.15
weight: 1.0
---

Edge case: sparse dramatic evidence and internal team disagreement on severity.
Guards against two failure modes: (1) fabricating a crisis to manufacture
urgency, and (2) refusing to write the narrative because the evidence is thin.
The skill should use the available signals honestly and construct an argument
from them.
