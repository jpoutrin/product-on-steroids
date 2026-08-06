---
id: product-vision-edge
skill: product-vision
input:
  prompt: "Refine our current vision — it's not landing with the team: 'To be the leading AI-powered platform leveraging synergies to deliver best-in-class solutions for our stakeholders.'"
  context: "Existing vision is jargon-heavy, generic, and unmemorable. Product is a scheduling tool for home-services contractors (plumbers, electricians)."
expected:
  - "Names why the current statement fails (jargon, not memorable, no emotion, no real person)"
  - "Produces a rewritten one-sentence vision that is concrete, jargon-free, and emotionally resonant"
  - "Anchors the new vision to the actual customer (home-services contractors) and their world"
  - "Offers alternative phrasings so the team can choose deliberately"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge case: refining an existing vague, jargon-laden vision rather than starting
blank. Guards that the skill diagnoses the failure modes, strips buzzwords, and
re-anchors the vision to a real customer instead of polishing the abstraction.
