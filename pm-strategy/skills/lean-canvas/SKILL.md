---
name: lean-canvas
description: >
  Draft an Ash Maurya Lean Canvas — all nine blocks (Problem, Customer Segments,
  UVP, Solution, Channels, Revenue Streams, Cost Structure, Key Metrics, Unfair
  Advantage) — and surface the riskiest assumptions with cheap validation
  experiments. Use when de-risking an early-stage startup or new venture, capturing
  a business hypothesis on one page, pressure-testing a problem before building, or
  aligning a founding team fast.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/lean-canvas/template.md
---

# Draft a Lean Canvas (Ash Maurya)

## Purpose
Capture the whole business model of an early-stage venture on **one page** — Ash
Maurya's nine-block Lean Canvas — so a founding team can see its hypothesis at a
glance, spot the parts most likely to kill the business, and design the cheapest
experiments to test them first. Lean Canvas is deliberately **problem- and
risk-first**: it front-loads the customer's problem and the assumptions that carry
the most uncertainty, treating the canvas as a snapshot to iterate, not a plan to
execute.

**When NOT to use:** for an established product with a proven model where you need
the classic operations lens (partners, activities, resources), use `business-model`
(the Osterwalder Business Model Canvas). For a defensible strategy narrative
(vision, trade-offs, coherence), use `product-vision` or `product-strategy`. To
quantify the opportunity, use `market-sizing`. Lean Canvas is a fast hypothesis
brainstorm, **not** a strategy document or a financial model.

## Inputs
- **Required:** the product/venture idea and at least a first guess at **who has
  the problem** (customer segment) and **what problem** you believe they have. If
  the user gives only a solution ("an app that does X"), ask what problem it solves
  and for whom before drafting — Lean Canvas starts from the problem, not the
  solution.
- **Optional:** existing customer/interview evidence, competitor or alternative
  solutions the segment uses today, a pricing idea, known costs, any traction or
  metrics. Absent these, fill the block as an explicit **assumption** and flag it,
  rather than inventing facts.

## Output Contract
The deliverable is a **Lean Canvas** — the nine blocks plus a riskiest-assumptions
list — filled in canvas order (see `template.md`):

1. **Problem** — top 1–3 problems for the segment, plus the **existing
   alternatives** customers use today (the incumbent to beat).
2. **Customer Segments** — target segment(s) and, called out separately, the
   **early adopters** you would test with first.
3. **Unique Value Proposition** — a single, clear, compelling message stating why
   you are different and worth attention; a **high-level concept** analogy is
   optional (e.g. "X for Y").
4. **Solution** — the smallest set of features (roughly one per problem) that would
   address the top problems; kept deliberately thin.
5. **Channels** — paths to reach the early adopters (free and paid).
6. **Revenue Streams** — revenue model, pricing idea, and what drives revenue.
7. **Cost Structure** — the main fixed and variable costs to operate and acquire.
8. **Key Metrics** — the few numbers that tell you the business is working
   (activation, retention, revenue signals).
9. **Unfair Advantage** — something that **cannot be easily copied or bought**
   (insider info, community, personal authority, patents) — or, honestly, "none
   yet."
10. **Riskiest assumptions & experiments** — the 3–5 assumptions that would sink
    the business if wrong, ranked, each paired with a cheap test (interview,
    landing page, concierge/Wizard-of-Oz MVP).

Format: the 3×3 canvas rendered as nine labelled blocks (prose or a table), then a
short ranked risk list. Length: ~1 page. Each block is 1–5 tight bullets, **specific
and testable**, not marketing fluff; unknowns are labelled as assumptions.

**GOOD (excerpt):**
> **Problem:** Freelance designers lose ~4 hrs/week chasing late invoices.
> *Existing alternatives:* manual email reminders, spreadsheets, generic tools like PayPal.
> **Customer Segments:** solo B2B freelancers, EU. *Early adopters:* Dribbble-active designers billing >€3k/mo.
> **UVP:** "Get paid on time without the awkward chase." *(High-level concept: autopilot for invoice reminders.)*
> **Unfair Advantage:** founder is a well-known figure in a 20k-designer community (hard to copy).
> *Riskiest assumption (rank 1): designers will pay to automate reminders. Test: landing page + €9/mo pre-order, target 20 sign-ups in 2 weeks.*

**BAD (excerpt):**
> "**Problem:** people need a better invoicing app. **Solution:** an app with AI. **UVP:** the best invoicing tool. **Unfair Advantage:** great UX and first-mover."
> — fails: problem is a restated solution with no segment and no existing alternative; UVP is a generic superlative; "great UX / first-mover" are not real unfair advantages (both are copyable); no early adopters and no riskiest-assumption tests.

## Process
1. **Anchor on segment + problem.** Name the customer segment and the top 1–3
   problems; if only a solution was given, elicit the problem first.
2. **List existing alternatives** the segment uses today — this is the real
   competition and the bar the UVP must clear.
3. **Split out early adopters** from the broader segment — who you would recruit
   for the first tests.
4. **Write the UVP** as one sharp, differentiated line (not "better"); add a
   high-level concept analogy if it clarifies.
5. **Sketch the Solution** as the thinnest feature set — ideally one per top
   problem; resist scope creep.
6. **Map Channels** to reach early adopters (free and paid).
7. **Draft Revenue Streams and Cost Structure** — pricing/revenue model and the
   main fixed/variable costs.
8. **Pick Key Metrics** — the few activation/retention/revenue numbers that prove
   the model works.
9. **State the Unfair Advantage** — only genuinely hard-to-copy items; write "none
   yet" rather than pad it with copyable traits.
10. **Rank riskiest assumptions and design cheap tests** — order by "would sink the
    business if wrong × most uncertain," pair each with a lightweight experiment.
11. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] **All nine blocks** are present and filled (or explicitly "assumption" /
      "none yet" — never left blank).
- [ ] The Problem block names concrete problems **and** the **existing
      alternatives** the segment uses today.
- [ ] Customer Segments **separately identifies early adopters**, not just a broad
      market.
- [ ] The UVP is a **single differentiated line**, not a generic superlative
      ("better", "best", "easy-to-use").
- [ ] Solution is a **thin feature set** (~one per problem), not a full backlog.
- [ ] Unfair Advantage lists only **hard-to-copy** items (or honestly "none yet") —
      no "great UX", "first-mover", or "hard work".
- [ ] A ranked list of **3–5 riskiest assumptions**, each paired with a **cheap
      validation experiment**, is included.
- [ ] Every unknown block is **labelled an assumption**, not stated as fact.
- [ ] If written to a file, it follows `template.md` — all sections present, in
      order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `lean-canvas-happy` (happy path) — a concrete early-stage B2B idea with a clear
  segment; expects all nine blocks plus ranked risky-assumption tests.
- `lean-canvas-edge` (edge) — a solution-first pitch with no stated problem; the
  skill must elicit/frame the problem and flag unknowns as assumptions.
- `lean-canvas-adversarial` (adversarial) — a padded pitch with fake unfair
  advantages ("great UX, first-mover") that the skill must reject or reframe.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `business-model` — the classic Osterwalder Business Model Canvas (partners /
  activities / resources); use it once the model is proven and you need the
  operations lens Lean Canvas omits.
- `product-vision` — supplies the vision and strategic narrative Lean Canvas
  deliberately leaves out.
- `market-sizing` — quantifies the opportunity behind the Customer Segments and
  Revenue blocks (TAM/SAM/SOM).

### External Frameworks
- Ash Maurya, *Running Lean* (2nd ed., 2012) — the canonical Lean Canvas, its
  nine blocks, and the "capture the riskiest assumptions first" discipline this
  skill is built on.
- Ash Maurya, *Scaling Lean* — traction metrics and the customer-factory model
  behind the Key Metrics block.
- Steve Blank & Bob Dorf, *The Startup Owner's Manual* — customer-development and
  early-adopter concepts feeding the Problem / Customer Segments blocks.
