---
id: brainstorm-ideas-new-happy
skill: brainstorm-ideas-new
input:
  prompt: "Generate product ideas for a new AI-powered customer success platform targeting mid-market B2B SaaS (50–500 person orgs). The core problem: CS teams struggle to track customer health across fragmented data (CRM, support tickets, product usage). The business outcome: reduce churn by enabling proactive support."
  context: "Mid-market B2B SaaS, US + EU. No pricing anchors yet. Competitive context: Gainsight, Totango, Vitally exist but are expensive and hard to implement. Technology: assume modern ML and API integrations available."
expected:
  - "Ideation spans three distinct perspectives (PM, Designer, Engineer) with genuinely different ideas per perspective"
  - "Top 5 prioritized ideas are ranked by core value delivery (solves the health-tracking problem), speed to validate, and differentiation"
  - "Each prioritized idea includes 1–2 sentences of specific reasoning and 2–3 testable assumptions (not vague positioning)"
  - "Ideas are grounded in the target segment and user problem (mid-market, CS teams, data fragmentation)"
  - "All 15 ideas are distinct (no duplicates or trivial variants)"
  - "Output follows template.md structure with all 5 sections populated"
rubric:
  perspective_diversity: 0.25
  grounding: 0.2
  prioritization: 0.25
  assumptions_actionable: 0.2
  distinctness: 0.1
weight: 1.0
---

Happy path: clear segment + well-defined problem + business outcome. Guards
against blue-sky ideation, generic ideas, and single-perspective thinking.
Validates that the skill surfaces cross-functional insights and grounds ideas
in user reality.
