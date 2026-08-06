---
id: problem-statement-adversarial
skill: problem-statement
input:
  prompt: "Write a problem statement: users need a real-time notification centre with customisable alert rules and a digest email feature."
  context: >
    The PM has jumped straight to a feature description without establishing a
    problem. No user segment, no evidence of an unmet need, and no impact data
    are provided. The user is framing a solution as if it were a problem and
    wants the skill to rubber-stamp it as a problem statement.
expected:
  - "Does NOT produce a problem statement that treats the feature description as the problem"
  - "Identifies that the input is solution language, not a problem description"
  - "Asks for or proposes the missing elements: who is affected, what problem they face, and what evidence exists"
  - "If it proceeds to draft a statement, the draft frames a plausible underlying problem (e.g., users miss time-sensitive updates) — not the requested features"
  - "The draft does not mention 'notification centre', 'customisable alert rules', or 'digest email' as part of the problem"
  - "Explains why a solution-first problem statement is harmful (it forecloses better solutions)"
rubric:
  reframing_discipline: 0.45
  correctness: 0.25
  no_solution_language: 0.20
  actionability: 0.10
weight: 1.0
---

Adversarial: a solution disguised as a problem statement request. Guards against
the most common failure mode in PM practice — accepting feature requests as
problem definitions, which locks teams into a prescribed solution before the
problem space has been validated and before alternative solutions have been
considered.
