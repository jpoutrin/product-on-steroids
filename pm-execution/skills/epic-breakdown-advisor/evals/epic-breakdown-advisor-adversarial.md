---
id: epic-breakdown-advisor-adversarial
skill: epic-breakdown-advisor
input:
  prompt: "Just give me 10 user stories for the AI features epic."
  context: |
    No epic goal stated. No target user specified. No success metric. No team context.
    User is pressing for an immediate list of stories and has explicitly said
    "don't ask me questions, just generate the stories."
expected:
  - "Does NOT silently generate 10 generic stories without clarifying the epic goal and target user"
  - "Explains why proceeding without an epic goal and target user would produce a story list that cannot be validated or sequenced"
  - "Asks for at minimum: the epic goal/outcome, the target user, and one piece of context about the team or delivery constraint"
  - "If the user continues to refuse all clarification, the skill generates a clearly labeled PROVISIONAL breakdown with explicit assumptions stated upfront and a warning that it must be validated before use"
  - "Does not treat 'AI features' as a single well-defined epic — calls out that it describes a theme, not an epic with a stated outcome"
rubric:
  scoping_discipline: 0.40
  clarification_quality: 0.30
  fallback_quality: 0.20
  completeness: 0.10
weight: 1.0
---

Adversarial: a vague, pressured request with no epic context and explicit
resistance to clarification. Guards against the most common failure mode —
producing a generic, ungrounded story list that looks useful but cannot be
sequenced, sized, or validated because the epic's goal and user were never
defined. Also guards against the skill refusing entirely when the user won't
cooperate: a labeled provisional output is better than silence.
