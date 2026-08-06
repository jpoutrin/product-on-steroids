---
id: ideal-customer-profile-happy
skill: ideal-customer-profile
input:
  prompt: "Define our ICP. We sell a workflow-automation SaaS for RevOps teams."
  context: |
    Existing data available:
    - 120 paying customers, Q1 2025 win/loss analysis (42 closed-won, 18 churned).
    - Best-performing cohort by LTV and expansion: Series A–C B2B SaaS companies,
      50–300 employees, US-based, with a VP of RevOps or equivalent.
    - Churned accounts: mostly < 30 employees (no dedicated RevOps function) and
      companies > 500 employees (required on-prem deployment we can't support).
    - Average sales cycle 5 weeks; champion is always RevOps lead, approver is CFO
      or CRO.
    - Top trigger events from win data: recent CRM migration, new VP RevOps hired
      in last 90 days, just closed Series A.
    - Pricing: $2K–$8K/month. Sales motion: inside sales, demo-driven.
expected:
  - "ICP Summary names a specific segment — not just 'mid-market B2B SaaS'"
  - "Firmographic table includes company size range anchored to the 50–300 employee pattern from win data"
  - "Trigger events section lists at least two of the three top triggers from the win data (CRM migration, new VP RevOps, Series A)"
  - "Buying process identifies the champion (RevOps lead) and economic buyer (CFO or CRO) as distinct roles"
  - "Negative ICP explicitly disqualifies companies < 30 employees and > 500 employees with stated rationale"
  - "Every criterion is tagged with a confidence level (validated, hypothesis, or assumption)"
  - "Evidence & Validation Notes cites the win/loss analysis and churn cohort as sources"
rubric:
  correctness: 0.40
  completeness: 0.30
  actionability: 0.30
weight: 1.0
---

Happy path: sufficient win/loss and churn data to produce a fully data-backed
ICP. Guards against vague segment labels, missing disqualification criteria, and
untagged confidence levels. Verifies that the skill draws distinct roles in the
buying process rather than collapsing them.
