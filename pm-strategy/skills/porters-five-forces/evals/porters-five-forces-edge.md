---
id: porters-five-forces-edge
skill: porters-five-forces
input:
  prompt: "Assess the attractiveness of the local food-delivery marketplace industry in a mid-size European city. It's a two-sided platform: restaurants on one side, diners on the other, and gig couriers as the supply of delivery capacity."
  context: "Two-sided marketplace. Buyer power and supplier power must be reasoned for distinct participant groups, and network effects complicate the rivalry and new-entrant ratings."
expected:
  - "Recognizes the two-sided structure and reasons buyer power (diners) and supplier power (restaurants and/or couriers) as distinct sides rather than collapsing them"
  - "Accounts for network effects when rating new entrants and rivalry (strong network effects raise entry barriers but multi-homing/low switching can offset them)"
  - "Still rates all five forces Low/Med/High with evidence and trends"
  - "Reaches an overall verdict that acknowledges the marketplace dynamics (e.g. thin margins from high rivalry and multi-homing) rather than treating it as a single-sided market"
  - "Strategic implications address the dominant forces (e.g. deepen one side's lock-in, exclusive supply)"
rubric:
  correctness: 0.30
  two_sided_reasoning: 0.30
  completeness: 0.25
  actionability: 0.15
weight: 1.0
---

Edge: a two-sided marketplace where the buyer and supplier forces map to
different participant groups and network effects complicate the entrant/rivalry
ratings. Guards against mechanically applying single-sided reasoning.
