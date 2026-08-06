---
id: brainstorm-ideas-existing-adversarial
skill: brainstorm-ideas-existing
scenario: >
  Out-of-scope or contradictory request: User conflates "existing product ideas"
  with either (a) ideating for a new market/product entirely, or (b) designing
  experiments rather than raw ideas. Skill should recognize the boundary and
  decline, suggesting the appropriate alternative skill.
input:
  prompt: >
    We want to enter a completely new market—design software for architects.
    We've never built anything for that space before. Brainstorm ideas for our
    new product and how to test them.
  context: >
    (out of scope) We have a generic SaaS platform but no domain knowledge or
    product in architecture. Budget is $100K.
expected:
  - "Skill declines the request and explains why: this is a new product, not an existing-product improvement."
  - "Skill suggests the appropriate alternative: brainstorm-ideas-new (for new product ideation) and brainstorm-experiments-existing or a discovery research skill (for testing)."
  - "Skill clarifies the boundary: this skill is for improving or extending an existing product; new markets require market research and new-product ideation first."
rubric:
  correctness: >
    The skill correctly identifies the out-of-scope request (new product entry,
    not existing-product improvement). The suggested alternative skills are
    correct. The explanation of the boundary is clear: this skill assumes an
    existing product and customer segment; new-market entry is a different
    problem with different steps (market research, customer validation before
    building).
  completeness: >
    Skill explains what it cannot do (new-product ideation with no existing
    customer base) and offers a clear path forward (market research first, then
    brainstorm-ideas-new, then experiments). No vague deflection or partial
    ideation on out-of-scope input.
  actionability: >
    User understands why their request doesn't fit this skill. They know which
    skill to use next and why. The skill may offer brief guidance on the
    decision tree (e.g., "First, validate the market exists; second, sketch
    the new product; third, test assumptions") but reserves full ideation for
    the appropriate skill.
weight: 1.0
---

This scenario tests the skill's awareness of its own boundaries. It guards
against: scope creep (using the skill for new-product ideation when it's
designed for existing-product improvement), confused prioritization (mixing
idea generation with experiment design), and user confusion about which tool to
reach for. A strong output shows the skill can recognize when a request is
out of scope, explain why clearly, and route the user to the correct tool.
