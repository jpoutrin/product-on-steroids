---
id: roadmap-planning-happy
skill: roadmap-planning
input:
  prompt: "Plan our Q3 roadmap across our three strategic themes."
  context: >
    Themes: Activation, Retention, Platform-debt. 5 squads, 12-week quarter.
    Known: ~25% of capacity goes to KTLO/on-call, one squad has 3 weeks of leave.
    SSO migration must land before the new onboarding flow can start.
expected:
  - "Names both a planning period and a review interval (explicit cadence)"
  - "Derives available capacity by subtracting KTLO/on-call/leave from raw squad-weeks, not 100% of headcount"
  - "Allocates capacity across the three themes in a table that sums to available capacity, each theme tied to an objective"
  - "Sequences SSO migration before the onboarding flow and states the dependency as the reason"
  - "Schedules risk-heavy/blocking work early to de-risk, with owner and needed-by on dependencies"
  - "Defines a review rhythm with checkpoints, attendees, and off-cycle replan triggers"
rubric:
  correctness: 0.35
  completeness: 0.25
  sequencing_rationale: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: enough themes, capacity, and a real dependency chain to run the full
planning process. Guards against planning against raw headcount, arbitrary
ordering, and a plan with no review rhythm.
