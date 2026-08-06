---
id: discovery-interview-prep-edge
skill: discovery-interview-prep
input:
  prompt: >
    I have a discovery call on Friday with someone from our user panel. I don't
    know much about them — just that they signed up as a "finance professional"
    in our panel. Goal is to learn more about how they work. 30 minutes. No
    note-taker. Can you help me prep?
  context: >
    Early generative discovery. No specific problem space locked yet. PM has
    not articulated hypotheses and has minimal participant context.
expected:
  - Skill does NOT produce a full prep sheet immediately; it first asks the PM
    to sharpen the learning objective (what decision will this interview inform?)
    before generating the artifact.
  - Skill surfaces the missing information — participant context gap and absent
    hypotheses — and prompts the PM to provide or construct them.
  - Once the PM provides (or is helped to articulate) a sharper goal and
    hypotheses, the skill produces a valid prep sheet with all 7 sections.
  - Skill helps the PM construct at least 2 falsifiable hypotheses from the
    vague goal if the PM cannot supply them.
  - The final Key Questions are still open-ended and non-leading despite the
    thin context — they rely on broad behavioural openers that work for any
    finance professional.
  - Logistics section reflects the 30-min constraint and no note-taker (async
    note-taking or transcript recommended).
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge scenario: PM provides near-zero context — no participant background, no
hypotheses, and a vague learning objective ("learn more about how they work").
Guards against the skill blindly producing a generic prep sheet that would be
useless in the interview. Validates that the skill enforces the goal-sharpening
step and elicits hypotheses before proceeding, while still being helpful rather
than just refusing to continue.
