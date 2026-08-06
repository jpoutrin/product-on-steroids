---
name: pestle-analysis
description: >
  Run a point-in-time PESTLE macro-environment scan (Political, Economic,
  Social, Technological, Legal, Environmental), each factor rated on impact and
  likelihood with a "so what for our product" implication. Use when assessing
  the macro environment, evaluating market-entry risk, scoping external factors
  for a strategy, or surfacing regulatory and macro blind spots.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/pestle-analysis/template.md
---

# PESTLE Macro-Environment Analysis

## Purpose
Produce a **point-in-time** scan of the macro-environmental forces acting on a
product, market, or entry decision — organized across the six PESTLE lenses
(Political, Economic, Social, Technological, Legal, Environmental). Every factor
carries an **impact** rating, a **likelihood** rating, and a one-line **"so what
for our product"** implication, so the reader sees not just *what is happening
out there* but *what to do about it*. Supports market-entry go/no-go, strategy
scoping, and regulatory-roadmap planning by surfacing external blind spots
early.

**When NOT to use:** ongoing tracking of how these forces *change over time* —
that is `pestel-delta-monitor`, the recurring companion to this one-time scan.
Also not for internal strengths/weaknesses (use a SWOT), competitive teardown
(use `competitor-analysis`), or sizing the opportunity (use `market-sizing`).
PESTLE frames the *macro* backdrop; it does not pick the plan or size the prize.

## Inputs
- **Required:** the product/business, the target **market or geography**, and
  the **industry/sector**. If any of the three is missing, ask for it before
  scanning — PESTLE factors are meaningless without geographic and sector
  context (a legal factor in the EU differs from one in the US).
- **Optional:** the strategic question driving the scan (market entry vs. annual
  refresh vs. risk review — default: strategy scoping), known regulatory or
  market changes to weight, analyst reports or internal data (read and cite
  them), a time anchor (default: "as of today").

## Output Contract
The deliverable is a **PESTLE scan** with these sections (see `template.md`):

1. **Scope & As-Of Date** — product/business, market & geography, sector, the
   question driving the scan, and the date the snapshot reflects.
2. **Six factor tables** — one per lens (Political, Economic, Social,
   Technological, Legal, Environmental). Each row = a factor, its **Impact**
   (High/Med/Low), its **Likelihood** (High/Med/Low), and a **"So what for our
   product"** implication. 3–5 factors per lens.
3. **Priority factors** — the High-impact × High/Med-likelihood factors pulled
   across all six lenses, each tagged Opportunity / Threat / Compliance and
   given a strategic response.
4. **Assumptions & watch-list** — numbered assumptions/unknowns with confidence
   levels, plus the leading indicators to hand off to `pestel-delta-monitor`.

Format: prose scope note + six tables + a priority list. Length: ~1–2 pages.
Every factor is either **cited** or clearly **labeled an estimate/assumption** —
and every factor has a stated implication (no bare observations).

**GOOD (excerpt):**
> **Legal — GDPR enforcement tightening (Impact: High · Likelihood: High):**
> DPAs issued €1.2B in fines in 2024 (Source X). *So what:* our EU consent flow
> must ship before launch, adding ~3 dev-weeks — a hard gate, not a nice-to-have.
> → *Priority: Compliance.*

**BAD (excerpt):**
> "Political: there is some political uncertainty. Economic: the economy matters.
> Technological: AI is a big trend."
> — fails: vague, no impact/likelihood ratings, no geography, and no "so what"
> implication — an untriaged word-cloud, not a scan.

## Process
1. **Fix scope** — confirm product, market/geography, sector, driving question,
   and as-of date. Ask for any missing required input before proceeding.
2. **Scan each lens** — for Political, Economic, Social, Technological, Legal,
   Environmental in turn, identify 3–5 relevant factors; cite or label each.
3. **Rate each factor** — assign Impact (H/M/L) and Likelihood (H/M/L) from the
   product's point of view, not in the abstract.
4. **Write the "so what"** — for every factor, state the concrete implication
   for *this* product; drop factors with no plausible implication.
5. **Extract priority factors** — pull the High-impact × High/Med-likelihood
   rows across all lenses; tag each Opportunity / Threat / Compliance and give a
   strategic response.
6. **Log assumptions & watch-list** — number unknowns with confidence levels and
   name the leading indicators to monitor over time.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] **All six** lenses are present, each with **3–5 factors** (none padded, none skipped).
- [ ] Every factor carries **both** an Impact and a Likelihood rating (H/M/L).
- [ ] Every factor has a **"so what for our product"** implication — no bare observations.
- [ ] Ratings are made **from the product's viewpoint** in the stated geography/sector, not generic.
- [ ] Every factor is **cited** or clearly **labeled an estimate/assumption**.
- [ ] Priority factors are the High-impact rows, each tagged **Opportunity / Threat / Compliance** with a response.
- [ ] Assumptions are **numbered** with confidence levels; a watch-list for `pestel-delta-monitor` is included.
- [ ] This is framed as a **point-in-time snapshot** (as-of date stated), not a change-over-time tracker.
- [ ] If written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `pestle-analysis-happy` (happy path) — a scoped EU market-entry scan with enough context to rate all six lenses and extract priorities.
- `pestle-analysis-edge` (edge) — a sparse-context ask where the skill must elicit missing geography/sector before scanning and flag low-confidence factors.
- `pestle-analysis-adversarial` (adversarial) — a vague "just list PESTLE factors" ask the skill must refuse to answer as an untriaged word-cloud, forcing ratings and implications.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `pestel-delta-monitor` — the recurring companion that tracks how these six forces *change over time*; this scan sets its baseline and hands off the watch-list.
- `market-sizing` — sizes the opportunity this scan frames; the two run side by side in an entry decision.
- `competitor-analysis` — micro/competitive teardown that complements this macro scan (PESTLE vs. Porter/SWOT altitude).

### External Frameworks
- Francis Aguilar, *Scanning the Business Environment* (1967) — origin of the ETPS/PEST environmental-scanning discipline this skill formalizes.
- Gerry Johnson, Kevan Scholes & Richard Whittington, *Exploring Corporate Strategy* — the PESTEL variant and the impact × likelihood prioritization used here.
- [Product Compass — The Product Frameworks Compendium](https://www.productcompass.pm/p/the-product-frameworks-compendium) — PESTLE as one of the macro-environment strategy frameworks and its complementarity with SWOT.
