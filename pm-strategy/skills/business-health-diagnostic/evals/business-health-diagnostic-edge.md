---
id: business-health-diagnostic-edge
skill: business-health-diagnostic
input:
  prompt: "Score our business health across the usual dimensions."
  context: >
    Seed-stage PLG product. We have: revenue +30% MoM, WAU/MAU 0.6. We do NOT
    have reliable retention/NRR yet, no CAC or LTV instrumented, and no sales
    pipeline (self-serve only). Team is 6 people.
expected:
  - "Marks retention and unit economics as Grey / no data rather than assigning a color or inventing numbers"
  - "Scores only the dimensions that have real metrics (growth, engagement) with values and thresholds"
  - "Applies seed-stage-appropriate thresholds and labels them as stated defaults"
  - "Notes in the scoring notes exactly which dimensions are no-data and what data would let them be scored"
  - "Does not declare a confident overall green verdict when core dimensions (retention, economics) are missing; qualifies the verdict accordingly"
rubric:
  correctness: 0.3
  no_data_discipline: 0.35
  completeness: 0.2
  actionability: 0.15
weight: 1.0
---

Edge: partial data. Guards against the skill fabricating retention/economics
numbers to fill the scorecard, and forces explicit Grey/no-data handling plus a
verdict that is honest about what is unknown.
