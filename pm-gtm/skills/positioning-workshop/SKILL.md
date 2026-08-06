---
name: positioning-workshop
description: >
  Use when a product team needs to develop or reset their positioning from
  scratch, wants to run a structured positioning session with cross-functional
  stakeholders, or needs to generate the raw material that feeds a positioning
  statement or messaging framework.
version: 0.1.0
type: workflow
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/positioning-workshop/template.md
---

# Positioning Workshop (AI Co-Facilitation)

## Purpose
Run a six-exercise positioning workshop that leads a cross-functional team
through April Dunford's positioning process in a single session. The PM plays
the facilitator; Claude acts as AI co-facilitator — running each exercise in
sequence, capturing the team's answers, surfacing tensions, and synthesising
the outputs into a Positioning Workshop Summary with a draft positioning
statement. The summary becomes the primary input for `positioning-statement`
(formalisation) and `positioning-ideas` (angle exploration).

**When NOT to use:** if the team already has an agreed-upon positioning basis
and only needs to formalise wording, use `positioning-statement` instead. If
the team wants to explore multiple positioning angles before committing to a
process, use `positioning-ideas` first. This workshop assumes the team is
ready to do the generative work — not passively review options.

## Inputs
- **Required:** product name and a one-paragraph product description — if
  absent, ask for it before starting Exercise 1; do not guess the product.
- **Required:** team composition — who is in the room (sales, marketing,
  product, engineering, CS)? Surface this at the session open so responses
  can be attributed.
- **Optional:** existing positioning artefacts (previous statements, pitch
  decks, battle cards) — read and treat as priors to challenge, not anchors
  to preserve.
- **Optional:** target market or segment hypothesis — if provided, surface it
  in Exercise 4 for the team to validate or override.

## Output Contract
The deliverable is a **Positioning Workshop Summary** structured as six
exercise outputs plus a synthesised positioning statement (see `template.md`):

1. **Competitive Alternatives** — a ranked list of what customers would use if
   this product did not exist, with a one-line rationale for each.
2. **Unique Attributes** — a list of features or capabilities that the product
   does uniquely well vs. every alternative on the list above.
3. **Value Enabled** — for each unique attribute, the customer value it
   delivers (not the feature description — the outcome the customer gains).
4. **Target Customers** — the customer segment(s) who care most about the
   identified value; include what makes them the best-fit buyers.
5. **Market Frame of Reference** — the category or context the team chooses to
   position within, with a brief rationale for why that frame serves customers
   better than alternatives considered.
6. **Positioning Statement Draft** — a synthesised statement in the canonical
   form: *For [target customers] who [need/want], [product] is a [market frame]
   that [unique value]. Unlike [competitive alternative], [product]
   [differentiator].*

Format: structured prose per exercise + the canonical positioning statement.
Length: one page per exercise is too long — aim for tight, decision-ready
bullets and a two-sentence statement. If the team produced genuine disagreement
in any exercise, surface it as a flagged tension rather than papering it over.

**GOOD (excerpt):**
> **Exercise 2 — Unique Attributes**
> - Real-time compliance engine that flags regulatory issues at draft time (no alternative does this inline)
> - Native integration with the three EHR systems used by 90% of EU clinics
> - Audit trail that is court-admissible without additional export steps
>
> *These attributes were agreed by all five participants.*

**BAD (excerpt):**
> "We are the best solution because we do everything better and faster."
> — fails: no specific attributes named, not differentiated against any
> alternative, cannot drive a positioning statement.

## Process
1. **Open the session** — confirm the product description and team composition;
   surface any existing positioning artefacts. Set the expectation: every
   exercise builds on the previous one; skipping is not allowed.
2. **Exercise 1 — Competitive alternatives** — ask: "If our product did not
   exist, what would each of your customers use instead?" Prompt for a complete
   list including doing-nothing. Rank by frequency of customer mention.
3. **Exercise 2 — Unique attributes** — ask: "For each alternative on the
   list, what does our product do that the alternative cannot or does not do?"
   Insist on specifics; reject vague superlatives ("we're better") in real time.
4. **Exercise 3 — Value (not features)** — for each attribute from Exercise 2,
   ask: "What does this enable the customer to achieve that they could not
   achieve before?" Translate each feature to an outcome.
5. **Exercise 4 — Target customers** — ask: "Who cares most about the value
   we've identified? What makes them the best-fit buyers?" If a segment
   hypothesis was provided, surface it here for validation.
6. **Exercise 5 — Market frame of reference** — present two or three candidate
   frames derived from the alternatives and value identified; ask the team to
   choose and state why. The frame should help the target customer understand
   the product, not what the team finds flattering.
7. **Exercise 6 — Positioning statement draft** — synthesise the five exercise
   outputs into the canonical positioning statement form. Present the draft,
   flag any unresolved tensions explicitly, and ask if the team endorses it or
   needs one round of revision.
8. **Capture flagged tensions** — any exercise where the team disagreed or
   produced multiple competing answers gets a one-line tension note in the
   summary so follow-on owners know what to resolve.
9. Run the Quality Bar; revise if any item fails; then return the Positioning
   Workshop Summary.

## Quality Bar
Before returning, confirm:
- [ ] All six exercises are present in the summary — none skipped, even if an
  exercise produced only a tension note.
- [ ] Exercise 1 includes at least two competitive alternatives (one of which
  may be "do nothing") and a rationale for each.
- [ ] Exercise 2 attributes are specific and falsifiable — no vague
  superlatives ("best," "fastest") without a concrete backing claim.
- [ ] Exercise 3 translates features to customer outcomes — no attribute is
  left as a feature description without a value statement.
- [ ] Exercise 4 names a customer segment with at least one stated reason why
  they are the best-fit buyer for the identified value.
- [ ] Exercise 5 names a chosen market frame and briefly explains why it serves
  the target customer better than alternatives considered.
- [ ] The positioning statement follows the canonical form and is internally
  consistent with Exercises 1–5.
- [ ] Any genuine team disagreement is surfaced as a flagged tension rather
  than silently resolved.
- [ ] If the output is written to a file, it follows `template.md` — all six
  exercise sections plus the Positioning Statement section present, in order,
  headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `positioning-workshop-happy` — cross-functional team with good product-market
  fit signals; exercises run smoothly.
- `positioning-workshop-edge` — team has strong disagreement on competitive
  alternative; workshop must surface the tension rather than paper it over.
- `positioning-workshop-adversarial` — team wants to skip exercises and "just
  get the statement"; skill must hold the process.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `positioning-ideas` — generates multiple positioning angle options before
  committing to a workshop; use upstream if the team needs a menu of directions
  before running the full facilitated process.
- `positioning-statement` — formalises and refines a chosen positioning basis
  into a polished, multi-format statement; use downstream of this workshop.
- `beachhead-segment` — identifies the best first target segment; the target
  customer output from Exercise 4 feeds directly into beachhead analysis.
- `competitor-analysis` — deep competitive teardown that enriches the
  competitive alternatives exercise with evidence-based differentiation.

### External Frameworks
- April Dunford, *Obviously Awesome* (2019) — the six-step positioning process
  this workshop operationalises; the canonical positioning statement form in
  Exercise 6 is taken directly from her framework.
- Geoffrey Moore, *Crossing the Chasm* (1991) — whole-product and market-frame
  thinking that informs Exercise 5 (market frame of reference).
- Steve Blank, *The Four Steps to the Epiphany* (2005) — customer-type
  segmentation and "who cares most" framing that underpins Exercise 4.
