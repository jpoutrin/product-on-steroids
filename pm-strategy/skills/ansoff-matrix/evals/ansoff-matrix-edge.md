---
id: ansoff-matrix-edge
skill: ansoff-matrix
input:
  prompt: "Map growth options for our project-management app on an Ansoff matrix and tell us what to do first."
  context: "Current product: PM app for freelance creatives. Current market: solo freelancers, US. No information given on capital, team size, brand strength, or competitive dynamics."
expected:
  - "Anchors the current product and current market before mapping"
  - "Populates all four quadrants with concrete, product-specific options despite thin input"
  - "Assigns differentiated risk levels per quadrant (penetration low, diversification high)"
  - "Because capabilities and constraints are unknown, states the sequencing recommendation as capability-contingent rather than inventing team size, capital, or brand facts"
  - "Names the specific inputs needed to firm up the sequence (e.g., capital available, team capacity) and how to get them"
  - "Warns against pursuing all four quadrants at once"
rubric:
  scoping_discipline: 0.35
  completeness: 0.25
  sequencing_quality: 0.25
  actionability: 0.15
weight: 1.0
---

Edge: sparse capability/constraint data. Guards against fabricating company
facts to force a confident sequence; the skill must flag the recommendation as
capability-contingent and name what would resolve it.
