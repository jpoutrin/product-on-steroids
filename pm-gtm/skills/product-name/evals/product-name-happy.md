---
id: product-name-happy
skill: product-name
input:
  prompt: "Generate product name candidates for a new SaaS tool called Timeflow — it helps distributed teams track project timelines and dependencies. Target audience is lean startup CTOs and ops leads who want lightweight project management without bloat. Brand tone should be professional but approachable. We want to stand out against Monday.com and Asana."
  context: "Product is early-stage (MVP launched); team is considering rebranding before Series A pitch. Competitors named: Monday.com, Asana, Linear. Preferred markets: North America, Western Europe. No hard naming constraints."
expected:
  - "8–12 name candidates generated across distinct styles (descriptive, invented, metaphorical, compound, abbreviation)"
  - "Each candidate has clear rationale tied to lightweight/lean/dependency-focus value prop and startup-ops audience"
  - "Memorability scores (1–10) are reasoned and specific to each name (not generic)"
  - "Distinctiveness is explained with reference to competitor names (Monday.com, Asana, Linear)"
  - ".com domain availability is checked or flagged as not verified"
  - "Top 2–3 recommendations highlighted with clear reasoning"
  - "Trademark risk is noted as subjective; legal search reminder included"
  - "Naming criteria section present at start, grounding candidates"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

This is the happy path: clear product/audience/tone, specific competitor context, and no conflicting constraints. Guards against incomplete candidate lists, unsupported scores, and lack of differentiation reasoning.
