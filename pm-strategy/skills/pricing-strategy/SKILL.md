---
name: pricing-strategy
description: >
  Set the price levels for a product — choose a pricing approach (value-based,
  competitive, or cost-plus), justify specific price points, and design
  anchoring, discounting, and willingness-to-pay research (e.g. Van Westendorp).
  Use when deciding how much to charge, setting or changing a price point,
  choosing between value-based and cost-plus pricing, or planning willingness-to-pay
  research.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/pricing-strategy/template.md
---

# Set Price Levels & Pricing Approach

## Purpose
Decide **how much to charge** for a product and defend it. Produce a pricing
recommendation that picks a pricing **approach** (value-based, competitive, or
cost-plus), sets specific **price points** anchored to willingness-to-pay and
the customer's alternative, and specifies **anchoring and discounting** tactics
— with each price grounded in value delivered rather than a round guess.

**When NOT to use:** choosing the *revenue model* or how to package/bundle tiers
(use `monetization-strategy` — subscription vs usage vs seat, freemium, tier
design); building the unit-economics / margin model that a price must clear (use
`finance-based-pricing-advisor` — CAC, LTV, contribution margin). This skill is
the **how-much-to-charge** layer: it sets the numbers on the page, given a model
and a cost floor.

## Inputs
- **Required:** the product and its value proposition, the target segment, and
  the customer's current alternative (incumbent tool, in-house build, or doing
  nothing) with its cost. If missing, ask for these three before recommending a
  price — a price with no value anchor and no alternative is unjustifiable.
- **Optional:** the revenue model / value metric already chosen (from
  `monetization-strategy`), competitor price points, a cost floor / target margin
  (from `finance-based-pricing-advisor`), survey data (Van Westendorp responses,
  conjoint), quantified customer outcomes (time saved, revenue gained, cost cut).
  If a value metric is not yet chosen, note it and recommend a placeholder.

## Output Contract
The deliverable is a **pricing recommendation** with these sections (see
`template.md`):

1. **Pricing Approach** — the chosen approach (value-based / competitive /
   cost-plus), why it fits this product and segment, and the value anchor:
   the customer's alternative and its cost, plus quantified outcome value.
2. **Willingness-to-Pay** — the WTP estimate and how it was derived (Van
   Westendorp band if survey data exists — Point of Marginal Cheapness to Point
   of Marginal Expensiveness with the Optimal Price Point; otherwise value-based
   inference or competitor triangulation). State the acceptable price range.
3. **Recommended Price Point(s)** — the specific number(s) with the value metric
   they attach to, positioned against the cost floor (must clear it) and against
   competitors (premium / parity / discount, with the reason).
4. **Anchoring & Discounting** — the anchor (decoy/high tier or reference price
   that makes the target price feel obvious), annual-vs-monthly or volume
   discount %, and any launch/introductory pricing with a defined end.
5. **Assumptions & Validation** — numbered assumptions, each with a confidence
   level (high/med/low) and how to test the most uncertain (WTP survey, A/B
   price-page test, founder-led sales calls).

Format: prose + one price table. Length: ~1 page. Every price point is tied to a
value anchor, a WTP band, or a competitor reference — never an unjustified number.

**GOOD (excerpt):**
> **Approach: value-based.** The alternative is 6 analyst-hours/month at €80/hr =
> **€480/mo of effort** replaced. Van Westendorp on 140 responses: cheap €39,
> expensive €99, **Optimal Price Point €59**. **Recommend €59/mo per workspace**
> (value metric: workspace) — ~12% of value delivered, a 25% premium over
> Competitor X's €47 justified by the automation gap. Annual −18% (€49/mo
> equivalent) as the anchored default.
> *Assumption 2 (med): €480/mo effort value holds below 50-seat teams — validate via 20 founder-led calls.*

**BAD (excerpt):**
> "Charge €50/month — it's a round number that feels right and competitors are
> around there." — fails: no approach named, no value anchor, no WTP band, no
> cost-floor check, price is a guess dressed as a competitive claim.

## Process
1. **Anchor to value** — state the customer's alternative and its cost, and the
   quantified outcome the product delivers; this bounds willingness-to-pay.
2. **Pick the approach** — value-based when outcome value is quantifiable
   (default), competitive when the market has a strong reference price, cost-plus
   only when neither holds; justify the choice.
3. **Estimate WTP** — run/read Van Westendorp if survey data exists (report the
   band and Optimal Price Point); otherwise infer from value share or triangulate
   from competitors. State the acceptable range.
4. **Set the price point(s)** — choose the number(s) inside the WTP band, confirm
   they clear the cost floor, and position against competitors with a reason.
5. **Design anchoring & discounting** — set the reference anchor and the
   annual/volume discount; time-box any introductory price.
6. **Map assumptions** — number them, rate confidence, name a validation test for
   the most uncertain.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] A pricing **approach** is named (value-based / competitive / cost-plus) with a reason it fits.
- [ ] Every price point is tied to a **value anchor**, a **WTP band**, or a **competitor reference** — none is a round guess.
- [ ] The customer's **alternative and its cost** are stated as the value floor.
- [ ] WTP is derived by a **named method** (Van Westendorp band + OPP, value share, or competitor triangulation).
- [ ] The recommended price is checked against the **cost floor** (clears it) and **positioned** vs competitors with a reason.
- [ ] **Anchoring and discounting** are specified (reference anchor + annual/volume discount %); intro pricing is time-boxed.
- [ ] Assumptions are **numbered** with confidence levels and a validation test for the most uncertain.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `pricing-strategy-happy` — B2B SaaS with Van Westendorp survey data and a clear
  alternative; must produce a value-based price with a WTP band.
- `pricing-strategy-edge` — no survey data and a thin competitive reference; must
  infer WTP from value share and flag it as an assumption to validate.
- `pricing-strategy-adversarial` — user asks for "the right price" with no value
  anchor; must refuse a round-number answer and elicit the alternative + value.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `monetization-strategy` — picks the revenue model, value metric, and tier
  packaging that this skill then sets the price *levels* for.
- `finance-based-pricing-advisor` — supplies the unit-economics cost floor and
  target margin the recommended price must clear.

### External Frameworks
- Van Westendorp Price Sensitivity Meter — the four-question survey (too cheap /
  cheap / expensive / too expensive) yielding the acceptable-price band and
  Optimal Price Point used for WTP estimation here.
- Thomas Nagle & Georg Müller, *The Strategy and Tactics of Pricing* — the
  value-based vs cost-plus vs competitive framing and the "price to value, not
  to cost" discipline this skill enforces.
- Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* — willingness-to-pay
  as the starting point for pricing and the case for testing WTP before launch.
