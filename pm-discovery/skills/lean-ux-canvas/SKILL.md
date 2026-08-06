---
name: lean-ux-canvas
description: >
  Use when a team is kicking off a new feature, initiative, or sprint and needs
  to align on the business problem, target users, solution hypotheses, and the
  first experiment to run — all on one page.
version: 0.1.0
type: component
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/lean-ux-canvas/template.md
---

# Lean UX Canvas

## Purpose
Produce a completed **Lean UX Canvas** — the one-page collaborative artifact
(Jeff Gothelf, 2013/2016) that frames a product initiative as a set of
hypotheses to be validated, not a feature list to be built. The canvas forces
a team to connect the business problem all the way through to user outcomes,
solution ideas, and a concrete learning experiment, in a single structured
session.

The output supports sprint planning, stakeholder alignment, discovery kick-off,
and go/no-go decisions at the initiative level.

**When NOT to use:**
- Pure problem exploration without any solution direction yet → use
  `problem-framing-canvas` instead (that skill has no Block 5/6/7/8).
- Continuous discovery across many opportunity areas → use
  `opportunity-solution-tree` (OST is a multi-level tree for ongoing work; this
  canvas is a one-page sprint planning artifact for a single initiative).
- Business-model planning (revenue streams, cost structure, channels) → use
  `lean-canvas` in `pm-strategy` (that skill covers the full Osterwalder / Ash
  Maurya business-model canvas; this skill is UX/product-initiative scoped).
- The team already has validated hypotheses and needs execution planning →
  the canvas phase is done; move to backlog refinement or a PRD.

## Inputs
- **Required:** a brief description of the initiative, feature, or problem
  space the team is addressing. If this is missing, ask for it before
  proceeding; do not guess the scope.
- **Optional:** known business metrics / OKRs that the initiative must move
  (feed Block 2); existing user research or personas (feed Block 3); any
  solution ideas already on the table (feed Block 5); a named product or
  service context (helps sharpen Block 1). If absent, surface reasonable
  defaults and flag them as assumptions.

## Output Contract
The deliverable is a **completed Lean UX Canvas** with all eight blocks filled
(see `template.md`):

1. **Business Problem** — a crisp statement of the problem the business faces
   and why it matters now. Not a solution statement. 1–3 sentences.
2. **Business Outcomes** — 2–4 measurable changes in user behavior that signal
   the business problem is solved (leading indicators, not revenue; e.g.,
   "7-day retention rises from 28% to 40%").
3. **Users** — who the canvas is designed for: specific user types or personas,
   not "all users." Include their context and relationship to the product.
4. **User Outcomes & Benefits** — what users want to achieve (the job-to-be-done
   they hire the product for). Expressed as user goals, not product features.
5. **Solution Ideas** — 2–5 concrete product or UX concepts that could create
   those user outcomes. Brief, not spec-level. These are inputs to hypotheses,
   not commitments.
6. **Hypotheses** — 2–4 structured hypothesis statements in the canonical form:
   "We believe [solution idea] will achieve [user outcome] for [user type].
   We'll know this is true when [measurable signal]."
7. **What's the Most Important Thing to Learn First?** — the single riskiest
   assumption that, if wrong, would invalidate the initiative. One sentence,
   phrased as a question.
8. **What's the Least Amount of Work to Learn It?** — the minimum viable
   experiment (prototype, interview, smoke test, spike, etc.) that would answer
   the Block 7 question. Include a time-box.

Format: eight clearly labeled blocks. Each block uses the length guidance
above. The whole canvas should fit on one page (printed A3 / two-column
layout). No prose preamble before Block 1.

**GOOD (excerpt):**
> **Block 6 — Hypotheses:**
> We believe adding an in-app guided tour will increase first-session task
> completion for first-time users. We'll know this is true when the Day-1
> task-completion rate rises above 60% (baseline: 41%) within two sprint
> cycles.

**BAD (excerpt):**
> "Block 5 — Solutions: Build a better onboarding, improve the dashboard, and
> add notifications."
> — fails: solutions are vague feature names with no connection to user
> outcomes; Block 6 hypotheses are absent; no measurable signal.

## Process
1. **Anchor the business problem (Block 1)** — ask the user to describe the
   initiative; synthesize it into a crisp problem statement. If the user
   provides a solution instead ("we want to build X"), reframe it as the
   problem that X would solve.
2. **Derive business outcomes (Block 2)** — surface 2–4 leading behavioral
   metrics. Prefer metrics the team can actually measure. Flag any that are
   lagging revenue metrics and suggest a leading proxy.
3. **Identify users (Block 3)** — name the specific user types or personas.
   If none are given, propose plausible types based on the problem context and
   ask the user to confirm.
4. **Surface user outcomes (Block 4)** — articulate what each user type wants
   to achieve; frame as jobs-to-be-done, not feature requests.
5. **Brainstorm solution ideas (Block 5)** — generate 2–5 concrete concepts.
   Include any ideas the user mentioned, then add alternatives that span the
   solution space (don't anchor on a single approach).
6. **Write hypotheses (Block 6)** — for each major solution idea, write a
   structured hypothesis linking solution → user outcome → user type →
   measurable signal. Ensure every hypothesis is falsifiable.
7. **Identify the riskiest assumption (Block 7)** — review the hypotheses and
   surface the single assumption that, if wrong, would cause the most harm.
   Frame it as a one-sentence question.
8. **Design the minimum experiment (Block 8)** — propose the lightest-weight
   test that answers Block 7 (interview, prototype test, A/B, smoke test,
   spike). Include a time-box (e.g., "5 user interviews in 3 days").
9. Run the Quality Bar below; revise any block that fails; then return the
   completed canvas.

## Quality Bar
Before returning, confirm:
- [ ] All eight blocks are present and non-empty.
- [ ] Block 1 is a **problem statement**, not a solution or feature request.
- [ ] Block 2 outcomes are **behavioral and measurable** (not "increase revenue"
  or vague sentiment).
- [ ] Block 3 names **specific user types**, not "users" or "customers" in
  general.
- [ ] Block 4 is expressed as **user goals** (jobs-to-be-done), not features.
- [ ] Block 5 contains **2–5 distinct ideas** that span the solution space.
- [ ] Block 6 hypotheses follow the canonical form and are **falsifiable** (each
  has a measurable signal).
- [ ] Block 7 identifies **one** riskiest assumption as a question.
- [ ] Block 8 names a **specific experiment type** and includes a **time-box**.
- [ ] If the canvas is written to a file, it follows `template.md` — all eight
  blocks present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `lean-ux-canvas-happy` — cross-functional team kicking off a new feature sprint
  with a clear business context.
- `lean-ux-canvas-edge` — a solo engineer trying to fill the canvas without
  stakeholder input.
- `lean-ux-canvas-adversarial` — user insists on skipping Block 6 hypotheses
  because "we already know what to build."

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `problem-framing-canvas` — pure problem-space exploration; no solution ideas
  or hypotheses. Use it before this canvas when the problem itself is unclear.
- `opportunity-solution-tree` — continuous discovery tree for mapping many
  opportunities and solutions over time; broader scope than a single sprint
  canvas.
- `lean-canvas` (pm-strategy) — Ash Maurya's business-model canvas covering
  revenue, cost, channels; shares the "lean" name but is a different artifact.

### External Frameworks
- Jeff Gothelf & Josh Seiden, *Lean UX* (3rd ed., O'Reilly, 2021) — the
  primary source for the eight-block canvas structure and hypothesis format.
- Jeff Gothelf, "The Lean UX Canvas" (Miro blog, 2016) — original public
  introduction of the canvas with the canonical block definitions.
- Clayton Christensen, *Competing Against Luck* (2016) — Jobs-to-be-Done
  theory underpinning Block 4 (user outcomes as hired jobs, not features).
