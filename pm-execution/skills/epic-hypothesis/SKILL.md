---
name: epic-hypothesis
description: >
  Craft a testable hypothesis statement for an epic that makes the team's bet
  explicit, names the expected outcome, and defines success criteria. Use when
  starting an epic, writing a product brief, aligning a team on what the work is
  trying to prove, or building a hypothesis-driven backlog.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/epic-hypothesis/template.md
---

# Epic Hypothesis

## Purpose
Produce a structured hypothesis statement for an epic — a single, testable bet
that captures what the team is building, who it is for, what outcome they expect,
how success will be measured, and when the team will know if the hypothesis holds.
The artifact makes implicit assumptions explicit so the team ships with shared
clarity rather than shared ambiguity.

**When NOT to use:**
- Decomposing the epic into stories (use `epic-breakdown-advisor` — that skill
  splits the work; this skill first frames the bet).
- Identifying what could go wrong after the hypothesis is set (use `pre-mortem`).
- Articulating the problem that motivates the epic (use `problem-statement` —
  that skill frames the pain; this skill frames the proposed solution bet).
- Estimating effort or sprint capacity (use `sprint-plan`).

## Inputs
- **Required:** an epic description or title — what the team is planning to build.
  If missing, ask for it; do not invent scope.
- **Required:** target user or customer segment — who the epic is for. If missing,
  ask; do not assume.
- **Optional:** desired outcome or OKR it ties to — if absent, derive the most
  plausible outcome from the epic description and flag it as an assumption.
- **Optional:** metric(s) for success — if absent, propose the most direct
  leading and lagging indicators for the expected outcome.
- **Optional:** validation timeframe — if absent, default to the next sprint cycle
  or release window and say so.
- **Optional:** existing context (user research, past experiments, competitor
  signals) — incorporate it into the confidence rating and assumptions list.

## Output Contract
The deliverable is an **epic hypothesis card** with these sections (see
`template.md`):

1. **Hypothesis Statement** — the canonical one-sentence form:
   "We believe [building X] for [user] will [achieve outcome], measured by
   [metric]. We'll know in [timeframe]." Each bracket is filled with a specific,
   non-generic value.
2. **Rationale** — 2–4 bullet points explaining *why* the team believes this:
   the signal (research, data, analogy) that grounds each part of the statement.
3. **Assumptions** — a numbered list of load-bearing assumptions the hypothesis
   rests on, each rated confidence: high / med / low, with a suggested validation
   method.
4. **Success Criteria** — a small table: metric, baseline (current value or
   "unknown"), target, and measurement method. Minimum one leading and one lagging
   indicator.
5. **Anti-goals** — 2–3 bullet points clarifying what success does *not* mean
   (guards against misaligned celebrations).
6. **Open Questions** — any unresolved unknowns the team must answer before or
   during execution.

Format: concise prose + one table. Length: fits on a single page.

**GOOD (excerpt):**
> **Hypothesis Statement:** We believe adding in-app guided onboarding checklists
> for first-time B2B users will increase 30-day feature activation from 34% to
> ≥ 50%, measured by the percentage of new seats completing the "core workflow"
> within 30 days of account creation. We'll know in 8 weeks (next release cycle).
>
> *Assumption 2 (low confidence): users who skip onboarding do so because the
> next step is unclear, not because they actively chose self-discovery — validate
> via 5 user interviews + session recordings before dev starts.*

**BAD (excerpt):**
> "We believe improving onboarding will help users and increase engagement."
> — fails: "improving" is undefined, "users" is unspecific, "help" is not
> measurable, no metric, no timeframe, no confidence signal.

## Process
1. **Clarify scope** — confirm the epic description, target user, and whether an
   OKR or desired outcome already exists. If missing, ask before proceeding.
2. **Draft the hypothesis statement** — fill the canonical template with
   specifics. Replace every bracket with a concrete value; flag any filled with
   an assumption.
3. **Build the rationale** — list the evidence or reasoning behind each filled
   slot; be honest about weak signals vs. strong data.
4. **Surface assumptions** — enumerate the beliefs the hypothesis rests on that
   are not yet validated. Rate confidence honestly.
5. **Define success criteria** — name at least one leading indicator (early
   signal within the timeframe) and one lagging indicator (the real outcome
   metric). Set baselines and targets with reasoning.
6. **Name anti-goals** — specify what the team will *not* celebrate as success to
   prevent metric gaming.
7. **Log open questions** — capture anything that must be resolved before or
   during execution to avoid mid-sprint pivots.
8. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The hypothesis statement is a single, grammatically complete sentence
  following the canonical form — no generic placeholders remain.
- [ ] "Building X" is a specific deliverable, not a fuzzy verb like "improving"
  or "fixing".
- [ ] "User" is a named segment, not a generic "users" or "customers".
- [ ] "Outcome" is a behavior or result the user experiences, not a feature launch.
- [ ] "Metric" is measurable, has a baseline (or "unknown — see open questions"),
  and has a target with direction and magnitude.
- [ ] "Timeframe" is a specific date range or sprint cycle, not "soon".
- [ ] At least one low-confidence assumption is identified and a validation method
  is proposed.
- [ ] The success-criteria table has at least one leading and one lagging
  indicator.
- [ ] Anti-goals are meaningful, not trivially obvious.
- [ ] If the output is written to a file, it follows `template.md` (a
  skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `epic-breakdown-advisor` — consumes the finished hypothesis to split the epic
  into well-scoped stories; run *after* this skill.
- `pre-mortem` — takes the hypothesis as input and stress-tests it by imagining
  failure; run *after* this skill.
- `problem-statement` — frames the problem space that motivates the epic; run
  *before* this skill if the problem is not yet crisp.
- `job-stories` — surfaces the underlying job-to-be-done that the hypothesis
  should tie its outcome to.

### External Frameworks
- Eric Ries, *The Lean Startup* (2011) — "Build-Measure-Learn" loop and the
  distinction between a value hypothesis (does the thing create value?) and a
  growth hypothesis (does it spread?); the canonical one-sentence form in this
  skill is built on Ries's hypothesis framing.
- Jeff Patton, *User Story Mapping* (2014) — outcome-oriented epic framing that
  separates the "outcome for users" from the "output we ship".
- Teresa Torres, *Continuous Discovery Habits* (2021) — opportunity trees and
  the discipline of naming the outcome before naming the solution; directly
  informs the "outcome" and "anti-goals" sections.
- [Atlassian — Writing better epics](https://www.atlassian.com/agile/project-management/epics)
  — practical guidance on epic scope and the risks of vague epic titles.
