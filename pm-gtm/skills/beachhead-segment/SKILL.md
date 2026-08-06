---
name: beachhead-segment
description: >
  Identify the narrowest, most winnable first market segment a product should
  dominate before expanding. Use when choosing a first target market, deciding
  where to concentrate limited GTM resources, or planning an initial market entry
  strategy.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/beachhead-segment/template.md
---

# Choose a Beachhead Market Segment

## Purpose
Produce a strategic beachhead segment decision — the one narrow slice of the market
a product should concentrate on first to win reference customers, validate PMF, and
build a platform for adjacent expansion. The analysis surfaces candidate segments,
scores them against Geoffrey Moore's four beachhead criteria (acute pain, 10x
advantage, reachability, referral potential), picks the strongest one, and defines
what winning looks like before moving on.

**When NOT to use:**
- **Long-term ICP definition** — use `ideal-customer-profile`. The ICP is the
  steady-state target; the beachhead may be narrower and temporary. This skill
  picks where to *start*, not where to *stay*.
- **Market sizing** — use `market-sizing` (pm-strategy). TAM/SAM/SOM for the
  beachhead is an *input* to this skill, not its output.
- **Full GTM strategy** — use `gtm-strategy`. The beachhead choice is one input
  into a broader GTM plan; it does not replace channel selection, messaging, or
  launch sequencing.

## Inputs
- **Required:** product description (what it does, for whom, against what status
  quo). If missing, ask before proceeding — the segment scoring depends entirely
  on what advantage the product brings.
- **Optional:** list of candidate segments the founder/PM is already considering;
  existing customer or interview data; known constraints (geography, sales motion,
  budget ceiling). If absent, the skill brainstorms candidates from first principles,
  but flags that they are hypothetical and need validation.

## Output Contract
The deliverable is a **beachhead segment brief** with these sections (see
`template.md`):

1. **Beachhead Definition** — one crisp statement: who they are, what acute pain
   they have, and where they are found.
2. **Why We Can Win Here** — pain severity (is it a hair-on-fire problem?), the
   product's 10x advantage over the status quo, and reachability (can we reach
   these buyers affordably and quickly?).
3. **Win Criteria** — three to five measurable signals that tell us we have
   dominated the beachhead and are ready to cross the chasm into the next segment.
4. **Next Segment** — the first bowling-pin move: which adjacent segment does
   beachhead dominance naturally unlock, and why?
5. **Risks** — the two or three biggest things that could invalidate this segment
   choice, each with a mitigation or early-warning indicator.

Format: prose + a brief candidate-segment comparison table (when ≥ 2 candidates
were evaluated). Length: ~1 page. Every claim about pain severity or winnability
is tied to evidence or explicitly labeled an assumption.

**GOOD (excerpt):**
> **Beachhead Definition:** Series-A SaaS founders in France (≤ 50 employees) who
> are filing VAT returns manually in a spreadsheet and spending 8+ hours/quarter
> on it. ~3,500 companies meet this profile today.
>
> **10x Advantage:** Our auto-reconciliation halves filing time versus the manual
> status quo and eliminates the most common VAT error class (missing intra-EU
> transactions). DocuSign and Pennylane do not cover this workflow.
>
> **Win Criterion 1:** ≥ 60% of reachable segment signed up or actively piloting
> within 18 months.

**BAD (excerpt):**
> "We'll target SMBs in Europe."
> — fails: no pain specificity, no stated advantage, no geographic or firmographic
> boundary that makes the segment winnable, and no win criteria.

## Process
1. **Clarify the product** — confirm what the product does and the key advantage
   it has over the current status quo. If unclear, ask.
2. **Enumerate candidates** — list 3–6 segment hypotheses (vertical × company-size
   × role combinations). Use the founder's existing candidates if provided; augment
   from first principles if not.
3. **Score each candidate** on four dimensions using the phuryn criteria:
   - *Burning pain* — does this segment experience the problem acutely and daily?
   - *Willingness to pay* — is there a clear budget and a compelling ROI?
   - *Winnability* — can we realistically capture 60–70% of this segment in 3–18
     months with current resources?
   - *Referral potential* — will customers recommend to adjacent segments, enabling
     the bowling-pin expansion?
4. **Apply Moore's concentration test** — the winning segment must be *small enough*
   to dominate with focused effort and *large enough* to fund the next expansion.
   Flag any segment that fails this test even if it scores well on the four dimensions.
5. **Select and justify** — pick the top candidate; write the Beachhead Definition
   and Why We Can Win Here sections grounded in the scoring.
6. **Define win criteria** — state 3–5 measurable signals (adoption rate, NPS,
   reference-customer count, payback period) that mark beachhead dominance.
7. **Map the next bowling pin** — identify the first adjacent segment that beachhead
   dominance unlocks; state the mechanism (shared persona, shared workflow,
   word-of-mouth path).
8. **Surface risks** — name the top 2–3 invalidation scenarios with early-warning
   indicators.
9. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The beachhead is defined with enough specificity (vertical, company size or
  persona, geography) that a sales rep could build a target list from it.
- [ ] The 10x advantage over the status quo is stated — not just "better", but
  *how* and *by how much*.
- [ ] At least two candidate segments were evaluated (even briefly) so the
  recommendation is a choice, not an assumption.
- [ ] Win criteria are **measurable** — each has a number and a time horizon, not
  just "strong adoption".
- [ ] The next segment (bowling pin) is identified with the mechanism that connects
  it to the beachhead.
- [ ] Every claim about pain or advantage is grounded in evidence or explicitly
  labeled an assumption requiring validation.
- [ ] If the output is written to a file, it follows `template.md` — all five
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `beachhead-segment-happy` (happy path) — B2B SaaS with clear beachhead options;
  skill picks the strongest and justifies it against the four criteria.
- `beachhead-segment-edge` (edge) — multiple apparently-equal segment options;
  skill must apply a tie-breaking framework rather than picking arbitrarily.
- `beachhead-segment-adversarial` (adversarial) — founder insists on going broad
  from day 1; skill must push back and redirect toward a narrower beachhead.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `ideal-customer-profile` — the long-run target customer definition; the beachhead
  may be a strict subset of the ICP.
- `gtm-strategy` — the beachhead segment choice is a foundational input to the
  full GTM strategy.
- `market-sizing` (pm-strategy) — TAM/SAM/SOM estimates for the beachhead inform
  the concentration test in Step 4 of this skill.

### External Frameworks
- Geoffrey Moore, *Crossing the Chasm* (1991, rev. 2014) — the canonical beachhead
  and bowling-pin expansion model this skill is built on.
- Bill Aulet, *Disciplined Entrepreneurship* (2013), Steps 3–7 — market
  segmentation, beachhead selection, and end-user profile for new ventures.
- Steve Blank, *The Four Steps to the Epiphany* — customer discovery and segment
  validation techniques that supply the evidence this skill requires.
