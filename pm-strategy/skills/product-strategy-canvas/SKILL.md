---
name: product-strategy-canvas
description: >
  Build a comprehensive product strategy as a 9-section Product Strategy Canvas —
  vision, market segments, relative cost position, value propositions, trade-offs,
  metrics, growth, capabilities, and defensibility — with coherence checks and
  testable hypotheses. Use when defining product strategy, writing a strategic
  plan, setting product direction, or aligning a team on how the product will
  compete, win, and grow.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/product-strategy-canvas/template.md
---

# Build a Product Strategy Canvas

## Purpose
Produce a coherent product strategy — the **9-section Product Strategy Canvas** —
that states how a product will compete, win, and grow: an aspirational vision,
the problem-defined segments it serves, its cost-vs-value position, per-segment
value propositions, explicit trade-offs, the metrics that measure success, the
growth engine, the capabilities required, and why the position is defensible. The
canvas exists to align a team and guide decisions, so it must be internally
consistent and name the hypotheses that must hold for it to work.

**When NOT to use:** writing a one-line **product vision** alone (use
`product-vision`), **sizing** the opportunity (use `market-sizing`), picking the
**first target segment** in depth (use `beachhead-segment`), or turning strategy
into a quarter of **objectives/roadmap** (that is downstream execution). The
canvas frames the whole strategy; it does not replace those focused artifacts —
it consumes and reconciles them.

## Inputs
- **Required:** the product and its current positioning, plus enough market
  context to reason about segments and competitors (who the product is for, the
  problem it solves, who else solves it). If missing, ask for the product
  description, the customer problem, and the top 2–3 alternatives before drafting;
  do not invent a market.
- **Optional:** company resources/constraints and priorities (shapes trade-offs
  and capabilities), known metrics or a North Star candidate, existing vision or
  segment/sizing work to fold in, competitive/defensibility data, and growth
  motion preference (sales-led vs product-led). Absent these, mark the relevant
  canvas cells as **hypotheses** rather than guessing them as fact.

## Output Contract
The deliverable is a **Product Strategy Canvas** with these 9 sections plus a
coherence check, in order (see `template.md`):

1. **Vision** — the aspirational impact and values; 1–3 sentences, inspiring but concrete.
2. **Market Segments** — 2–3 segments defined by **problems/Jobs-to-Be-Done and desired outcomes** (not demographics); name the first segment and why it goes first.
3. **Relative Costs** — the cost-vs-value position (low-cost like Southwest vs premium value like Starbucks) *relative to competitors*, stated as a deliberate choice.
4. **Value Proposition** — per target segment: **What before** (current pain), **How** (how the product delivers), **What after** (improved outcome), **Alternatives** (what they use today).
5. **Trade-offs** — explicit list of what the product **will NOT do** (features/markets/segments out of scope) and how each "no" amplifies focus.
6. **Key Metrics** — the **North Star** (single measure of durable success) and the **OMTM** (one metric that matters this quarter); they must ladder to the vision.
7. **Growth** — the growth motion (sales-led vs product-led), primary acquisition channels, and a note on unit economics / how it scales.
8. **Capabilities** — competencies and resources required to win; what to **build vs partner** for.
9. **Can't / Won't (Defensibility)** — why competitors can't easily copy this: network effects, switching costs, IP, or other barriers.
Plus **Coherence & Hypotheses** — a short check that the nine cells reinforce
each other, a numbered list of the **critical hypotheses that must be true**, and
a **low-effort experiment** to test each of the most uncertain ones.

Format: prose with clear section headings and one value-proposition table.
Length: ~1–2 pages. Every cell is either grounded in an input or **explicitly
labeled a hypothesis** — never an unmarked guess.

**GOOD (excerpt):**
> **Segment 1 (first):** solo accountants drowning in manual receipt entry (JTBD:
> "close the books without losing evenings"). Chosen first because the pain is
> acute, they pay out of pocket, and word-of-mouth is dense in this niche.
> **Trade-off:** we will **not** build payroll — it dilutes the receipt-automation
> wedge and invites incumbents. *Hypothesis 2 (must be true): solos will switch
> tools for a 10× faster close — test with a 20-user concierge pilot.*

**BAD (excerpt):**
> "Vision: be the best finance app. Segments: SMBs and enterprises. We'll do
> everything customers want and grow fast."
> — fails: vision is generic, segments are demographic and unfocused, no
> trade-offs (says yes to everything), no metrics, no defensibility, no hypotheses.

## Process
1. **Draft the vision** — the aspirational impact and values the product upholds.
2. **Define 2–3 segments** by problem/JTBD and desired outcome; pick the first segment and justify the sequence.
3. **Choose the cost-vs-value position** relative to competitors, as a deliberate trade-off (low-cost or premium value).
4. **Write per-segment value props** — What before / How / What after / Alternatives for each target segment.
5. **State explicit trade-offs** — the features, markets, and segments the product will NOT pursue, and why each "no" sharpens focus.
6. **Set metrics** — a North Star that reflects durable value and a quarterly OMTM; confirm both ladder up to the vision.
7. **Design the growth engine** — sales-led vs product-led, primary channels, and unit-economics logic.
8. **Name required capabilities** — competencies/resources to win, and build-vs-partner calls.
9. **Establish defensibility** — the barriers (network effects, switching costs, IP) that make the position hard to copy.
10. **Run the coherence check** — verify the nine cells reinforce one another; surface the critical hypotheses that must be true and a cheap experiment for each of the most uncertain.
11. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] All **9 canvas sections** are present and filled (not skipped or merged).
- [ ] Segments are defined by **problem/JTBD and outcome**, not demographics, and a **first segment** is named with a reason.
- [ ] A **cost-vs-value position** is chosen explicitly and stated relative to competitors — not left ambiguous.
- [ ] Each target segment has a value prop with **What before / How / What after / Alternatives**.
- [ ] Trade-offs list concrete things the product **will NOT do**; the strategy does not implicitly say yes to everything.
- [ ] **North Star and OMTM** are both present, distinct, and ladder up to the vision.
- [ ] Defensibility names a **specific barrier** (network effects / switching costs / IP / other), not a generic "we're better".
- [ ] A **coherence check** confirms the cells reinforce each other, with **numbered hypotheses** and a low-effort experiment for the most uncertain.
- [ ] Every cell is grounded in an input or **explicitly labeled a hypothesis** — no unmarked guesses.
- [ ] If the canvas is written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `product-strategy-canvas-happy` (happy path) — a well-specified B2B product with clear positioning; the canvas fills all 9 cells coherently with hypotheses.
- `product-strategy-canvas-edge` (edge) — sparse inputs (early-stage idea, no metrics/competitive data); the canvas must label thin cells as hypotheses rather than fabricating them.
- `product-strategy-canvas-adversarial` (adversarial) — a "we'll do everything for everyone" brief with pressure to skip trade-offs; the skill must force focus, segments, and explicit "won't do".

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `product-vision` — the vision cell (section 1) should reuse the one-line vision this skill produces, not restate a new one.
- `market-sizing` — quantifies the segments' opportunity; TAM/SAM/SOM inform which segment goes first and the growth ambition.
- `beachhead-segment` — deepens the "first segment" choice (section 2) the canvas names at a high level.

### External Frameworks
- Ravi Mehta, *Product Strategy Canvas* — the 9-cell structure (vision → defensibility) this skill operationalizes and its "how we compete, win, and grow" framing.
- Roman Pichler, *Strategize* — product vision + strategy laddering to goals; grounds the vision/metrics coherence check.
- Clayton Christensen, *Jobs to Be Done* — the problem/outcome-based segment definition used in section 2 (segments are jobs, not demographics).
- Michael Porter, *Competitive Strategy* — cost-leadership vs differentiation (section 3) and the barriers-to-entry lens for defensibility (section 9).
