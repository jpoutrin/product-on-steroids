---
id: problem-framing-canvas-edge
skill: problem-framing-canvas
input:
  prompt: >
    We need a Problem Framing Canvas for our onboarding flow. Half the team
    thinks the drop-off at step 3 is a real problem; the other half says users
    who drop off just weren't a good fit and we shouldn't try to retain them.
    We have: 52% completion rate for onboarding (steps 1–5), internal target
    was 70%. No qualitative research yet. Engineering says step 3 is a complex
    form. Marketing says the segment reaching step 3 is already qualified.
  context: >
    B2B SaaS product. PM, engineering lead, and marketing lead are the three
    stakeholders. No user interviews on this topic yet. The team has been
    arguing for two weeks without resolution.
expected:
  - The Evidence block explicitly flags that qualitative research is missing and names specific research activities needed (e.g., user interviews, session recordings).
  - The Open Questions block captures the team's core disagreement — "Is the step-3 drop-off a fit problem or a usability problem?" — as an explicit question with a research activity.
  - The canvas does not take sides or resolve the disagreement by fiat; it frames it as an unresolved question.
  - The Problem block acknowledges the ambiguity rather than asserting a single cause.
  - The canvas is still substantively filled across all nine blocks — the disagreement does not produce an empty or skeletal output.
rubric:
  correctness: 0.35
  completeness: 0.35
  actionability: 0.30
weight: 1.0
---

Edge-case guard. Validates that the skill handles team disagreement about
whether a problem is real by surfacing the disagreement as Open Questions
rather than silently resolving it or refusing to produce a canvas. Ensures
the skill does not fabricate evidence or take sides, while still producing a
useful artifact that the team can use to prioritize research to resolve the
disagreement. Prevents both false certainty and an empty output.
