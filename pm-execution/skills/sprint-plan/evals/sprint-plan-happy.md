---
id: sprint-plan-happy
skill: sprint-plan
input:
  prompt: "Plan the sprint for our team starting Monday."
  context: "5-person team, 2-week sprint. Historical velocity: ~30 points/sprint. 1 person in meetings 30% of time. Backlog is groomed and estimated. No external dependencies flagged yet."
expected:
  - "Sprint goal is a single, clear sentence describing success."
  - "Team capacity is calculated: team size × duration, adjusted for availability, with historical velocity referenced."
  - "A 15–20% buffer is reserved and its size is justified."
  - "Committed stories total ≤ available capacity (respects the buffer)."
  - "Each story has story points, an owner, and dependencies noted (or 'none')."
  - "Every risk identified includes a specific mitigation (escalate, pair, swap story, reduce scope)."
  - "Definition of Ready is verified (AC clear, estimated, no blockers) for each committed story."
rubric:
  correctness: 0.35
  completeness: 0.3
  capacity_reasoning: 0.2
  actionability: 0.15
weight: 1.0
---

Well-groomed backlog, clear velocity history, no external blockers. Guards against skipped capacity math and unmitigated risks.

