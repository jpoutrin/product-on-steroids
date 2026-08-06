---
name: create-prd
description: >
  Author the content of a Product Requirements Document covering problem framing,
  objectives, segments, value propositions, solution, and release planning. Use
  when writing a new PRD, drafting a feature spec, turning discovery findings into
  a requirements document, or reviewing and enriching an existing PRD.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/create-prd/template.md
---

# Create a Product Requirements Document

## Purpose
Produce the written content of a PRD — a structured artifact that aligns
engineers, designers, leadership, and stakeholders on what to build, for whom,
why, and how success is measured. The eight sections cover the full arc from
problem context through release planning.

**When NOT to use:** PRD lifecycle management (status tracking, archival,
linking to tasks) belongs to Forge's PRD tooling — do not overlap. This skill
writes PRD *content*, not metadata. For market-size estimates, use
`market-sizing`. For OKR-only work, use an OKR skill. For competitive teardowns,
use `competitor-analysis`.

## Inputs
- **Required:** initiative name and the problem being solved — at minimum one
  sentence each. If the user provides neither, ask before writing; do not invent
  scope.
- **Required:** target customer or user type — broad segment is fine. Ask if
  completely absent.
- **Optional:** success metrics / OKR targets — default to placeholder language
  ("to be validated") if not supplied; flag them for the team to complete.
- **Optional:** attached research, briefs, URLs, or conversation transcripts —
  read and cite any provided material.
- **Optional:** release constraints (team size, timeline, phasing preferences).

## Output Contract
The deliverable is a **PRD document** with these eight sections (see
`template.md`):

1. **Summary** — 2–3 sentences: what the initiative is, why it matters now.
2. **Contacts** — key stakeholders: name, role, and accountability note.
3. **Background** — context, change/trigger that makes this timely, and why the
   moment is right.
4. **Objective** — strategic rationale, company and customer benefit, alignment
   to vision/strategy, and 1–3 SMART key results (OKR format).
5. **Market Segment(s)** — who the primary and secondary audiences are, defined
   by job-to-be-done or pain, not demographics alone; constraints listed.
6. **Value Proposition(s)** — customer jobs addressed, gains delivered, pains
   avoided, and differentiation from the current best alternative.
7. **Solution** — four subsections: UX/Prototypes (flows or wireframe notes),
   Key Features (descriptions with scope notes), Technology (only if
   non-obvious), Assumptions (explicit beliefs not yet validated).
8. **Release** — phasing in relative terms (MVP vs. future iterations), scope
   tradeoffs, and how the team will know v1 is ready to ship.

Format: Markdown with `##` and `###` headings matching `template.md`. Length:
1–3 pages. Every assumption is labeled; every metric has a placeholder or a
source. Use plain, concrete language — assume a non-specialist reader.

**GOOD (excerpt):**
> **Objective:** Reduce checkout abandonment for mobile users by 20% within two
> quarters, increasing monthly revenue by €40k (KR: cart-completion rate ≥ 72%
> on mobile, measured in GA4).
>
> **Key Features:** *One-tap address autofill* — uses the stored address from
> the user's account; eliminates the 4-field form on mobile. In scope for v1.

**BAD (excerpt):**
> "We want to improve the user experience significantly to drive revenue growth."
> — fails: no measurable target, no feature specifics, no segment, no
> differentiation.

See `template.md` for the fill-in structure.

## Process
1. **Read inputs** — ingest any provided files, briefs, or URLs; note gaps.
2. **Ask for blockers** — if initiative name, problem, or customer type are
   missing, ask for them before writing.
3. **Draft Summary and Background** — anchor every claim to provided context;
   flag anything inferred.
4. **Draft Objective and Key Results** — use SMART OKR format; mark
   unconfirmed metrics with `[TBD — validate with data team]`.
5. **Draft Segments and Value Propositions** — frame segments by
   jobs-to-be-done; list pains and gains concretely.
6. **Draft Solution** — write features as capability statements with scope
   boundaries; call out assumptions explicitly.
7. **Draft Release section** — phase in relative terms; avoid calendar dates
   unless the user supplied them.
8. **Save to file** — name the file `PRD-[initiative-name].md`; the PostToolUse
   hook will validate conformance to `template.md`.
9. Run the Quality Bar below; revise any failing item before returning.

## Quality Bar
Before returning, confirm:
- [ ] All eight sections are present and headings match `template.md` exactly.
- [ ] Summary is ≤ 3 sentences and states what, why, and why now.
- [ ] Objective includes at least one SMART key result with a measurable target
  and timeframe.
- [ ] Segment(s) are defined by job or pain, not demographics alone.
- [ ] Value Proposition names at least one specific pain avoided and one gain
  delivered.
- [ ] Solution subsection "Assumptions" lists at least one explicit belief to
  validate.
- [ ] Release section uses relative timeframes (not calendar dates) unless the
  user provided a date.
- [ ] Language is clear and jargon-free — a non-specialist can read it without
  a glossary.
- [ ] Every unconfirmed metric or placeholder is labeled `[TBD]`.
- [ ] The file is saved as `PRD-[initiative-name].md` following `template.md`
  (the skill-scoped PostToolUse hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `create-prd-happy` — well-specified B2B SaaS feature with clear segment,
  success metrics, and release phasing.
- `create-prd-edge` — sparse brief: only a product name and a vague problem;
  skill must elicit missing inputs and produce a valid draft.
- `create-prd-adversarial` — user requests a PRD but conflates content authoring
  with PRD lifecycle status updates; skill must write content only and redirect
  lifecycle management to Forge tooling.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — size the addressable market before or alongside defining
  segments; feeds the Background and Objective sections.
- `competitor-analysis` — competitive differentiation data feeds the Value
  Proposition section.
- `user-stories` — decompose PRD features into user stories once the PRD is
  approved.
- `pre-mortem` — run a pre-mortem on the solution section before committing
  to build.

### External Frameworks
- Paweł Huryn, [*How to Write a Product Requirements Document? The Best PRD Template*](https://www.productcompass.pm/p/prd-template) — the 8-section structure this skill is built on.
- Paweł Huryn, [*A Proven AI PRD Template by Miqdad Jaffer (Product Lead @ OpenAI)*](https://www.productcompass.pm/p/ai-prd-template) — AI-era PRD writing conventions.
- Clayton Christensen, *Competing Against Luck* (2016) — Jobs-to-be-Done framing for segments and value propositions.
- Christina Wodtke, *Radical Focus* (2016) — SMART OKR format referenced in the Objective section.
