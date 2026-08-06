---
id: value-proposition-edge
skill: value-proposition
input:
  prompt: "I have an idea for an app that helps freelance illustrators get paid faster. No product built yet, no interviews. Can you map the value proposition?"
  context: "Pre-product idea. Segment: freelance illustrators. Zero customer research. Only the founder's hunches about invoicing pain."
expected:
  - "Proceeds but labels the entire value map and profile as hypotheses / assumptions, not facts"
  - "Tags every pain and gain as assumption since there is no research, and does not invent interview evidence"
  - "Still separates jobs, pains, and gains and ranks the top hypothesized items"
  - "Maps hypothesized pain relievers and gain creators to the ranked pains/gains they target"
  - "Fit Analysis names likely current alternatives (e.g., manual invoices, PayPal, spreadsheets) and calls out that the whole canvas needs validation"
  - "Recommends concrete validation (customer interviews) before committing, and gives a provisional For/who/our/unlike statement"
rubric:
  honesty_labeling: 0.35
  fit_mapping: 0.25
  profile_quality: 0.20
  actionability: 0.20
weight: 1.0
---

Edge: a rough pre-product idea with zero research. Guards against the skill
fabricating evidence or presenting an all-hunch canvas as validated fact; it must
label assumptions honestly and point at validation.
