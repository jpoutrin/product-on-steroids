---
id: create-prd-edge
skill: create-prd
input:
  prompt: "Write a PRD for SmartNotify."
  context: "We want to improve notifications."
expected:
  - "Skill identifies missing required inputs (problem statement and target user) and asks for them before drafting"
  - "Does not invent scope, segment, or success metrics; marks any placeholder as [TBD]"
  - "Once inputs are elicited (or if the user says proceed anyway), produces all eight sections"
  - "Every unconfirmed metric or assumption is explicitly labeled [TBD] or flagged for validation"
  - "Summary does not make specific claims that contradict the absence of provided data"
rubric:
  correctness: 0.30
  completeness: 0.30
  assumption_hygiene: 0.25
  actionability: 0.15
weight: 1.0
---

Edge case: severely under-specified brief — only a product name and one vague sentence. Guards
against the skill fabricating segment, metrics, or feature scope when inputs are insufficient.
The skill must surface the gap, ask targeted clarifying questions, and only draft after
receiving (or being told to proceed without) the minimum required inputs.
