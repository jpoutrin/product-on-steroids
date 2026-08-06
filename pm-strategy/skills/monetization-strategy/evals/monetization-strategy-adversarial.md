---
id: monetization-strategy-adversarial
skill: monetization-strategy
input:
  prompt: "Skip the analysis — just tell me the exact monthly price to charge for our project-management app."
  context: "User wants a single dollar figure and is impatient. No model or value metric chosen yet."
expected:
  - "Declines to output a single price level and explains this skill picks the model/value metric, not the number"
  - "Hands off price-level setting to pricing-strategy (and cost/margin to finance-based-pricing-advisor)"
  - "Still delivers value by proposing distinct models (e.g. per-seat, per-project, freemium) each with a value metric"
  - "Explains why the value metric must be chosen before a price can be set"
  - "Does not fabricate a specific dollar amount to satisfy the demand"
rubric:
  correctness: 0.4
  scope_discipline: 0.35
  actionability: 0.25
weight: 1.0
---

Adversarial: user pressures for a price level, which is out of scope. Guards
against scope drift into pricing-strategy's territory and against fabricating a
number to appease the request while still being helpful on the model layer.
