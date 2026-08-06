---
id: gtm-strategy-edge
skill: gtm-strategy
input:
  prompt: "We're launching a project management tool for software engineering teams. The market is dominated by Jira, which has ~80% share. How do we build a GTM strategy here?"
  context: "Product differentiator: zero-config setup and AI-generated sprint plans. Target: small engineering teams (5–30 devs) at startups who find Jira too heavy. We have 8 interviews with frustrated Jira users at Series A–B startups. No current customers. Budget: lean, primarily founder-led sales and content."
expected:
  - "Acknowledges the incumbent dominance explicitly and uses it to sharpen the beachhead — targets the segment most underserved by Jira (small teams who find it too heavy) rather than competing head-on"
  - "Positioning takes a clear anti-Jira or category-differentiated stance with proof points, and names what the product explicitly cedes to Jira"
  - "Market entry motion fits the lean budget and founder-led context (e.g., PLG or community-led) rather than recommending expensive SLG"
  - "Channel mix reflects low-cost, high-reach channels appropriate for reaching startup engineering teams (e.g., developer communities, content, Product Hunt)"
  - "Expansion arc acknowledges the incumbent risk and proposes a logical bowling-pin sequence — not a direct attack on Jira's core enterprise segment"
  - "Launch sequencing includes a go/no-go criterion tied to ICP validation before scaling spend"
  - "Success metrics include a competitive displacement metric or churn-from-incumbent signal alongside standard acquisition/activation metrics"
rubric:
  correctness: 0.40
  completeness: 0.25
  actionability: 0.20
  assumptions_explicit: 0.15
weight: 1.0
---

Edge case: entering a market with a dominant incumbent holding ~80% share. Guards against
naive "compete on all fronts" strategies and generic positioning that fails to account for
switching costs and incumbent lock-in. Validates that the skill uses the incumbent context
to sharpen segment selection, positioning negative space, and channel choices — not just
acknowledge it as a bullet point and move on.
