---
id: marketing-ideas-edge
skill: marketing-ideas
input:
  prompt: "I have a consumer app for personal finance that helps people track spending and set savings goals. I'm a solo founder, pre-launch, and I want to build awareness once we're live."
  context: "No specific ICP defined yet. No budget stated. No existing channels or data. Positioning not set. Global or US market unclear."
expected:
  - "Asks clarifying questions or makes reasonable assumptions explicit (e.g., 'Assuming your ICP is young professionals, 25–40, with disposable income in the US')"
  - "Generates 10–15 ideas despite sparse context — does not refuse or demand perfect inputs"
  - "Ideas span diverse channels with an emphasis on high-leverage, low-cost tactics suitable for pre-launch solo founder (e.g., founder community, product hunt, word-of-mouth, organic social)"
  - "Explicitly labels assumptions about positioning, ICP, and stage (e.g., 'Assumption: you're positioning on simplicity vs. Mint's complexity')"
  - "Includes at least 3–4 ideas for product-led or community-driven growth (given budget constraints and stage)"
  - "Summary table is included and sortable"
rubric:
  handling_sparse_context: 0.30
  completeness: 0.25
  assumption_clarity: 0.25
  actionability: 0.20
weight: 1.0
---

Edge case: sparse context (no ICP, budget, positioning, or stage clarity). Guards against refusing to ideate and ensures the skill makes reasonable assumptions, flags them, and delivers actionable ideas suitable for a resource-constrained, early-stage scenario.
