---
name: brainstorm-experiments-new
description: >
  Design lean-startup experiments (pretotypes) for a new product or market entry,
  testing riskiest assumptions with minimal effort before building. Use when validating
  a new product concept, identifying testable hypotheses, or planning early customer
  discovery.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/brainstorm-experiments-new/template.md
---

# Design Lean-Startup Experiments (New Product)

## Purpose
Generate a portfolio of low-effort, high-learning pretotype experiments to validate
a new product concept or market entry hypothesis. Each experiment isolates a riskiest
assumption (demand, problem severity, willingness to pay, etc.) and proposes a lean
method to test it before engineering investment. Supports go/no-go and prioritization
decisions for early validation.

**When NOT to use:** designing experiments for an existing product (use `brainstorm-experiments-existing`),
brainstorming solution ideas without hypotheses (use `brainstorm-ideas-new`), or planning
full-scale A/B tests after launch (use domain-specific experiment frameworks).

## Inputs
- **Required:** a new product concept or market entry (problem, target customer, proposed solution or value hypothesis).
  Ask if the user does not provide these three anchors.
- **Optional:** market research, customer interviews, competitive context, budget/timeline constraints, or existing
  landing pages / mockups. If provided, read them first.

## Output Contract
The deliverable is an **experiment portfolio card**, structured as:

1. **Core Hypothesis** — an XYZ statement in the form "At least X% of Y will do Z" (market, confidence, behavior).
2. **Experiment Plan** — 2–4 lean pretotypes, each with:
   - **Experiment name & method** (landing page, concierge MVP, wizard-of-oz, video test, pre-order, etc.)
   - **Hypothesis tested** (the specific assumption this isolates)
   - **Metric & success threshold** (what counts as validation, and the bar)
   - **Effort & timeline** (rough story points or weeks)
3. **Riskiest Assumptions** — ranked by impact to go/no-go, with which experiments address each.
4. **Key Principles** — skin-in-the-game (real commitment, not opinion), YODA (your own data, not analogies),
   behavioral measure (not stated interest).

See `template.md` for the fill-in structure.

**GOOD (excerpt):**
> **Core Hypothesis:** At least 25% of mid-market product managers will sign up for a pre-order of a
> synthesis AI tool, indicating demand.
> **Experiment 1 — Landing Page + Waitlist** | Tests demand signal | Metric: 20%+ of 500 emails click "join waitlist" |
> 3 days. **Experiment 2 — Pre-Order** | Tests willingness to pay | Metric: 10%+ of email readers purchase | 5 days.

**BAD (excerpt):**
> "Build an MVP and launch it. People will love it." — fails because: no hypothesis, no metric, no definition
> of success, no isolation of the riskiest assumption.

## Process
1. **Anchor the core hypothesis** — restate problem, target customer, and value prop; phrase as XYZ ("X% of Y will Z").
2. **List riskiest assumptions** — rank by impact to go/no-go (demand, problem severity, willingness to pay, channel fit).
3. **Design 2–4 pretotypes** — for the top 1–3 assumptions, suggest lean methods (landing page, concierge, video,
   wizard-of-oz, pre-order, email campaign, survey, prototype test).
4. **Specify each experiment** — hypothesis tested, metric, success threshold, effort, timeline.
5. **Map assumptions to experiments** — show which assumption each experiment validates.
6. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The core hypothesis is stated as an XYZ statement ("At least X% of Y will Z").
- [ ] 2–4 experiments are included, each with a distinct assumption, metric, and success threshold.
- [ ] At least one experiment includes skin-in-the-game (real commitment: payment, time, reputation).
- [ ] Metrics are behavioral, not opinion-based ("sign up", "purchase", "attend", not "interested").
- [ ] Effort and timeline are estimated (rough, ballpark acceptable).
- [ ] Riskiest assumptions are mapped to experiments; the portfolio covers go/no-go blockers.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `brainstorm-experiments-existing` — experiments for feature validation in an existing product.
- `brainstorm-ideas-new` — ideation (solution ideas without hypotheses); inputs to this skill.
- `identify-assumptions-new` — structured assumption surfacing for new concepts; feeds into experiment design.

### External Frameworks
- Alberto Savoia, *The Right It* (2019) — pretotype / concierge MVP methodology, YODA (your own data) principle,
  skin-in-the-game as a demand signal.
- Steve Blank, *The Four Steps to the Epiphany* (2013) — customer discovery experiments and iterative validation.
- Ash Maurya, *Lean Product Playbook* (2014) — hypothesis-driven experimentation and MVP design.
