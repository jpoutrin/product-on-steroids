---
name: wwas
description: >
  Draft a shipping/commitment document describing exactly what ships in a sprint
  or release—product features, scope, and acceptance criteria in structured format.
  Use when finalizing sprint scope, communicating release contents, writing a
  shipping brief, or committing to delivery timelines.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/wwas/template.md
---

# What We Are Shipping (WWAS)

## Purpose
Produce a concise, structured **shipping commitment document** that clearly
defines what is included (in scope) and explicitly excludes what is not—the
exact deliverable set for a sprint or release. Eliminates ambiguity about
scope, sets clear team expectations, and provides a communication tool for
stakeholders. Supports sprint planning, release coordination, and post-delivery
accountability.

**When NOT to use:** high-level roadmap planning (use `roadmap` or `okr-planning`),
retrospectives or post-mortems (use `pre-mortem` or retro templates),
detailed feature specifications (use `create-prd`), or individual user
stories (use `job-stories` or backlog-item templates).
WWAS aggregates *what* ships; it does not specify *how* to build it.

## Inputs
- **Required:** the product/sprint/release name, the set of features or
  capabilities shipping (links to designs, PRDs, or issue trackers).
- **Optional:** target date, team(s) involved, known dependencies, personas
  or user segments affected, success metrics or key results tied to the release.

## Output Contract
The deliverable is a **shipping commitment document** with these sections
(see `template.md`):

1. **Shipping Period** — sprint name/number or release version, dates, target audience/teams.
2. **In Scope** — a bulleted list of each feature/capability shipping, with a
   1–2 sentence summary and a link to design/spec (Figma, GitHub issue, PRD,
   or equivalent). Each item is independently shippable.
3. **Out of Scope** — major features or known nice-to-haves explicitly *not*
   shipping; 1–2 sentences explaining why (timeline, dependency, priority).
4. **Acceptance Criteria** — what constitutes "shipped": code merged, tested,
   deployed to production, docs updated, support briefed, stakeholders notified, etc.
5. **Key Dependencies** — any upstream/downstream work, APIs, or external
   integrations that this release depends on; risk/mitigation for each.
6. **Stakeholder Checklist** — sign-offs or communication touches needed
   (legal, support, design, marketing, finance); who owns each.

Format: structured prose with checklists. Length: 1–3 pages (typically one page
per sprint, 1–2 for major releases). Every item is independently understandable
and traceable to a source (Figma link, GitHub issue, Jira ticket, PRD).

**GOOD (excerpt):**
> **In Scope:**
> - Real-time spending tracker: users see spending updated within 2s of logging
>   an expense. [Figma link] [GitHub issue #1234]
> - Budget alerts: users receive in-app notifications when spending exceeds 80%
>   of monthly budget. [PRD Section 3.2]
>
> **Out of Scope:**
> - SMS/email notifications (defer to Q3 per priority ranking) — tech spike
>   scheduled for next sprint.
> - Multi-currency support (single-currency MVP this release to reduce risk).

**BAD (excerpt):**
> "We are shipping the budget feature. It will have spending tracking and alerts."
> — fails: no links to design/specs, no per-item clarity, acceptance criteria
>   missing, scope boundaries vague.

## Process
1. **Gather the feature/item list** — collect links to all shipping features
   (GitHub issues, PRD sections, Figma links, or equivalent).
2. **Define in-scope clearly** — for each feature, write a 1–2 sentence
   "what" (not "how"); include the link.
3. **List out-of-scope explicitly** — what major features or user asks are *not*
   shipping; explain the trade-off (timeline, priority, risk).
4. **Set acceptance criteria** — what does "done" mean: merged, tested, deployed,
   docs live, support briefed, legal approved, etc.
5. **Map dependencies** — upstream work, third-party APIs, or external events
   this release depends on; note risks.
6. **Create a stakeholder checklist** — who needs to sign off or be notified
   (support, marketing, legal, design, finance); mark owner for each.
7. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Each in-scope item has a 1–2 sentence description (what will ship, not how).
- [ ] Each in-scope item **links to a source** (Figma, GitHub, PRD, or Jira).
- [ ] Out-of-scope items are **explicitly listed** with a clear reason (timeline, priority, dependency, risk).
- [ ] Acceptance criteria are **concrete and testable** — not vague ("quality" is unclear; "no P0 bugs" is clearer).
- [ ] All major **dependencies are named** with risk and mitigation.
- [ ] A **stakeholder checklist** exists with clear owners and sign-off criteria.
- [ ] The document is **self-contained** — a reader unfamiliar with the sprint can understand scope and trade-offs.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`: happy + edge + adversarial.
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `create-prd` — detailed product specification for a single feature; consumes one in-scope item from WWAS.
- `job-stories` — individual user-story format; multiple job stories roll up to a WWAS in-scope item.
- `pre-mortem` — identify and mitigate risks for the release; complements WWAS dependencies and acceptance criteria.
- `brainstorm-okrs` — high-level objectives; WWAS is the tactical "what ships" that delivers against an OKR.

### External Frameworks
- Atlassian, *Agile Coach — Sprint Planning* — sprint scope-setting and commitment practices.
- Roman Pichler, *Agile Product Management with Scrum* (2010) — sprint backlog as the "contract" between team and stakeholders.
- Jeff Patton, *User Story Mapping* (2014) — organizing features into releases by user workflow and priority.
