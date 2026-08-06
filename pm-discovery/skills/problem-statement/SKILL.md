---
name: problem-statement
description: >
  Craft a crisp, evidence-backed problem statement that frames the problem space
  without prescribing a solution. Use when kicking off a discovery sprint,
  writing the problem section of a PRD, aligning stakeholders on what we are
  solving, or distilling research insights into a shareable written artifact.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/problem-statement/template.md
---

# Craft a Problem Statement

## Purpose
Produce a short, written artifact (1–3 paragraphs or a structured block) that
makes the problem space legible and aligned across stakeholders. A good problem
statement answers four questions in plain language: Who experiences the problem?
What is the problem and when does it occur? Why does it matter (what is the
measurable or qualitative impact)? What evidence do we have?

It is the canonical input to PRD headers, sprint kickoffs, design briefs, and
executive updates. It is not a solution, a feature request, or a How Might We
brainstorm — those come after.

**When NOT to use:**
- You need to *uncover* the underlying motivation driving a behaviour — use
  `jobs-to-be-done` first, then come back here to crystallise the insight.
- You are running a structured workshop to explore the full problem landscape —
  use `problem-framing-canvas` (a larger artifact with multiple lenses).
- You already have a well-defined problem and need to spec the solution — go
  straight to `create-prd` or `create-prd-feature`.
- The user is asking for a root-cause investigation (5 Whys, fishbone) — that is
  a different analytical task, not a communication artifact.

## Inputs
- **Required:** a description of the user segment and the problem they face,
  even if rough. If missing, ask: "Who is experiencing this problem, and what
  are they trying to do when it occurs?"
- **Required:** at least one piece of supporting evidence (quote, metric, survey
  finding, support-ticket volume, etc.). If the user has none, note that the
  statement is hypothesis-grade and flag it prominently.
- **Optional:** the context or trigger (the situation in which the problem
  occurs). Defaults to leaving context implicit if not provided.
- **Optional:** a desired outcome or success direction (what changes if we solve
  it). Used to shape the Impact section; omit if purely exploratory.
- **Optional:** explicit out-of-scope notes. If not provided, derive reasonable
  boundaries from the problem description.

## Output Contract
The deliverable is a **problem statement document** with these sections (see
`template.md`):

1. **Problem Statement** — the core 2–3 sentence statement in the canonical
   form: *"We have observed that [user segment] [experiences problem] when
   [context]. The impact is [measurable or qualitative effect]. We believe
   [addressing it] will [desired outcome]."* Must be falsifiable, free of
   solution language, and written so a non-expert reader immediately grasps
   the stakes.
2. **User Affected** — one or two sentences identifying the user segment, their
   relevant goal, and how prevalent or representative they are (% of user base,
   cohort size, persona name if applicable).
3. **Evidence** — a bullet list of 1–5 data points or qualitative signals that
   substantiate the problem. Each bullet names the source type (e.g., user
   interview, NPS comment, analytics event, support ticket). Mark as
   "hypothesis — validate" if evidence is weak or absent.
4. **Impact** — what happens if we do nothing: business impact (churn, lost
   revenue, NPS drag) and/or user impact (time lost, workaround cost, frustration
   level). Include a metric or an order-of-magnitude estimate where possible.
5. **Out of Scope** — 2–4 bullets stating explicitly what this problem statement
   does *not* cover, to prevent scope creep in downstream work.

Format: structured Markdown, short. The entire document should fit on one page
(roughly 300–500 words). Avoid jargon; write for a mixed audience of engineers,
designers, and business stakeholders.

**GOOD (excerpt):**
> **Problem Statement**
> We have observed that B2B account managers lose track of which customer
> commitments remain unfulfilled when juggling more than three active accounts.
> The impact is that ~22% of renewal conversations surface a missed commitment
> discovered too late to act on, contributing to a 6-point NPS drop in the
> "Enterprise" tier. We believe surfacing pending commitments proactively will
> reduce missed-commitment incidents by at least half, measurable in the next
> renewal cohort.

**BAD (excerpt):**
> "Users want a dashboard to see their tasks."
> — fails: solution language ("dashboard"), no segment, no evidence, no impact,
> not falsifiable.

## Process
1. **Clarify the essentials** — confirm user segment, problem trigger/context,
   and at least one evidence signal. If any are missing, ask before proceeding;
   do not invent them.
2. **Draft the core statement** — write the 2–3 sentence canonical statement
   first. Test it: is it falsifiable? Does it mention a solution? If yes, remove
   the solution language.
3. **Populate User Affected** — name the segment and its goal; add prevalence if
   known.
4. **List Evidence** — pull in what the user supplied; label each bullet with
   its source type. If evidence is thin, add the "hypothesis — validate" flag.
5. **Quantify Impact** — translate the problem into business or user cost. Use
   the user's data; if none provided, state the impact direction and flag the
   need for measurement.
6. **Define Out of Scope** — derive 2–4 explicit exclusions from the problem
   description to prevent downstream scope creep.
7. **Sanity-check distinctness** — confirm the statement frames the problem, not
   a solution, and does not overlap with adjacent problem spaces named in the
   context.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The core statement names a user segment, a problem, a context (when it
  occurs), and an impact — all four in 2–3 sentences.
- [ ] The statement is **falsifiable**: a reader could in principle disprove it
  with evidence.
- [ ] The statement contains **no solution language** (no product names, no
  features, no implementation details).
- [ ] At least one evidence signal is listed; if absent, the document is
  flagged "hypothesis — validate."
- [ ] Impact is quantified or directionally estimated; it is not left as a vague
  "users are frustrated."
- [ ] Out of Scope contains at least 2 bullets that a reasonable person might
  otherwise assume were in scope.
- [ ] The entire document fits within ~300–500 words.
- [ ] If the output is written to a file, it follows `template.md` — all 5
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `problem-statement-happy` (happy path) — well-specified B2B SaaS problem with
  user research and metrics available.
- `problem-statement-edge` (edge) — weak evidence scenario: the PM has only
  anecdotes and no quantitative data; the skill must produce a flagged
  hypothesis-grade statement.
- `problem-statement-adversarial` (adversarial) — the user provides a solution
  disguised as a problem; the skill must detect and reframe it.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `jobs-to-be-done` — uncovers the underlying motivation; run before this skill
  when the problem is still fuzzy; the JTBD insight feeds the core statement.
- `problem-framing-canvas` — a larger workshop artifact that explores the
  problem landscape across multiple lenses; the canvas output can be distilled
  into a problem statement using this skill.
- `create-prd` — consumes the problem statement as its opening section; run
  this skill first, then hand the output to `create-prd`.
- `discovery-process` — the meta-workflow; problem statement is one deliverable
  within a broader discovery sprint.

### External Frameworks
- Melissa Perri, *Escaping the Build Trap* (2018) — problem vs. solution framing
  discipline; the "outcome over output" principle underpins the falsifiability and
  no-solution-language requirements.
- Teresa Torres, *Continuous Discovery Habits* (2021) — opportunity framing and
  the importance of grounding problem statements in observed behaviour and unmet
  needs rather than assumed solutions.
- Geoffrey Moore, *Crossing the Chasm* (1991) — the value proposition template
  ("For [user] who [need], [product] is a [category] that [benefit]") as a
  complementary lens for shaping the Impact section.
