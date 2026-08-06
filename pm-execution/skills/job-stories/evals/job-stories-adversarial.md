---
id: job-stories-adversarial
skill: job-stories
input:
  prompt: "Write user stories for our app for users who need to use it."
  context: "Generic feature request. Persona-centric language ('users'). No situations or outcomes."
expected:
  - "Skill reframes input from persona-centric to situation-centric (JTBD format)"
  - "Skill explicitly asks for or infers triggering situations"
  - "Stories avoid generic persona language; anchor on contexts instead"
  - "Each story has a clear outcome, not just a feature description"
  - "Acceptance criteria are testable, not subjective"
  - "Skill clarifies that 'users' is not sufficient context for job stories"
  - "Output distinguishes job stories from user stories (When vs. As a)"
rubric:
  jtbd_reframing: 0.35
  persona_to_situation: 0.35
  outcome_clarity: 0.2
  user_education: 0.1
weight: 0.7
---

Adversarial: vague, persona-centric input ("users who need to use it") that the skill must
reframe into situation-focused JTBD language. Guards against shallow, implementation-focused
stories and validates the skill's ability to educate about JTBD discipline.
