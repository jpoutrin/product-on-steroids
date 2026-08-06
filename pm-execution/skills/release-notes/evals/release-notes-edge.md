---
id: release-notes-edge
skill: release-notes
input:
  prompt: "Create release notes from these two tickets: [Ticket 1: 'Reduced API latency by optimizing queries.'] [Ticket 2: 'Removed deprecated auth endpoint v1. Migrate to v2 by Jan 31.']"
  context: "Raw material is sparse (1–2 brief tickets with minimal detail). One change is a breaking change requiring migration steps. Product: developer-facing API. Tone: technical but clear."
expected:
  - "Infers and expands sparse descriptions into complete, benefit-driven entries without making unsupported claims"
  - "Breaking change section includes clear migration timeline and step-by-step guidance"
  - "Balances technical depth (appropriate for API audience) with clarity (no unexplained jargon)"
  - "Each entry is still 1–3 sentences and user-focused, even with minimal input"
  - "Output follows template.md structure with Breaking Changes section properly filled"
rubric:
  inference_quality: 0.3
  clarity: 0.3
  breaking_change_clarity: 0.2
  completeness: 0.2
weight: 1.0
---

Edge case: sparse raw material (1–2 brief tickets) that requires careful inference and expansion. Guards against two risks: (1) glossing over breaking changes, and (2) padding with unsupported speculation. Skill must expand thoughtfully and clearly flag when more context is needed.
