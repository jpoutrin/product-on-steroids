---
id: identify-assumptions-new-edge
skill: identify-assumptions-new
input:
  prompt: "We're launching a mobile app for migrant workers in Southeast Asia to send remittances without traditional banks. P2P payments, very low fees, built on Stellar blockchain. Target: Philippines, Vietnam, Thailand. What are our biggest assumptions?"
  context: "Team: CEO (fintech background), 1 engineer, 1 community person (Tagalog-speaking). Regulatory landscape varies by country (some restrictions on crypto). User research: 20 interviews with remittance corridors, high trust in informal channels (word-of-mouth). Limited competition data for this exact segment."
expected:
  - "Identifies the full eight-category landscape despite sparse data and emerging-market context"
  - "Distinguishes between trust/adoption assumptions (edge-case for this user group) and technical viability assumptions (blockchain complexity)"
  - "Ethics category is weighted heavily (regulatory, user protection, financial vulnerability)"
  - "Validation approach reflects the operating environment (community research, not scalable surveys; regulatory consultations, not formal licensing path)"
  - "Handles ambiguity in competitor data by explicit acknowledgment ('low confidence: we haven't found direct competitors, but informal channels dominate')"
  - "Output follows template.md structure with all 6 sections in order"
rubric:
  sensitivity_to_context: "Assumptions are tailored to emerging market + blockchain + vulnerable population (not generic SaaS); recognizes trust as a primary value lever, regulatory as high-impact risk, and community as distribution channel"
  handling_sparse_data: "Confidence levels appropriately low where data is sparse (regulatory clarity, competitor landscape, user behavior at scale); validation approach names specific proxies or research methods rather than assuming availability of standard data"
  ethics_prioritization: "Ethics category assumptions are present and weighted as high-impact (user financial protection, regulatory compliance, fraud risk); not treated as secondary"
  pragmatic_validation: "Suggests validation methods realistic to the context and budget (community interviews, regulatory advisors, partnerships with remittance operators) rather than enterprise-scale research"
weight: 1.0
---

This edge case tests the skill's ability to surface assumptions in a new, ambiguous, and high-risk context: a fintech venture in emerging markets with regulatory uncertainty, limited competitive data, and vulnerable users. The skill should handle sparse information gracefully, weight ethics appropriately, and suggest validation methods that fit the operating environment. Guards against: assuming standard SaaS assumptions apply, downplaying regulatory/ethics risks, suggesting validation methods that are unaffordable or unavailable in the target market.
