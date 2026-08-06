---
id: decision-memo-happy
skill: decision-memo
input:
  prompt: "Write a decision memo for our VP of Product on whether to move our growth tier to usage-based pricing."
  context: >
    We currently charge $49/mo flat for the growth tier. Cohort analysis shows
    power users (top 20%) generate 8x the API calls of median users. Three
    enterprise deals stalled last quarter because of pricing optics. Options are:
    (A) keep flat pricing, (B) move to usage-based with a $20 base + $0.005/call,
    (C) introduce a hybrid $29 base + $0.003/call above 10k calls. VP of Product
    is Sarah Chen. We need a decision by June 20 because engineering kicks off
    Q3 billing work on June 23.
expected:
  - "States the decision as a specific question (flat vs usage-based pricing for the growth tier), not a vague topic"
  - "Presents all three options (A, B, C) each with an explicit benefit and an explicit cost or risk"
  - "Makes a clear recommendation for one option, not a call to 'discuss further'"
  - "Names Sarah Chen as the decision owner with the June 20 deadline"
  - "Explains the cost of deferral (engineering kickoff June 23)"
  - "Identifies the critical assumption that would change the recommendation"
  - "Stays within approximately one page with no jargon"
rubric:
  correctness: 0.30
  completeness: 0.25
  recommendation_clarity: 0.25
  actionability: 0.20
weight: 1.0
---

Happy path: well-specified decision with a named owner, a hard deadline, three
real options, and supporting data. Guards against the memo hedging instead of
recommending, missing the deferral-cost signal, or presenting options as equally
valid when the data already favors one.
