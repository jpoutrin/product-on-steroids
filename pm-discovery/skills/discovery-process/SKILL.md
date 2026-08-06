---
name: discovery-process
description: >
  Plan and orchestrate a complete discovery effort — choosing the right methods,
  sequencing them into phases, and producing a Discovery Plan that guides the
  entire arc from problem exploration to synthesized insights. Use when kicking
  off a new discovery cycle, scoping a discovery sprint, designing a continuous
  discovery cadence, or deciding which research methods to run and in what order.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/discovery-process/template.md
---

# Plan a Discovery Effort

## Purpose
Produce a **Discovery Plan** — a structured, time-bounded roadmap that specifies
what question a discovery effort is trying to answer, which methods will answer
it, in what sequence, and what artifacts will result. The plan gives a PM and
their team a shared operating picture before the first interview is scheduled.

This is the **meta-skill**: it does not run individual research methods itself —
it decides *which* skills from the pm-discovery toolkit to invoke and *when*, so
the team's time and participant pool are spent on signal, not scattered activity.

**When NOT to use:**
- You need to execute a single specific method, not plan the overall arc — go
  directly to `interview-script`, `opportunity-solution-tree`, `user-personas`,
  etc.
- The discovery question is already fully defined and the method is decided —
  use `discovery-interview-prep` to prepare for one specific session.
- The work is post-discovery: synthesizing already-collected data → use
  `summarize-interview`, `jobs-to-be-done`, or `problem-statement`.
- You are prioritizing or roadmapping (post-discovery execution) — this skill
  stops at the plan; it does not build roadmaps or prioritize opportunities.

## Inputs
- **Required:** the discovery trigger — what business or product event prompted
  this discovery effort (new initiative, metric drop, strategic bet, etc.) and
  the rough scope (product area, customer segment, geographic market). If missing,
  ask for the trigger and scope before producing the plan; do not assume them.
- **Optional:**
  - A draft "discovery question" or hypothesis — the skill will sharpen it if
    provided, or generate one from the trigger if absent.
  - Time horizon or sprint length — defaults to a 4–6-week discovery sprint.
  - Cadence preference — sprint-scoped (bounded) vs. continuous weekly cadence
    (Teresa Torres model); defaults to sprint-scoped unless stated.
  - Known constraints — access to users, size of participant pool, stakeholder
    deadlines, budget, team bandwidth.
  - Existing research or data — what is already known and does not need to be
    re-discovered.

## Output Contract
The deliverable is a **Discovery Plan document** structured as below (see
`template.md`):

1. **Discovery Goal** — the primary question the effort will answer, restated as
   a crisp "We need to understand …" statement; the decision it will unlock; and
   a measurable "done" criterion for when discovery is complete enough to act.
2. **Methods & Rationale** — a table of recommended research methods (skills to
   invoke), each with: method name, purpose (what it answers), the pm-discovery
   skill that operationalizes it, and why this method over alternatives.
3. **Phase Plan** — three phases with dates/durations and the methods assigned
   to each:
   - *Explore* — wide, generative; understand the problem space without
     pre-judging solutions.
   - *Validate* — focused, evaluative; test the leading hypothesis or
     opportunity frame against real users.
   - *Synthesize* — convergent; turn raw findings into a shared model
     (opportunity tree, persona set, problem statement) that feeds execution.
4. **Artifacts Checklist** — the specific documents the plan will produce, each
   mapped to the phase that produces it and the skill that generates it.
5. **Risks & Mitigations** — the top 3–5 risks that could derail this discovery
   effort (low user access, leading questions, confirmation bias, scope creep,
   stakeholder pre-commitment to a solution) and a concrete mitigation for each.

Format: structured document (~1.5–2 pages). Each section uses headings and
tables or bullet lists. Do not produce a wall of prose.

**GOOD (excerpt):**
> **Discovery Goal:** We need to understand why SMB finance managers abandon the
> invoice-approval flow before submission — and whether the friction is cognitive
> (too many steps) or trust-based (unsure the action is reversible). Done when
> we can state the primary failure mode with ≥ 3 confirming participant quotes
> and a proposed OST branch to explore.
>
> **Phase Plan (4 weeks):**
> | Phase | Week | Methods | Skills |
> |-------|------|---------|--------|
> | Explore | 1–2 | 5 problem interviews, diary study review | `interview-script`, `summarize-interview` |
> | Validate | 3 | Assumption mapping, 3 concept tests | `identify-assumptions-new`, `opportunity-solution-tree` |
> | Synthesize | 4 | JTBD synthesis, problem statement | `jobs-to-be-done`, `problem-statement` |

**BAD (excerpt):**
> "We'll do some user interviews and figure out what's wrong. Let's also maybe
> look at analytics and talk to sales."
> — fails: no goal statement, no sequencing logic, no artifacts, no rationale
> for why these methods and not others, no done criterion.

## Process
1. **Clarify the trigger and scope** — if the trigger or scope is absent or
   vague, ask one focused question to pin them before proceeding.
2. **Draft the Discovery Goal** — restate the trigger as a "We need to
   understand …" question. Add the decision it will unlock and the done
   criterion.
3. **Audit existing knowledge** — note what is already known from prior
   research, analytics, or stakeholder input so the plan doesn't re-discover
   the obvious. Flag gaps.
4. **Select methods** — for each knowledge gap, choose the most efficient method
   from the pm-discovery toolkit. Prefer depth (5–8 rich interviews) over
   breadth (20 shallow surveys) for early explore phases. Document the rationale
   for each choice.
5. **Sequence into phases** — assign methods to Explore / Validate / Synthesize.
   Ensure Explore comes before Validate; do not skip to validation without a
   generative phase. Assign realistic durations using the time horizon input.
6. **Enumerate artifacts** — list every document the plan will produce and which
   skill generates it.
7. **Identify risks** — brainstorm what could go wrong (access, bias, scope
   creep, pre-committed stakeholders). Keep the top 3–5 and write a one-line
   mitigation each.
8. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The Discovery Goal is phrased as "We need to understand …", includes the
  decision it unlocks, and has a concrete done criterion.
- [ ] Every selected method has an explicit rationale ("this over X because …").
- [ ] All three phases (Explore, Validate, Synthesize) are present with
  durations; Explore comes before Validate.
- [ ] Each artifact in the Artifacts Checklist is mapped to a phase and a
  specific pm-discovery skill.
- [ ] Risks & Mitigations lists 3–5 items with one-line mitigations — not
  generic platitudes ("we'll be careful") but concrete actions.
- [ ] The plan does not pre-commit to a solution — discovery stays in problem
  space through the Explore phase.
- [ ] If the user specified a cadence preference (sprint vs. continuous), the
  plan respects it; if absent, the default sprint-scoped format is used.
- [ ] If the output is written to a file, it follows `template.md` — all 5
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `discovery-process-happy` — standard sprint-scoped discovery kick-off for a
  B2B SaaS product team with a clear trigger and moderate user access.
- `discovery-process-edge` — continuous discovery cadence request with a vague
  trigger, constrained user access, and an existing opinionated stakeholder.
- `discovery-process-adversarial` — PM already has a solution in mind and frames
  the request as "validate our idea" rather than genuinely exploring the problem.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `interview-script` — operationalizes the interview sessions recommended in the
  Explore phase; consumes the Discovery Goal as the interview objective.
- `summarize-interview` — digests raw interview notes into structured findings;
  feeds the Synthesize phase.
- `opportunity-solution-tree` — the primary Synthesize artifact for mapping
  opportunities; the plan's Phase 3 output.
- `user-personas` — produced in Synthesize when the plan identifies distinct
  customer segments worth modeling.
- `jobs-to-be-done` — alternative synthesize artifact when the frame is
  functional-progress rather than segment-based.
- `problem-statement` — the terminal deliverable of a well-run discovery arc;
  produced at the end of Synthesize.
- `identify-assumptions-new` — used in the Validate phase to surface and
  prioritize assumptions before investing in concept tests.
- `discovery-interview-prep` — prepares a PM for a single interview session;
  runs *within* the Explore phase, not instead of this plan.
- `customer-journey-map` — optional Explore artifact when the problem spans
  multiple touchpoints or actors.

### External Frameworks
- Teresa Torres, *Continuous Discovery Habits* (2021) — the weekly interview
  cadence, opportunity solution tree, and assumption testing sequence that
  inform the three-phase structure of this skill.
- IDEO / HASSO-PLATTNER Design Thinking model — Empathize → Define → Ideate
  sequence maps to Explore → Synthesize → (execution); used to validate phase
  ordering logic.
- Marty Cagan, *Inspired* (2nd ed., 2018), Ch. 5–7 — discovery vs. delivery
  distinction; the "dual-track" framing that positions this skill as the
  discovery-lane orchestrator.
- Erika Hall, *Just Enough Research* (2nd ed., 2019) — method selection
  heuristics (when to interview vs. survey vs. observe) that underpin the
  Methods & Rationale table guidance.
