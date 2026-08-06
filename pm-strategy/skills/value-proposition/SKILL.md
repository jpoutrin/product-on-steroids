---
name: value-proposition
description: >
  Map a Value Proposition Canvas — customer jobs, pains, and gains against your
  pain relievers, gain creators, and products — then distill it into a crisp
  value-proposition statement. Use when designing a value proposition or testing
  problem/solution fit for a specific customer segment.
when_to_use: >
  Invoke when articulating why a named segment should choose your product,
  preparing a JTBD-grounded value map before launch messaging, or running a
  fit analysis to surface orphan features and uncovered top pains/gains.
argument-hint: "[segment] [product or offering]"
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a9
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/value-proposition/template.md
---

# Design a Value Proposition (Canvas + Statement)

## Purpose
Produce a **Value Proposition Canvas** for one customer segment — the customer
profile (jobs to be done, pains, gains) mapped explicitly against the value map
(pain relievers, gain creators, products & services) — and distill it into a
single crisp value-proposition statement. The canvas exposes **fit**: whether
each reliever/creator actually addresses a ranked pain or gain, or is an orphan
feature nobody asked for. Supports problem/solution-fit decisions, feature
prioritization, and segment-specific messaging.

**When NOT to use:** writing polished positioning or headline copy for a launch
(use gtm `value-prop-statements` — that is marketing copy; this is the
strategy-side fit analysis behind it); sizing the opportunity (use
`market-sizing`); or picking which segment to serve first (use
`beachhead-segment`). This skill assumes the segment is already chosen and maps
value for it — it does not select the segment or sell the message.

## Inputs
- **Required:** the **one customer segment** and the **product/offering**. If a
  segment isn't named, ask for it and refuse to map "everyone" — a canvas is
  segment-specific. If the product is only a rough idea, proceed but label the
  value map as hypotheses.
- **Optional:** customer research / interview notes (cite them and mark which
  jobs, pains, gains are evidence-backed vs assumed), current alternatives the
  segment uses today, feature list, JTBD statements, willingness-to-pay signals.

## Output Contract
The deliverable is a **Value Proposition Canvas** for one segment, structured as
(see `template.md`):

1. **Segment** — the single customer segment this canvas is for (one line).
2. **Customer Profile — Jobs** — the jobs to be done (functional, social,
   emotional), the top ones **ranked** by importance to the customer.
3. **Customer Profile — Pains** — frustrations, risks, and obstacles, ranked by
   severity; each tagged *evidence* or *assumption*.
4. **Customer Profile — Gains** — outcomes and benefits the customer wants,
   ranked by relevance; each tagged *evidence* or *assumption*.
5. **Value Map — Pain Relievers** — how the product kills specific ranked pains;
   each reliever names the pain it maps to.
6. **Value Map — Gain Creators** — how the product produces specific ranked
   gains; each creator names the gain it maps to.
7. **Value Map — Products & Services** — the offering elements the relievers and
   creators rest on.
8. **Fit Analysis** — which top pains/gains are covered vs uncovered, and which
   relievers/creators are **orphans** (map to no ranked pain/gain); alternatives
   the segment uses today and why they'd switch.
9. **Value Proposition Statement** — one crisp 1–2 sentence statement:
   *For [segment] who [job/need], our [product] [key benefit] unlike [alternative].*

Format: prose + bullets, with a two-column canvas table (profile ↔ map). Length:
~1–2 pages. Every pain and gain is tagged evidence-or-assumption; every reliever
and creator names the ranked item it maps to.

**GOOD (excerpt):**
> **Pain (P1, evidence — 6/8 interviews):** non-designers waste hours in
> PowerPoint and still ship off-brand graphics.
> **Pain Reliever → P1:** drag-and-drop branded templates produce on-brand
> graphics in minutes, no design skill needed.
> **Fit:** P1 (top pain) is covered. *Orphan:* the "AI background remover" gain
> creator maps to no ranked gain — deprioritize or validate.
> **Statement:** For SMB marketers who need on-brand graphics fast, Canva turns
> hours of design work into minutes — unlike Photoshop's steep learning curve.

**BAD (excerpt):**
> "Customers want great design. Our product has templates, AI tools, and
> collaboration. It's better than the competition."
> — fails: no segment, jobs/pains/gains not separated or ranked, relievers map
> to nothing, no evidence/assumption tags, no fit analysis, statement is generic.

## Process
1. **Fix the segment** — confirm exactly one segment; refuse "everyone."
2. **Profile jobs** — list functional/social/emotional jobs to be done; rank the
   top few by importance to the customer, not to you.
3. **Profile pains** — list frustrations/risks/obstacles, rank by severity, tag
   each *evidence* or *assumption*.
4. **Profile gains** — list desired outcomes/benefits, rank by relevance, tag
   each *evidence* or *assumption*.
5. **Map pain relievers** — for each top pain, state how the product relieves it;
   name the pain each reliever targets.
6. **Map gain creators** — for each top gain, state how the product creates it;
   name the gain each creator targets.
7. **List products & services** — the offering elements relievers/creators rest on.
8. **Analyze fit** — flag uncovered top pains/gains and orphan relievers/creators;
   name current alternatives and the switching reason.
9. **Write the statement** — distill into one 1–2 sentence value-proposition
   statement in the *For/who/our/unlike* shape.
10. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The canvas is scoped to **exactly one named segment** (no "everyone").
- [ ] Jobs, pains, and gains are **separated** (not merged) and the top items are **ranked**.
- [ ] Every pain and gain is tagged **evidence** or **assumption**.
- [ ] Every pain reliever names the **ranked pain** it maps to; every gain creator names the **ranked gain** it maps to.
- [ ] The **Fit Analysis** explicitly calls out uncovered top pains/gains **and** orphan relievers/creators.
- [ ] Current **alternatives** and the reason to switch are named.
- [ ] The **value-proposition statement** is 1–2 sentences and follows the *For/who/our/unlike* shape.
- [ ] If the canvas is written to a file, it follows `template.md` — all 9 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `value-proposition-happy` (happy path) — a B2B segment with interview evidence; full canvas + fit + statement.
- `value-proposition-edge` (edge) — a rough pre-product idea with no research, forcing an all-assumption canvas that is honestly labeled.
- `value-proposition-adversarial` (adversarial) — an "everyone loves it" feature-led ask the skill must scope to one segment and confront with fit/orphans.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `beachhead-segment` — chooses the segment this canvas is built for; run it first when the segment is undecided.
- `market-sizing` — sizes the opportunity behind the segment; this canvas explains *why* that market would buy.
- `value-prop-statements` (pm-gtm) — turns this fit analysis into launch-ready positioning and messaging copy.

### External Frameworks
- Alexander Osterwalder et al., *Value Proposition Design* (2014) — the canonical **Value Proposition Canvas** (customer profile: jobs/pains/gains ↔ value map: pain relievers/gain creators/products) and the concept of **fit** this skill operationalizes.
- Clayton Christensen — **Jobs to Be Done**: framing the customer profile around the progress the customer is trying to make, not demographics.
- W. Chan Kim & Renée Mauborgne, *Blue Ocean Strategy* — the **Value Curve** for visually comparing the offering against alternatives across the factors the fit analysis surfaces.
