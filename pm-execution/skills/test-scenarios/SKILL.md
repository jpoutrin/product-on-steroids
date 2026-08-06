---
name: test-scenarios
description: >
  Generate comprehensive test scenarios from a user story, including test
  objectives, starting conditions, user roles, step-by-step actions, and
  expected outcomes. Use when writing QA test cases, creating test plans,
  defining acceptance tests, or preparing for feature validation.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/test-scenarios/template.md
---

# Test Scenarios

## Purpose
Produce a complete, QA-ready set of test scenarios for a given user story —
covering the happy path, edge cases, and error conditions — so engineers and
QA teams can validate an implementation without ambiguity. Each scenario
specifies the starting system state, the user role performing the test, the
exact step-by-step actions, and the observable expected outcomes.

**When NOT to use:** exploratory testing without a specific user story (use an
unstructured test session instead); performance/load testing design (different
discipline); writing automated test code in a programming language (this skill
produces human-readable test plans, not code); or reviewing test results after
execution (this skill creates plans, not reports).

## Inputs
- **Required:** the user story (title + acceptance criteria). If only a feature
  description is given, ask for the acceptance criteria before proceeding — they
  define what "done" means and drive scenario coverage.
- **Optional:** product or system name — used to label scenarios clearly.
- **Optional:** additional testing context or constraints (environment
  restrictions, known limitations, existing data setup). If absent, assume a
  clean default environment and note that assumption.

## Output Contract
The deliverable is a **test scenario document** structured as (see `template.md`):

1. **Overview** — the user story under test, its acceptance criteria, and the
   total number of scenarios generated.
2. **Test Scenarios** — one scenario block per acceptance criterion plus
   additional edge-case and error scenarios. Each block contains:
   - **Test Scenario** (name)
   - **Test Objective** (what is validated)
   - **Starting Conditions** (system state, data, permissions required)
   - **User Role** (who performs the test)
   - **Test Steps** (numbered, each with action → expected result inline)
   - **Expected Outcomes** (observable results, one bullet each)
3. **Coverage Summary** — a brief table mapping each acceptance criterion to the
   scenario(s) that cover it, plus a note on any gaps.

Format: structured plain text or Markdown. Length scales with the number of
acceptance criteria; aim for one tight scenario per criterion plus
representative edge cases.

**GOOD (excerpt):**
> **Test Scenario:** View Recently Viewed Products — Exclude Current Product
>
> **Test Objective:** Verify that the recently-viewed section displays correctly
> and excludes the product the user is currently viewing.
>
> **Starting Conditions:**
> - User is logged in with browser history enabled
> - User has viewed at least 2 products in the current session
> - User is on a product page different from previously viewed items
>
> **Test Steps:**
> 1. Navigate to any product page → Section appears at the bottom with previously viewed items
> 2. Scroll to bottom → "Recently viewed" section is visible with product cards
> 3. Check the card list → Current product is NOT included in the list
>
> **Expected Outcomes:**
> - Section displays 4–8 product cards with image, title, and price
> - Current product is excluded from the list
> - Each card shows a "Viewed X minutes ago" timestamp

**BAD (excerpt):**
> "Test that the recently-viewed feature works."
> — fails: no starting conditions, no step-by-step actions, no specific expected
> outcomes; a QA engineer cannot execute this without guessing.

## Process
1. **Parse the user story** — identify the actor, goal, and each acceptance
   criterion. If criteria are absent or vague, ask before proceeding.
2. **Plan coverage** — map one primary scenario per acceptance criterion; flag
   any criterion that needs more than one scenario (e.g., valid + invalid input).
3. **Define starting conditions** — specify system state, required data
   (existing records, user accounts, feature flags), and permissions for each
   scenario.
4. **Assign user role** — name the persona or role that performs the test
   (e.g., "Registered User", "Admin", "Guest").
5. **Write test steps** — break each interaction into the smallest observable
   unit; record the expected result inline after each step (action → result).
6. **State expected outcomes** — list observable, binary results: what the tester
   sees, reads, or can measure after all steps are complete.
7. **Add edge cases** — invalid inputs, boundary values, empty states, permission
   boundaries, and race conditions relevant to the story.
8. **Write the coverage summary** — table mapping acceptance criteria to scenarios;
   call out any criterion that has no scenario.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every acceptance criterion has at least one corresponding scenario.
- [ ] Each scenario includes **starting conditions** (no implicit assumed state).
- [ ] Test steps are numbered and each step records its own expected result inline.
- [ ] **Expected Outcomes** are observable and binary — a tester can unambiguously
  mark each as pass or fail without judgment calls.
- [ ] At least one **edge-case or error scenario** is included (invalid input,
  boundary condition, or permission boundary).
- [ ] The **Coverage Summary** table is present and maps criteria → scenarios,
  with any gaps noted.
- [ ] If the output is written to a file, it follows `template.md` (a
  skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `test-scenarios-happy` — full user story with clear acceptance criteria;
  validates standard happy-path output and inline expected results.
- `test-scenarios-edge` — user story with a single, ambiguous acceptance
  criterion; validates that the skill asks a clarifying question rather than
  guessing.
- `test-scenarios-adversarial` — caller provides only a feature name with no
  acceptance criteria and pushes for immediate scenarios; validates that the
  skill requests criteria before generating.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `user-stories` — produces the user stories that feed this skill as input;
  run it first when stories haven't been written yet.
- `acceptance-criteria` — sharpens the acceptance criteria that this skill maps
  to scenarios; use it when criteria are vague before generating test scenarios.

### External Frameworks
- ISTQB Syllabus (Foundation Level) — defines test condition, test case, and
  test step terminology that this skill's output format follows.
- Gojko Adzic, *Specification by Example* (2011) — living documentation and
  scenario-based acceptance testing that underpins the step/outcome structure.
- Mike Cohn, *User Stories Applied* (2004) — acceptance-criteria patterns for
  user stories that define the coverage targets for this skill.
