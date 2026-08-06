---
name: market-sizing
description: >
  Estimate market size (TAM, SAM, SOM) using both top-down and bottom-up
  methods, with growth projections and explicit assumptions. Use when sizing a
  market opportunity, estimating addressable market, building a business case,
  evaluating market entry, or preparing an investor pitch.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a9
---

# Estimate Market Size (TAM, SAM, SOM)

## Purpose
Produce a defensible estimate of the Total Addressable Market (TAM), Serviceable
Addressable Market (SAM), and Serviceable Obtainable Market (SOM) for a product
or opportunity — triangulated top-down **and** bottom-up, with every load-bearing
assumption made explicit so a reader can challenge or update it. Supports
go/no-go, prioritization, business-case, and fundraising decisions.

**When NOT to use:** detailed financial modeling / revenue forecasting for an
existing line (use finance metrics skills), competitive teardown (use
`competitor-analysis`), or choosing a first segment (use `beachhead-segment`).
Market sizing bounds the opportunity; it does not pick the plan.

## Inputs
- **Required:** the product/opportunity and its market boundaries — problem
  space, customer type (B2B/B2C, segment), geography. If missing, ask for these
  three before sizing; do not guess the scope.
- **Optional:** preferred method (top-down vs bottom-up emphasis), pricing anchor,
  known population/unit counts, analyst reports or internal data (read and cite
  them), time horizon (default: current + 2–3 year projection).

## Output Contract
The deliverable is a **market-sizing memo** with these sections (see
`template.md`):

1. **Market Definition** — problem space, segment & geographic boundaries, scoping decisions.
2. **TAM** — a top-down estimate (with sources) *and* a bottom-up estimate (units × price × frequency), the reconciliation of the two, and a single current TAM figure.
3. **SAM** — the serviceable slice of TAM, the constraints that define it (geography, language, channel, product, pricing tier), and SAM as a % of TAM with reasoning.
4. **SOM** — realistically obtainable share over 1–3 years, its basis (competitive position, GTM capacity, traction), and SOM as a % of SAM with reasoning.
5. **Summary table** — TAM/SAM/SOM as three distinct numbers, current vs 2–3-year projection.
6. **Growth drivers & trends** — what could expand or contract the market.
7. **Key assumptions & risks** — numbered, each with a confidence level (high/med/low) and how to validate the most uncertain ones.

Format: prose + one summary table. Length: ~1–2 pages. Every number is either
cited or labeled an assumption/estimate — never an unsupported figure.

**GOOD (excerpt):**
> **TAM (bottom-up):** ~24M EU SMBs × 15% needing e-signature × €180/yr = **€0.65B**.
> **TAM (top-down):** EU e-signature market €1.2B (Source X, 2025) × ~55% SMB share = **€0.66B**. The two reconcile within ~2%.
> *Assumption 3 (med confidence): 15% of SMBs have a recurring signature need — validate via a 200-SMB survey.*

**BAD (excerpt):**
> "The market is huge — roughly €5B TAM, and we can capture 10%."
> — fails: one number, one method, no bottom-up cross-check, no sources, SOM is a round guess with no basis.

## Process
1. **Define the market** — fix problem space, segment, geography, and scoping decisions.
2. **Top-down** — start from total industry size (cite it) and narrow to the relevant slice.
3. **Bottom-up** — build from unit economics (customers × price × frequency) to cross-validate.
4. **Reconcile** — compare the two TAM figures; explain and narrow any gap.
5. **Scope SAM** — apply product/channel/geography/pricing constraints to TAM.
6. **Estimate SOM** — realistic 1–3-year share given competition and GTM capacity.
7. **Project growth** — how TAM/SAM/SOM evolve over 2–3 years.
8. **Map assumptions** — number them, rate confidence, name validation steps.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] TAM, SAM, and SOM are reported as **three distinct numbers** (value and, where relevant, volume).
- [ ] TAM is estimated **both** top-down and bottom-up, and the two are explicitly reconciled.
- [ ] Every market figure is **cited** or clearly **labeled an assumption/estimate**.
- [ ] SAM and SOM are expressed as a % of the level above, each with stated reasoning.
- [ ] SOM is a **defensible fraction** of SAM tied to competitive position / GTM capacity — not a round guess.
- [ ] Key assumptions are **numbered** with confidence levels and validation steps.
- [ ] A 2–3-year projection is included alongside current figures.

## Validation & Eval
Scenario cards in `evals/`:
- `market-sizing-b2b-saas-eu` (happy path) — bottom-up-preferred B2B SaaS sizing.
- `market-sizing-consumer-edge` (edge) — sparse-data consumer market needing proxy anchors.
- `market-sizing-adversarial` (adversarial) — vague ask ("size the AI market") the skill must scope down and refuse to one-number.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `beachhead-segment` — picks the first target segment; consumes the SAM/SOM boundaries this skill sets.
- `competitor-analysis` — competitive position and share data feed the SOM defensible-fraction estimate.

### External Frameworks
- Bill Aulet, *Disciplined Entrepreneurship* (2013), Steps 2 & 5 — canonical **bottom-up TAM** (end users × annual revenue per user) and the dual top-down/bottom-up, conservative-estimate discipline this skill is built on.
- Steve Blank, *The Four Steps to the Epiphany* — TAM/SAM/target-market segmentation for new ventures.
- [Sequoia — Writing a Business Plan](https://sequoiacap.com/article/writing-a-business-plan/) — investor-lens "market potential" expectations for a sizing memo used in fundraising.
