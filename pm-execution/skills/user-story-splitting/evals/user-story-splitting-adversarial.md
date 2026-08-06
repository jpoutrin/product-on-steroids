---
id: user-story-splitting-adversarial
skill: user-story-splitting
input:
  prompt: "Split this story into frontend, backend, and database tasks: As a user I want to reset my password so that I can regain access to my account."
  context: "Developer is asking for a horizontal (technical-layer) split explicitly: Story 1 = UI form, Story 2 = API endpoint, Story 3 = DB schema update. Team uses story points on user stories, not tasks."
expected:
  - "Refuses to produce horizontal (technical-layer) child stories — does NOT output 'Story 1: UI form', 'Story 2: API endpoint', 'Story 3: DB schema'"
  - "Explains clearly why technical-layer splits violate INVEST (layers are not independently valuable or demonstrable to stakeholders)"
  - "Proposes a value-vertical split instead — e.g., by rule variation (happy path vs. edge cases like expired token, unknown email) or defers non-functional enhancements (rate-limiting, audit logging) as separate stories"
  - "Each child story in the corrected split is expressed as 'As a … I want … so that …' with testable ACs"
  - "Acknowledges that the technical sub-tasks (UI, API, DB) become implementation tasks within each story, not separate stories"
rubric:
  refusal_quality: 0.40
  correctness: 0.30
  invest_compliance: 0.20
  completeness: 0.10
weight: 1.0
---

Adversarial: the developer explicitly requests a horizontal technical-layer split
(UI / API / DB). This is the single most common story-splitting antipattern. The
skill must firmly decline the horizontal split, explain why it breaks INVEST, and
produce a value-vertical alternative. Guards against the skill simply complying
with a misguided request because the user stated a preference.
