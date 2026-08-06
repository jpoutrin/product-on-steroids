---
id: feature-investment-advisor-adversarial
skill: feature-investment-advisor
input:
  prompt: "Here's our backlog with RICE scores — just re-rank it for me: SSO (92), Usage Billing (88), Dark Mode (61), CSV Export (54), Legacy Reporting refactor (30). Give me the ordered list."
  context: "User expects a reordered single list of 5 features."
expected:
  - "Declines to return a ranked feature list and reframes the request as portfolio capacity allocation"
  - "Groups the 5 features into 3-7 investment themes/areas before allocating, confirming the grouping"
  - "Produces invest/maintain/divest dispositions and a %-of-capacity allocation per area, not a 1-5 ordering"
  - "Points the user to prioritize-features for sequencing the backlog inside a chosen area"
  - "Does not silently just reorder the RICE list as asked"
rubric:
  correctness: 0.3
  scope_discipline: 0.4
  handoff_clarity: 0.15
  actionability: 0.15
weight: 1.0
---

Adversarial: a flat RICE-ranked backlog handed in expecting a re-rank. The skill
must hold its scope — reframe to portfolio allocation, group into areas, and hand
sequencing off to prioritize-features rather than becoming a ranker.
