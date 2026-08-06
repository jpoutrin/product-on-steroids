---
id: cohort-analysis-adversarial
skill: cohort-analysis
input:
  prompt: "Analyze our retention and tell us why users are churning."
  context: "<no data provided; no metric definition; no cohort specification; no time period>"
expected:
  - "Asks clarifying questions before attempting analysis (data format, cohort definition, retention metric)"
  - "Defines cohort scope: 'Do you mean weekly, monthly, or event-based cohorts?'"
  - "Specifies retention metric: 'What constitutes an active user? Any login, or 5+ events/week?'"
  - "Requests data or a summary table (cohort size, retention %, time periods)"
  - "Does NOT fabricate findings or recommend actions based on guessed data"
  - "Briefly explains why each clarification is load-bearing for analysis quality"
rubric:
  correctness: 0.5
  asks_right_questions: 0.35
  avoids_fabrication: 0.15
weight: 1.0
---

Adversarial: vague ask with no data or context. Skill must identify gaps and ask
clarifying questions rather than proceeding blindly. Guards against false confidence
and wasted analysis on under-specified problems. Tests graceful degradation when the
user's request is incomplete.
