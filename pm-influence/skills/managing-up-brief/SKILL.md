---
name: managing-up-brief
description: >
  Prep doc for a live conversation with a senior leader. Use when preparing a
  1:1 or review meeting with a VP, C-suite leader, or skip-level, when you need
  to align on a decision, secure sponsorship, surface a risk, or navigate a
  sensitive topic in real time.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/managing-up-brief/template.md
---

# Managing-Up Conversation Brief

## Purpose
Produce a structured prep document a PM uses before a live conversation with a
senior leader — covering what to say, what to ask, how to handle objections, and
what outcome to walk out with. The brief lets you enter a 1:1 or review fully
prepared, controlling the narrative rather than reacting in the room.

This skill focuses on **dialogue preparation**: anticipating the leader's concerns
and framing your position so you can steer a real-time exchange. It is distinct
from drafting a written artifact intended to travel without you.

**When NOT to use:**
- **Async written update** → use `exec-update` (the leader reads it without you).
- **Async decision sign-off** → use `decision-memo` (drives approval via written
  doc, not live discussion).
- **Broad organizational alignment** → use `alignment-narrative` (shapes shared
  understanding across many stakeholders over time; not targeted conversation prep).
- **Onboarding a new executive** → use `executive-onboarding-playbook`.

## Inputs
- **Required:** the meeting purpose — what decision, ask, or topic you need to
  navigate. If missing, ask before drafting.
- **Required:** the leader's role and known priorities/pressures — at minimum
  their function and what they care about most. Infer from context if the user
  provides enough signals; otherwise ask.
- **Optional:** the specific ask or desired outcome — what you want to leave the
  meeting with (a decision, a green light, increased visibility). Default: derive
  from the meeting purpose.
- **Optional:** known objections or hot-button topics — what the leader typically
  pushes back on. Default: surface the most likely objections from the situation
  described.
- **Optional:** relevant context or recent history — prior discussions, current
  org priorities, relationship dynamics. Use to calibrate tone and framing.

## Output Contract
The deliverable is a **managing-up brief** with these sections (see `template.md`):

1. **Meeting Context** — one-paragraph situation summary: the leader, their
   priorities, the meeting occasion, and the stakes of the conversation.
2. **Desired Outcome** — a single crisp sentence: what "winning" this conversation
   looks like. Includes both the explicit ask (a decision, alignment, resource)
   and the implicit goal (trust, visibility, political capital).
3. **Opening Line** — one or two sentences to open the meeting with: sets the
   frame, signals confidence, and orients the leader without preamble.
4. **Key Points to Land** — 3–5 bullets, each with a one-line supporting
   rationale. Ordered by leader priority, not PM priority.
5. **Anticipated Objections & Responses** — a table: each objection in the
   leader's language, the reframe or concession, and a one-line response script.
   Minimum 3 objections.
6. **Questions to Ask** — 2–4 open questions that advance the outcome, surface
   hidden constraints, or build the relationship. Not rhetorical.
7. **Pre-Wire Checklist** — named stakeholders to brief before the meeting, the
   ask for each, and whether they are done.

Format: structured markdown with headers and one table. Length: 1–2 pages — long
enough to be useful, short enough to scan in 5 minutes before the meeting.

**GOOD (excerpt):**
> **Desired Outcome:** Leave with VP Engineering's explicit support to include
> the auth rework in Q3 scope, reducing incident risk before the holiday freeze.
>
> **Opening Line:** "I want to use our time to align on one scoping decision for
> Q3 — it affects holiday reliability and I want your read on the tradeoff."
>
> **Objection:** "We can't slip the roadmap for tech debt." → **Response:** "Agreed
> — I'm proposing we absorb it within existing Q3 capacity by descoping Feature Y,
> which is lower-priority per last quarter's OKR review."

**BAD (excerpt):**
> "Tell them about the auth rework and why it matters. Be clear and confident."
> — fails: no opening line, no framing by leader priority, no objection handling,
> no desired outcome stated — this is a topic list, not a conversation brief.

See `template.md` for the fill-in structure.

## Process
1. **Identify the leader's lens** — what metrics, risks, or org priorities
   dominate this leader's worldview right now? Frame everything through that lens.
2. **Crystallize the desired outcome** — what do you need to walk out with?
   Separate the explicit ask (a yes/no/more-info) from the implicit goal (trust,
   sponsorship, precedent). Write the outcome sentence before drafting anything else.
3. **Draft the opening line** — the first 30 seconds control the frame. Write one
   or two sentences that signal confidence and orient the leader without context-dumping.
4. **Select and order key points** — choose the 3–5 points that most directly
   serve the desired outcome. Order them by what the leader cares about, not by
   what the PM wants to explain first.
5. **Anticipate objections** — list every realistic pushback, including the ones
   that are uncomfortable to hear. For each, write the leader's version of the
   objection (in their language), then a response that is either a reframe, a
   concession with a counter, or a deferral with a commitment. Do not write
   defensive responses.
6. **Write questions to ask** — open questions that either advance the outcome or
   surface constraints you do not yet know. Avoid questions you could answer
   yourself with research.
7. **Build the pre-wire checklist** — identify anyone whose support will make the
   leader more likely to say yes. List them, the ask, and whether done. A senior
   leader should rarely hear your idea for the first time in the room.
8. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The desired outcome is a **single sentence** that names both what you want
  and why it matters to the leader (not "align on X" as a generic goal).
- [ ] The opening line is written out in full — not "introduce the topic" but
  the actual words to say.
- [ ] Key points are **ordered by leader priority**, not PM logic.
- [ ] Every anticipated objection is written in the **leader's language**, not the
  PM's framing.
- [ ] At least **3 objections** are surfaced, including at least one uncomfortable one.
- [ ] Questions are **genuinely open** — they cannot be answered with a yes/no and
  they advance the outcome or surface unknowns.
- [ ] The pre-wire checklist names **specific people**, not just roles.
- [ ] The brief is **scannable in under 5 minutes** — no paragraphs where bullets
  suffice; no context the leader already knows.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped
  hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `managing-up-brief-happy` (happy path) — standard sponsorship ask for a
  resourcing decision with a known leader profile.
- `managing-up-brief-edge` (edge) — sensitive topic with a risk-averse leader;
  must surface the uncomfortable objection and avoid hedging.
- `managing-up-brief-adversarial` (adversarial) — vague ask ("help me prep for
  my 1:1") with no meeting purpose; skill must elicit required inputs before drafting.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `exec-update` — async written update to a senior audience; use when the leader
  reads without you present.
- `decision-memo` — async sign-off doc; use when you want approval on a written
  proposal rather than live alignment.
- `alignment-narrative` — broad shared-understanding building across multiple
  stakeholders; use when influence spans beyond a single conversation.
- `stakeholder-engagement-advisor` — identifies engagement strategy and cadence
  across a stakeholder map; feeds the pre-wire step of this skill.

### External Frameworks
- Michael Watkins, *The First 90 Days* (2003) — "managing up" chapter: diagnose
  the leader's style before adapting communication; the situation-diagnosis step
  in this skill draws from that model.
- Julie Zhuo, *The Making of a Manager* (2019) — feedback and meeting framing
  for new managers navigating upward; the opening-line and question-crafting
  sections are informed by her approach.
- Patrick Lencioni, *The Five Dysfunctions of a Team* (2002) — trust and
  conflict norms; informs why surfacing uncomfortable objections (rather than
  softening them) builds credibility over time.
