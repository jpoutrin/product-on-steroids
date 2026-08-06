---
id: wwas-happy
skill: wwas
input:
  prompt: "Create a shipping doc for our Q3 sprint 2 release."
  context: "We're shipping three features: real-time spending tracker (Figma link: https://figma.com/design/abc123), budget alerts (GitHub issue #567), and expense categories (PRD link). Sprint runs Aug 1–14. Team: 4 engineers + 1 designer. Main users: mobile app users in US/EU. Dependencies: none known. Stakeholders: support, marketing, design."
expected:
  - "Clearly lists each feature in-scope with a 1–2 sentence description and a link to design/spec"
  - "Includes out-of-scope section with at least one deferred feature and a reason (e.g., timeline, priority)"
  - "Defines acceptance criteria with concrete, testable items (e.g., 'code merged', 'deployed to production', 'support briefed')"
  - "Maps dependencies (or explicitly states none) with owner and risk/mitigation"
  - "Stakeholder checklist includes design, support, and marketing with clear owners"
  - "Shipping period is clearly stated with dates and teams involved"
  - "Document is self-contained and traceable to sources (GitHub, Figma, PRD)"
rubric:
  clarity: 0.3
  completeness: 0.35
  traceability: 0.25
  actionability: 0.1
weight: 1.0
---

Standard sprint with clear inputs, multiple features, and known stakeholders.
Guards against vague scope and missing traceability (links, owners).
