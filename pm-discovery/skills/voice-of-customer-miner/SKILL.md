---
name: voice-of-customer-miner
description: >
  Use when you have a body of raw qualitative customer text — support tickets,
  app store reviews, community posts, interview transcripts, or survey
  open-ends — and need a structured synthesis that preserves actual customer
  language, groups themes across sources, and surfaces actionable signals.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/voice-of-customer-miner/template.md
---

# Voice-of-Customer Miner

## Purpose
Extract, group, and synthesize the voice of the customer from raw qualitative
text sources. The deliverable is a structured VoC synthesis that identifies
the top recurring themes, anchors each theme with verbatim customer quotes,
tags sentiment and volume, surfaces jobs-to-be-done signals, and flags notable
absences — so a PM can move from unstructured feedback noise to grounded
product decisions.

**When NOT to use:** scoring a single text for positive/negative sentiment only
(use `sentiment-analysis`); processing a structured feature-request backlog or
JIRA issue list (use `analyze-feature-requests`); distilling a single interview
session into key takeaways (use `summarize-interview`). VoC Miner requires
multiple real customer texts and must not be invoked when the goal is a
sentiment score rather than a thematic synthesis.

## Inputs
- **Required:** one or more raw customer text corpora — paste the texts or
  provide the source label (e.g., "App Store reviews Q1 2025", "Zendesk tickets
  March"). If no text is provided, ask for it; do not fabricate or infer content.
- **Optional:** focus area or product surface (default: infer from the texts);
  customer segment filter (e.g., "free-tier only", "enterprise accounts"); desired
  number of top themes (default: top 5, capped at 10); source labels for each
  corpus (default: derive from context or label as "Source A/B/…").

## Output Contract
The deliverable is a **VoC Synthesis Report** structured as (see `template.md`):

1. **Summary** — one paragraph: overall signal strength, corpus size (how many
   sources, approximate mention count), dominant sentiment direction, and the
   single most urgent theme.
2. **Theme Breakdown** — a table with one row per theme: theme name, sentiment
   tag (Positive / Negative / Mixed), volume (n mentions or "~n"), and one to
   three verbatim exemplar quotes per theme, attributed to source.
3. **Notable Gaps** — what customers are conspicuously *not* saying: features
   they never mention, areas of silence that may indicate low salience or
   suppressed dissatisfaction.
4. **JTBD Signals** — the underlying jobs customers are trying to do, inferred
   from the language patterns (e.g., "I just need to…", "all I want is…").
   One bullet per job, with a supporting quote.
5. **Recommended Actions** — three to five prioritized actions for the product
   team, each tied back to a theme or gap. Label each action with the theme(s)
   it addresses.

Format: narrative summary + one theme table + bullet lists. Length: ~1–2 pages.
Every quote is verbatim from the input text — paraphrased summaries are labeled
clearly and never substituted for quotes.

**GOOD (excerpt):**
> **Theme: Slow onboarding (Negative | ~18 mentions)**
> - *"It took me three days to get my first report out. I literally had to watch
>   four YouTube videos."* — App Store review
> - *"Why is there no guided setup? Every other tool I've used walks you through
>   it."* — Support ticket
> **JTBD:** Users want to reach first value in under 30 minutes without external
> help.

**BAD (excerpt):**
> "Customers feel the onboarding is too slow and complicated." — fails: this is
> a paraphrase, not a quote; no source attribution; no volume count; collapses
> distinct voices into a single editorial claim.

## Process
1. **Ingest and label** — read all provided texts; assign a source label to each
   corpus; count approximate total mentions available.
2. **First pass — open coding** — scan every text and annotate emerging themes;
   do not force a theme list yet; use the customer's own words as theme names
   where possible.
3. **Theme consolidation** — merge overlapping codes into coherent themes;
   cap at the requested number (default 5, max 10); name each theme in
   plain language that mirrors customer phrasing.
4. **Quote selection** — for each theme, pick the one to three most vivid,
   representative verbatim quotes from across different sources; never paraphrase.
5. **Sentiment and volume tagging** — tag each theme Positive, Negative, or Mixed;
   count or estimate mention frequency across all sources.
6. **Cross-source pattern check** — verify each theme appears in more than one
   source before elevating it; single-source themes are noted as "limited signal."
7. **Notable Gaps** — identify topics absent from the corpus that the PM might
   expect to see; hypothesize why they might be missing.
8. **JTBD extraction** — translate recurring language patterns into job statements
   ("When I…, I want to…, so I can…" or simplified form); anchor each with a quote.
9. **Recommended Actions** — draft three to five concrete actions; tie each to a
   theme or gap; order by frequency × sentiment severity.
10. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every exemplar quote in Theme Breakdown is **verbatim** from the input — no
  paraphrases substituted for quotes.
- [ ] Each theme carries a **sentiment tag** (Positive / Negative / Mixed) and an
  explicit **volume count or estimate**.
- [ ] No theme is elevated from a **single source** without being flagged as
  "limited signal."
- [ ] The Notable Gaps section addresses what is **absent**, not just what is
  present — at least two gaps are named.
- [ ] JTBD Signals section contains at least one job statement per major theme,
  each supported by a quote.
- [ ] Recommended Actions are **tied back** to specific themes or gaps by name —
  no free-floating recommendations.
- [ ] The skill **refused to fabricate** any quote, customer name, or data point
  not present in the provided input.
- [ ] If the output is written to a file, it follows `template.md` — all five
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `summarize-interview` — distills a single interview session; feeds raw
  transcripts that may be ingested here as one corpus among many.
- `sentiment-analysis` — scores texts for positive/negative polarity; use when
  you need a score, not a thematic synthesis.
- `analyze-feature-requests` — processes structured backlog or JIRA items;
  complementary to VoC Miner for closing the loop between discovery and delivery.

### External Frameworks
- Griffin & Hauser (1993), "The Voice of the Customer" (*Marketing Science*) —
  foundational definition of VoC as the hierarchy of customer needs expressed in
  the customer's own words; the verbatim-quote discipline this skill enforces
  comes directly from their methodology.
- Clayton Christensen, *Competing Against Luck* (2016) — Jobs-to-be-Done theory
  underlying the JTBD Signals section; the "hire / fire" framing for surfacing
  unmet jobs from qualitative language.
- Kano Model (Noriaki Kano, 1984) — theme sentiment tagging maps loosely to
  Kano's Basic / Performance / Delight categories; useful when prioritizing
  Recommended Actions.
