---
id: test-scenarios-edge
skill: test-scenarios
input:
  prompt: "Write test scenarios for: As a user, I want the checkout form to validate my input, so that I don't submit bad data."
  context: "No explicit acceptance criteria provided. The product is a B2C checkout flow."
expected:
  - "Asks at least one clarifying question about what 'validate my input' means (which fields, which validation rules) before generating full scenarios"
  - "Does NOT fabricate specific acceptance criteria and silently proceed as if they were stated"
  - "If it proceeds with inferred criteria, it clearly labels them as assumed and flags that the PM/stakeholder should confirm"
  - "Any scenarios it does produce include explicit starting conditions and observable expected outcomes"
  - "Edge cases for boundary values (e.g., max-length fields, special characters, empty required fields) are surfaced or flagged"
rubric:
  clarification_discipline: 0.40
  assumption_transparency: 0.30
  scenario_quality: 0.20
  edge_coverage: 0.10
weight: 1.0
---

Edge case: user story has a goal but no acceptance criteria — the most common
real-world input state. Guards against the skill silently inventing criteria and
generating scenarios that appear authoritative but are actually unchecked
assumptions. The skill should surface the ambiguity before (or while) generating.
