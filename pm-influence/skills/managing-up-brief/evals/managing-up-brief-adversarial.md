---
id: managing-up-brief-adversarial
skill: managing-up-brief
input:
  prompt: "Help me prep for my 1:1 with my manager next week."
  context: "No meeting purpose, no leader profile, no ask, no topic specified."
expected:
  - "Does NOT produce a generic brief with placeholder content"
  - "Asks for the meeting purpose before drafting — what decision, ask, or topic needs to be navigated"
  - "Asks for or infers the leader's role and known priorities before proceeding"
  - "If any brief is drafted, it is clearly marked as an example requiring the user to supply the missing inputs"
  - "Explains why the missing inputs matter — a brief without a desired outcome and leader lens is not useful preparation"
rubric:
  elicitation_discipline: 0.45
  refusal_of_generic_output: 0.30
  explanation_quality: 0.25
weight: 1.0
---

Adversarial: a completely underspecified request — no meeting purpose, no leader profile, no ask.
This is the most common failure mode: producing a generic five-section brief full of placeholders
that looks like output but provides no real preparation value. The skill must ask for the two
required inputs (meeting purpose, leader priorities) before drafting rather than generating a
content-free template and calling it a brief. Guards against output theater — the appearance of
prep without the substance.
