---
name: retro
description: >
  Facilitate a structured sprint retrospective with thematic synthesis, action
  items, and carry-over tracking. Use when running a retrospective, reflecting
  on a sprint, creating action items from team feedback, or learning how to run
  effective retros.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/retro/template.md
---

# Facilitate a Sprint Retrospective

## Purpose
Capture and structure team insights from a sprint, release, or project phase —
surfacing what worked, what didn't, and **prioritized action items with owners
and deadlines** — so that improvements compound across cycles. The output is
actionable, not blame-seeking; retros drive iterative improvement.

**When NOT to use:** post-mortems (pre-incident reflection, not post-sprint
retrospective), meeting summarization (use `summarize-meeting` — this skill
produces *structured reflection*, not transcript), or one-off team check-ins
without actionable next steps. Retros are for recurring, structured learning.

## Inputs
- **Required:** sprint/phase identifier, sprint dates, team size, and mode of
  feedback (e.g., team meeting, async survey, sticky notes, Slack thread). If
  the user provides raw feedback artifacts (survey responses, sticky notes,
  Slack exports, previous retro notes), read and process them first.
- **Optional:** sprint goal and outcome (committed vs. completed story points),
  prior retro action items and their status, velocity history, team dynamics
  context, or a chosen retro format (Start/Stop/Continue, 4Ls, Sailboat, or
  custom). Default: infer format from team context.

## Output Contract
The deliverable is a **retro summary memo** with these sections (see
`template.md`):

1. **Sprint Performance** — goal achieved/partial/missed, velocity commitment vs.
   completion, key blockers/wins.
2. **Themes & Feedback** — 3–5 thematic groupings of team input (organized by
   format: Start/Stop/Continue, Liked/Learned/Lacked/Longed, or Wind/Anchor/Rocks/Island).
3. **Action Items** — 2–3 prioritized improvements, each with owner, deadline,
   and success metric; reference prior actions and their status.
4. **Carry-over from Last Retro** — track completion of prior commitments
   (Done / In Progress / Not Started).

Format: prose + one action-item table. Length: ~1–2 pages. Tone: constructive,
focused on systems not blame.

**GOOD (excerpt):**
> **Sprint 42 Retrospective — Aug 6–20, 2026**
> ### Themes (4Ls Format)
> - **Liked:** standup cadence, pair-programming sessions, and async docs
> - **Learned:** time-zone async is hard; we need a sync window
> - **Lacked:** clarity on acceptance criteria before dev started
> - **Longed For:** a working CI/CD pipeline to unblock integration testing
>
> ### Action Items
> | Priority | Action | Owner | Deadline | Success Metric |
> |---|---|---|---|---|
> | 1 | Draft acceptance-criteria checklist | PM | Aug 27 | Adopted in Sprint 43 |
> | 2 | Unblock CI/CD (owner: Eng) | Eng Lead | Sep 3 | 90% of PRs run automated tests |
>
> *Carry-over from Sprint 41: "Hire contract QA" — In Progress (offer extended, start date Sep 10)*

**BAD (excerpt):**
> "Sprint went fine. Team was slow. Let's be faster next sprint."
> — fails: no thematic structure, no specific blockers, no actions with owners/dates, no metric to measure improvement.

## Process
1. **Choose or infer a retro format** — Start/Stop/Continue (simplest), 4Ls
   (emotional/learning lens), Sailboat (metaphorical), or custom. If unsure, ask
   the team or default to Start/Stop/Continue.
2. **If raw feedback provided** (survey, sticky notes, Slack, etc.), read it
   first; group items into 3–5 thematic clusters; note sentiment and frequency.
3. **Analyze sprint performance** — Did the team achieve the sprint goal?
   Velocity: over-/under-committed? Major blockers and how they were resolved?
   Collaboration patterns (strong pairs, bottlenecks)?
4. **Generate 2–3 action items** — each specific, assignable, measurable, with a
   deadline within 1–2 sprints. Avoid vague goals ("communicate better"); prefer
   concrete steps ("hold a Friday sync for X−Y timezones").
5. **Track prior actions** — if available, show status of retro items from the
   previous cycle (Done / In Progress / Not Started) and explain blockers if not
   completed.
6. **Run the Quality Bar** — then return the memo.

## Quality Bar
Before returning, confirm:
- [ ] Sprint performance (goal, velocity, blockers) is **clearly stated**, not vague.
- [ ] Feedback is **organized into 3–5 themes**, not a flat list.
- [ ] The **retro format** (Start/Stop/Continue, 4Ls, etc.) is declared and used consistently.
- [ ] **2–3 action items** are prioritized, each with owner, deadline, and a success metric (not "be better").
- [ ] Action item deadlines are **within 1–2 sprints** (realistic, not deferred).
- [ ] **Carry-over tracking** shows prior actions' status (Done / In Progress / Not Started).
- [ ] Tone is **constructive** — systems, not blame; improvement-focused, not punitive.
- [ ] If the output is written to a file, it follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `retro-happy` (happy path) — clear feedback, strong data (velocity, blockers), generates actionable improvements.
- `retro-edge` (edge) — sparse or conflicting feedback; skill must synthesize and clarify assumptions.
- `retro-adversarial` (adversarial) — demoralizing sprint (missed goal, major crisis); skill surfaces root causes and maintains constructive framing.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `summarize-meeting` — transcribes and summarizes a discussion; use *before*
  retro if you have a recorded standup or retro meeting to distill into themes.
- `pre-mortem` — identifies risks and failure modes *before* a sprint; retro
  reflects on what actually happened *after*.

### External Frameworks
- Norm Kerth, *Project Retrospectives: A Handbook for Team Review* (2001) —
  foundational retrospective facilitation methodology; inspires the
  "Prime Directive" (assume good intent, systems over blame).
- Agile Retrospectives: Making Good Teams Great (Derby & Larsen, 2006) — classic
  four-question retro format and advanced facilitation patterns.
- Sailboat, 4Ls, Start/Stop/Continue — standard retro formats; choose based on
  team maturity and context.
