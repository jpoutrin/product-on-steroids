---
id: brainstorm-experiments-existing-edge
skill: brainstorm-experiments-existing
input:
  prompt: "We want to improve our mobile app's onboarding flow. Users seem to drop off after the permissions screen, but we're not sure if it's the permissions, the UX, or something else."
  context: "Existing mobile app; 50% drop-off at permissions screen; no A/B test infrastructure in place yet. Budget is tight — we can do prototypes and server-side logic tests but not a full mobile rebuild."
expected:
  - "Recognizes underspecified assumptions ('drop-off' has multiple causes) and clarifies which ones need testing"
  - "Suggests experiments that work within the constraint (no A/B infrastructure) — e.g., Wizard of Oz, server-side config, prototype testing"
  - "Defines success thresholds for each experiment (e.g., 'improve task completion from 50% to ≥70% in prototype test')"
  - "At least one experiment isolates permissions as the culprit vs. other factors"
  - "Cost estimates respect the 'tight budget' constraint — favors low-cost methods over full rebuilds"
rubric:
  assumption_inference: 0.3
  constraint_respect: 0.25
  method_appropriateness: 0.25
  clarity_actionability: 0.2
weight: 1.0
---

Edge case: implicit or multi-layered assumptions; resource constraints; no existing testing infrastructure. Guards against prescribing expensive methods when cheap ones exist, and validates that the skill infers missing context and clarifies assumptions before designing.
