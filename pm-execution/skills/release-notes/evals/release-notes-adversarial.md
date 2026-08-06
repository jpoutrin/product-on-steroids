---
id: release-notes-adversarial
skill: release-notes
input:
  prompt: "Here are the git commit messages: 'fix: memory leak in event handler' 'refactor: consolidate logger instances' 'perf: batch query optimization' 'fix: race condition in concurrent writes'"
  context: "Raw material is highly technical (git commits, code diffs only, no high-level descriptions). No explicit audience, tone, or product context provided."
expected:
  - "Skill does NOT ship generic release notes; instead asks for clarification on: (1) product type and audience (end users vs developers), (2) business impact of each change, (3) preferred tone"
  - "If the skill proceeds despite missing context, it translates technical terms into plain language but flags uncertainty"
  - "Asks whether user wants internal technical changelog or customer-facing release notes (different purposes)"
  - "Does not ship release notes that lead with jargon (memory leak, race condition, event handler) without translating to user benefit"
rubric:
  appropriateness: 0.4
  clarification: 0.35
  refusal_or_caution: 0.25
weight: 1.0
---

Adversarial case: highly technical raw material (git commits, code diffs) without audience or product context. Skill must refuse to ship generic release notes or ask critical questions about audience, impact, and intent. Guards against shipping internal jargon to end users and ensures the skill doesn't conflate technical changelogs with marketing copy.
