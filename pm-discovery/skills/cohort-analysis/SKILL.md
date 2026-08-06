---
name: cohort-analysis
description: >
  Analyze user retention and behavior across time-based cohorts to identify
  retention curves, aha moments, and churn drivers. Use when analyzing user
  retention by acquisition cohort, studying feature adoption over time,
  investigating churn patterns, or identifying engagement trends.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/cohort-analysis/template.md
---

# Cohort Analysis & Retention Explorer

## Purpose
Interpret user engagement and retention patterns by time-based cohort (weekly/monthly
acquisition groups) to identify retention curves, feature-adoption inflection points,
churn drivers, and product recommendations — grounded in cohort-level quantitative
findings and validated against qualitative research needs. Supports product roadmap,
activation/retention, and feature prioritization decisions.

**When NOT to use:** A/B test or experiment analysis (use `ab-test-analysis`), SQL query
authoring or data retrieval (use `sql-queries`), or general time-series forecasting
(use analytics forecasting skills). This skill interprets *ready* cohort data, not
fetches or compares experiments.

## Inputs
- **Required:** user engagement/retention data in tabular form (CSV, Excel, JSON, or
  pasted) with cohort identifiers (signup week/month), time periods, and retention or
  engagement metrics (e.g., % active, DAU, feature usage).
- **Optional:** product context (feature launches, pricing changes, UX updates during
  the period), expected churn drivers, minimum cohort size threshold, and desired
  output format (heatmap, line chart, written report, or Python analysis script).

## Output Contract
The deliverable is a **cohort analysis report** with these sections (see `template.md`):

1. **Data Summary** — cohort overview (date range, cohort sizes, metrics available),
   data quality assessment (missing values, anomalies), and a numerical snapshot.
2. **Retention Curves** — quantified retention over time, key drop-off points, and
   cohort-to-cohort comparison (table or prose).
3. **Key Inflection Points** — notable changes in retention/engagement, feature
   adoption aha moments, and cohort differences (numbered list with magnitudes).
4. **Churn Drivers & Patterns** — hypothesized root causes tied to data (early vs.
   late churn, segment-level variation, correlation with product changes).
5. **Product Recommendations** — 2–4 prioritized actions grounded in findings (e.g.,
   improve onboarding, test feature adoption, run qualitative research).
6. **Follow-Up Research** — specific qualitative (interviews, surveys) and quantitative
   (cohort experiments, segmentation) next steps to validate patterns.

Length: ~1–2 pages. Format: structured prose + 1–2 summary tables/visuals. Every
assertion ties to data or is flagged a hypothesis.

**GOOD (excerpt):**
> **Key Finding:** Jan 2025 cohort (n=1,247) shows 40% Week-1 → Week-4 churn vs.
> 22% for Dec 2024 (n=1,892). Onboarding flow changed Jan 1. **Hypothesis:** new
> email-verification step adds friction. **Next step:** Interview 10 Jan cohort
> churned users to confirm.

**BAD (excerpt):**
> "Retention is declining in newer cohorts. We should improve the product."
> — fails: no numbers, no cohort-to-cohort comparison, no specific churn driver,
> no testable recommendation.

## Process
1. **Ingest & validate** — read the user's cohort data, verify structure, flag
   missing periods or cohort misalignment, summarize cohort sizes and date ranges.
2. **Calculate retention** — compute period-over-period retention rates (e.g., Week 2
   retention = active in Week 2 / cohort size), identify inflection points (biggest
   drops), and compare cohorts (older vs. newer).
3. **Spot patterns** — surface anomalies (sudden drops, seasonal swings, cohort
   divergence), correlate with product changes if the user provided context.
4. **Generate recommendations** — map findings to 2–4 priority actions tied to data
   (reduce early churn, drive adoption, investigate segment differences).
5. **Design follow-ups** — suggest specific qualitative (who, what, when) and
   quantitative (cohort experiment, funnel drill-down) research to validate.
6. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Retention curves or engagement trends are **quantified with actual data**
  (not guesses or round numbers).
- [ ] At least two cohorts are **compared** to surface differences (older vs. newer,
  pre- vs. post-launch).
- [ ] Inflection points (biggest drops or adoption jumps) are **named and tied to
  magnitudes** (e.g., "40% drop Week 1 → 4").
- [ ] Churn drivers and patterns are **either data-backed or explicitly flagged as
  hypotheses** requiring follow-up research.
- [ ] Product recommendations are **specific and testable** (not vague; tied to
  findings, not guesses).
- [ ] Follow-up research includes both **qualitative** (interviews, surveys) and
  **quantitative** (experiments, segmentation) next steps.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped
  hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `cohort-analysis-happy` (happy path) — clean monthly retention data, clear
  cohort divergence, product-launch correlation to identify.
- `cohort-analysis-edge` (edge) — sparse data (small cohorts, missing weeks),
  multiple metrics (DAU, feature adoption, churn), skill must summarize and flag
  limitations.
- `cohort-analysis-adversarial` (adversarial) — vague ask ("analyze our retention")
  with no data or context attached; skill must ask clarifying questions.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `ab-test-analysis` — interprets A/B experiment results; cohort-analysis interprets
  historical user cohorts.
- `sql-queries` — retrieves and structures cohort data; this skill interprets it.
- `retention-funnel` — deep-dive into a single churn point; cohort-analysis scans
  across all retention periods.

### External Frameworks
- [AARRR Metrics (Pirate Metrics)](https://www.reforge.com/blog/aarrr-metrics) —
  Activation and Retention focus; cohort analysis fuels these metrics.
- [Cohort Analysis 101: How to Reduce Churn and Make Better Product Decisions](https://www.productcompass.pm/p/cohort-analysis) —
  product-compass walkthrough of methods and pitfalls.
- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr) —
  how cohort analysis fits into broader product analytics.
