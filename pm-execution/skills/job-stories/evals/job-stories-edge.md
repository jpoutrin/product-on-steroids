---
id: job-stories-edge
skill: job-stories
input:
  prompt: "Break this into job stories: we need expense categorization in our app."
  context: "Minimal details. No design mockup. No user research data. No segment info."
expected:
  - "Skill asks clarifying questions about user situations and triggering contexts before generating stories"
  - "Skill asks about outcomes and what success looks like"
  - "Skill requests design mockup link or explains why it's needed"
  - "Generated stories have situation and outcome clarity despite sparse input"
  - "Stories avoid assumptions about personas; focus on job contexts"
  - "Acceptance criteria remain testable and outcome-focused despite sparse context"
rubric:
  clarifying_questions: 0.35
  situation_outcome_clarity: 0.35
  assumption_handling: 0.2
  acceptance_criteria_quality: 0.1
weight: 0.8
---

Edge case: sparse input requiring the skill to ask clarifying questions about situations,
contexts, and outcomes before generating stories. Guards against machine-generated stories
with unmeasurable outcomes and generic motivations.
