---
name: sprint-plan
description: >
  Plan a sprint with capacity estimation, story selection, dependency mapping,
  and risk identification. Use when preparing for sprint planning, estimating
  team capacity, selecting stories, or balancing sprint scope against velocity.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/sprint-plan/template.md
---

# Plan a Sprint

## Purpose
Produce a defensible sprint plan that balances team capacity, story selection,
dependencies, and risk — with explicit sequencing and mitigations so the sprint
can execute with clarity. Supports sprint kickoffs, capacity planning, and
risk-aware scope commits.

**When NOT to use:** detailed story refinement (use `user-story`), roadmap
planning across multiple sprints (use `product-roadmap`), or retrospective
analysis (use dedicated retro frameworks). Sprint planning bounds *this* sprint's
scope; it does not plan the year.

## Inputs
- **Required:** sprint duration (2 weeks, 1 week, etc.), team roster with
  availability (PTO, on-call, meetings), and a prioritized product backlog.
- **Optional:** historical velocity data (last 3 sprints), previous sprint
  reports, story estimates, known blockers or dependencies.

## Output Contract
The deliverable is a **sprint plan** with these sections (see `template.md`):

1. **Sprint Goal** — one sentence describing what success looks like.
2. **Team Capacity** — number of team members, availability adjustments,
   historical velocity, and calculated available capacity in story points or
   ideal hours, *with* a 15–20% buffer for unexpected work.
3. **Committed Stories** — prioritized list of stories with story points, owner,
   and dependencies; total capacity used and remaining buffer.
4. **Dependency Map** — stories that depend on other stories or external teams,
   sequencing recommendations, and critical path identification.
5. **Risks & Mitigations** — stories with high uncertainty, external
   dependencies, knowledge concentration, or other threats, each with a
   mitigation strategy.
6. **Success Criteria** — how the team will measure sprint success.

Format: prose + tables/lists. Length: ~1–2 pages. Every capacity figure is
reasoned; every story is linked to a goal.

**GOOD (excerpt):**
> **Team Capacity:** 5 people × 2 weeks = ~40 ideal hours. Historical velocity:
> ~28 points/sprint. Adjustments: 1 person in meetings 40% of sprint = −8 hours.
> Available capacity: ~28 points. **Buffer (20%): 5.6 points → reserve 6 points.**
> **Committed: 22 points** (6 stories). **Remaining: ~6 points for bugs/urgent work.**
>
> **Risk:** Story X depends on external API (third-party team). Mitigation:
> escalate API timeline by EOD Friday; if slip, swap Story X for Story Y.

**BAD (excerpt):**
> "We're committing 35 points. Team is 5 people. We should be able to do this."
> — fails: no velocity basis, no buffer, no reasoning about dependencies,
> no risk plan if the external blocker slips.

## Process
1. **Define sprint goal** — one clear sentence; align team on what success is.
2. **Estimate team capacity**:
   - Count team members and their availability (PTO, on-call, meetings).
   - Pull historical velocity (average story points per sprint from last 3 sprints).
   - Apply availability adjustments to get net available capacity.
   - Reserve 15–20% for unexpected work, bugs, tech debt.
3. **Select and sequence stories**:
   - Pull from the prioritized backlog in order.
   - Verify each story meets Definition of Ready (clear acceptance criteria,
     estimated, no blockers).
   - Stop when committed capacity is reached.
4. **Map dependencies**:
   - Identify stories that depend on other stories or external teams.
   - Sequence dependent stories so blockers are unblocked early.
   - Flag external dependencies and owners.
   - Identify the critical path (longest chain of dependencies).
5. **Identify risks and mitigations**:
   - Flag stories with high uncertainty, complexity, or knowledge concentration.
   - Flag external dependencies that could slip.
   - For each risk, define a mitigation (escalate, swap story, reduce scope).
6. **Define success criteria** — how the team knows the sprint was successful.
7. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Sprint goal is a **single, clear sentence** describing what success looks
  like.
- [ ] Team capacity is **calculated** from team size, availability, historical
  velocity, and a reasoned buffer (15–20%).
- [ ] Every committed story is **estimated and in the backlog** (no new stories
  added mid-sprint without a buffer burn).
- [ ] Committed stories total is ≤ available capacity (respect the buffer).
- [ ] **Dependencies are mapped** — sequencing shows which stories block which.
- [ ] External dependencies are **flagged** and assigned an owner.
- [ ] **Every risk has a mitigation** — escalation, story swap, or scope
  reduction.
- [ ] Definition of Ready is **verified** for each story (AC clear, estimated,
  no blockers).
- [ ] If written to a file, it follows `template.md` — all 6 sections present,
  in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `sprint-plan-happy` (happy path) — well-groomed backlog, clear velocity,
  straightforward dependencies.
- `sprint-plan-edge` (edge) — sparse velocity history, high uncertainty stories,
  tight capacity.
- `sprint-plan-adversarial` (adversarial) — vague backlog, external blockers,
  team unavailability, conflicting priorities.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `user-story` — write well-formed user stories; these feed the sprint backlog.
- `product-roadmap` — plan across multiple sprints; sprint plans execute
  roadmap milestones.

### External Frameworks
- Scrum Guide (2020) — sprint planning ceremony, Definition of Done, capacity
  planning.
- Agile Estimating and Planning (Mike Cohn, 2005) — velocity-based capacity,
  story selection, buffer and contingency planning.
- James Shore, *The Art of Agile Development* (2007) — risk identification and
  mitigation in sprints.
