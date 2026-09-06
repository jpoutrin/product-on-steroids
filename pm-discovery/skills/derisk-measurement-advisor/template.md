# Measurement Advisory: <Assumption Under Test — one line>

## Assumption Under Test
<!-- Restate the assumption in its falsifiable form. -->
**Assumption:** <falsifiable statement, e.g., "At least 5 % of free users will
upgrade to a paid plan within 14 days when shown the new pricing modal.">

**Null hypothesis (not de-risked):** <what it looks like if the assumption is
wrong, e.g., "Upgrade rate remains below 5 % or is indistinguishable from the
control.">

## Primary Metric
<!-- The one number that signals pass or fail. -->
**Metric:** <name and definition>
**Unit:** <%, count, median time, etc.>
**Data source & collection method:** <e.g., billing-event attribution in
Stripe; server-side event "subscription.created" within 14 days of
account_created>
**Measurement window:** <e.g., 14 days post-exposure>

## Leading Indicators
<!-- 2–4 early signals readable before the primary metric is conclusive.
     For each: signal name, earliest readable time point, what it tells you. -->

| Leading Indicator | Earliest readable | What it signals |
|-------------------|------------------|-----------------|
| <indicator>       | <e.g., day 2>    | <early confirmation or warning> |
| <indicator>       | <e.g., day 5>    | <early confirmation or warning> |
| <indicator>       | <e.g., day 7>    | <early confirmation or warning> |

## Guardrail Metrics
<!-- 2–3 metrics that must NOT degrade. Each needs an explicit floor or ceiling. -->

| Guardrail Metric | Acceptable floor/ceiling | Rationale |
|------------------|--------------------------|-----------|
| <metric>         | <e.g., ≥ 40 % D7 retention> | <why this matters> |
| <metric>         | <e.g., < 2 % refund rate> | <why this matters> |
| <metric>         | <e.g., NPS ≥ 35>           | <why this matters> |

## Baseline & Target
<!-- Current measured (or estimated) state → success threshold. -->

| | Current baseline | Success threshold | Minimum detectable effect |
|-|-----------------|------------------|--------------------------|
| **Primary metric** | <e.g., 3.2 %>  | <e.g., ≥ 5.0 %>  | <e.g., 1.8 pp absolute>  |

**Baseline source:** <e.g., 90-day rolling average, n = 4 800 accounts>

**Threshold justification:** <one to two sentences explaining why this number
represents meaningful de-risking — business impact or unit-economics logic.>

## Sample Size / Duration
<!-- For quantitative assumptions: show the key inputs. -->
**Statistical approach:** <e.g., two-sample proportions test, two-tailed>
**Power:** <e.g., 80 %> | **α:** <e.g., 0.05>
**Baseline rate:** <e.g., 3.2 %> | **MDE:** <e.g., 1.8 pp> | **Relative lift:** <e.g., 56 %>

**Minimum sample per variant:** <n, with calculation reference or tool used>
**Current traffic:** <e.g., ~200 signups/day>
**Minimum run duration:** <e.g., 9 days per variant = 18 days total>

<!-- For qualitative assumptions: replace the block above with saturation logic. -->
<!-- **Saturation approach:** <e.g., 6 interviews per segment × 3 segments = 18
     sessions; stop when 2 consecutive sessions yield no new themes.>
     **Confidence level at saturation:** <low/medium/high — explain.> -->

## Inconclusive Protocol
<!-- What the team does if results fall between pass and fail after the full
     test window. Cover all three branches: extend, pivot, or accept. -->

**Define "inconclusive":** Results where the primary metric is <between X and
Y> after the full run window and the confidence interval is wide enough to
contain both the null and the success threshold.

**If inconclusive:**
1. **Extend (preferred if):** <condition, e.g., the point estimate is trending
   upward and traffic allows a 50 % extension without novelty-effect bias>.
   Extend by: <e.g., one additional week; re-evaluate at that point only>.
2. **Pivot experiment design (if):** <condition, e.g., the leading indicators
   suggest the assumption is correct but the experiment design is not isolating
   it — e.g., too much contamination between variants>.
3. **Accept uncertainty (default):** Treat the assumption as **partially
   de-risked**: proceed with a reduced confidence level, flag as a monitored
   risk, and set a post-launch review trigger at <milestone or date>.
4. **Escalate (if):** <condition, e.g., business decision requires a go/no-go
   before results are conclusive — bring raw trend data to stakeholders and
   document the residual risk explicitly>.
