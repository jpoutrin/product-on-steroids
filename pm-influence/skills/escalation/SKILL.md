---
name: escalation
description: >
  Use when a blocked decision or critical risk has not been resolved through
  normal channels and requires surfacing to a higher level of leadership — when
  standard stakeholder alignment has failed, when a dependency blocker threatens
  a milestone, or when a risk will cause irreversible harm if left unaddressed
  beyond the current week.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/escalation/template.md
---

# Escalation Message / Memo

## Purpose
Produce a structured escalation memo that surfaces a blocked decision or
critical risk to the right level of leadership — clearly, concisely, and in a
way that preserves relationships while making the urgency and stakes impossible
to misread. The escalation names the situation, documents what has already been
tried, states exactly what is needed and from whom, and specifies the consequence
if nothing changes by a named date.

The goal is *resolution*, not blame: an escalation should read as a request for
help from a leader who can unblock, not an accusation against a peer who has
failed.

**When NOT to use:**
- A decision that has not yet been attempted through normal channels — try
  `decision-memo` first to drive the choice at the right level.
- A routine status update to leadership — use `exec-update`.
- A situation where the real root cause is unclear ownership — resolve that first
  with `raci-decision-rights`; escalation before clarity wastes leadership
  bandwidth and damages credibility.
- A conflict that a direct conversation between the two parties could resolve —
  escalation skips a step and can create lasting political friction; exhaust
  direct options first.
- An issue that is important but not time-sensitive — schedule a normal
  conversation rather than triggering urgency that is not real.

## Inputs
- **Required:** the blocker or risk — what is stuck, and why it cannot move
  without this escalation. If the user cannot articulate the specific blockage,
  help them identify it before drafting.
- **Required:** what has already been tried — at minimum two or three concrete
  attempts (meetings, decisions proposed, stakeholders engaged). A bare escalation
  with no prior effort signals poor judgment; document the trail.
- **Required:** what is specifically needed — a decision, a resource, an
  exception, an instruction to a peer. Name it precisely; vague asks produce
  vague responses.
- **Required:** the escalation recipient — name and role. If the right recipient
  is genuinely uncertain, surface that as an input gap before drafting.
- **Required:** the deadline and consequence — by when is a response needed, and
  what happens (to customers, to the business, to the team) if nothing changes
  by that date.
- **Optional:** supporting evidence — data, quotes, dependencies affected,
  external commitments at risk. Default: include whatever exists; if thin, note
  the gap rather than fabricating.
- **Optional:** proposed resolution — if the PM has a preferred path, state it
  and invite the recipient to counter or approve it. Not required; sometimes
  the right ask is "help me decide."

## Output Contract
The deliverable is an **escalation memo** (see `template.md`), structured as:

1. **Header block** — date, sender, recipient (name + role), subject line
   beginning with "Escalation:" and naming the blocker in one sentence.
2. **Situation** — two to four sentences: what the initiative is, what is blocked
   or at risk, and how long it has been stuck. No background lecture; only what
   is load-bearing to understand the stakes.
3. **What has been tried** — a numbered list of two to five concrete prior
   attempts, each with a date or time reference and the outcome. This is the
   evidence that normal channels have failed.
4. **What is needed** — a single, crisp ask: the specific decision, resource,
   exception, or action required. One sentence. If multiple things are needed,
   list them ranked by priority — but minimize the ask.
5. **Consequence if unresolved** — one to two sentences on the specific,
   tangible impact if no action is taken by the stated deadline: customer impact,
   missed milestone, financial cost, team consequence.
6. **Deadline** — the latest date by which a response is needed for the
   consequence to be avoidable, with a brief rationale tied to a real constraint
   (a sprint, a contract clause, a customer commitment).
7. **Proposed path (optional)** — if the PM has a recommended resolution, two
   to three sentences inviting the recipient to approve, counter, or redirect.

Format: plain prose, memo style. Length: half a page maximum. No jargon. No
passive voice. Every factual claim is either cited or labeled an assumption.
Tone: direct and collaborative — not defensive, not accusatory.

**GOOD (excerpt):**
> **What is needed:** A decision from you, by June 12, on whether to grant the
> Data team a 3-week exception to the shared-infrastructure freeze so we can
> proceed with the migration. Without this exception, the Q2 data-platform
> milestone cannot ship.
>
> **Consequence if unresolved:** If no decision by June 12, the migration slips
> to Q3, which triggers a €40K penalty clause in the FinCorp contract and
> affects revenue recognition this quarter.

**BAD (excerpt):**
> "There have been some issues with the Data team and we wanted to flag this for
> awareness. Hopefully we can find a path forward soon."
> — fails: no specific ask, no deadline, no consequence, buries the blocker in
> vague language, and asks for "awareness" instead of a decision.

See `template.md` for the fill-in structure.

## Process
1. **Confirm the blocker** — work with the user to articulate exactly what is
   stuck, why it cannot be resolved at the current level, and how long it has
   been stuck. If the blocker is vague, push for specificity before proceeding.
2. **Document the trail** — enumerate prior attempts with dates and outcomes.
   If fewer than two prior attempts exist, flag that the escalation may be
   premature and suggest what to try first; proceed only if the user confirms
   genuine urgency.
3. **Identify the right recipient** — the escalation should go to the minimum
   level of leadership needed to unblock the situation. Over-escalating wastes
   executive attention and signals poor judgment; under-escalating does nothing.
4. **Sharpen the ask** — translate the blocker into a single, unambiguous
   request. Compound asks dilute urgency and make it easy for the recipient to
   respond partially and consider the matter closed.
5. **Name the consequence concretely** — convert abstract risk into specific,
   tangible impact: a date, a dollar amount, a customer commitment, a team
   outcome. Vague consequences are ignored.
6. **Set the deadline with a rationale** — pick the latest defensible date that
   still allows the consequence to be avoided, and explain why that date is real.
7. **Draft the proposed path (if relevant)** — if the PM has a view on
   resolution, state it clearly so the recipient can approve rather than invent.
   Frame it as an invitation, not a demand.
8. **Calibrate tone** — re-read the draft. Every sentence should communicate
   "I need your help" rather than "they failed." Remove blame language,
   exaggeration, or political framing.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The subject line begins with "Escalation:" and names the blocker in one sentence.
- [ ] The situation is four sentences or fewer and states how long the issue has been stuck.
- [ ] At least two concrete prior attempts are documented with dates or time references and their outcomes.
- [ ] The ask is a single, specific request — one decision, resource, exception, or action.
- [ ] The consequence is concrete: a date, dollar amount, customer commitment, or team outcome — not a vague risk.
- [ ] A clear deadline is stated with a rationale tied to a real constraint.
- [ ] Tone is direct and collaborative — no blame language, no passive voice, no exaggeration.
- [ ] Length is half a page maximum; no jargon.
- [ ] No unsupported factual claims — every number or assertion is cited or labeled an assumption.
- [ ] If the output is written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `escalation-happy` — clear blocker with a documented trail of prior attempts,
  a specific ask, and a concrete deadline; tests that the memo is crisp, direct,
  and relationship-preserving.
- `escalation-edge` — escalation appears premature (only one prior attempt, no
  stated consequence); the skill must surface what should be tried first and only
  draft if the user confirms urgency overrides the normal sequence.
- `escalation-adversarial` — user provides a vague, blame-heavy brief ("the Data
  team keeps ignoring us, escalate this"); the skill must reframe without blame
  language and extract a specific ask before drafting.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `decision-memo` — standard decision request at the current level; use this
  first before escalating if the decision has not yet been formally posed.
- `exec-update` — routine status reporting to leadership; not urgent, not blocked.
- `raci-decision-rights` — clarifies who owns which category of decisions;
  upstream to escalation when ownership is the root cause of the blockage.
- `managing-up-brief` — synchronous conversation prep; use when the escalation
  warrants a live conversation rather than an async memo.

### External Frameworks
- Barbara Minto, *The Pyramid Principle* (1987) — SCQA structure (Situation,
  Complication, Question, Answer) that maps directly onto this memo's flow and
  ensures the ask surfaces at the top rather than being buried in background.
- Amy Edmondson, *The Fearless Organization* (2018) — psychological safety and
  the conditions under which teams surface bad news early; escalation is a signal
  of a healthy culture, not failure, when done with evidence and without blame.
- Patrick Lencioni, *The Five Dysfunctions of a Team* (2002) — conflict avoidance
  as a root dysfunction; structured escalation is the organizational mechanism
  for resolving conflicts that direct conversation cannot.
