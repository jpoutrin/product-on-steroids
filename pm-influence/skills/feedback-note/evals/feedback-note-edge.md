---
id: feedback-note-edge
skill: feedback-note
input:
  prompt: "Can you write a positive feedback note for Marcus? He's been doing
    a really great job lately and I want to recognize him."
  context: "Marcus is a peer PM. No further details provided."
expected:
  - "The skill does NOT draft a note immediately from the vague input"
  - "The skill asks for the specific situation — which event, when, where"
  - "The skill asks for the specific behavior Marcus demonstrated"
  - "If the user provides the specifics in a follow-up, the resulting note has all four SBI sections filled with that detail"
  - "The note does not contain generic praise such as 'you always do great work' or 'people love working with you'"
rubric:
  elicitation_before_drafting: 0.40
  sbi_structure: 0.30
  specificity: 0.20
  tone_calibration: 0.10
weight: 1.0
---

Edge case: the user provides only a vague compliment with no incident, no
observable behavior, and no impact. The skill must resist drafting a hollow
note and must ask for the concrete moment instead. Guards against generating
feel-good feedback that the recipient cannot learn from or replicate.
