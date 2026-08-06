---
id: raci-decision-rights-edge
skill: raci-decision-rights
input:
  prompt: "We're a 6-person startup. I'm the founding PM and also do growth. Our
    CTO does both engineering and data. We have one designer. We occasionally loop
    in our CEO for major calls. Build me a RACI for product decisions."
  context: "Pre-series-A SaaS. No dedicated Legal or Finance — CEO handles those.
    The team is small so we want to keep the consulted set minimal and avoid
    over-engineering the process."
expected:
  - "Consolidates overlapping roles into canonical role names (e.g., PM/Growth as
    PM, CTO/Data as CTO) with clear notes in the Role Glossary"
  - "Keeps the C set thin — flags when a role accumulates too many C entries given
    team size"
  - "CEO is Accountable only for decisions that genuinely require it (major pivots,
    large spend); does not over-assign CEO as A"
  - "Every row still has exactly one A — no 'TBD' or 'founder team' accountabilities"
  - "Includes a Gaps & Risks note about missing specialized roles (Legal, Finance)
    and the risk of a CEO bottleneck"
  - "Operating Cadence is appropriately lightweight for a small startup"
rubric:
  role_consolidation: 0.30
  single_accountability_rule: 0.30
  startup_calibration: 0.20
  gaps_surfaced: 0.20
weight: 1.0
---

Edge case: role overlap and thin team. The skill must handle founders wearing
multiple hats without creating ambiguous or merged-role accountabilities. Guards
against the common startup failure of assigning everything to the CEO as A, which
creates a decision bottleneck — and against the opposite failure of leaving A as
TBD because the org is flat.
