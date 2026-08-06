---
id: business-model-edge
skill: business-model
input:
  prompt: "Map the Business Model Canvas for a free consumer note-taking app monetized by ads and a premium tier."
  context: "Most users never pay. Revenue comes from advertisers (indirect payer) plus a small % who upgrade to premium. Existing business."
expected:
  - "Distinguishes non-paying users from the paying/monetized segments, treating advertisers as a distinct customer segment (multi-sided / indirect payer)"
  - "Value Propositions differ for free users, premium users, and advertisers"
  - "Revenue Streams capture both the advertising stream and the premium subscription, not just 'freemium'"
  - "Cost Structure reflects that free users are a cost served in order to create advertiser value / a premium funnel"
  - "Economics check reasons about conversion rate and ARPU so revenue exceeds the cost of serving free users at scale"
  - "All 9 blocks populated with no TBD"
rubric:
  correctness: 0.35
  completeness: 0.3
  coherence: 0.2
  actionability: 0.15
weight: 1.0
---

Edge: a free/freemium model where the payer is not the primary user. Guards
against collapsing free users, premium users, and advertisers into one segment,
and against a revenue block that ignores the indirect (advertiser) stream.
