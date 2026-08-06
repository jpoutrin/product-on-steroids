---
name: ab-test-analysis
description: >
  Analyze A/B test results with statistical significance, sample size validation, confidence intervals, and ship/extend/stop recommendations. Use when evaluating experiment results, checking if a test reached significance, interpreting split test data, or deciding whether to ship a variant.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/ab-test-analysis/template.md
---

# Analyze A/B Test Results

## Purpose
Interpret A/B (and multivariate) test results with statistical rigor — assessing significance, practical magnitude, guardrail impact, and novelty effects — to translate experiment data into a clear go/no-go recommendation (ship, extend, stop, investigate). Supports release decisions, feature prioritization, and experimentation discipline.

**When NOT to use:** designing or planning a new A/B test (use `brainstorm-experiments-existing` for that), understanding longitudinal user behavior (use `cohort-analysis`), or analyzing non-experimental observational data. This skill reads **completed test results**, not historical behavior patterns.

## Inputs
- **Required:** test results data — control and variant metrics (conversions, engagement, revenue, or custom KPIs). Provide raw counts or summary stats (means, sample sizes, p-values). If you have a CSV or raw data export, paste it directly.
- **Optional:** guardrail metrics (metrics that should *not* degrade), minimum practical significance threshold (how much lift matters for the business), test duration and traffic split, novelty/primacy effect considerations, segment-level breakdowns.

## Output Contract
The deliverable is an **A/B test analysis memo** (see `template.md`) with these sections:

1. **Experiment Overview** — hypothesis, what changed, primary metric, guardrail metrics, duration, sample sizes.
2. **Test Validation** — sample size / power check, randomization (SRM), novelty/primacy effect flags.
3. **Statistical Results** — control and variant metrics, relative lift, p-value, 95% confidence interval, significance determination.
4. **Guardrail Check** — status of secondary metrics and why they matter.
5. **Recommendation** — ship / extend / stop / investigate, with reasoning.
6. **Next Steps** — what to do if shipping; if not, how to resolve.

Format: prose + one results table. Length: ~1–2 pages. Every number is cited or calculated step-by-step — no unsupported conclusions.

**GOOD (excerpt):**
> **Statistical Results:**
> | Metric | Control | Variant | Lift | p-value | Significant? |
> |--------|---------|---------|------|---------|--------------|
> | Conversion | 12.3% | 14.1% | +1.8pp | 0.032 | Yes |
> 
> The variant achieved 14.6% relative lift with p < 0.05 and a 95% CI of [+0.3pp, +3.3pp]. The effect is statistically and practically significant (exceeds 1pp business bar). No guardrail concerns.
> 
> **Recommendation:** Ship — roll out to 100%.

**BAD (excerpt):**
> "The test showed our variant is better — it had 15% conversion vs 12%, so we should definitely ship it. No guardrails to worry about."
> — fails: no p-value or sample sizes, missing confidence interval, no novelty effect check, no guardrail confirmation, assumes practical significance without stating business bar.

## Process
1. **Validate the test setup** — check sample size (power ≥ 80%), run duration (≥ 1–2 business cycles), randomization health (SRM < 5%), novelty/primacy wear-off. Flag if test is underpowered.
2. **Calculate statistical metrics** — conversion/engagement rate per arm, relative lift, p-value (two-tailed z-test for proportions or chi-squared for counts), 95% CI, significance call (p < 0.05).
3. **Review guardrail metrics** — confirm secondary KPIs (revenue, engagement, load time, churn) are flat or positive; if degraded, note the trade-off.
4. **Segment breakdown (if data provided)** — report results by user cohort (e.g., new vs. returning, mobile vs. desktop); flag inversions (metric wins in one segment, loses in another).
5. **Issue recommendation** — map result to decision: Significant lift + green guardrails → Ship; lift present but underpowered → Extend; flat/negative result → Stop; lift present but guardrail concern → Investigate.
6. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Test setup is explicitly validated (sample sizes, power, duration, SRM, novelty effect window).
- [ ] Statistical metrics (p-value, 95% CI, relative lift) are calculated and shown step-by-step or via script.
- [ ] Guardrail metrics are explicitly reviewed, and any degradations are flagged and explained.
- [ ] Recommendation (ship / extend / stop / investigate) is tied to quantitative thresholds, not hunches.
- [ ] Segment breakdowns are included if data permits; cross-segment inversions are highlighted.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `ab-test-analysis-happy` (happy path) — straightforward positive result with statistical significance, no guardrail concerns; skill recommends ship.
- `ab-test-analysis-edge` (edge) — result with caveats: positive lift, but guardrail concern or underpowered test; skill recommends investigate or extend.
- `ab-test-analysis-adversarial` (adversarial) — ambiguous or low-power data where recommendation hinges on business context; skill handles gracefully and asks clarifying questions.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `brainstorm-experiments-existing` — designing new tests; consumes the test plan this skill validates post-hoc.
- `cohort-analysis` — longitudinal user behavior and retention; orthogonal to A/B results interpretation.

### External Frameworks
- Ronny Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (2020) — the authoritative text on A/B testing rigor, power analysis, and guardrail discipline.
- [A/B Testing 101 + Examples](https://www.productcompass.pm/p/ab-testing-101-for-pms) — practical PM guide to test interpretation, guardrails, and decision-making.
- [Testing Product Ideas: The Ultimate Validation Experiments Library](https://www.productcompass.pm/p/the-ultimate-experiments-library) — experiment taxonomy and templates.
