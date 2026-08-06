---
name: metrics-dashboard
description: >
  Design a product metrics dashboard as a metric tree — North Star, its input
  levers, health guardrails, and business metrics — with a definition, cadence,
  owner, target, and alert threshold per metric. Use when designing a metrics
  dashboard, defining a North Star and its inputs, instrumenting a product for
  analytics, or building a KPI monitoring plan.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/metrics-dashboard/template.md
---

# Design a Product Metrics Dashboard

## Purpose
Produce a **dashboard specification** for a product: a metric tree that ties a
single North Star Metric (NSM) to the 3–5 input levers that drive it, the health
guardrails that keep the NSM from being gamed, and the business metrics that
translate it to revenue. Every metric is fully defined — exact formula, review
cadence, accountable owner, target, and alert threshold — organized by the
product's funnel/lifecycle so a team can instrument and monitor it. Supports
instrumentation, weekly/monthly reviews, and OKR tracking.

**When NOT to use:** you need metric *definitions or benchmarks* rather than a
dashboard design (use `saas-revenue-growth-metrics`, `saas-economics-efficiency-metrics`,
or `finance-metrics-quickref`); you're picking the NSM's underlying *strategy*
(use `product-vision`); or you're running a single funnel-drop investigation
(that's analysis, not dashboard design). This skill designs the artifact; it does
not query live data.

## Inputs
- **Required:** the product and its core value moment — what the product does and
  the single action where a user gets value (the NSM anchor), plus the business
  model (B2B/B2C, subscription/transactional). If missing, ask for the product,
  its value moment, and business model before designing; do not invent an NSM.
- **Optional:** existing NSM or KPIs, the funnel/lifecycle stages (default: AARRR
  — Acquisition, Activation, Retention, Referral, Revenue), current OKRs or
  strategy docs (read and align to them), available analytics tooling, and any
  known baseline values or targets.

## Output Contract
The deliverable is a **dashboard specification** with these sections (see
`template.md`):

1. **North Star Metric** — the single metric, its exact formula, why it captures
   core value delivery (leading indicator of business success), and its target.
2. **Metric Tree** — the NSM decomposed into 3–5 **input metrics** (the levers
   that move it), each mapped to a funnel/lifecycle stage; show the arithmetic or
   causal link from inputs up to the NSM.
3. **Metric Definitions table** — one row per metric (NSM, inputs, health,
   business) with columns: Metric · Layer · Formula (numerator/denominator + time
   window) · Cadence · Owner · Target · Alert Threshold.
4. **Health Guardrails** — 2–4 counter-metrics that ensure the NSM isn't gamed
   (e.g. latency, error rate, complaint/NPS), each with a threshold.
5. **Business Metrics** — the revenue/cost/unit-economics layer (e.g. MRR, CAC,
   LTV, churn) linking the product metric tree to the business.
6. **Review Cadence & Alerts** — what is reviewed daily/weekly/monthly/quarterly,
   and for each alert: threshold, who is notified, channel, and response time.

Format: prose + one metric table + a metric-tree sketch. Length: ~1–2 pages.
Every metric is **actionable** (would change a decision) and defined as a
**ratio/rate over a time window**, never a raw vanity count.

**GOOD (excerpt):**
> **North Star:** Weekly Active Teams that shipped ≥1 doc = `# teams with ≥1 publish event / rolling 7 days`. Target: 1,200 (from 940).
> **Metric Tree:** NSM ← Activation (`% new teams reaching first publish ≤7d`, Owner: Growth, target 45%) × Retention (`% W1 teams active in W4`, Owner: PM-Core, 60%).
>
> | Metric | Layer | Formula | Cadence | Owner | Target | Alert |
> |---|---|---|---|---|---|---|
> | Publish latency p95 | Health | p95 ms, publish endpoint, 5-min window | Daily | SRE | <800ms | >1.5s 10min → #oncall |

**BAD (excerpt):**
> "North Star: total signups (up and to the right!). Also track page views, MRR, and NPS."
> — fails: NSM is a vanity cumulative count, not a value-moment rate; no metric tree linking inputs to the NSM; no formulas, owners, cadences, or thresholds; metrics are an unstructured list, not layered.

## Process
1. **Anchor the NSM** — from the product's core value moment, define one
   customer-centric metric as a rate/ratio over a window; write its exact formula
   and target; confirm it's a leading indicator, not a lagging vanity total.
2. **Build the metric tree** — decompose the NSM into 3–5 input levers, each tied
   to a funnel/lifecycle stage; show the arithmetic or causal path inputs → NSM.
3. **Add health guardrails** — pick 2–4 counter-metrics that would catch the NSM
   being gamed or the product degrading.
4. **Add business metrics** — the revenue/cost/unit-economics layer linking the
   tree to business outcomes.
5. **Define every metric** — fill the table: formula (numerator/denominator +
   window), cadence, owner, target, alert threshold — no blank cells.
6. **Set cadence & alerts** — assign each metric a review rhythm; for each alert
   name threshold, audience, channel, and response time.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Exactly **one** North Star Metric, expressed as a rate/ratio over a time window and tied to the product's value moment — not a cumulative vanity count.
- [ ] The NSM decomposes into **3–5 input metrics**, each mapped to a funnel/lifecycle stage, with the input→NSM link made explicit.
- [ ] There are **≥2 health guardrails** that would catch the NSM being gamed or the product degrading.
- [ ] A **business-metrics** layer links the tree to revenue/cost/unit economics.
- [ ] Every metric has a **formula** (numerator/denominator + window), **cadence**, **owner**, **target**, and **alert threshold** — no blank cells in the table.
- [ ] Every metric is **actionable** (would change a decision); flagged vanity metrics are excluded or explicitly labeled.
- [ ] Each alert names a **threshold, audience, channel, and response time**.
- [ ] If the output is written to a file, it follows `template.md` — all 6 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `metrics-dashboard-happy` (happy path) — B2B SaaS collaboration tool with a clear value moment; full NSM → inputs → health → business tree with defined rows.
- `metrics-dashboard-edge` (edge) — early-stage consumer app with no revenue and sparse data; must still pick a leading NSM and usable proxy inputs.
- `metrics-dashboard-adversarial` (adversarial) — user demands "just track signups and pageviews"; the skill must reject vanity metrics and build a proper value-moment tree.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `product-vision` — sets the strategy the North Star Metric must operationalize; the NSM should be a leading indicator of the vision's success.
- `saas-revenue-growth-metrics` / `saas-economics-efficiency-metrics` — metric glossaries/benchmarks that supply definitions and target values for the business-metrics layer of the tree.
- `finance-metrics-quickref` — quick-reference formulas for the revenue/unit-economics rows.

### External Frameworks
- Ben Yoskovitz & Alistair Croll, *Lean Analytics* — the 4 criteria for a good metric (understandable, comparative, ratio/rate, behavior-changing) and the vanity-vs-actionable distinction this skill enforces.
- Amplitude / John Cutler — the **North Star Framework** (one NSM decomposed into input metrics) that structures the metric tree.
- Dave McClure — **AARRR "Pirate" metrics** (Acquisition, Activation, Retention, Referral, Revenue) as the default funnel/lifecycle organization.
- Google — the **HEART framework** (Happiness, Engagement, Adoption, Retention, Task success) as an alternative lifecycle lens for UX-heavy products.
