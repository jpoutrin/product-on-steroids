---
name: prioritize-assumptions
description: >
  Rank assumptions by impact × uncertainty to determine testing order and
  suggest validation experiments. Use when triaging a list of assumptions,
  deciding which to test first, or building a testing roadmap.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/prioritize-assumptions/template.md
---

# Prioritize Assumptions by Impact and Uncertainty

## Purpose
Triage a set of assumptions (from `identify-assumptions-new` or `identify-assumptions-existing`)
by ranking them against two dimensions: **impact** (how much the assumption affects the go/no-go
decision) and **uncertainty** (confidence level in the assumption). The output is a prioritized
assumption matrix with testing recommendations, guiding which assumptions to test first and how.
Supports sprint planning, experiment roadmaps, and resource allocation for validation.

**When NOT to use:** surfacing assumptions (use `identify-assumptions-new` or `identify-assumptions-existing`),
designing experiments after you've chosen which assumptions to test (use `brainstorm-experiments-new` or
`brainstorm-experiments-existing`), or building a full product roadmap (use domain-specific roadmap skills).
This skill prioritizes; it does not discover or test.

## Inputs
- **Required:** a list of assumptions (text, table, or exported list from identify-assumptions skills).
  Each assumption should include: (1) the assumption statement, (2) rough confidence level (high/medium/low or 1–10).
  If missing, ask the user to provide these before ranking.
- **Optional:** decision criteria (what makes an assumption "critical to validate?"), competitor or market
  context that shifts impact scoring, or desired testing timeline. If provided, read and incorporate.

## Output Contract
The deliverable is an **assumption prioritization matrix**, structured as:

1. **Priority Matrix** — a 2×2 grid (or ranked table) with impact (y-axis) vs. uncertainty (x-axis),
   placing each assumption in the appropriate quadrant.
2. **Testing Roadmap** — prioritized list of which assumptions to test first, second, etc., with rank,
   assumption, impact, uncertainty, and **recommended validation method** (experiment type, research, etc.).
3. **Quadrant Actions** — guidance for each quadrant:
   - **High Impact, Low Uncertainty** → proceed to implementation or defer (low risk, lower learning value).
   - **High Impact, High Uncertainty** → test immediately (high risk, critical to resolve).
   - **Low Impact, High Uncertainty** → test only if time permits (learning value moderate, risk tolerable).
   - **Low Impact, Low Uncertainty** → deprioritize (low risk, low learning value).
4. **Key Scoring Rationale** — a brief explanation of how impact and uncertainty were scored (e.g.,
   "Willingness to pay is high impact because it determines pricing strategy").

See `template.md` for the fill-in structure.

**GOOD (excerpt):**
> | Rank | Assumption | Impact | Uncertainty | Method |
> |------|-----------|--------|-------------|--------|
> | 1 | Mid-market SMBs will pay €50/mo for this tool | High | High | 5-customer pre-order test, 1 week |
> | 2 | Current pain point affects >30% of target segment | High | Medium | 50-customer survey, 2 weeks |
> | 3 | Mobile-first UI is required for adoption | Medium | High | Prototype A/B test with 100 users, 3 weeks |
>
> **Rationale:** Willingness to pay is ranked highest because it's a go/no-go gate and we've had no paid validation.
> Problem severity is ranked second (high impact but medium confidence from discovery interviews).

**BAD (excerpt):**
> | Assumption | Priority |
> | All customers want this | High |
> | UI should be clean | Medium |
>
> — fails because: no impact/uncertainty scoring columns (no method), assumptions are vague ("want" vs. "pay"),
> no validation method, no rationale for ranking order.

## Process
1. **Parse the assumption list** — extract each assumption and note the confidence level provided or inferred from context.
2. **Score impact** — for each assumption, assess: if this assumption proved false, would it kill the product/market/pricing?
   Rate as high/medium/low (or 7–10 / 4–6 / 1–3 on a scale).
3. **Score uncertainty** — assess: how confident are we in this assumption today? Rate as high/medium/low confidence
   (inverting to "low/medium/high uncertainty").
4. **Build the matrix** — plot assumptions on the 2×2 grid or table, sorted by priority (high impact × high uncertainty first).
5. **Recommend validation methods** — for top-priority (high impact, high uncertainty) assumptions, suggest a lean experiment type
   and rough effort/timeline (e.g., "concierge test, 1 week").
6. **Articulate quadrant actions** — briefly explain what to do with assumptions in each quadrant.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every assumption is scored on both **impact** and **uncertainty** (not just "priority").
- [ ] Assumptions are ranked by **impact × uncertainty** (high/high is top; low/low is bottom).
- [ ] At least the top 3–5 assumptions include a **recommended validation method** (experiment type, research method).
- [ ] Assumptions are distinct and testable (not vague like "people will like this").
- [ ] The matrix or table shows the **2×2 quadrant logic** (or explicit scoring if using a ranked table).
- [ ] A brief **rationale** explains the most critical assumption or the biggest uncertainty shift from discovery.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `identify-assumptions-new` — surface assumptions for a new product concept; feeds into this skill.
- `identify-assumptions-existing` — surface assumptions for an existing product; feeds into this skill.
- `brainstorm-experiments-new` — design lean experiments for top-priority assumptions from this skill.
- `brainstorm-experiments-existing` — design experiments for existing-product assumptions from this skill.

### External Frameworks
- Dan Olsen, *The Lean Product Playbook* (2015) — ICE scoring (Impact × Confidence × Ease) for prioritization.
- Alberto Savoia, *The Right It* (2019) — assumption mapping and prioritization for pretotyping.
- Ash Maurya, *Lean Product Playbook* (2014) — riskiest-assumption-first framework and testing roadmaps.
