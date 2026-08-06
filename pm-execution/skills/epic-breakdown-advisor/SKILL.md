---
name: epic-breakdown-advisor
description: >
  Advise how to break an epic into user stories, milestones, and delivery
  phases, recommending the best decomposition strategy for the given context.
  Use when a team holds a large epic and needs to decide how to slice it into
  shippable increments, plan delivery phases, or choose between vertical
  slicing, walking skeleton, MLP, and similar approaches.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/epic-breakdown-advisor/template.md
---

# Epic Breakdown Advisor

## Purpose
Produce a structured breakdown plan for a single epic: recommend the most
appropriate decomposition strategy given team context, then translate that epic
into an ordered set of user stories, a milestone ladder, and delivery phases
with explicit rationale. The output helps a PM and team align on what to build,
in which order, and why — before sprint planning begins.

**When NOT to use:**
- **Single large story splitting** — use `user-story-splitting` to cut one
  oversized story into smaller ones.
- **Spatial story mapping** — use `user-story-mapping` to arrange an existing
  backlog into a narrative flow; that skill organizes stories you already have.
- **Epic framing / hypothesis** — use `epic-hypothesis` to frame the bet before
  decomposing; this skill assumes the epic's goal is already decided.
- **Sprint assignment** — use `sprint-plan` to assign ready stories to sprint
  slots; this skill creates those stories, not the sprint schedule.
- **Multiple epics simultaneously** — this skill advises on one epic at a time.

## Inputs
- **Required:** The epic statement — its goal, the user problem it solves, and
  the target user(s). If not provided, ask: *"What outcome does this epic
  achieve for which user?"* before proceeding.
- **Required:** Delivery context — team size, tech maturity of the area
  (greenfield vs existing system), and any hard deadlines or milestone gates.
  If absent, ask for these; they determine the right strategy.
- **Optional:** Acceptance criteria or success metrics for the epic — used to
  validate completeness of the story set.
- **Optional:** Known constraints (dependencies, compliance gates, platform
  limits, or must-ship requirements) — incorporated into the milestone plan.
- **Optional:** Preferred breakdown strategy — if the team already has a
  preference (e.g., always vertical slices), note it and apply it; otherwise
  the skill recommends.

## Output Contract
The deliverable is an **epic breakdown plan** with these sections (see
`template.md`):

1. **Epic Summary** — one-sentence restatement of the epic goal, target user,
   and success metric.
2. **Recommended Strategy** — the chosen decomposition approach with a two-to-
   three sentence rationale for why it fits this context over alternatives.
3. **User Stories** — an ordered list of stories in `As a … I want … so that …`
   format, each with an acceptance criterion and a T-shirt size estimate (XS/S/M/L).
4. **Milestone Ladder** — logical milestones (not sprints) that mark meaningful
   checkpoints: each milestone names its stories, the user value unlocked, and
   whether it is a potential early-ship candidate.
5. **Delivery Phases** — the stories and milestones grouped into ≤ 3 phases
   (Foundation / Core / Enrich, or equivalent), with a one-line rationale for
   each phase boundary.
6. **Risks & Sequencing Notes** — up to five items: dependencies, unknowns, or
   sequencing constraints the team should resolve before or during execution.

Format: structured text with numbered lists and one milestone table. Length:
~1–2 pages. Avoid vague placeholders — every story name and milestone must
reflect the actual epic content.

**GOOD (excerpt):**
> **Recommended Strategy:** Vertical slicing — each story delivers end-to-end
> user value in isolation and can ship independently.
>
> **Story 1 (S):** As a logistics manager I want to filter shipments by status
> so that I can focus on delayed items without scrolling the full list.
> *AC: filter persists across page reload; ≤ 2 s latency at 10 k rows.*

**BAD (excerpt):**
> "Story 1: Backend API. Story 2: Frontend. Story 3: Testing."
> — fails: these are horizontal layers, not user-value slices; no user, no
> benefit, no acceptance criterion, and the sequence leaves nothing shippable
> until the very end.

## Process
1. **Clarify the epic** — confirm the goal, target user, and success metric;
   if missing, ask before proceeding.
2. **Read the context** — note team size, tech maturity, deadlines, and
   constraints; these drive strategy selection.
3. **Select the strategy** — evaluate the main approaches and pick the best fit:
   - *Vertical slicing* — thin end-to-end slices through each user workflow;
     best when the area is well-understood and stories can ship independently.
   - *Walking skeleton* — a minimal end-to-end skeleton first, then flesh out;
     best for greenfield systems or when integration risk is the biggest unknown.
   - *MLP (Minimum Lovable Product)* — the smallest set that delivers a
     complete, delightful experience for one user segment; best for new-product
     epics where user delight is the gate.
   - *Risk-first* — lead with the riskiest or most uncertain story to validate
     the assumption before building the rest; best when a key unknown could
     invalidate the entire epic.
   - *Compliance/dependency-first* — lead with stories that unblock others or
     satisfy a regulatory gate; best when external dependencies impose ordering.
4. **Draft user stories** — decompose the epic into independently deliverable
   stories, each with a user, a want, a benefit, and a concrete acceptance
   criterion. Aim for 5–12 stories; if more, consider whether the epic should
   be split into child epics.
5. **Define milestones** — identify 2–4 meaningful checkpoints that mark value
   delivered to users, not internal technical gates.
6. **Group into phases** — assign stories and milestones to ≤ 3 delivery phases,
   respecting dependencies and the chosen strategy.
7. **Identify risks** — flag sequencing constraints, external dependencies, or
   unknowns that could block delivery.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The recommended strategy is **named and justified** with ≥ 2 sentences
  explaining why it fits this context better than the main alternative.
- [ ] Every user story follows the `As a … I want … so that …` format and has
  at least one concrete, testable acceptance criterion.
- [ ] Stories are **independently deliverable** within the chosen strategy —
  no story requires another to be in production before it can ship.
- [ ] The milestone ladder marks **user-visible value** delivered at each
  checkpoint, not internal technical gates.
- [ ] Delivery phases have **no more than 3** and each phase boundary is
  explained by a rationale (what changes between phases and why).
- [ ] The story list covers the epic's stated success metric — nothing critical
  is missing and nothing irrelevant is included.
- [ ] Size estimates (XS/S/M/L) are present and plausible (L stories are
  flagged as candidates for further splitting).
- [ ] Risks section lists at least one genuine sequencing constraint or unknown.
- [ ] If the output is written to a file, it follows `template.md` (a
  skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `epic-breakdown-advisor-happy` (happy path) — a well-specified B2B SaaS epic
  with clear context, yielding a vertical-slice breakdown.
- `epic-breakdown-advisor-edge` (edge) — a greenfield platform epic with high
  integration risk where walking skeleton is the right call.
- `epic-breakdown-advisor-adversarial` (adversarial) — a vague epic with no
  user, no success metric, and pressure to skip directly to story generation.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `user-story-splitting` — cuts one oversized story; use after this skill
  identifies any L-sized stories that need further decomposition.
- `user-story-mapping` — arranges the stories this skill generates into a
  spatial narrative flow for alignment workshops.
- `epic-hypothesis` — frames the product bet and defines the epic goal;
  should be run before this skill.
- `sprint-plan` — assigns the ready stories produced here to sprint slots.

### External Frameworks
- Jeff Patton, *User Story Mapping* (2014) — the source of activity → task →
  story decomposition hierarchy and "walking skeleton" thinking that underpins
  the milestone and phase structure here.
- Richard Lawrence & Paul Rayner, *Behavior-Driven Development with Cucumber* —
  INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small,
  Testable) used to validate each story in the Quality Bar.
- Gojko Adzic, *Impact Mapping* (2012) — goal-first decomposition discipline
  (why → who → how → what) that governs the epic-to-story translation in step 4.
- Henrik Kniberg, "Making Sense of MVP" (2016 blog) — the MLP / walking-skeleton
  distinction that drives strategy selection in step 3.
