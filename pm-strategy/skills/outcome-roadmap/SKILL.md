---
name: outcome-roadmap
description: >
  Rewrite an output-focused (feature-list) roadmap into an outcome-focused one
  that states customer and business impact, with success metrics and flexible
  release windows. Use when shifting to an outcome roadmap, making a roadmap
  more strategic, rewriting a feature list as outcomes, or preparing a roadmap
  for leadership alignment.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a9
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/outcome-roadmap/template.md
---

# Transform a Roadmap into Outcome-Focused Format

## Purpose
Convert an output-focused roadmap (a list of features/projects by quarter) into
an **outcome-focused roadmap**: each item restated as a measurable customer or
business outcome, with a success metric and a flexible release window. This
clarifies *why* each initiative exists, aligns teams around results rather than
features, and keeps the plan resilient when execution details change.

**When NOT to use:** setting company-level goals or OKRs from scratch (that is
`product-vision` / an OKR skill — this skill assumes the initiatives already
exist), writing a single feature spec/PRD, or detailed delivery scheduling with
hard dates and dependencies (a delivery/execution plan). This skill reframes an
existing roadmap; it does not invent the strategy or the sprint plan.

## Inputs
- **Required:** the current roadmap — the initiatives/features and their
  quarter or phase. If the user hasn't provided one, ask them to paste it (even
  a rough bullet list per quarter is enough). Do not invent initiatives.
- **Optional:** company strategy / objectives or OKRs to align against (map each
  outcome to one), known metrics or baselines (use them instead of placeholders),
  customer segments, and time horizon (default: keep the user's quarters/phases
  but express windows as ranges, not fixed dates).

## Output Contract
The deliverable is an **outcome roadmap** with these sections (see `template.md`):

1. **Strategic Context** — 2–4 lines: the strategy/objectives the roadmap serves
   and the key customer-need assumptions the outcomes bet on.
2. **Outcome Roadmap (by quarter/phase)** — for each period, a table with one row
   per initiative: the **original output**, the **outcome statement**, and the
   **success metric**. Outcome statements use the format
   *Enable [customer segment] to [desired outcome] so that [business impact]*.
3. **Metrics & Sequencing** — the leading/lagging metric per outcome (or a note
   that a baseline is TBD) plus dependencies or sequencing notes.
4. **Assumptions & Flexibility** — the customer-need assumptions each outcome
   rests on, and an explicit note that windows are ranges (quarters, not dates).

Format: short prose + one table per period. Length: ~1–2 pages. Every outcome is
**measurable** (names a metric or an explicit "baseline TBD"), and every release
window is a **range/quarter**, never a hard calendar date presented as a commitment.

**GOOD (excerpt):**
> **Q2** · Output: *Build advanced search filters & AI recommendations*
> → Outcome: **Enable shoppers to find the right product 50% faster so that
> conversion on search sessions rises.** Metric: median search-to-purchase time
> (baseline 4.1 min → target 2.0 min); search-session conversion +3pp.
> *Assumption: slow product discovery is a top-3 driver of search abandonment.*

**BAD (excerpt):**
> "Q2 (Apr 14): Ship search filters, AI recommendations, dashboard redesign."
> — fails: still a feature list on a hard date, no customer/business outcome, no
> metric, no "so that…" — a reader can't tell what success looks like.

## Process
1. **Read the roadmap** — list every initiative with its quarter/phase exactly as given.
2. **Align to strategy** — if objectives/OKRs were provided, note which each initiative serves; capture the strategic context.
3. **Interrogate each output** — ask "so what?" until you reach real customer/business value: what problem does it solve, what changes for the user, which metric moves?
4. **Rewrite as an outcome** — *Enable [segment] to [desired outcome] so that [business impact]*; collapse multiple outputs serving one outcome into a single outcome row.
5. **Attach a metric** — a leading/lagging measure with a baseline→target, or an explicit "baseline TBD" — never leave an outcome unmeasurable.
6. **Set flexible windows** — keep the user's quarters/phases but express timing as ranges, not committed dates; note dependencies and sequencing.
7. **Surface assumptions** — state the customer-need bet each outcome rests on so it can be challenged.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every original output has a corresponding **outcome statement** in the *Enable … to … so that …* form (customer outcome **and** business impact both present).
- [ ] Every outcome names a **success metric** (baseline→target) or an explicit "baseline TBD" — none is left unmeasurable.
- [ ] No outcome is a disguised feature ("ship X", "build Y"); each survives the "so what?" test.
- [ ] Release windows are **ranges/quarters**, not hard calendar dates presented as commitments.
- [ ] Outcomes are mapped to the provided strategy/objectives (or their absence is flagged as an assumption to confirm).
- [ ] Key **customer-need assumptions** are stated so they can be challenged.
- [ ] If the roadmap is written to a file, it follows `template.md` — all 4 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `outcome-roadmap-happy` (happy path) — a full feature-list roadmap with baselines; produces measurable outcome rows.
- `outcome-roadmap-edge` (edge) — features with no baselines/metrics; must add "baseline TBD" placeholders and name the metric, not skip it.
- `outcome-roadmap-adversarial` (adversarial) — vanity/hard-date "roadmap" the skill must reframe, strip the committed dates, and refuse to leave as a feature list.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `product-vision` — supplies the strategy/objectives this skill aligns each outcome to; run it first when the strategic context is missing.
- `market-sizing` — the market opportunity that justifies which business outcomes are worth targeting.

### External Frameworks
- Josh Seiden, *Outcomes Over Output* (2019) — the definition of an outcome (a change in customer behavior that drives business results) that this skill's "so what?" test operationalizes.
- Marty Cagan, *Inspired* / SVPG — outcome-based roadmaps and the argument against feature-list "output" roadmaps.
- John Doerr, *Measure What Matters* — Objectives & Key Results as the metric spine each outcome row hangs its success measure on.
