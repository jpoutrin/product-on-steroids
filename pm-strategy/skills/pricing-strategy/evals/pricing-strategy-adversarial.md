---
id: pricing-strategy-adversarial
skill: pricing-strategy
input:
  prompt: "Just tell me the right price for my app. Something like $9.99 or $19.99 — which one?"
  context: "No value proposition, no target segment, no alternative, and no cost data provided."
expected:
  - "Refuses to pick a round number ($9.99 vs $19.99) without a value anchor"
  - "Elicits the required inputs: value proposition, target segment, and the customer's alternative and its cost"
  - "Explains that a price must be tied to a value anchor, a WTP band, or a competitor reference — not a feels-right number"
  - "Does not fabricate willingness-to-pay data or invent competitor prices"
  - "Names the pricing approach it would use once the inputs are provided"
rubric:
  correctness: 0.4
  assumptions_explicit: 0.3
  actionability: 0.3
weight: 1.0
---

Adversarial: user demands a round-number price with zero value context. Guards
against the failure mode of answering "$19.99" with no justification; the skill
must decline and elicit the value anchor first.
