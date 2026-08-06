---
name: alignment-narrative
description: >
  Craft a structured narrative that builds shared understanding and buy-in across
  stakeholders. Use when you need to shift mental models before a decision,
  persuade a skeptical leadership audience, align a fragmented team around a
  strategic direction, or frame a complex problem so stakeholders feel the
  urgency and inevitability of the proposed path.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/alignment-narrative/template.md
---

# Alignment Narrative

## Purpose
Produce a **persuasive narrative document** that takes stakeholders from scattered
or conflicting mental models to a shared understanding of the problem, the
strategic direction, and the desired response. An alignment narrative is not a
status update, a decision request, or a slide deck — it is a structured story
built to change how the audience *thinks* before asking them to act.

The narrative follows the **Minto SCQA spine** (Situation → Complication →
Question → Answer) to build logical inevitability, and uses **story-based
persuasion** to make the stakes feel concrete and personal to the reader. The
result is a written artifact (1–3 pages) the PM can share asynchronously or
walk through in a meeting.

**When NOT to use:**
- You need to *report status* on a project already underway → use `exec-update`.
- You need to *force a binary decision* with explicit trade-offs evaluated → use `decision-memo`.
- You need to *plan the delivery logistics* of a stakeholder communication (who gets what, when, in what sequence) → use `stakeholder-engagement-advisor`.
- The ask is simple, the audience is already aligned, and persuasion is not the bottleneck → skip the narrative and communicate directly.

## Inputs
- **Required:** the core claim (the direction or truth you want the audience to
  accept) — if the PM cannot state it in one sentence, ask them to before writing.
- **Required:** the audience — role, current belief or concern, and what "aligned"
  looks like for them. Without this the narrative cannot be tuned.
- **Optional:** the business context or current Situation (what is already true
  and uncontested) — if absent, infer from context but flag the assumption.
- **Optional:** supporting evidence (data points, customer quotes, competitive
  signals, prior decisions) — the narrative cites these; without them it signals
  that evidence is thin and asks the PM to supply at least one anchor.
- **Optional:** the desired call to action — what you want the audience to *do*
  after reading. Default: endorse the direction and unblock the team.

## Output Contract
The deliverable is an **alignment narrative document** structured in five
sections (see `template.md`):

1. **Situation** — the shared, uncontested reality the audience already accepts.
   Grounds the reader without triggering disagreement. 2–4 sentences, factual
   and brief.
2. **Complication** — the tension, disruption, or gap that makes the status quo
   insufficient. This is where the narrative creates urgency. One specific,
   evidence-backed Complication is stronger than a list. 3–6 sentences.
3. **Key Question** — the central question the Complication forces. Usually a
   single sentence starting with "So the question is…" or "This raises the question…"
   It must feel *inevitable* given the Complication, not manufactured.
4. **Answer (Strategic Direction)** — the answer to the Key Question. States the
   proposed direction clearly, with the 2–3 reasons why this answer is right.
   Not a list of options; the narrative commits to one. 4–8 sentences.
5. **Call to Action** — what the audience is asked to do next, expressed as a
   concrete, time-bound request. One sentence.

Format: prose. Length: 1–3 pages (400–900 words). No jargon visible to the
audience; the PM's internal reasoning stays internal.

**GOOD (excerpt):**
> **Situation:** Enterprise customers currently manage their supplier relationships
> across three disconnected tools — email, spreadsheets, and our platform — and
> have told us in eight interviews this quarter that the switching cost is their
> primary friction point.
>
> **Complication:** Our two largest competitors launched native supplier portals
> in Q2. Three customers have already told their CSMs they are evaluating switching
> at renewal. If we hold our current roadmap, we enter Q1 renewal season with a
> known gap our competitors will exploit.
>
> *Why this works:* the Complication is specific, externally evidenced, and makes
> inaction visibly costly — it changes the reader's assessment of risk without
> requiring them to trust the PM's judgment.

**BAD (excerpt):**
> "We need to invest in supplier management because it's strategic and customers
> want it. This is a big opportunity and we should move fast."
>
> — fails: no uncontested Situation to anchor in, Complication is vague, no
> evidence, Key Question absent, and the Answer is a direction without reasoning.

## Process
1. **Extract the core claim** — ask the PM to state in one sentence what they
   want the audience to believe after reading. If they cannot, workshop the claim
   before writing any narrative.
2. **Profile the audience** — identify role, current belief, biggest objection,
   and what "aligned" means in behavioral terms.
3. **Build the Situation** — choose facts the audience already accepts. If in
   doubt, pick the most recent shared data point from a meeting or report.
4. **Identify the Complication** — find the single sharpest disruption: a metric
   shift, a competitive move, a customer behavior change, a constraint newly visible.
   Use evidence; do not manufacture urgency.
5. **Derive the Key Question** — write the question the Complication logically
   forces. Test: would a skeptic agree this question is the right one to ask?
6. **State the Answer clearly** — commit to one direction. State 2–3 reasons in
   order of the audience's likely priorities (not the PM's).
7. **Write the Call to Action** — make it concrete (a decision, an unblock, an
   endorsement) and time-bound (by when, in what forum).
8. **Tune for the audience** — re-read as the audience. Remove jargon they do
   not use. Raise or lower technical depth. Emphasize the objection they are most
   likely to hold.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **Situation** contains only uncontested facts — no editorial, no ask.
- [ ] The **Complication** is specific and evidenced (not "customers want X" but "three customers told us Y in interviews on Z date").
- [ ] The **Key Question** follows inevitably from the Complication — a skeptic would agree it is the right question.
- [ ] The **Answer** commits to one direction with 2–3 stated reasons, ordered by audience priority.
- [ ] The **Call to Action** is a single, concrete, time-bound request.
- [ ] The narrative avoids PM-internal language (roadmap jargon, sprint terminology, internal nicknames) that the audience does not use.
- [ ] The whole document is 400–900 words.
- [ ] If the narrative is written to a file, it follows `template.md` — all 5 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `alignment-narrative-happy` — well-resourced ask with clear evidence and a skeptical VP audience.
- `alignment-narrative-edge` — sparse evidence, internal disagreement, no single Complication yet clear.
- `alignment-narrative-adversarial` — PM wants the narrative to advocate for a decision already made; skill must serve persuasion, not post-hoc rationalization.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `stakeholder-engagement-advisor` — plans *who* receives the narrative, in what sequence, and with what preparation; consumes the narrative this skill produces.
- `decision-memo` — forces a specific binary or multi-option choice; use when the audience needs to decide, not just align.
- `exec-update` — surfaces project status; use when the audience needs information, not persuasion.

### External Frameworks
- Barbara Minto, *The Pyramid Principle* (1987) — the SCQA (Situation, Complication, Question, Answer) spine this skill's structure is built on.
- Robert Cialdini, *Influence* (1984, rev. 2021) — commitment/consistency and social-proof principles that underpin stakeholder buy-in mechanics.
- Nancy Duarte, *Resonate* (2010) — story-based persuasion structure (what is vs. what could be) that informs how the Complication and Answer are framed.
