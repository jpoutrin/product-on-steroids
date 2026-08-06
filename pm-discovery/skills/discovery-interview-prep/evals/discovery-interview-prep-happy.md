---
id: discovery-interview-prep-happy
skill: discovery-interview-prep
input:
  prompt: >
    I have a 45-min discovery interview tomorrow with Camille, a Head of
    Operations at a 200-person logistics company. She was referred by our CSM.
    We already know she runs a team of 8 and uses spreadsheets to track carrier
    invoices. My learning objective: understand whether invoice reconciliation
    errors are causing her team to lose meaningful time each month, and why.
    My hypotheses: H1 — ops managers at this scale manually cross-check carrier
    invoices against internal POs because their TMS doesn't export a
    reconcilable format; H2 — reconciliation errors surface late (post-payment)
    because there is no automated flag. I'll have a note-taker; recording
    consent TBD.
  context: >
    Generative discovery phase. Team exploring whether invoice-reconciliation
    pain is large enough to anchor a new product surface. No solution concept
    yet.
expected:
  - Interview Goal is expressed as a single answerable question tied to the
    reconciliation pain, not a broad topic.
  - Both H1 and H2 are present verbatim or paraphrased as falsifiable claims.
  - All 5 Key Questions are open-ended and anchored in past behaviour (e.g.
    "Walk me through…", "Tell me about the last time…"); none lead toward a
    solution or ask a hypothetical preference.
  - Each Key Question is annotated with the hypothesis it serves (H1 or H2).
  - Listening Cues include concrete observable signals — specific words or
    stories that would confirm/deny each hypothesis.
  - Forbidden Frames explicitly names leading questions, solution-pitching, and
    hypothetical-preference questions.
  - Logistics section records the 45-min duration, recording consent as TBD,
    and note-taker as present.
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy-path scenario: PM arrives with a clear, specific learning objective, two
well-formed hypotheses, and good prior context on the participant. Guards against
the skill producing generic "tell me about your day" questions or omitting the
hypothesis-to-question mapping. Validates that the output is actionable enough
that a PM could walk into the interview cold and use the sheet without additional
preparation.
