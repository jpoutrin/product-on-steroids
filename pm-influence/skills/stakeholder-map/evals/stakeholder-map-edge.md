---
id: stakeholder-map-edge
skill: stakeholder-map
input:
  prompt: "Map stakeholders for our platform API migration — we're deprecating v1 and forcing partners to v2."
  context: "Three external partners integrate with our API and have contractual SLAs. One partner (Acme Corp) is our largest revenue source but is not on our org chart and has no formal internal sponsor. Internal: CTO (owns the decision), two backend engineers (do the work), Head of Partnerships (manages partner relationships), Legal (contract review). Timeline: 6 months."
expected:
  - "Correctly identifies Acme Corp as a high-power external stakeholder despite not appearing on the internal org chart"
  - "Places Acme Corp in Manage Closely or Keep Satisfied (not Monitor) given their revenue impact"
  - "Treats external partners as stakeholders with real influence, not just passive consumers"
  - "Head of Partnerships is in Manage Closely due to being the bridge to external power"
  - "Conflict risk between CTO's deprecation timeline and partners' contractual SLA obligations is surfaced"
  - "Engagement strategy accounts for external communication channels (e.g., partner portal, account manager calls) not just internal tools"
rubric:
  correctness: 0.40
  external_stakeholder_handling: 0.25
  conflict_identification: 0.20
  actionability: 0.15
weight: 1.0
---

Edge case: external stakeholder with high power but no internal org-chart presence.
Guards against the failure of defaulting all external parties to Monitor, and
against missing conflict risks between internal timelines and contractual obligations.
