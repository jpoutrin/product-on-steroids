---
id: gtm-motions-happy
skill: gtm-motions
input:
  prompt: "Design the GTM motion stack for a B2B SaaS document collaboration tool targeting SMBs."
  context: "ACV: $50/month. Sales cycle: 2–3 weeks. Self-serve product, minimal onboarding friction. Addressable market: ~80k SMBs in EU/US. Team: 1 growth engineer, 1 product manager. Budget: $10k/month."
expected:
  - "Product profile is captured with concrete numbers (ACV, cycle, market, team size, budget)"
  - "All 7 motions are scored 1–10 with explicit fit justifications tied to the product profile"
  - "Primary motion (PLG) is clearly recommended with defensible rationale (low ACV, self-serve, SMB market)"
  - "Secondary motion(s) identified (e.g., community or inbound) with stated rationale for how they complement"
  - "90-day playbooks are specific and actionable per motion (quick wins, deliverables, tools, go/no-go gates)"
  - "Buyer journey is mapped per motion to awareness/consideration/decision/retention"
  - "Success metrics are motion-specific (CAC for paid, activation rate for PLG, engagement for community)"
  - "Key assumptions are numbered with confidence levels and validation methods"
rubric:
  correctness: 0.3
  completeness: 0.25
  motion_fit_reasoning: 0.25
  actionability: 0.2
weight: 1.0
---

Happy path: well-constrained product profile (low ACV, self-serve, SMB-focused, small team) with clear fit for PLG as primary. Guards against generic recommendations and ensures fit reasoning is grounded in product characteristics.

