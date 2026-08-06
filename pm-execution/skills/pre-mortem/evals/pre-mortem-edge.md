---
id: pre-mortem-edge
skill: pre-mortem
input:
  prompt: "Quick pre-mortem: We're about to do a feature rollout to 10% of production (dark launch). No formal PRD — just a one-pager and Slack conversations. Launch window is this week."
  context: "Engineering says feature is 'feature-complete' but there are known edge cases. No performance testing at scale. Customer success hasn't been briefed yet. Minimal monitoring setup."
expected:
  - "Acknowledges incomplete context (missing formal PRD, no testing data) and asks clarifying questions rather than inventing risks"
  - "Identifies risks that are concrete despite sparse information (e.g., lack of performance baseline, CS unaware of feature behavior)"
  - "Flags at least one Elephant around monitoring/observability assumptions"
  - "Distinguishes between 'we don't know' (Elephant) and 'we know this is risky' (Tiger)"
  - "Provides actionable mitigations even with compressed timeline"
rubric:
  context_awareness: 0.3
  risk_clarity: 0.25
  uncertainty_handling: 0.25
  timeline_realism: 0.2
weight: 1.0
---

Edge case: sparse input, compressed timeline, incomplete information. Skill must navigate between asking for clarity and making risk calls with what's available. Guards against over-confident analysis when context is thin, and against false confidence in "edge cases."
