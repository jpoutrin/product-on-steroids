---
name: feedback-note
description: >
  Draft a short, structured written feedback note using Situation-Behavior-Impact
  (SBI) framing. Use when you need to deliver positive reinforcement to a peer or
  direct report, provide constructive correction after a specific incident, prepare
  written feedback for a performance cycle, or document feedback before a 1:1.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/feedback-note/template.md
---

# Feedback Note (SBI)

## Purpose
Produce a concise, professional written feedback note — addressed to a named
colleague, direct report, or peer — using Situation-Behavior-Impact (SBI)
framing. The note is written to be sent or read, not spoken aloud. It gives the
recipient enough context to understand exactly what happened, how they behaved,
and what effect that had, so they can reinforce or change that behavior.

**When NOT to use:**
- Preparing talking points for a live conversation with your manager — use `managing-up-brief`.
- Sending a status update to leadership — use `exec-update`.
- Capturing team-wide retrospective learnings — use `retro`.
- Writing a 360 review entry (multi-topic, aggregated) — this skill handles a
  single-incident note; compose multiple notes separately if you need multi-topic.
- Addressing a serious HR or legal matter — consult HR directly; a structured
  note is not the right vehicle.

## Inputs
- **Required:** recipient's name and role, feedback direction (positive /
  constructive), and the specific situation or incident — what happened, when,
  and where. If the user provides no incident details, ask: "Can you describe the
  specific situation and what [name] did?"
- **Optional:** the relationship (peer / direct report / cross-functional partner),
  desired tone (candid, warm, formal), and any preferred next step or follow-up
  ask. If omitted, tone defaults to professional-warm and no explicit follow-up
  is added.

## Output Contract
The deliverable is a **feedback note** structured in four sections (see
`template.md`):

1. **Opening** — one sentence naming the recipient and setting the purpose
   (positive or constructive).
2. **Situation** — the specific context: when, where, and what was happening.
   One to two sentences; no vague generalities.
3. **Behavior** — the observable action the recipient took. Factual, specific,
   free of interpretation or judgment labels. One to three sentences.
4. **Impact** — the concrete effect of that behavior on the team, project,
   stakeholder, or outcome. One to three sentences.
5. **Close** (optional but recommended) — a one-sentence forward-looking
   statement: reinforcement (positive) or a specific ask to change or continue
   (constructive).

Format: plain prose, ≤ 250 words, second person ("you"), no bullet lists in the
body. Headings may optionally appear in the delivered note if the sender prefers
structured layout — controlled by template choice.

**GOOD (excerpt):**
> During last Tuesday's Q3 planning session with the growth team, you noticed
> that two stakeholders were talking past each other on the launch date. You
> paused the discussion, restated both positions without bias, and proposed a
> structured trade-off conversation for the following day. That move prevented
> the meeting from derailing and gave the team a concrete path forward — the
> growth lead told me afterward it was exactly what was needed.

**BAD (excerpt):**
> "You always do a great job in meetings and people like working with you."
> — fails: no specific situation, no observable behavior, no impact, pure praise
> that the recipient cannot replicate or learn from.

## Process
1. **Identify the incident** — extract (or elicit) the single situation, the
   specific behavior, and the resulting impact. If the user provides a vague
   summary ("they were great"), ask for the concrete moment.
2. **Classify direction** — positive reinforcement or constructive correction.
   Do not mix both in one note; if the user wants both, generate two notes.
3. **Draft Opening** — one sentence, warm and direct.
4. **Draft Situation** — anchor in time/place/context; strip opinion.
5. **Draft Behavior** — describe the observable action only. Avoid "you seemed"
   or "I think you were"; use "you did X".
6. **Draft Impact** — name the concrete effect. Cite the team, the output, the
   stakeholder, or the metric. For constructive notes, name the negative effect
   without exaggerating.
7. **Draft Close** — for positive: reinforce the behavior and invite repetition.
   For constructive: state one specific change you are asking for.
8. **Calibrate tone** — re-read for: (a) no judgment labels (lazy, careless,
   brilliant, exceptional — none of these); (b) second person throughout;
   (c) length ≤ 250 words; (d) no bullet lists in the body.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The note names a **specific situation** (time, place, or event) — no
  general statements like "you always" or "you never."
- [ ] The **Behavior** section describes an **observable action**, not an
  inference, trait, or judgment label.
- [ ] The **Impact** section names a **concrete effect** on a person, team,
  project, or outcome — not a feeling about the behavior.
- [ ] The note does **not mix positive and constructive feedback** in the same
  document.
- [ ] Tone is **professional** — neither harsh nor sycophantic; the recipient
  can read it without feeling attacked or patronized.
- [ ] Length is **≤ 250 words** (excl. heading/opening line).
- [ ] The note is written in **second person** ("you did / you said / you
  proposed") throughout.
- [ ] If the output is written to a file, it follows `template.md` (a
  skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `feedback-note-happy` — constructive note for a direct report who missed a
  deadline with clear situation/behavior/impact to work from.
- `feedback-note-edge` — positive feedback request with only a vague
  compliment; skill must elicit specifics before drafting.
- `feedback-note-adversarial` — user asks to combine positive and constructive
  feedback in one note; skill must decline to mix and offer two separate notes.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `managing-up-brief` — structures a conversation with a senior leader; not for
  peer/direct-report written feedback.
- `stakeholder-engagement-advisor` — manages ongoing relationship strategy;
  this skill handles a single discrete feedback moment.

### External Frameworks
- Center for Creative Leadership, *SBI Feedback Model* — the canonical
  Situation-Behavior-Impact framework this skill is built on.
- Kim Scott, *Radical Candor* (2017) — "care personally, challenge directly";
  the Impact step operationalizes the caring-directly axis.
- Douglas Stone & Sheila Heen, *Thanks for the Feedback* (2014) — receiver
  psychology that informs how the Behavior and Impact sections are framed to
  be receivable rather than triggering defensiveness.
