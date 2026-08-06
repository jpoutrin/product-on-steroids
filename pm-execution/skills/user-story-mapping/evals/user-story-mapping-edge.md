---
id: user-story-mapping-edge
skill: user-story-mapping
input:
  prompt: "Map out the user story map for our password reset feature."
  context: >
    No existing stories provided. Single narrow feature. Primary user: an existing
    app user who forgot their password. Target: ship in one release. Team has not
    specified any stories yet.
expected:
  - "Skill derives stories from the journey description rather than refusing or asking for a pre-existing list"
  - "Backbone still reflects the user journey steps (e.g. Request Reset, Receive Email, Set New Password, Confirm Login)"
  - "Walking skeleton covers the minimal end-to-end reset flow"
  - "Output notes explicitly that stories were derived from the journey, not provided by the user"
  - "With only one release, deferred section captures nice-to-haves (e.g. magic link, security alerts)"
  - "Map is appropriately compact — not padded with fictional stories to fill a template"
rubric:
  story_derivation: 0.30
  backbone_quality: 0.25
  completeness: 0.25
  scope_honesty: 0.20
weight: 1.0
---

Edge case: narrow single-feature scope with no input stories. Guards against the
skill refusing to produce output without a pre-existing backlog, and against
padding a shallow map with invented stories. Also tests that the skill scales
down gracefully — a compact map is correct here.
