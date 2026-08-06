---
id: problem-statement-happy
skill: problem-statement
input:
  prompt: "Write a problem statement for our B2B SaaS product."
  context: >
    Product: a project-management tool used by software engineering teams at
    mid-market companies (50-500 employees). The PM has the following research:
    user interviews (n=14) show that engineering leads spend 30-45 min per week
    manually cross-referencing sprint boards with Slack messages to track
    unresolved dependencies. 3 out of 5 retrospectives in the last quarter
    surfaced 'dependency visibility' as a top friction point. Analytics show
    that 68% of blocked tickets sit unresolved for more than 2 days before an
    owner is pinged. Churn analysis flags 2 accounts lost in Q3 citing
    'visibility gaps'. Target segment: engineering leads at mid-market B2B SaaS
    companies. Goal: reduce cross-team coordination overhead.
expected:
  - "Core statement names engineering leads as the user segment"
  - "Core statement describes the problem without prescribing a feature or solution"
  - "Core statement is falsifiable — a reader could in principle disprove it"
  - "Evidence section lists at least 3 bullets and each names its source type (interview, analytics, churn analysis, etc.)"
  - "Impact section includes at least one quantitative signal (time cost, churn, or ticket-resolution delay)"
  - "Out of Scope contains at least 2 bullets excluding adjacent problems"
  - "No solution language appears in the Problem Statement section"
rubric:
  correctness: 0.35
  completeness: 0.30
  no_solution_language: 0.20
  format: 0.15
weight: 1.0
---

Happy path: a well-specified problem with a clear user segment, multiple evidence
sources, and quantitative signals. Guards against solution-first framing,
missing evidence attribution, and vague impact statements.
