---
id: press-release-happy
skill: press-release
input:
  prompt: "Write a Working Backwards press release and FAQ for a new tool that lets small medical clinics get insurance claims paid the next day instead of waiting a month."
  context: "Customer: solo and small (1-3 person) US medical practices. Problem today: 30-day reimbursement waits and manual resubmission of rejected claims. Name idea: Nimbus. Rough price idea unknown."
expected:
  - "Future-dated, customer-facing release written as if the product already exists and is loved"
  - "Names the specific customer (small US medical practices) and their concrete problem (slow, manual insurance reimbursement)"
  - "Includes a leader quote and a named, plausible customer quote with a real before/after benefit"
  - "Has a clear how-to-get-started step and both an External and an Internal FAQ"
  - "Internal FAQ names the biggest risk and how they know customers want this; unknown price is marked [assumption], not invented as fact"
  - "Ends with a plain go / refine / no-go read and the next thing to validate"
rubric:
  correctness: 0.35
  completeness: 0.3
  assumptions_explicit: 0.2
  actionability: 0.15
weight: 1.0
---

Happy path: a well-specified B2B idea with a clear customer and problem. Guards
against skipping the FAQ, missing the customer quote, or inventing pricing that
was never given instead of labeling it an assumption.
