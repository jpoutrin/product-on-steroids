---
id: market-sizing-consumer-edge
skill: market-sizing
input:
  prompt: "Size the market for a consumer app that helps hobby beekeepers track hive health."
  context: "Niche consumer market, little published data. Global. No pricing decided yet."
expected:
  - "Defines the market boundaries and flags the sparse-data situation up front"
  - "Builds a bottom-up estimate from a proxy population (e.g., number of hobby beekeepers) and a proposed price/frequency anchor it introduces and labels"
  - "Attempts a top-down estimate or explicitly explains why reliable top-down data is unavailable, rather than inventing a source"
  - "Reports TAM, SAM, and SOM as three distinct numbers even under uncertainty"
  - "Marks low-confidence assumptions and names concrete ways to validate the population and willingness-to-pay"
rubric:
  correctness: 0.30
  completeness: 0.25
  assumptions_explicit: 0.30
  actionability: 0.15
weight: 1.0
---

Edge case: thin public data and no pricing. Guards against fabricating sources
and against refusing to size — the skill should proxy, anchor, label confidence,
and still deliver three numbers.
