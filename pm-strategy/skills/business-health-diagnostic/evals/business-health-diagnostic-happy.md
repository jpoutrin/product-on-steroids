---
id: business-health-diagnostic-happy
skill: business-health-diagnostic
input:
  prompt: "Give me a health diagnostic for our SaaS product this quarter."
  context: >
    Growth-stage B2B SaaS. Revenue +14% MoM (up from +11%). NRR 82% (down from
    91%). LTV:CAC 2.1 (flat). WAU/MAU 0.55 (up). Pipeline coverage 3.2x (flat).
    Engineering on-time delivery 78% (down). No customer benchmark provided.
expected:
  - "Produces a per-dimension RAG scorecard table with the actual metric value and the threshold applied for each row"
  - "Scores growth green but sets the OVERALL verdict to amber (not green) because retention is red, and states growth is masking the retention leak"
  - "Marks retention red against a stated threshold (e.g. NRR <90% red) and shows the downward trend"
  - "Labels thresholds as stated defaults since no customer benchmark was provided"
  - "Ranks 2-4 top risks, each tied to its triggering metric value and a one-line why-it-matters, led by the retention/NRR drop"
  - "Names 2-3 focus areas tied to the ranked risks, not a generic to-do list"
rubric:
  correctness: 0.35
  completeness: 0.25
  threshold_discipline: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a full metric set where one strong dimension (growth) masks a red one
(retention). Guards against a naive "green because growth is up" rollup and against
coloring dimensions without stating thresholds.
