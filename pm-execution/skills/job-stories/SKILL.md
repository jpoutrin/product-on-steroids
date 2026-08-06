---
name: job-stories
description: >
  Create job stories using the 'When [situation], I want to [motivation], so I can
  [outcome]' format with detailed acceptance criteria. Use when writing job stories,
  creating JTBD-style backlog items, expressing user situations and motivations, or
  focusing on user context rather than personas.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/job-stories/template.md
---

# Create Job Stories (When/I Want/So I Can)

## Purpose
Generate job stories that capture user situations, motivations, and outcomes in the
Jobs-to-be-Done (JTBD) framework format: "When [situation], I want to [motivation],
so I can [outcome]." Each story includes detailed acceptance criteria focused on
validating the outcome is achieved, not just the feature exists. Prioritizes context
and user goals over roles and personas, enabling cross-persona feature discovery and
clearer outcome validation.

**When NOT to use:** persona-centric user stories (use `user-stories`), swimlane
feature decomposition (use a task-breakdown skill), or technical acceptance criteria
(use dev-focused story refinement). Job stories complement but do not replace user
stories; use when the *situation* matters more than *who* is acting.

## Inputs
- **Required:** the product or system name, the feature or job to break into stories,
  any design mockups or prototypes (Figma/Miro link), and user situations or job
  scenarios that trigger the need.
- **Optional:** pricing/pricing anchor, known user segments, competitive context, or
  business outcomes you expect this feature to drive.

## Output Contract
The deliverable is a **set of job stories** following this structure (see
`template.md`). Each job story includes:

1. **Outcome Title** — a concise, result-focused heading.
2. **Job Story statement** — "When [situation], I want to [motivation], so I can [outcome]."
3. **Design link** — URL to mockup or prototype (Figma, Miro, etc.) if available.
4. **Acceptance criteria** — 5–8 measurable, observable criteria that confirm the
   outcome is achieved. Each criterion must be testable and outcome-focused, not
   implementation-focused.

Deliver 3–5 distinct job story blocks in this format.

**GOOD (excerpt):**
> **Title:** Track Weekly Snack Spending
>
> **Job Story:** When I'm preparing my weekly allowance for snacks, I want to quickly see how much I've spent so far, so I can make sure I don't run out of money before the weekend.
>
> **Acceptance Criteria:**
> 1. Display Spending Summary with 'Weekly Spending Overview' section visible on load
> 2. Real-Time Update triggers when an expense is logged
> 3. Progress Indicator (progress bar) shows 0–100% of weekly budget
> 4. Remaining Budget is highlighted in a prominent color
> 5. User can access detailed spending log with breakdown by category
> 6. Notifications trigger at 80% budget threshold
> 7. Weekend-specific reminder appears by Thursday evening
> 8. Navigation to detailed breakdown is less than 1 click away

**BAD (excerpt):**
> "When a user spends money, they want to track it, so they can be aware."
> — fails: situation is generic (not a triggering context), motivation is vague
> (not an actionable desire), outcome is unmeasurable (what does "aware" mean?).

## Process
1. **Identify triggering situations** — what circumstances or contexts cause the user
   to engage with this job?
2. **Define motivations** — what does the user want to accomplish or feel?
3. **Clarify outcomes** — what does success look like? Be specific and measurable.
4. **Apply JTBD discipline** — focus on the *job* (the goal), not the *role* (the persona).
5. **Create acceptance criteria** — each criterion should validate an aspect of the
   outcome. Use observable, measurable language (visible, clickable, notified, etc.).
6. **Link to design** — attach mockups or prototypes so developers and QA see the
   context.
7. **Avoid feature creep** — acceptance criteria validate the outcome, not every
   possible feature variant.
8. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every job story has a clear **situation** (triggering context, not a persona).
- [ ] Every motivation is **specific and actionable** (not generic like "be aware").
- [ ] Every outcome is **measurable and observable** (can QA or a user confirm it?).
- [ ] Acceptance criteria are **outcome-focused**, not implementation-focused.
- [ ] Each criterion is **testable** (not "the user is happy"; instead "the progress bar updates in < 1 second").
- [ ] Design links are **present** and point to actual mockups or prototypes.
- [ ] At least **3–5 distinct job stories** are generated per feature.
- [ ] If the stories are written to a file, they follow `template.md` — all sections present and in order, headings matching.

## Validation & Eval
Scenario cards in `evals/`:
- `job-stories-happy` (happy path) — well-scoped job with clear situations, motivations, and outcomes.
- `job-stories-edge` (edge) — sparse job description requiring the skill to ask clarifying questions before breaking into stories.
- `job-stories-adversarial` (adversarial) — vague, persona-centric input ("build a feature for users") the skill must reframe into JTBD language.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `user-stories` — persona-centric story format; use when the *role* (who) matters more than the *situation* (when/why).
- `pre-mortem` — identifies risks and assumptions in job stories before development starts.
- `acceptance-criteria` — detailed framework for writing outcome-focused acceptance criteria.

### External Frameworks
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course) — canonical JTBD theory and application.
- Clayton M. Christensen, *The Innovator's Solution* (2003) — foundational Jobs Theory and how to apply it to product design.
- Bob Moesta & Chris Jones, *Demand-Side Sales* — practical JTBD storytelling for understanding customer decision-making.
