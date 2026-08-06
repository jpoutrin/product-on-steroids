---
id: product-strategy-session-edge
skill: product-strategy-session
input:
  prompt: "Help me plan a 90-minute remote strategy session to pick our top platform bet for next year. Problem: our founder tends to dominate and the team defers to whatever she says, so past sessions ended with fake alignment. We don't use any formal decision model. Six people on a video call across three time zones."
  context: "Remote/hybrid format, a dominant HiPPO (founder), no agreed decision-rights model, and a history of false consensus. The decision (top platform bet) and timebox (90 min) are clear, but the decision model is not."
expected:
  - "Names a decision model up front (defaults to a single Decider vs input roles) since none exists, and states who the Decider is"
  - "Builds in facilitation techniques that surface independent input before the founder speaks (e.g. silent/anonymous write, dot-vote) to counter the HiPPO effect"
  - "Adapts the agenda for remote/multi-timezone constraints (async pre-work, tighter timeboxes, explicit turn-taking)"
  - "Includes a convergence plan with an explicit stall/escalation path and a mechanism to distinguish real commitment from deference"
  - "Timeboxes fit the 90-minute budget"
rubric:
  correctness: 0.3
  completeness: 0.3
  facilitation_safeguards: 0.4
weight: 1.0
---

Edge case: a politically-charged remote session with a dominant stakeholder and no decision model. Guards that the skill installs decision rights, sequences techniques so independent views surface before the HiPPO anchors the room, and plans for stall/escalation and false-consensus rather than assuming smooth convergence.
