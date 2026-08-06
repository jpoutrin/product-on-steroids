---
name: pre-mortem
description: >
  Identify risks by imagining a product has failed and working backward to surface
  real problems (Tigers), overblown concerns (Paper Tigers), and unspoken worries
  (Elephants). Classify risks by urgency and create mitigation plans. Use when
  preparing for launch, stress-testing a product plan, or determining what could
  go wrong.
version: 0.1.0
type: workflow
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/pre-mortem/template.md
---

# Pre-Mortem: Risk Analysis for Product Launch

## Purpose

Conduct a structured risk-identification exercise that forces critical thinking about what could go wrong before launch, when there's still time to act. By assuming failure and working backward, surface hidden concerns, separate legitimate threats from overblown worries, and create action plans to mitigate launch-blocking issues.

**When NOT to use:** retrospective analysis after launch (use a post-mortem or incident review), competitive teardowns (use `competitor-analysis`), or technical debt audits (use engineering-focused risk frameworks). Pre-mortem is forward-looking, before commitment.

## Inputs

- **Required:** the PRD or product plan — product description, target market, key assumptions, and timeline. If missing, ask for scope before proceeding.
- **Optional:** cross-functional context (engineering feasibility, go-to-market readiness, dependency map), competitive landscape, business model specifics.

## Output Contract

The deliverable is a **pre-mortem risk analysis** with these sections (see `template.md`):

1. **Tigers (Real Risks)** — risks with evidence that could derail the project, categorized as launch-blocking, fast-follow, or track.
2. **Paper Tigers (Overblown Concerns)** — valid surface concerns that are unlikely or overblown, with reasoning.
3. **Elephants (Unspoken Worries)** — uncertain, undiscussed assumptions that deserve investigation before launch.
4. **Action Plans for Launch-Blocking Tigers** — for each, include risk description, mitigation action, owner, and decision date.
5. **Validation Plan** — how to verify the most uncertain assumptions before launch.

Format: structured prose + summary tables. Length: 1–2 pages. Every risk is anchored to a specific failure mode or assumption, never vague.

**GOOD (excerpt):**
> **Tiger (Launch-Blocking):** Core onboarding flow untested at scale. We've validated with 50 users; enterprise deployment requires 1000+ concurrent users. **Mitigation:** Load-test staging with 2000 concurrent; resolve critical paths by launch-14. **Owner:** Engineering. **Due:** Launch-21.

**BAD (excerpt):**
> "Market might not want it." — too vague; no specific failure mode, no owner, no actionable mitigation.

## Process

1. **Read the PRD** — understand product, market, key assumptions, timeline, and dependencies.
2. **Assume Failure** — imagine the launch happened but failed: customers don't adopt, revenue misses, reputation takes a hit. What went wrong?
3. **Brainstorm Risks** — identify what went wrong, what was missed, what we were overconfident about. Aim for 12–15 raw risks.
4. **Categorize as Tiger / Paper Tiger / Elephant** — apply the definitions (real evidence, overblown, or uncertain).
5. **Classify Tigers by Urgency** — launch-blocking, fast-follow, or track.
6. **Create Mitigation Plans** — for each launch-blocking Tiger, write: risk, specific mitigation action, owner, due date.
7. **Map Validation** — for the most uncertain assumptions, name how to validate before launch.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar

Before returning, confirm:

- [ ] At least one Tiger is identified (if none, the analysis is incomplete; assume at least one real risk exists).
- [ ] Tigers are anchored to specific failure modes, not vague worries.
- [ ] Every launch-blocking Tiger has a named owner and a decision date.
- [ ] Paper Tigers include reasoning for why they're overblown (evidence, context, or data).
- [ ] Elephants are articulated clearly and include a suggested investigation approach.
- [ ] Mitigation actions are concrete and achievable before launch-blocking deadlines.
- [ ] If written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval

Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills

- `market-sizing` — TAM/SAM/SOM assumptions can become Elephants if not validated.
- `competitive-analysis` — competitive risk factors feed Tiger identification.
- `prd-structure` — PRD clarity determines pre-mortem quality; unclear PRDs yield vague risks.

### External Frameworks

- Gary Klein, *Pre-Mortem: The Best Way to Imagine Disaster and Plan to Avoid It* — foundational source on pre-mortem methodology, framing as prospective hindsight.
- Daniel Kahneman, *Thinking, Fast and Slow* (2011), "The Planning Fallacy" chapter — psychological basis for why pre-mortems surface biases that regular planning misses.
- [Product Compass — How Meta and Instagram Use Pre-Mortems to Avoid Post-Mortems](https://www.productcompass.pm/p/how-to-run-pre-mortem-template) — practical case study and template.
