---
id: proto-persona-happy
skill: proto-persona
input:
  prompt: >
    We're kicking off a new B2B feature for our SaaS product: an AI-assisted
    contract review tool aimed at small legal teams inside mid-market companies.
    We have a kickoff doc with notes from our Head of Sales, Head of Customer
    Success, and our two founders. No user interviews yet. Can you build a
    proto-persona so we can align the team before discovery starts?
  context: >
    Kickoff notes indicate: target is in-house legal counsel or a "legal ops"
    role at companies of 200–1000 employees, likely frustrated by slow contract
    turnaround, probably uses email + Word/Google Docs today, wants to look
    competent to the business without needing a large headcount.
expected:
  - "Output carries a prominent [HYPOTHESIS — NOT VALIDATED] banner or equivalent disclaimer"
  - "Every section of Goals, Frustrations, and Behaviors is labeled [ASSUMED]"
  - "Quote is labeled [INVENTED]"
  - "Validation Plan contains at least 3 specific, actionable research steps (not vague)"
  - "At least one explicit red-flag result is stated in the Validation Plan"
  - "No claim in the artifact is presented as validated fact"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy-path scenario: a team at the very start of discovery, with multi-stakeholder
kickoff notes but zero user research. Guards the core output quality — that the
skill produces a well-structured, fully labeled proto-persona card with a concrete
Validation Plan rather than a polished persona that elides its hypothetical nature.
The key risk this eval guards against is producing a plausible-sounding persona
that a team might mistake for a validated deliverable.
