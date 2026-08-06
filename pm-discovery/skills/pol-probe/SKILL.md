---
name: pol-probe
description: >
  Map the organizational, political, and landscape forces surrounding a product
  initiative before engaging stakeholders formally. Use when preparing for a
  cross-functional initiative, anticipating stakeholder resistance, navigating
  budget or approval chains, or assessing external constraints (regulatory,
  competitive, market timing) that could block execution.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/pol-probe/template.md
---

# POL Probe — Politics / Organization / Landscape Brief

## Purpose
Produce a **POL Brief**: a structured intelligence document a PM uses to
understand the organizational and political terrain around a specific initiative
*before* entering formal stakeholder engagement. It surfaces who holds power,
who benefits or loses, where the approval chain runs, what external forces
constrain the initiative, and how to sequence conversations for maximum
effectiveness.

This is an organizational intelligence skill, not a user research skill. It
answers "Who do I need to move, and in what order?" — not "What do users want?"

**When NOT to use:**
- Preparing for a user discovery session → use `discovery-interview-prep`.
- Building an ongoing stakeholder relationship map for influence → use
  `stakeholder-map` (pm-influence plugin).
- Planning a user research program → use `discovery-process`.
- Financial or market landscape analysis → use `market-sizing` or
  `competitor-analysis`.

## Inputs
- **Required:** Initiative name and one-line description — what the PM is
  trying to ship or change. If missing, ask before proceeding.
- **Required:** Org context — the PM's company/team, their role, and any
  known stakeholders. If the PM is new and context is thin, proceed with a
  best-effort brief flagged with explicit confidence gaps (see Edge scenario).
- **Optional:** Known allies, blockers, or tensions — include as-is; the skill
  surfaces *additional* dynamics it can infer from the organizational pattern.
- **Optional:** Time horizon — when the initiative needs a decision or launch
  (default: next 90 days).
- **Optional:** External constraints the PM is already aware of (regulatory
  window, competitive pressure, board cycle).

## Output Contract
The deliverable is a **POL Brief** with these six sections (see `template.md`):

1. **Initiative Summary** — what is at stake: the initiative's goal, the
   decision needed, and why it matters now. 2–4 sentences.
2. **Political Map** — who has formal and informal power; who benefits, who
   loses, who is indifferent; alliances and tensions. Presented as a named
   roster with role, power level (High / Med / Low), stance (Champion /
   Neutral / Skeptic / Blocker), and a one-line rationale.
3. **Organizational Levers** — the actual decision-making path: approval chain,
   budget owner, veto points, committee cycles (e.g., planning sprints, QBRs)
   that govern when decisions can realistically be made.
4. **Landscape Constraints** — external forces that shape the initiative's
   feasibility window: regulatory timelines, competitive moves, market timing,
   technology dependencies, or board-level priorities.
5. **Risk Register** — top 3–5 political and organizational risks, each with
   likelihood (H/M/L), impact (H/M/L), and a mitigation action.
6. **Engagement Strategy** — recommended sequencing of stakeholder
   conversations (who to brief first, who to co-opt before the main pitch,
   who to isolate or avoid early), with a one-sentence rationale per step.

Format: structured prose with one named-roster table (Political Map) and one
risk table (Risk Register). Total length ~1–2 pages. All confidence gaps must
be flagged inline as `[Low confidence — validate with: <source>]`.

**GOOD (excerpt):**
> **Political Map (excerpt):**
> | Name | Role | Power | Stance | Rationale |
> |------|------|-------|--------|-----------|
> | Ana Ruiz | CTO | High | Champion | Data platform fits her 2025 infra consolidation goal |
> | Ben Park | VP Sales | High | Skeptic | Fears engineering distraction from pipeline features |
> | Carla Menz | Data Eng Lead | Med | Champion | Has been asking for this capability for 6 months |
>
> **Engagement Strategy (step 1):** Brief Ana Ruiz first to secure executive
> air cover before any group presentation — without it, Ben Park's skepticism
> will dominate the room.

**BAD (excerpt):**
> "There are some political dynamics to be aware of. The CTO seems supportive
> and Sales might push back. You should talk to people and build buy-in."
> — fails: no named individuals, no power/stance breakdown, no sequencing
> logic, no risk register, no actionable next step.

## Process
1. **Clarify scope** — confirm initiative name, the decision needed, and the
   time horizon. If org context is thin, note it and flag confidence gaps
   throughout; do not refuse to produce the brief.
2. **Build the Political Map** — identify formal decision-makers (by title and
   name where known), informal influencers, and parties with something to gain
   or lose. Assign power level and stance; write a one-line rationale for each.
3. **Trace the Organizational Levers** — map the approval chain from the PM's
   position to final sign-off. Identify the budget owner, veto holders, and any
   committee or calendar cycle the decision must pass through.
4. **Assess the Landscape** — identify external forces (regulatory, competitive,
   market timing, technology, board priorities) that create urgency or
   constraint. Prioritize forces with a concrete timeline within the next 12
   months.
5. **Draft the Risk Register** — select the top 3–5 political/org risks (not
   product risks). For each: name it, rate likelihood and impact, and propose a
   mitigation action the PM controls.
6. **Design the Engagement Strategy** — sequence stakeholder conversations:
   who to brief 1-on-1 before any group session, who to co-opt as a visible
   ally, who to neutralize through indirect reassurance, who to engage last.
   Anchor each step in the Political Map and Risk Register.
7. **Flag confidence gaps** — mark any element where information is inferred
   or absent with `[Low confidence — validate with: <source>]`.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The Political Map names **specific individuals or roles** (not vague
  groups), each with power level, stance, and a rationale.
- [ ] The Organizational Levers section identifies the **actual approval chain**
  and at least one budget owner or veto point.
- [ ] The Risk Register contains **3–5 political or org risks** (not product
  risks), each with likelihood, impact, and a mitigation the PM can act on.
- [ ] The Engagement Strategy gives **sequenced, named steps** — not generic
  "build buy-in" advice.
- [ ] Every element derived from limited information carries a
  **`[Low confidence — ...]` flag**.
- [ ] The output is **honest**: if a stakeholder is a genuine blocker, they are
  labeled as such — no spin or diplomatic softening that obscures the reality.
- [ ] If the output is written to a file, it follows `template.md` with all
  six sections present and headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `pol-probe-happy` — cross-functional data platform initiative; rich org
  context; guards against generic stakeholder lists with no sequencing logic.
- `pol-probe-edge` — PM is new to the company; thin context; guards against
  refusal and against false confidence in inferred dynamics.
- `pol-probe-adversarial` — hostile stakeholder; PM requests framing that
  makes them say yes; guards against spin replacing honest risk assessment.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `discovery-interview-prep` — prepares for user discovery sessions; consumes
  personas and research questions, not org dynamics.
- `stakeholder-map` (pm-influence) — builds ongoing stakeholder relationship
  maps for influence; pol-probe feeds the initial intelligence into that map.
- `discovery-process` — plans user research programs; pol-probe is about org
  terrain, not user research design.
- `competitor-analysis` — provides competitive intelligence for the Landscape
  Constraints section.

### External Frameworks
- Roger Fisher & William Ury, *Getting to Yes* (1981) — principled negotiation;
  the "interests vs positions" lens underpins how this skill surfaces what
  stakeholders *actually* care about behind their stated stance.
- Jeffrey Pfeffer, *Power: Why Some People Have It and Others Don't* (2010) —
  organizational power dynamics framework; informs the power-level taxonomy
  and the Organizational Levers section.
- Jeanne Liedtka & Tim Ogilvie, *Designing for Growth* (2011) — stakeholder
  ecosystem mapping; source for the "who benefits / who loses" framing in the
  Political Map.
