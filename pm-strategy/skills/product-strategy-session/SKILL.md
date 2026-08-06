---
name: product-strategy-session
description: >
  Facilitate a live, timeboxed product-strategy working session — a run-of-show
  agenda, the questions to ask at each stage, techniques to converge a group, and
  a synthesized readout of decisions, open questions, and next steps. Use when
  running a strategy offsite or workshop, aligning a cross-functional group on
  product direction, unblocking a stalled strategy debate, or preparing to
  facilitate a strategy meeting.
version: 0.1.0
type: interactive
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/product-strategy-session/template.md
---

# Facilitate a Product Strategy Session

## Purpose
Run a **live product-strategy working session** end to end: propose a timeboxed
run-of-show, drive each stage with the right questions, apply convergence
techniques to move a group from divergent opinions to shared decisions, and
capture a synthesized readout (decisions made, trade-offs accepted, open
questions, and owned next steps). The skill orchestrates the **human session**;
it does not itself author the strategy document. A well-run session might
*produce the inputs to* a `product-strategy-canvas`, but its deliverable is the
session plan and the readout that records what the group actually decided.

**When NOT to use:** authoring the strategy artifact itself (use
`product-strategy-canvas`), writing a one-line vision (use `product-vision`),
sizing the market (use `market-sizing`), or setting the quarter's objectives (use
`brainstorm-okrs`). This skill facilitates the conversation; those skills produce
the documents the conversation feeds. Also skip it for a routine status meeting or
a 1:1 — a facilitated multi-stakeholder session is overhead that only pays off
when a real strategic decision is contested or unmade.

## Inputs
- **Required:** the **decision the session must reach** (the strategic question on
  the table), the **participants and their roles** (who decides vs. advises), and
  the **time available**. If any is missing, ask for all three before planning —
  a session without a decision-owner and a target decision drifts into discussion
  theater. If the user only gives a vague topic ("talk about strategy"), press for
  the specific choice being made.
- **Optional:** pre-reads or prior artifacts (vision, canvas, market data —
  reference them and time-box their review), known points of disagreement or
  political constraints, format (in-person / remote / hybrid), and the DACI/RAPID
  decision model already in use. Absent a stated model, default to naming a single
  **Decider** and treating everyone else as **input**.

## Output Contract
The deliverable is a **session facilitation pack** in two parts (see
`template.md`):

**Part A — Run-of-Show (produced before the session):**
1. **Session Frame** — the decision to reach, the Decider, participants & roles, total timebox, desired end-state.
2. **Agenda / Timebox table** — ordered stages, each with a duration, goal, facilitation technique, and the key question(s) to ask.
3. **Convergence Plan** — how each divergent stage will be closed (e.g. dot-voting, disagree-and-commit, decider's call) and the escalation path if the group stalls.
4. **Pre-reads & Ground Rules** — what to send in advance and the rules that keep the room productive.

**Part B — Session Readout (produced during/after the session):**
5. **Decisions Made** — each decision, its rationale, the Decider, and the trade-off explicitly accepted.
6. **Open Questions** — unresolved items, why they're unresolved, and what would resolve them.
7. **Next Steps** — owned action items with owner + due date, and the follow-up checkpoint.

Format: two tables (agenda, next steps) plus short prose sections. Length:
~1–2 pages. Every agenda stage is timeboxed and carries a facilitation technique;
every decision names its accepted trade-off; every next step has a named owner.

**GOOD (excerpt):**
> **Stage 3 — Narrow to two bets (25 min, technique: silent write → dot-vote).**
> Q: "Which of these five directions best defends against Competitor X in 18 months?"
> Converge: each participant places 3 dots; Decider breaks any tie.
> …
> **Decision:** Pursue the SMB self-serve motion. **Trade-off accepted:** we deprioritize the top-5 enterprise logos this half. **Decider:** VP Product. **Open question:** does self-serve cannibalize the sales-led pipeline? — resolve via a 30-day pricing test.

**BAD (excerpt):**
> "Agenda: 1. Discuss strategy. 2. Decide. 3. Wrap up. Everyone should share thoughts and we'll align."
> — fails: no timeboxes, no facilitation technique, no convergence mechanism, no named Decider, no trade-offs, no owned next steps. This is a discussion, not a decision session.

## Process
1. **Establish the frame** — confirm the exact decision to reach, the Decider, the participants and their roles, and the timebox. If unclear, elicit before planning.
2. **Design the arc** — sequence stages from *context → diverge → converge → decide → commit*. Allocate the timebox so convergence and decision get real minutes, not leftovers.
3. **Attach a technique to every stage** — pair each stage with a concrete facilitation move (silent brainstorm, affinity grouping, dot-voting, 2×2 prioritization, disagree-and-commit, pre-mortem) and the specific question(s) that stage answers.
4. **Plan convergence and escalation** — for each divergent stage, state how it closes and what happens if the group stalls (timeboxed parking lot, Decider's call, deferred with a resolution path).
5. **Prepare pre-reads and ground rules** — list what to send ahead and the rules (one conversation at a time, decisions need a trade-off, "disagree and commit" is allowed) that keep the room converging.
6. **Facilitate / synthesize** — as decisions land, record each with its rationale, Decider, and the trade-off accepted; capture what stayed open and why; assign every action an owner and date.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **decision to reach** and the **Decider** are named up front — the session has a single owner of the call.
- [ ] **Every agenda stage is timeboxed** and the durations sum to the available time.
- [ ] **Every stage carries a facilitation technique** and at least one specific question to ask — no stage is just "discuss".
- [ ] The agenda arc moves from **diverge to converge to decide** — convergence is planned, not assumed.
- [ ] A **stall/escalation path** exists for the moment the group cannot agree.
- [ ] Each **decision names the trade-off accepted** and its Decider; nothing is recorded as decided without a cost.
- [ ] **Open questions** carry a resolution path, not just a restatement of the disagreement.
- [ ] **Every next step has a named owner and a due date**, plus a follow-up checkpoint.
- [ ] The readout stays a facilitation record — it does **not** try to author the strategy canvas itself (hand that to `product-strategy-canvas`).
- [ ] If the pack is written to a file, it follows `template.md` — all 7 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `product-strategy-session-happy` (happy path) — a clearly-scoped offsite deciding between two growth motions with a named Decider and fixed timebox.
- `product-strategy-session-edge` (edge) — a remote, politically-charged session with a dominant HiPPO and no agreed decision model; the plan must build in convergence and escalation safeguards.
- `product-strategy-session-adversarial` (adversarial) — a vague "let's talk strategy" ask with no decision and no Decider; the skill must refuse to plan a decision session until it elicits the frame.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `product-strategy-canvas` — the strategy *artifact* a good session feeds; this skill runs the human meeting, the canvas skill writes the document.
- `product-vision` — a vision pre-read anchors the session's context stage.
- `brainstorm-okrs` — the downstream skill that turns session decisions into a quarter's objectives.

### External Frameworks
- **DACI / RAPID** decision-rights models (Intuit; Bain) — naming a single Decider vs. input/advise roles, the backbone of this skill's convergence plan.
- **Liberating Structures** (Lipmanowicz & McCandless) — the timeboxed facilitation moves (1-2-4-All, dot-voting, silent-write-then-share) attached to each agenda stage.
- Gary Klein, *pre-mortem* technique (HBR, 2007) — the risk-surfacing move used in the converge/decide stages to stress-test a candidate strategy before committing.
