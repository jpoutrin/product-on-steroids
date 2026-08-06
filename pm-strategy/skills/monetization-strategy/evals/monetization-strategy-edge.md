---
id: monetization-strategy-edge
skill: monetization-strategy
input:
  prompt: "We're building a marketplace connecting freelance illustrators with small businesses. How do we monetize?"
  context: "Two-sided. Illustrators are supply-constrained and price-sensitive; businesses have budget. Chicken-and-egg liquidity risk at launch."
expected:
  - "Explicitly reasons about which side pays (supply vs demand) rather than assuming both"
  - "Proposes 3-5 distinct models including transaction/take-rate and at least one non-transaction alternative"
  - "Names a value metric for each (e.g. take-rate on GMV, listing fee, subscription for demand side)"
  - "Flags marketplace-specific risks: liquidity, disintermediation, trust and safety"
  - "Validation experiments account for the chicken-and-egg problem (e.g. subsidize one side first)"
  - "Recommendation weighs which side to monetize given supply is the constrained side"
rubric:
  correctness: 0.3
  completeness: 0.25
  reasoning_on_who_pays: 0.3
  actionability: 0.15
weight: 1.0
---

Edge: two-sided marketplace where "who pays" is genuinely ambiguous and the
value metric depends on which side is monetized. Guards against defaulting to a
single-side assumption and ignoring liquidity/disintermediation dynamics.
