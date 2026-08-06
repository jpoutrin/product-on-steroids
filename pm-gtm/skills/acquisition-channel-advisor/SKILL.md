---
name: acquisition-channel-advisor
description: >
  Prioritize acquisition channels for a product given ICP, stage, and budget.
  Use when choosing which channels to invest in, building a GTM channel strategy,
  evaluating channel mix, or pressure-testing a channel bet.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/acquisition-channel-advisor/template.md
---

# Acquisition Channel Advisor

## Purpose
Produce a prioritized channel scorecard — grounded in the Traction 19-channel
framework (Gabriel Weinberg & Justin Mares) — that tells a PM or founder exactly
which acquisition channels to focus on now, why, and how to run a cheap first
experiment. Each channel is scored on four dimensions (reach, conversion, cost,
ICP fit) so the recommendation is defensible and can be updated as data comes in.

**When NOT to use:**
- Specific campaign ideas inside a channel (use `marketing-ideas`; that skill
  designs the creative or copy within a channel you already chose).
- Organic-only situations where paid is off the table and the question is purely
  about SEO, virality, or community loops (use `organic-growth-advisor`).
- Competitive teardown (use `competitor-analysis`); channel intel may feed into
  the ICP fit score here, but the teardown itself is a separate artifact.
- Revenue or pricing decisions — this skill addresses customer inflow only.

## Inputs
- **Required:** product type and core value proposition. Without these, ask
  before scoring; channel fit depends heavily on what you are selling.
- **Required:** ICP description — industry, company size or demographics,
  role/persona, primary pain. If absent, ask for these before scoring.
- **Required:** stage — pre-PMF / early-traction / scaling. Stage determines
  which channels are testable vs. premature to invest in.
- **Required (budget):** monthly acquisition budget or "zero / bootstrapped".
  If the user does not provide it, ask; zero budget eliminates paid channels.
- **Optional:** geography or language constraints (default: global / English).
- **Optional:** existing channel experiments and results — include in scoring
  if provided; note their absence and surface assumptions instead.
- **Optional:** target CAC or payback period — used to flag channels where
  cost is structurally unlikely to meet the target.

## Output Contract
The deliverable is a **channel scorecard and test plan** (see `template.md`):

1. **Context & Constraints** — product type, ICP summary, stage, budget ceiling,
   and any hard constraints (geography, CAC target). One short paragraph.
2. **Channel Evaluation** — a table scoring every considered channel on: Reach
   (addressable volume, H/M/L), Conversion (typical rate for this ICP, H/M/L),
   Cost (budget required to test meaningfully, H/M/L), ICP Fit (how well this
   channel reaches the ICP, H/M/L), and a weighted Score (0–10). Include at
   least 8 channels drawn from the Traction 19; justify exclusions briefly.
3. **Top 3 Recommended Channels** — the three highest-scoring channels with
   a one-sentence rationale for each and an explicit "why not #4" note.
4. **Test Protocol (Channel 1)** — a concrete 30-day experiment: hypothesis,
   leading metric, budget, success threshold, and failure signal.
5. **Next Review Trigger** — the signal or date at which the channel mix
   should be revisited (e.g., "when CAC stabilises across 50 paid conversions"
   or "after 90 days of content indexing").

Format: short prose intro + one evaluation table + numbered recommendations +
experiment block. Length: 1–2 pages. Every score has a one-line justification;
no unsupported assertions.

**GOOD (excerpt):**
> | LinkedIn Ads | H | M | H | H | 7.2 | Large ICP audience; high CPC (~$8–12) offset by high conversion rate for B2B SaaS demos. |
> **Channel 1 — LinkedIn Ads:** Hypothesis: targeting "VP Engineering at 50–200 person SaaS" will yield demo-request CVR ≥ 3% at $50 CPL or below. Budget: $2,000 for 30 days. Success: ≥ 40 demo requests at ≤ $50 CPL. Failure signal: < 10 clicks with ≥ 500 impressions → creative issue; or clicks but 0 conversions → landing page issue.

**BAD (excerpt):**
> "We recommend Facebook Ads, Google Ads, and LinkedIn. These are the biggest channels."
> — fails: no scoring, no ICP fit justification, no test protocol, no ranked rationale.

## Process
1. **Gather inputs** — confirm product type, ICP, stage, and budget. If any
   required input is missing, ask before proceeding; do not guess the ICP.
2. **Screen the Traction 19** — walk all 19 channels; eliminate those that are
   structurally incompatible (e.g., trade shows for a $0 budget, viral loop
   for a tool with single-user sessions). Note each elimination briefly.
3. **Score candidates** — for the remaining channels, assign H/M/L on each
   of the four dimensions (Reach, Conversion, Cost, ICP Fit) using explicit
   reasoning tied to the provided ICP and stage.
4. **Compute weighted scores** — Reach × 0.2 + Conversion × 0.3 + Cost × 0.2
   + ICP Fit × 0.3, mapping H=3, M=2, L=1. Round to one decimal.
5. **Rank and pick top 3** — select the three highest-scoring channels;
   explain why the fourth-ranked channel was not included.
6. **Write the test protocol** — for Channel 1, define a 30-day experiment
   with hypothesis, leading metric, budget, success threshold, and failure signal.
7. **Set the review trigger** — specify the data signal or calendar date that
   should prompt re-evaluation of the channel mix.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] At least 8 of the Traction 19 channels are explicitly considered and
  either included in the table or eliminated with a one-line reason.
- [ ] Every channel in the table has scores on all four dimensions with a
  brief justification in the table row.
- [ ] The Top 3 section includes a "why not #4" note (prevents sycophantic
  agreement with whatever the user mentioned first).
- [ ] The Test Protocol has a falsifiable success threshold and a named
  failure signal (not just "track the metrics").
- [ ] Budget constraints are respected: any channel requiring spend the user
  cannot cover is either eliminated or flagged as "future / post-funding".
- [ ] The adversarial check: if the user advocates for a channel that scores
  poorly, the scorecard reflects the honest score — not a revised score to
  match the user's preference.
- [ ] If the output is written to a file, it follows `template.md` — all
  5 sections present, in order, headings matching (a skill-scoped hook
  re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `acquisition-channel-advisor-happy` (happy path) — B2B SaaS, $0 budget,
  pre-PMF, founder-led sales.
- `acquisition-channel-advisor-edge` (edge) — B2C consumer app with saturated
  paid channels and thin organic signal.
- `acquisition-channel-advisor-adversarial` (adversarial) — exec insists on
  a channel that scores poorly; skill must give honest scorecard.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `marketing-ideas` — generates specific campaign concepts within a channel
  this skill has already prioritized; downstream consumer of channel choices.
- `organic-growth-advisor` — deep-dives organic loops (SEO, virality, community);
  this skill's organic channel scores are an entry point to that deeper analysis.
- `beachhead-segment` — the ICP definition this skill requires as input; run
  it first if the ICP is not yet crisp.
- `market-sizing` — reach estimates in the channel table should be consistent
  with the SAM/SOM established by this skill.

### External Frameworks
- Gabriel Weinberg & Justin Mares, *Traction* (2014) — the 19-channel taxonomy
  and the Bullseye Framework (outer ring → promising → focus) that informs
  the screening and ranking process in this skill.
- Andrew Chen, "The Law of Shitty Clickthroughs" — explains channel saturation
  over time; informs the edge-case handling for saturated paid channels.
- Brian Balfour, "Why You Shouldn't Build A Growth Team" — model-channel fit
  reasoning that underpins the ICP Fit dimension weighting.
