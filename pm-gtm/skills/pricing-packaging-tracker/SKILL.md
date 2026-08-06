---
name: pricing-packaging-tracker
description: >
  Collect, structure, and synthesize competitor pricing and packaging data into
  a Pricing & Packaging Competitive Tracker. Use when researching how competitors
  price and package their product, preparing for a pricing strategy review,
  building evidence for a tier-redesign decision, or auditing the market before
  setting or changing price points.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/pricing-packaging-tracker/template.md
---

# Pricing & Packaging Competitive Tracker

## Purpose
Produce a structured, point-in-time snapshot of how 3–7 named competitors price
and package their product — covering tier names, price points, included features,
billing model, and perceived value metric — so that a product or pricing team has
a factual foundation for pricing strategy decisions.

This is a **research and tracking skill**, not a pricing advisor. It collects and
organises publicly available pricing data; it does not recommend what to charge.
Every entry must carry a "Last verified" date because SaaS pricing changes
frequently — a tracker without dates is unreliable.

**When NOT to use:**
- You want a broad competitive landscape of features and market position → use
  `competitive-research-snapshot` (this skill goes deeper on pricing dimensions
  but does not cover general feature parity or market narrative).
- You need a sales-ready one-pager to handle objections in deals → use
  `competitive-battlecard` (tactical, not strategic research).
- You already have the data and want to decide what to charge → consult a
  pricing-strategy skill or finance modelling; this skill only structures the
  evidence, it does not make the recommendation.

## Inputs
- **Required:** a list of 3–7 named competitors whose pricing pages are publicly
  accessible (or partially accessible). If the user provides fewer than 3, ask
  for more before proceeding; fewer than 3 does not support pattern detection.
- **Optional — product context:** the user's own product name, current tier
  structure, and price points (used only to frame the "Pricing Gaps &
  Opportunities" section, not to anchor the competitor data).
- **Optional — scope constraints:** geography (e.g. USD vs EUR pricing), segment
  focus (SMB vs Enterprise), specific dimensions to prioritise (e.g. billing
  model, seat vs usage pricing).
- **Optional — existing data:** screenshots, copied pricing-page text, or prior
  tracker versions the user can paste in; use these as primary source, fall back
  to known public data only when the user confirms it is acceptable.

## Output Contract
The deliverable is a **Pricing & Packaging Competitive Tracker** (see
`template.md`) with these sections:

1. **Tracker Summary** — product being researched, competitors covered, date of
   research, and a one-sentence scope caveat (prices are public / self-reported
   and change frequently).
2. **Pricing Comparison Table** — one row per competitor, columns: Tier Name(s),
   Price Point(s), Billing Model (monthly/annual/usage/custom), Included Feature
   Highlights, Value Metric (what the tier charges for — seats, MAUs, events,
   etc.), and Last Verified date. At least one column for each dimension.
3. **Packaging Patterns** — 3–5 bullet observations on what feature-fencing
   patterns emerge across the set (e.g. "all players gate SSO to highest tier",
   "usage-based caps are a common upgrade trigger").
4. **Value Metric Analysis** — for each distinct value metric found (seats,
   usage, outcomes, etc.), a short paragraph on which competitors use it, the
   typical range, and what it signals about their monetisation strategy.
5. **Pricing Gaps & Opportunities** — where the competitive set leaves a gap
   (underserved segment, missing price point, unconventional billing model not
   yet used). If the user's own product was provided, frame gaps relative to it;
   otherwise frame as open market observations. This section surfaces
   *questions* for pricing strategy, not recommendations.

Format: a prose preamble per section followed by structured tables or bullets.
Length: ~2–3 pages. **Every price point must include a Last Verified date.**
Numbers from the user's own product are clearly separated from competitor data.

**GOOD (excerpt):**
> **Competitor: Acme (acme.io/pricing, last verified 2025-08-01)**
> | Tier | Price | Billing | Value metric | Key features |
> |------|-------|---------|--------------|--------------|
> | Starter | $29/mo | Monthly | Per seat (up to 3) | Core analytics, CSV export |
> | Growth | $99/mo | Annual | Per seat | + API access, SSO |
> | Enterprise | Custom | Annual | Custom | + SLA, dedicated CSM |
>
> *Packaging pattern: SSO is gated to Enterprise across 4 of 5 competitors —
> a consistent signal that it is treated as an enterprise feature, not a
> usability requirement.*

**BAD (excerpt):**
> "Acme charges around $100/month and has three tiers."
> — fails: no tier names, no billing model, no value metric, no source date,
> no feature breakdown. Unusable for strategy decisions.

## Process
1. **Confirm scope** — verify the competitor list (3–7 names), any product
   context provided, and whether the user has pricing-page data to share. If
   fewer than 3 competitors are named, ask for more before continuing.
2. **Collect pricing data** — for each competitor, retrieve publicly visible
   pricing from their pricing page (ask the user to paste text or screenshots if
   live browsing is unavailable). Record the source URL and date for every entry.
3. **Structure the comparison table** — populate Tier Name, Price Point, Billing
   Model, Value Metric, Included Feature Highlights, and Last Verified per
   competitor. Flag any competitor where data is partial or absent (e.g.
   "Enterprise: custom / no public pricing").
4. **Identify packaging patterns** — look across the table for shared
   feature-fencing moves (SSO gating, API access tier, storage caps, seat vs
   usage switching points). Summarise 3–5 patterns with evidence.
5. **Analyse value metrics** — group competitors by value metric; note the metric
   range and what it implies about monetisation strategy for each group.
6. **Surface gaps and opportunities** — identify where the competitive set leaves
   unaddressed price points, underserved segments, or unexplored billing models.
   Frame as questions or hypotheses, not prescriptions.
7. **Add freshness guidance** — note in the Tracker Summary that SaaS pricing
   changes frequently and recommend a re-verification cadence (suggested:
   quarterly for fast-moving markets, semi-annually otherwise).
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] All 5 template sections are present in order (Tracker Summary, Pricing
  Comparison Table, Packaging Patterns, Value Metric Analysis, Pricing Gaps &
  Opportunities).
- [ ] Every competitor in the Pricing Comparison Table has a **Last Verified**
  date — no entry is undated.
- [ ] Every competitor with no public pricing has an explicit "custom / no public
  data" note rather than being omitted or left blank.
- [ ] At least **3 packaging pattern observations** are present, each citing
  evidence from the table (not just assertions).
- [ ] The Value Metric Analysis covers every distinct value metric found across
  the set.
- [ ] Pricing Gaps & Opportunities is framed as observations or questions, **not
  as pricing recommendations** — this skill does not set prices.
- [ ] The Tracker Summary includes the scope caveat about pricing data freshness
  and suggests a re-verification cadence.
- [ ] If the output is written to a file, it follows `template.md` — all 5
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `pricing-packaging-tracker-happy` (happy path) — 5 SaaS competitors with full
  public pricing pages; expects a complete tracker with all dimensions filled.
- `pricing-packaging-tracker-edge` (edge) — one key competitor uses enterprise-
  only / custom pricing with no public data; skill must handle partial data
  gracefully and flag the gap explicitly.
- `pricing-packaging-tracker-adversarial` (adversarial) — user skips data
  collection and asks the skill to recommend "charge more"; skill must insist on
  sourcing competitor data before surfacing any gaps or opportunities.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `competitive-research-snapshot` — broad feature/market comparison across
  competitors; consumes the pricing dimension this skill provides as one input
  among many.
- `competitive-battlecard` — sales-tactic one-pager built partly from the pricing
  data this tracker produces.
- `beachhead-segment` — segment targeting that may inform which competitor tiers
  and value metrics are most relevant to track.

### External Frameworks
- Kyle Poyar & OpenView, *Product-Led Growth Benchmarks* — annual SaaS pricing
  and packaging benchmarks including value-metric prevalence and tier structure
  norms; useful calibration for the Packaging Patterns section.
- Patrick Campbell / ProfitWell, *State of SaaS Pricing* — longitudinal data on
  pricing-page design, billing model adoption, and feature-fencing trends in SaaS.
- Madhavan Ramanujam & Georg Tacke, *Monetizing Innovation* (2016) — the
  "packaging before pricing" principle and the four monetisation strategies
  (mass-market, dynamic, segmented, premium) that underlie value-metric choices.
