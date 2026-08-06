---
name: business-health-diagnostic
description: >
  Produce a RAG-status (red/amber/green) health verdict across the core
  dimensions of a product business — growth, retention, unit economics,
  engagement, pipeline, and team/delivery — scoring each against thresholds,
  flagging the top risks, and recommending focus areas. Use when assessing
  the overall health of a product or business line, preparing a board or
  leadership health review, triaging where to focus next quarter, or turning a
  pile of metrics into a single "how are we doing" verdict.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/business-health-diagnostic/template.md
---

# Business Health Diagnostic (RAG Scorecard)

## Purpose
Synthesize the scattered metrics of a product business into a single, defensible
**health verdict**: a red/amber/green (RAG) status for each core dimension —
growth, retention, unit economics, engagement, pipeline, and team/delivery — an
overall verdict, the top risks driving any amber/red, and a short list of focus
areas. It answers "how healthy is this business right now, and where should we
look first?" so leaders can triage attention. It **diagnoses** current state; it
does not forecast, plan the fix, or define the metrics themselves.

**When NOT to use:** computing or defining the underlying metrics (use
`saas-revenue-growth-metrics`, `saas-economics-efficiency-metrics`, or
`metrics-dashboard`); root-causing a single failing metric in depth (use a
funnel/retention analysis); or building the remediation plan or roadmap (this
skill names focus areas, it does not sequence the work). This is a synthesized
verdict, not a metric glossary or an action plan.

## Inputs
- **Required:** the metrics for the dimensions being assessed — at minimum a
  growth number (e.g. MoM/YoY revenue or user growth), a retention/churn number,
  and a unit-economics number (e.g. LTV:CAC or gross margin). If none are
  provided, ask for the RAG dimensions' key metrics before scoring; **never
  invent numbers** to fill a dimension.
- **Required:** the business context — stage (seed / growth / scale),
  motion (B2B / B2C / PLG / sales-led), so thresholds are stage-appropriate.
- **Optional:** target or plan values, trend direction (improving/flat/declining),
  prior-period values, benchmark source, and any dimension the user wants
  weighted more heavily. Absent a benchmark, use the default thresholds below and
  **state that they are defaults**.

## Output Contract
The deliverable is a **health scorecard** (see `template.md`), structured as:

1. **Verdict** — one overall RAG status and a one-line summary of why.
2. **Scorecard table** — one row per assessed dimension with columns: Dimension,
   Key metric (value), Threshold applied, RAG, Trend (↑/→/↓). Any dimension with
   no data is marked **Grey / no data**, not guessed.
3. **Top risks** — the 2–4 amber/red items that most threaten the business,
   ranked, each with the number that triggered it and why it matters.
4. **Focus areas** — 2–3 dimensions to concentrate on next, tied to the risks
   (a pointer to where to look, not a project plan).
5. **Scoring notes** — the thresholds used, whether they are defaults or
   benchmark-sourced, and any dimension marked no-data.

Format: one summary line + one table + short ranked lists. Length: ~1 page.
Every RAG call is tied to an explicit threshold and the actual metric value;
no dimension is colored without a number behind it (or is marked Grey/no-data).

**GOOD (excerpt):**
> **Overall: AMBER** — strong growth is masking a retention leak that caps LTV.
>
> | Dimension | Key metric | Threshold | RAG | Trend |
> |---|---|---|---|---|
> | Growth | +14% MoM revenue | ≥10% MoM (growth-stage) | 🟢 | ↑ |
> | Retention | 82% NRR | ≥100% healthy; <90% red | 🔴 | ↓ |
> | Unit economics | LTV:CAC 2.1 | ≥3.0 healthy; <2 red | 🟡 | → |
>
> *Top risk 1: NRR 82% (↓ from 91%) — churn is eroding the base faster than new
> logos add to it; every point of growth costs more. Thresholds: default
> SaaS benchmarks (no customer benchmark provided).*

**BAD (excerpt):**
> "The business looks healthy overall — growth is great and things are trending
> up. We should keep pushing on acquisition."
> — fails: one hand-wavy verdict, no per-dimension RAG, no thresholds, no metric
> values, no ranked risks; colors nothing and cites nothing.

## Process
1. **Frame** — confirm stage and motion; pick the RAG dimensions in scope
   (growth, retention, unit economics, engagement, pipeline, team/delivery).
2. **Gather metrics** — map each dimension to its key metric value and, if
   available, trend and prior value. Mark any dimension without a number as
   **Grey / no data** and do not score it.
3. **Set thresholds** — apply stage-appropriate thresholds; note whether each is
   a customer benchmark or a stated default.
4. **Score each dimension** — assign 🟢/🟡/🔴 by comparing the metric to its
   threshold; record the trend arrow.
5. **Roll up the verdict** — set the overall RAG: any red in a core dimension
   caps the overall at amber-or-worse; explain what the top color is masking.
6. **Rank the risks** — surface the 2–4 amber/red items that most threaten the
   business, each with its triggering number and why it matters.
7. **Name focus areas** — 2–3 dimensions to look at next, tied to the ranked risks.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every scored dimension has a **RAG color**, a **metric value**, and the
      **threshold** that produced the color — no color without a number.
- [ ] Any dimension lacking data is marked **Grey / no data**, never guessed or
      colored.
- [ ] Thresholds are labeled as **customer benchmark** or **stated default**, and
      are appropriate to the given stage/motion.
- [ ] There is **one overall verdict** whose color respects the rollup rule (a red
      core dimension caps the overall at amber-or-worse) and names what a strong
      color may be masking.
- [ ] Top risks are **ranked** (2–4), each tied to a triggering metric and a
      one-line "why it matters".
- [ ] Focus areas (2–3) are **tied to the ranked risks**, not a generic to-do list,
      and stop at "where to look" rather than a project plan.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped
      hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `business-health-diagnostic-happy` — full metric set; growth-green masking a
  retention-red, must produce a correct amber rollup with ranked risks.
- `business-health-diagnostic-edge` — partial data (two dimensions missing) the
  skill must mark Grey/no-data instead of guessing.
- `business-health-diagnostic-adversarial` — "just tell me we're healthy" with
  cherry-picked good metrics; the skill must refuse a green verdict without the
  retention/economics data and flag the gap.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `saas-revenue-growth-metrics` — computes the growth and retention inputs this
  scorecard scores; this skill consumes its numbers, it does not recompute them.
- `saas-economics-efficiency-metrics` — supplies the unit-economics inputs
  (LTV:CAC, payback, margin) scored in the economics dimension.
- `metrics-dashboard` — the standing metric surface; this diagnostic is the
  periodic RAG verdict layered on top of that dashboard's numbers.

### External Frameworks
- David Skok, *SaaS Metrics 2.0* — the canonical retention/LTV:CAC/payback
  benchmarks behind the default thresholds (LTV:CAC ≥ 3, payback ≤ 12 months).
- Andrew Chen, *The Cold Start Problem* — engagement/retention as the leading
  indicator of durable health, informing why retention caps the rollup.
- RAG (Red/Amber/Green) status reporting — the standard programme/portfolio
  health-reporting convention this scorecard adapts to product-business dimensions.
