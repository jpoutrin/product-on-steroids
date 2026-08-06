---
id: dummy-dataset-happy
skill: dummy-dataset
input:
  prompt: "Generate a sample dataset of e-commerce transactions for testing our checkout flow."
  context: "100 rows, CSV format. Columns: transaction_id, customer_id, timestamp, product_category, amount_usd, payment_method. Constraints: amounts between $10 and $500, timestamps in the last 30 days, payment methods realistic (credit card 60%, PayPal 25%, Apple Pay 15%)."
expected:
  - "Column definitions are explicit with data types and generators named"
  - "Constraints and distributions are stated (e.g., payment method split 60/25/15)"
  - "CSV output is well-formed with headers and 100 valid rows"
  - "First 5–10 sample rows are shown inline so the user can validate structure"
  - "Quick-start instructions provided (e.g., how to load into pandas)"
  - "Data looks realistic: transaction IDs are unique, amounts are in the stated range, timestamps are in the last 30 days"
rubric:
  completeness: 0.35
  constraints_honored: 0.3
  usability: 0.25
  realism: 0.1
weight: 1.0
---

Happy path with clear domain, realistic constraints, and all sections required by the
Output Contract. Guards against vague or incomplete datasets and missing distribution guidance.

