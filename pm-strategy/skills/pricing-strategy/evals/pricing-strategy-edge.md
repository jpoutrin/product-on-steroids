---
id: pricing-strategy-edge
skill: pricing-strategy
input:
  prompt: "What should we charge for our new API monitoring tool? We have no survey data yet."
  context: "Early-stage, no WTP survey. Alternative is a manual on-call rotation the team estimates costs ~€2,000/mo in engineer time. Only one loose competitor at $99/mo with a different scope."
expected:
  - "Chooses value-based (or value-share) inference because survey data is absent, and says so"
  - "Anchors WTP to the ~€2,000/mo alternative and infers a price as a share of value delivered"
  - "Triangulates cautiously against the single $99 competitor while noting the scope mismatch"
  - "Explicitly flags the inferred WTP as a med/low-confidence assumption to validate"
  - "Recommends validating via a Van Westendorp survey or founder-led sales calls before committing"
rubric:
  correctness: 0.3
  completeness: 0.2
  assumptions_explicit: 0.3
  actionability: 0.2
weight: 1.0
---

Edge case: no survey data and a thin competitive reference. Guards against
inventing a false-precision WTP band and forces value-share inference plus an
explicit flag that the number is unvalidated.
