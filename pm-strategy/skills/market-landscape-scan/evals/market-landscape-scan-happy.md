---
id: market-landscape-scan-happy
skill: market-landscape-scan
input:
  prompt: "We're a payroll company thinking about entering global HR/employer-of-record software. Give me a landscape scan of the space."
  context: "B2B, SMB and mid-market buyers, focus North America + EU. Seed players we've heard of: Deel, Rippling, Workday, Gusto. Orientation question: is there room to enter?"
expected:
  - "States the boundary up front — customer job, buyer type (B2B SMB/mid-market), geography (NA+EU), and exclusions"
  - "Groups players into 3–6 categories (e.g. incumbents, challengers, adjacent, emerging) with roles, not a flat list or per-rival teardown"
  - "Lists 3–6 trends each with a direction (rising/declining) and a 'so what' for a new entrant"
  - "Surfaces 2–4 white spaces framed as hypotheses to validate, each tied to a category or trend"
  - "Includes a text-rendered category map on two named axes positioning categories (not individual companies) and reads the empty quadrant"
  - "Ends with an orientation answer and one named deeper follow-up (e.g. competitor-analysis or market-sizing)"
rubric:
  correctness: 0.3
  completeness: 0.3
  categorization: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a clear boundary and seed players are enough to cluster categories,
read trends, and draw the map. Guards against flat player lists, per-rival
teardowns, and a scan with no map or no orientation takeaway.
