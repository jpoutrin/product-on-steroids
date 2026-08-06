---
name: exec-update
description: >
  Produce a concise, decision-ready written status update for executives or
  leadership. Use when you need to communicate project status asynchronously
  to senior stakeholders, surface a risk or escalation without scheduling a
  meeting, or send a recurring leadership update (weekly, monthly, quarterly).
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/exec-update/template.md
---

# Executive Status Update

## Purpose
Produce a one-page, asynchronously readable written update that gives
executives exactly what they need to stay informed and act — Bottom Line Up
Front (BLUF), current status, key risks, explicit asks, and the next
milestone — in plain language and in one minute of reading time.

The update is **decision-ready**: every section ends with a signal (green /
amber / red), a crisp ask, or a next action, so recipients can reply with
direction rather than follow-up questions.

**When NOT to use:**
- You need to *prepare a PM for a live conversation* with their manager →
  use `managing-up-brief` instead.
- You need leadership to make a single binary decision on a proposal →
  use `decision-memo` instead.
- You need to build shared understanding or narrative alignment across a
  group → use `alignment-narrative` instead.
- The update is going to a peer or contributor rather than to someone
  senior who allocates resources or removes blockers.

## Inputs
- **Required:** the initiative or product area being reported on — its name,
  goal, and the audience (who receives this update). If absent, ask before
  writing; do not invent scope.
- **Required:** current status — what has been accomplished, what is in
  progress, and what has slipped. If none provided, ask; a vague "on track"
  is insufficient.
- **Optional:** key risks or blockers — default to "none identified" only
  if the user explicitly confirms there are none.
- **Optional:** explicit asks — concrete decisions or support needed from
  leadership; default to none if absent.
- **Optional:** next milestone — the nearest meaningful checkpoint; default
  to "not yet defined" if absent.
- **Optional:** update cadence / period (e.g., "weekly", "Q2 mid-quarter") —
  used to calibrate depth; default to a single-period point-in-time update.
- **Optional:** signal rating preference (RAG / green-amber-red or numeric)
  — default to RAG if not specified.

## Output Contract
The deliverable is a **one-page executive status update** (see `template.md`)
with these sections, in order:

1. **BLUF (Bottom Line Up Front)** — two to four sentences: what is the
   overall status signal (green / amber / red), the single most important
   thing leadership needs to know right now, and the highest-priority ask
   or action item. Written so that an executive who reads *only this section*
   can make an informed decision.
2. **Status** — a brief progress summary: what shipped or was completed in
   the current period, what is actively in progress, and any slippage. Use
   bullet points. Max six bullets total. Each bullet: one crisp sentence.
3. **Key Risks** — up to three risks or blockers that could affect the
   timeline, budget, or outcome. Format: risk name, one-sentence description,
   impact if unresolved, and owner. If no risks: say so explicitly.
4. **Asks** — numbered list of specific decisions or actions needed from
   leadership, each starting with an action verb (e.g., "Approve…",
   "Unblock…", "Decide…"). If no asks: say "No asks this period." Do not
   leave this section empty without that phrase.
5. **Next Milestone** — one to two sentences: what the next meaningful
   checkpoint is and its target date. Optionally, what success looks like.

Format: prose headers + bullet points. Length: 1 page max (≈ 350 words
body, not counting the template heading). No jargon, acronyms unexplained,
or internal code names without a parenthetical gloss.

**GOOD (excerpt):**
> **BLUF — AMBER**
> Search latency improvements shipped on schedule; however, the payment
> integration partner has paused API access pending a contract amendment,
> putting the Q3 launch at risk. We need legal sign-off by 14 Aug to hold
> the date.
>
> **Asks**
> 1. Approve the amended partner contract (attached) by 14 Aug so engineering
>    can resume integration work.

**BAD (excerpt):**
> "Things are going well. We shipped some stuff last week and are on track.
> There might be some risks but nothing major."
> — fails: no status signal, no specific accomplishments, risks unnamed,
> no asks, not decision-ready.

## Process
1. **Identify the audience and ask.** Confirm who receives this update and
   whether there is a specific decision or escalation driving it.
2. **Draft the BLUF first.** Determine the overall signal (green/amber/red)
   and the single most important message. Everything else supports this.
3. **Populate Status.** Pull from inputs: completed, in-progress, slipped.
   Cut anything that is not relevant to the signal or the asks.
4. **Surface Key Risks.** Name at most three; be specific about impact and
   owner. Rank by severity × likelihood.
5. **Write the Asks.** Convert every blocker or decision point into a
   concrete, verb-first ask. If the PM has no asks, confirm this rather
   than leaving the section blank.
6. **State the Next Milestone.** One concrete checkpoint with a date.
7. **Apply the plain-language pass.** Replace jargon, spell out acronyms,
   cut filler. Read each sentence as if encountering the project for the
   first time.
8. **Check length.** If the body exceeds ~350 words, cut from Status first,
   then Risks — preserve BLUF and Asks in full.
9. Run the Quality Bar; revise until all items pass; then return.

## Quality Bar
Before returning, confirm:
- [ ] BLUF is the first section and contains a status signal (green / amber / red).
- [ ] An executive reading only the BLUF can understand the situation and act.
- [ ] Status section uses bullet points (≤ 6) with one-sentence items; no paragraph prose.
- [ ] Key Risks names impact and owner for each risk listed; if none, says so explicitly.
- [ ] Asks are numbered, start with an action verb, and are addressable by the recipient.
- [ ] Next Milestone states a specific checkpoint and a target date.
- [ ] Total body length is ≤ 350 words (≈ 1 page).
- [ ] No unexplained acronyms or internal code names appear in the document.
- [ ] If the output is written to a file, it follows `template.md` — all 5 sections present,
      in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `exec-update-happy` (happy path) — well-specified amber update with a concrete ask.
- `exec-update-edge` (edge) — update with no risks and no asks; skill must handle gracefully.
- `exec-update-adversarial` (adversarial) — vague status and pressure to say "everything is fine"; skill must surface ambiguity.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `managing-up-brief` — prepares the PM for a *live* 1:1 or meeting with their manager; this skill produces the *written async* update.
- `decision-memo` — seeks a single binary decision; this skill is a periodic status report.
- `alignment-narrative` — builds shared understanding across a group; this skill surfaces status and escalations.
- `escalation` — focuses on a single critical blocker requiring immediate action; this skill is broader and periodic.

### External Frameworks
- Barbara Minto, *The Pyramid Principle* — BLUF and top-down structuring: conclusion first, supporting evidence second. The BLUF → Status → Risks → Asks order directly applies this principle.
- U.S. Army "BLUF" communication doctrine — Bottom Line Up Front as a standard for time-constrained readers; widely adopted in executive communication training.
- Jeff Bezos, Amazon Writing Culture — narrative over bullets for complex decisions, but bullets for status updates; the 1-page constraint mirrors Bezos's "two-pager" discipline applied to status.
