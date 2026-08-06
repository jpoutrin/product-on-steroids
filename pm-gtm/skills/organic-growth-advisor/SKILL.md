---
name: organic-growth-advisor
description: >
  Use when planning or auditing organic growth for a product — SEO/content,
  community-building, product-led virality, word-of-mouth, developer ecosystems,
  or organic partnerships — and need a sequenced playbook with realistic timelines
  and a measurement plan, without paid acquisition spend.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/organic-growth-advisor/template.md
---

# Organic Growth Playbook

## Purpose
Produce a sequenced, ICP-tailored **Organic Growth Playbook** that recommends the
highest-leverage organic channels, sequences them by effort and time-to-impact,
and supplies a concrete measurement plan — grounded in the product's current stage
and team capacity.

Organic growth is inherently long-tail. This skill is built to set honest
expectations: SEO compound effects typically take 6–18 months; community flywheels
take 3–12 months to show signal; referral programmes need product-market fit to
amplify. The skill never oversells quick wins.

**When NOT to use:**
- You need a multi-channel strategy that includes paid media — use
  `acquisition-channel-advisor` (all channels, including paid).
- You need to design or diagnose a specific growth-loop mechanic — use
  `growth-loops` (loop architecture and flywheel modelling).
- You need a full go-to-market launch plan — use `product-launch-plan`.
- Organic tactics are already chosen and you just need copy or content briefs —
  this is strategy, not content production.

## Inputs
- **Required:** product description and ICP (who it serves, job-to-be-done,
  segment). If missing, ask: "Who is the target user and what core problem does the
  product solve?" — do not assume the ICP.
- **Required:** current growth stage — pre-PMF, early traction, scaling, or
  mature. If unclear, ask: the right tactics differ dramatically by stage.
- **Optional:** time horizon (default: 12 months). Shorter horizons narrow the
  playbook to higher-velocity tactics.
- **Optional:** organic channels already in use and any existing baseline metrics
  (organic traffic, referral rate, community size). These set the benchmark and
  avoid recommending what's already running without acknowledging it.
- **Optional:** team capacity/content budget. Affects effort ratings. If absent,
  assume a lean team (1–2 people on growth).
- **Optional:** product-specific growth hooks (shareable outputs, invite flows,
  API/integrations, developer surface). These unlock PLG and viral tactics.

## Output Contract
The deliverable is an **Organic Growth Playbook** structured as (see `template.md`):

1. **Organic Growth Context** — ICP, stage, time horizon, existing baseline,
   key constraints. One paragraph; makes the playbook anchored and auditable.
2. **Recommended Tactics** — a table of tactics with columns: Tactic / Channel
   Type / Effort (S/M/L) / Time-to-Impact / Primary Metric. Each row has one
   line of rationale below the table entry explaining *why* it fits this ICP.
3. **Sequencing** — three phases (Phase 1: Months 1–3, Phase 2: Months 4–6,
   Phase 3: Months 7–12) with which tactics to start, build on, and scale, and
   the dependency logic between phases.
4. **Quick Wins vs Long-Term Bets** — explicit separation of tactics that can show
   signal within 90 days versus those that compound over 6–18 months. Both are
   included; neither is labelled as "easy" without also stating the effort cost.
5. **Measurement Plan** — one leading indicator and one lagging indicator per
   tactic, suggested tooling, and a 30/60/90-day review cadence.

Format: prose context block + tactic table + sequencing narrative + measurement
table. Length: 2–3 pages. Every claim about timeline or ROI is qualified with a
confidence note (high/med/low); no figures are stated without basis.

**GOOD (excerpt):**
> **SEO / Long-form Content** | Content | M | 9–18 months | Organic search impressions, keyword rank  
> *Why:* ICP (B2B HR managers) actively searches for "employee onboarding checklist" — 2.4K/mo volume (Ahrefs); a 10-post pillar cluster is achievable with a 2-person team in Q1.  
> **Time-to-Impact note (med confidence):** First ranking movements expected at month 4–6; meaningful traffic compounding at month 9–12. Do not report this tactic as a "quick win."

**BAD (excerpt):**
> "Start a blog and you'll see traffic in a few weeks. LinkedIn posts go viral easily."  
> — fails: no ICP fit rationale, no effort estimate, no realistic timeline, oversells speed.

## Process
1. **Clarify missing inputs** — if ICP or stage is absent, ask before proceeding.
   Do not invent the product context.
2. **Diagnose organic fit** — for each major organic channel (SEO/content,
   community, product-led virality, word-of-mouth, developer ecosystem,
   organic partnerships), assess whether the ICP and product create a natural
   growth surface. Eliminate channels with no fit; do not recommend them to
   pad the list.
3. **Select and size tactics** — for each retained channel pick 1–3 concrete
   tactics, estimate effort (S = <2 hrs/wk, M = 2–8 hrs/wk, L = >8 hrs/wk),
   and assign a realistic time-to-impact range. Cite any volume/benchmark data
   if available; otherwise label estimates as such.
4. **Sequence across phases** — order tactics by dependency and velocity.
   Phase 1 should build foundations (content infrastructure, community seed,
   referral hooks). Phase 2 accelerates. Phase 3 scales what shows signal.
5. **Separate quick wins from long-term bets** — be explicit. Quick wins
   should show measurable signal within 90 days; long-term bets compound over
   6–18 months. If nothing qualifies as a true quick win, say so — do not
   invent one.
6. **Build the measurement plan** — assign a leading indicator (early signal,
   weeks 1–4) and a lagging indicator (business outcome, months 3–12) to each
   tactic. Recommend lightweight tooling appropriate to the team's stage.
7. **Set timeline expectations in the Context block** — explicitly state that
   organic growth is a 6–18-month investment, not a 30-day channel.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] ICP and stage are explicitly stated in the Organic Growth Context — not assumed silently.
- [ ] Every recommended tactic has an effort rating (S/M/L) AND a time-to-impact range — no tactic is listed without both.
- [ ] No tactic is labelled a "quick win" with a time-to-impact > 90 days.
- [ ] At least one tactic with time-to-impact > 6 months is present and clearly labelled as a long-term bet.
- [ ] The sequencing has three distinct phases with dependency logic — not just a flat list.
- [ ] The measurement plan has at least one leading and one lagging indicator per tactic.
- [ ] Channels with no ICP fit have been dropped — the playbook is opinionated, not exhaustive.
- [ ] Timeline realism: the Context block explicitly notes that organic results compound over months, not days.
- [ ] If the exec wants results in < 90 days, the output explicitly states what is and is not achievable organically in that window.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `organic-growth-advisor-happy` (happy path) — B2B SaaS with content budget and 12-month horizon.
- `organic-growth-advisor-edge` (edge) — consumer app wanting to "go viral" with no community or product hooks.
- `organic-growth-advisor-adversarial` (adversarial) — exec wants organic results in 30 days; skill must set realistic expectations without caving.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `acquisition-channel-advisor` — full channel mix including paid; use when organic-only scope is too narrow.
- `growth-loops` — loop architecture and flywheel modelling; use when the growth mechanic design (not strategy) is the question.
- `product-launch-plan` — end-to-end launch strategy; organic growth is one component within it.
- `beachhead-segment` — first-segment selection; feeds the ICP input this skill depends on.

### External Frameworks
- Andrew Chen, *The Cold Start Problem* (2021) — network-effect and community cold-start tactics; foundational for PLG and community sequencing.
- Rand Fishkin, *Lost and Founder* (2018) and SparkToro research — realistic SEO compounding timelines and content-channel fit for B2B.
- Brian Balfour, [Reforge Growth Series](https://www.reforge.com/blog) — acquisition/retention/revenue loops; channel-product fit framework.
- Lenny Rachitsky, [How the biggest consumer apps got their first 1,000 users](https://www.lennysnewsletter.com/p/how-the-biggest-consumer-apps-got) — empirical organic seeding tactics by product type.
