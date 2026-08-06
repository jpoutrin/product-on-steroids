---
name: saas-economics-efficiency-metrics
description: >
  Compute and interpret SaaS unit-economics and capital-efficiency metrics — CAC,
  LTV, LTV:CAC, CAC payback, gross margin, burn multiple, magic number, sales
  efficiency, and Rule of 40 — each with its formula, benchmark, and common
  pitfalls. Use when evaluating whether a SaaS business is efficient, diagnosing
  weak unit economics, deciding whether to pour fuel on growth, or preparing an
  efficiency section for a board or investor deck.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/saas-economics-efficiency-metrics/template.md
---

# SaaS Unit Economics & Capital-Efficiency Metrics

## Purpose
Turn a set of SaaS financial and go-to-market inputs into a clear read on **unit
economics** (does each customer make money, and how fast?) and **capital
efficiency** (how much growth do we buy per dollar burned?). The deliverable is a
metrics scorecard — every metric shown with its formula, its computed value, a
benchmark verdict, and the pitfalls that could be inflating or deflating it — so a
reader can decide whether to accelerate spend, fix the funnel, or extend runway.

**When NOT to use:** top-line growth and retention accounting — MRR/ARR bridges,
NRR/GRR, growth rate, cohort expansion — belong to `saas-revenue-growth-metrics`;
a bare one-line definition of a single term belongs to `finance-metrics-quickref`.
This skill assumes the revenue/retention picture is already known and goes **deep
on the economics and efficiency of acquiring and serving customers**. It does not
build the operating model or forecast (use a finance-modeling skill).

## Inputs
- **Required:** enough to compute at least one economics metric — typically some of:
  new customers or new ARR in a period, sales & marketing (S&M) spend, ARPA
  (average revenue per account), gross margin %, customer/revenue churn, and net
  new ARR + cash burn for a period. If the user gives only a vague "are our
  economics good?", ask for **S&M spend, new ARR (or new customers × ARPA),
  gross margin %, and churn** before computing — do not invent numbers.
- **Optional:** blended vs. new-logo CAC preference (default: state which you
  used), expansion revenue (for LTV with net revenue retention), segment splits
  (SMB/mid-market/enterprise), the decision the reader faces (accelerate / fix /
  extend runway), and target benchmarks if the company has its own.

## Output Contract
The deliverable is a **unit-economics & efficiency scorecard** with these sections
(see `template.md`):

1. **Inputs & Assumptions** — the raw figures used, the period, and any assumption
   (e.g. "blended CAC, all S&M / all new logos"). Flag anything estimated.
2. **Unit Economics** — for each computed metric (**CAC**, **LTV**, **LTV:CAC**,
   **CAC payback**, **gross margin**): the formula used, the value, the benchmark
   verdict (healthy / watch / unhealthy), and one interpretation line.
3. **Capital Efficiency** — same treatment for **burn multiple**, **magic number**,
   **sales efficiency**, and **Rule of 40**.
4. **Scorecard table** — every metric with value · benchmark · verdict, at a glance.
5. **Read & Pitfalls** — the 2–4 metrics that most drive the verdict, the specific
   pitfalls that could be distorting them, and the recommended action.

Format: prose + two tables (or one). Length: ~1 page. Every metric shows its
**formula and the numbers plugged in** — never a bare value. Every verdict cites a
**named benchmark** (e.g. "LTV:CAC ≥ 3 is healthy; < 1 loses money per customer").

**Benchmark reference (state these; don't rely on the reader knowing them):**
- **CAC payback:** < 12 mo excellent, 12–18 mo healthy for B2B, > 24 mo a red flag.
- **LTV:CAC:** ≥ 3:1 healthy, ~1:1 breakeven (loses money after opex), > 5:1 may
  signal underinvestment in growth.
- **Gross margin:** 70–80%+ for software; < 60% suggests a services-heavy or
  infra-heavy cost base that caps every downstream ratio.
- **Burn multiple** (net burn ÷ net new ARR): < 1 great, 1–1.5 good, 1.5–2
  suspect, > 2 bad (Bessemer/Sacks scale).
- **Magic number** (net new ARR ÷ prior-quarter S&M): > 0.75 pour fuel on, 0.5–0.75
  fine, < 0.5 fix the funnel before spending more.
- **Rule of 40:** growth % + profit (or FCF) margin % ≥ 40 is the efficiency bar.

**GOOD (excerpt):**
> **CAC payback** = CAC ÷ (ARPA × gross margin) = €9,000 ÷ (€400/mo × 75%) =
> **30 months** — *unhealthy* (bar: < 12 mo excellent, > 24 mo red flag). Pitfall
> to check: this uses **blended** CAC; new-logo CAC would be higher still, so the
> real payback is likely worse, not better.

**BAD (excerpt):**
> "LTV:CAC is 3.2, so the economics are healthy."
> — fails: no formula, no numbers, no gross-margin adjustment in LTV, ignores that
> a high blended ratio can hide unprofitable new-logo acquisition; a bare ratio
> with no pitfall check is not a verdict.

## Process
1. **Gather & label inputs** — pin the period, the figures, and whether CAC/LTV are
   blended or new-logo. Mark estimates.
2. **Compute unit economics** — CAC = S&M ÷ new customers; LTV = (ARPA × gross
   margin) ÷ churn (or ARPA × gross margin × avg lifetime); LTV:CAC; CAC payback =
   CAC ÷ (ARPA × gross margin); gross margin = (revenue − COGS) ÷ revenue. Show
   each formula with numbers.
3. **Compute capital efficiency** — burn multiple = net burn ÷ net new ARR; magic
   number = (net new ARR this period × 4 if quarterly-annualized) ÷ prior-period
   S&M; sales efficiency (same family, gross vs. net); Rule of 40 = growth % +
   margin %.
4. **Benchmark each** — attach the named benchmark and a healthy/watch/unhealthy
   verdict to every metric.
5. **Flag pitfalls** — blended-vs-new-logo mixing, LTV without gross-margin
   adjustment, LTV inflated by optimistic lifetime/low churn, magic number skewed
   by a lumpy enterprise deal, Rule-of-40 gamed by one-time margin, ignoring
   payback when celebrating LTV:CAC.
6. **Write the read** — name the 2–4 metrics driving the verdict and the action
   (accelerate / fix funnel / extend runway).
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every reported metric shows its **formula with the actual numbers plugged in**, not just a value.
- [ ] **LTV and CAC payback are gross-margin-adjusted** (contribution, not top-line ARPA).
- [ ] Each metric carries a **named benchmark** and a healthy/watch/unhealthy verdict.
- [ ] It is stated whether CAC/LTV are **blended or new-logo**, and the mixing pitfall is checked.
- [ ] At least the applicable set is covered: **CAC, LTV, LTV:CAC, CAC payback, gross margin** (unit economics) and **burn multiple, magic number, Rule of 40** (efficiency) where inputs allow; missing ones are named as "not computable — needs X".
- [ ] The read names the **2–4 driving metrics** and a concrete action, not a generic "improve efficiency".
- [ ] Metrics belonging to `saas-revenue-growth-metrics` (MRR/ARR/NRR/growth rate) are **not** re-derived here beyond what a formula needs as an input.
- [ ] If written to a file, it follows `template.md` — all 5 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `saas-economics-efficiency-metrics-happy` — full B2B SaaS input set; expects the complete scorecard with formulas, benchmarks, and a spend decision.
- `saas-economics-efficiency-metrics-edge` — partial inputs (no churn, blended-only CAC); must compute what it can, name the uncomputable metrics, and refuse to guess.
- `saas-economics-efficiency-metrics-adversarial` — a flattering bare ratio ("LTV:CAC is 5, we're crushing it") that hides a broken payback and blended-CAC distortion; must not rubber-stamp it.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `saas-revenue-growth-metrics` — supplies MRR/ARR, growth rate, and NRR/churn that feed LTV and the Rule-of-40 growth term; that skill owns those metrics, this one consumes them.
- `finance-metrics-quickref` — one-line glossary of the same terms for quick lookup; use it when a full scorecard is overkill.
- `market-sizing` — bounds the SAM/SOM the LTV:CAC and payback verdicts must scale against when justifying growth spend.

### External Frameworks
- David Skok, *For Entrepreneurs* — "SaaS Metrics 2.0": the canonical LTV, CAC, LTV:CAC ≥ 3, and months-to-recover-CAC (< 12) formulations and benchmarks.
- David Sacks & Bessemer — **Burn Multiple** and **Magic Number** as capital-efficiency gauges and their healthy/suspect/bad bands.
- Brad Feld — **Rule of 40** for balancing growth against profitability at scale.
