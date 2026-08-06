---
name: finance-based-pricing-advisor
description: >
  Ground a pricing decision in unit economics — derive a price floor and target
  from costs and margin goals, then stress-test a proposed price against
  gross-margin and LTV:CAC / payback guardrails and flag where the numbers break.
  Use when setting or defending a price from a P&L view, sanity-checking a
  proposed price against margin and CAC economics, or diagnosing why current
  pricing does not clear the unit-economics bar.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/finance-based-pricing-advisor/template.md
---

# Finance-Based Pricing Advisor

## Purpose
Turn a pricing question into a **unit-economics verdict**: given costs, target
margins, CAC, and LTV/payback goals, compute the **price floor** (below which the
unit loses money or a required margin), a **finance-justified target price**, and
a **guardrail check** on any price the team is proposing — reporting gross margin,
LTV:CAC, and CAC-payback at that price and naming exactly where each guardrail
breaks. This is the finance-guardrail voice: it does not invent willingness-to-pay
or pick a packaging model — it tells you whether a number survives the P&L.

**When NOT to use:** choosing *how* to set price from customer value (Van
Westendorp, value-based tiering, discounting tactics) — use `pricing-strategy`;
deciding *whether* to charge subscription vs usage vs one-time — use
`monetization-strategy`; a full efficiency-metric readout (Rule of 40, burn
multiple, magic number) — use `saas-economics-efficiency-metrics`. This skill
takes a candidate price (or a margin goal) and judges it against the economics; it
does not discover the price from the market.

## Inputs
- **Required:** unit **cost structure** — variable cost to serve one unit/seat/month
  (COGS: infra, support, payment fees, third-party) and, if known, the target
  **gross-margin floor** (default 70–80% for SaaS if unstated). If the user gives a
  proposed price but no costs, ask for per-unit variable cost before verdicting —
  do not assume a margin.
- **Optional:** **CAC** and **customer lifetime** (or churn) to compute LTV:CAC and
  payback; **proposed price** to stress-test; target **LTV:CAC** (default ≥ 3:1) and
  **payback** (default ≤ 12 months B2C / ≤ 18 months B2B) guardrails; fixed-cost or
  volume context. If CAC/lifetime are absent, verdict on gross margin only and mark
  the LTV:CAC and payback checks **N/A — needs CAC & lifetime**.

## Output Contract
The deliverable is a **pricing finance memo** with these sections (see
`template.md`):

1. **Inputs & Assumptions** — the cost, margin-floor, CAC, and lifetime figures
   used, each marked *given* or *assumed (default)*; any default applied is named.
2. **Price Floor** — the minimum price that clears the gross-margin floor:
   `floor = variable_cost / (1 − margin_floor)`, shown with the arithmetic.
3. **Finance-Justified Target Price** — a target above the floor that also satisfies
   the LTV:CAC and payback guardrails (or the floor itself if economics are the only
   constraint), with the reasoning for the headroom chosen.
4. **Guardrail Check** — for the proposed price (or the target), a table of: gross
   margin %, LTV:CAC, CAC-payback (months) — each with the target and a PASS / FAIL /
   N/A verdict.
5. **Where It Breaks** — the binding constraint(s): which guardrail fails first, at
   what price/cost/CAC it would flip to PASS, and the lever to pull (raise price, cut
   COGS, lower CAC, extend lifetime).
6. **Verdict** — one line: PROCEED / PROCEED WITH FIX / DO NOT PROCEED, plus the
   single most important number.

Format: prose + two small tables (guardrail check, break-even lever). Length: ~1
page. Every ratio shows its inputs; no guardrail verdict without the arithmetic
behind it.

**GOOD (excerpt):**
> **Price floor:** €4/seat variable cost ÷ (1 − 0.80) = **€20/seat/mo** to hold an 80% margin.
> **Guardrail check @ proposed €25:** margin (25−4)/25 = **84% PASS** (≥80); LTV = €25 × 84% × 30mo = €630, LTV:CAC = 630/€300 = **2.1:1 FAIL** (<3); payback = €300 / (€25 × 84%) = **14.3 mo PASS** (≤18).
> **Where it breaks:** LTV:CAC is the binding constraint. It clears 3:1 at €36/seat (holding CAC) *or* if CAC drops to €210. **Verdict: PROCEED WITH FIX** — the €25 price is margin-safe but CAC-inefficient; raise price toward €36 or cut CAC before scaling spend.

**BAD (excerpt):**
> "€25 looks healthy — good margin, and LTV is way above CAC, so ship it."
> — fails: no per-unit cost, no floor arithmetic, LTV:CAC asserted not computed, no payback, no binding constraint, no price/CAC at which it flips.

## Process
1. **Gather inputs** — confirm per-unit variable cost and margin floor; pull CAC and
   lifetime/churn if a full check is wanted. Mark each figure *given* or *assumed
   (default)* and name any default used.
2. **Compute the price floor** — `variable_cost / (1 − margin_floor)`; show the math.
   This is the hard minimum; nothing below it is defensible.
3. **Compute the target price** — start at the floor; if CAC/lifetime are present,
   raise until LTV:CAC ≥ target and payback ≤ target, and justify the headroom.
4. **Run the guardrail check** on the proposed price (or target): gross margin %,
   LTV:CAC = (price × margin × lifetime_months) / CAC, payback = CAC / (price ×
   margin per month). Verdict each PASS / FAIL / N/A against its target.
5. **Find where it breaks** — identify the first failing guardrail, solve for the
   price (or CAC/cost/lifetime) that flips it to PASS, and name the lever.
6. **Verdict** — PROCEED / PROCEED WITH FIX / DO NOT PROCEED with the single
   load-bearing number.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **price floor** is shown with its arithmetic (`cost / (1 − margin_floor)`), not just asserted.
- [ ] Every guardrail verdict (gross margin, LTV:CAC, payback) shows the **inputs and the computation**, not just PASS/FAIL.
- [ ] Guardrails compared against **explicit targets** (margin floor, LTV:CAC ≥ 3:1 default, payback ≤ 12/18 mo default) — defaults named where used.
- [ ] Each input is labeled **given** or **assumed (default)**; no silent margin or CAC assumption.
- [ ] The **binding constraint** is named and solved: the price/CAC/cost/lifetime at which it flips to PASS.
- [ ] If CAC or lifetime is missing, the LTV:CAC and payback checks are marked **N/A — needs CAC & lifetime**, not faked.
- [ ] The verdict is one of PROCEED / PROCEED WITH FIX / DO NOT PROCEED with a single most-important number.
- [ ] If written to a file, it follows `template.md` — all 6 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `finance-based-pricing-advisor-happy` (happy path) — full inputs (cost, margin
  floor, CAC, lifetime, proposed price); expects floor, target, guardrail table, and
  a named binding constraint.
- `finance-based-pricing-advisor-edge` (edge) — CAC and lifetime missing; must
  verdict on gross margin and mark LTV:CAC / payback **N/A**, not fabricate them.
- `finance-based-pricing-advisor-adversarial` (adversarial) — a "just tell me it's
  fine" ask with no cost data; must refuse to bless the price and demand per-unit
  cost before verdicting.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `saas-economics-efficiency-metrics` — the efficiency-metric readout (Rule of 40, magic number, burn multiple) that this skill's LTV:CAC and payback checks feed into.
- `finance-metrics-quickref` — definitions and formulas for CAC, LTV, gross margin, and payback used by this advisor.
- `pricing-strategy` — sets the candidate price from customer value; this skill stress-tests that candidate against the P&L.
- `monetization-strategy` — chooses the revenue model; this skill prices a unit *within* that model.

### External Frameworks
- David Skok, *SaaS Metrics 2.0* — the LTV:CAC ≥ 3:1 and CAC-payback ≤ 12 months benchmarks this skill uses as default guardrails.
- Bessemer Venture Partners, *State of the Cloud* / "Good, Better, Best" efficiency benchmarks — margin and payback ranges for judging whether a price clears the unit-economics bar.
- Contribution-margin / break-even pricing (managerial accounting) — the `price = variable_cost / (1 − margin_floor)` floor derivation at the core of the memo.
