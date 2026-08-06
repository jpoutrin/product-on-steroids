---
id: release-notes-happy
skill: release-notes
input:
  prompt: "Write release notes for our v2.1 release. We shipped 3 new features, improved 2 existing areas, and fixed 4 bugs."
  context: "Raw material: 3 JIRA tickets (feature), 2 performance tickets (improvements), 4 bug tickets (fixes). Product: B2B SaaS project management tool. Tone: professional and benefit-focused. Audience: end users and team leads."
expected:
  - "Divides changes into at least three clear sections: New Features, Improvements, Bug Fixes"
  - "Each entry is 1–3 sentences, leading with user benefit rather than technical detail"
  - "Entries use plain language without jargon, ticket numbers, or internal codenames"
  - "Each section describes *why it matters* to the user, not just what changed"
  - "Tone is professional and aligns with B2B SaaS conventions"
  - "Output follows template.md structure with all relevant sections present and in order"
rubric:
  correctness: 0.35
  benefit_focus: 0.25
  clarity: 0.25
  completeness: 0.15
weight: 1.0
---

Happy path: enough structured raw material (clear tickets with descriptions) to build a polished release notes document. Guards against purely technical descriptions and unsupported claims.
