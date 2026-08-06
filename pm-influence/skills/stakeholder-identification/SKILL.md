---
name: stakeholder-identification
description: >
  Discover all relevant stakeholders — including non-obvious ones — for a
  product initiative and produce a raw stakeholder inventory with role,
  function, and rationale for inclusion. Use when starting a new initiative,
  kicking off a planning cycle, preparing a stakeholder map, or whenever the
  question is "who needs to be in the room?"
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/stakeholder-identification/template.md
---

# Stakeholder Identification

## Purpose
Produce a complete stakeholder inventory — a raw, role-by-role list of every
person or group that the initiative affects, depends on, or must comply with.
This inventory is the essential input for stakeholder mapping and engagement
planning; it surfaces non-obvious stakeholders (legal, security, data,
finance, customer success, regulators) that are routinely missed in early
discovery.

The output is deliberately a *flat list, not a map*. Mapping (influence vs
interest grid, stance scoring) and engagement strategy come next, in separate
skills.

**When NOT to use:**
- You already have a stakeholder list and want to map it → use `stakeholder-map`.
- You know who the stakeholders are and want to plan how to engage them → use `stakeholder-engagement-advisor`.
- The ask is a RACI or decision-rights matrix, not a discovery exercise → use `raci-decision-rights`.
- The scope is a single meeting or a narrow tactical ask where a one-line "who to invite" suffices.

## Inputs
- **Required:** initiative or product name and a one-sentence description of
  what it changes, delivers, or decides. If absent, ask: "What is the
  initiative and what will it change or decide?" Do not proceed without this.
- **Required:** organizational context — company size / structure, whether the
  initiative is internal-facing, customer-facing, or mixed. If absent, ask a
  single clarifying question: "Is this initiative internal, customer-facing, or
  both, and roughly how large is the organization?"
- **Optional:** known stakeholder names or teams already identified — used as
  seeds, not as the complete list; the skill still scans for gaps.
- **Optional:** regulatory or compliance context (industry sector, geographic
  markets, data sensitivity) — triggers inclusion of legal, privacy, security,
  and regulatory bodies when relevant.
- **Optional:** explicit exclusions (teams or roles confirmed out of scope) —
  noted in the output but not re-surfaced as candidates.

## Output Contract
The deliverable is a **stakeholder inventory** structured as (see `template.md`):

1. **Initiative Summary** — one sentence restating scope and change; confirms
   the lens through which stakeholders were identified.
2. **Stakeholder Inventory Table** — rows are individual stakeholders or groups,
   columns: Role/Title, Function/Team, Why Included (one line), Category
   (sponsor / decision-maker / contributor / affected party / gatekeeper /
   external). Each row is atomic: no merged "leadership" catch-alls.
3. **Non-Obvious Stakeholders — Callout** — a short bulleted section highlighting
   stakeholders beyond the obvious product + engineering core, with one-line
   rationale for each. This is the section reviewers check for depth.
4. **Gaps & Uncertainties** — open questions: roles that may exist but could not
   be confirmed, dependencies not yet scoped, regulatory bodies that need
   validation.

Format: markdown table + prose callout + bullet list. Length: as long as the
inventory requires; never pad with generic text.

**GOOD (excerpt):**
> | Legal Counsel | Legal | Data-sharing clause in partner contract requires sign-off | gatekeeper |
> | Customer Success Lead | CS | Manages accounts most affected by the pricing change; needs comms runway | affected party |
>
> **Non-Obvious Stakeholders:**
> - **Security Engineering** — new API surface introduces auth scope changes; must review before launch.
> - **Finance / FP&A** — pricing change triggers revenue-recognition implications; must sign off on model.

**BAD (excerpt):**
> "Key stakeholders: Product, Engineering, Sales, Leadership."
> — fails: no individual roles, no non-obvious functions, no rationale for
> inclusion, no categories, no gaps flagged.

## Process
1. **Restate the initiative** — confirm scope, change, and affected customer or
   user segment. Surface any ambiguity before proceeding.
2. **Seed from the obvious core** — identify direct owners: product, engineering,
   design, and the business sponsor or executive champion.
3. **Scan the non-obvious rings** — systematically walk through each function
   below and ask "does this initiative touch them?":
   - **Go-to-market:** Sales, Marketing, Customer Success, Solutions Engineering,
     Partnerships.
   - **Risk & compliance:** Legal, Security, Privacy / Data Protection, Finance,
     Audit, Risk.
   - **Operations:** IT / Infra, Data / Analytics, Support, Procurement.
   - **Governance:** Executives, Board (for material changes), Steering committees.
   - **External:** Regulators, Key customers / customer advisory boards, Vendors,
     Integration partners.
4. **Apply the regulatory / compliance filter** — if a regulated industry, data
   sensitivity flag, or cross-border scope was supplied, add relevant gatekeepers
   (DPO, CISO, compliance officer, external regulator).
5. **Validate completeness** — for each stakeholder listed, confirm: "Who approves?
   Who is blocked by this? Who has to do work because of this? Who bears the risk?"
   Fill gaps surfaced by these questions.
6. **Classify each stakeholder** — assign one category: sponsor, decision-maker,
   contributor, affected party, gatekeeper, external.
7. **Write the Non-Obvious Callout** — extract the ≥ 3 most surprising or
   commonly-missed stakeholders and write one-line rationale for each.
8. **List Gaps & Uncertainties** — name roles not yet confirmed, dependencies not
   yet scoped, and any regulatory bodies requiring validation.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every row in the inventory names an **individual role or named group** — no catch-all rows like "Leadership" or "Stakeholders."
- [ ] Each row has a **one-line rationale** explaining why this person or group is included.
- [ ] Each stakeholder is assigned exactly **one category** (sponsor / decision-maker / contributor / affected party / gatekeeper / external).
- [ ] The **non-obvious rings** (legal, security, finance, CS, data, ops, external) were explicitly scanned — at least one finding from each relevant ring is present or its absence is explained.
- [ ] The **Non-Obvious Callout** contains ≥ 3 entries with distinct rationale lines (not rephrases of the same point).
- [ ] **Gaps & Uncertainties** contains at least one open question — inventories without open questions are almost always incomplete.
- [ ] No stakeholder is listed twice under different names.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `stakeholder-identification-happy` — a concrete B2B SaaS pricing-change initiative; guards baseline completeness and non-obvious coverage.
- `stakeholder-identification-edge` — a purely-internal data-platform migration; guards against skipping external rings correctly and surfacing data-governance stakeholders.
- `stakeholder-identification-adversarial` — vague ask ("who are the stakeholders for our product?") with no scope; guards against producing a generic list without first scoping the initiative.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `stakeholder-map` — takes the inventory produced here and plots stakeholders on an influence × interest grid with stance scoring.
- `stakeholder-engagement-advisor` — designs the engagement cadence and communication approach for stakeholders once they are identified and mapped.
- `raci-decision-rights` — defines decision-making authority across the stakeholder set; presupposes an identified stakeholder list.

### External Frameworks
- Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK)*, Chapter 13 — canonical stakeholder identification process and registry format.
- R. Edward Freeman, *Strategic Management: A Stakeholder Approach* (1984) — foundational definition of stakeholders as "any group or individual who can affect or is affected by the achievement of the organization's objectives."
- Ackermann & Eden, "Stakeholder Management: The Lens of Ecology" — the "power, interest, dynamism" extension that motivates scanning beyond the immediate project team.
