---
id: lean-ux-canvas-happy
skill: lean-ux-canvas
input:
  prompt: >
    We're kicking off a sprint to improve onboarding for new B2B users of our
    project-management SaaS. Retention at Day 7 is 28% and we need to get it
    to 40%. The team includes design, engineering, and customer success. Help us
    fill in the Lean UX Canvas for this initiative.
  context: >
    Cross-functional team (PM, designer, 2 engineers, CS rep). They have user
    interview notes showing that new users struggle to connect their first
    project within the first session. Business OKR: increase 7-day retention
    to 40% this quarter.
expected:
  - Block 1 states the onboarding drop-off as a business problem, not as a feature request
  - Block 2 includes Day-7 retention (28% → 40%) as a measurable behavioral outcome
  - Block 3 identifies specific user types (e.g., "new B2B admin" or "first-time team lead"), not "users" in general
  - Block 4 expresses user goals as jobs-to-be-done (e.g., "get the team running on their first project"), not feature names
  - Block 5 lists at least 2 distinct solution ideas spanning different approaches
  - Block 6 contains at least 2 falsifiable hypothesis statements in the canonical "We believe / We'll know" form with measurable signals
  - Block 7 names a single riskiest assumption as a question (not a list)
  - Block 8 proposes a concrete, time-boxed experiment (e.g., "5 moderated user interviews in 3 days")
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy-path scenario: a well-resourced cross-functional team with clear business
context and a real OKR. Guards against the skill producing vague block content
(feature lists instead of hypotheses, generic "users" instead of named types,
missing experiment time-box). The canvas should be fully actionable — a team
could walk out of the session and run the experiment in Block 8 the next day.
