---
id: jobs-to-be-done-happy
skill: jobs-to-be-done
input:
  prompt: "Map the jobs to be done for our core customer segment."
  context: >
    Customer segment: mid-level finance managers (controllers) at 50–500 person
    companies. Triggering situation: end-of-month close when they must reconcile
    team credit-card expenses against budget lines before the CFO review.
    Interview signals available — representative quotes: "I spend half a day
    chasing receipts from people who are travelling", "I'm always worried I'll
    miss something and get called out in the leadership meeting", "My CEO watches
    the expense report like a hawk — if it's messy it reflects on me".
expected:
  - "Names the customer segment and triggering situation explicitly (finance manager, month-end close)"
  - "Identifies the primary functional job as a verb-object phrase decoupled from any solution (e.g. reconcile expenses accurately before the CFO review)"
  - "Covers all three job types: functional, emotional, and social"
  - "Each job statement follows the canonical When/I want to/so I can format with all three clauses present"
  - "Metrics of success are expressed as customer-observable outcomes, not product features"
  - "Discovery signals section cites or references the provided interview quotes as confirming evidence"
  - "No solution or product feature is embedded inside any job statement"
rubric:
  correctness: 0.35
  completeness: 0.30
  format_conformance: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: rich interview signals provided for a clearly scoped segment. Guards
against the most common failure modes — outputting feature requests instead of
jobs, omitting emotional or social dimensions, and writing job statements that
lack the situation or outcome clause. All three job types should emerge cleanly
from the interview quotes.
