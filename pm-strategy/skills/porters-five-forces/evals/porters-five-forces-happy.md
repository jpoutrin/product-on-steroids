---
id: porters-five-forces-happy
skill: porters-five-forces
input:
  prompt: "Run a Porter's Five Forces analysis on the B2B e-signature SaaS industry for EU mid-market companies. We're an incumbent with ~8% share. Cloud infra is cheap, there's no strong IP moat, buyers integrate the tool into their contract workflows, and there are a handful of large players plus several funded startups."
  context: "Well-scoped: category, customer type, geography, and vantage point (named incumbent) all given, with enough structural detail to rate every force."
expected:
  - "Rates all five forces (rivalry, new entrants, substitutes, buyer power, supplier power) as Low/Med/High"
  - "Backs each rating with specific evidence from the prompt (e.g. cheap cloud infra + no IP moat → higher entrant threat; workflow integration → higher switching costs / lower buyer power)"
  - "Assigns a trend (strengthening/weakening/stable) to each force"
  - "Reaches an overall attractiveness verdict that follows from the ratings by weighing dominant forces, not a simple average"
  - "Gives prioritized strategic implications tied to the highest-pressure forces (e.g. deepen workflow lock-in to counter easy entry)"
  - "States the incumbent vantage point and stays on industry structure, not a rival-by-rival teardown"
rubric:
  correctness: 0.35
  completeness: 0.30
  actionability: 0.20
  evidence_quality: 0.15
weight: 1.0
---

Happy path: a fully scoped industry with enough structural detail to rate all
five forces and reach a defensible verdict. Guards against skipped forces,
evidence-free ratings, and a verdict that doesn't follow from the ratings.
