---
id: dummy-dataset-edge
skill: dummy-dataset
input:
  prompt: "I need synthetic data for rare-event testing. We log fraudulent transaction detection, and fraud is 0.5% of all transactions. Generate 5000 transactions, JSON format."
  context: "Need realistic fraud patterns. Columns: transaction_id, timestamp, amount, customer_segment, merchant_category, is_fraud, fraud_score. Fraud only in 0.5% (25 transactions). Fraud score should correlate with fraud label."
expected:
  - "Pragmatic sampling approach explained (e.g., intentionally oversample fraud for testability while documenting the caveat)"
  - "Constraints honored: ~0.5% fraud rate, fraud_score correlates with is_fraud"
  - "JSON is well-formed and valid"
  - "First 5–10 rows shown, including at least one fraud example"
  - "Trade-off documented: acknowledges that 0.5% is realistic but unpractical for testing, suggests alternatives (synthetic oversampling, unit test mocks)"
  - "Quick-start with jq or Python JSON parsing provided"
rubric:
  pragmatism: 0.35
  constraints_honored: 0.25
  transparency: 0.25
  usability: 0.15
weight: 1.0
---

Edge case requiring pragmatic trade-offs (sparse real-world distribution vs. testability).
Guards against naive application of constraints that make testing impossible, and ensures
the skill explains its choices transparently.

