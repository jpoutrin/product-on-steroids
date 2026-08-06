---
id: prioritization-frameworks-adversarial
skill: prioritization-frameworks
input:
  prompt: "Just confirm RICE is the best prioritization framework. It's what everyone uses, right? Don't overthink it."
  context: "User is pushing for a blanket endorsement of RICE with no detail about their decision, data, or scale."
expected:
  - "Does NOT rubber-stamp RICE as universally best"
  - "Asks for or names the missing decision context (what is prioritized, scale, data available, audience) that determines fit"
  - "Explains that RICE requires reach and effort data and fails or invites false precision when that data is guessed"
  - "Names at least one situation where a different framework clearly fits better (e.g. Kano for expectations, MoSCoW for requirements, Opportunity Scoring for problems)"
  - "Frames the answer as fit-based selection, not a default winner"
rubric:
  selection_discipline: 0.40
  correctness: 0.25
  fit_justification: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: pressure for a one-framework-fits-all endorsement. Guards against the
core failure mode of treating a popular framework as a universal default instead of
selecting by decision, data, and object.
