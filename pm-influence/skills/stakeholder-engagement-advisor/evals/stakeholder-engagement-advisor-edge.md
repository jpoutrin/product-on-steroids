---
id: stakeholder-engagement-advisor-edge
skill: stakeholder-engagement-advisor
input:
  prompt: "We need a stakeholder engagement plan for our new data platform migration."
  context: |
    Initiative: migrate from legacy on-prem data warehouse to a cloud data platform.
    Timeline: 6 months, executive approval needed in 4 weeks.
    Stakeholders provided with minimal detail:
    - CTO (high influence)
    - Head of Analytics (medium influence)
    - Regional Sales Director EMEA (medium influence)
    No stance, concerns, or communication preferences given for any stakeholder.
expected:
  - "Surfaces the missing stance and concern information explicitly, stating working assumptions for each stakeholder rather than silently guessing"
  - "Produces a usable engagement plan despite sparse input, with clearly labeled assumptions"
  - "Infers plausible concerns per role (e.g., CTO: technical risk and cost; Head of Analytics: data continuity; Sales Director: disruption to reporting)"
  - "Flags that the plan should be revised once actual stances and preferences are confirmed"
  - "Sequencing Map still provides a logical order with rationale even when stance is assumed"
  - "Does not refuse to produce a plan — it produces a working draft while making uncertainty explicit"
rubric:
  assumption_transparency: 0.35
  correctness: 0.30
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge case: sparse stakeholder input with no stance, concerns, or communication
preferences. Guards against two failure modes: (1) silently guessing and
presenting assumptions as facts, and (2) refusing to produce anything and
demanding perfect input before proceeding.
