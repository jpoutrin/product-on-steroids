---
id: stakeholder-identification-edge
skill: stakeholder-identification
input:
  prompt: "Who are the stakeholders for our internal data-platform migration — we are moving from an on-prem Hadoop cluster to a cloud-based data lakehouse."
  context: "Company: 1,200-person enterprise, financial services sector. Migration is internal-only; no customer-facing impact. Timeline: 12 months. Involves sensitive financial and PII data."
expected:
  - "Correctly omits or minimizes external customer-facing stakeholders (Sales, Customer Success) with explanation that this is internal-only"
  - "Identifies Security and CISO as gatekeepers given financial services sector and PII data"
  - "Identifies Data Protection Officer or equivalent privacy role given PII data handling"
  - "Identifies Finance / Procurement for cloud spend approval — cloud migrations have material budget implications"
  - "Identifies downstream data consumers (Analytics, BI teams, data scientists) as affected parties whose workflows are disrupted"
  - "Identifies IT / Infra and Platform Engineering as core contributors, not just a single 'Engineering' catch-all"
  - "Non-Obvious Stakeholders callout surfaces the regulatory/compliance angle specific to financial services"
  - "Gaps & Uncertainties asks whether a Steering Committee or Change Advisory Board approval is required"
rubric:
  completeness: 0.30
  non_obvious_coverage: 0.30
  scope_discipline: 0.25
  role_specificity: 0.15
weight: 1.0
---

Edge case: an internal-only initiative in a regulated industry. Guards against
two opposite failure modes — (1) including all customer-facing roles by default
without considering that this is an internal migration, and (2) missing the
compliance, security, and data-governance stakeholders that a financial services
context demands. The regulated-sector filter in the Process must fire.
