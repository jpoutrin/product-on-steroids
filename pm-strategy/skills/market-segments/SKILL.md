---
name: market-segments
description: >
  Define and prioritize customer segments by problem / job-to-be-done (not just
  demographics), score each on size, attractiveness, and reachability, and pick a
  first/beachhead segment. Use when segmenting a market, identifying a target
  audience, choosing where to focus first, or evaluating a new market to enter.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/market-segments/template.md
---

# Define & Prioritize Market Segments

## Purpose
Break a market into 3–5 distinct, non-overlapping customer segments defined by the
**problem / job-to-be-done** they share (not demographics alone), score each on
**size, attractiveness, and reachability**, and recommend a single **first/beachhead
segment** to focus on. Supports targeting, focus, and market-entry decisions by
turning a broad "everyone" market into a ranked, defensible short-list.

**When NOT to use:** computing TAM/SAM/SOM dollar figures (use `market-sizing` — this
skill *scopes* segments, it does not run the sizing math), building a single detailed
buyer persona (this operates one level up, across segments), or competitive teardown
(use `competitor-analysis`). This skill picks *who first*; it does not size the wallet
or build the plan.

## Inputs
- **Required:** the product/opportunity and its market boundaries — problem space,
  customer type (B2B/B2C), rough geography. If missing, ask for these three before
  segmenting; do not guess the scope.
- **Optional:** research/interview notes, customer or CRM data, existing personas
  (read and cite behavioral patterns and needs clusters), a preferred segmentation
  dimension, strategic constraints (channels you own, regions you can serve).

## Output Contract
The deliverable is a **segmentation & beachhead memo** with these sections (see
`template.md`):

1. **Segmentation Basis** — the market being split and the primary dimension(s) used
   (needs/JTBD-first, then behavioral/firmographic/demographic as modifiers); why
   these produce distinct, non-overlapping segments.
2. **Segment Profiles** — 3–5 segments, each with: a memorable name; the core
   **job-to-be-done** and desired outcome; the acute pain / trigger; who they are
   (behavioral + demo/firmo characteristics); and current alternatives/workarounds.
3. **Prioritization Matrix** — one table scoring every segment on **Size**,
   **Attractiveness** (pain intensity, willingness/ability to pay, growth, competitive
   whitespace), and **Reachability** (can you find and sell to them via a channel you
   have) on a stated scale, with a composite rank.
4. **Beachhead Recommendation** — the single first segment to win, *why* it beats the
   others (tie to matrix scores + fit + a foothold to expand from), and the top 1–2
   assumptions to validate before committing.

Format: prose + one scoring table. Length: ~1–2 pages. Segments must be
**distinct and non-overlapping**; every score carries a one-line justification, not a
bare number.

**GOOD (excerpt):**
> **Segment B — "Solo bookkeepers at 1–5-person agencies."** JTBD: *close the month
> without chasing receipts by email.* Trigger: quarterly VAT deadline. Alternative
> today: a shared spreadsheet + manual reminders.
> | Segment | Size | Attractiveness | Reachability | Composite |
> |---|---|---|---|---|
> | B | 3 (med) | 5 (acute pain, pays now) | 5 (reachable via accounting-tool marketplaces) | **13 — #1** |
>
> **Beachhead: Segment B** — smaller than A but the pain is acute, they already pay
> for point tools, and the accounting-marketplace channel is one we own. *Validate:
> that VAT-deadline urgency (not price) drives the switch.*

**BAD (excerpt):**
> "Our segments are 25–34-year-olds, 35–44-year-olds, and enterprises. All are big and
> attractive, so we'll target everyone."
> — fails: age buckets are demographics with no shared job, segments overlap and aren't
> distinct, scores are undifferentiated ("all big"), and there is no beachhead pick.

## Process
1. **Fix the scope** — confirm problem space, customer type, and geography; restate the
   market being segmented.
2. **Choose the basis** — lead with needs/JTBD; layer behavioral/firmographic/demographic
   as modifiers. Confirm the dimensions yield distinct, non-overlapping cuts.
3. **Define 3–5 segments** — name each and write its core JTBD, desired outcome, acute
   pain/trigger, characteristics, and current alternatives.
4. **Validate distinctness** — check no two segments share the same job + buyer; merge or
   re-cut if they overlap.
5. **Score** — rate each segment on Size, Attractiveness, and Reachability on a stated
   scale, one-line justification per cell; compute a composite rank.
6. **Pick the beachhead** — recommend one first segment, justify vs. the runners-up, and
   name the foothold it opens for expansion.
7. **Surface assumptions** — list the 1–2 riskiest beliefs behind the pick and how to
   validate them.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] 3–5 segments, each defined by a **job-to-be-done / problem** — not demographics alone.
- [ ] Segments are **distinct and non-overlapping** (no two share the same job + buyer).
- [ ] Every segment has a named JTBD, an acute pain/trigger, and its current alternative.
- [ ] All segments are scored on **Size, Attractiveness, and Reachability** with a stated
      scale and a one-line justification per score — no bare numbers.
- [ ] A **single beachhead** is recommended and justified against the runners-up, tied to
      the matrix and to an expansion foothold.
- [ ] The 1–2 riskiest assumptions behind the pick are named with a validation step.
- [ ] Dollar sizing is deferred to `market-sizing` — this memo scopes, it does not size.
- [ ] If written to a file, it follows `template.md` — all 4 sections present, in order,
      headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `market-segments-happy` (happy path) — B2B tool with interview notes; full JTBD-based
  segmentation, scoring, and a defensible beachhead.
- `market-segments-edge` (edge) — sparse-data consumer market where segments must be
  inferred from behavior and distinctness is hard to hold.
- `market-segments-adversarial` (adversarial) — a demographics-only, "target everyone"
  ask the skill must re-cut into JTBD segments and force a single beachhead.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — computes TAM/SAM/SOM dollar figures for the segments this skill
  defines; run it after picking the beachhead to size the wallet. This skill scopes,
  that one sizes.
- `competitor-analysis` — the "competitive whitespace" input to the Attractiveness score
  comes from a competitive read of each segment.

### External Frameworks
- Clayton Christensen, *Jobs to Be Done* — segment by the job customers hire the product
  for, not by demographic attribute; the needs-first basis this skill leads with.
- Geoffrey Moore, *Crossing the Chasm* — the beachhead / bowling-pin logic of winning one
  focused segment first and expanding from that foothold.
- Bill Aulet, *Disciplined Entrepreneurship*, Steps 1 & 3 — market segmentation and
  selecting a single beachhead market as the discipline behind the prioritization here.
