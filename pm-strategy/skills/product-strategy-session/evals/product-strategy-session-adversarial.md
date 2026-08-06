---
id: product-strategy-session-adversarial
skill: product-strategy-session
input:
  prompt: "Set up a strategy meeting for my team. Just give me a full agenda now — I want to get everyone in a room to talk about our product strategy and get aligned."
  context: "No specific decision is named, no Decider identified, no timebox, and no participants/roles. 'Get aligned' is a discussion goal, not a decision."
expected:
  - "Refuses to hand over a decision-session agenda until the frame is elicited"
  - "Asks specifically for the concrete decision to reach, the Decider, the participants and their roles, and the available time"
  - "Explains why a session without a target decision and a decision owner becomes discussion theater / fake alignment"
  - "Does not fabricate a decision, invent participants, or emit a generic 'discuss then align' agenda that violates the Output Contract"
  - "Optionally offers to proceed once the missing frame inputs are supplied"
rubric:
  correctness: 0.4
  refusal_discipline: 0.4
  actionability: 0.2
weight: 1.0
---

Adversarial: a vague "let's talk strategy and align" request with no decision, no Decider, no roles, and no timebox, plus pressure to emit an agenda immediately. Guards that the skill elicits the required frame instead of producing a hollow, timebox-free, decision-free agenda that would fail its own Quality Bar.
