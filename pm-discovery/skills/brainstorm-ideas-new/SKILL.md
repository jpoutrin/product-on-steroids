---
name: brainstorm-ideas-new
description: >
  Generate structured product ideas for a new product or market entry from
  multiple perspectives. Use when starting product discovery for a new product,
  exploring initial features for a startup idea, or conducting unconstrained
  ideation from user problems and market gaps.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/brainstorm-ideas-new/template.md
---

# Brainstorm Product Ideas (New Product)

## Purpose
Generate a prioritized list of product ideas for a new product or market entry
through multi-perspective ideation (PM, Designer, Engineer). Supports initial
product discovery — determining what the product should be — by surfacing
opportunities from user problems, market gaps, and technology shifts, with
opportunity framing and quick viability assessment. Feeds downstream decisions
about positioning, business model, and first features.

**When NOT to use:** enhancements to an existing product (use
`brainstorm-ideas-existing`), designing experiments to validate a new product
(use `brainstorm-experiments-new`), or strategic/competitive analysis (use
market-research skills). This skill ideates; it does not validate.

## Inputs
- **Required:** target segment, user problem or market opportunity, and desired
  business outcome. If any is missing, ask before ideating.
- **Optional:** competitive context, technology constraints, pricing anchors,
  available data (market research, user interviews). Use these to ground ideas
  in reality, but do not require them to proceed.

## Output Contract
The deliverable is a **new-product ideas list** with these sections (see
`template.md`):

1. **Opportunity Framing** — the target segment, user problem/gap, and business
   outcome driving ideation.
2. **PM Perspective (5 ideas)** — features emphasizing market fit, value
   creation, and competitive advantage.
3. **Designer Perspective (5 ideas)** — features emphasizing UX, onboarding,
   and engagement.
4. **Engineer Perspective (5 ideas)** — features emphasizing technical
   innovation, platform capabilities, and integrations.
5. **Top 5 Prioritized Ideas** — cross-perspective ranking by: (1) core value
   delivery (solves the primary problem?), (2) speed to validate, (3)
   differentiation potential.
6. **Per-Idea Detail** — for each of the 5 prioritized ideas: 1–2 sentences of
   reasoning + 2–3 key assumptions to test.

Format: prose + one summary table. Length: ~1–2 pages. Tone: specific and
actionable, grounded in the opportunity, not blue-sky.

**GOOD (excerpt):**
> **Opportunity:** B2B customer success teams (50–500 person orgs) struggling to
> track customer health signals across fragmented data sources (CRM, support,
> analytics). Business outcome: reduce churn by enabling proactive support.
>
> **PM Perspective:** Single-dashboard customer health feeds from Salesforce,
> Intercom, and GA; early warning on churn signals; playbooks for common
> at-risk profiles.
>
> **Top 5 – Idea #1: "Health Score by Segment"**
> *Reasoning:* Builds on existing data, quick to validate (1–2 customer
> interviews), directly addresses the core problem.
> *Assumptions:* (a) CS teams have an agreed definition of "at-risk"; (b)
> integrating CRM data is feasible within 2 weeks; (c) health scores reduce
> churn response time by >20%.

**BAD (excerpt):**
> "We should build an AI assistant that uses machine learning to predict
> customer churn. We'll also add a mobile app, integrations, and real-time
> alerts."
> — fails: vague, no grounding in user problem or segment, no differentiation,
> no viability assessment, no testable assumptions.

## Process
1. **Confirm the opportunity** — segment, user problem, desired outcome. Ask
   clarifying questions if any is vague.
2. **Ideate from three perspectives** — generate 5 specific feature ideas each
   from: (a) PM (market fit, value, competition); (b) Designer (UX,
   onboarding, engagement); (c) Engineer (technical innovation, platform,
   integrations).
3. **Prioritize the top 5 across all perspectives** — weight by: core value
   delivery, speed to validate, differentiation.
4. **Detail each prioritized idea** — 1–2 sentences of reasoning + 2–3 key
   assumptions to test (not a full experiment design — quick validation hooks).
5. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Ideas are grounded in a specific segment and user problem — no
  blue-sky ideation.
- [ ] Each perspective contributes genuinely different ideas (PM ≠ Designer ≠
  Engineer views).
- [ ] Top 5 are ranked by: core value delivery, speed to validate,
  differentiation — not just volume.
- [ ] Reasoning for each prioritized idea is specific and testable (not vague
  positioning language).
- [ ] Assumptions are explicit and actionable (e.g., "validate via 2–3
  customer interviews" not "seems feasible").
- [ ] Ideas are distinguishable from each other (no duplicates or trivial
  variants).
- [ ] If output is written to a file, it follows `template.md` (a skill-scoped
  hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `brainstorm-ideas-existing` — ideates enhancements to an existing product
  (iterative discovery).
- `brainstorm-experiments-new` — designs experiments and bets to validate a
  new product concept (builds on this skill's ideas).

### External Frameworks
- [Continuous Product Discovery Masterclass
  (CPDM)](https://www.productcompass.pm/p/cpdm) (video course) — the discovery
  phases this skill supports (vision → initial discovery → continuous).
- [Startup
  Canvas](https://www.productcompass.pm/p/startup-canvas) — product strategy
  and business model for a new product; positioning follows from this skill's
  ideas.
