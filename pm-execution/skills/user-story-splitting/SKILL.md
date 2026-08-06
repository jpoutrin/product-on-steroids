---
name: user-story-splitting
description: >
  Break a large or epic user story into smaller, independently-deliverable stories
  using proven patterns (SPIDR, INVEST, workflow steps, data variations, business
  rules, defer performance). Use when a story is too big for one sprint, fails
  INVEST (especially Independent or Small), or is flagged as an epic that needs
  decomposition before sprint planning.
version: 0.1.0
type: workflow
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/user-story-splitting/template.md
---

# Split Large User Stories

## Purpose
Take a user story (or epic) that is too large to complete in a single sprint and
produce a set of smaller stories that are each independently valuable, estimable,
and deliverable — without losing the original intent or creating artificial
technical sub-tasks. The output supports sprint planning, backlog grooming, and
story-point calibration.

**When NOT to use:**
- **Organizing a roadmap spatially** — use `user-story-mapping` (2-D backbone/walk).
- **Breaking an epic top-down** — use `epic-breakdown-advisor` (top-down decomposition
  from theme → feature → story; this skill operates on individual stories that
  are already at the story level but oversized).
- **Writing new stories from scratch** — use `user-stories` (green-field authoring).
- The story is already right-sized (fits comfortably within the team's sprint
  capacity with no ambiguity); splitting further would fragment value.

## Inputs
- **Required:** the large story or epic in "As a … I want … so that …" form (or
  equivalent). If only a title is provided, ask for the full story before
  proceeding.
- **Optional:**
  - **Sprint capacity / definition of small** — what "small" means to this team
    (e.g., ≤ 5 story points, ≤ 3 days). Defaults to "completable in one sprint by
    two developers."
  - **Acceptance criteria or context** — existing ACs, constraints, or background
    help pick the right split pattern.
  - **Preferred split pattern** — if the team has a preference (e.g., "always split
    by workflow step first"), apply it. Otherwise the skill chooses the best-fit
    pattern(s) from SPIDR.
  - **Non-goals / out-of-scope** — explicit exclusions from the original story help
    avoid re-including them in child stories.

## Output Contract
The deliverable is a **story-splitting plan** with these sections (see `template.md`):

1. **Original Story** — the source story restated verbatim plus a brief diagnosis
   of why it is oversized (INVEST dimension(s) failing).
2. **Split Pattern(s) Applied** — which SPIDR pattern(s) were used and why they
   fit this story better than the alternatives.
3. **Child Stories** — the resulting smaller stories, each with: a story title,
   the full "As a … I want … so that …" statement, and 2–4 acceptance criteria.
   Each child must satisfy INVEST independently.
4. **Story Map** — a one-line parent → children tree showing how the children
   together cover the original story's intent (and what is explicitly deferred).
5. **Deferred / Out of Scope** — anything intentionally left for a later iteration,
   with a brief rationale.
6. **Quality Check** — a per-child INVEST pass/fail table so the requester can
   verify the split at a glance.

Format: structured markdown. Length: concise — child stories are punchy (2–5 lines
each); the full plan is typically 1–2 pages. Never pad with generic advice.

**GOOD (excerpt):**
> **Split pattern:** Workflow Steps — the original story covers three sequential
> phases (search → compare → book) that can each deliver value independently.
>
> **Child 1 — Search results:**
> As a traveller I want to search for available hotels by city and date so that
> I can see what is available before committing.
> AC: Returns a paginated list sorted by price. Shows "no results" clearly.

**BAD (excerpt):**
> "Story 1: Frontend work. Story 2: Backend API. Story 3: Database schema."
> — fails because these are technical layers, not independently-deliverable slices
> of user value; none can be demonstrated to a stakeholder in isolation.

## Process
1. **Restate and diagnose** — quote the original story; identify which INVEST
   dimension(s) fail (usually S = too large, or I = tightly coupled) and why.
2. **Select split pattern(s)** — evaluate all six SPIDR lenses against the story;
   pick the one(s) that produce the most independently valuable slices:
   - **S — Spike** (for unknowns; produce a time-boxed research story first)
   - **P — Path / workflow** (split by sequential user steps)
   - **I — Interface** (split by UI surface or channel)
   - **D — Data** (split by data type, entity, or complexity tier)
   - **R — Rules** (split by business-rule variation or exception path)
   - **INVEST — Performance / non-functional** (defer "fast / secure / accessible"
     tiers as separate stories)
3. **Draft child stories** — for each split, write the full "As a … / I want … /
   so that …" with 2–4 ACs. Keep stories vertical (full stack, end-to-end value)
   rather than horizontal (technical layer).
4. **Verify coverage** — confirm the child stories together cover 100% of the
   original story's stated intent (nothing silently dropped); note anything
   deliberately deferred.
5. **INVEST check** — for each child story verify: Independent (not blocked by
   another child), Negotiable, Valuable (a stakeholder cares), Estimable,
   Small, Testable.
6. **Build the story map** — a one-liner parent → children tree with explicit
   "deferred" callouts.
7. Run the Quality Bar; revise any failing child before returning.

## Quality Bar
Before returning, confirm:
- [ ] Every child story is expressed as "As a … I want … so that …" (or an
  agreed equivalent) — not a technical task or layer description.
- [ ] Every child story has 2–4 acceptance criteria that are testable and
  specific.
- [ ] Every child story is **Independent** — it can be developed, tested, and
  demoed without completing another child first (no hidden ordering).
- [ ] Every child story is **Valuable** on its own — a stakeholder could accept
  it and get benefit before any other child is done.
- [ ] Every child story is **Small** — it fits the team's stated sprint capacity
  (or, if unknown, is clearly smaller than the original).
- [ ] The children together **cover the full intent** of the original story
  (nothing is silently dropped without being noted as deferred).
- [ ] The chosen split pattern is named and justified — not just implied.
- [ ] The Quality Check table lists each child story against the six INVEST
  dimensions.
- [ ] If the output is written to a file, it follows `template.md` — all 6
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `user-story-splitting-happy` — clear, oversized story with good context;
  expects a clean workflow-step split with full INVEST verification.
- `user-story-splitting-edge` — a story where the obvious split pattern (workflow)
  does not work well; expects the skill to choose an alternative (data variation
  or business rules) and justify why.
- `user-story-splitting-adversarial` — a request to split a story into technical
  layers (frontend / backend / DB); expects the skill to refuse that approach
  and produce value-vertical slices instead.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `user-stories` — writes new stories from scratch; this skill refines existing
  ones that are already written but oversized.
- `user-story-mapping` — organizes stories spatially on a backbone; consume its
  output to identify which stories need splitting before sprint planning.
- `epic-breakdown-advisor` — top-down decomposition from theme → feature → story;
  use it first when the input is an epic rather than a single large story.
- `sprint-plan` — consumes the child stories produced by this skill to build a
  sprint plan with capacity estimates.

### External Frameworks
- Richard Lawrence & Gojko Adzic, *Fifty Quick Ideas to Improve Your User Stories*
  (2014) — the practical source for split-by-workflow, split-by-data-variation,
  and split-by-business-rule patterns this skill applies.
- Bill Wake, "INVEST in Good Stories, and SMART Tasks" (XP123, 2003) — the INVEST
  mnemonic underpinning the Quality Bar and per-child verification table.
- SPIDR (Mike Cohn, *User Stories Applied*, 2004) — the six split lenses codified
  in Process step 2: Spike, Path, Interface, Data, Rules, + performance deferral.
