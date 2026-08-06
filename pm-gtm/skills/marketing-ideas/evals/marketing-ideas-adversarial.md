---
id: marketing-ideas-adversarial
skill: marketing-ideas
input:
  prompt: "Give me 100 marketing ideas for our company."
  context: "No product info. No ICP. No positioning. No funnel stage. No budget. No constraints. Vague pressure for quantity over quality."
expected:
  - "Does NOT return a generic list of 100 unscoped ideas (e.g., 'Do TikTok, do LinkedIn, do podcasts…')"
  - "Asks for required inputs (product, ICP, positioning) before ideating — does not guess"
  - "Explains why 100 generic ideas are less useful than 10–15 tailored, scoped ideas"
  - "If it proceeds with reasonable assumptions, it clearly flags them and explains the scope (e.g., 'Assuming a B2B SaaS for SMBs, US-only, early stage')"
  - "Delivers ideas tied to the assumptions and positioned for quality over quantity"
  - "Does not sacrifice the Quality Bar (effort/impact estimates, funnel stages, channel diversity, positioning alignment) in pursuit of a high count"
rubric:
  scoping_discipline: 0.35
  asking_for_inputs: 0.25
  quality_over_quantity: 0.25
  assumption_clarity: 0.15
weight: 1.0
---

Adversarial: vague, under-scoped request with pressure for quantity and no context. Guards against the skill returning generic checklists divorced from product/ICP/positioning, and ensures it resists the quantity vs. quality trap.
