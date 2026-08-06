---
name: discovery-interview-prep
description: >
  Use when preparing for a specific upcoming user discovery interview session —
  sharpening the learning objective, aligning questions to hypotheses, and
  defining listening cues before you enter the room (or the call).
version: 0.1.0
type: component
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/discovery-interview-prep/template.md
---

# Prepare for a Discovery Interview Session

## Purpose
Produce a one-page tactical prep sheet for a single upcoming discovery interview.
The artifact sharpens the PM's learning objective for this session, surfaces what
is already known about the participant, makes the hypotheses to test explicit,
derives non-leading open-ended questions directly from those hypotheses, and arms
the PM with listening cues so they recognise signal when it arrives. The goal is
to walk into the interview in learning mode — not pitching, not validating a
predetermined answer, and not improvising.

**When NOT to use:**
- Building the full multi-session discovery plan or research arc — use
  `discovery-process` for that.
- Writing the actual interview script document (with all questions, probes, and
  transitions) the interviewer reads verbatim during the session — use
  `interview-script` for that.
- Probing stakeholder politics or org-level dynamics — use `pol-probe` for that.
- Running or synthesising findings across multiple interviews — those are separate
  execution and synthesis steps.

## Inputs
- **Required — upcoming session context:** date/time, participant name or
  pseudonym, participant role and company (or segment), and the specific learning
  objective for *this* session. If the objective is missing or vague ("learn
  about them"), pause and help the PM sharpen it before continuing: ask what
  decision this interview is meant to inform.
- **Required — hypotheses:** 2–3 specific, falsifiable assumptions the PM wants
  to test. If the PM hasn't articulated them, elicit: "What do you currently
  believe is true that this interview could prove wrong?"
- **Optional — prior knowledge of the participant:** past interactions, inferred
  pain points, company context, role, how they were recruited. Used to tailor
  questions and avoid wasting time on known facts.
- **Optional — session constraints:** duration (default 45 min), recording
  consent status, note-taker present (yes/no/async).
- **Optional — broader discovery context:** which phase (generative vs.
  evaluative), which problem space or job-to-be-done the team is exploring.

## Output Contract
The deliverable is a **discovery interview prep sheet** structured as (see
`template.md`):

1. **Interview Goal** — one sentence: the specific learning objective for this
   session, expressed as a question the interview should answer (not "learn about
   X" but "understand whether X is a blocker for personas like this participant").
2. **Participant Context** — who they are (role, company/segment, how recruited),
   what is already known that's relevant, and a one-line "so what" — why *this*
   person is worth interviewing *now*.
3. **Hypotheses to Test** — 2–3 specific, falsifiable beliefs this interview
   could validate or invalidate. Each is labelled H1, H2, … and stated as a
   testable claim ("We believe [persona] experiences [pain] because [reason]").
4. **Key Questions** — top 5 open-ended, non-leading questions mapped to the
   hypotheses (annotate which hypothesis each serves). Questions start from
   experience/behaviour, not opinions or solutions. Ordered by conversational
   flow, not by hypothesis order.
5. **Listening Cues** — for each hypothesis, 2–3 observable signals (words,
   emotions, pauses, stories) that would confirm or deny it. Written as "Listen
   for … which would suggest …".
6. **Forbidden Frames** — 3–5 specific question types or framings to avoid in
   this session, with a one-line reason. Always includes: leading questions,
   solution-pitching, and hypothetical-preference questions ("Would you pay…?").
7. **Logistics** — session duration, recording consent status, note-taker
   arrangement, and any session-specific setup notes.

Format: structured prose with labelled subsections. Length: fits one page
(~400–600 words). Every question maps to a hypothesis — no orphan questions.

**GOOD (excerpt):**
> **H2:** We believe mid-market ops managers lose track of approvals because
> they rely on email threads with no single source of truth.
>
> **Q3 (→ H2):** Walk me through the last time an approval took longer than
> expected — what happened?
>
> **Listening cue (H2):** Listen for mentions of "searching email" or
> "following up manually" — suggests the pain is real and frequent.

**BAD (excerpt):**
> "Q3: Would you use a dashboard that centralised approvals?"
> — fails: leads the participant to the solution, tests preference not behaviour,
> yields no falsifiable signal on H2.

## Process
1. **Confirm the session goal** — if the learning objective is vague or missing,
   ask the PM what decision this interview will inform; rewrite until the goal
   is one answerable question.
2. **Surface prior knowledge** — review any context provided about the
   participant; note what is already known so questions don't re-tread it.
3. **Lock the hypotheses** — if fewer than 2 are provided, elicit them; if more
   than 3 are offered, help the PM prioritise to the 2–3 most uncertain ones for
   this session.
4. **Draft Key Questions** — for each hypothesis, generate candidate open-ended
   questions anchored in past behaviour ("Tell me about a time…", "Walk me
   through…", "What does that look like for you?"). Cull to 5 questions total;
   annotate hypothesis mapping.
5. **Sequence the questions** — order for natural conversational flow: start wide
   (context/background), narrow toward the hypotheses, end open ("What else
   should I know?").
6. **Define Listening Cues** — for each hypothesis write 2–3 observable signals;
   make them specific enough that a note-taker can flag them in real time.
7. **Write Forbidden Frames** — enumerate question types to avoid; always flag
   leading questions, solution references, and hypothetical-preference patterns.
8. **Fill Logistics** — duration, recording consent, note-taker.
9. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The Interview Goal is a single answerable question — not a topic or a
  wish list.
- [ ] There are exactly 2–3 hypotheses, each falsifiable ("We believe X because Y").
- [ ] Every Key Question maps to a specific hypothesis (annotation present).
- [ ] No Key Question leads the participant toward a solution, product concept,
  or stated preference ("Would you…?", "Do you think…?").
- [ ] Questions are anchored in past behaviour or current experience — not
  hypotheticals.
- [ ] Listening Cues are concrete and observable — not "they seem interested".
- [ ] Forbidden Frames section is present and includes at least: leading
  questions, solution-pitching, and hypothetical-preference questions.
- [ ] If the output is written to a file, it follows `template.md` — all 7
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `discovery-interview-prep-happy` (happy path) — PM has a clear hypothesis,
  knows the participant, 45-min session; produces sharp prep with non-leading questions.
- `discovery-interview-prep-edge` (edge) — PM has zero context on participant and
  a vague goal; skill must sharpen the goal before producing prep.
- `discovery-interview-prep-adversarial` (adversarial) — PM wants to "test our
  solution concept in the interview"; skill reframes toward learning-first and
  flags solution-pitching as a Forbidden Frame.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `discovery-process` — plans the full multi-session discovery arc; the session
  this skill preps is one node within that arc.
- `interview-script` — the full script document used *during* the interview;
  this skill's Key Questions feed into that script.
- `pol-probe` — stakeholder politics probing for org-level discovery; different
  participant type and objectives.
- `synthesis-affinity` — downstream skill that clusters raw interview notes into
  themes after sessions are complete.

### External Frameworks
- Teresa Torres, *Continuous Discovery Habits* (2021) — opportunity-solution tree
  and the discipline of interviewing for opportunity discovery, not solution
  validation; directly informs the "learning-first" and hypothesis-driven approach.
- Steve Portigal, *Interviewing Users* (2013) — question sequencing (context →
  specifics → reflection), listening cues, and the interview-as-conversation arc
  this skill's Process mirrors.
- Cindy Alvarez, *Lean Customer Development* (2014) — hypothesis articulation
  ("We believe … because …") and the five canonical discovery questions that
  anchor non-leading question design.
