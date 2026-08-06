---
name: ansoff-matrix
description: >
  Map growth options onto the Ansoff Matrix — market penetration, market
  development, product development, diversification — with a risk profile per
  quadrant and a recommended sequenced growth path. Use when weighing growth
  options, planning market or product expansion, choosing where to invest for
  growth, or building a growth strategy narrative.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/ansoff-matrix/template.md
---

# Ansoff Growth Matrix

## Purpose
Produce an Ansoff Matrix that places concrete growth options into the four
product×market quadrants — **market penetration** (current product / current
market), **market development** (current product / new market), **product
development** (new product / current market), and **diversification** (new
product / new market) — attaches an explicit risk profile to each quadrant, and
recommends a **sequenced growth path** (which quadrant to pursue first, next, and
later) tied to the company's capabilities and constraints. Supports where-to-grow
decisions, expansion planning, and the growth section of a strategy narrative.

**When NOT to use:** sizing the opportunity behind a chosen option (use
`market-sizing`), competitive teardown (use `competitor-analysis`), picking a
first customer segment inside one market (use `beachhead-segment`), or feature-level
roadmap sequencing (use an execution/roadmap skill). Ansoff frames *directions* of
growth; it does not size, staff, or schedule the plan.

## Inputs
- **Required:** the current product(s) and the current market definition
  (customer type, segment, geography). If missing, ask for these before mapping;
  without a clear "current product / current market" anchor the four quadrants
  are meaningless.
- **Optional:** current penetration/traction and performance, growth targets and
  timeline, company capabilities and constraints (capital, team, brand), known
  adjacent markets or product ideas, and competitive dynamics. If capabilities and
  constraints are absent, state the sequencing recommendation as capability-
  contingent rather than inventing them.

## Output Contract
The deliverable is an **Ansoff growth-matrix memo** with these sections (see
`template.md`):

1. **Anchor** — the current product and current market, stated explicitly, so the "new" axes are unambiguous.
2. **Matrix** — a 2×2 table (Current/New Product × Current/New Market) with the four quadrant names in place.
3. **Quadrant analysis** — for each of the four quadrants: 2–3 concrete, named growth options for *this* product; the **risk level** (Low / Medium / Medium / High respectively) with a one-line why; and an indicative timeline. Diversification is flagged highest-risk; penetration lowest.
4. **Recommended growth path** — a sequenced 1→2→3 ordering across quadrants (typically penetration → development → diversification), each step justified by risk-reward and by the stated capabilities/constraints, with a trigger for moving to the next step. Explicitly warns against pursuing all four at once.
5. **Key assumptions & risks** — numbered, each with a confidence level (high/med/low) and how to validate the most uncertain.

Format: prose + one 2×2 matrix table. Length: ~1–2 pages. Every option is
specific to the product (not a generic list), and every quadrant carries its
risk label.

**GOOD (excerpt):**
> **Product development (new product / current market) — risk: Medium.** Same buyers, new build. Options: (1) add an approvals/workflow module for existing e-sign customers; (2) a compliance-audit add-on. Timeline ~12–18 mo.
> **Recommended path:** 1) **Penetration** now — cut churn + upsell (low risk, funds the rest); 2) **Market development** into DACH once EN retention >90% (trigger); 3) revisit **diversification** only after step 2 pays back. Do **not** run market development and diversification in parallel — capital and brand can't stretch to both.

**BAD (excerpt):**
> "We should grow via penetration, market development, product development, and diversification — all high-opportunity areas we'll pursue in parallel."
> — fails: generic options not tied to the product, no risk differentiation across quadrants, no sequencing, and recommends the classic spread-too-thin anti-pattern.

## Process
1. **Anchor the axes** — state the current product and current market plainly; everything "new" is defined relative to these.
2. **Draw the matrix** — lay out the 2×2 with the four quadrant names.
3. **Fill each quadrant** — 2–3 concrete growth options specific to this product, per quadrant.
4. **Assign risk** — label each quadrant Low/Medium/Medium/High (penetration → development → diversification) with a one-line rationale and indicative timeline.
5. **Sequence the path** — recommend a 1→2→3 ordering justified by risk-reward and the stated capabilities/constraints; define the trigger to advance each step; warn against parallel pursuit of all quadrants.
6. **Map assumptions** — number the load-bearing assumptions, rate confidence, name validation steps.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **current product and current market are stated explicitly** so "new product" / "new market" are unambiguous.
- [ ] All **four quadrants** are populated, each with 2–3 **concrete, product-specific** growth options (not a generic checklist).
- [ ] Each quadrant carries an **explicit risk level**; penetration is lowest and diversification is highest, each with a one-line rationale.
- [ ] A **sequenced growth path** (1→2→3) is recommended with a justification and an advance trigger per step.
- [ ] The memo **warns against pursuing all four quadrants at once** (spread-too-thin anti-pattern).
- [ ] The sequencing is tied to stated **capabilities/constraints**, or explicitly labeled capability-contingent when those are unknown.
- [ ] Key assumptions are **numbered** with confidence levels and validation steps.
- [ ] If the memo is written to a file, it follows `template.md` — all 5 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `ansoff-matrix-happy` (happy path) — a well-anchored SaaS product with capabilities stated; produces a full four-quadrant map and a defensible sequence.
- `ansoff-matrix-edge` (edge) — thin capability/constraint data; sequencing must be stated as capability-contingent rather than invented.
- `ansoff-matrix-adversarial` (adversarial) — pressure to "pursue everything now"; the skill must differentiate risk and refuse the all-at-once anti-pattern.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — sizes the opportunity behind a chosen quadrant; consumes the market boundaries this skill sets.
- `competitor-analysis` — competitive dynamics inform quadrant risk and the sequencing triggers.
- `beachhead-segment` — picks the first segment within a market-development or diversification move.

### External Frameworks
- H. Igor Ansoff, "Strategies for Diversification," *Harvard Business Review* (1957) — the original product/market growth matrix this skill operationalizes.
- H. Igor Ansoff, *Corporate Strategy* (1965) — the gap-analysis and risk-escalation logic (penetration lowest risk → diversification highest) behind the sequenced path.
