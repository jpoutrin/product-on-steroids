---
id: positioning-statement-happy
skill: positioning-statement
input:
  prompt: "Write a positioning statement for our product."
  context: |
    Product: Observe
    What it does: Engineering analytics platform that shows team-level deployment
    frequency, lead time, and change failure rate pulled automatically from
    GitHub, GitLab, and Jira — no code instrumentation required.
    Target customer: VP Engineering or Director of Engineering at a SaaS company
    with 50–500 engineers who is under pressure from the CTO to improve
    deployment velocity without adding headcount.
    Key differentiator: zero-instrumentation setup (connects in under one day)
    versus competitors (LinearB, Jellyfish) that require weeks of integration
    work and dedicated DevOps effort.
    Chosen positioning angle: "The DORA-metrics platform that works out of the
    box" — own the 'zero-instrumentation' category within engineering analytics.
    Competitors named: LinearB, Jellyfish.
expected:
  - "Positioning statement names VP Engineering or Director of Engineering as the target customer (specific role, not 'engineering teams')"
  - "Category declared as engineering analytics (or equivalent) — a single named category"
  - "Key benefit is outcome-oriented (deployment velocity, DORA metrics, performance insight) not feature-oriented"
  - "Reason to believe is concrete: references the zero-instrumentation / sub-one-day setup claim specifically"
  - "Completed statement fits in one sentence"
  - "Tagline is 3–7 words and intelligible standalone"
  - "Rationale names at least one competitor (LinearB or Jellyfish) and explains why this frame beats them"
  - "Three test questions cover distinct dimensions: comprehension, differentiation, purchase relevance"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy path: all required inputs are present and unambiguous. Guards against the
skill producing a vague, jargon-heavy statement when clean inputs are provided.
The ICP is specific, the differentiator is concrete, and two named competitors
exist — so the reason-to-believe and rationale should be sharp and verifiable.
The eval checks that the skill delivers a crisp, paste-ready artifact rather than
a workshop-style exploration.
