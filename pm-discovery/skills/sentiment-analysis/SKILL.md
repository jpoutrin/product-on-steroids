---
name: sentiment-analysis
description: >
  Synthesize a body of text (app reviews, support tickets, NPS comments,
  survey responses) into a sentiment report with overall score, theme
  breakdown, exemplar quotes, and recommended actions. Use when analyzing user
  feedback at scale, running sentiment analysis on reviews or surveys, or
  identifying satisfaction patterns.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/sentiment-analysis/template.md
---

# Analyze Sentiment & Themes in Customer Feedback

## Purpose
Read a collection of customer feedback (app reviews, support tickets, NPS
comments, survey responses, social listening) and synthesize it into a
structured sentiment report: identify overall sentiment polarity (positive /
negative / neutral), group feedback by theme, score the strength of each
theme, surface representative quotes, and recommend actions. Supports
product positioning, roadmap prioritization, customer success, and support
triage decisions — especially in early-stage or high-velocity products where
raw feedback volume exceeds the team's capacity to read it individually.

**When NOT to use:** structured backlog analysis or feature-request
prioritization (use `analyze-feature-requests`), broader qualitative mining
or jobs-to-be-done discovery (use `voice-of-customer-miner`), or competitive
market analysis (use skills in `pm-strategy` or `pm-gtm`). This skill assumes
you have raw feedback; it does not conduct interviews or design surveys.

## Inputs
- **Required:** a set of customer feedback — anywhere from 20 to 500+ pieces
  — in any format (CSV, plaintext list, PDF, email thread, spreadsheet, Slack
  export). Each piece should include the raw text; optionally include source
  (app store, support, NPS survey, social), date, customer segment, or rating.
- **Optional:** product category or context (e.g., "mobile app," "B2B SaaS");
  specific themes to look for or exclude (e.g., "focus on UX, ignore feature
  backlog"); sentiment anchors or past baselines to compare against.

## Output Contract
The deliverable is a **customer sentiment report** with these sections (see
`template.md`):

1. **Executive Summary** — overall sentiment score (-1 to +1 scale or % positive
   / negative / neutral), total feedback count analyzed, sources, date range,
   and a one-paragraph summary of the top satisfaction drivers and detractors.
2. **Sentiment Overview** — breakdown by polarity (positive, neutral, negative)
   and optional score distribution; trending (if multiple time periods are
   available).
3. **Thematic Breakdown** — 4–8 themes or topics, each with frequency,
   representative quotes (≥ 2 per theme), sentiment polarity (per theme),
   customer segments affected, and business impact (customer churn risk, feature
   opportunity, operational issue, positioning risk, etc.).
4. **Top Positive Themes** — what customers love, ranked by frequency and
   strength; strategic positioning angles.
5. **Top Detractors & Pain Points** — critical issues, ranked by frequency and
   severity; quick wins vs. strategic fixes; churn risk.
6. **Recommended Actions** — 3–5 prioritized recommendations tied to themes,
   including quick wins (support/comms), tactical improvements, and strategic
   bets.

Format: prose + tables. Length: ~2–3 pages. Every theme is represented by at
least two exemplar quotes; no high-frequency issue is left unaddressed.

**GOOD (excerpt):**
> **Theme: Onboarding friction (18% of feedback, negative polarity)**
> - "Spent 45 minutes setting up; gave up before I used it." (SaaS trial, day 3)
> - "Your templates saved me, but finding them was impossible." (Active user, positive but still cited friction)
> - Segments affected: First-time SMB users, non-technical founders
> - Business impact: ~12% trial-to-paid drop-off; easy win.
> - Action: Audit the first-run experience; add contextual help; A/B test a guided tour.

**BAD (excerpt):**
> "Customers said good things and bad things. 60% liked the UI, 40% didn't like
> support. We should improve support."
> — fails: no themes, no quotes, no sentiment scores, no segment breakdown, no
> trade-off rationale, no distinction between perception and churn risk.

## Process
1. **Intake & standardize** — parse the feedback set, tag with source, date,
   and segment if available; note any obvious duplicates or spam.
2. **Scan for polarity** — quickly classify each piece as positive (satisfied /
   praising), negative (frustrated / complaining), or neutral (factual /
   unclear). Track overall sentiment distribution.
3. **Extract themes** — group feedback by topic or problem space (e.g.,
   "performance," "documentation," "support response time," "pricing"); aim for
   4–8 themes.
4. **Score each theme** — frequency (% of total feedback), polarity (positive /
   negative / mixed), and business impact (churn risk, feature opportunity,
   operational issue, brand signal).
5. **Select exemplar quotes** — pick ≥ 2 representative quotes per theme (mix
   positive and negative; vary customer type).
6. **Synthesize actions** — for top detractors and opportunities, draft 3–5
   recommendations (quick wins, tactical fixes, strategic shifts).
7. **Run the Quality Bar below; revise if any item fails; then return.**

## Quality Bar
Before returning, confirm:
- [ ] Overall sentiment is scored (-1 to +1, or % positive/negative/neutral)
  with a clear methodology (e.g., "polarity of each feedback unit averaged").
- [ ] Every theme is represented by ≥ 2 exemplar quotes (not paraphrases;
  direct text).
- [ ] Thematic frequency is stated (% of total feedback or count / total).
- [ ] Segments affected are named (if available in source data; e.g., "free vs.
  paid," "B2B vs. B2C," "mobile vs. desktop").
- [ ] Business impact is stated for each major theme (churn risk, feature
  opportunity, support burden, brand/positioning issue, retention lever, etc.).
- [ ] Recommended actions are ≥ 3, tied to specific themes, and ranked by
  effort or impact.
- [ ] No high-frequency issue (> 5%) is left unaddressed in themes or actions.
- [ ] If the output is written to a file, it follows `template.md` — all 6
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `sentiment-analysis-happy` (happy path) — large dataset with clear themes,
  mixed polarity, and actionable patterns.
- `sentiment-analysis-edge` (edge) — small or biased dataset, mixed languages,
  unclear polarity; skill must flag confidence limits.
- `sentiment-analysis-adversarial` (adversarial) — contradictory feedback,
  extreme outliers, or attempt to steer toward a predetermined conclusion;
  skill must synthesize objectively.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `voice-of-customer-miner` — mines qualitative insights from raw customer
  conversations, interview transcripts, or support tickets; surfaces JTBD and
  unmet needs. Use this for *discovery*; use sentiment-analysis for *scale
  synthesis*.
- `analyze-feature-requests` — categorizes and prioritizes feature requests by
  theme and impact. Use this when feedback has been formalized into specific
  asks.

### External Frameworks
- Sentiment analysis fundamentals — polarity (positive / negative / neutral),
  intensity (strong vs. weak), and subjectivity.
- JTBD (Jobs-to-be-Done) framework — sentiment often tracks whether a customer
  can complete their job; themes may map to job steps or desired outcomes.
- Tone & positioning — customer language is a signal for brand perception and
  positioning gaps (e.g., perceived as "expensive but reliable" vs. "cheap but
  broken").
