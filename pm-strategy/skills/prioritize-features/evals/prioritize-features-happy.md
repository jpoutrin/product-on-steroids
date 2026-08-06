---
id: prioritize-features-happy
skill: prioritize-features
input:
  prompt: "Prioritize our Q3 backlog to move activation rate: guided onboarding, SSO, in-app checklist, dashboard redesign, referral program, CSV import."
  context: "Objective: lift new-user activation. Reach data available per feature (users/quarter). Effort estimates in person-weeks exist. Team wants a top 5 with rationale."
expected:
  - "States the objective (activation rate) and the framework (RICE) with its per-factor scale up front"
  - "Scores every one of the six candidates as a row with visible Reach, Impact, Confidence, Effort and a computed RICE score"
  - "Ranks by score descending and recommends a top 5, each with a one-line rationale naming the deciding factor and trade-off"
  - "Lists the deprioritized item(s) with a one-line reason"
  - "Flags any low-confidence Impact/Reach score with a validation step"
rubric:
  correctness: 0.35
  completeness: 0.25
  actionability: 0.25
  assumptions_explicit: 0.15
weight: 1.0
---

Happy path: clear objective plus reach and effort data, so RICE applies cleanly.
Guards against ranking without a visible scoring table or an unexplained top 5.
