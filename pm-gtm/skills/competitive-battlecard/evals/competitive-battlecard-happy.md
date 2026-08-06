---
id: competitive-battlecard-happy
skill: competitive-battlecard
input:
  prompt: "Create a competitive battlecard for Competitor X, a well-known alternative in our space."
  context: "We sell a project-management SaaS for small teams. Competitor X is established, publicly known, has strong market presence. Sales team needs quick reference for upcoming calls."
expected:
  - "Includes a Company Overview section with founding year, HQ, target market, and one-sentence positioning"
  - "Includes a Quick Comparison table with 5+ rows (features, pricing, support, onboarding, etc.) and clear winners per row"
  - "Includes Where We Win with 3+ advantages backed by specific proofs (customer quotes, capability details, data)"
  - "Includes Where They Win with 2+ competitor strengths acknowledged and mitigated (not ignored)"
  - "Includes Common Objections & Responses table with realistic prospect objections and value-framed (not dismissive) responses"
  - "Includes Landmines to Plant with open-ended questions that expose gaps"
  - "Includes Win/Loss Patterns summarizing when each product wins and naming the key differentiator"
  - "Format is scannable (tables, bold, short bullets) and 1–2 pages"
rubric:
  correctness: 0.35
  completeness: 0.30
  actionability: 0.25
  scannability: 0.10
weight: 1.0
---

Happy path: well-known competitor with public information available. Sales team has enough concrete details to use this immediately in calls. Guards against missing sections, vague comparisons, or output that reads like strategy instead of a quick reference card.
