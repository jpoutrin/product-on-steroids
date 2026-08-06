---
id: market-sizing-b2b-saas-eu
skill: market-sizing
input:
  prompt: "Size the market for an EU SMB e-signature tool."
  context: "Bottom-up preferred. ~24M EU SMBs. Anchor pricing €15/mo. B2B SaaS, EU-only for now."
expected:
  - "Reports TAM, SAM, and SOM as three distinct numbers"
  - "Shows both a top-down and a bottom-up TAM and reconciles them"
  - "Bottom-up uses customers x price x frequency with the given €15/mo and ~24M SMB anchors"
  - "States every key assumption explicitly with a source or a caveat and a confidence level"
  - "SOM is a defensible fraction of SAM tied to competitive position or GTM capacity, not a round guess"
  - "Includes a 2-3 year projection alongside current figures"
rubric:
  correctness: 0.35
  completeness: 0.25
  assumptions_explicit: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: enough anchors to do a real bottom-up build and reconcile against a
top-down slice. Guards against single-method sizing and unsupported round numbers.
