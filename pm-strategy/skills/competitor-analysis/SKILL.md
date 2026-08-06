---
name: competitor-analysis
description: >
  Map the competitive landscape into a brief — profile direct competitors on
  positioning, strengths, weaknesses, and pricing, then surface concrete
  differentiation opportunities. Use when doing competitive research, preparing a
  competitive brief, building a battlecard, or hunting for a differentiation wedge.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/competitor-analysis/template.md
---

# Competitive Analysis Brief

## Purpose
Produce a decision-grade competitive brief for a product or opportunity: define
the competitive set, profile each direct competitor on positioning, strengths,
weaknesses, and pricing, then convert the pattern of gaps into a short list of
**differentiation opportunities** and a positioning recommendation. Every claim is
either cited or flagged as an inference, so a reader can trust — and challenge —
the read of the landscape.

**When NOT to use:** sizing the opportunity in dollars (use `market-sizing`),
picking a first target segment (use `beachhead-segment`), win/loss analysis of
your own deals, or a full go-to-market plan. This skill maps rivals and finds the
wedge; it does not size the market or write the plan.

## Inputs
- **Required:** the product/opportunity under analysis and its market boundaries —
  problem space, customer type (B2B/B2C, segment), geography. If missing, ask for
  these three before profiling; do not guess the scope, or the competitive set
  will be wrong.
- **Optional:** a named list of competitors to include (otherwise identify them via
  research), any supplied competitor data (pricing sheets, feature matrices,
  review exports, analyst reports — read and cite them directly), the number of
  competitors to profile (default 5 direct), and which axis matters most for
  differentiation (features / price / segment / channel).

## Output Contract
The deliverable is a **competitive analysis brief** with these sections (see
`template.md`):

1. **Market & Competitive Set** — one-paragraph market definition, then the direct
   competitors chosen (default 5) tagged leader / challenger / niche, plus notable
   indirect or adjacent alternatives named and set aside.
2. **Competitor Profiles** — one profile per competitor, each covering: positioning
   & target segment; core strengths (2–4); weaknesses & gaps (2–4); pricing model
   & price point; and the threat it poses. Every load-bearing claim is cited
   (source) or marked `(inference)`.
3. **Comparison Matrix** — a table with competitors as rows and the axes that
   matter (positioning, price, key strength, key gap) as columns, for at-a-glance
   contrast.
4. **Differentiation Opportunities** — 3–5 specific, defensible openings drawn from
   the *pattern of gaps* across the set (unmet need, underserved segment,
   price/UX/channel gap), each tied to the evidence that supports it.
5. **Positioning Recommendation** — the recommended competitive positioning, the
   1–3 differentiators to lead with, segments to target or avoid, and the top
   competitive threats to monitor over the next 12–18 months.

Format: prose + one comparison matrix. Length: ~1–2 pages. Direct competitors are
distinguished from adjacent alternatives; no strength/weakness is asserted without
a source or an explicit `(inference)` tag.

**GOOD (excerpt):**
> **DocuSign** — *leader; enterprise + mid-market.* Strengths: deepest integration
> catalog (350+), brand trust in regulated buying (Source: G2, 2025). Gaps: SMB
> pricing seen as steep — €10/user/mo entry vs €0 freemium rivals (Source: pricing
> page, Jan 2026); onboarding rated slow by SMB reviewers *(inference from 12 G2
> reviews)*. Threat: incumbency + procurement lock-in.
> **Opportunity 2:** No leader offers a true freemium tier for <5-seat SMBs — an
> underserved segment DocuSign and Adobe both price out.

**BAD (excerpt):**
> "DocuSign is the market leader and very popular. It's expensive. We can beat them
> by being better and cheaper."
> — fails: no positioning tag, no cited strengths/gaps, "better" is not a
> differentiator, no evidence, opportunity is a slogan not a gap in the set.

## Process
1. **Scope the market** — fix problem space, customer type, and geography; state
   what counts as a *direct* competitor here vs an adjacent alternative.
2. **Assemble the set** — identify (or take the given) direct competitors, default
   5; tag each leader / challenger / niche; name notable indirect players and set
   them aside with a reason.
3. **Gather intelligence** — for each competitor, research positioning, features,
   pricing, and reviews; read any supplied data directly; cite every source and
   mark unsourced reads `(inference)`.
4. **Profile each competitor** — write positioning, 2–4 strengths, 2–4
   weaknesses/gaps, pricing model & point, and the threat it poses.
5. **Build the comparison matrix** — one row per competitor across the axes that
   matter, so contrasts are legible at a glance.
6. **Find differentiation opportunities** — read *across* the profiles for the
   pattern of shared gaps; extract 3–5 specific openings, each tied to evidence.
7. **Recommend positioning** — the wedge to own, differentiators to lead with,
   segments to target/avoid, and 12–18-month threats to monitor.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The competitive set is **scoped** — direct competitors are distinguished from adjacent alternatives, each tagged leader / challenger / niche.
- [ ] Each competitor has **both** strengths (2–4) **and** weaknesses/gaps (2–4) — no profile is all-praise or all-criticism.
- [ ] Every load-bearing claim is **cited** or explicitly marked `(inference)` — no unsupported assertions.
- [ ] Pricing model **and** a concrete price point are given for each competitor (or the gap is flagged as unknown).
- [ ] There is a **comparison matrix** letting a reader contrast the set at a glance.
- [ ] Differentiation opportunities (3–5) are **specific and evidence-tied**, drawn from the pattern of gaps across the set — not generic "be better/cheaper".
- [ ] The positioning recommendation names **1–3 differentiators** to lead with and the threats to monitor.
- [ ] If the brief is written to a file, it follows `template.md` — all 5 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `competitor-analysis-happy` (happy path) — a B2B SaaS category with named rivals and supplied pricing; expects full profiles, matrix, and gap-derived opportunities.
- `competitor-analysis-edge` (edge) — a thin-data / emerging space where much is unknown; the skill must mark inferences, flag unknowns, and still find a wedge.
- `competitor-analysis-adversarial` (adversarial) — a vague, unscoped ask that lists a giant as the only "competitor"; the skill must scope the market and refuse a one-competitor, all-praise read.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — sizes the opportunity; consumes this brief's read of competitive position to set a defensible SOM fraction.
- `beachhead-segment` — picks the first target segment; the underserved-segment opportunities surfaced here feed that choice.

### External Frameworks
- Michael Porter, *Competitive Strategy* (1980) — Five Forces and the discipline of positioning against rivals rather than an abstract "better product".
- W. Chan Kim & Renée Mauborgne, *Blue Ocean Strategy* — the strategy canvas / value-curve lens behind reading *across* the competitive set for uncontested gaps.
- April Dunford, *Obviously Awesome* — positioning against the competitive alternatives customers actually consider, the frame for the recommendation section.
