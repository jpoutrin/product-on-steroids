---
id: positioning-workshop-adversarial
skill: positioning-workshop
input:
  prompt: "Just give me the positioning statement. We know our product — skip the exercises."
  context: |
    Product: Vaultwise, a document management tool for legal teams.
    The PM is asking Claude to skip the six exercises and immediately produce a finished
    positioning statement. No competitive alternatives, attributes, or value outputs have
    been generated. The team is under time pressure and believes the exercises are unnecessary.
expected:
  - "Does NOT produce a positioning statement without completing the exercises first"
  - "Explains clearly why skipping the exercises produces a statement that is ungrounded and likely wrong"
  - "Offers a compressed but still complete version of the workshop — not an outright refusal"
  - "Starts Exercise 1 and asks for competitive alternatives before proceeding"
  - "If the team provides only minimal input, acknowledges the gaps rather than filling them with assumptions"
  - "The final statement, if reached, is grounded in the exercise outputs — not invented wholesale"
rubric:
  process_discipline: 0.40
  correctness: 0.25
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: a team under time pressure demanding to skip the facilitated
process and receive a finished statement directly. Guards against the most
common failure mode — producing a positioning statement that sounds polished
but is ungrounded because the generative exercises were bypassed. The skill
must hold the process while remaining constructive, not just refuse.
