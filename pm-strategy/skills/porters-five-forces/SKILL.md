---
name: porters-five-forces
description: >
  Assess the structural attractiveness of an industry with Porter's Five Forces
  — competitive rivalry, threat of new entrants, threat of substitutes, buyer
  power, and supplier power — rating each force Low/Med/High with evidence, then
  reaching an overall attractiveness verdict and strategic implications. Use when
  analyzing industry structure, evaluating market attractiveness before entry,
  assessing where industry profitability leaks, or stress-testing a strategy
  against competitive forces.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/porters-five-forces/template.md
---

# Porter's Five Forces (Industry Attractiveness)

## Purpose
Produce a structured read on **how attractive an industry is to compete in** by
rating the five forces that determine long-run profitability — competitive
rivalry, threat of new entrants, threat of substitutes, buyer power, and supplier
power. Each force is rated **Low / Med / High** with concrete evidence and a
trend (strengthening/weakening), rolling up to an overall attractiveness verdict
and the strategic implications for positioning. Supports market-entry go/no-go,
where-to-play choices, and stress-testing a strategy against structural forces.

**When NOT to use:** a rival-by-rival teardown of named competitors (use
`competitor-analysis` — this skill is about *industry structure*, not individual
firms), macro-environment scanning (use a PESTLE skill), sizing the opportunity
(use `market-sizing`), or an internal SWOT. Five Forces judges the *board*, not
the *players* or the *pot*.

## Inputs
- **Required:** the **industry/market definition** — the product-or-service
  category, customer type (B2B/B2C, segment), and geographic scope. If missing,
  ask for these three before analyzing; a force rating for an undefined industry
  is meaningless (chocolate is a different game from artisanal chocolate in the EU).
- **Optional:** known competitors and their relative size/share, supplier and
  customer landscape, candidate substitutes, entry-barrier facts (capital, IP,
  regulation, scale), and the analysis vantage point (a specific incumbent vs. a
  would-be entrant — attractiveness is position-dependent). Read and cite any
  analyst reports or internal data provided. Default vantage point: a new/typical
  entrant.

## Output Contract
The deliverable is an **industry-attractiveness brief** with these sections (see
`template.md`):

1. **Industry Definition & Vantage Point** — the category, customer type, geography, and whose lens (entrant vs. named incumbent).
2. **The Five Forces** — one subsection per force (Rivalry, New Entrants, Substitutes, Buyer Power, Supplier Power). Each states a **rating (Low/Med/High)**, a **trend** (↑ strengthening / ↓ weakening / → stable), 2–4 bullets of **evidence** driving the rating, and the **profitability implication**.
3. **Force Summary Table** — five rows: force · rating · trend · one-line driver.
4. **Overall Attractiveness Verdict** — Attractive / Moderate / Unattractive, justified by which forces dominate. High-force pressure = less attractive; state it, don't just average.
5. **Strategic Implications** — the 2–3 highest-pressure forces prioritized, each with a concrete response (reduce a strong force / exploit a weak one) and any positioning opportunity.

Format: prose + one summary table. Length: ~1–2 pages. Every rating is backed by
**evidence**, not asserted; the verdict follows from the ratings, not a hand-wave.

**GOOD (excerpt):**
> **Threat of New Entrants — High ↑.** Cloud infra rents scale that once had to be
> built; no proprietary IP moat; two funded startups launched in 2025. *Implication:*
> margins will be competed down as entrants chase the same mid-market buyer.
>
> **Verdict: Moderate-to-Unattractive.** Low switching costs (High buyer power) and
> easy entry are the two dominant forces; supplier power is Low and does not offset them.

**BAD (excerpt):**
> "Rivalry is high, suppliers are medium, entrants are low. Overall the industry
> looks pretty good."
> — fails: no evidence behind any rating, no trend, and the verdict contradicts the
> ratings (a High-rivalry industry is not "pretty good") — it averaged instead of reasoning.

## Process
1. **Define the industry & vantage point** — fix category, customer type, geography, and whose lens; refuse to rate an undefined industry.
2. **Rate Competitive Rivalry** — concentration, growth, differentiation, fixed/exit costs → Low/Med/High + trend + evidence.
3. **Rate Threat of New Entrants** — barriers (capital, IP, scale, network effects, regulation), incumbent retaliation → rating + trend + evidence.
4. **Rate Threat of Substitutes** — existence, price-performance, and switching cost of alternatives that solve the same job → rating + trend + evidence.
5. **Rate Buyer Power** — concentration, switching costs, price sensitivity, backward-integration threat, information → rating + trend + evidence.
6. **Rate Supplier Power** — concentration, switching costs, input criticality, forward-integration threat → rating + trend + evidence.
7. **Roll up the verdict** — weigh the dominant (highest-pressure) forces, don't average; state Attractive/Moderate/Unattractive with the reasoning.
8. **Derive strategic implications** — prioritize the top 2–3 forces and give a concrete response for each; note positioning opportunities.
9. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] All **five** forces are rated **Low/Med/High** — none skipped or merged.
- [ ] Each rating carries **specific evidence** (not a bare adjective) and a **trend** (↑/↓/→).
- [ ] The industry is **defined** (category · customer type · geography) and the **vantage point** (entrant vs. named incumbent) is stated.
- [ ] The overall verdict **follows from the ratings** by weighing dominant forces — it is not a simple average and does not contradict them.
- [ ] Strategic implications prioritize the **highest-pressure** forces and give a **concrete** response for each.
- [ ] The analysis stays on **industry structure**, not a rival-by-rival teardown (that's `competitor-analysis`).
- [ ] If the output is written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `porters-five-forces-happy` (happy path) — a well-scoped B2B SaaS industry with enough context to rate all five forces and reach a defensible verdict.
- `porters-five-forces-edge` (edge) — a two-sided marketplace where buyer and supplier sides must be reasoned separately and network effects complicate the entrant/rivalry ratings.
- `porters-five-forces-adversarial` (adversarial) — a vague "is this industry good?" ask with no definition and pressure for a one-word answer the skill must scope and refuse to hand-wave.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `competitor-analysis` — rival-by-rival teardown of named firms; consumes the Rivalry and New-Entrants reads from this skill and drills into specific competitors.
- `market-sizing` — sizes the opportunity this skill judges the structure of; a High-attractiveness verdict is only worth acting on if the SAM/SOM justify it.

### External Frameworks
- Michael E. Porter, *Competitive Strategy* (1980), Ch. 1 — the canonical Five Forces model and the structural determinants of each force this skill rates.
- Michael E. Porter, "The Five Competitive Forces That Shape Strategy," *Harvard Business Review* (Jan 2008) — the updated treatment; the discipline of judging *industry* profitability structure rather than any single competitor.
