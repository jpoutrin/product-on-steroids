---
id: incoming-request-advisor-adversarial
skill: incoming-request-advisor
input:
  prompt: "A stakeholder keeps asking for the same dashboard feature. I've already
    said no twice but they won't let it go. Can you help me handle this?"
  context: "No strategy summary provided. PM has not explained why they declined
    the previous two times. The stakeholder's seniority and relationship are
    not described."
expected:
  - "Skill asks for missing required inputs before producing a disposition — strategy context and stakeholder identity are mandatory"
  - "Skill does not produce a draft reply without knowing the strategic rationale for prior declines"
  - "Skill surfaces the avoidance risk: saying no repeatedly without explanation erodes trust"
  - "Once clarifying inputs are provided (in follow-up), the skill produces a disposition grounded in strategy, not fatigue"
  - "Draft reply (after clarification) does not repeat 'no' without offering a concrete resolution path"
rubric:
  correctness: 0.35
  elicitation_quality: 0.30
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: under-specified ask plus a PM who may be avoiding the conversation
rather than navigating it. Tests two traps: (1) producing a response plan without
required inputs, and (2) validating repeated declines without examining whether
the PM's reasoning is actually sound. The skill must pause, elicit, and then
surface the relational risk of serial refusals.
