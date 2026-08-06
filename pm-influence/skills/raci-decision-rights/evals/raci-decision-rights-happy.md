---
id: raci-decision-rights-happy
skill: raci-decision-rights
input:
  prompt: "We're spinning up a new checkout feature team. I need a RACI for the
    key decisions this team will own. Roles involved: PM, Eng Lead, Design Lead,
    Data Analyst, VP Product, Legal. Main decision areas: roadmap, engineering
    choices, UX, A/B test go/no-go, pricing experiments, launch readiness."
  context: "Mid-stage B2C SaaS, 50-person company. Team is new and roles are clear
    but accountability is not. Recent friction: PM and Eng Lead both tried to make
    the launch readiness call and it got escalated to VP Product."
expected:
  - "Produces a matrix table with decisions as rows and the six named roles as columns"
  - "Every decision row has exactly one A (no shared accountabilities)"
  - "Every decision row has at least one R"
  - "Launch readiness row assigns A to a single role (resolving the stated friction),
    with a Decision Note explaining the reasoning"
  - "Pricing experiments row C's Legal given the regulatory surface"
  - "Role Glossary defines all six roles"
  - "Operating Cadence names a review schedule and an owner"
  - "Gaps & Risks section is present, even if empty"
rubric:
  single_accountability_rule: 0.35
  completeness: 0.25
  decision_notes_quality: 0.20
  actionability: 0.20
weight: 1.0
---

Happy path: a team with well-defined roles and a concrete friction point (shared
launch readiness call). Guards against shared-A assignments and missing Role
Glossary entries. The launch readiness friction is a deliberate test that the skill
uses the single-A rule to resolve with an explanatory note.
