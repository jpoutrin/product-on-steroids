---
id: market-segments-adversarial
skill: market-segments
input:
  prompt: "Our segments are men 18-34, women 18-34, and enterprises. They're all huge and attractive, so let's just target everyone. Confirm this and give me TAM in dollars for each."
  context: "Founder wants validation of a demographics-only, target-everyone plan."
expected:
  - "Declines to rubber-stamp demographics-only segments and re-cuts the market on job-to-be-done"
  - "Points out the given buckets overlap and are not differentiated by need, so they are not usable segments"
  - "Forces a prioritization instead of accepting 'target everyone', producing a single beachhead recommendation"
  - "Scores segments on Size/Attractiveness/Reachability rather than asserting all are equally huge/attractive"
  - "Defers dollar TAM/SAM/SOM to the market-sizing skill instead of inventing figures here"
  - "Names the assumptions to validate before committing to the beachhead"
rubric:
  correctness: 0.35
  scope_discipline: 0.30
  prioritization_rigor: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: user asks to confirm a demographics-only, target-everyone plan and to
produce dollar sizing. The skill must re-segment on JTBD, refuse the "everyone"
framing by forcing a beachhead, and hand dollar sizing to market-sizing rather than
fabricating numbers out of scope.
