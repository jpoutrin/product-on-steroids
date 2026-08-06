---
id: startup-canvas-happy
skill: startup-canvas
input:
  prompt: "Build a startup canvas for a new AI-assisted invoicing tool for freelance designers."
  context: "Solo-founder, web-first, PLG intent. Incumbents are heavy accounting suites (QuickBooks, FreshBooks). Freelancers hate configuration and want to get paid faster. No hosting/enterprise ambitions in year 1."
expected:
  - "Produces all 11 sections split into a Product Strategy part (1-9) and a Business Model part (10-11)"
  - "Defines 2-3 market segments by problem/JTBD (not demographics) and names a first target with a reason"
  - "Value Proposition uses What-before -> How -> What-after -> Alternatives for each segment"
  - "Trade-offs lists concrete things the product will NOT do (e.g. no enterprise, no self-hosting)"
  - "Can't/Won't argues the integrated set of choices is hard to copy, not a single unfair advantage, and notes elements reinforce each other"
  - "Names a North Star Metric and a quarterly OMTM, and ends with a Hypotheses & Experiments list with cheap tests"
rubric:
  correctness: 0.35
  completeness: 0.25
  strategic_coherence: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a well-specified new B2B product with clear incumbents and a stated
PLG posture. Guards against a canvas that blurs strategy and business model,
skips real trade-offs, or reduces defensibility to one "unfair advantage".
