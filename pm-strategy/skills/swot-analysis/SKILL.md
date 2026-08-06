---
name: swot-analysis
description: >
  Run a strategic SWOT that pushes past a 4-quadrant list into a TOWS
  "so what → action" synthesis, with each item evidenced and disciplined as
  internal (Strength/Weakness) vs external (Opportunity/Threat). Use when doing
  a strategic assessment, evaluating a product or business position, prepping a
  planning offsite, or turning a competitive read into prioritized moves.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/swot-analysis/template.md
---

# SWOT → TOWS Strategic Assessment

## Purpose
Produce a decision-useful strategic assessment of a product or business: the four
SWOT quadrants — **Strengths** and **Weaknesses** (internal, things we control)
and **Opportunities** and **Threats** (external, things we don't) — each backed by
evidence, then *cross-referenced* into a TOWS synthesis that turns the grid into
3–5 prioritized, owned strategic moves. The value is in the "so what," not the list.

**When NOT to use:** sizing the opportunity in numbers (use `market-sizing`), a
deep feature-by-feature competitive teardown (use `competitor-analysis`), or
choosing the first segment to attack (use `beachhead-segment`). SWOT frames the
strategic position; it does not quantify the market or pick the plan on its own.

## Inputs
- **Required:** the subject and its strategic frame — the product/business being
  assessed, and *against what* (a named competitor set, a market, or a specific
  decision). If missing, ask "SWOT of what, relative to whom or what?" before
  starting; an unframed SWOT drifts into generic truisms.
- **Optional:** company capabilities/resources/constraints, competitive landscape,
  market trends, customer feedback or usage data (read and cite it), and the
  decision on the table (build / defend / pivot / exit). Absent these, state the
  assumptions you are reasoning from.

## Output Contract
The deliverable is a **SWOT → TOWS assessment** with these sections (see
`template.md`):

1. **Frame** — the subject, the reference point (vs whom/what), and the decision it informs. One or two sentences.
2. **SWOT grid** — 4–7 items per quadrant. Each item is one line: a claim plus its **evidence** (data point, source, or observation) — never a bare adjective. Internal/external discipline is strict: a Strength/Weakness is something the org controls; an Opportunity/Threat exists in the market regardless of us.
3. **TOWS synthesis** — the cross-referenced strategy pairs: **SO** (use strengths to seize opportunities), **ST** (use strengths to blunt threats), **WO** (fix weaknesses to unlock opportunities), **WT** (limit weaknesses exposed to threats). At least one pairing per cell that has a real match; each names the two items it connects.
4. **Prioritized moves** — 3–5 recommendations drawn from the TOWS pairs, each tagged with its posture (Build / Defend / Pivot / Exit), an owner, and a metric to track.
5. **Key uncertainties** — the 2–4 items whose truth most changes the strategy, each with how to validate it.

Format: prose frame + a 2×2 grid (or four labeled lists) + TOWS pairs + a moves
table. Length: ~1–2 pages. Every SWOT item carries evidence or is flagged an
assumption; every move traces to a TOWS pair.

**GOOD (excerpt):**
> **S2:** Onboarding completion 82% vs. industry ~55% (internal analytics, Q2) — a controllable strength.
> **O1:** New EU e-invoicing mandate takes effect 2026 (external, applies market-wide).
> **SO move (S2 × O1):** Position frictionless onboarding as the fastest path to compliance → *Build*, owner: PMM, metric: mandate-driven signups.

**BAD (excerpt):**
> Strengths: "Great team, good product." Opportunities: "AI is growing."
> — fails: bare adjectives with no evidence, "great team" is not framed against anyone, no TOWS cross-reference, and no action falls out of the grid.

## Process
1. **Frame it** — pin the subject, the reference point (vs whom/what), and the decision. Refuse to proceed on an unframed request.
2. **Strengths** — list 4–7 internal advantages, each with evidence; confirm each is org-controlled.
3. **Weaknesses** — list 4–7 internal gaps, each with evidence; be honest, focus on addressable ones.
4. **Opportunities** — list 4–7 external openings (trends, gaps, competitor stumbles); confirm each exists independent of us.
5. **Threats** — list 4–7 external risks, each assessed for probability/impact.
6. **Audit the axes** — recheck every item for the internal-vs-external test; move any misfiled item.
7. **Cross-reference (TOWS)** — generate SO / ST / WO / WT pairs, naming the two items each connects.
8. **Prioritize moves** — distill 3–5 recommendations from the pairs; tag posture, owner, metric.
9. **Flag uncertainties** — name the 2–4 assumptions that most swing the strategy and how to test them.
10. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The assessment is **framed** — subject, reference point (vs whom/what), and the decision are stated up front.
- [ ] Every SWOT item carries **evidence** (data, source, or observation) or is explicitly flagged an assumption — no bare adjectives.
- [ ] **Internal vs external discipline** holds: every S/W is org-controlled; every O/T exists in the market regardless of us.
- [ ] A **TOWS synthesis** is present with SO / ST / WO / WT pairs, each naming the two items it connects — not just four restated lists.
- [ ] **3–5 prioritized moves**, each traceable to a TOWS pair and tagged with posture (Build/Defend/Pivot/Exit), owner, and metric.
- [ ] The most strategy-swinging **uncertainties** are named with a way to validate each.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `swot-analysis-happy` (happy path) — a well-framed B2B product SWOT that must yield evidenced quadrants and TOWS-derived moves.
- `swot-analysis-edge` (edge) — misfiled/ambiguous factors the skill must sort correctly across the internal/external axis.
- `swot-analysis-adversarial` (adversarial) — an unframed "just do a SWOT" ask with bare vibes that the skill must frame and evidence rather than echo.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — quantifies the opportunity a SWOT identifies qualitatively; feed its TAM/SAM into the O and SO reasoning.
- `competitor-analysis` — supplies the evidenced competitive read that grounds Strengths, Weaknesses, and Threats against a named rival set.
- `beachhead-segment` — consumes the prioritized SO/Build moves when choosing where to attack first.

### External Frameworks
- Heinz Weihrich, "The TOWS Matrix — A Tool for Situational Analysis" (*Long Range Planning*, 1982) — the canonical SO/ST/WO/WT cross-referencing this skill uses to turn a static SWOT into strategy.
- Albert Humphrey / Stanford SRI — origin of the SWOT quadrants and the internal-vs-external framing.
- Michael Porter, *Competitive Strategy* (1980) — five-forces lens for sourcing defensible external Opportunities and Threats.
