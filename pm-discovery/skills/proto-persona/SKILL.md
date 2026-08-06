---
name: proto-persona
description: >
  Use when a team needs a fast, shared hypothesis about who they are building
  for before any user research exists — to align on assumptions, surface
  disagreements early, and define what needs to be validated.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/proto-persona/template.md
---

# Build a Proto-Persona (Pre-Research Hypothesis)

## Purpose
Produce a clearly labeled, deliberately provisional persona — built from team
assumptions rather than validated research — so the team can align on a shared
mental model of the target user, surface conflicting assumptions, and identify
exactly what needs to be tested before the persona can be trusted.

A proto-persona is created in hours, not weeks. It is a **hypothesis artifact**,
not a research artifact. Every section is explicitly tagged as assumed, and the
output concludes with a Validation Plan that maps assumptions to specific
research actions.

**When NOT to use:**
- When you already have user interview data, survey results, or ethnographic
  notes — use `user-personas` instead; the proto-persona would just ignore
  real evidence.
- When the goal is segmentation strategy (finding which segments exist) —
  use `user-segmentation` first, then build a proto-persona per segment.
- When a stakeholder wants to use the output as a final, validated persona
  without follow-up research — decline and redirect to `user-personas`.

## Inputs
- **Required:** the product or feature idea being explored — problem space,
  target context (B2B/B2C, industry, geography). If absent, ask for the
  product idea and who the team loosely thinks the user might be before
  proceeding.
- **Optional:** raw team assumptions (e.g., from a kickoff or Slack thread),
  stakeholder names or roles who have domain knowledge, any prior market
  research or analogous product context. Incorporate whatever is provided;
  explicitly note when inputs come from a single stakeholder only.

## Output Contract
The deliverable is a **proto-persona card** structured as (see `template.md`):

1. **Name & Role (Hypothesis)** — a memorable name, role/title, and the
   context in which this person encounters the problem. One short paragraph.
2. **Goals (Assumed)** — 3–5 bullet points: what this person is trying to
   achieve relevant to the product space.
3. **Frustrations (Assumed)** — 3–5 bullet points: pain points and friction the
   team believes this person faces today.
4. **Behaviors (Assumed)** — 3–5 bullet points: how this person currently
   behaves (tools, workarounds, habits) in the relevant context.
5. **Quote (Invented)** — one plausible first-person quote that captures the
   persona's mindset. Clearly labeled as invented.
6. **Validation Plan** — a numbered list of 3–5 specific research actions
   (interview questions, surveys, usability tests, analytics checks) that would
   confirm or invalidate the key assumptions, plus a "red flag" — what result
   would mean this proto-persona is wrong.

All sections are labeled **[ASSUMED]** or **[INVENTED]** to prevent readers
from treating the artifact as validated.

Format: plain prose with bullet lists. Length: ~one page. No unsupported claims
should appear without an explicit assumption label.

**GOOD (excerpt):**
> **Goals [ASSUMED]**
> - Close deals faster by reducing the back-and-forth on contract signatures.
> - Look professional to enterprise buyers without needing an IT team.
>
> **Validation Plan**
> 1. Interview 5 SDRs at Series A–C B2B SaaS companies: "Walk me through
>    the last time a deal was delayed because of contracting." (Tests:
>    frustration severity, frequency.)
> 2. Red flag: if fewer than 3 of 5 interviewees mention signature/contracting
>    as a pain point, the core frustration assumption is wrong.

**BAD (excerpt):**
> "Our user is a busy sales rep who loves automation and hates manual work."
> — fails: no assumption labels, no validation plan, no specificity, written as
> fact rather than hypothesis.

## Process
1. **Clarify scope** — confirm the product idea, target context (B2B/B2C,
   industry, geography), and any stakeholder assumptions provided. If the
   brief is from a single stakeholder, note this explicitly.
2. **Synthesize assumptions** — gather all team-supplied cues (Slack threads,
   kickoff notes, analogous products) and list the raw assumptions before
   drafting.
3. **Draft Name & Role** — give the persona a memorable name and anchor them
   in a realistic role and work/life context where they encounter the problem.
4. **Draft Goals, Frustrations, Behaviors** — write 3–5 bullets per section
   drawn directly from the synthesized assumptions; label every section
   **[ASSUMED]**.
5. **Write the Quote** — compose one plausible first-person quote that
   crystallizes the persona's frustration or aspiration; label it
   **[INVENTED]**.
6. **Write the Validation Plan** — for each load-bearing assumption (especially
   the core frustration and the primary goal), specify a concrete research
   action (interview script excerpt, survey question, analytics check). Include
   one explicit "red flag" result that would falsify the persona.
7. **Apply the assumption banner** — add a prominent disclaimer at the top of
   the card: "This is a proto-persona — a hypothesis built from team
   assumptions, not user research. Treat it as provisional until validated."
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] A prominent **[HYPOTHESIS — NOT VALIDATED]** banner appears at or near
  the top of the artifact.
- [ ] Every section of Goals, Frustrations, and Behaviors is labeled
  **[ASSUMED]** and the Quote is labeled **[INVENTED]**.
- [ ] The Validation Plan contains **≥ 3 specific research actions** (not
  vague instructions like "do interviews") tied to named assumptions.
- [ ] At least one explicit **red flag** result is stated: what outcome would
  mean this proto-persona is wrong.
- [ ] If inputs came from a single stakeholder, that limitation is flagged in
  the card.
- [ ] The artifact does **not** present any claim as validated fact.
- [ ] If the output is written to a file, it follows `template.md` — all 6
  sections present, in order, headings matching (a skill-scoped hook
  re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `proto-persona-happy` — new B2B feature idea, multi-stakeholder kickoff,
  no research yet; guards the core happy-path output quality.
- `proto-persona-edge` — single stakeholder's assumptions only; guards correct
  handling of thin-basis inputs while still producing a useful artifact.
- `proto-persona-adversarial` — user wants to use the proto-persona as a
  final, validated deliverable and skip research; guards the refusal and
  redirect to `user-personas`.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `user-personas` — research-validated persona; the natural successor once
  interviews and data validate (or replace) the proto-persona's assumptions.
- `user-segmentation` — identifies which segments exist; run this before
  building a proto-persona if the target segment itself is uncertain.
- `discovery-session` — structures the research sessions that the Validation
  Plan feeds into.

### External Frameworks
- Lean UX (Jeff Gothelf & Josh Seiden, 2013) — proto-personas originated here
  as "assumption-based personas" to bootstrap team alignment before discovery.
- IDEO Human-Centred Design Kit — emphasizes provisional artifacts as starting
  points for empathy, not endpoints.
- Teresa Torres, *Continuous Discovery Habits* (2021) — opportunity mapping
  starts with provisional user assumptions before evidence is gathered.
