---
name: prioritize-features
description: >
  Rank a backlog of feature ideas by impact, effort, risk, and strategic
  alignment (ICE/RICE + Opportunity Score), returning a scored table and a
  defensible top-5 with rationale and what was cut. Use when prioritizing a
  feature backlog, making scope or roadmap trade-off decisions, or ranking
  product ideas against an objective.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/prioritize-features/template.md
---

# Prioritize a Feature Backlog

## Purpose
Turn a raw list of feature ideas into a **ranked, scored shortlist** so the team
can commit to the highest-value work with a defensible rationale. Score every
candidate on Impact, Effort, Risk, and Strategic alignment against a stated
objective, then recommend the top 5 — and say explicitly what was deprioritized
and why. Supports roadmap planning, sprint/quarter scoping, and stakeholder
alignment on trade-offs.

**When NOT to use:** discovering *which problems* are worth solving (use a
discovery/opportunity skill — prioritize solutions only after the opportunity is
validated); sizing the market behind an idea (use `market-sizing`); or sequencing
already-committed work into a delivery plan (that is release planning, not
prioritization). This skill ranks candidates; it does not invent them or validate
demand.

## Inputs
- **Required:** the **product objective / success metric** the backlog serves, and
  the **list of candidate features**. If either is missing, ask for it before
  scoring — ranking without a stated objective produces arbitrary results. If the
  user attaches a spreadsheet, backlog, or opportunity assessment, read and score
  from it directly.
- **Optional:** scoring framework preference (ICE vs RICE — default ICE for small
  teams, RICE when reach varies widely across items); customer data (importance /
  satisfaction survey → Opportunity Score); effort estimates or T-shirt sizes;
  known dependencies or hard constraints (deadline, compliance, platform).

## Output Contract
The deliverable is a **prioritization brief** with these sections (see
`template.md`):

1. **Objective & method** — the objective/metric being optimized, the framework
   used (ICE or RICE), and the 1–10 scoring convention for each factor.
2. **Scoring table** — every candidate as a row, with a column per factor
   (Impact/Reach, Confidence, Ease/Effort, Strategic fit or Risk), a computed
   **score**, and a rank. Sorted by score descending.
3. **Top 5 recommendations** — ranked 1–5, each with a one-line rationale naming
   the factor(s) that carried it and the key trade-off accepted.
4. **Deprioritized & why** — the notable items cut, each with a one-line reason
   (low impact, high risk, blocked, off-strategy), so cuts are auditable.
5. **Assumptions & confidence** — the load-bearing scoring assumptions (esp. any
   low-confidence Impact/Reach guesses) and how to validate them.

Format: one scored table + prose. Length: ~1 page. Every rank traces to a score;
every score's factors are visible in the table — no unexplained ordering.

**GOOD (excerpt):**
> **Method:** RICE, optimizing *activation rate*. Reach = users/quarter, Confidence 0–100%, Effort in person-weeks.
>
> | # | Feature | Reach | Impact | Conf | Effort | RICE | Rank |
> |---|---------|------:|:------:|:----:|-------:|-----:|:---:|
> | A | Guided onboarding | 8k | 2.0 | 80% | 4 | **3200** | 1 |
> | B | SSO | 1.2k | 1.0 | 90% | 6 | 180 | 5 |
>
> **#1 Guided onboarding** — top RICE; directly moves activation (the objective). Trade-off: delays SSO, accepted because SSO reach is 6× smaller.
> *Assumption (low conf): 80% confidence on onboarding impact — validate with a 2-week A/B before full build.*

**BAD (excerpt):**
> "We should build onboarding, SSO, and dashboards next — those feel highest impact."
> — fails: no objective, no scores, no framework, no ranking math, nothing deprioritized, "feel" instead of evidence.

## Process
1. **Confirm the objective** — the metric/outcome the backlog serves; if absent, ask before scoring.
2. **Pick the framework** — ICE (default) or RICE (when reach varies widely); if customer importance/satisfaction data exists, derive an **Opportunity Score** = Importance × (1 − Satisfaction) to inform the Impact factor.
3. **Score each candidate** on Impact/Reach, Confidence, Ease/Effort, and Strategic fit/Risk, on a stated scale — reuse the same scale for every row.
4. **Compute & rank** — ICE = Impact × Confidence × Ease; RICE = (Reach × Impact × Confidence) / Effort. Sort descending; break ties with strategic fit.
5. **Select the top 5** — with a one-line rationale each, naming the deciding factor and the trade-off accepted.
6. **Record deprioritized items** — each with a one-line reason, so cuts are auditable.
7. **Surface assumptions** — flag low-confidence scores and name a validation step for the most uncertain ones.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **objective/metric** being optimized is stated up front — no ranking without it.
- [ ] The **scoring framework** (ICE or RICE) and its per-factor scale are named and applied **consistently** across all candidates.
- [ ] **Every candidate** appears as a row with visible factor scores and a computed score — no item ranked without a score.
- [ ] The **top 5** are ranked with a rationale that names the deciding factor(s) and the trade-off accepted.
- [ ] At least the notable **deprioritized** items are listed with a one-line reason.
- [ ] **Low-confidence** Impact/Reach scores are flagged with a validation step — guesses are labeled, not hidden.
- [ ] Ranking reflects the **stated objective**, not unstated preference — order traces to the numbers.
- [ ] If the brief is written to a file, it follows `template.md` — all 5 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `prioritize-features-happy` (happy path) — a clear objective plus RICE-scorable backlog; expects a full scored table and a defensible top 5.
- `prioritize-features-edge` (edge) — no effort estimates and sparse data; the skill must switch to ICE, elicit or T-shirt-size effort, and flag low-confidence scores.
- `prioritize-features-adversarial` (adversarial) — "just tell me what to build next" with no objective; the skill must refuse to rank until it establishes the objective/metric.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — sizes the opportunity behind a feature; feeds the Impact/Reach inputs this skill scores.
- `product-vision` — the vision/objective that this skill's "Strategic fit" factor and objective are measured against.

### External Frameworks
- Dan Olsen, *The Lean Product Playbook* — **Opportunity Score** = Importance × (1 − Satisfaction); prioritize validated problems, not solutions, and feed the result into the Impact factor.
- Sean Ellis / GrowthHackers — **ICE** (Impact × Confidence × Ease) for fast initiative scoring.
- Intercom — **RICE** (Reach × Impact × Confidence ÷ Effort), which adds Reach as a distinct factor for larger or higher-variance backlogs.
- Noriaki Kano — **Kano model** (must-be / performance / delighter) as a qualitative cross-check on which features merely satisfy vs. differentiate.
