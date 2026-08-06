---
id: market-segments-happy
skill: market-segments
input:
  prompt: "Segment the market for our B2B expense-management tool and tell us which segment to go after first."
  context: "Interview notes attached: freelancers dread quarterly VAT; small agencies chase receipts by email; mid-market finance teams want approval workflows. We sell via accounting-software marketplaces."
expected:
  - "Defines 3-5 distinct, non-overlapping segments each anchored on a job-to-be-done, not demographics"
  - "Each segment names its JTBD, an acute pain/trigger, characteristics, and current alternative"
  - "Scores every segment on Size, Attractiveness, and Reachability on a stated scale with a one-line justification per score"
  - "Recommends a single beachhead segment and justifies it against the runners-up and an expansion foothold"
  - "Ties reachability to the accounting-marketplace channel the company owns"
  - "Names the 1-2 riskiest assumptions behind the pick with a validation step"
rubric:
  correctness: 0.35
  completeness: 0.25
  prioritization_rigor: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: rich interview notes support a real JTBD-based cut, a differentiated
scoring pass, and a defensible beachhead. Guards against demographic-only segments
and undifferentiated "all attractive" scoring.
