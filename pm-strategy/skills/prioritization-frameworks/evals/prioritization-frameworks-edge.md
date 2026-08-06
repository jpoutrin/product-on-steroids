---
id: prioritization-frameworks-edge
skill: prioritization-frameworks
input:
  prompt: "We're an early team trying to decide which customer problems to tackle. We don't have analytics or reach numbers yet. How should we prioritize?"
  context: "Pre-PMF, ~8 candidate problems from user interviews. No quantitative reach or effort data. Some qualitative sense of which pains are worst."
expected:
  - "Does NOT force RICE, since reach/effort data is absent"
  - "Steers toward prioritizing problems/opportunities over solutions"
  - "Recommends Opportunity (Importance-vs-Satisfaction) Scoring or Value-vs-Effort as a fit for sparse data and a problem object"
  - "Names the specific data to gather (e.g. importance/satisfaction survey) that would unlock a more rigorous framework later"
  - "Names a primary pick and a fallback rather than leaving it open-ended"
rubric:
  fit_justification: 0.35
  correctness: 0.30
  data_awareness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge: sparse data and a customer-problem object. Guards against defaulting to the
heaviest framework (RICE) when its inputs don't exist, and rewards steering to a
problem-first, data-light method plus naming the data that unlocks a heavier one.
