---
id: epic-breakdown-advisor-edge
skill: epic-breakdown-advisor
input:
  prompt: "Break down our new Payments Platform epic. We're building this from scratch."
  context: |
    Epic goal: replace a third-party payment processor with an in-house payments platform
    supporting card, bank transfer, and wallet methods.
    Target user: end customers of a marketplace; internal finance ops team.
    Success metric: 99.9% payment success rate; < 2 s checkout latency.
    Team: 3 backend engineers new to payments domain, 1 security specialist, 1 QA.
    Constraints: PCI-DSS compliance required before processing real cards; hard deadline
    in 16 weeks tied to a contract expiry with the current processor.
    No existing in-house payment code — greenfield.
expected:
  - "Recommends walking skeleton (or risk-first) and explains why greenfield + compliance risk warrants it over vertical slicing"
  - "Places PCI-DSS compliance gate and security hardening as early milestones, not deferred to a later phase"
  - "Identifies integration/compliance uncertainty as the primary sequencing risk"
  - "Does not produce a layer-based decomposition (Backend API, Frontend, QA) as the story structure"
  - "Milestone ladder flags which milestone is the earliest point real payment processing can be validated end-to-end"
  - "Story list covers at least card payment, bank transfer, and error handling as separate stories"
  - "Flags any L-sized stories (e.g., PCI audit prep) as candidates for further splitting"
rubric:
  strategy_fit: 0.30
  risk_identification: 0.25
  story_quality: 0.25
  milestone_and_phases: 0.20
weight: 1.0
---

Edge case: a greenfield, compliance-heavy epic with a hard deadline and a team
new to the domain. Guards against the skill defaulting to vertical slicing when
walking skeleton or risk-first is clearly superior, and against burying the
compliance gate in a late phase when it should anchor the milestone ladder.
