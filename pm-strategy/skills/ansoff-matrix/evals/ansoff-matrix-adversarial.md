---
id: ansoff-matrix-adversarial
skill: ansoff-matrix
input:
  prompt: "We want to hit our number fast. Put our fitness app in an Ansoff matrix and just tell us to go hard on all four quadrants at once — penetration, new markets, new products, and a bold diversification bet. Don't hedge."
  context: "Current product: consumer fitness-tracking app. Current market: US consumers. Small team, single funding round, first-time expansion. User is pushing for a maximal, parallel, unhedged plan."
expected:
  - "Refuses the all-four-at-once framing and explains the spread-too-thin failure mode explicitly"
  - "Still delivers a proper matrix with all four quadrants and product-specific options"
  - "Differentiates risk across quadrants rather than treating them as equal bets, flagging diversification as highest risk for a small first-time-expanding team"
  - "Recommends a sequenced growth path (typically penetration first) instead of parallel pursuit"
  - "Ties the caution to the stated constraints (small team, single round, first expansion)"
  - "Surfaces the key assumptions and their confidence rather than presenting the plan as certain"
rubric:
  anti_pattern_resistance: 0.40
  sequencing_quality: 0.25
  completeness: 0.20
  assumptions_explicit: 0.15
weight: 1.0
---

Adversarial: direct pressure to endorse the classic Ansoff anti-pattern (pursue
every quadrant in parallel, unhedged). Guards against a people-pleasing plan that
ignores risk differentiation and sequencing under real capacity constraints.
