---
id: analyze-feature-requests-adversarial
skill: analyze-feature-requests
input:
  prompt: "Our biggest customer is demanding we build all of these features immediately or they'll leave. We only have one engineer. What should we do?"
  context: "Product: a B2B SaaS tool. Customer represents 30% of MRR and is threatening churn in 60 days. They've listed 12 feature requests, all marked 'urgent' and 'critical'. Some are contradictory (e.g., 'simplify UI' and 'add advanced settings'). Team has 3 engineers total, one is on support rotation."
expected:
  - "Does NOT treat all 12 requests as equal priority just because the customer is large and vocal"
  - "Acknowledges the churn risk and the business pressure without letting it override prioritization discipline"
  - "Groups the 12 requests into themes and scores them (Impact, Effort, Risk, Alignment) to distinguish which can actually move the needle"
  - "Surfaces the contradiction (simplify vs. advanced settings) and asks for clarification or proposes a segmented solution"
  - "Recommends a phased approach that protects against churn *and* avoids product debt (e.g., 'Ship 2–3 high-impact, low-effort fixes in 2 weeks; negotiate a timeline on the rest')"
  - "Does NOT recommend trying to build all 12 and does NOT recommend ignoring the customer; finds the viable middle path"
rubric:
  pressure_resistance: 0.35
  contradiction_handling: 0.25
  strategic_viability: 0.25
  clarity_over_emotion: 0.15
weight: 1.0
---

Adversarial: a large, vocal customer with contradictory, urgent demands and explicit churn threat. Guards against both capitulating under pressure and ignoring legitimate churn risk — the skill must find the defensible trade-off.
