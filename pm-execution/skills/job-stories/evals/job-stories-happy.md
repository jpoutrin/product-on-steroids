---
id: job-stories-happy
skill: job-stories
input:
  prompt: "Create job stories for a mobile expense tracker app. Users want to track daily spending and stay within budget limits."
  context: "Feature: weekly budget alerts. Design mockup available in Figma. Target: personal finance users aged 20–35."
expected:
  - "Generates 3–5 distinct job stories in JTBD format"
  - "Each job story has a clear, specific situation (triggering context, not generic persona)"
  - "Motivations are actionable and specific, not vague"
  - "Outcomes are measurable and observable"
  - "Each job story includes 5–8 testable, outcome-focused acceptance criteria"
  - "Design link is present and points to actual mockup"
  - "Acceptance criteria focus on outcome validation, not implementation details"
rubric:
  jtbd_adherence: 0.3
  outcome_clarity: 0.3
  acceptance_criteria_quality: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: well-scoped feature with clear user situations and desired outcomes.
Guards against vague feature descriptions and persona-centric (not situation-centric) stories.
