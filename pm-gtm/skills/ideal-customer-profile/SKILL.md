---
name: ideal-customer-profile
description: >
  Define the firmographic, behavioral, and situational profile of the customer
  who gets maximum value from the product and is most profitable to acquire and
  retain. Use when targeting a new market, aligning sales and marketing on who
  to pursue, deciding who to disqualify, or revisiting segment focus after
  traction data has accumulated.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/ideal-customer-profile/template.md
---

# Ideal Customer Profile

## Purpose
Produce a structured ICP document that specifies the firmographic, behavioral,
and situational characteristics of the customer segment that (a) derives the
most value from the product and (b) is most efficient to acquire and retain.
The ICP is a strategic choice, not a description — it includes explicit
inclusion criteria, disqualification criteria (Negative ICP), and the evidence
behind each claim.

**When NOT to use:**
- Individual user archetypes within a known segment → use `user-personas`
  (pm-discovery): personas are human archetypes; ICP is a firmographic/segment
  profile.
- Choosing the very first segment to enter → use `beachhead-segment`: that
  skill optimizes for fastest initial wedge; ICP defines the long-term target.
- Splitting an existing user base into sub-groups for analysis → use
  `user-segmentation` (pm-discovery): segmentation divides; ICP makes a
  strategic commitment about who to serve.
- Validating whether product-market fit exists → use a PMF survey skill first;
  then return here once you have retention signal to anchor from.

## Inputs
- **Required:** Product description and primary value proposition — what problem
  it solves and for whom. If the user hasn't provided this, ask before
  proceeding; the ICP cannot be derived without knowing what value is being
  delivered.
- **Required (B2B):** At least one of: existing customer list with revenue/LTV
  data, win/loss analysis, customer interview notes, or churn data. If none
  exists (pre-customer stage), say so explicitly and proceed with hypothesis
  mode (flag all claims as unvalidated).
- **Required (B2C):** Psychographic research, behavioral analytics, or cohort
  data distinguishing high-engagement from low-engagement users.
- **Optional:** Sales motion (PLG, inside sales, enterprise), pricing tier,
  geographic constraints, strategic priorities (e.g., "expand upmarket"). These
  shape which firmographic traits are relevant.
- **Optional:** Existing ICP hypothesis — the skill will stress-test and refine
  it rather than start from scratch.

## Output Contract
The deliverable is a structured **ICP document** (see `template.md`):

1. **ICP Summary** — one-paragraph strategic statement of who the ICP is and
   why, suitable for an exec brief or a sales deck header.
2. **Firmographic Profile (B2B) / Demographic & Behavioral Profile (B2C)** —
   inclusion criteria with specifics (e.g., company size range, industry
   verticals, tech stack requirements, revenue band; or for B2C: age/life-stage
   range, psychographic traits, platform/channel behavior).
3. **Trigger Events** — the conditions or moments that make this customer ready
   to buy now (e.g., Series A fundraise, regulatory change, new hire of a VP
   Engineering, switching from a legacy tool after a pain event).
4. **Buying Process** — who discovers, who evaluates, who approves, typical
   sales-cycle length, key objections, and what "done evaluating" looks like.
5. **Negative ICP** — explicit disqualification criteria: characteristics that
   signal a prospect will churn, won't pay, or will cost more to serve than
   they return.
6. **Evidence & Validation Notes** — sources for each claim (customer interview,
   cohort analysis, win/loss data) and confidence levels (validated / hypothesis
   / assumption). Flags which criteria most need validation.

Format: structured document with section headings, short prose plus bulleted
criteria lists. Length: 1–2 pages. Every inclusion/exclusion criterion is either
data-backed or flagged as a hypothesis.

**GOOD (excerpt):**
> **Firmographic — Company Size:** 50–500 employees. Below 50: no dedicated ops
> function (no budget owner for this category). Above 500: procurement cycle
> extends to 6+ months and requires MSA — outside our current sales motion.
> *Source: win/loss analysis, Q1 2025 — 78% of closed-won deals in this band.*

**BAD (excerpt):**
> "Our ICP is mid-market B2B SaaS companies that need better collaboration."
> — fails: no size range, no industry, no disqualification criteria, no
> evidence, "need better collaboration" is not a trigger event.

## Process
1. **Anchor on value delivery** — identify what job the product does best and
   who experiences the most acute version of that pain. If customer data exists,
   start there; if not, articulate the hypothesis explicitly.
2. **Segment existing customers by outcome** — rank by LTV, time-to-value,
   churn rate, expansion revenue, and NPS. The ICP emerges from the top cohort,
   not the average customer.
3. **Extract firmographic patterns (B2B)** — company size, industry/vertical,
   geography, tech stack, company stage, department structure, and budget
   profile of the top cohort. Note outliers and whether they are signal or noise.
4. **Extract psychographic and behavioral patterns (B2C)** — life stage,
   motivations, platform habits, frequency of need, and what triggers a search
   for a solution.
5. **Map trigger events** — what changed in the customer's world just before
   they evaluated the product? These are the moments to target in GTM motion.
6. **Document the buying process** — roles involved (champion, economic buyer,
   technical gatekeeper), decision timeline, common objections, and what
   "sufficient proof" looks like to close.
7. **Define the Negative ICP** — who looks like the ICP but consistently churns,
   under-uses the product, generates high support cost, or won't pay the target
   price. Make disqualification criteria explicit so sales can use them.
8. **Rate evidence confidence** — for each criterion, tag it: validated (data
   from ≥ 5 customers), hypothesis (directional signal from < 5), or assumption
   (reasoned but untested). Flag the highest-uncertainty criteria for validation.
9. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The ICP Summary is a strategic commitment — it names a specific segment,
  not a vague "mid-market" or "enterprise" label.
- [ ] Every inclusion criterion (firmographic or behavioral) has at least one
  specific, testable value (e.g., "50–500 employees", not "mid-size").
- [ ] Trigger events are present — at least two situations that signal readiness
  to buy now, not just descriptors of who the customer is.
- [ ] A Negative ICP section exists with at least two explicit disqualifiers.
- [ ] Every criterion is tagged with a confidence level (validated / hypothesis /
  assumption). No criterion appears without a tag.
- [ ] The ICP is distinct from a persona: it describes a segment profile, not a
  named individual archetype.
- [ ] If output is written to a file, it follows `template.md` — all six sections
  present, in order, headings matching (a skill-scoped hook re-checks this on
  write).

## Validation & Eval
Scenario cards live in `evals/`:
- `ideal-customer-profile-happy` — B2B SaaS with clear best-customer patterns
  from existing retention and win/loss data.
- `ideal-customer-profile-edge` — early-stage startup with zero customers yet;
  skill must produce a hypothesis-mode ICP and flag every criterion.
- `ideal-customer-profile-adversarial` — sales team input that wants the ICP to
  include every company with a budget; skill must resist scope creep and enforce
  disqualification criteria.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `beachhead-segment` (pm-gtm) — chooses the first segment to enter; consumes
  the ICP's inclusion criteria to define the initial wedge.
- `user-personas` (pm-discovery) — creates individual archetypes within the ICP
  segment; runs after ICP is defined.
- `user-segmentation` (pm-discovery) — divides a user base into sub-groups;
  feeds data that can sharpen ICP firmographic boundaries.
- `competitor-analysis` (pm-gtm) — competitive positioning data can reveal which
  ICP segments competitors are ignoring, informing ICP differentiation.

### External Frameworks
- Geoffrey Moore, *Crossing the Chasm* (1991) — the "whole product" lens and
  the discipline of targeting a beachhead before expanding ICP scope.
- Clayton Christensen, *Jobs to Be Done* — behavioral and motivational framing
  for trigger events and the functional/emotional/social job structure used in
  the Firmographic + Trigger sections.
- Winning by Design, *ICP and Revenue Architecture* — operationalizing ICP
  across sales, marketing, and CS with shared disqualification criteria.
- [5 GTM Principles You Should Know as a PM](https://www.productcompass.pm/p/5-gtm-principles-with-frameworks-templates) — Paweł Huryn's GTM overview covering ICP, positioning, and go-to-market motion alignment.
