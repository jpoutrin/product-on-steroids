---
name: saas-revenue-growth-metrics
description: >
  Compute, benchmark, and interpret SaaS revenue-retention and growth metrics —
  MRR/ARR and its new/expansion/contraction/churned components, NRR, GRR, ARR
  growth rate, the SaaS quick ratio, logo vs revenue retention, and ARPA
  expansion. Use when analyzing recurring-revenue health, reviewing a growth
  dashboard, diagnosing whether growth is durable or leaky, or preparing
  retention numbers for a board or investor update.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/saas-revenue-growth-metrics/template.md
---

# SaaS Revenue & Growth-Retention Metrics

## Purpose
Turn a set of recurring-revenue inputs into the canonical SaaS revenue-and-growth
metrics — each computed with the right formula, benchmarked against
what-good-looks-like, interpreted (not just reported), and flagged for the
pitfalls that most often make the number lie. Supports growth-durability
diagnosis (is expansion covering churn?), board/investor reporting, and deciding
whether the retention or acquisition engine needs the next fix.

Covered: MRR/ARR; the MRR bridge (new, expansion, contraction, churned MRR);
Net Revenue Retention (NRR) and Gross Revenue Retention (GRR); ARR growth rate;
the SaaS quick ratio; logo (customer) vs revenue retention; and ARPA/ARPU +
expansion.

**When NOT to use:** unit-economics or capital-efficiency questions — CAC, LTV,
LTV:CAC, CAC payback, burn multiple, magic number, or Rule of 40 (use
`saas-economics-efficiency-metrics`); a one-line definition lookup for any finance
term (use `finance-metrics-quickref`); or forecasting/modeling forward ARR (this
skill measures and diagnoses the trailing picture, it does not build the model).

## Inputs
- **Required:** enough to compute at least one metric end-to-end. The minimal set
  is **starting-period MRR (or ARR)** plus the **MRR movements for the period**
  (new, expansion, contraction, churned) OR ending MRR. If the user gives only a
  single MRR/ARR snapshot, ask for the period's movements (or a start-and-end
  pair) — retention and growth metrics need two points in time, not one.
- **Optional:** customer counts at start/end and logos lost (enables logo
  retention and ARPA); the reporting cohort/segment and period length (default:
  monthly movements, retention quoted on a **trailing-12-month** basis);
  contract/billing terms if annual prepay distorts monthly MRR; company stage and
  ACV/segment (SMB vs mid-market vs enterprise) so benchmarks are applied to the
  right band, not a generic one.

## Output Contract
The deliverable is a **revenue-metrics readout** with these sections (see
`template.md`):

1. **Inputs & period** — the starting figures, the movements used, the period
   length, and the retention basis (monthly vs TTM); state any assumption made to
   fill a gap.
2. **MRR bridge** — start MRR → + new → + expansion → − contraction → − churned →
   end MRR, as a walk that reconciles to ending MRR exactly.
3. **Metrics table** — one row per computed metric: **value**, the **formula
   applied** (with the actual numbers substituted), the **benchmark band**
   (good / median / weak), and a one-line **read**. Only include metrics the
   inputs support; mark the rest "insufficient data — need X".
4. **Interpretation** — 2–4 sentences: is growth durable (NRR ≥ 100%? quick
   ratio ≥ 4?), where is the leak (contraction vs churn, revenue vs logo), and
   what the numbers together say that no single one does.
5. **Pitfalls & caveats** — the specific ways these numbers could mislead here
   (e.g. annual-prepay lumpiness, cohort mixing, small-N noise, NRR flattering a
   high-churn base).

Format: prose + the MRR bridge + one metrics table. Length: ~1 page. Every metric
shows its formula with numbers substituted; every benchmark cites the band it is
judged against. Never report a retention or growth number without stating the
period and basis.

**GOOD (excerpt):**
> **NRR (TTM)** = (start MRR 100k + expansion 12k − contraction 3k − churned 6k) ÷ start 100k = **103%**.
> Benchmark: good ≥ 110%, median ~100–105%, weak < 100% (mid-market B2B). **Read:** just above water — the base grows without new logos, but only barely; expansion (12k) barely outpaces gross revenue loss (9k).
> **Quick ratio** = (new 15k + expansion 12k) ÷ (contraction 3k + churned 6k) = **3.0** — below the ≥ 4 "efficient growth" bar; churn is eating too much of what's added.

**BAD (excerpt):**
> "Retention is 95% and MRR is growing nicely, so we're healthy."
> — fails: no period/basis (95% of what, over what window?), no formula, no benchmark band, revenue vs logo retention conflated, and "growing nicely" is not a computed ARR growth rate.

## Process
1. **Confirm the inputs & period** — pin the starting figure, the four MRR
   movements (or start/end pair), the period length, and the retention basis;
   if a required piece is missing, ask before computing (don't invent movements).
2. **Build the MRR bridge** — walk start → new → expansion → contraction →
   churned → end and confirm it reconciles to ending MRR exactly; a bridge that
   doesn't tie means an input is wrong.
3. **Compute the metrics** — for each supported metric apply its formula with the
   actual numbers: NRR = (start + expansion − contraction − churned) ÷ start;
   GRR = (start − contraction − churned) ÷ start; ARR growth = (end − start) ÷
   start; quick ratio = (new + expansion) ÷ (contraction + churned); logo
   retention = customers retained ÷ starting customers; ARPA = MRR ÷ customers.
   Skip (and flag) any metric the inputs can't support.
4. **Benchmark each** — attach the good/median/weak band for the company's stage
   and segment, not a generic one; note when a number is out of band.
5. **Interpret across metrics** — read NRR with GRR (expansion masking churn?),
   revenue retention with logo retention (losing small accounts, keeping revenue?
   or vice versa), and the quick ratio as the growth-efficiency summary.
6. **Surface pitfalls** — call out the specific distortions in play (annual
   prepay, cohort mixing, small N, a shrinking base flattering ratios).
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **MRR bridge reconciles** to ending MRR exactly (start + new + expansion − contraction − churned = end).
- [ ] Every metric shows its **formula with the actual numbers substituted**, not just a final value.
- [ ] **NRR and GRR are both reported** when movements are available, and the difference between them is interpreted (expansion vs pure retention).
- [ ] Each metric carries a **benchmark band** (good / median / weak) matched to the company's stage/segment.
- [ ] Every retention and growth figure states its **period and basis** (monthly vs TTM); no bare percentages.
- [ ] **Revenue retention and logo retention are kept distinct** — never one used as a proxy for the other.
- [ ] Metrics the inputs can't support are **flagged "insufficient data"**, not guessed.
- [ ] At least one **relevant pitfall/caveat** for this specific data is named.
- [ ] If written to a file, the output follows `template.md` — all 5 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `saas-revenue-growth-metrics-happy` (happy path) — full MRR movements given;
  expects a reconciling bridge, NRR/GRR/quick-ratio/growth all computed,
  benchmarked, and interpreted together.
- `saas-revenue-growth-metrics-edge` (edge) — annual-prepay + only a start/end
  ARR snapshot; expects the skill to request movements, quote the right basis,
  and flag prepay lumpiness rather than fabricate a bridge.
- `saas-revenue-growth-metrics-adversarial` (adversarial) — a single flattering
  NRR quoted with no period and a shrinking base; expects the skill to refuse to
  bless it, demand period/basis, and separate revenue from logo retention.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `saas-economics-efficiency-metrics` — CAC, LTV, payback, burn multiple, magic number, Rule of 40; the acquisition/efficiency side of the same dashboard this skill's retention side pairs with.
- `finance-metrics-quickref` — compact one-line glossary for any term referenced here; use it for a fast definition, this skill for the full computed-and-benchmarked readout.
- `market-sizing` — TAM/SAM/SOM bounds the opportunity that ARR growth is progressing against.

### External Frameworks
- David Skok, *For Entrepreneurs* — "SaaS Metrics 2.0" and the **SaaS quick ratio** framing (growth added vs revenue lost) that underpins this skill's growth-efficiency read.
- Bessemer Venture Partners, *State of the Cloud* / "Good, Better, Best" cloud benchmarks — the NRR / GRR / growth benchmark bands by stage and segment.
- Jason Lemkin, *SaaStr* — operator benchmarks for NRR, logo vs revenue churn, and why net-negative churn (NRR > 100%) is the durable-growth bar.
