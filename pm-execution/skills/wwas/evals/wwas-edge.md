---
id: wwas-edge
skill: wwas
input:
  prompt: "We need a shipping doc for the major release in 3 weeks. There are lots of moving pieces."
  context: "Release has 6 features across three teams (backend, mobile, web). Two are dependent on a third-party API integration not yet confirmed. Support/marketing timeline is tight—release announcement needs to go live day-of. We have 3 PRDs, 5 GitHub issues, and 1 Figma file. Legal review needed. One known nice-to-have (dark mode) we're deferring."
expected:
  - "Clearly separates in-scope features (6 items, each with link and short desc) from out-of-scope (dark mode with reason)"
  - "Explicitly identifies and maps the two features blocked by third-party API; names risk and mitigation (e.g., fallback implementation, rollback plan)"
  - "Acceptance criteria include legal sign-off and coordinated marketing/support go-live"
  - "Stakeholder checklist has clear owners and acknowledges tight timeline for marketing/support"
  - "Dependencies section names the third-party API risk and at least one mitigation (contingency implementation, feature flag for rollback)"
  - "Scope is self-contained despite complexity; reader understands cross-team coordination and critical path"
rubric:
  risk_identification: 0.35
  dependency_clarity: 0.3
  stakeholder_coordination: 0.2
  scope_boundaries: 0.15
weight: 1.0
---

Complex release with dependencies, multi-team work, and tight external constraints.
Guards against scope creep, missing risk mitigation, and ambiguous stakeholder ownership.
