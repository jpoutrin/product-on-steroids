---
name: north-star-metric
description: >
  Define a single North Star Metric plus 3-5 supporting input metrics that form a
  metrics constellation, classify the business game (Attention, Transaction,
  Productivity), and validate the candidate against 7 criteria. Use when choosing a
  North Star Metric, setting up a metrics framework, deciding what to measure, or
  evaluating North Star candidates.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/north-star-metric/template.md
---

# Define a North Star Metric

## Purpose
Choose one **North Star Metric (NSM)** — a single, customer-centric KPI that
captures the value customers get from the product and leads long-term business
success — and the 3-5 **input metrics** that most directly drive it. The
deliverable classifies the business game being played, proposes an NSM validated
against seven criteria, and names the constellation of inputs teams can move in
the short term. It supports building a metrics framework, aligning the org on one
number, and deciding what to optimize.

**When NOT to use:** setting quarterly goals/targets (that's OKRs — the NSM is the
*what*, Key Results express expected change in it); building a full funnel or
activation-metric taxonomy (use an AARRR/HEART funnel skill); picking product bets
or roadmap (that's strategy — choosing the NSM is *a* strategic input, not the
strategy). The NSM is a single customer-value KPI, **never** a revenue/LTV metric
and never a list of metrics.

## Inputs
- **Required:** what the product does and who its customer is — the value it
  delivers and the core action a customer takes to get that value. If missing, ask
  for the product, its primary customer segment, and the one job customers hire it
  for before proposing a metric; do not guess.
- **Optional:** business/revenue model, company vision or mission (feeds the
  vision-alignment criterion), metrics currently tracked, key segments and use
  cases. If absent, infer the business game from the product description and state
  the inference as an assumption.

## Output Contract
The deliverable is a **North Star Metric brief** with these sections (see
`template.md`):

1. **Business Game** — one of Attention / Transaction / Productivity, with a
   one-line justification tied to how the product creates value.
2. **North Star Metric** — a single named metric with a precise definition
   (what counts, over what period, per what unit). One number, customer-centric,
   not revenue.
3. **7-Criteria Validation** — a checklist scoring the candidate against all seven
   criteria (Easy to Understand, Customer-Centric, Sustainable Value, Vision
   Alignment, Quantitative, Actionable, Leading Indicator), each pass/fail with a
   one-line reason.
4. **Input Metrics** — 3-5 leading indicators, each with a definition and a
   one-line note on how it drives the NSM and why it is easier to move short-term.
5. **Anti-patterns Avoided** — a short note confirming the NSM is not a vanity/
   revenue metric, not multiple metrics, and not an OKR.

Format: prose + two short lists/tables (criteria + inputs). Length: ~1 page. The
NSM is exactly one metric; input metrics number 3-5.

**GOOD (excerpt):**
> **Business Game:** Productivity — Notion-style value is completing knowledge work faster.
> **NSM:** *Weekly Active Editing Users* — distinct users who created or edited content in the last 7 days.
> **Input metrics:** (1) new-workspace activation rate, (2) docs created per user in week 1, (3) collaborators invited per workspace, (4) week-4 retention. Each is easier to move than the NSM and directly feeds it.

**BAD (excerpt):**
> "North Star: **Monthly Recurring Revenue**, plus signups and NPS."
> — fails: revenue is not customer-centric and lags rather than leads; three metrics is not a *single* North Star; NPS/signups is a constellation dumped in place of one NSM.

## Process
1. **Elicit context** — confirm the product, its customer, and the core value
   action; ask for the required inputs if missing.
2. **Classify the business game** — Attention, Transaction, or Productivity; state
   the reason. This shapes which metric families are plausible.
3. **Draft the NSM candidate** — one metric that reflects delivered customer value
   and leads revenue; write a precise definition (unit, action, time window).
4. **Validate against the 7 criteria** — score each; if any fail, revise the
   candidate before moving on.
5. **Derive 3-5 input metrics** — pick the leading indicators that most directly
   move the NSM and are easier to shift short-term; note the causal link for each.
6. **Screen anti-patterns** — confirm it is not revenue/LTV, not multiple metrics,
   not an OKR/target.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The North Star is exactly **one** metric with a precise, unit-and-window definition.
- [ ] It is **customer-centric** (value delivered) and a **leading** indicator — not revenue/LTV, not a lagging outcome.
- [ ] The **business game** is classified (Attention / Transaction / Productivity) with a justification.
- [ ] The candidate is scored against **all seven criteria**, each pass/fail with a reason.
- [ ] **3-5 input metrics** are given, each with a definition and its causal link to the NSM.
- [ ] Anti-patterns are explicitly screened (not multiple metrics, not revenue, not an OKR).
- [ ] Any inferred context (e.g. game classification without a stated model) is flagged as an assumption.
- [ ] If the brief is written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `north-star-metric-happy` (happy path) — a B2B productivity SaaS with clear value action; expects one customer-centric NSM, game classification, 7-criteria pass, and 3-5 inputs.
- `north-star-metric-edge` (edge) — a marketplace where the tempting NSM (GMV/revenue) violates the customer-centric criterion; the skill must reject it and propose a value-based transaction metric.
- `north-star-metric-adversarial` (adversarial) — user demands "make revenue our North Star" and lists five metrics; the skill must refuse the anti-pattern, pick one customer-centric metric, and explain why revenue is a lagging input at best.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — bounds the opportunity the NSM tracks progress within; SAM/SOM inform whether the NSM's ceiling is meaningful.
- `product-vision` — supplies the vision/mission the NSM's vision-alignment criterion is scored against.

### External Frameworks
- Amplitude, *The North Star Playbook* (Sean Ellis / John Cutler) — the North Star Framework, the metric-plus-inputs "constellation," and the three business games (Attention, Transaction, Productivity).
- [The North Star Framework 101 (Product Compass)](https://www.productcompass.pm/p/the-north-star-framework-101) — the seven criteria and worked candidate examples this skill validates against.
- Dave McClure, *AARRR (Pirate) Metrics* — the funnel-stage input metrics that most commonly feed a North Star.
