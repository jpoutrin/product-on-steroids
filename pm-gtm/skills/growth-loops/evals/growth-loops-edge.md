---
id: growth-loops-edge
skill: growth-loops
input:
  prompt: "We're a B2B analytics platform. Our users are data analysts. How do we grow?"
  context: "Product: dashboards + SQL queries + Slack alerts. Users are individual analysts, but dashboards can be shared within teams. No referral program. Monetization is per-user seat licensing. No obvious viral or social sharing loop."
expected:
  - "Identifies multiple loops even where sharing is not native (e.g., 'analyst shares insight via Slack → colleague sees value → signs up'; data-loop where more data attracts power users)"
  - "Acknowledges loops that are weak or absent in this product (e.g., 'viral sharing is low friction'; instead describes collaboration loop, maybe an internal data feedback loop)"
  - "Estimates K-factors honestly — low for some loops, noting the constraint (B2B, non-social, per-seat pricing limits viral)"
  - "Still recommends a prioritized loop and a realistic roadmap, even if none have K > 1 (e.g., strengthen collaboration loop to retain and expand seat count within existing customers)"
  - "Distinguishes between acquisition loops (bringing new users) and retention/expansion loops (which matter more for B2B seat-based models)"
rubric:
  loop_identification_nonobvious: 0.30
  honesty_about_constraints: 0.25
  coefficient_realism: 0.20
  prioritization_context_aware: 0.25
weight: 1.0
---

Edge case: product without obvious viral potential. Skill must map realistic loops given the constraint (B2B, non-shareable, seat-based pricing) and pivot to retention/expansion loops rather than forcing viral. Guards against one-size-fits-all loop playbooks.
