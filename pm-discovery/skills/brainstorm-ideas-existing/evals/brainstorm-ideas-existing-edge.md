---
id: brainstorm-ideas-existing-edge
skill: brainstorm-ideas-existing
scenario: >
  Sparse context with ambiguous objective: User mentions a productivity app but
  doesn't clearly define the problem or segment. Skill must ask clarifying
  questions before ideating, then proceed once context is provided. Guards
  against the skill ideating blindly on vague input.
input:
  prompt: >
    We have a productivity app and want to improve it. Can you brainstorm some
    ideas? We're thinking it should be more useful for teams, but I'm not sure
    which direction to go.
  context: >
    (minimal) The app currently has task management, note-taking, and a calendar.
    10K MAU, mostly freelancers and small agencies.
expected:
  - "Skill asks clarifying questions: target segment, current pain point, strategic objective, any research data."
  - "After clarification, ideation proceeds with all three perspectives represented."
  - "Top 5 ideas align with the refined objective (not generic productivity improvements)."
  - "Assumptions and feasibility tags are grounded in the product's current feature set."
rubric:
  correctness: >
    The skill does not ideate on vague input; it asks for product, segment,
    objective, and constraints. Once the user provides clarification (e.g.,
    "small agencies struggle to delegate tasks—we want better task assignment"),
    ideas are correct and specific to that refined objective. Ideas do not assume
    context the user didn't provide.
  completeness: >
    If proceeding after clarification, all three perspectives are represented.
    Prioritized ideas include name, description, reasoning, ≥2 assumptions, and
    feasibility/impact tags. No ideas remain generic or placeholder-like.
  actionability: >
    After clarification, ideas are specific to the product and segment (e.g.,
    "permission templates for small-agency task delegation" vs. "improve
    collaboration"). Feasibility tags reflect the current app's feature set. If
    ideas require cross-app integration (email, Slack), that constraint is called
    out.
weight: 1.0
---

This scenario tests the skill's judgment to recognize ambiguous input and ask
for clarification rather than guessing. It guards against: ideating on vague
requests, generic ideas that don't fit the product, and assumptions that ignore
the actual segment. A strong output shows the skill can:
(1) recognize when context is missing, (2) ask targeted clarifying questions,
(3) proceed once clarity is provided, and (4) ground the ideation in the
refined product context.
