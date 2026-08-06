---
name: opportunity-solution-tree
description: >
  Build an Opportunity Solution Tree (OST) to connect a desired business outcome
  to customer opportunities, product solutions, and experiment bets. Use when
  structuring a discovery sprint, deciding what to build next, aligning the
  product trio on opportunity prioritization, or auditing whether a roadmap is
  grounded in customer needs rather than feature lists.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/opportunity-solution-tree/template.md
---

# Opportunity Solution Tree (OST)

## Purpose
Produce a structured four-level tree that traces a single measurable business
outcome down through customer opportunities, candidate solutions, and experiment
bets — making the logical chain from "why we're doing this" to "what we'll test
next" visible and auditable. Supports continuous discovery decisions: which
opportunities to pursue, which solutions to generate, and which experiments to
run first.

**When NOT to use:**
- Roadmap sequencing or sprint planning once opportunities are already validated
  (use `roadmap-prioritization` or `okr-planning`).
- Competitive feature analysis or positioning (use `competitor-analysis`).
- Generating personas or synthesizing interview data into raw insights
  (use `interview-synthesis` or `user-persona`); OST consumes that output, it
  does not replace it.
- Brainstorming without a defined outcome — the tree requires a single measurable
  outcome at the top; if none exists, define it first.

## Inputs
- **Required:** a desired outcome — a single measurable metric the team is
  pursuing (e.g., "increase 30-day retention from 28% to 40%"). If missing or
  multi-metric, ask the user to nominate one before proceeding; do not guess.
- **Required:** customer research signal — interview quotes, survey themes,
  support tickets, analytics patterns, or a summary of user pain points. At
  least a rough set of signals is needed to frame opportunities; if truly absent,
  flag the gap and offer a skeleton with clearly marked hypothetical placeholders.
- **Optional:** existing opportunity or solution ideas the team has already named
  — organize and enrich them rather than starting from scratch.
- **Optional:** prioritization emphasis — Opportunity Score (Importance ×
  (1 − Satisfaction)) or qualitative judgment; default to qualitative when
  numeric data is unavailable.
- **Optional:** depth requested — stub (one pass through all four levels) vs.
  full (multiple solutions per opportunity, detailed experiment specs).

## Output Contract
The deliverable is an **Opportunity Solution Tree document** structured as four
hierarchical levels (see `template.md`):

1. **Desired Outcome** — the single measurable top-of-tree metric: what it is,
   the current baseline, the target, and its source (OKR / strategy).
2. **Opportunities** — 3–7 customer needs, pains, or desires discovered through
   research, framed from the customer's perspective ("I struggle to…" / "I wish
   I could…"). Each entry includes a one-sentence evidence anchor, an Opportunity
   Score or qualitative priority rating, and a rank.
3. **Solutions** — for each prioritized opportunity (top 2–3), at least 3
   candidate solutions — not features, but approaches that could address the
   opportunity. Tag the lens (PM / Designer / Engineer / Customer) for
   each to encourage trio diversity. Identify the chosen solution(s) to carry
   into experiments.
4. **Experiments** — for each chosen solution, 1–2 fast, cheap tests. Each
   experiment specifies: hypothesis, method, primary metric, and success
   threshold.

Format: hierarchical markdown with clear level headings. Length scales with
depth requested; a stub fits ~1 page, a full tree ~2–3 pages.

**GOOD (excerpt):**
> **Opportunity 1 (rank #1):** "I struggle to remember where I left off after
> returning to the app after a few days." — *Source: 6/10 interview sessions.*
> Opportunity Score: Importance 0.8 × (1 − Satisfaction 0.2) = **0.64** (high priority)
>
> Solution 1a (PM lens): "Last-session resumption card on home screen"
> Solution 1b (Engineer lens): "Push notification with a 24-hr re-engagement
> summary"
> Solution 1c (Designer lens): "Progress breadcrumb trail visible on every screen"
>
> Experiment for 1a: **Hypothesis** — showing a resumption card will increase
> D7 retention by ≥5pp. **Method** — A/B test, 50/50 split, 2 weeks.
> **Metric** — D7 retention. **Success threshold** — ≥5pp lift, p < 0.05.

**BAD (excerpt):**
> "Opportunities: improve onboarding, add notifications, redesign the dashboard."
> — fails: these are features/solutions, not customer opportunities; no evidence
> anchors, no framing from the customer's perspective, no prioritization.

## Process
1. **Anchor the outcome** — confirm or help articulate the single desired outcome
   with a baseline and target. If the user gives multiple metrics, ask them to
   pick one; do not average or concatenate.
2. **Extract opportunities** — from the provided research, identify 3–7 customer
   needs/pains. Frame each from the customer's perspective. Group closely related
   ones (avoid a flat list of redundant variants).
3. **Prioritize opportunities** — apply Opportunity Score (Importance ×
   (1 − Satisfaction)) if numeric data is available; otherwise use a qualitative
   High / Medium / Low rating with a stated rationale. Rank and flag the top 2–3
   for solution generation.
4. **Generate solutions** — for each top-priority opportunity, brainstorm ≥ 3
   solutions, tagging PM / Designer / Engineer / Customer lens. Resist anchoring
   on the first idea; explicitly force at least one unconventional option.
5. **Select and justify** — for each opportunity, nominate the 1–2 solutions with
   the best risk/effort/impact profile to carry into experiments. Name the
   trade-offs briefly.
6. **Design experiments** — for each selected solution, specify a hypothesis,
   method (A/B test, prototype test, fake-door, etc.), primary metric, and success
   threshold. Prefer experiments that surface real signal over opinion-based
   validation.
7. **Assemble the tree** — render the full four-level hierarchy in the `template.md`
   structure.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The tree has exactly **one** desired outcome at the top, with a baseline and
  target metric stated.
- [ ] Every opportunity is framed from the **customer's perspective** (need/pain/
  desire), not as a feature or solution.
- [ ] Each opportunity has at least one **evidence anchor** (interview count,
  survey %, analytics observation, or explicit hypothesis label).
- [ ] The top 2–3 opportunities are **explicitly ranked** and prioritized.
- [ ] Each prioritized opportunity has **≥ 3 candidate solutions** tagged with
  the generative lens (PM / Designer / Engineer / Customer).
- [ ] Each experiment has a **hypothesis, method, metric, and success threshold**
  — not just "run a test."
- [ ] No opportunity is actually a feature or a solution in disguise.
- [ ] If the output is written to a file, it follows `template.md` — all four
  levels present, in order, with matching headings (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `opportunity-solution-tree-happy` — full research signal, clear outcome, happy
  path through all four levels.
- `opportunity-solution-tree-edge` — sparse research data; skill must generate a
  skeleton with explicit hypothesis labels and flag the discovery gap.
- `opportunity-solution-tree-adversarial` — user provides a feature list as
  "opportunities"; skill must reframe them into genuine customer opportunities and
  push back on solution-first framing.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `interview-synthesis` — synthesizes raw interview transcripts into opportunity
  themes that feed the Opportunities level of this tree.
- `user-persona` — persona context informs how opportunities are framed and
  weighted.
- `roadmap-prioritization` — consumes validated opportunities and solutions from
  the OST to sequence the roadmap.

### External Frameworks
- Teresa Torres, *Continuous Discovery Habits* (2021) — the canonical source for
  the OST four-level structure (outcome → opportunities → solutions → experiments)
  and the principle of continuous weekly discovery cadence this skill is built on.
- Dan Olsen, *The Lean Product Playbook* (2015) — Opportunity Score formula
  (Importance × (1 − Satisfaction)) used to rank opportunities in step 3.
- [The Extended Opportunity Solution Tree](https://www.productcompass.pm/p/the-extended-opportunity-solution-tree) — Product Compass deep-dive on OST variations and common failure modes.
- [What Is Product Discovery? The Ultimate Guide Step-by-Step](https://www.productcompass.pm/p/what-exactly-is-product-discovery) — broader discovery context in which OST sits.
