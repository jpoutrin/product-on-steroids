---
name: derisk-measurement-advisor
description: >
  Use when you have chosen a specific assumption to test and need to design a
  rigorous measurement plan — defining the primary metric, leading indicators,
  guardrail metrics, baseline, success threshold, minimum sample size or
  duration, and an inconclusive protocol before running the experiment.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/derisk-measurement-advisor/template.md
---

# Derisk Measurement Advisor

## Purpose
Produce a **Measurement Advisory** for a specific assumption under test —
specifying exactly what data to collect, what numbers signal the assumption is
resolved (either direction), how long or how many users you need, and what to
do when results are ambiguous. The output bridges the gap between knowing which
assumption is riskiest and actually closing it with evidence.

**When NOT to use:**
- Surfacing or ranking which assumptions to test — use `identify-assumptions`
  or `prioritize-assumptions` first.
- Generating experiment ideas — use `brainstorm-experiments-*` to choose an
  experiment type; then bring the chosen experiment here to design its
  measurement.
- Interpreting results after the experiment has already run — use
  `ab-test-analysis` or a similar results-interpretation skill.
- Assumptions that have already been validated or killed; this skill designs
  measurement plans for open assumptions only.

## Inputs
- **Required:** the assumption under test, stated clearly (one sentence). If
  the user provides a vague risk ("we assume users want this"), reflect it back
  and ask for the falsifiable form before proceeding.
- **Required:** the experiment or data-collection method chosen (survey,
  A/B test, fake-door, prototype usability study, etc.). If not provided, ask
  which method the team plans to use; do not invent one.
- **Optional:** current baseline metrics or known data — used to anchor the
  target threshold. If absent, the advisor notes where baselines must be
  established before the test begins.
- **Optional:** constraints — time box, budget, team capacity, regulatory
  limits on data collection, minimum detectable effect. The advisor factors
  these into the sample-size and duration estimate.
- **Optional:** context on the product stage (pre-launch, beta, GA) and user
  pool size — shapes what statistical rigor is achievable.

## Output Contract
The deliverable is a **Measurement Advisory** for a specific assumption,
structured as (see `template.md`):

1. **Assumption Under Test** — the assumption restated in its falsifiable form,
   plus the null hypothesis (what "not de-risked" looks like).
2. **Primary Metric** — the single number that will determine pass/fail; its
   definition, unit, and how it is collected.
3. **Leading Indicators** — two to four early signals readable before the
   primary metric is statistically conclusive, with the earliest time point
   each becomes readable.
4. **Guardrail Metrics** — two to three metrics that must NOT degrade during
   the test; each with its acceptable floor/ceiling.
5. **Baseline & Target** — the current measured (or estimated) baseline for
   the primary metric, the minimum success threshold, and, where relevant, the
   minimum detectable effect.
6. **Sample Size / Duration** — the minimum number of participants or days to
   reach the stated statistical power (default 80 % power, α = 0.05) or, for
   qualitative assumptions, the saturation logic used.
7. **Inconclusive Protocol** — what the team does if results fall between
   pass and fail thresholds after the full test window: extend, pivot, accept
   uncertainty, or escalate.

Format: structured prose under seven `##` headers, one summary table under
section 5 (Baseline & Target). Length: ~1–1.5 pages. Every threshold is
justified; sample-size calculations show the key inputs (baseline rate, MDE,
power, α). For qualitative assumptions, statistical language is replaced with
saturation and confidence-level reasoning.

**GOOD (excerpt):**
> **Primary Metric:** Free-to-paid conversion rate within 14 days of account
> creation, measured via payment-event attribution in the billing system.
> **Baseline:** 3.2 % (last 90 days, n = 4 800 accounts). **Target:** ≥ 5.0 %
> (56 % relative lift). **Minimum sample:** 1 740 per variant (80 % power,
> α = 0.05, two-tailed). At current traffic of ~200 signups/day, run for
> ≥ 9 days per variant.

**BAD (excerpt):**
> "We'll run the experiment for a week with 50 users. If conversion goes up,
> we'll call it de-risked."
> — fails: no baseline, no stated threshold, 50 users is almost certainly
> underpowered for a conversion-rate change, and "goes up" is not a
> falsifiable criterion.

## Process
1. **Restate the assumption** — convert vague risk language into a falsifiable
   statement. If the user's input is not falsifiable (e.g., "users will trust
   us more"), translate it into proxy metrics and flag the translation
   explicitly.
2. **Identify the primary metric** — choose the one metric most directly
   connected to the assumption. Prefer metrics that are (a) directly observable
   or measurable, (b) attributable to the experiment, and (c) readable within
   the test window. Name the data source and collection method.
3. **Select leading indicators** — find two to four signals that move before
   the primary metric is conclusive. These serve as early-warning or
   early-confirmation signals. Note when each becomes readable.
4. **Define guardrail metrics** — identify what must not break. Typical
   guardrails: engagement depth, retention, support ticket rate, NPS / CSAT,
   revenue from non-test segments. Set a floor or ceiling for each.
5. **Establish baseline and target** — document the current state of the
   primary metric (from historical data or a baseline measurement period).
   Set the minimum success threshold using business impact logic or a minimum
   detectable effect. Build a summary table.
6. **Calculate sample size / duration** — for quantitative assumptions, apply
   a two-sample proportions or means test at 80 % power, α = 0.05, showing
   the key inputs. For qualitative assumptions (user-trust, perception), use
   saturation logic (typically 5–8 interviews per segment, ≥ 3 segments) and
   note confidence-level instead of p-values.
7. **Write the inconclusive protocol** — define the decision rule if results
   fall between pass and fail after the test window: extend (if traffic allows
   and effect is trending), pivot experiment design, accept uncertainty and
   treat the assumption as partially de-risked, or escalate to a stakeholder
   decision.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The assumption is stated in **falsifiable form** — a clear pass/fail
  criterion, not a vague hope.
- [ ] The **primary metric** is named with its definition, unit, and data
  source — not just "conversion rate" but whose, over what window, from what
  funnel stage.
- [ ] **Baseline** is provided (measured or estimated) and the **success
  threshold** is justified with business logic or a stated MDE — not a
  round-number guess.
- [ ] **Sample size or duration** is derived from the baseline, MDE, power,
  and α — the inputs are visible, not just the conclusion.
- [ ] For **qualitative assumptions**, statistical language is replaced with
  saturation and confidence-level reasoning; the advisor is explicit about
  the limitation.
- [ ] **Guardrail metrics** are listed with explicit floors/ceilings — not
  just named.
- [ ] The **inconclusive protocol** covers what happens if results are between
  pass and fail after the full window — it does not skip this case.
- [ ] If the output is written to a file, it follows `template.md` — all
  seven sections present, in order, headings matching (a skill-scoped hook
  re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `derisk-measurement-advisor-happy` — SaaS freemium conversion assumption
  with a chosen A/B experiment; expects a complete, statistically grounded plan.
- `derisk-measurement-advisor-edge` — qualitative/unmeasurable assumption
  ("users will trust us more"); advisor must translate to proxy metrics and
  be transparent about limitations.
- `derisk-measurement-advisor-adversarial` — PM wants to declare the
  assumption de-risked after one week with 50 users; advisor must flag
  insufficient power and prescribe correct thresholds.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `prioritize-assumptions` — ranks which assumptions to test next; hands off
  the chosen assumption to this skill for measurement design.
- `brainstorm-experiments-*` — generates experiment options; this skill
  designs the measurement plan once an experiment type is chosen.
- `ab-test-analysis` — interprets results after an experiment completes; this
  skill designs measurement before the experiment runs.
- `identify-assumptions` — surfaces hidden assumptions; this skill measures
  a specific one.

### External Frameworks
- Evan Miller, [*How Not To Run an A/B Test*](https://www.evanmiller.org/how-not-to-run-an-ab-test.html) — canonical warning against peeking and underpowered tests; directly shapes the sample-size and inconclusive-protocol steps.
- Ron Kohavi, Diane Tang & Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge, 2020) — guardrail metrics, novelty effects, and minimum-detectable-effect framing used in steps 4–6.
- Teresa Torres, *Continuous Discovery Habits* (2021) — assumption mapping and the falsifiability discipline that underpins step 1 of this skill's process.
- Jacob Cohen, *Statistical Power Analysis for the Behavioral Sciences* (2nd ed., 1988) — theoretical basis for the 80 % power / α = 0.05 defaults and the two-sample test used in step 6.
