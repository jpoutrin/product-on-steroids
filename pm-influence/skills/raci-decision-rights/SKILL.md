---
name: raci-decision-rights
description: >
  Use when you need to clarify who owns, approves, or is consulted on recurring
  decisions for a product area or initiative — especially before a launch,
  reorg, or when escalations keep happening on the same topics.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/raci-decision-rights/template.md
---

# RACI Decision-Rights Matrix

## Purpose
Produce a RACI (Responsible, Accountable, Consulted, Informed) matrix that makes
explicit who owns each recurring decision in a product area or initiative — before
ambiguity causes missed launches, duplicated work, or escalation loops. The output
is an actionable reference teams can socialize, align on, and revisit at milestone
boundaries.

**When NOT to use:**
- **Stakeholder mapping** (use `stakeholder-map`): if the goal is to understand
  stakeholder power/interest dynamics and engagement strategy, not decision ownership.
- **Single-decision memos** (use `decision-memo`): if you are driving one specific
  decision right now and need a recommendation + rationale, not a governance framework.
- **Unblocking a stuck decision** (use `escalation`): if a specific decision has
  already stalled and needs an escalation path — RACI prevents that proactively; it
  does not unblock decisions that are already stuck.
- **Org design / reporting lines**: RACI clarifies decision authority, not headcount
  or hierarchy. Do not use it to redraw org charts.

## Inputs
- **Required:** the product area or initiative scope — name, boundaries, and any
  known pain points (e.g., "pricing decisions always get escalated to the CEO").
  If this is missing, ask before proceeding; the decision list is scope-dependent.
- **Required:** the roles or functions that participate in decisions (PM, Eng Lead,
  Design Lead, Data, Legal, Finance, Marketing, etc.). If the user only provides
  names, convert them to roles.
- **Optional:** a list of specific decisions to cover. If absent, derive a canonical
  set from the scope (see Process step 2).
- **Optional:** team size / org maturity signal — early-stage startups often need
  thinner RACIs (fewer consulted parties) than large enterprises.
- **Optional:** format preference — table vs. narrative. Default: table.

## Output Contract
The deliverable is a **RACI decision-rights matrix** with these sections (see
`template.md`):

1. **Scope & Context** — the product area or initiative name, boundaries, the
   problem this RACI solves, and any scoping decisions made.
2. **Role Glossary** — each role in the matrix, one-line description, and the
   person/team currently filling it (if known).
3. **Decision-Rights Matrix** — a table with decisions as rows and roles as columns;
   each cell is R, A, C, I, or blank. Every row must have exactly one A; every row
   must have at least one R. Include a legend below the table.
4. **Decision Notes** — a numbered list of brief notes for any decision with unusual
   assignments, known tensions, or important caveats (e.g., "Legal must be consulted
   before any pricing change that touches EU customers").
5. **Operating Cadence** — how and when the matrix is reviewed/updated (default:
   quarterly or at major milestone boundaries), and who owns the review.
6. **Known Gaps & Risks** — any decisions the team raised that could not be cleanly
   assigned, roles that are over-loaded (too many A entries), or missing roles.

Format: prose intro + role glossary + one table + numbered notes + short prose for
sections 5–6. Length: ~1–2 pages. Every A is a single role; no shared accountabilities.

**GOOD (excerpt):**
> | Pricing change (< 10 %) | R | A |   | C | I |
> | Pricing change (≥ 10 %) |   | C | R | C | I |
>
> *Note 3: Pricing changes ≥ 10% are Accountable to the VP Product (not PM) because
> they require board visibility. PM remains Responsible for the analysis and proposal.*

**BAD (excerpt):**
> | Pricing change | PM / VP Product | Legal |
> — fails: shared A violates the single-accountability rule; columns are not RACI
> roles; no distinction between change thresholds.

## Process
1. **Confirm scope** — restate the product area/initiative and its boundaries; note
   any explicit out-of-scope decisions. Ask for clarification if scope is ambiguous.
2. **Enumerate decisions** — list 8–15 recurring decision types in the area. Group
   by category if useful (e.g., roadmap, pricing, engineering, launch). If the user
   provided a list, validate completeness; add obvious gaps and flag them.
3. **Enumerate roles** — list every function that participates. Collapse synonymous
   titles to canonical roles. Flag any roles that appear in the discussion but are
   not represented on the team.
4. **Assign RACI** — for each decision × role cell:
   - **R (Responsible):** does the work / drives the decision analysis. ≥ 1 per row.
   - **A (Accountable):** owns the outcome; approves the final decision. Exactly 1 per row.
   - **C (Consulted):** must be asked and heard before a decision is finalized (two-way).
   - **I (Informed):** notified after a decision is made (one-way).
   - Blank if the role has no involvement.
5. **Apply discipline rules:**
   - Reject shared A: if the user wants "PM and VP Product are both accountable," clarify
     who is the final approver and move the other to C or R.
   - Flag over-consulted rows: more than 3–4 C entries on a single decision is a
     governance smell — note it.
   - Check for missing R: a decision with only C and I entries has no owner; flag it.
6. **Write Decision Notes** — annotate decisions where the assignment may surprise
   stakeholders or where the user flagged tension.
7. **Set Operating Cadence** — propose a review schedule and owner.
8. **Surface Gaps & Risks** — note any decisions that could not be cleanly assigned
   or roles that are consistently over-loaded.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every decision row has **exactly one A** (single accountability; no shared A).
- [ ] Every decision row has **at least one R** (someone is doing the work).
- [ ] The matrix covers **all decisions the user raised**; any omissions are
  explained in Gaps & Risks.
- [ ] The **Role Glossary** defines every column in the matrix.
- [ ] **Decision Notes** exist for any assignment that is non-obvious or was
  contested.
- [ ] No role has A on more than ~30% of decisions without an explicit note — this
  signals a bottleneck.
- [ ] **Operating Cadence** names a review schedule and an owner.
- [ ] If the output is written to a file, it follows `template.md` — all 6 sections
  present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `raci-decision-rights-happy` (happy path) — mid-stage SaaS PM building a RACI
  for a new checkout feature team with clear roles and a mixed set of decisions.
- `raci-decision-rights-edge` (edge) — early-stage startup where founders fill
  multiple roles; the skill must handle role overlap and thin consulted sets.
- `raci-decision-rights-adversarial` (adversarial) — request to assign shared
  accountability; the skill must surface the problem and propose a single A owner.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `stakeholder-map` — maps stakeholder influence and interest; complements the
  role list here but does not assign decision authority.
- `decision-memo` — drives one specific decision; use RACI output as governance
  context when writing a memo.
- `escalation` — handles a decision already stuck; a well-maintained RACI prevents
  most escalations by pre-assigning authority.
- `alignment-narrative` — communicates a decision outcome to stakeholders; the
  RACI's I column is the audience list.

### External Frameworks
- Rasci, *Responsibility Assignment Matrix* (RACI/RASCI) — original methodology;
  the single-A rule and C vs. I distinction come from the canonical RACI literature.
- Patrick Lencioni, *The Five Dysfunctions of a Team* — accountability gaps and
  avoidance are the root cause this skill addresses.
- Amazon's *PRFAQ / Working Backwards* — decision rights are clarified early in
  the product process; aligns with the "who decides" discipline in the Amazon model.
