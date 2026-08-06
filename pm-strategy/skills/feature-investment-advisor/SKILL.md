---
name: feature-investment-advisor
description: >
  Recommend how to allocate product effort across a portfolio of areas/bets —
  invest, maintain, or divest each — with a horizon mix (H1/H2/H3) and a % of
  capacity per theme, argued as an advisor rather than a ranked list. Use when
  allocating engineering/product capacity across a portfolio, deciding where to
  double-down vs. wind down, setting a horizon (H1/H2/H3) balance, or defending a
  bet portfolio to leadership.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/feature-investment-advisor/template.md
---

# Portfolio Investment Advice (Allocate Effort Across Bets)

## Purpose
Advise how to **allocate finite product/engineering capacity across a portfolio**
of investment areas (themes, bets, product lines) — recommending for each a
disposition (**invest / maintain / divest**), the resulting **% of capacity**,
and a **horizon mix** (H1 run-the-business / H2 grow / H3 explore). The output is
an advisor's recommendation with reasoning and trade-offs, so a leadership team
can decide *where the effort goes*, not merely *what order to build in*.

**When NOT to use:** ranking or sequencing a single backlog of features (use
`prioritize-features`), choosing which scoring framework to apply (use
`prioritization-frameworks`), or sizing a single market (use `market-sizing`).
This skill sits **above** the backlog — it decides how much fuel each area gets,
then hands the chosen areas to those skills to plan the work inside them.

## Inputs
- **Required:** the **portfolio of areas/bets** and, per area, at least a rough
  read on **ROI / value**, **strategic fit**, and **risk** (qualitative is fine).
  If the user gives a flat feature list instead of areas, first group it into
  3–7 themes and confirm; if fit/risk are missing for an area, ask for a
  high/med/low read rather than inventing one. Total available **capacity**
  (teams, headcount, or %) is required to allocate against — if absent, allocate
  in percentages and say so.
- **Optional:** current baseline allocation (to compare against and quantify the
  shift), target horizon balance or a mandate (e.g. "protect the core, but 20%
  to new bets"), time window (default: next 2–4 quarters), constraints
  (must-keep commitments, contractual/compliance floors), risk appetite.

## Output Contract
The deliverable is a **portfolio investment memo** with these sections (see
`template.md`):

1. **Portfolio at a glance** — the 3–7 areas, each tagged with ROI/value,
   strategic fit, risk (high/med/low), and its **disposition** (invest /
   maintain / divest). One table.
2. **Allocation recommendation** — recommended **% of capacity per area** that
   sums to 100%, shown **vs. the current baseline** (delta per area), with the
   headline shift stated in one sentence.
3. **Horizon mix** — the recommended **H1 / H2 / H3 split** (must sum to 100%),
   the rationale, and how it compares to any mandate or healthy-balance heuristic.
4. **Rationale per disposition** — for each area, 1–3 sentences of *advisor
   voice* on **why** invest/maintain/divest, naming the ROI-vs-fit-vs-risk
   trade-off that drove it (not just a restated score).
5. **What we are deliberately NOT funding** — the divest/starve calls made
   explicit, with the freed capacity and where it is redeployed.
6. **Risks & revisit triggers** — the top portfolio risks and the **leading
   signals** that should trigger reallocation before the next cycle.

Format: prose + two small tables (allocation, horizon). Length: ~1–2 pages.
Every allocation figure is a number that ties back to a stated capacity; every
disposition carries a reason, not just a label. Advisor voice throughout — this
recommends and defends a shape; it is **not** a ranked feature list.

**GOOD (excerpt):**
> **Shift:** move ~15 pts of capacity from *Legacy Reporting* (**divest**, ROI
> low / fit low / risk low) into *Usage-Based Billing* (**invest**, ROI high /
> fit high / risk med).
>
> | Area | Disposition | Now → Rec | Δ |
> |------|-------------|-----------|---|
> | Core Platform | maintain | 40% → 40% | 0 |
> | Usage-Based Billing | invest | 15% → 30% | +15 |
> | Legacy Reporting | divest | 20% → 5% | −15 |
>
> **Horizon:** 60 / 30 / 10 (H1/H2/H3) — we hold H1 to protect the core, and
> the +15 into Billing is an H2 grow bet, not an H3 experiment, because two
> enterprise deals already gate on it.
> *Not funding:* Legacy Reporting beyond keep-the-lights-on; the 15 pts freed is
> the entire source of the Billing increase.

**BAD (excerpt):**
> "1. Usage-based billing (RICE 92)  2. SSO (RICE 80)  3. Reporting (RICE 44)…"
> — fails: this is a ranked backlog, not a portfolio allocation. No %-of-capacity,
> no invest/maintain/divest, no horizon mix, no advisor reasoning, nothing
> deliberately un-funded. That is `prioritize-features`, not this skill.

## Process
1. **Frame the portfolio** — resolve inputs into 3–7 areas; if given a flat
   backlog, group into themes and confirm before proceeding.
2. **Read each area** on ROI/value, strategic fit, and risk (high/med/low); flag
   any read that is an assumption rather than evidence.
3. **Assign a disposition** per area — invest / maintain / divest — from the
   ROI×fit×risk pattern (high-fit high-ROI → invest; low-fit low-ROI → divest;
   proven core → maintain; high-risk high-upside → a bounded H3 bet).
4. **Allocate capacity** — set % per area summing to 100%, anchored to real
   capacity; compute the delta vs. the current baseline and the headline shift.
5. **Set the horizon mix** — choose an H1/H2/H3 split (summing to 100%) that
   respects any mandate and keeps a healthy run/grow/explore balance; justify it.
6. **Make the divests explicit** — state what is being starved, the freed
   capacity, and where it is redeployed (nothing vanishes).
7. **Name risks & revisit triggers** — top portfolio risks and the leading
   signals that should force reallocation mid-cycle.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every area carries a **disposition** (invest / maintain / divest), not just a score.
- [ ] The **allocation %** across areas **sums to 100%** and is shown **against the current baseline** with a per-area delta.
- [ ] Allocation is tied to a **stated capacity** (teams/headcount/%), not floating numbers.
- [ ] The **horizon mix (H1/H2/H3) sums to 100%** and is justified against any mandate or a run/grow/explore heuristic.
- [ ] Each disposition has an **advisor-voice reason** naming the ROI-vs-fit-vs-risk trade-off — not a restated number.
- [ ] At least one **divest/not-funding** call is made explicit, with freed capacity redeployed (unless the portfolio is genuinely all-invest, stated so).
- [ ] The output reads as **allocation advice**, not a ranked backlog; it does not sequence individual features.
- [ ] Risks each carry a **leading revisit signal**, not just a description.
- [ ] If written to a file, it follows `template.md` — all 6 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `feature-investment-advisor-happy` (happy path) — a portfolio with clear
  ROI/fit/risk reads and a baseline; must produce dispositions, a summed
  allocation with deltas, and a justified horizon mix.
- `feature-investment-advisor-edge` (edge) — a mandate constraint ("protect the
  core, ≥15% to new bets") that must bind the horizon mix and force a divest to
  fund it.
- `feature-investment-advisor-adversarial` (adversarial) — a flat RICE-ranked
  backlog handed in expecting a re-rank; the skill must reframe to portfolio
  allocation and refuse to just reorder features.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `prioritize-features` — ranks/sequences the backlog *inside* an area once this skill has decided how much capacity that area gets.
- `prioritization-frameworks` — supplies the scoring lens (RICE/WSJF/etc.) that produces the per-area ROI reads this skill allocates against.
- `market-sizing` — the TAM/SAM/SOM behind an area's ROI/value input.

### External Frameworks
- McKinsey **Three Horizons of Growth** (Baghai, Coley, White, *The Alchemy of Growth*, 1999) — the H1/H2/H3 run-grow-explore balance this skill recommends.
- **BCG Growth–Share Matrix** — invest/maintain/divest dispositions map to the star/cash-cow/dog/question-mark quadrants.
- Boston-style **portfolio / horizon budgeting** and Ravi Mehta's *Product Strategy* quadrant — capacity-allocation-across-bets framing that distinguishes this from single-backlog prioritization.
