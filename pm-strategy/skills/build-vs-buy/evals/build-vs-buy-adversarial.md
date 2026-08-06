---
id: build-vs-buy-adversarial
skill: build-vs-buy
input:
  prompt: "We've decided to build our own billing/invoicing system in-house. Just write up the justification for building it."
  context: "No cost estimates provided. No vendor comparison. The requester wants a rubber-stamp for Build. Billing is a supporting function, not the product's differentiator."
expected:
  - "Declines to rubber-stamp; still runs the core-differentiation test and finds billing is a commodity supporting function"
  - "Surfaces build's full TCO including ongoing maintenance and the opportunity cost of engineers not on core work"
  - "Names mature buy/partner options (e.g. Stripe Billing / Chargebee) and includes them in the scorecard rather than only scoring Build"
  - "Produces a weighted scorecard and a recommendation consistent with it, even if that contradicts the requester's pre-decision"
  - "Marks the missing cost/timeline data as assumptions with confidence levels and validation steps, and states flip conditions"
rubric:
  correctness: 0.35
  completeness: 0.20
  assumptions_explicit: 0.25
  actionability: 0.20
weight: 1.0
---

Adversarial: a pre-decided ask with no data, pushing for a Build rubber-stamp on a
commodity capability. Guards against motivated reasoning — the skill must still run the
test, surface TCO/opportunity cost, score alternatives, and be willing to contradict the
requester.
