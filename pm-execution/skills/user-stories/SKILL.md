---
name: user-stories
description: >
  Generate well-formed user stories using the "As a [persona], I want [action],
  so that [outcome]" format with acceptance criteria. Use when writing user
  stories, breaking down a feature into backlog items, creating sprint-ready
  cards, or defining acceptance criteria for a new capability.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/user-stories/template.md
---

# Write User Stories

## Purpose
Produce a complete, sprint-ready set of user stories for a feature — each
following the "As a [persona], I want [action], so that [outcome]" format with
4–6 acceptance criteria — so that the team can estimate, plan, and build with
shared clarity on scope and expected behaviour.

**When NOT to use:** when motivation-first framing matters more than role/action
structure, use `job-stories` ("When … I want … so that …" format); when you need
to map stories across a user journey, use `user-story-mapping`; when a story is
already written and needs splitting, use `user-story-splitting`. This skill
**creates** stories from a feature brief — it does not split existing ones or
produce journey maps.

## Inputs
- **Required:** product or system name and the feature to decompose. If the
  feature is ambiguous, ask: "What user problem does this feature solve, and who
  are the primary user roles?"
- **Optional:** link to design files (Figma, Miro, etc.) — referenced in each
  story's Design field; key assumptions or constraints (accessibility, platform,
  performance targets); preferred story granularity (default: one sprint per
  story).

## Output Contract
The deliverable is a **user-story set** — one card per story, each structured as
(see `template.md`):

1. **Title** — short imperative phrase naming the capability (e.g., "Recently Viewed Section").
2. **Description** — single sentence in "As a [persona], I want [action], so that [outcome]" format.
3. **Design** — link to relevant design artefact, or "N/A" if none provided.
4. **Acceptance Criteria** — 4–6 numbered, testable conditions; each is observable and unambiguous.

Format: one markdown block per story, stories separated by `---`. Length: as
many stories as needed to cover the feature; each card ~10–15 lines. Stories are
independent and sized for one sprint.

**GOOD (excerpt):**
> **Title:** Recently Viewed Section
>
> **Description:** As an Online Shopper, I want to see a "Recently viewed"
> section on the product page so that I can easily revisit items I considered.
>
> **Design:** [Figma link]
>
> **Acceptance Criteria:**
> 1. The section appears at the bottom of the product page for any user who has
>    previously viewed at least one product in their session.
> 2. It is not shown to users visiting their first product page of the session.
> 3. The current product is excluded from the displayed items.
> 4. Each card shows the product image, title, price, and "Viewed X minutes ago" label.
> 5. Clicking a card navigates the user to that product's page.
> 6. The section is accessible via keyboard and screen readers (WCAG 2.1 AA).

**BAD (excerpt):**
> **Description:** Make a recently viewed thing on the product page.
>
> **Acceptance Criteria:** It should work correctly.
>
> — fails: no persona or outcome in the description; acceptance criteria are not
> testable and give no observable conditions.

## Process
1. **Parse the feature brief** — identify the product, the capability, and any
   provided design links or constraints.
2. **Identify user personas** — list the distinct user roles affected; if not
   provided, infer from context or ask.
3. **Decompose into stories** — break the feature into independently deliverable
   stories, one per distinct user action or system behaviour. Apply the INVEST
   criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable).
4. **Draft each story** — write Title, Description ("As a … I want … so that …"),
   and Design link.
5. **Write acceptance criteria** — 4–6 numbered conditions per story; each must
   be observable, unambiguous, and testable by QA.
6. **Check independence** — ensure stories can be developed in any order; split
   any story that chains on another's completion.
7. **Check sizing** — each story should be completable in one sprint; split any
   story that is too large.
8. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every story uses the exact "As a [persona], I want [action], so that [outcome]" format — no variations.
- [ ] Each story has **4–6 acceptance criteria**, each of which is numbered, observable, and unambiguous.
- [ ] Stories are **independent** — none blocks another's start; they can be built in any order.
- [ ] Every story is **sized for one sprint**; any story spanning multiple sprints has been split.
- [ ] A **Design** field is present on every story (link or explicit "N/A").
- [ ] Personas are **specific** (e.g., "Online Shopper", "Account Admin") — not generic ("user", "person").
- [ ] Acceptance criteria cover **happy path, at least one edge case, and one accessibility or performance condition** where relevant.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `user-stories-happy` — well-specified e-commerce feature with a design link.
- `user-stories-edge` — feature with no design link and ambiguous user roles.
- `user-stories-adversarial` — vague one-liner the skill must scope before writing stories.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `job-stories` — alternate format ("When … I want … so that …") preferred when motivation context matters more than role clarity.
- `user-story-mapping` — arranges stories across a user journey; consumes the story set this skill produces.
- `user-story-splitting` — splits an oversized story into sprint-ready pieces; use when a story from this skill is still too large.
- `epic-breakdown-advisor` — upstream skill that identifies which epics need decomposition before this skill authors the stories.

### External Frameworks
- Mike Cohn, *User Stories Applied* (2004) — originator of the "As a … I want … so that …" format and the INVEST criteria.
- Ron Jeffries, *The 3 C's of User Stories* (Card, Conversation, Confirmation) — foundational framing for what makes a story complete.
- [How to Write User Stories: The Ultimate Guide](https://www.productcompass.pm/p/how-to-write-user-stories) — practical guidance on story format, sizing, and acceptance criteria.
