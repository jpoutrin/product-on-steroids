---
name: monetization-strategy
description: >
  Choose how a product captures value — the revenue model (subscription vs
  usage vs seat vs freemium vs transactional vs ad), the value metric to charge
  on, and the tier/packaging shape — with audience fit, risks, and a validation
  experiment per option. Use when picking a business model, comparing revenue
  models, deciding what to charge for (the value metric), or designing packaging
  and tiers. Not for setting price levels or discounts — hand those to
  pricing-strategy.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/monetization-strategy/template.md
---

# Choose a Monetization Model

## Purpose
Decide **how a product captures value**: which revenue model it runs on
(subscription, usage-based, per-seat, freemium, one-time, transactional/marketplace,
or ad/sponsorship), **what it charges on** (the value metric — the unit that scales
with the value the customer gets), and the shape of its **packaging and tiers**.
Produce 3–5 distinct model options, each scored on audience fit, unit-economics
sketch, and risks, plus a cheap validation experiment — then recommend 1–2 to test
first. Supports business-model selection and packaging decisions.

**When NOT to use:** setting the actual price *levels*, discount ladders, or
price-fence tactics (use `pricing-strategy`) or building a cost-plus / margin
model for a fixed price point (use `finance-based-pricing-advisor`). This skill
picks the *model and metric*; it does not set the number. If the user already has
a model and only wants a price, hand off. Also not market sizing (`market-sizing`)
or competitive teardown (`competitor-analysis`).

## Inputs
- **Required:** the product/feature and its value proposition, and the target
  segment(s) (B2B/B2C, buyer vs user). If missing, ask for these two before
  proposing models — model fit is meaningless without knowing who pays and for what.
- **Optional:** company priority (revenue vs user growth vs profitability;
  default: balance growth and revenue), known willingness-to-pay signals or budget
  constraints, how competitors monetize (read/cite if provided), delivery cost
  shape (fixed vs marginal, to sanity-check the value metric), and any hybrid the
  user already leans toward.

## Output Contract
The deliverable is a **monetization options memo** with these sections (see
`template.md`):

1. **Context & Constraints** — product value prop, who pays vs who uses, target
   segment, stated company priority. 3–5 bullets.
2. **Model Options (3–5)** — each a distinct revenue model (do not list two
   near-duplicates). For each: **how it works** (who pays, for what, cadence),
   the **value metric** it charges on and why that metric tracks value,
   **audience fit** (why this segment would accept it), a one-line
   **unit-economics sketch** (the CAC/LTV or margin dynamic, directional not a
   forecast), the **top 1–2 risks**, and a **validation experiment** (method,
   success metric, decision rule).
3. **Comparison table** — one row per option; columns: Value metric ·
   Audience fit (H/M/L) · Revenue predictability (H/M/L) · Top risk ·
   Test cost (Low/Med/High).
4. **Recommendation** — the 1–2 models to test first, why (fit × ease × learning
   value), and whether a **hybrid** (e.g. freemium + seat) is warranted.
5. **Packaging sketch** — for the recommended model, the tier shape (free/entry/
   pro/enterprise or usage bands), what gates each tier, and the value metric that
   scales price across tiers.
6. **Test roadmap** — sequenced experiments with a go/no-go criterion each.

Format: prose + one comparison table. Length: ~1–2 pages. Every model names an
explicit **value metric** — never "we'll charge for the product." Price *levels*
are out of scope; refer them to `pricing-strategy`.

**GOOD (excerpt):**
> **Option B — Usage-based (per 1k API calls).** Value metric: API calls, because
> a customer's value scales directly with call volume and cost does too, so margin
> stays stable as accounts grow. Fit: **H** for infra-savvy B2B devs who expect
> metered infra. Unit econ: near-zero marginal cost per call → gross margin holds
> as usage climbs; CAC amortizes over expanding accounts (land-and-expand). Risk:
> revenue is lumpy and customers optimize calls down. **Experiment:** meter 8 beta
> accounts for 6 weeks at a nominal rate; go if median account shows growing calls
> and <20% churn intent. *(Price per call → pricing-strategy.)*

**BAD (excerpt):**
> "Charge $29/month for the Pro plan; competitors charge $25–35 so we sit in the
> middle."
> — fails: sets a price *level* (that's `pricing-strategy`), names no value
> metric, offers one model instead of 3–5, and has no fit/risk/experiment.

## Process
1. **Confirm inputs** — value prop, who pays vs who uses, segment, priority. Ask if any of the first two are missing.
2. **Generate 3–5 distinct models** — pull from the model palette (subscription, usage, seat, freemium, one-time, transactional/marketplace, ad); reject near-duplicates.
3. **Name the value metric per model** — the unit that scales with delivered value *and* keeps margin sane; reject metrics that decouple price from value or from cost.
4. **Assess fit & sketch unit economics** — for each, why the segment accepts it and the directional CAC/LTV or margin dynamic (not a forecast).
5. **Surface top risks** — adoption, predictability, gaming, churn, or implementation, 1–2 per model.
6. **Design a validation experiment per model** — cheapest test of willingness-to-pay-on-this-metric, with a success metric and go/no-go rule.
7. **Compare & recommend** — build the table, pick 1–2 to test first, flag any hybrid.
8. **Sketch packaging** — tier shape and gates for the recommended model; scope out actual prices.
9. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] **3–5 distinct** revenue models are proposed — no two are near-duplicates of the same model.
- [ ] Each model names an **explicit value metric** and says why it tracks delivered value (and doesn't wreck margin).
- [ ] Each model has **audience fit**, a **unit-economics sketch**, **1–2 risks**, and a **validation experiment with a go/no-go rule**.
- [ ] A **comparison table** lets the reader scan options on the same axes.
- [ ] A clear **1–2 model recommendation** is made, with hybrid explicitly considered.
- [ ] A **packaging/tier sketch** is given for the recommended model.
- [ ] **No price levels or discount tactics** are set — those are deferred to `pricing-strategy` (say so if the user pushes).
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `monetization-strategy-happy` (happy path) — B2B API product with clear usage signal; should yield distinct models each with a named value metric.
- `monetization-strategy-edge` (edge) — two-sided marketplace where "who pays" is ambiguous; must reason about which side monetizes.
- `monetization-strategy-adversarial` (adversarial) — user asks "just tell me the price"; skill must decline to set a level and stay in the model/metric layer.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `pricing-strategy` — sets the price *levels*, fences, and discount tactics once this skill has chosen the model and value metric; the direct downstream handoff.
- `finance-based-pricing-advisor` — cost/margin modeling for a chosen price point; consumes the value metric and unit-economics sketch produced here.
- `market-sizing` — TAM/SAM/SOM bounds; the addressable-market context that a model's revenue potential is judged against.

### External Frameworks
- Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016) — "willingness-to-pay first" and the primacy of choosing the right **value metric** before price.
- Patrick Campbell / ProfitWell — value-metric selection ("charge on the axis your customer's value grows on") and packaging/tiering discipline for SaaS.
- [Product Pricing Strategies 101 (Product Compass)](https://www.productcompass.pm/p/product-pricing-strategies-101) — survey of revenue-model archetypes and where each fits.
