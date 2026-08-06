---
id: gtm-strategy-happy
skill: gtm-strategy
input:
  prompt: "Build a GTM strategy for our new SaaS product — an AI-powered contract review tool for in-house legal teams at mid-market US companies (200–2000 employees)."
  context: "We have 12 customer discovery interviews with in-house counsel. Key pain: manual contract review takes 3–5 days per contract; legal teams are overwhelmed. Competitors: legacy CLM vendors (Ironclad, ContractPodAi) are complex and expensive. Our differentiator: setup in <1 day, no IT required. Pricing TBD. Targeting a Q3 launch."
expected:
  - "Beachhead segment is specific — names the persona (in-house counsel / legal ops), company size (mid-market, 200–2000 employees), and acute pain (contract review time / backlog)"
  - "Market entry motion is named (e.g., PLG or SLG) and justified against the legal buyer's research and buying behavior"
  - "Positioning follows the house format: For [customer], [product] is the [category] that [differentiation] because [proof point]"
  - "Channel mix names 2–4 channels, tiers them primary/secondary/experimental, and justifies each against how legal buyers discover and evaluate tools"
  - "Pricing names a model and anchor or tier structure with rationale; open decisions are flagged rather than omitted"
  - "Launch sequencing has pre-launch, launch, and post-launch phases each with at least one go/no-go criterion"
  - "Success metrics include both leading indicators (awareness/acquisition) and lagging indicators (activation/revenue) with targets and measurement cadence"
rubric:
  correctness: 0.35
  completeness: 0.30
  actionability: 0.20
  assumptions_explicit: 0.15
weight: 1.0
---

Happy path: well-scoped product with customer research, clear competitor context, and
a defined launch window. Guards against generic output ("target all businesses"), missing
channel rationale, and metrics that only cover one funnel stage. Validates that the skill
integrates customer evidence into every section rather than producing a template-filled-with-boilerplate.
