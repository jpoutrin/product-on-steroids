---
id: stakeholder-map-happy
skill: stakeholder-map
input:
  prompt: "Create a stakeholder map for our new in-app analytics dashboard feature."
  context: "B2B SaaS product team, ~40-person company. Known stakeholders: VP Product (sponsor), Head of Engineering (builds it), 3 enterprise customers (pilot users), Head of Sales (will use it in demos), Legal (data privacy review), Customer Success (onboarding). Feature ships in Q3."
expected:
  - "Places every named stakeholder in a Power × Interest quadrant with a rationale"
  - "VP Product and Head of Engineering are in Manage Closely (High Power, High Interest)"
  - "Legal appears in Keep Satisfied (High Power, Low Interest) or Manage Closely with appropriate rationale"
  - "Enterprise customers and Customer Success appear in Keep Informed (Low Power, High Interest)"
  - "Communication plan table has one row per stakeholder with frequency, channel, and key message"
  - "At least one conflict risk is identified (e.g., Sales wanting demo-ready polish vs. Engineering shipping MVP)"
rubric:
  correctness: 0.35
  completeness: 0.30
  actionability: 0.25
  conflict_identification: 0.10
weight: 1.0
---

Happy path: well-scoped initiative with a concrete stakeholder list and clear
power/interest signals. Guards against incomplete quadrant placement, missing
communication plan rows, and failure to surface obvious conflicts.
