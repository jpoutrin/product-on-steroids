---
id: pricing-packaging-tracker-happy
skill: pricing-packaging-tracker
input:
  prompt: >
    Build a pricing and packaging tracker for our project-management tool.
    Competitors to cover: Linear, Notion, Asana, Monday.com, and ClickUp.
    All have public pricing pages. Focus on USD pricing, SMB to mid-market tiers.
    Our product is currently $25/user/month (annual) with a single flat tier.
  context: >
    User has confirmed all five competitors have fully public pricing pages.
    They want to understand value metrics, feature-fencing patterns, and where
    gaps exist relative to their own flat-tier model.
expected:
  - "Produces all 5 template sections in order: Tracker Summary, Pricing Comparison Table, Packaging Patterns, Value Metric Analysis, Pricing Gaps & Opportunities"
  - "Every row in the Pricing Comparison Table includes a Last Verified date"
  - "All five competitors (Linear, Notion, Asana, Monday.com, ClickUp) appear in the table with at least one tier each"
  - "At least 3 packaging pattern observations are present, each citing evidence from specific competitors"
  - "Value Metric Analysis covers per-seat pricing and at least one other metric found across the set"
  - "Pricing Gaps & Opportunities is framed as observations or questions, not as 'you should charge X'"
  - "Tracker Summary includes a freshness caveat and a suggested re-verification cadence"
  - "The user's own $25/user/month flat tier is noted in context but kept clearly separate from competitor data"
rubric:
  correctness: 0.35
  completeness: 0.30
  structure_conformance: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: five well-known SaaS competitors with fully public pricing pages and
a user who has provided their own current price point. Guards against missing
Last Verified dates, omitting competitors, and framing opportunities as direct
pricing recommendations. Also checks that the user's own product data is not
conflated with competitor data.
