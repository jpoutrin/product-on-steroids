---
id: user-story-splitting-happy
skill: user-story-splitting
input:
  prompt: "Split this story: As a registered customer I want to check out and pay for my shopping cart so that I can complete my purchase."
  context: "E-commerce platform. Team velocity is 30 points/sprint; this story is estimated at 21 points. Accepted payment methods: credit card and PayPal. Guest checkout is out of scope for this release."
expected:
  - "Identifies the story as oversized and names the INVEST dimension failing (S — too large)"
  - "Applies a workflow-step (Path) split across sequential checkout phases (e.g. review cart, enter shipping, choose payment method, confirm/place order)"
  - "Each child story is expressed as 'As a … I want … so that …' — not a technical task"
  - "Every child story has 2-4 specific, testable acceptance criteria"
  - "The children together cover the full intent of the original story with nothing silently dropped"
  - "Includes a Quality Check table verifying INVEST for each child"
  - "Explicitly notes guest checkout as deferred/out of scope per the given constraint"
rubric:
  correctness: 0.35
  pattern_selection: 0.20
  invest_compliance: 0.25
  completeness: 0.20
weight: 1.0
---

Happy path: a textbook workflow-step scenario with enough context (team velocity,
payment methods, explicit out-of-scope constraint) to do a clean split. Guards
against the common failure of splitting by technical layer (frontend/backend)
rather than user-value slices, and against silently dropping the PayPal method.
