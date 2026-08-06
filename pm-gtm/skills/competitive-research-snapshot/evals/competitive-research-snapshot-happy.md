---
id: competitive-research-snapshot-happy
skill: competitive-research-snapshot
input:
  prompt: >
    Build a competitive research snapshot for our project management SaaS
    (Flowdesk). We compete with Asana, Monday.com, ClickUp, Notion, and Linear.
    We target engineering-led teams at 50-250-person companies with a
    developer-friendly API and no-code automation. Use the default dimensions.
  context: >
    Pricing: Flowdesk is $12/seat/mo (public). Asana, Monday, ClickUp, Notion,
    Linear pricing pages are all publicly available. G2 reviews exist for all
    five competitors. The PM wants to brief the growth team before Q3 planning.
expected:
  - Comparison table covers all five named competitors across at least the 7 default dimensions
  - Every cell is filled, "—", or marked "(est.)" — no unsupported assertions
  - "Where to Win" has 3-5 bullets each grounded in a table observation (e.g. citing which competitors lack the API or developer GTM)
  - Landscape Overview names the market and the competitive dynamics in 3-6 sentences
  - Snapshot is clearly a broad scan, not a deep profile of any single player
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy path: a PM provides a known SaaS market, five direct competitors, and
good context (pricing, positioning, research sources). Guards against the
skill producing a thin or one-sided output when input is generous — the table
should be fully populated, the Where to Win section should be specific and
evidence-linked, and no competitor should be omitted from the table.
