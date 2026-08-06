---
id: market-landscape-scan-edge
skill: market-landscape-scan
input:
  prompt: "Scan the landscape for AI agents that autonomously operate accounting software for small businesses. It feels very early — I barely know who's in it."
  context: "B2B, micro/small-business buyers, global. Nascent space, few established named players. Orientation question: is a category forming and where's the opening?"
expected:
  - "Fixes the boundary despite the nascent space and flags that named players are sparse"
  - "Infers categories by role (e.g. horizontal AI-agent platforms, vertical accounting incumbents adding AI, adjacent bookkeeping-automation tools, emerging startups) rather than enumerating rivals"
  - "Reads trends shaping an emerging market with direction and 'so what', labeling observations vs cited facts"
  - "Frames white spaces as hypotheses to validate, appropriate to a space with thin evidence"
  - "Still delivers a category map on two named axes even with few concrete players, positioning categories not companies"
  - "Orients on whether a category is forming and names one deeper follow-up"
rubric:
  correctness: 0.3
  completeness: 0.25
  categorization: 0.25
  actionability: 0.2
weight: 1.0
---

Edge case: a nascent market with few named players forces category and trend
inference over enumeration. Guards against the skill giving up for lack of a
competitor list, or over-claiming certainty on thin evidence.
