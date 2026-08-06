---
id: wwas-adversarial
skill: wwas
input:
  prompt: "Build us a shipping doc for Q3."
  context: ""
expected:
  - "Skill asks clarifying questions rather than guessing scope: which sprint(s) in Q3? Which product/team? What features/work items?"
  - "Skill declines to fill template with vague data; instead structures questions around shipping period, feature list, and stakeholders"
  - "If a partial answer is provided, skill acknowledges gaps and flags what's missing before drafting (e.g., 'I need links to designs/PRDs to make this traceable')"
  - "Skill suggests a follow-up with `create-prd` or `job-stories` if the user is trying to spec features rather than commit to shipping"
rubric:
  clarification_quality: 0.4
  scope_enforcement: 0.35
  handoff_recognition: 0.25
weight: 1.0
---

Vague input without enough context to build a real shipping doc.
Guards against garbage-in-garbage-out; skill must scope down, ask clarifying
questions, and refuse to fill the template with unsupported placeholders.
