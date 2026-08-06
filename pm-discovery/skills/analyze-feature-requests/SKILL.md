---
name: analyze-feature-requests
description: >
  Categorize and prioritize feature requests by theme, impact, effort, and
  strategic alignment. Use when reviewing customer feature requests, triaging
  a backlog, or making prioritization decisions.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/analyze-feature-requests/template.md
---

# Analyze and Prioritize Feature Requests

## Purpose
Transform a collection of incoming feature requests (from support tickets, sales conversations, NPS comments, community forums, or a backlog) into a structured, prioritized analysis that groups requests by theme, evaluates strategic fit, scores impact and effort, and surfaces the highest-value opportunities. This analysis informs backlog sequencing and helps avoid feature creep driven by vocal customers rather than evidence.

**When NOT to use:** mining qualitative insights from raw customer conversations (use `voice-of-customer-miner`), de-risking solution bets with assumption testing (use `prioritize-assumptions`), or defining your product strategy and vision (use skills in `pm-strategy`). This skill assumes you already have a set of requests; it does not discover or validate customer needs.

## Inputs
- **Required:** a set of feature requests — anywhere from 5 to 100+ — in any format (CSV, spreadsheet, list of descriptions, bullet points). Each request should include a title and brief description; optionally include source (support, sales, community), how many times it was asked, or customer segment.
- **Optional:** your current product goals or strategy statement (helps evaluate strategic alignment); any constraints or context (roadmap commitments, resource limits, market threats).

## Output Contract
The deliverable is a **feature request analysis report** with these sections (see `template.md`):

1. **Request Summary** — total count, sources represented, and a rollup of coverage.
2. **Thematic Clusters** — 3–8 themes, each with grouped requests, frequency, and a one-sentence theme name.
3. **Opportunity Scoring** — for each theme (or top N requests if no clustering), a score on Impact (customer value + breadth), Effort (development cost), Risk (technical or market uncertainty), and Strategic Alignment (fit with stated goals). Use a simple 1–5 scale or the Opportunity Score formula (Impact × (1 − Satisfaction)).
4. **Top 3–5 Priorities** — ranked by the scoring model, each with rationale, key risks, and the minimal test to validate the assumption that it will move the needle.
5. **Alternative & declining patterns** — themes or requests that scored low and why, brief notes on deferred requests (so they are not forgotten).

Format: prose + tables. Length: ~2–4 pages. No single request should be left unaddressed or scored.

**GOOD (excerpt):**
> **Theme: Offline Access (4 requests, sales + support)**
> - Importance: 4/5 (affects mobile users in low-connectivity zones)
> - Satisfaction: 2/5 (current app requires internet)
> - Opportunity Score: 4 × 0.8 = 3.2
> - Effort: 4/5 (requires local sync architecture)
> - Strategic alignment: 3/5 (fits product vision, not a P1)
> - Rationale: High demand from a growing use case, but expensive to build. Recommend a lightweight pilot (single feature, one segment) before full offline.

**BAD (excerpt):**
> "Add dark mode, add webhooks, let users invite friends — these should all be done soon because many people asked."
> — fails: no clustering, no scoring, no trade-off rationale, no risk or effort assessment, no distinction between strategic wishes and tactical feature requests.

## Process
1. **Intake & dedupe** — parse the request set, standardize format, identify duplicates or near-duplicates (group them).
2. **Cluster by theme** — look for patterns (user problem, system area, customer segment). Give each theme a name and a count of requests in it.
3. **Score each theme or top request** — Impact (1–5), Effort (1–5), Risk (1–5), Strategic Alignment (1–5). Optionally compute an Opportunity Score or prioritization index.
4. **Synthesize rationales** — for the top 3–5, write a one-paragraph rationale (why it scores high, what risk to watch, what the smallest validation step is).
5. **Surface trade-offs** — explicitly note themes that scored low and why (e.g., "High effort, low impact" or "Out of strategic scope").
6. **Run the Quality Bar below; revise if any item fails; then return.**

## Quality Bar
Before returning, confirm:
- [ ] Every request is assigned to a theme or listed as standalone; no request is orphaned or ignored.
- [ ] Themes are named clearly and their request count is stated.
- [ ] Impact, Effort, Risk, and Strategic Alignment are scored (or Opportunity Score computed) for at least the top 5 themes / requests.
- [ ] Top 3–5 priorities have a clear rationale tied to their scores, not just a gut call.
- [ ] At least one trade-off or declining request is explained (e.g., why something scored low).
- [ ] If the output is written to a file, it follows `template.md` — all 5 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `analyze-feature-requests-happy` (happy path) — structured dataset with clear clusters, enough context to score confidently.
- `analyze-feature-requests-edge` (edge) — mixed format, some requests vague or partial, scoring constrained by missing context.
- `analyze-feature-requests-adversarial` (adversarial) — contradictory requests, high emotion, pressure to make everything a P1.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `voice-of-customer-miner` — mines qualitative insights from raw customer conversations, interview transcripts, or support tickets; outputs themes and sentiment. Use this *before* feature requests have been formally articulated.
- `prioritize-assumptions` — de-risks a solution bet by testing assumptions and running lean experiments. Use this *after* a feature is prioritized to validate whether it will move the needle.

### External Frameworks
- Dan Olsen, *The Lean Product Playbook* (2015), Ch. 4 — **Opportunity Score** (Importance × (1 − Satisfaction)) is the canonical framework for feature prioritization from customer feedback.
- Kano Model — categorizes features into basic needs, performance needs, and delighters; helps avoid building table-stakes as if they were strategic wins.
- Digging into RICE (Reach, Impact, Confidence, Effort) — common in product orgs, especially for weighing different customer segments' requests against each other.
