---
id: stakeholder-identification-happy
skill: stakeholder-identification
input:
  prompt: "Identify all stakeholders for a B2B SaaS pricing change — we are moving from per-seat to usage-based pricing for our project-management tool."
  context: "Company: ~200-person SaaS startup. B2B, mid-market focus. Change affects existing contracts, billing infrastructure, and customer communications. Launching in 3 months."
expected:
  - "Inventory includes individual roles, not catch-all groups like 'leadership'"
  - "Each row includes a one-line rationale for inclusion"
  - "Each stakeholder is assigned exactly one category (sponsor, decision-maker, contributor, affected party, gatekeeper, external)"
  - "Non-obvious rings are covered: Finance/FP&A flagged for revenue-recognition implications, Legal for contract amendment requirements, Customer Success for customer communications and churn risk"
  - "Non-Obvious Stakeholders callout contains at least 3 distinct entries with clear rationale"
  - "Gaps & Uncertainties section contains at least one open question"
  - "Billing/infrastructure engineering is identified as a contributor, not just product and front-end"
rubric:
  completeness: 0.35
  non_obvious_coverage: 0.30
  role_specificity: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: a concrete pricing-change initiative with enough context to produce
a thorough inventory. Guards against inventories that list only the core product
and engineering team while missing legal, finance, CS, and billing infrastructure
owners. The non-obvious rings are what distinguishes a shallow list from a
decision-ready one.
