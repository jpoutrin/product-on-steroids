---
id: problem-statement-edge
skill: problem-statement
input:
  prompt: "Help me write a problem statement for a mobile banking app."
  context: >
    The PM is early in discovery. They have observed anecdotally that users
    complain about the onboarding flow in app store reviews, but have no
    interview data, no funnel metrics, and no support ticket counts. User
    segment is 'new users trying to open a first account on mobile'. The PM
    wants a problem statement to share with leadership next week to get buy-in
    for a discovery sprint.
expected:
  - "Produces a problem statement that frames the problem without inventing evidence the PM did not provide"
  - "Flags the output as hypothesis-grade (e.g., '⚠ Hypothesis — validate' or equivalent language)"
  - "Lists app store reviews as the only evidence source, accurately reflecting what was given"
  - "Does not fabricate metrics, percentages, or interview findings not present in the input"
  - "Impact section states the impact direction and explicitly calls out that quantification is needed"
  - "Out of Scope contains at least 2 relevant exclusion bullets"
rubric:
  evidence_honesty: 0.40
  correctness: 0.30
  completeness: 0.20
  format: 0.10
weight: 1.0
---

Edge case: thin evidence scenario. The PM has only anecdotal signals and no
quantitative data. Guards against the skill inventing plausible-sounding metrics
or omitting the hypothesis flag — both of which would give stakeholders false
confidence and lead to poorly grounded investment decisions.
