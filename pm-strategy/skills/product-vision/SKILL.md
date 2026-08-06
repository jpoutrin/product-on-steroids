---
name: product-vision
description: >
  Craft an inspiring, achievable, and emotionally resonant product vision — a
  memorable one-sentence north star plus the reasoning behind it. Use when
  defining or refining a product vision, writing a vision statement, aligning a
  team around a shared direction, or preparing a vision to anchor strategy.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/product-vision/template.md
---

# Craft a Product Vision

## Purpose
Produce a compelling **product vision**: a single memorable sentence describing
the future the product is working toward, backed by the reasoning that makes it
inspiring, achievable, and emotionally resonant. The vision is the north star
that motivates the team and aligns stakeholders *before* strategy, roadmap, and
OKRs are set — it answers "what are we aspiring to, and why does it matter?"

**When NOT to use:** picking *how* to get there over the next quarters (use
`product-strategy-canvas` or `outcome-roadmap`), setting measurable targets (use
`brainstorm-okrs` or `north-star-metric`), or writing external launch/marketing
copy (use `positioning-statement` / `press-release`). Vision sets direction and
meaning; it does not choose the plan or the metric.

## Inputs
- **Required:** the product/company and the core problem it solves — what it is,
  who it serves, and the change it wants to create. If missing, ask for these
  three before drafting; do not invent a mission the user has not confirmed.
- **Optional:** current state and traction, market positioning, company values,
  time horizon (default: 3–5 year aspiration), audience emphasis (customers /
  employees / investors), and any existing vision to refine. Read and cite any
  workspace files the user points to.

## Output Contract
The deliverable is a **product-vision brief** with these sections (see
`template.md`):

1. **Context** — the product, who it serves, and the core problem, in 2–4 lines.
2. **Vision statement** — the recommended vision as **one memorable sentence**,
   in clear, jargon-free, emotionally resonant language.
3. **Options considered** — 3–5 distinct vision variations (each one sentence)
   spanning different angles/tones, so the choice is deliberate not accidental.
4. **Rationale** — why the recommended option wins on all three tests:
   **inspiring** (motivates the team), **achievable** (credible given
   resources/market), and **emotional** (creates meaning and connection).
5. **Alignment** — how the vision ties to company values and the market
   opportunity, and one line each on what it means for customers, employees, and
   investors.

Format: prose + a short options list. Length: ~½–1 page. The vision statement
itself must be **one sentence** a person can repeat from memory.

**GOOD (excerpt):**
> **Vision:** *A world where any small business can get paid the moment the work
> is done — no invoices, no waiting, no chasing.*
> Inspiring: reframes cash flow as instant, not a monthly ordeal. Achievable:
> builds on rails we already run for 40k merchants. Emotional: speaks to the
> founder's dread of an empty account.

**BAD (excerpt):**
> "Our vision is to be the leading AI-powered platform that leverages synergies
> to deliver best-in-class solutions for our stakeholders."
> — fails: jargon, no emotion, not memorable, describes no future for a real
> person, and could belong to any company.

## Process
1. **Gather context** — confirm the product, the customer, and the core problem;
   read any files the user provides.
2. **Find the future** — envision the ideal end state for the customer and the
   company if the problem were fully solved.
3. **Draft options** — write 3–5 one-sentence vision variations across different
   angles (customer outcome, world-change, values-led, category-creating).
4. **Test each** against inspiring / achievable / emotional; discard the weak.
5. **Recommend** the strongest and explain why on all three tests.
6. **Anchor it** — connect to company values, market opportunity, and the three
   audiences (customers, employees, investors).
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The vision statement is **one sentence** and memorable enough to repeat.
- [ ] It is **jargon-free** and describes a future for a real person, not an org chart.
- [ ] It passes all three tests — **inspiring, achievable, emotional** — and the rationale says how.
- [ ] **3–5 distinct options** were offered before the recommendation, so the choice is deliberate.
- [ ] It sets *direction*, not a plan or a metric (no roadmap items, no KPIs masquerading as vision).
- [ ] It ties explicitly to company values and market opportunity.
- [ ] If the brief is written to a file, it follows `template.md` — all 5 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `product-vision-happy` (happy path) — a scoped B2B product with clear problem and traction.
- `product-vision-edge` (edge) — refining an existing vague/jargon-laden vision into a memorable one.
- `product-vision-adversarial` (adversarial) — a thin ask ("give us a vision") the skill must scope and resist filling with buzzwords or a strategy/metric.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `product-strategy-canvas` — turns the vision into the how (bets, positioning); consumes the direction this skill sets.
- `north-star-metric` — makes the vision measurable; the vision must exist first so the metric has something to point at.
- `brainstorm-okrs` — translates vision into near-term objectives; downstream of a settled vision.

### External Frameworks
- Geoffrey Moore, *Crossing the Chasm* — the "elevator pitch"/positioning template as a discipline for a single credible, customer-anchored future statement.
- Simon Sinek, *Start With Why* — the "why" as the emotional core that makes a vision inspire rather than merely inform.
- Roman Pichler, *Strategize* — the product-vision-as-north-star model: an inspiring, shared, and continuous aspiration that anchors (and outlives) strategy.
