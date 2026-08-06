---
id: brainstorm-experiments-existing-happy
skill: brainstorm-experiments-existing
input:
  prompt: "We're adding a notification preference panel to our email product. Users can opt into daily digests, real-time alerts, or turn off notifications. We need experiments to validate that users will use the feature and that it improves retention."
  context: "Existing product with 100k MAU; 30% open rate on emails; retention baseline 60% 30-day. Engineering capacity: 1–2 sprints. Can run A/B tests; infrastructure for gradual rollout exists."
expected:
  - "Generates at least 3 distinct experiments using different methods (e.g., fake door, A/B test, prototype/usability)"
  - "Each experiment has a clear, measurable hypothesis tied to one of the input assumptions"
  - "Every row specifies a concrete success metric and numeric threshold (not 'high' or 'good')"
  - "Includes both low-cost (prototype, spike) and production tests (A/B test) with risk mitigation for the latter"
  - "Cost and timeline estimates are grounded and realistic (e.g., '2–3 days dev' not 'quick')"
  - "Prioritization or rationale explains which experiments resolve the highest risk or run fastest"
rubric:
  hypothesis_clarity: 0.25
  method_rigor: 0.25
  metric_definition: 0.25
  feasibility_estimates: 0.15
  prioritization: 0.1
weight: 1.0
---

Happy path: realistic feature idea with clear product context and engineering capacity. Validates that the skill generates diverse, grounded experiments with concrete metrics and prioritization.
