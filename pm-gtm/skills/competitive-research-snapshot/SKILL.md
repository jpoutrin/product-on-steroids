---
name: competitive-research-snapshot
description: >
  Produce a fast, broad competitive landscape scan across 3-7 competitors with
  a structured comparison table and differentiation summary. Use when preparing
  for a launch, refreshing competitive intel before a planning cycle, briefing
  a new PM on the landscape, or quickly mapping who plays where in a market.
version: 0.1.0
type: component
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/competitive-research-snapshot/template.md
---

# Competitive Research Snapshot

## Purpose
Produce a fast, structured scan of the competitive landscape: who the players
are, how they are positioned, how they differ on key dimensions (pricing,
target segment, GTM motion, key features, strengths, weaknesses), and where
the whitespace lies for your product. The deliverable is a **comparison table
+ where-to-win summary** that a PM can digest in under 10 minutes and act on.

This is a **snapshot** — intentionally broad and regularly refreshable, not a
deep analytical teardown of any single competitor.

**When NOT to use:**
- You need a deep one-competitor profile for a sales battle: use
  `competitive-battlecard` instead.
- You are doing a strategic competitive deep-dive to inform product positioning
  over a multi-year horizon: use `competitor-analysis` (pm-strategy).
- You need to size the overall market opportunity: use `market-sizing`.
- You have fewer than 2 competitors/substitutes to compare — a snapshot
  table adds no value; write a single positioning statement instead.

## Inputs
- **Required:** product or category to analyze — the name and a one-sentence
  description of what it does. Without this, ask before proceeding.
- **Required:** list of competitors (or "discover them") — if the user says
  "discover," surface 3-7 players from known market signals; if they supply a
  list, use it as-is (flag any that fall outside the category).
- **Optional:** comparison dimensions — default set is: Pricing model, Target
  segment, GTM motion, Key features (top 3), Positioning tagline/promise,
  Strengths, Weaknesses. User may add or swap dimensions.
- **Optional:** research sources — links, documents, prior research the user
  can share. Cite whatever is provided; label uncited cells as "(estimated)" or
  "(inferred from public signals)".
- **Optional:** time horizon — default is "current snapshot"; user may request
  a forward-looking view (flag that it will be more speculative).

## Output Contract
The deliverable is a **competitive research snapshot** structured as (see
`template.md`):

1. **Competitive Landscape Overview** — one paragraph (3-6 sentences) naming
   the market, the players covered, and the key competitive dynamics at play.
   State how many direct vs. indirect competitors are included and why.
2. **Comparison Table** — a Markdown table with competitors as rows and
   dimensions as columns. Minimum dimensions: Pricing Model, Target Segment,
   GTM Motion, Key Features, Positioning Promise, Strengths, Weaknesses.
   Each cell is concise (≤ 15 words or a short list). Empty cells are
   "—"; uncertain cells are marked "(est.)".
3. **Where to Win** — 3-5 bullet points identifying differentiation
   opportunities: gaps competitors leave unaddressed, segments underserved,
   and dimensions where your product can lead. Each bullet names the opportunity
   and the supporting evidence from the table.
4. **Gaps & Risks** — 2-4 bullets on blind spots in the snapshot (missing
   data, indirect substitutes not covered, dimensions not compared) and market
   risks (a competitor about to close a gap, pricing pressure, etc.).

Format: prose overview + one Markdown table + two bulleted sections. Target
length: 1-2 pages. Every competitive claim is either sourced or labeled
"(est.)" — never presented as certain when inferred.

**GOOD (excerpt):**
> **Where to Win:**
> - **Upmarket SMB gap:** Competitors A and B target VSBs (<10 seats) or
>   Enterprise (>500). The 50-250-seat SMB band has no specialist — your
>   per-seat pricing and self-serve onboarding fit it directly.
> - **Transparent pricing:** 4 of 5 competitors use "contact sales" pricing.
>   Public, instant pricing is a differentiator for PLG motion. (Source: each
>   competitor's pricing page, checked 2025-06)

**BAD (excerpt):**
> "We are better than Competitor X in every way."
> — fails: no evidence, no table backing, not a differentiation opportunity,
> reads as advocacy not analysis.

## Process
1. **Confirm scope** — verify the product/category and the competitor list
   (or discover 3-7 players). If the user supplied fewer than 2 competitors,
   ask whether to include indirect substitutes before continuing.
2. **Set dimensions** — use the default set unless the user specifies
   alternatives. Document any swaps.
3. **Gather intel** — for each competitor, populate each dimension from
   provided sources, public signals (pricing pages, G2/Capterra, press
   releases, LinkedIn), or reasonable inference. Label every inferred cell
   "(est.)".
4. **Identify indirect competitors** — if the category is new or the direct
   list is thin (<3), expand to include substitutes (spreadsheets, manual
   processes, adjacent tools). Flag them as "indirect."
5. **Draft the Comparison Table** — one row per competitor, columns per
   dimensions. Keep cells tight; move explanations to footnotes or prose.
6. **Write the Landscape Overview** — 3-6 sentences framing the market
   structure, competitive dynamics, and scope of this snapshot.
7. **Derive Where to Win** — scan the table for gaps, whitespace, underserved
   segments, and dimensions where your product can lead. Write 3-5 bullets
   grounded in the table.
8. **Flag Gaps & Risks** — note missing data, uncovered substitutes, and
   forward-looking risks. Be honest about what the snapshot cannot see.
9. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The snapshot covers **3-7 competitors** (direct and/or indirect);
  if fewer are available, the Gaps & Risks section explains why and names
  what substitute categories were considered.
- [ ] The **Comparison Table** is present with at least the 7 default
  dimensions (or documented substitutes) and one row per competitor.
- [ ] Every cell is **filled, "—", or labeled "(est.)"** — no blank cells
  and no unsupported assertions presented as facts.
- [ ] **Where to Win** has 3-5 bullets, each tied to evidence in the table
  (not generic claims).
- [ ] The snapshot is **clearly distinct** from a single-competitor battlecard:
  it is broad and cross-cutting, not a deep teardown of one player.
- [ ] **Indirect competitors** are flagged as such if included; the scope
  decision is stated in the Overview.
- [ ] If written to a file, it follows `template.md` — all 4 sections present
  in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `competitive-research-snapshot-happy` (happy path) — SaaS market with 5
  known direct competitors and good research input provided.
- `competitive-research-snapshot-edge` (edge) — new category with no direct
  competitors; skill must surface and classify indirect substitutes.
- `competitive-research-snapshot-adversarial` (adversarial) — user asks for
  a snapshot that validates a pre-made conclusion favoring a specific
  competitor; skill must stay neutral and evidence-grounded.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `competitive-battlecard` — one-competitor deep profile for sales; the
  snapshot's table rows are a fast input to individual battlecards.
- `competitor-analysis` (pm-strategy) — deep strategic analysis of competitive
  position over time; uses snapshot data as a starting point.
- `market-sizing` — bounds the opportunity the landscape sits in; the snapshot
  segments data can feed SAM scoping.
- `beachhead-segment` — the "Where to Win" opportunities narrow directly into
  first-segment selection.

### External Frameworks
- Porter's Five Forces — structural lens for Gaps & Risks (threat of new
  entrants, substitutes, buyer power); informs which blind spots to flag.
- Geoffrey Moore, *Crossing the Chasm* — positioning and segment targeting
  concepts that underpin the "Where to Win" analysis for technology products.
- [G2 / Capterra category pages](https://www.g2.com) — primary public source
  for user-reported competitor strengths, weaknesses, and segment fit.
