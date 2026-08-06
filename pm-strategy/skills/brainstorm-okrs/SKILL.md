---
name: brainstorm-okrs
description: >
  Brainstorm three alternative team-level OKR sets aligned to company strategy —
  an inspirational qualitative Objective plus ~3 measurable, outcome-based Key
  Results each. Use when setting quarterly OKRs, aligning team goals with company
  strategy, drafting objectives, or learning how to write effective OKRs.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/brainstorm-okrs/template.md
---

# Brainstorm Team OKRs

## Purpose
Generate **three distinct, credible OKR sets** for a team, each a qualitative,
inspirational Objective paired with ~3 quantitative, outcome-based Key Results
that ladder up to company strategy. The point is to spark a strategic
prioritization discussion — not to hand down one "right" answer — so the three
options must be genuinely different bets, each defensible on its own.

**When NOT to use:** locking a single final OKR the team will commit to (this
skill diverges; the team converges after), tracking or scoring OKR progress
mid-quarter (that is a review, not drafting), or defining company-level strategy
and North Star (use a strategy/vision skill — OKRs ladder *up* to those, they do
not replace them).

## Inputs
- **Required:** the **team / product area** the OKRs are for, and the **company
  objective or strategy** they must ladder up to. If the company objective is
  missing, ask for it (or the North Star Metric / top company goal) before
  drafting — OKRs unanchored to strategy are worthless; do not invent the
  company goal.
- **Optional:** the **quarter / time horizon** (default: next quarter), current
  baseline metrics (to set credible targets), known KPIs or the North Star
  Metric (Key Results can express expected change in these), strategy docs or
  team context (read and cite them). If no baselines exist, state each target as
  an assumption and flag it.

## Output Contract
The deliverable is an **OKR brainstorm memo** with these sections (see
`template.md`):

1. **Context & Alignment** — the team, the company objective/strategy being
   laddered up to, the quarter, and any baseline metrics or NSM/KPIs in play.
2. **Three OKR Sets** — presented with **equal weight** (no option pre-declared
   the winner). Each set has: an **Objective** (1–2 sentences, qualitative,
   inspirational, time-bound); **~3 Key Results** (each an independently
   measurable *outcome* metric with a target, at a 60–70% confidence stretch);
   and a **2–3 sentence rationale** tying it to the company goal and naming the
   strategic bet it represents.
3. **How to Choose** — 2–4 questions or trade-offs that distinguish the three
   sets, to guide the team's convergence discussion.
4. **Assumptions & Notes** — target assumptions (where no baseline existed),
   data-availability flags, and any metric that is a KPI/NSM vs a one-quarter KR.

Format: prose + clearly delimited OKR blocks. Length: ~1–2 pages. Every Key
Result is an **outcome** (a change in customer/business behavior), never an
output ("ship 5 features"), and is **independently measurable**.

**GOOD (excerpt):**
> **Set A — "Effortless onboarding"** *(bet: activation is the growth lever)*
> **Objective:** Delight new users with an onboarding so smooth they reach value on day one.
> **Key Results:**
> - Onboarding CSAT ≥ 75% (baseline 61%)
> - 66% of signups complete onboarding within 2 days (baseline 41%)
> - Median time-to-value ≤ 20 min (baseline 55 min)
> *Rationale: activation is the biggest drop in the funnel; lifting it ladders directly to the company's "double net-new active teams" objective.*

**BAD (excerpt):**
> **Objective:** Improve the product. **Key Results:** Ship onboarding redesign; launch 5 new features; increase engagement.
> — fails: objective is not inspirational or time-bound; KRs are outputs ("ship", "launch") not measurable outcomes; "increase engagement" has no metric or target; only one set offered, so there is nothing to choose between.

## Process
1. **Anchor to strategy** — restate the company objective / NSM the team must
   serve; if absent, ask for it before proceeding. Read and cite any provided
   strategy or team docs.
2. **Map the levers** — identify the 3–5 outcomes this team most influences and
   how each ladders up to the company goal.
3. **Draft three bets** — turn the levers into three *distinct* Objectives, each
   a different strategic bet (e.g., activation vs retention vs expansion). Keep
   them qualitative, inspirational, and time-bound.
4. **Set Key Results** — for each Objective write ~3 outcome metrics with
   targets at a 60–70% confidence stretch; use baselines where available, else
   label the target an assumption. Note any KR that is also a KPI/NSM change.
5. **Balance the options** — ensure all three are credible and none is an
   obvious throwaway; make them meaningfully different, not paraphrases.
6. **Write the chooser** — surface the 2–4 trade-offs the team should weigh to
   converge.
7. **List assumptions** — target assumptions and data-availability flags.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Exactly **three** OKR sets, presented with **equal weight** (none labeled the winner).
- [ ] Each Objective is **qualitative, inspirational, and time-bound** — not a metric or a task.
- [ ] Each set has **~3 Key Results**, each an **outcome** (not an output) and **independently measurable** with a numeric target.
- [ ] Targets are **ambitious but credible** (~60–70% confidence); each uses a baseline or is **explicitly flagged as an assumption**.
- [ ] Every set's rationale **ladders up to the stated company objective / NSM**.
- [ ] The three sets are **genuinely distinct bets**, not reworded versions of one.
- [ ] A "How to Choose" section gives the team the trade-offs to converge on.
- [ ] If the memo is written to a file, it follows `template.md` — all sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `brainstorm-okrs-happy` (happy path) — a team with a clear company objective and baselines; expects three distinct, outcome-based sets that ladder up.
- `brainstorm-okrs-edge` (edge) — no baselines and a vague company goal; the skill must elicit the anchor and flag every target as an assumption.
- `brainstorm-okrs-adversarial` (adversarial) — user asks for output-based KRs ("KR = launch 5 features"); the skill must reframe to outcomes and refuse output metrics.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `product-vision` — sets the strategic direction and North Star that these OKRs must ladder up to; run it first when the company objective is unclear.
- `market-sizing` — TAM/SAM/SOM context that informs whether growth-oriented Key Result targets are credible.

### External Frameworks
- Christina Wodtke, *Radical Focus* (2016) — the canonical Objective (qualitative, inspirational, time-bound) + ~3 Key Results (quantitative) model, and the weekly commit/confidence cadence behind the 60–70% stretch.
- John Doerr, *Measure What Matters* (2018) — OKR laddering from company to team, and the outcome-over-output discipline.
- [OKR vs KPI: What's the Difference?](https://www.productcompass.pm/p/okr-vs-kpi-whats-the-difference) — how Key Results, KPIs, and the North Star Metric interrelate rather than compete.
