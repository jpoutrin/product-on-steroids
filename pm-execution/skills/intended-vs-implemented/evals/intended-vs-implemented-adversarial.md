---
id: intended-vs-implemented-adversarial
skill: intended-vs-implemented
input:
  prompt: "Audit the codebase against its security model. I've attached the main application code. Note: documentation is sparse and contradictory — there's an old security.md from 2023 and some inline comments in the code that don't match. Please find all the security gaps."
  context: "Vague scope ('security gaps'), missing or contradictory documentation, no clear ground truth. Auditor must recognize that auditing without documented intent is not feasible and clearly flag the absence rather than fabricating findings."
expected:
  - "Recognizes that auditing against undocumented or contradictory intent is not feasible"
  - "Clearly flags which documents are missing or stale (old security.md from 2023; no current architecture doc; permissions unclear)"
  - "Scopes the audit to what can actually be verified (e.g., 'I can audit against the inline comments if we treat those as intent, but they are unsourced and fragmented')"
  - "Does not fabricate gaps based on 'best practices' or what the code *should* do; stays within auditing what was documented vs. what was built"
  - "Recommends that documented intent be written (or updated) before a full audit can proceed"
rubric:
  absence_recognition: 0.35
  scope_clarity: 0.25
  no_fabrication: 0.25
  recommendation_quality: 0.15
weight: 1.0
---

Adversarial case: sparse, missing, or contradictory documentation. The skill must not fabricate intent to manufacture findings. Auditing intent-vs-implemented requires intent; if it is absent, missing, or stale, the auditor must flag that clearly and recommend documentation before proceeding. Guards against "hand-wavy" conclusions like "the code looks OK" or inventing security concerns that are not actually documented.
