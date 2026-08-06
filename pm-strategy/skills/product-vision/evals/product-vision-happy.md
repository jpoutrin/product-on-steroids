---
id: product-vision-happy
skill: product-vision
input:
  prompt: "Help us craft a product vision for our small-business invoicing app."
  context: "B2B fintech. 40k active merchants. Core problem: small businesses wait weeks to get paid and spend hours chasing invoices. Values: fairness, simplicity, momentum for small teams."
expected:
  - "A single memorable, jargon-free sentence as the recommended vision statement"
  - "3–5 distinct one-sentence options across different angles before the recommendation"
  - "Rationale explicitly covering all three tests: inspiring, achievable, emotional"
  - "Alignment to the stated company values and the market opportunity"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy path: clear product, real customer, well-defined problem, and stated values.
Guards that the skill produces a memorable one-sentence vision, offers a deliberate
set of options, and justifies the pick on inspiring/achievable/emotional rather
than defaulting to a single buzzword sentence.
