---
name: jobs-to-be-done
description: >
  Map the progress a customer segment is trying to make — as functional,
  emotional, and social jobs — and express each in the canonical job statement
  format. Use when uncovering underlying customer motivations, reframing a
  problem space around progress rather than features, preparing discovery
  interviews, or feeding job insights into an opportunity-solution tree or
  product strategy.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/jobs-to-be-done/template.md
---

# Map Jobs to Be Done

## Purpose
Produce a structured JTBD analysis that makes explicit the progress a customer
segment is trying to make — decoupled from any solution, product, or demographic
lens. The output is a set of job statements (functional, emotional, and social)
anchored to a specific situation, together with the metrics the customer would
use to judge whether the job was done well. This equips PMs to prioritize
opportunities, frame discovery interviews, and brief design or engineering on
the underlying motivation rather than assumed features.

**When NOT to use:** when you need a demographic profile of your user (use
`user-personas`); when you need a single written problem framing artifact for
a stakeholder brief (use `problem-statement`); when you are building out a full
opportunity decomposition tree (use `opportunity-solution-tree` — this skill
produces the job analysis that *feeds* that tree, not the tree itself); or when
you already have clear job statements and need to ideate solutions (move
directly to solution brainstorming).

## Inputs
- **Required:** a customer segment or context — who is being studied and in what
  situation. If absent, ask: "Who is the customer and what situation are they in
  when they reach for a solution?" Do not guess the segment.
- **Optional:** raw interview quotes, survey data, or observation notes — provide
  them and the skill will extract job signals ("when … I want to … so I can …"
  language). Without this, the skill reasons from the described situation and
  flags that claims should be validated with primary research.
- **Optional:** scope constraint — functional-only, or all three job types
  (default: all three).

## Output Contract
The deliverable is a **JTBD analysis** with these sections (see `template.md`):

1. **Situation & Context** — the specific circumstance that triggers the job;
   who the customer is, what they are trying to accomplish, and what forces
   (push, pull, habit, anxiety) are at play.
2. **Functional Job** — the literal task the customer is trying to complete,
   expressed in verb-object form ("file quarterly taxes", "find a trusted
   plumber"). One primary functional job; secondary functional jobs bulleted.
3. **Emotional Job** — how the customer wants to feel (or avoid feeling) as they
   do the job. One sentence per emotional dimension.
4. **Social Job** — how the customer wants to be perceived by others as a result
   of doing the job. One sentence per social dimension.
5. **Job Statements** — the canonical "When [situation], I want to [motivation],
   so I can [expected outcome]." format. One statement per job type (functional,
   emotional, social); group related variants as sub-bullets.
6. **Metrics of Success** — the criteria the customer uses to judge whether the
   job was done well. Express as measurable or observable outcomes, not product
   features ("tax filed before deadline with no audit flags", not "fast
   e-filing UI").
7. **Discovery Signals** — phrases or patterns from interviews/observation that
   confirm or challenge this job analysis; flag any assumptions not yet
   validated.

Format: structured prose with clear headings. Length: 1–2 pages. Every job
statement must be testable against an interview quote or labeled a hypothesis
for validation.

**GOOD (excerpt):**
> **Functional Job:** Reconcile monthly team expenses accurately.
>
> **Job Statement (functional):** "When I close the books at month-end, I want
> to match every charge to the right budget line without chasing receipts, so
> I can submit the report on time and avoid audit risk."
>
> *Validation status: confirmed — 4/6 interview participants used the phrase
> "chasing receipts" unprompted.*

**BAD (excerpt):**
> "Customers want a better expense dashboard."
> — fails: this is a solution, not a job. No situation, no outcome, no
> emotional or social dimension, no validation signal.

## Process
1. **Fix the segment and situation** — name the customer type and the specific
   trigger situation. If either is missing, ask before proceeding.
2. **Extract job signals** — scan any provided quotes or notes for "when …",
   "help me …", "I wish …", "so I can …" language. These are raw job candidates.
3. **Identify the functional job** — strip solutions, adjectives, and features;
   find the underlying verb-object action the customer is trying to complete.
4. **Layer emotional and social jobs** — ask: How does the customer want to feel
   during or after doing this job? How do they want to appear to peers,
   managers, or family?
5. **Write canonical job statements** — one per job type, using the "When
   [situation], I want to [motivation], so I can [outcome]" format. Each
   statement must contain a situation clause, a motivation clause, and an
   outcome clause.
6. **Define metrics of success** — restate the outcome clause as a measurable or
   observable criterion the customer would recognize as "job done".
7. **Surface discovery signals** — cite confirming or conflicting evidence from
   input data; flag any statement that is a hypothesis rather than a confirmed
   observation.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The segment and triggering situation are explicitly named — no generic
  "users" or "customers".
- [ ] The functional job is expressed as a verb-object phrase, not a solution
  or feature request.
- [ ] All three job types (functional, emotional, social) are addressed, or the
  omission of one is explicitly justified.
- [ ] Every job statement contains a situation clause, a motivation clause, and
  an outcome clause in the canonical format.
- [ ] Metrics of success are expressed as customer-observable outcomes, not
  product capabilities or UI attributes.
- [ ] Each job statement is either backed by a discovery signal (quote/
  observation) or explicitly flagged as a hypothesis.
- [ ] No solution, feature, or technology is embedded in the job statement
  itself.
- [ ] If the output is written to a file, it follows `template.md` — all 7
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `jobs-to-be-done-happy` (happy path) — segment with rich interview signals;
  all three job types present and well-formed.
- `jobs-to-be-done-edge` (edge) — vague segment description with no interview
  data; skill must elicit clarification and flag all statements as hypotheses.
- `jobs-to-be-done-adversarial` (adversarial) — input frames the job as a
  feature request; skill must reframe to underlying motivation and refuse to
  output a solution-embedded job statement.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `user-personas` — describes who the customer is demographically; JTBD describes
  what progress they seek regardless of who they are. Run personas before JTBD
  when segment identity is still unclear.
- `problem-statement` — produces a single written problem artifact for
  stakeholders; JTBD produces structured job statements that reveal the
  underlying motivation behind any problem statement.
- `opportunity-solution-tree` — consumes JTBD job statements as the desired
  outcome node at the top of the tree; run JTBD first.
- `discovery-interview` — generates an interview guide; JTBD analysis
  informs the question design and provides the hypotheses to validate.

### External Frameworks
- Clayton Christensen, *The Innovator's Dilemma* (1997) and "Know Your Customers'
  Jobs to Be Done" (*Harvard Business Review*, 2016) — originating "hire a product
  to do a job" framing and the three job dimensions this skill is built on.
- Tony Ulwick, *Jobs to Be Done: Theory to Practice* (2016) — Outcome-Driven
  Innovation; source of the metrics-of-success (desired outcome statement)
  discipline used in Section 6.
- Bob Moesta & Chris Spiek, *Demand-Side Sales* (2020) — four forces (push/pull/
  habit/anxiety) used in the Situation & Context section; job story format
  ("When … I want to … so I can …").
- Alan Klement, *When Coffee and Kale Compete* (2018) — social and emotional job
  dimensions and the "struggling moment" as the trigger for the situation clause.
