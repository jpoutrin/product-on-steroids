---
name: brainstorm-experiments-existing
description: >
  Design low-effort experiments to validate assumptions about an existing
  product — A/B tests, prototypes, spikes, and production tests. Use when
  testing feature ideas cheaply, validating product assumptions, or planning
  risk-controlled experiments.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/brainstorm-experiments-existing/template.md
---

# Design Experiments for Existing Products

## Purpose
Generate a set of testable, low-effort experiments (A/B tests, feature stubs,
prototypes, spikes, production tests) designed to validate specific assumptions
about an existing product — with explicit hypotheses, success metrics, and
cost/speed estimates to support prioritization. The output enables the team to
choose which assumptions to test first and plan the experiment roadmap.

**When NOT to use:** brainstorming raw ideas (use `brainstorm-ideas-existing`),
surfacing assumptions in the first place (use `identify-assumptions-existing`),
ranking assumptions by importance (use `prioritize-assumptions`), or designing
experiments for *new* products/markets (use `brainstorm-experiments-new`).
Experiments require assumptions already identified; this skill designs the tests.

## Inputs
- **Required:** feature idea or assumption set for an existing product —
  describe what the team wants to build or validate and which assumptions are
  load-bearing (e.g., "Users will adopt this notification setting" or "The
  search algorithm change won't hurt relevance").
- **Optional:** risk tolerance, budget/timeline constraints (e.g., "must stay
  within 1 sprint" or "production tests must limit exposure to <5% of users"),
  existing product context (docs, analytics setup, user behavior baselines).

## Output Contract
The deliverable is an **experiment design memo** with these sections (see `template.md`):

1. **Feature Idea & Assumptions** — brief description of what's being tested and 2–4 key testable beliefs.
2. **Experiments** — a table with one row per experiment, columns: Hypothesis (prediction statement), Experiment (method), Success Metric (measurable quantity), Success Threshold (target value), Cost Estimate, Timeline.
3. **Risk Mitigation** — for production tests (A/B tests, spikes), traffic caps, rollback triggers, or time windows.
4. **Prioritization Notes** — which experiments resolve highest risk, which run fastest, and recommended order.

Format: prose + one summary table. Length: ~1–2 pages. Every experiment is testable and grounded.

**GOOD (excerpt):**
> | Hypothesis | Experiment | Success Metric | Success Threshold | Cost | Speed |
> |-----------|-----------|----------------|-------------------|------|-------|
> | Users will adopt in-app messaging when preferences are accessible | Feature stub: Show settings link in top nav (no backend); measure clicks over 3 days | Click-through rate on pref link | ≥15% of weekly users click | 2 hours frontend | 3 days |
> | Existing API response time ≤500ms will not degrade with 10x load | Load test with production traffic pattern; spike instances | P95 API latency | ≤600ms (20% margin) | 4 hours test setup | 1 day |

**BAD (excerpt):**
> "Test if users like notifications" — fails because hypothesis is vague opinion (not a prediction), no metric or threshold defined, method is unspecified, no cost/speed estimate.

## Process
1. **Parse the assumptions** — identify the testable beliefs in the user's feature idea or statement (e.g., "We assume users want X and will pay Y").
2. **Brainstorm experiments per assumption** — generate 2–3 low-effort methods per assumption (fake door, spike, prototype test, survey, A/B test, Wizard of Oz, stub).
3. **Define hypotheses, metrics, and thresholds** — for each experiment, state what success looks like in measurable terms (not opinions).
4. **Estimate cost and speed** — use past sprints, tooling known to the team, and risk (production tests cost more) to estimate.
5. **Prioritize risk vs. learning** — call out which experiments de-risk the most and which are fastest to run.
6. **Organize as a table** — sort by speed or importance; annotate any production-test risk mitigations (e.g., "Limit to 5% of users" or "Run Fri–Mon only").
7. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every experiment has a clear, measurable hypothesis (not an opinion or vague belief).
- [ ] Each row specifies a concrete method (e.g., "A/B test in prod" not "test it").
- [ ] Every metric has a success threshold (numeric, not "high" or "good").
- [ ] At least one experiment tests each assumption mentioned or implied in the input.
- [ ] Cost and speed estimates are realistic and grounded (not hand-wavy; e.g., "2–3 days" not "quick").
- [ ] If production tests are included, risk-mitigation strategies are named (e.g., traffic cap, rollback plan, time window).
- [ ] If output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `brainstorm-experiments-existing-happy` (happy path) — a realistic feature idea with clear assumptions; output should span multiple experiment methods and prioritize by risk/speed.
- `brainstorm-experiments-existing-edge` (edge) — sparse context or implicit assumptions; skill must infer and clarify assumptions before designing.
- `brainstorm-experiments-existing-adversarial` (adversarial) — vague input ("test if this works") with no metrics or cost constraints; skill must refuse to one-number and demand measurable hypotheses and constraints.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `identify-assumptions-existing` — surfaces assumptions in a feature idea or strategy; feeds the assumptions this skill tests.
- `prioritize-assumptions` — ranks assumptions by criticality; tells you which experiments to run first.
- `brainstorm-ideas-existing` — generates raw feature/product ideas; this skill designs experiments to *test* them.
- `brainstorm-experiments-new` — experiments for new products/markets where the baseline or user base is unknown.

### External Frameworks
- Ash Maurya, *Lean Product Playbook* (2014) — lean testing and the hierarchy of assumptions (riskiest = most important to test).
- Steve Blank, *The Four Steps to the Epiphany* (2013) — customer validation and low-cost experiment design (fake door, prototype, Wizard of Oz).
- Kent Beck, *Extreme Programming Explained* (2000) — technical spikes as risk-reduction experiments.
- [Product Compass — Testing Product Ideas](https://www.productcompass.pm/p/the-ultimate-experiments-library) — catalogue of experiment methods and when to use each.
