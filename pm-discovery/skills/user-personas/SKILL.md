---
name: user-personas
description: >
  Synthesize qualitative and quantitative research data into 2–4 research-validated
  user personas — each with JTBD, pain points, desired gains, behaviors, and an
  unexpected insight. Use when building personas from survey data, interview
  transcripts, or usability studies; when segmenting users for product decisions;
  or when grounding a PRD, roadmap, or design sprint in real user evidence.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/user-personas/template.md
---

# Research-Validated User Personas

## Purpose
Produce 2–4 research-validated user personas from real data — surveys, interviews,
analytics, usability sessions, or a combination — that capture the true diversity
of the user base. Each persona surfaces jobs-to-be-done, pain points, desired
gains, behavioral patterns, and at least one counterintuitive insight, so product
and design teams can make decisions grounded in evidence rather than assumption.

**When NOT to use:**

- **No research data yet.** If you have hypotheses but no user data, use
  `proto-persona` instead — it produces a pre-research hypothesis persona to
  guide your first round of interviews, not a validated artifact.
- **Segmentation analysis.** If the goal is to find and size segments rather
  than characterize them, start with `user-segmentation`.
- **Interview synthesis only.** If you need a structured summary of a single
  interview set without the full persona format, use `interview-synthesis`.
- **Competitive profiling.** If you want to understand a competitor's user base,
  use `competitor-analysis`.

**Proto-persona vs. this skill:** `proto-persona` is a quick pre-research
hypothesis that costs nothing to create and should be invalidated or confirmed
by real data. This skill is the *confirmation step* — it consumes that data and
produces a research-backed artifact that can drive product and design decisions.
Never use this skill to dress up untested assumptions as validated personas.

## Inputs
- **Required:** research data — one or more of: survey responses (raw or
  aggregated), interview transcripts or notes, usability-test observations,
  analytics exports, NPS/CSAT verbatims. If none is provided, ask for it; do
  not invent data.
- **Required:** product or problem space context — what product are these personas
  for, and what decisions will they inform?
- **Optional:** number of personas desired (default: derive from distinct
  segments visible in data, up to 4). If the user specifies a count that
  contradicts the data segments, flag the tension.
- **Optional:** emphasis dimension — e.g., "focus on B2B buyers vs. end users"
  or "highlight retention risk users". Default: balanced coverage.
- **Optional:** existing proto-personas or hypotheses — use to validate or
  invalidate rather than confirm blindly.

## Output Contract
The deliverable is a **persona set** of 2–4 research-validated personas (see
`template.md`). Each persona contains:

1. **Name & Role** — a memorable name (not a demographic label) + role or
   context description, plus 3–5 demographic anchors drawn from the data.
2. **Primary Job-to-be-Done** — the core outcome the persona is trying to
   achieve, the context and frequency of the job, and what "done" looks like
   for them.
3. **Top Pain Points** — 3 specific challenges or obstacles, each tied to
   evidence from the data with severity noted.
4. **Desired Gains** — 3 outcomes, benefits, or solutions the persona seeks,
   with how they measure success.
5. **Behavioral Patterns** — 2–3 observable habits or workflows relevant to the
   product, with data source or observation reference.
6. **Unexpected Insight** — one counterintuitive finding from the data that
   contradicts common assumptions; why it matters for product decisions.
7. **Representative Quote** — a verbatim or lightly synthesized quote (flagged
   as synthesized if not verbatim) that captures the persona's voice.

**GOOD (excerpt):**
> **JTBD:** Priya needs to get a supplier contract reviewed and signed within 24 hours
> of a deal close — she does this ~3× per week. "Done" means a countersigned PDF
> in her inbox with no back-and-forth.
> **Pain (severity: high):** PDF redlines land in email with no threading — she
> loses version history (18/24 interviewees cited this).
> **Unexpected Insight:** Priya owns a personal Acrobat Pro subscription and
> pays out of pocket because IT procurement takes 6 weeks. This is a willingness-
> to-pay signal, not a "power user" signal — validate pricing on self-serve.

**BAD (excerpt):**
> "Sarah, 32, marketing professional who likes efficiency."
> — fails: no JTBD, no data evidence, demographic label not behavioral, no pain
> points or gains, no insight, unactionable for product decisions.

## Process
1. **Ingest data** — read all provided files and artefacts; flag gaps (e.g.,
   "no behavioral data for segment X") before proceeding.
2. **Extract signals** — pull recurring motivations, frustrations, jobs, and
   behaviors; note frequency of each signal (how many respondents / sessions).
3. **Cluster into segments** — group signals into 2–4 behaviorally distinct
   clusters; name each cluster by the dominant job, not demographics.
4. **Draft personas** — for each cluster, populate all 7 sections of the Output
   Contract, citing the data signal (e.g., "12/20 interviewees") for each claim.
5. **Surface the unexpected insight** — look for findings that contradict the
   product team's prior assumptions or the initial proto-personas; document why
   the finding matters.
6. **Cross-check distinctness** — verify personas are meaningfully different
   from each other; if two clusters collapse, merge them and note the merge.
7. **Validate quote authenticity** — use a verbatim quote where possible; if
   synthesized, label it explicitly ("synthesized from 5 interviews").
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every persona claim (pain, gain, behavior, JTBD) is tied to a specific
      data source or a frequency count — no unsupported assertions.
- [ ] Each persona has a distinct primary JTBD that does not overlap with
      another persona's JTBD.
- [ ] Personas are behaviorally differentiated, not just demographically split.
- [ ] Each persona includes exactly one Unexpected Insight that is
      counterintuitive (not an obvious restatement of a pain point).
- [ ] Every quote is either verbatim or explicitly labeled "synthesized."
- [ ] If the data contained gaps or low-confidence signals, they are flagged
      rather than smoothed over.
- [ ] The number of personas matches the distinct segments visible in the data;
      if it does not, the tension is explained.
- [ ] If the output is written to a file, it follows `template.md` — all 7
      sections present per persona, in order, headings matching (a skill-scoped
      hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `user-personas-happy` — full survey + interview data set, clear segments.
- `user-personas-edge` — thin data (one interview round, no analytics).
- `user-personas-adversarial` — request to "create personas" with no research
  data provided; user resists asking for data.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `proto-persona` — pre-research hypothesis persona; feeds and is validated by
  this skill. Use before user research; use this skill after.
- `interview-synthesis` — structures findings from a single interview round;
  output feeds into step 2 (Extract signals) of this skill's process.
- `user-segmentation` — finds and sizes segments; often a prerequisite when
  the team has analytics but no qualitative data.
- `jobs-to-be-done` — deep JTBD framework; use when the job framing needs more
  rigor than a persona JTBD section provides.

### External Frameworks
- Alan Cooper, *The Inmates Are Running the Asylum* (1999) — originator of
  goal-directed design personas; the behavioral-over-demographic principle
  this skill is built on.
- Lene Nielsen, *Personas — User Focused Design* (2019) — ten-step persona
  method with evidence-grounding discipline.
- Clayton Christensen, *Competing Against Luck* (2016) — Jobs-to-be-Done
  framing used in sections 2 and 3 of each persona.
- [User Interviews: The Ultimate Guide to Research Interviews](https://www.productcompass.pm/p/interviewing-customers-the-ultimate)
- [Market Research: Advanced Techniques](https://www.productcompass.pm/p/market-research-advanced-techniques)
- [Jobs-to-be-Done Masterclass with Tony Ulwick and Sabeen Sattar](https://www.productcompass.pm/p/jobs-to-be-done-masterclass-with) (video course)
