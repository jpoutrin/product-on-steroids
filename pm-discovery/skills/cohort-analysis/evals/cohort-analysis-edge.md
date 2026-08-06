---
id: cohort-analysis-edge
skill: cohort-analysis
input:
  prompt: "We have weekly user cohorts with incomplete data. Week 1 has 3 cohorts, but only 2 have Week 4 data. Multiple metrics: DAU, feature adoption %, churn rate. What patterns do you see?"
  context: "Data is sparse and unevenly populated. Cohort sizes range 50–200 users (small). Jan onboarding redesign happened mid-week. No other context provided."
expected:
  - "Acknowledges data limitations (incomplete weeks, small cohort size) and flags confidence constraints"
  - "Prioritizes metrics (e.g., focus on retention %; flag adoption % as secondary due to sparse data)"
  - "Makes quantified findings from available data without guessing missing periods"
  - "Recommends data-collection improvements (e.g., 'fill in missing Week 4 for early cohorts')"
  - "Qualitative research design accounts for small sample size (e.g., 'interview all 15 churned Jan users')"
  - "Patterns are hedged: 'likely driver' or 'hypothesis requiring validation' rather than stated fact"
rubric:
  correctness: 0.3
  completeness: 0.25
  data_honesty: 0.3
  actionability: 0.15
weight: 1.0
---

Edge case: sparse, incomplete data with small cohorts and minimal context. Guards
against false confidence in incomplete data. Tests the skill's ability to work within
constraints, flag limitations, and suggest better data collection without fabricating
findings.
