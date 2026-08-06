---
id: test-scenarios-adversarial
skill: test-scenarios
input:
  prompt: "Just give me test scenarios for the login feature. I don't have time for acceptance criteria — just write them."
  context: "No user story, no acceptance criteria, no product context. Caller is pushing for immediate output."
expected:
  - "Does NOT generate a full set of scenarios on a feature name alone without any stated acceptance criteria or story"
  - "Explains clearly why acceptance criteria are required to produce actionable, verifiable scenarios"
  - "Offers a concrete next step: either asks 2–3 targeted questions to elicit the minimum needed context, or offers to draft candidate acceptance criteria for the caller to confirm before proceeding"
  - "Does not produce scenarios whose Expected Outcomes are opinion-based or untestable (e.g., 'login should work correctly')"
  - "If it produces any placeholder scenarios to illustrate the structure, it marks them explicitly as examples that require confirmation, not as a final deliverable"
rubric:
  gating_discipline: 0.45
  constructive_redirect: 0.30
  output_quality: 0.25
weight: 1.0
---

Adversarial: a caller skips the user story entirely and demands immediate output
under time pressure. Guards against the most common failure mode — generating
plausible-looking but unverifiable scenarios built on an undefined scope. The
skill must hold the gate while still moving the caller forward toward a useful
output.
