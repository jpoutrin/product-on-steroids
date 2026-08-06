---
name: executive-onboarding-playbook
description: >
  Build a structured first-90-days onboarding plan for a new executive joining a
  product area. Use when a VP, CPO, or CEO is newly appointed, when a PM needs to
  brief a new leader without overwhelming them, or when establishing early credibility
  and controlling the narrative during a leadership transition.
version: 0.1.0
type: workflow
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/executive-onboarding-playbook/template.md
---

# Executive Onboarding Playbook

## Purpose
Produce a structured multi-week playbook that helps a PM successfully onboard a
new executive (VP, CPO, CEO) into a product area. The playbook controls the narrative
the executive receives, sequences information at a pace the executive can absorb,
identifies the relationships they must form early, and ensures the PM builds
credibility and trust rather than triggering information overload or confusion.

Grounded in Michael Watkins' *The First 90 Days* framework — distinguish learning
from deciding from delivering — and tailored to the product-management context where
the PM is often the executive's primary guide to the product.

**When NOT to use:**
- Routine status updates to an established executive — use `exec-update` instead.
- A one-time conversation brief (a single meeting) — use `managing-up-brief`.
- A general stakeholder map with no executive focus — use `stakeholder-map`.
- Onboarding a new team member (IC or PM); this skill is strictly for senior
  executives (VP and above) arriving into a product area the PM owns or co-owns.

## Inputs
- **Required:** the executive's role and scope (which product area(s), VP vs CPO
  vs CEO, internal hire or external). If missing, ask before proceeding.
- **Required:** the PM's relationship to the executive — direct report, peer area
  PM, or skip-level. This determines who leads the onboarding and how much
  context-setting falls to this PM specifically.
- **Optional:** the executive's background and any known priorities or hypotheses
  they arrive with — shapes what to lead with and what gaps to surface early.
- **Optional:** known landmines — technical debt, team morale issues, past
  decisions under dispute — the PM must decide whether to proactively surface these
  or wait. If missing, default to proactive disclosure on material issues.
- **Optional:** current product state — maturity (0→1, growth, scaling), OKRs,
  and biggest bets. If missing, the playbook frames the context-building sessions
  the PM would run to fill this in.

## Output Contract
The deliverable is an **executive onboarding playbook** structured as a phased
timeline (see `template.md`):

1. **Executive Snapshot** — who the executive is, their background, known
   priorities or hypotheses, and what the PM needs from them in the first 90 days.
2. **What NOT to do in Week 1** — an explicit list of anti-patterns: context dumps,
   internal politics, open issues, premature asks for decisions.
3. **Week 1: Orient and Listen** — listening-tour meetings the executive attends,
   what the PM shares (product north star, team roster, current state at a glance),
   and what to hold back. No asks, no presentations over 5 slides.
4. **Weeks 2–4: Contextualize and Connect** — deeper dives into the product
   strategy, roadmap, and key bets; relationship-building intros the PM facilitates
   (engineering lead, design lead, key customers); surfaces the first 1–2 open
   strategic questions for the executive to weigh in on.
5. **Days 30–90: Align and Decide** — where the PM seeks the executive's active
   input: resource calls, prioritization trade-offs, org decisions, external
   relationships. Includes one explicit "how are we doing?" check-in at day 30.
6. **Relationship Map** — 5–8 key relationships the executive must form; for each:
   name/role, what they care about, recommended framing for the first meeting.
7. **Landmines & Proactive Disclosures** — things the executive will discover
   eventually; better from the PM than from a surprise. Framed as informed context,
   not complaints.
8. **Early Wins to Offer** — 1–2 things the PM can help the executive claim as wins
   by day 60, building mutual credibility.

Format: prose paragraphs with bullet sub-lists. Length: 2–4 pages. Each week
section is scannable by an executive reading on mobile.

**GOOD (excerpt):**
> **Week 1 — What to hold back:** Do not surface the Q3 roadmap reprioritization
> dispute between Eng and Design. The executive needs context on *why* the
> current roadmap exists before they can form a useful opinion. Schedule that
> conversation for week 3 only after the roadmap walk-through.

**BAD (excerpt):**
> "In week 1 tell the exec everything about the product, team, roadmap, tech debt,
> stakeholders, and open decisions so they can get up to speed fast."
> — fails: information overload in week 1 destroys trust and causes premature
> pattern-matching before the executive has enough context to judge correctly.

## Process
1. **Gather inputs** — collect the executive's role, scope, background, and the
   PM's relationship to them. If any required inputs are missing, ask for them.
2. **Build the Executive Snapshot** — synthesize who this person is, what they
   bring, and what the PM needs from them.
3. **Audit the information set** — list everything the PM knows about the product
   area and explicitly decide what to sequence into Week 1 vs Weeks 2–4 vs Days
   30–90. Apply the "orient before decide" rule: no asks for decisions until the
   executive has at least 3 weeks of context.
4. **Design the listening tour** — identify the 4–6 meetings the executive should
   attend in week 1 (include direct reports, a customer call, and one cross-
   functional peer). Frame each with a single goal.
5. **Map relationships** — identify the 5–8 critical relationships; for each, write
   one sentence on what that person needs from the executive and one sentence on
   what framing the PM recommends.
6. **Surface landmines** — name the 2–3 things the executive will eventually
   discover. Decide the right moment and framing for each.
7. **Identify early wins** — find 1–2 decisions or signals the PM can set up for
   the executive to make visibly and confidently before day 60.
8. **Write the playbook** following the 8-section structure in `template.md`.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Week 1 content is information-only — no asks for decisions, no org politics,
  no more than one 5-slide overview.
- [ ] Each phase (W1 / W2–4 / D30–90) has a clear, distinct purpose and does not
  duplicate content from an adjacent phase.
- [ ] The relationship map names real people or roles (not "key stakeholders
  generally") and gives the PM concrete framing for each first meeting.
- [ ] Landmines are framed as informed context the PM proactively shares — not
  venting or complaints — with a recommended disclosure timing.
- [ ] Early wins are specific and achievable by day 60 — not aspirational outcomes
  that depend on the executive's long-term authority.
- [ ] The "What NOT to do in Week 1" section is explicit and actionable (not
  generic advice like "don't overwhelm them").
- [ ] The playbook serves the PM's credibility-building goal, not just the
  executive's information needs. Both parties benefit from the sequencing.
- [ ] If the output is written to a file, it follows `template.md` — all 8 sections
  present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `executive-onboarding-playbook-happy` (happy path) — new external CPO joining a
  mid-stage B2B SaaS company; PM is a direct report with full context.
- `executive-onboarding-playbook-edge` (edge) — internal promotion of a VP Eng to
  CPO; they know the product already but the PM must reset the relationship dynamic.
- `executive-onboarding-playbook-adversarial` (adversarial) — PM asks to "just dump
  everything into a week 1 doc so the new CEO can self-serve"; skill must push back.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `exec-update` — ongoing status cadence for an established executive; use this
  after the first-90-days onboarding is complete.
- `managing-up-brief` — prepares a single conversation with a senior stakeholder;
  complements week-by-week sessions in this playbook.
- `stakeholder-map` — general stakeholder identification and influence mapping;
  feeds the Relationship Map section of this playbook.
- `alignment-narrative` — crafts the story the PM tells about the product direction;
  the Week 2–4 roadmap walk-through draws on it.

### External Frameworks
- Michael Watkins, *The First 90 Days* (2003, updated 2013) — the foundational
  leadership-transition framework: STARS model (Start-up / Turnaround / Accelerated
  Growth / Realignment / Sustaining Success), the "orient → decide → deliver"
  sequencing, and the listening-tour methodology this skill operationalizes.
- Liz Wiseman, *Multipliers* (2010) — chapter on "The Debate Maker" informs the
  skill's principle that executives form better judgments when given structured
  context rather than premature recommendations.
- Julie Zhuo, *The Making of a Manager* (2019) — Chapter 9 ("Hiring Well") and
  her writing on onboarding new leaders: the PM's role in making a new manager's
  first weeks successful rather than reactive.
