---
id: brainstorm-ideas-new-edge
skill: brainstorm-ideas-new
input:
  prompt: "Help us brainstorm a new product for a global luxury e-commerce logistics startup. We're exploring how to use generative AI to improve package tracking and delivery experience."
  context: "Logistics, global, B2C. Target users: luxury e-commerce customers (high-touch, expects personalization). Budget: Series A, scaling. No prior data collection or customer interviews."
expected:
  - "Skill asks clarifying questions to narrow the problem before ideating (what is the customer pain point today? what does logistics success look like?)"
  - "Ideas are grounded in specific luxury e-commerce customer problems (not generic logistics or generic AI)"
  - "Top 5 balance quick-to-validate wins against differentiation potential (luxury market rewards personalization and experience)"
  - "Assumptions acknowledge data scarcity (no baseline customer behavior data) but remain testable"
  - "Ideas distinguish between what customers need (tracking transparency) vs. what is technically possible (AI for its own sake)"
rubric:
  clarification: 0.2
  problem_grounding: 0.25
  validation_realism: 0.25
  scope_discipline: 0.2
  assumption_realism: 0.1
weight: 0.8
---

Edge case: vague problem statement (focuses on technology, not customer pain).
Guards against AI/tech-first ideation and validates that the skill asks for
clarity before proceeding. Tests whether the skill resists scope creep and
prioritizes quick validation in a data-sparse environment.
