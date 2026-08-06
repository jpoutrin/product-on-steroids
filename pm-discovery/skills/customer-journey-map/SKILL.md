---
name: customer-journey-map
description: >
  Map the end-to-end customer experience across every stage and touchpoint,
  surfacing emotions, pain points, and improvement opportunities. Use when
  diagnosing friction in the user journey, planning onboarding improvements,
  aligning cross-functional teams on the customer experience, or building the
  discovery foundation before redesigning a flow.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/customer-journey-map/template.md
---

# Customer Journey Map

## Purpose
Produce a structured, stage-by-stage map of the holistic customer experience —
from first awareness through active use and eventual offboarding — for a specific
persona and job-to-be-done. The map captures actions, touchpoints, thoughts,
emotions, pain points, and opportunities at each stage, and concludes with a
prioritized set of improvement recommendations. It supports discovery, onboarding
redesign, retention analysis, and cross-functional alignment.

**When NOT to use:**
- **Storyboard** — if you need a narrative, scene-by-scene UX sequence for a
  *single* scenario or prototype flow, use `storyboard`. A CJM covers the whole
  relationship arc (awareness → advocacy); a storyboard zooms into one moment.
- **User personas** — if the ask is to *define* who the user is rather than map
  what they do, use `user-personas` first, then feed the persona here.
- **Funnel / analytics audit** — if quantitative drop-off rates are already known
  and the goal is to diagnose *why* users drop at a specific step, a targeted
  analytics or session-recording review is more direct than a full CJM.
- **Process maps / service blueprints** — if the primary audience is internal
  operations (backend systems, staff workflows), a service blueprint or process map
  is more appropriate than a customer-facing journey map.

## Inputs
- **Required:** the product or experience to map, and the primary persona (role,
  segment, or JTBD). If the persona is not provided, ask for it before proceeding —
  a generic "user" journey is not actionable.
- **Optional:**
  - Customer research materials (interview transcripts, survey data, support
    tickets, session recordings, NPS verbatims) — read and synthesize them into
    the map.
  - Scope constraint: which journey stages to focus on (e.g., onboarding only,
    or post-churn re-engagement).
  - Emotional scale preference: sentiment labels (frustrated / neutral / delighted)
    or emoji indicators — default is sentiment labels.
  - Output format preference: narrative prose per stage, table, or both — default
    is the stage table plus a critical-moments callout and prioritized recommendations.

## Output Contract
The deliverable is a **customer journey map document** structured as follows (see
`template.md`):

1. **Persona & Scope** — who is mapped, their JTBD, and which stages are in scope.
2. **Journey Stage Table** — one row per stage (Awareness → Consideration →
   Acquisition → Onboarding → Engagement → Retention → Advocacy), with columns
   for: Touchpoints, User Actions, Thoughts & Questions, Emotion, Pain Points,
   and Opportunities.
3. **Critical Moments** — explicit callouts for the Aha Moment, Moments of Truth
   (commitment / abandonment decision points), and top Churn Triggers.
4. **Prioritized Improvements** — ranked list of opportunities by impact
   (conversion or retention) × effort, with quick-win vs. strategic-investment
   labeling.

Format: Markdown table for the stage grid, prose callouts for Critical Moments,
numbered list for Improvements. Length: ~2–3 pages. Every pain point has at
least one linked opportunity; every opportunity is grounded in a stage and
touchpoint, not free-floating.

**GOOD (excerpt):**
> **Stage: Onboarding** | Touchpoints: welcome email, in-app checklist, docs |
> Emotion: Anxious → Curious | Pain Point: "Checklist has 9 steps; user
> abandons at step 4 (integrations) — too complex, no context."  |
> Opportunity: "Add a guided setup wizard for the two most common integration
> paths; reduce mandatory steps to ≤ 3 for day-1 value."

**BAD (excerpt):**
> "Users feel frustrated during onboarding."
> — fails: no touchpoint, no specific action, emotion is label-only with no
> context, pain point is too vague to act on, no linked opportunity.

## Process
1. **Confirm persona and JTBD** — if not supplied, ask for segment, role, and
   the primary goal the customer is trying to achieve. Do not proceed with a
   generic "user."
2. **Ingest research artifacts** — read any supplied transcripts, tickets, or
   analytics; note which stages and pain points are evidence-backed vs. inferred.
3. **Define the stage set** — adapt the default seven stages (Awareness /
   Consideration / Acquisition / Onboarding / Engagement / Retention / Advocacy)
   to the product; merge or split stages as needed (e.g., a pure self-serve B2C
   product may collapse Consideration into Awareness; an enterprise product may
   expand Acquisition into Evaluation + Procurement).
4. **Map each stage** — for every stage document: touchpoints (where), user
   actions (what), thoughts & questions (what's on their mind), emotion (how they
   feel), pain points (friction, confusion, drop-off risk), and opportunities
   (how to improve).
5. **Identify critical moments** — flag the Aha Moment (first experience of core
   value), Moments of Truth (commitment or abandonment decision points), and top
   Churn Triggers (where users most commonly drop off).
6. **Draft prioritized improvements** — rank opportunities by impact on conversion
   or retention, label quick wins (≤ 1 sprint) vs. strategic investments, and
   flag which require deeper discovery before scoping.
7. **Label evidence vs. inference** — mark each pain point and opportunity as
   [evidence] (grounded in research) or [inference] (hypothesis to validate).
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The persona is specific (role/segment + JTBD), not a generic "user."
- [ ] Every stage in scope has all six columns populated (Touchpoints, Actions,
  Thoughts, Emotion, Pain Points, Opportunities) — no blank cells.
- [ ] Every pain point has at least one linked opportunity in the same row.
- [ ] Critical Moments are called out explicitly: Aha Moment, at least one Moment
  of Truth, and top Churn Triggers.
- [ ] Prioritized Improvements are ranked by impact × effort and labeled
  quick-win vs. strategic.
- [ ] Evidence-backed findings are distinguished from inferences/hypotheses.
- [ ] The journey stages are appropriate for the product type (not blindly copied
  from the default seven if they don't fit).
- [ ] If the output is written to a file, it follows `template.md` — all four
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `customer-journey-map-happy` — well-scoped B2C SaaS product with a clear
  persona and partial research; guards the baseline end-to-end output quality.
- `customer-journey-map-edge` — sparse-data B2B enterprise product where most
  stages must be inferred; guards correct labeling of evidence vs. inference and
  appropriate scope narrowing.
- `customer-journey-map-adversarial` — vague ask ("map the user journey for my
  app") with no persona; guards that the skill elicits the persona before
  proceeding rather than producing a generic map.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `user-personas` — define the persona before mapping their journey; feed the
  persona's JTBD, goals, and frustrations directly into Step 1 of this skill.
- `storyboard` — for a narrative UX sequence zoomed into one scenario or
  prototype flow; use after the CJM identifies which moment to detail.
- `discovery-interview-synthesis` — synthesize raw interview transcripts into
  the evidence layer that populates pain points and opportunities in this skill.

### External Frameworks
- Nielsen Norman Group, *Journey Mapping 101* (2020) — canonical definition of
  the journey map artifact, distinction from service blueprints, and guidance on
  evidence-based vs. hypothesis maps.
- Kalbach, J., *Mapping Experiences* (2016, O'Reilly) — comprehensive treatment
  of journey maps, experience maps, and service blueprints with worked examples.
- [User Journey Mapping 101 — Product Compass](https://www.productcompass.pm/p/user-journey-mapping-101) — concise practitioner primer on mapping stages and surfacing actionable insights.
- [Funnel Analysis 101 — Product Compass](https://www.productcompass.pm/p/funnel-analysis) — complements the CJM with quantitative drop-off data to prioritize which stage pain points matter most.
