---
id: north-star-metric-edge
skill: north-star-metric
input:
  prompt: "Our marketplace's North Star should be GMV, right? Confirm and give input metrics."
  context: "Two-sided marketplace connecting local service pros and homeowners. GMV is the number the board watches. No vision statement provided."
expected:
  - "Classifies the business game as Transaction"
  - "Rejects GMV as the North Star because it is revenue-like and fails the customer-centric criterion"
  - "Proposes one customer-centric transaction metric (e.g. completed bookings / successful matches per period) with a definition"
  - "Runs the 7-criteria validation showing why the value-based metric passes where GMV fails"
  - "Flags the missing vision as an assumption when scoring vision-alignment"
  - "Gives 3-5 input metrics that lead the chosen NSM"
rubric:
  correctness: 0.35
  customer_centric: 0.3
  completeness: 0.2
  assumptions_explicit: 0.15
weight: 1.0
---

Edge: the obvious, board-favored metric (GMV) is a revenue proxy that violates the
customer-centric criterion. The skill must resist confirmation bias, pick a
value-based transaction metric, and justify it via the 7 criteria — while flagging
the absent vision rather than inventing one.
