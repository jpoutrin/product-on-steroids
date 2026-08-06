---
id: user-segmentation-edge
skill: user-segmentation
scenario: >
  Sparse or skewed feedback (mostly support tickets, limited interviews, no usage logs).
  Skill must work with limited data, flag confidence gaps clearly, and avoid over-extrapolating.
input:
  prompt: >
    We're an early-stage B2C mobile productivity app with 50K users. I have 200 support
    tickets from the last 3 months and 8 user interviews. Can you segment our user base?
  context: >
    Support tickets are skewed toward churned/frustrated users. Interviews are 8 power users
    (recruited from engaged user cohort). No usage telemetry or survey data available.
    Product focus: task management and habit tracking.
expected:
  - Output identifies 2–3 segments despite data limitation; does not over-segment or hallucinate.
  - Confidence levels are explicit; segments from support tickets are flagged as "potentially survival bias" or "churn-skewed".
  - Segments from interviews are marked "high engagement bias" or "not representative of casual users".
  - Skill acknowledges missing data sources (e.g., "no usage telemetry, no survey of inactive users").
  - Recommendations are conservative; does not recommend heavy investment in segments with thin data.
  - Validation notes clearly state "next steps to reduce confidence gaps" (e.g., "survey 200 casual users", "analyze usage logs for day-1–day-30 cohort").
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

**Why this scenario exists:**
This guards against false confidence. Early-stage products or those with incomplete data often
lack rich feedback. The skill must segment with integrity despite limitations—identifying
patterns where they exist, flagging bias and gaps prominently, and resisting the urge to
over-interpret thin data. Measures whether the skill prioritizes honest confidence levels and
clear caveats over an illusion of completeness.
