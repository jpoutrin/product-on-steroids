---
id: value-proposition-happy
skill: value-proposition
input:
  prompt: "Design a value proposition for our async video tool, targeting remote engineering managers. We interviewed 8 of them."
  context: "Segment named. Interview notes: managers hate status-meeting overload (7/8), want to unblock reports without a call (6/8), fear losing visibility if meetings shrink (5/8). Product: record-and-share Loom-style clips with threaded replies and auto-transcripts. Alternatives today: Zoom, Slack huddles, written updates."
expected:
  - "Scopes the canvas to the single named segment (remote engineering managers), not 'everyone'"
  - "Separates jobs, pains, and gains and ranks the top items by importance to the customer"
  - "Tags each pain and gain as evidence or assumption, using the interview counts as evidence"
  - "Each pain reliever names the ranked pain it maps to, and each gain creator names the ranked gain"
  - "Fit Analysis flags any uncovered top pain/gain and any orphan reliever/creator, and names alternatives (Zoom/Slack/written updates) with a switching reason"
  - "Ends with a 1-2 sentence value-proposition statement in the For/who/our/unlike shape"
rubric:
  fit_mapping: 0.35
  profile_quality: 0.25
  evidence_tagging: 0.20
  statement_quality: 0.20
weight: 1.0
---

Happy path: a named segment with real interview evidence, enough to build a full
canvas with evidence-backed jobs/pains/gains, explicit reliever/creator mapping,
and a fit analysis. Guards against merged profiles, unmapped features, and a
generic statement.
