---
id: positioning-statement-edge
skill: positioning-statement
input:
  prompt: "Help us write a positioning statement. We serve both developers and CTOs."
  context: |
    Product: Layerform
    What it does: Infrastructure-as-code platform that lets developers spin up
    isolated cloud environments in minutes using reusable layer definitions —
    so they can test features without blocking each other on shared staging.
    Buyer personas:
      - Developer (end user): values speed, self-service, no DevOps ticket queue.
      - CTO / VP Eng (economic buyer): values cost control, environment sprawl
        reduction, and compliance auditability.
    The company has been messaging to both audiences simultaneously and is
    confusing prospects. They have chosen to anchor the positioning on the
    developer (end user) for the primary statement, while acknowledging the
    economic buyer in the sales process separately.
    Chosen angle: Own "ephemeral environments" category for developers at
    growth-stage startups (50–300 devs) where sharing a staging environment is
    the #1 bottleneck to shipping.
    Competitors: Okteto, Namespace.so, internal Terraform scripts.
expected:
  - "Skill commits to a single primary target customer (developer) — does not hedge by writing a compound statement like 'for developers and CTOs'"
  - "Positioning statement names the developer persona as [target customer], not both personas"
  - "Category is declared (ephemeral environments or equivalent) rather than a generic 'platform' or 'tool'"
  - "Key benefit addresses developer pain (unblocked, self-service, fast) not CTO pain"
  - "Rationale acknowledges the multi-persona tension and explicitly explains the primary persona choice"
  - "Tagline is 3–7 words and would resonate with a developer, not a CTO"
  - "Three test questions address distinct dimensions: comprehension, differentiation, purchase relevance"
rubric:
  correctness: 0.45
  completeness: 0.25
  actionability: 0.30
weight: 1.0
---

Edge case: platform product with two legitimate buyer personas. The user says
"we serve both" — a common trap that produces diluted positioning. The skill
must force the primary persona choice (already made by the team in the context)
and write a statement anchored on that persona, not attempt a composite statement
that tries to satisfy both audiences simultaneously. The rationale section is
where the multi-persona tension is explicitly resolved.
