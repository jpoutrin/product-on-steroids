---
name: roadmap-communication
description: >
  Tailor an existing roadmap into an audience-specific communication (execs,
  engineering, sales/CS, or customers) — right framing, message hierarchy,
  what to reveal vs omit, commitments vs directional bets, and an FAQ. Use when
  presenting a roadmap to leadership, briefing engineering, enabling sales/CS,
  sharing a customer-facing roadmap, or answering "when will X ship?".
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/roadmap-communication/template.md
---

# Communicate a Roadmap to a Specific Audience

## Purpose
Take an **existing roadmap** and repackage it into a single audience-tailored
communication that lands with one group — executives, engineering, sales/CS, or
customers. The same underlying plan carries different framing, altitude, and
disclosure rules per audience: execs want outcomes and trade-offs, engineering
wants sequencing and dependencies, sales/CS want what to promise and how to
handle asks, customers want value and honest timing. The deliverable protects
the PM from the two classic failure modes — over-committing to dates that become
broken promises, and under-informing so the audience can't act.

**When NOT to use:** building or (re)prioritizing the roadmap itself (use
`roadmap-planning`), or authoring the canonical outcome-based roadmap artifact
(use `outcome-roadmap`). This skill assumes the roadmap already exists and is
agreed; it only *communicates* it. Also not for general stakeholder alignment
absent a roadmap (use an influence/stakeholder skill).

## Inputs
- **Required:** the existing roadmap (themes/outcomes, items, and their
  confidence/timing) **and** the target audience. If the roadmap is missing, do
  not invent items — ask for it or point to `roadmap-planning`. If the audience
  is unnamed, ask which of {exec, engineering, sales/CS, customer} before
  drafting; framing rules diverge too much to guess.
- **Optional:** the communication's purpose/decision (e.g. approve headcount,
  unblock a dependency, renew an account), delivery format (deck, email, portal
  post, all-hands talk), confidentiality constraints (what must not leave the
  building), and known objections or hot questions to pre-empt in the FAQ.

## Output Contract
The deliverable is an **audience-tailored roadmap brief**, structured as (see
`template.md`):

1. **Audience & Intent** — who this is for, the one decision/action it should
   drive, and the disclosure posture (internal-confidential / partner / public).
2. **Headline message** — the single takeaway in ≤ 2 sentences, at the right
   altitude for the audience (outcome for execs/customers; sequencing for eng;
   value + timing for sales/CS).
3. **Message hierarchy** — 3–5 tailored points, most-important first, each tied
   to what *this* audience cares about (not a feature dump).
4. **Commitments vs directional bets** — an explicit two-column split: what is
   **committed** (date/scope you'll stand behind) vs **directional** (exploring,
   no promise). Every dated item names a confidence level.
5. **Reveal / Omit** — what to include for this audience and what to deliberately
   hold back or soften, each with a one-line reason (e.g. "omit internal
   re-platform — no customer value, invites scope questions").
6. **FAQ / objection handling** — 3–6 likely questions or pushbacks with crisp
   answers, including the hardest one ("why isn't *my* thing on here?" /
   "can you commit to Q3?").

Format: prose + the two-column commitments table + the FAQ list. Length: ~1
page. No item is presented as committed unless it is genuinely committed with a
confidence level; directional work is never given a hard date.

**GOOD (excerpt):**
> **Headline (exec):** We're concentrating H1 on activation — the metric gating
> net revenue retention — and deliberately deferring the connector backlog.
>
> | Committed | Directional |
> |---|---|
> | Guided onboarding — GA end of Q2 (high) | AI setup assistant — exploring, no date |
>
> *FAQ — "Can we promise the AI assistant to the Acme renewal?"* No. It's a
> directional bet with no committed date; promise guided onboarding (Q2) instead
> and position the assistant as "on our radar, not yet scheduled."

**BAD (excerpt):**
> "Here's the full roadmap — everything we're building this year, with target
> dates for all 22 items. Share it with whoever asks."
> — fails: no audience framing, no headline, every item flattened to a false
> commitment, nothing omitted, no reveal/omit reasoning, no FAQ.

## Process
1. **Fix audience & intent** — name the audience and the single decision/action
   this communication must drive; set the disclosure posture.
2. **Read the roadmap through their lens** — map each item to what this audience
   cares about; drop what's irrelevant to them.
3. **Write the headline** — one takeaway at the right altitude; if you can't say
   it in two sentences, the intent isn't sharp enough yet.
4. **Order the message hierarchy** — 3–5 points, most-important first, framed in
   the audience's terms.
5. **Split commitments vs directional bets** — put every item in one column;
   attach a confidence level to every date; refuse to date directional work.
6. **Decide reveal vs omit** — for each candidate item, include or hold back with
   a one-line reason; respect the disclosure posture.
7. **Draft the FAQ** — pre-empt the 3–6 hardest questions, especially date-
   pressure and "why not my feature," with answers that don't over-commit.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **audience** and the **one decision/action** it drives are stated up top.
- [ ] There is a single **headline** (≤ 2 sentences) at the audience's altitude.
- [ ] The message hierarchy is **audience-framed and prioritized** — not a flat feature list.
- [ ] **Commitments and directional bets are explicitly separated**; no directional item carries a hard date.
- [ ] **Every dated/committed item has a confidence level.**
- [ ] A **reveal/omit** decision with a one-line reason exists for the sensitive items, consistent with the disclosure posture.
- [ ] The **FAQ** answers the hardest question (date pressure and/or "why isn't my thing here?") without over-committing.
- [ ] If written to a file, it follows `template.md` — all 6 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `roadmap-communication-happy` (happy path) — tailor one roadmap into an exec
  brief with a clean commitments/directional split.
- `roadmap-communication-edge` (edge) — same roadmap re-tailored for a
  customer-facing post, where disclosure rules and reveal/omit dominate.
- `roadmap-communication-adversarial` (adversarial) — sales pressure to commit a
  directional bet to a hard date for a renewal; the skill must refuse and reframe.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `roadmap-planning` — produces and prioritizes the roadmap this skill communicates; upstream dependency.
- `outcome-roadmap` — the canonical outcome-based roadmap artifact this skill reframes per audience.

### External Frameworks
- C. Todd Lombardo et al., *Product Roadmaps Relaunched* (2017) — roadmap-as-communication, the theme/outcome framing, and setting confidence/"disclaimer" expectations rather than committing to a feature-and-date list.
- Marty Cagan, *INSPIRED* — "high-integrity commitments" vs discovery bets: the discipline behind separating what you'll stand behind from what you're still exploring.
- Teresa Torres, *Continuous Discovery Habits* — outcomes-over-outputs framing that keeps audience communication anchored on value, not a feature dump.
