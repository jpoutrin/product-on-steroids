---
name: gtm-strategy
description: >
  Produce a go-to-market strategy document that aligns target customer, market
  entry approach, positioning, channel mix, pricing, and launch sequencing into
  a coherent plan. Use when planning a product launch, defining a market entry
  strategy, or aligning cross-functional teams around a go-to-market plan.
version: 0.1.0
type: workflow
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/gtm-strategy/template.md
---

# GTM Strategy

## Purpose
Produce a **GTM strategy document** — the master plan that aligns who the
product is for, how it enters the market, what position it holds, which channels
carry it, how it is priced, and in what sequence the launch unfolds. The output
is a structured, decision-ready artifact that a cross-functional team (product,
marketing, sales, leadership) can use to coordinate and execute a launch.

**When NOT to use:**
- Deep ICP profiling alone → use `ideal-customer-profile` (ICP is one section
  of GTM; run that skill first and feed the output here).
- Crafting the positioning statement as a standalone deliverable → use
  `positioning-statement`.
- Choosing specific execution tactics (PLG loops, outbound sequences) → use
  `gtm-motions`; this skill sets the strategy those motions must serve.
- Competitive teardown → use `competitor-analysis`; its output informs the
  positioning section here.
- Market sizing → use `market-sizing`; its TAM/SAM/SOM feed the beachhead
  scoping section here.

GTM strategy is the **umbrella plan**; the other skills produce its components.
Use this skill to assemble and integrate those components into a single,
internally-consistent plan.

## Inputs
- **Required:** product description (what it does, for whom, key differentiators)
  and the problem it solves. If missing, ask before proceeding.
- **Required:** intended launch context — new product, new market, new segment,
  or competitive re-entry. If ambiguous, ask; the entry approach differs sharply
  across these.
- **Optional:** ICP or customer research (interviews, surveys, jobs-to-be-done).
  If absent, surface that gap explicitly and note assumptions made in the Target
  Customer section.
- **Optional:** existing positioning, pricing, or channel constraints. If absent,
  derive from product description and flag as tentative.
- **Optional:** launch timeline / deadline. If absent, recommend a sequencing
  based on readiness signals rather than a hard date.
- **Optional:** competitive landscape data. If absent, ask or note assumptions.

## Output Contract
The deliverable is a **GTM strategy document** with these sections (see
`template.md`):

1. **Target Customer** — the primary segment the launch targets (beachhead),
   described in terms of who they are, what job they need done, and what
   pain they feel acutely enough to act. One crisp profile; note expansion
   segments for later.
2. **Market Entry Strategy** — the beachhead rationale (why this segment first)
   and the expansion arc (what adjacencies open once the beachhead is won).
   Include the market entry motion (PLG, SLG, channel-led, community-led, etc.)
   and why it fits this segment.
3. **Positioning** — the position the product claims in the target customer's
   mind: category, primary differentiation, and proof points. State what the
   product is NOT positioned as (negative space). Follow the house format:
   *For [customer], [product] is the [category] that [differentiation] because
   [proof point].*
4. **Channel Mix** — which 2–4 channels carry the product to the target customer,
   with rationale for each (audience fit, cost, control, scalability) and a
   primary/secondary/experimental tier to focus execution.
5. **Pricing Approach** — the pricing model (freemium, usage-based, seat,
   value-based, etc.), the anchor price or tier structure, and the rationale
   (willingness to pay, competitive anchoring, land-and-expand logic). Flag
   open pricing decisions if data is insufficient.
6. **Launch Sequencing** — a phased plan: pre-launch (readiness gates), launch
   (activities, announcements, channel activation), and post-launch (feedback
   loops, optimization cadence). Include 2–3 go/no-go criteria per phase.
7. **Success Metrics** — 3–5 leading and lagging KPIs that indicate whether the
   GTM plan is working, with targets and measurement cadence. Distinguish
   awareness → acquisition → activation metrics so each team knows what it owns.

Format: prose with one table per section where tabular form aids comparison.
Length: ~3–5 pages. Every strategic claim is grounded in named evidence, a
stated assumption, or explicitly flagged as a hypothesis to validate.

**GOOD (excerpt):**
> **Market Entry Strategy — Beachhead:** Mid-market SaaS finance teams (50–500
> employees) feeling acute pain around manual expense reconciliation. Rationale:
> highest willingness to pay, shortest sales cycles (<30 days), referenceable for
> enterprise expansion. Entry motion: product-led (free trial → CS-assisted
> expansion) because finance buyers self-research and distrust outbound. Expansion
> arc: enterprise finance teams (500+), then HR/ops buyer persona once finance
> footprint is established.

**BAD (excerpt):**
> "Our target is all businesses that need expense management. We'll use all
> available marketing channels and price competitively."
> — fails: no beachhead specificity, no channel rationale, no pricing logic,
> no expansion arc, no metrics. Generic = unexecutable.

## Process
1. **Orient** — confirm the launch context (new product / new market / new
   segment / re-entry) and identify which input sections are present vs. must be
   derived with stated assumptions.
2. **Target Customer** — define or validate the beachhead segment; call out
   missing ICP data and any assumptions made.
3. **Market Entry** — choose the entry motion and beachhead rationale; sketch
   the expansion arc.
4. **Positioning** — craft the positioning statement and proof points; define
   the negative space.
5. **Channel Mix** — select 2–4 channels, tier them, and justify fit with the
   target customer's discovery and buying behavior.
6. **Pricing** — recommend a model and anchor, grounded in competitive context
   or stated willingness-to-pay assumptions; flag any open decisions.
7. **Launch Sequencing** — structure the pre/launch/post phases with go/no-go
   gates.
8. **Success Metrics** — define 3–5 KPIs spanning awareness through activation;
   assign ownership and measurement cadence.
9. Run the Quality Bar below; revise any failing item; then return.

## Quality Bar
Before returning, confirm:
- [ ] All seven sections are present and in order (Target Customer → Market Entry
  → Positioning → Channel Mix → Pricing → Launch Sequencing → Success Metrics).
- [ ] The beachhead segment is **specific** (named persona, company profile, or
  job-to-be-done) — not a broad category like "all businesses."
- [ ] The market entry motion (PLG, SLG, channel-led, etc.) is **explicitly
  named and justified** against the target customer's buying behavior.
- [ ] The positioning follows the house format with category, differentiation,
  and at least one proof point.
- [ ] Channel mix has **2–4 channels**, each tiered (primary / secondary /
  experimental) with rationale.
- [ ] Pricing names a model and an anchor or tier structure; open decisions are
  flagged rather than glossed over.
- [ ] Launch sequencing has **three phases** (pre-launch / launch / post-launch)
  each with at least one go/no-go criterion.
- [ ] Success Metrics include **both leading and lagging indicators** tied to
  awareness, acquisition, and activation.
- [ ] Every strategic claim is grounded in evidence, a stated assumption, or
  flagged as a hypothesis to validate — no unsupported assertions.
- [ ] If the output is written to a file, it follows `template.md` (a
  skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `gtm-strategy-happy` (happy path) — new SaaS product launch with solid
  customer research and competitive context.
- `gtm-strategy-edge` (edge) — entering a market dominated by one entrenched
  incumbent with 80%+ share.
- `gtm-strategy-adversarial` (adversarial) — executive demands a GTM plan with
  zero customer research; skill must surface the gap, derive from stated
  assumptions, and flag the hypothesis risk.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `ideal-customer-profile` — produces the ICP that feeds the Target Customer
  section; run before this skill when ICP is not yet defined.
- `positioning-statement` — produces a standalone positioning artifact; its
  output integrates directly into the Positioning section.
- `gtm-motions` — specifies the execution tactics (PLG loops, outbound cadences,
  partner plays) that operate within the strategy this skill sets.
- `market-sizing` — provides TAM/SAM/SOM that inform the beachhead scoping and
  expansion arc.
- `competitor-analysis` — competitive landscape data that feeds the positioning
  and pricing sections.

### External Frameworks
- April Dunford, *Obviously Awesome* (2019) — the context-of-use positioning
  method; the house positioning format in this skill derives from her five
  components.
- Geoffrey Moore, *Crossing the Chasm* (1991) — beachhead segment selection and
  the bowling-pin expansion model underpinning the Market Entry section.
- Brian Balfour, "Why Product-Market Fit Is Not Enough" (2017) — the
  product–channel–model–market fit framework that informs channel mix selection.
- [5 GTM Principles You Should Know as a PM](https://www.productcompass.pm/p/5-gtm-principles-with-frameworks-templates) — Product Compass overview of GTM planning for PMs.
