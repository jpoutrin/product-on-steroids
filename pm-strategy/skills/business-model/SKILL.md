---
name: business-model
description: >
  Build a classic 9-block Business Model Canvas (Osterwalder/Strategyzer) that
  maps how a business creates, delivers, and captures value, with the blocks
  cross-checked for alignment and unit economics tested. Use when documenting a
  business model, articulating how the whole operation connects for a strategy
  or investor deck, or analyzing an existing business's model.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/business-model/template.md
---

# Build a Business Model Canvas (9 Blocks)

## Purpose
Produce a complete Business Model Canvas — the classic 9 building blocks from
Alexander Osterwalder / Strategyzer — that documents how a business **creates**
value (key partners, activities, resources), **delivers** it (value propositions,
customer relationships, channels, segments), and **captures** it (cost structure,
revenue streams). The blocks are filled so they reinforce each other, and the
economics are sanity-checked (revenue exceeds cost at scale; LTV comfortably
above CAC). Supports strategy articulation, corporate/portfolio review, and
investor materials where you must show how all operational pieces connect.

**When NOT to use:** early-stage hypothesis testing where Problem/Solution/Unfair
Advantage matter more than Partners/Resources — use `lean-canvas` (Ash Maurya);
new-product strategy that separates strategic bets from the money model — use
`startup-canvas` (Huryn); sizing the opportunity — use `market-sizing`; pricing
or packaging design — use a pricing skill. This skill maps the model as a whole;
it does not pick the strategy, validate demand, or set the price.

## Inputs
- **Required:** the product/service and its target customer(s). If missing, ask
  for a one-line description of what the business sells and to whom before
  drafting — do not invent the offer.
- **Optional:** current operations or key assumptions, competitive/industry
  context, pricing anchor or known unit economics, and whether this documents an
  **existing** business (map reality) or a **proposed** one (label assumptions).
  Absent these, draft from stated facts and flag each inferred block as an
  assumption.

## Output Contract
The deliverable is a **Business Model Canvas** covering all 9 blocks, grouped as
create / deliver / capture (see `template.md`):

1. **Customer Segments** — who is served; segment type (mass, niche, segmented,
   multi-sided) and each segment's defining characteristics.
2. **Value Propositions** — the value delivered and the problem solved per
   segment; both quantitative (price, speed, quality) and qualitative (design,
   status) elements.
3. **Channels** — how customers become aware, purchase, receive value, and get
   support; direct vs indirect, owned vs partner.
4. **Customer Relationships** — how each segment relationship is established and
   maintained (personal, self-service, automated, community, co-creation).
5. **Revenue Streams** — how the business earns per segment; mechanism
   (transaction, subscription, licensing, usage) and pricing logic.
6. **Key Resources** — the assets required (physical, IP, human, financial).
7. **Key Activities** — the critical activities (production, problem-solving,
   platform/network).
8. **Key Partnerships** — strategic partners/suppliers and what they provide.
9. **Cost Structure** — the main costs; fixed vs variable, cost-driven vs
   value-driven.

Plus a short **Coherence & Economics** note: how the blocks reinforce each other
and whether the model is viable (revenue > cost at scale; LTV > ~3× CAC), listing
the key assumptions and risks. Format: a labeled 9-block canvas (list or table)
+ the coherence note. Length: ~1 page. Every block is populated (no "TBD"); an
inferred entry is labeled an assumption.

**GOOD (excerpt):**
> **Customer Segments:** two-sided — (a) urban commuters wanting on-demand rides;
> (b) drivers seeking flexible income.
> **Value Propositions:** riders → arrives in <5 min, cashless, upfront price;
> drivers → flexible hours, weekly payout.
> **Revenue Streams:** ~25% take rate per ride; surge pricing at peak.
> **Cost Structure:** variable — driver payouts, payment fees; fixed — engineering,
> support. Value-/network-driven, not cost-driven.
> *Coherence: the driver segment (supply) directly enables the rider value prop
> (fast pickup); take-rate revenue scales with both. Assumption: driver
> retention high enough to keep pickup times low — the model's key risk.*

**BAD (excerpt):**
> "Value Prop: a great app. Customers: everyone. Revenue: we'll figure out
> monetization later. Partners: TBD."
> — fails: vague/undifferentiated value prop, "everyone" is not a segment, an
> empty revenue block (no capture mechanism), a TBD block, and zero coherence or
> economics check.

## Process
1. **Profile customer segments** — identify each distinct segment and its type.
2. **Define value propositions** — the value and problem solved per segment.
3. **Map channels** — awareness → purchase → delivery → after-sales.
4. **Set customer relationships** — the relationship type per segment.
5. **Define revenue streams** — capture mechanism and pricing per segment.
6. **List key resources** — the assets the model requires.
7. **List key activities** — the critical activities that deliver the value prop.
8. **Identify key partnerships** — who supplies what the business does not.
9. **Outline cost structure** — main costs, fixed vs variable, cost driver.
10. **Check coherence & economics** — confirm the 9 blocks align and reinforce,
    test viability (revenue > cost at scale, LTV > ~3× CAC), and surface the key
    assumptions and risks.
11. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] **All 9 blocks** are present and populated — no block left empty or "TBD".
- [ ] Customer Segments are **specific** (not "everyone"); the Value Propositions
      map to those segments and solve a stated problem.
- [ ] Revenue Streams name a concrete **capture mechanism** and pricing logic;
      Cost Structure separates fixed vs variable.
- [ ] The blocks are **coherent** — the create-side (partners/activities/resources)
      supports the value prop, and the delivery-side reaches the named segments.
- [ ] **Economics are sanity-checked** — revenue exceeds cost at scale and LTV is
      comfortably above CAC (or the gap is flagged as the key risk).
- [ ] For an existing business the canvas maps **reality**; for a proposed one,
      each inferred block is **labeled an assumption** with the top risks named.
- [ ] If written to a file, it follows `template.md` — all sections present, in
      order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `business-model-happy` (happy path) — a two-sided marketplace with clear
  segments and monetization; guards against empty/incoherent blocks.
- `business-model-edge` (edge) — a free/freemium product where the revenue and
  customer-segment blocks must handle non-paying users and an indirect payer.
- `business-model-adversarial` (adversarial) — a vague "we have an app" ask the
  skill must refuse to fill with hand-waving, eliciting the offer/customer first.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `lean-canvas` — the startup problem/solution variant; use it instead when
  Problem/Solution/Unfair-Advantage matter more than Partners/Resources.
- `startup-canvas` — separates strategy from the money model for new products.
- `market-sizing` — sizes the opportunity the segments/value-prop blocks describe.

### External Frameworks
- Alexander Osterwalder & Yves Pigneur, *Business Model Generation* (2010) — the
  canonical 9-block Business Model Canvas this skill implements.
- Strategyzer — *Business Model Canvas* (the maintained template and block
  definitions).
- Osterwalder et al., *Value Proposition Design* (2014) — deepens the Value
  Propositions ↔ Customer Segments fit that anchors canvas coherence.
