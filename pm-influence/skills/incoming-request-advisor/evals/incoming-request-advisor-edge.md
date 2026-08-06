---
id: incoming-request-advisor-edge
skill: incoming-request-advisor
input:
  prompt: "Our CPO just pinged me directly asking why we haven't built SSO yet.
    Three of our largest customers have asked for it, and she heard about it in
    a board meeting. She wants an answer by end of week."
  context: "SSO is not on the current roadmap. It was deprioritized six months
    ago due to engineering complexity. The CPO is two levels above me and has
    historically overridden roadmap decisions when she feels strongly. Current
    priority is a self-serve onboarding flow committed for next month."
expected:
  - "Disposition is not simply 'Accept' due to seniority pressure alone — must show strategic reasoning"
  - "Strategic rationale explicitly names the committed self-serve onboarding delivery risk if SSO is accepted now"
  - "Disposition acknowledges escalation risk without abandoning the principled position"
  - "Draft reply is more formal in tone than a peer reply, but not deferential to the point of capitulation"
  - "Draft reply proposes a structured path (e.g., brief call, written options memo) rather than a flat yes or no"
  - "Bridge-Preservation Notes address the reputational dimension of a CPO request"
rubric:
  correctness: 0.40
  tone_and_empathy: 0.25
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge case: seniority gradient plus political pressure. Tests whether the skill
holds a principled position when the requester outranks the PM, instead of
capitulating or rubber-stamping. The correct disposition is Conditionally Accept
or Redirect (propose an options memo), not a flat Accept or flat Decline.
