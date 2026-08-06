---
id: epic-breakdown-advisor-happy
skill: epic-breakdown-advisor
input:
  prompt: "Help me break down our Shipment Tracking epic into user stories and delivery phases."
  context: |
    Epic goal: logistics managers can track every shipment in real time from a single dashboard.
    Target user: logistics manager at a mid-size e-commerce company.
    Success metric: 80% of managers check the dashboard daily within 60 days of launch.
    Team: 2 backend, 2 frontend engineers, 1 QA; all familiar with the existing order-management system.
    Constraint: a partner API for carrier data must be integrated (contract signed, docs available).
    No hard deadline; next quarterly review is in 10 weeks.
expected:
  - "Recommends vertical slicing (or justifies an alternative with ≥ 2 sentences)"
  - "Produces ≥ 5 user stories each in As a … I want … so that … format"
  - "Every story has at least one concrete, testable acceptance criterion"
  - "Defines 2–4 milestones that mark user-visible value (not internal technical gates)"
  - "Groups stories into ≤ 3 delivery phases with a rationale for each phase boundary"
  - "Calls out the carrier API integration as a sequencing risk or dependency"
  - "Size estimates (XS/S/M/L) present on every story"
rubric:
  strategy_fit: 0.20
  story_quality: 0.30
  milestone_and_phases: 0.25
  risk_identification: 0.15
  completeness: 0.10
weight: 1.0
---

Happy path: a well-specified B2B SaaS epic with clear goal, user, team context,
and one known dependency. Guards against shallow output (layer-based decomposition,
missing ACs, vague milestones) and validates that the skill recommends vertical
slicing for a well-understood domain with an existing system to integrate into.
