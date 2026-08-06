---
id: feedback-note-happy
skill: feedback-note
input:
  prompt: "Write a constructive feedback note for my direct report, Priya."
  context: "Priya is a mid-level PM. Last Wednesday she sent the sprint review
    deck to stakeholders 90 minutes before the meeting without giving me a heads-up.
    Two executives arrived with no context and the first 20 minutes were spent
    re-explaining the goals. I want to address this directly but keep the tone
    constructive, not punishing. We have a 1:1 on Friday."
expected:
  - "The Situation section names last Wednesday's sprint review specifically — not a vague 'recently'"
  - "The Behavior section describes the observable action (sent the deck without a heads-up) without labeling Priya careless, thoughtless, or any trait"
  - "The Impact section names the concrete consequence (executives arrived uncontextualized, first 20 minutes lost)"
  - "The Close asks for a specific change going forward (e.g., share decks with manager 24h in advance)"
  - "The note is written in second person throughout"
  - "The note does not mix positive praise into a constructive note"
  - "Length is under 250 words"
rubric:
  sbi_structure: 0.35
  specificity: 0.30
  tone_calibration: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: PM has all the ingredients — named recipient, clear incident,
observable behavior, measurable impact. Guards against the skill producing vague
praise ("you could communicate better") or mixing encouragement into a
constructive note, which dilutes the message.
