---
name: startup-canvas
description: >
  Build a Startup Canvas (Paweł Huryn) that keeps strategy and business model
  distinct but connected — nine Product Strategy sections (Vision, Market
  Segments, Relative Costs, Value Proposition, Trade-offs, Key Metrics, Growth,
  Capabilities, Can't/Won't) plus Cost Structure and Revenue Streams. Use when
  launching a new product, evaluating a startup concept, or when you need both
  strategic clarity and a business model in one artifact.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/startup-canvas/template.md
---

# Build a Startup Canvas (Strategy + Business Model)

## Purpose
Produce a single Startup Canvas for a new product or startup concept that holds
**strategy and business model as two distinct-but-connected halves**: the nine
Product Strategy sections (Vision, Market Segments, Relative Costs, Value
Proposition, Trade-offs, Key Metrics, Growth, Capabilities, Can't/Won't) and the
business model (Cost Structure, Revenue Streams). It forces the two things
generic canvases blur — *why the strategy is hard to copy* (Can't/Won't) and
*what you deliberately won't do* (Trade-offs) — and ends by surfacing the
hypotheses that must be true and cheap experiments to test them. Supports
go/no-go, early strategy alignment, and founder/investor framing.

**When NOT to use:**
- **Established business, corporate strategy, or investor-facing model** → use
  `business-model` (Osterwalder 9-block BMC).
- **You only need speed to test a problem/solution hypothesis** → use
  `lean-canvas` (Ash Maurya) — a leaner, single-page hypothesis sheet.
- **You want only the strategy half (no cost/revenue model)** → use
  `product-strategy-canvas` (the nine sections without the business model).
- Pick Startup Canvas specifically when you need *both* strategic clarity **and**
  a business model for a **new** product, and want strategy kept separate from
  the money.

## Inputs
- **Required:** the product/startup idea and its intended customer — enough to
  name a problem and at least one market segment. If missing, ask for the idea,
  who it's for, and the problem it solves before drafting; do not invent a market.
- **Optional:** competitive landscape and substitutes, founder/team constraints
  and resources, cost positioning intent (low-cost vs premium), pricing ideas,
  known traction or data (read and cite). If absent, state the assumption inline
  and mark it as a hypothesis to validate.

## Output Contract
The deliverable is a **Startup Canvas** with these sections, in order (see
`template.md`):

**Part 1 — Product Strategy**
1. **Vision** — the aspiration and values; why the team shows up. 1–2 sentences.
2. **Market Segments** — 2–3 segments defined by problems/JTBD (not demographics), with the first segment named and *why it's first*.
3. **Relative Costs** — the cost-positioning choice: optimize for low cost or unique value (low cost ≠ low price).
4. **Value Proposition** — for each segment: *What before* (problem state) → *How* (features) → *What after* (outcome) → *Alternatives* (why you win vs competitors/substitutes).
5. **Trade-offs** — explicit list of what you will **NOT** do; each creates focus.
6. **Key Metrics** — a North Star Metric plus the One Metric That Matters (OMTM) for this quarter.
7. **Growth** — Product-Led vs Sales-Led, and the preferred channels.
8. **Capabilities** — competencies/resources to acquire; build vs partner.
9. **Can't/Won't** — why competitors can't or won't copy the *integrated* set of choices, and a note that the elements reinforce each other.

**Part 2 — Business Model**
10. **Cost Structure** — main costs; which recur; how they scale.
11. **Revenue Streams** — revenue per channel, pricing approach (penetration / value-based / competitive / usage-based / SaaS), and whether it's scalable.

**Then:** a short **Hypotheses & Experiments** list — the assumptions that must be
true, each paired with a low-effort test.

Format: labeled prose/bullets per section + the hypotheses list. Length: ~1–2
pages. Strategy and business model stay in separate parts. Any figure is either
cited or labeled a hypothesis.

**GOOD (excerpt):**
> **5. Trade-offs** — We will **not** support self-hosting, will **not** sell to
> enterprise (>500 seats) in year 1, and will **not** build a mobile app. Focus:
> web-first, SMB, opinionated defaults over configurability.
> **9. Can't/Won't** — Incumbents *won't* strip their configurability (it anchors
> enterprise deals), so our opinionated simplicity + SMB pricing + PLG motion
> reinforce each other and are painful for them to copy without cannibalizing.
> *Hypothesis: SMBs prefer defaults over config — test with a 20-user concierge pilot.*

**BAD (excerpt):**
> "Vision: be the best tool. Segments: everyone who needs it. Trade-offs: none —
> we'll do it all. Unfair advantage: our great team."
> — fails: no problem-defined segment, no real trade-offs (so no focus), a
> one-element "advantage" instead of an integrated Can't/Won't, no business model,
> no hypotheses.

## Process
1. **Vision** — state the aspiration and values in 1–2 sentences; keep it simple, it will evolve.
2. **Market Segments** — identify 2–3 segments by problem/JTBD; name the first target and why it's first.
3. **Relative Costs** — choose the cost positioning (low cost vs unique value).
4. **Value Proposition** — for each segment write What before → How → What after → Alternatives.
5. **Trade-offs** — list explicit "will not do" choices that create focus.
6. **Key Metrics** — set a North Star and this quarter's OMTM.
7. **Growth** — pick PLG vs SLG and the primary channels.
8. **Capabilities** — name competencies/resources to acquire and build-vs-partner calls.
9. **Can't/Won't** — argue why the *integrated* strategy is hard to copy and check the elements reinforce each other.
10. **Cost Structure & Revenue Streams** — estimate costs (recurring? scaling?) and revenue per channel with a pricing approach.
11. **Coherence check** — verify the eleven sections reinforce each other (strategy ↔ business model), then list the must-be-true hypotheses each with a low-effort experiment.
12. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] All **11 sections** are present, and strategy (1–9) and business model (10–11) are kept as **separate parts**.
- [ ] **Market Segments** are defined by problems/JTBD (not demographics), with a first segment named and justified.
- [ ] **Value Proposition** uses the What-before → How → What-after → Alternatives structure for each segment.
- [ ] **Trade-offs** lists concrete things the product will **NOT** do (not empty, not vague).
- [ ] **Can't/Won't** argues the *integrated* set of choices is hard to copy — not a single "unfair advantage" — and notes the elements reinforce each other.
- [ ] **Key Metrics** names both a North Star and a quarterly OMTM.
- [ ] A **Hypotheses & Experiments** list surfaces the must-be-true assumptions, each with a low-effort test.
- [ ] Any figure is **cited** or **labeled a hypothesis** — no unsupported numbers.
- [ ] If the canvas is written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `startup-canvas-happy` (happy path) — a well-specified new B2B product yields a full 11-section canvas with real trade-offs and an integrated Can't/Won't.
- `startup-canvas-edge` (edge) — thin/consumer input where segments and figures must be marked as hypotheses and paired with cheap experiments.
- `startup-canvas-adversarial` (adversarial) — a "no trade-offs, we'll do everything, our team is the advantage" ask the skill must push back on and rebuild into real trade-offs and an integrated defensibility argument.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `product-strategy-canvas` — the nine strategy sections on their own; Startup Canvas adds the Cost Structure + Revenue Streams business model on top.
- `business-model` — Osterwalder 9-block BMC for established businesses / investor materials; the alternative when strategy needn't be separated from the model.
- `lean-canvas` — Ash Maurya's leaner single-page hypothesis sheet; the alternative when you just need speed to test a problem/solution.
- `value-proposition` — deepens the What-before/How/What-after/Alternatives block per segment.
- `north-star-metric` — sets the North Star that section 6 references.

### External Frameworks
- Paweł Huryn, [*Startup Canvas: Product Strategy and a Business Model for a New Product*](https://www.productcompass.pm/p/startup-canvas) — the canvas this skill implements and its rationale for separating strategy from business model.
- Paweł Huryn, [*Product Strategy Canvas*](https://www.productcompass.pm/p/product-strategy-canvas) — the nine strategy sections (Part 1).
- Alexander Osterwalder, *Business Model Generation* — the BMC this canvas deliberately restructures (why no Key Partnerships/Resources, why add Vision and Can't/Won't).
