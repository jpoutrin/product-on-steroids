---
id: pricing-strategy-happy
skill: pricing-strategy
input:
  prompt: "Set the price for our B2B analytics workspace tool."
  context: "Alternative is 6 analyst-hours/month at €80/hr. Van Westendorp on 140 responses: cheap €39, expensive €99. Value metric already chosen: per workspace. Cost floor €12/mo."
expected:
  - "Names value-based as the pricing approach and justifies it against the quantified alternative (€480/mo of analyst effort)"
  - "Reports the Van Westendorp band and derives an Optimal Price Point from the €39/€99 responses"
  - "Recommends a specific price point per workspace inside the WTP band"
  - "Checks the price clears the €12/mo cost floor and positions it vs competitors with a reason"
  - "Specifies an anchor and an annual/volume discount"
  - "Lists numbered assumptions with confidence levels and a validation test"
rubric:
  correctness: 0.35
  completeness: 0.25
  assumptions_explicit: 0.2
  actionability: 0.2
weight: 1.0
---

Happy path: full inputs (value anchor, survey data, value metric, cost floor)
support a real value-based price with a Van Westendorp band. Guards against
skipping the WTP method or ignoring the cost floor.
