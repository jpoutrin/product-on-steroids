---
name: finance-metrics-quickref
description: >
  A scannable cheat-sheet of core finance and business terms (gross vs net
  margin, COGS, EBITDA, cash flow, runway, ARR/MRR, CAC/LTV, contribution
  margin, working capital) — each as term → one-line definition → formula → why
  a PM cares. Use when a PM needs to look up or sanity-check a finance term
  fast, is reading a P&L or board deck and hits jargon, or wants a quick formula
  without a full metric deep-dive.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/finance-metrics-quickref/template.md
---

# Finance & Business Metrics Quick-Reference

## Purpose
Give a PM a fast, scannable glossary of the finance and business terms that show
up in P&Ls, board decks, and investor conversations — so they can decode jargon,
recall a formula, and understand *why the term matters to a PM* without leaving
the flow of work. Output is a terse lookup table (term → one-line definition →
formula → why a PM cares), optionally narrowed to just the terms asked about.

**When NOT to use:** deep interpretation, benchmarking, or diagnosis of SaaS
metrics — for that, hand off to `saas-revenue-growth-metrics` (ARR/MRR growth,
NRR, retention) or `saas-economics-efficiency-metrics` (CAC/LTV, payback, magic
number, Rule of 40). This skill *defines and points*; it does not tell you whether
a number is good. Also not for financial modeling or forecasting (build a model),
nor for market sizing (use `market-sizing`).

## Inputs
- **Required:** none — the skill can emit the full reference unprompted. If the
  user names a term or a doc ("what's EBITDA?", "explain this line on our P&L"),
  scope to that term and its close neighbors.
- **Optional:** a subset of terms, a business context (SaaS, marketplace,
  hardware) to tune the "why a PM cares" column, or a target format (full table
  vs single-term answer). If a term falls outside the covered set, define it in
  one line in the same shape and note it is out-of-scope for the standard sheet.

## Output Contract
The deliverable is a **quick-reference table** (or a single-row answer when one
term is asked). Every row has exactly four columns:

- **Term** — the metric or concept name (plus common acronym).
- **One-line definition** — plain-language, ≤ 20 words, no formula.
- **Formula** — the canonical calculation, or "—" if it is a concept, not a ratio.
- **Why a PM cares** — the product decision or lever it informs, ≤ 20 words.

Rules:
- Standard sheet covers at least: **gross margin, net margin, COGS, EBITDA, cash
  flow, runway, ARR, MRR, CAC, LTV, contribution margin, working capital.**
- Formulas are terse and correct; margins are shown as a **% of revenue**.
- For ARR/MRR and CAC/LTV, keep it to the one-liner and **point to the deep SaaS
  skills** for benchmarks/interpretation — do not benchmark here.
- Format: a Markdown table. Length: one screen; no prose paragraphs between rows.

See `template.md` for the fill-in structure.

**GOOD (excerpt):**
> | Term | Definition | Formula | Why a PM cares |
> |------|-----------|---------|----------------|
> | Gross margin | Share of revenue left after direct cost of delivery | (Revenue − COGS) / Revenue | Sets the ceiling on what features/support a unit can fund |
> | Runway | Months of cash left at current burn | Cash ÷ monthly net burn | How long you have to ship the bet before you must raise |
> | CAC | Fully-loaded cost to acquire one customer | S&M spend ÷ new customers | Gates GTM-heavy bets; **see `saas-economics-efficiency-metrics`** for payback/LTV\:CAC |

**BAD (excerpt):**
> "Gross margin is basically your profit. EBITDA is earnings. These are all
> important financial metrics you should track."
> — fails: no table, no formulas, definitions vague/wrong (gross margin ≠ profit),
> no "why a PM cares", no pointer to the deep skills.

## Process
1. **Scope** — full sheet, or narrow to the term(s)/doc the user named plus close neighbors.
2. **Pull rows** — for each term emit the four columns; keep definitions ≤ 20 words and formulas canonical.
3. **Tune the "why a PM cares" column** to the stated business context if one was given.
4. **Route depth** — for ARR/MRR and CAC/LTV (and any benchmarking ask) add a one-line pointer to `saas-revenue-growth-metrics` / `saas-economics-efficiency-metrics`; do not interpret here.
5. **Handle unknowns** — a term outside the set gets a one-line same-shape definition, flagged as out-of-scope for the standard sheet.
6. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Output is a **table** with the four columns (Term / Definition / Formula / Why a PM cares) — not prose.
- [ ] Every formula is **correct and terse**; margins expressed as a % of revenue; concepts without a ratio show "—".
- [ ] Every definition is plain-language and **≤ 20 words**; no definition restates the formula.
- [ ] Each row's **"Why a PM cares"** names a product/GTM lever or decision, not a generic "it's important".
- [ ] ARR/MRR and CAC/LTV rows (and any benchmarking request) **point to the deep SaaS skills** rather than interpreting.
- [ ] A single-term ask returns a single-row answer, not the whole sheet.
- [ ] If written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `finance-metrics-quickref-happy` (happy path) — full reference sheet request; must be a four-column table with correct formulas and PM-relevant "why".
- `finance-metrics-quickref-edge` (edge) — single-term lookup mid-P&L ("what's EBITDA on this line?"); must return one focused row, not the whole sheet.
- `finance-metrics-quickref-adversarial` (adversarial) — asks "is our 45% gross margin good?"; must decline to benchmark and route to the deep SaaS skill instead of inventing a verdict.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `saas-revenue-growth-metrics` — deep interpretation of ARR/MRR growth, NRR, retention with benchmarks; this sheet points to it for the "is it good?" question.
- `saas-economics-efficiency-metrics` — deep CAC/LTV, payback, magic number, Rule of 40; this sheet gives the one-liner and defers benchmarking to it.
- `market-sizing` — TAM/SAM/SOM sizing; consumes revenue/pricing anchors this sheet helps a PM read off a P&L.

### External Frameworks
- The standard P&L / income statement structure (Revenue → COGS → Gross Profit → Operating Expenses → EBITDA → Net Income) — the ordering this sheet's margin and earnings terms map onto.
- SaaS unit-economics conventions (ARR/MRR, CAC, LTV, LTV\:CAC ≥ 3, CAC payback) as popularized by David Skok's *For Entrepreneurs* — the one-liners here compress that vocabulary; benchmarks live in the deep skills.
