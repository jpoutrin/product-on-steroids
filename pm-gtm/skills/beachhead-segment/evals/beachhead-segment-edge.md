---
id: beachhead-segment-edge
skill: beachhead-segment
input:
  prompt: "Which beachhead segment should we go after first?"
  context: |
    Product: async video messaging tool for remote teams, replacing internal
    meeting-heavy cultures. Works on web and mobile.
    Candidate segments after initial discovery interviews:
    (A) Remote-first product teams at startups (10-50 people, US), pain score 4/5,
    WTP medium, referral high — but highly competitive (Loom already dominant).
    (B) Customer success teams at mid-market SaaS (50-300 employees, US), pain
    score 4/5, WTP medium-high, referral medium — Loom present but not deeply
    adopted; CS workflows differ from dev workflows.
    (C) L&D / training teams at mid-market companies, pain score 3/5, WTP
    medium, referral low — less competitive but problem less acute.
    No existing paying customers. Founders come from a CS background.
expected:
  - "Applies a tie-breaking framework when segments appear equal on the four
    criteria — does not pick arbitrarily"
  - "Explicitly disqualifies or deprioritizes segment A due to Loom's dominance
    making it non-winnable without a clear differentiation lever"
  - "Recommends segment B with a rationale grounded in the founders' CS background
    as a distribution and credibility advantage"
  - "Acknowledges uncertainty (no paying customers) and recommends validation steps"
  - "States measurable win criteria for the recommended segment"
  - "Identifies the next bowling-pin segment from the recommended beachhead"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge case: two segments score nearly identically on the standard four criteria.
The skill must surface a tie-breaking lens (here: competitive winnability rules out
A; founders' domain advantage breaks the tie toward B) rather than producing an
arbitrary or wishy-washy recommendation. Guards against "it depends" non-answers
and against recommending the most famous segment (product teams) without checking
competitive winnability.
