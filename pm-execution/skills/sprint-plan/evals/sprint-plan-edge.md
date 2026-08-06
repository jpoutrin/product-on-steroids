---
id: sprint-plan-edge
skill: sprint-plan
input:
  prompt: "Help us plan sprint 8. This is only our third sprint, so velocity is uncertain."
  context: "3-person team. Last 2 sprints: 12 and 16 points. This sprint: 2 devs out sick first week, 1 person on-call half the sprint. Backlog has 3 high-uncertainty stories; the other 5 are well-defined. 2 stories depend on a third-party API team."
expected:
  - "Capacity calculation flags the sparse velocity history (asks for assumptions or uses a conservative range)."
  - "Availability adjustments are explicit: accounts for sick leave and on-call burden, with reasoning."
  - "High-uncertainty stories are flagged with risks (complexity, estimation confidence)."
  - "Mitigations for each risk are concrete: pair programming, pre-spike, scope reduction, or story swaps."
  - "External dependencies (API team) are flagged with owner and an escalation mitigation if the API timeline slips."
  - "Committed capacity is conservative relative to capacity (e.g., uses lower velocity estimate)."
rubric:
  correctness: 0.3
  capacity_reasoning: 0.3
  risk_identification: 0.25
  actionability: 0.15
weight: 1.0
---

Sparse velocity, high uncertainty, tight team capacity, external dependencies. Guards against over-committing despite risk signals and false precision on capacity.

