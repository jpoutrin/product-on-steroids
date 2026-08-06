---
id: pricing-packaging-tracker-edge
skill: pricing-packaging-tracker
input:
  prompt: >
    Build a pricing and packaging tracker for our HR software. Cover: BambooHR,
    Personio, HiBob, Rippling, and Workday. Focus on mid-market USD pricing.
  context: >
    BambooHR, Personio, and HiBob have pricing pages with some public information.
    Rippling has a "request a quote" model — no public pricing.
    Workday is fully enterprise-only with no public pricing.
    User has not provided their own product pricing.
expected:
  - "Rippling and Workday are included in the table with explicit 'custom / no public data' notes rather than being omitted"
  - "The Last Verified date is present for every row, including the custom-pricing rows"
  - "Packaging Patterns section acknowledges that pattern detection is limited by missing data from two of five competitors"
  - "Pricing Gaps & Opportunities section notes the custom-pricing-only segment as itself an observation (e.g. enterprise consolidation signal)"
  - "The skill does not fabricate price points for Rippling or Workday"
  - "Tracker Summary scope caveat specifically flags that 2 of 5 competitors have no public pricing"
  - "All 5 template sections remain present even with partial data"
rubric:
  correctness: 0.40
  completeness: 0.30
  structure_conformance: 0.20
  actionability: 0.10
weight: 1.0
---

Edge case: two of five competitors use enterprise-only or custom-quote pricing
with no publicly available price points. Guards against fabricating prices,
silently omitting competitors with no public data, and producing packaging
pattern conclusions that overreach beyond what the available data supports.
The skill must handle partial data gracefully and make the gaps visible.
