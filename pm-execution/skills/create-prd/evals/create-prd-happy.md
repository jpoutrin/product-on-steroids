---
id: create-prd-happy
skill: create-prd
input:
  prompt: "Write a PRD for a mobile checkout redesign on our B2B SaaS platform."
  context: |
    Product: SupplyFlow (B2B procurement SaaS, EU market).
    Problem: Mobile checkout abandonment is 58%; desktop is 31%. Root cause: 4-field address
    form and no saved-payment option on mobile.
    Target users: procurement managers at EU SMBs (50–500 employees) who approve
    purchases on the go.
    Success target: reduce mobile abandonment to ≤ 38% within 2 quarters.
    Release constraint: 2-engineer team; MVP in 6 weeks.
expected:
  - "All eight sections present (Summary, Contacts, Background, Objective, Market Segment, Value Proposition, Solution, Release)"
  - "Objective includes at least one SMART key result with a numeric target and timeframe"
  - "Segment is framed by job-to-be-done or pain (approving purchases on mobile), not demographics alone"
  - "Solution lists Key Features as capability statements with explicit v1 scope boundaries"
  - "Assumptions subsection contains at least one labeled belief to validate"
  - "Release section uses relative timeframes and states an MVP scope boundary"
  - "Language is clear and jargon-free"
rubric:
  correctness: 0.35
  completeness: 0.30
  actionability: 0.20
  clarity: 0.15
weight: 1.0
---

Happy path: all required inputs are provided (problem, segment, metric, constraint). Guards
against missing sections, vague objectives without measurable targets, and features described
without scope boundaries. Also verifies the skill does not touch PRD lifecycle status — that
belongs to Forge.
