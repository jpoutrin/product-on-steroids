---
id: positioning-workshop-happy
skill: positioning-workshop
input:
  prompt: "Run a positioning workshop for our product, Cliniflow."
  context: |
    Cliniflow is a clinical documentation tool for EU outpatient clinics.
    Team in the room: PM (facilitator), Head of Sales, VP Marketing, Lead Engineer, Customer Success Lead.
    Existing artefacts: a 12-month-old pitch deck that positioned Cliniflow as "the EHR for modern clinics."
    The team believes they have strong product-market fit signals in dermatology clinics (5–20 physicians).
expected:
  - "Runs all six exercises in order without skipping any"
  - "Exercise 1 produces at least two named competitive alternatives plus do-nothing, each with a rationale"
  - "Exercise 2 attributes are specific and falsifiable — not vague superlatives"
  - "Exercise 3 translates each attribute to a customer outcome, not a feature description"
  - "Exercise 4 names a segment (dermatology clinics or similar) with at least one reason tied to the identified value"
  - "Exercise 5 names a chosen market frame and explains why it serves target customers better than alternatives"
  - "Exercise 6 produces a positioning statement in the canonical April Dunford form, internally consistent with Exercises 1–5"
  - "Summary flags any team disagreement as a tension note rather than silently resolving it"
rubric:
  process_adherence: 0.30
  correctness: 0.30
  completeness: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a cross-functional team with good PMF signals and a stale prior
positioning. Guards against skipping exercises, collapsing features into values,
and carrying forward the old pitch-deck framing unchallenged.
