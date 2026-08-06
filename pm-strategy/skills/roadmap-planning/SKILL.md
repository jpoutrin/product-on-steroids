---
name: roadmap-planning
description: >
  Run the roadmap-planning process — set a planning cadence, allocate capacity
  across themes, sequence work against dependencies and risk, gather stakeholder
  inputs, and establish a review rhythm to produce a committed roadmap plan. Use
  when planning a quarter or half, allocating engineering capacity across bets,
  sequencing a backlog under dependencies, resetting a planning cadence, or
  preparing a roadmap review.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/roadmap-planning/template.md
---

# Plan a Roadmap (Cadence, Capacity, Sequencing & Review)

## Purpose
Run the **planning process** that turns strategy and a backlog into a committed,
sequenced roadmap plan for a defined horizon: pick a cadence, split available
capacity across themes/bets, order the work so dependencies and risks are retired
early, fold in stakeholder inputs, and set the review rhythm that keeps the plan
honest as reality moves. The output supports a go-forward commitment for the next
1–2 planning periods and a clear "why this order" rationale.

**When NOT to use:** designing the outcome/now-next-later *artifact* or its
narrative framing (use `outcome-roadmap`); prioritizing a single backlog by
score (use a prioritization skill); estimating market opportunity (use
`market-sizing`); or writing a strategy from scratch (use `product-vision` /
`product-strategy`). This skill assumes goals exist and plans the *execution of
them over time*; it does not invent the goals or render the shareable artifact.

## Inputs
- **Required:**
  - **Planning horizon & cadence anchor** — the period to plan (e.g., next
    quarter, next half) and how often the plan is re-cut. If missing, ask which
    horizon and default the cadence to quarterly planning with a monthly review.
  - **Strategic themes / objectives** — the 2–5 bets or goals the roadmap must
    serve. If absent, ask for them; do not invent strategy — decline and hand off
    to `product-strategy`.
  - **Team capacity** — team size / squad count and any known reductions (leave,
    hiring lag, on-call, KTLO tax). If unknown, ask; do not assume 100% is
    available for new work.
- **Optional:** the current backlog or candidate items, known dependencies
  (internal teams, vendors, platform work), fixed dates (compliance, contractual,
  events), risk register, and stakeholder list. Absent a backlog, plan at the
  theme/capacity level and flag that item-level sequencing is deferred.

## Output Contract
The deliverable is a **roadmap plan** with these sections (see `template.md`):

1. **Planning Frame** — horizon, cadence (planning + review), and the 2–5 themes
   the roadmap serves, each tied to a strategic objective.
2. **Capacity Allocation** — total available capacity for the horizon (after KTLO,
   on-call, leave), split across themes as an explicit **% or headcount table**;
   allocation must sum to available capacity, not to 100% of raw headcount.
3. **Sequenced Plan** — the ordered work per period (e.g., by month or sprint
   band), with the **sequencing rationale** (why this order) stated for each major
   item — dependency, risk-retirement, or value.
4. **Dependencies & Risks** — a table of blocking dependencies (owner, needed-by)
   and top risks (likelihood/impact + mitigation or the step that retires them);
   risk-heavy work is scheduled to be de-risked early, not last.
5. **Stakeholder Inputs** — who was consulted (eng, design, sales, support,
   leadership), the trade-offs/asks they raised, and how each was resolved
   (accepted / deferred / declined + reason).
6. **Review Rhythm** — the recurring checkpoints (cadence, attendees, decision the
   review can make: hold / re-sequence / re-scope) and the trigger conditions that
   force an off-cycle replan.

Format: prose + at least the capacity table and the dependency/risk table.
Length: ~1–2 pages. Every allocation reconciles to stated capacity; every
sequencing choice names its reason.

**GOOD (excerpt):**
> **Capacity (Q3):** 5 squads × 12 wks = 60 squad-weeks; −15 KTLO, −8 on-call/leave
> = **37 available**. Themes: Activation **19 (51%)**, Retention **11 (30%)**,
> Platform-debt **7 (19%)** → sums to 37.
> **Sequence:** Month 1 — *SSO migration* first (retires the vendor-API dependency
> that blocks 3 activation stories; de-risk early). Month 2 — activation onboarding
> flow (unblocked once SSO lands).

**BAD (excerpt):**
> "Q3: ship onboarding, SSO, dashboards, and billing. Team is 5 squads."
> — fails: no capacity math (allocation never subtracts KTLO or sums to available),
> no sequencing rationale, dependencies (SSO→onboarding) and risks unstated, no
> review rhythm.

## Process
1. **Set the frame** — confirm horizon and cadence (planning period + review
   interval); restate the 2–5 themes and the objective each serves.
2. **Compute available capacity** — start from raw headcount/squad-weeks, subtract
   KTLO, on-call, leave, and hiring lag to get *available* capacity; never plan
   against raw headcount.
3. **Allocate to themes** — split available capacity across themes as an explicit
   table; confirm the split reflects strategic weight and sums to available.
4. **Map dependencies & risks** — list blocking dependencies (owner, needed-by)
   and top risks (likelihood/impact); mark which work items each touches.
5. **Sequence** — order work per period so dependencies unblock downstream items
   and risk-heavy/uncertain work is scheduled to be de-risked early; record the
   reason for each major placement.
6. **Fold in stakeholder inputs** — capture eng/design/GTM/leadership asks and
   trade-offs; resolve each (accept / defer / decline) with a reason.
7. **Set the review rhythm** — define checkpoints, attendees, the decisions each
   review can make, and the triggers that force an off-cycle replan.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Cadence is explicit: both a **planning period** and a **review interval** are named.
- [ ] Available capacity is derived by **subtracting KTLO/on-call/leave** from raw headcount — not assumed to be 100%.
- [ ] Capacity is allocated across themes in a table that **sums to available capacity**, with each theme tied to an objective.
- [ ] Every major sequenced item states a **reason** (dependency, risk-retirement, or value) — order is justified, not arbitrary.
- [ ] Blocking **dependencies** have an owner and a needed-by; risk-heavy work is **de-risked early**, not deferred to the end.
- [ ] **Stakeholder inputs** are recorded with an accept/defer/decline resolution and reason for each.
- [ ] A **review rhythm** with checkpoints, attendees, allowable decisions, and off-cycle replan triggers is defined.
- [ ] If the plan is written to a file, it follows `template.md` — all 6 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `roadmap-planning-happy` (happy path) — a quarter with clear themes, capacity,
  and a dependency chain to sequence around.
- `roadmap-planning-edge` (edge) — capacity crunch (heavy KTLO + a hiring gap)
  where the split must reconcile to a shrunken available capacity and cut scope.
- `roadmap-planning-adversarial` (adversarial) — a stakeholder demands a fixed
  date-and-scope commitment with no capacity data; the skill must refuse to
  fabricate a plan and elicit capacity/cadence first.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `outcome-roadmap` — renders the shareable now/next/later artifact; consumes the
  sequenced plan and theme allocation this skill produces.
- `product-strategy` — supplies the objectives and themes this planning process
  allocates capacity against.
- `market-sizing` — opportunity sizing that can weight how much capacity a theme
  earns.

### External Frameworks
- Marty Cagan, *Inspired* / *Empowered* — outcome-over-output planning and the
  KTLO / discovery tax that this skill subtracts before allocating capacity.
- Melissa Perri, *Escaping the Build Trap* — the product operating cadence
  (strategy → planning → review) that motivates the cadence-and-review-rhythm frame.
- Basecamp, *Shape Up* — fixed-time / variable-scope appetite and the betting-table
  cadence that inform the capacity-first, period-based sequencing here.
