---
name: market-landscape-scan
description: >
  Map an unfamiliar market or category in one broad first pass — player
  categories (incumbents, challengers, adjacent, emerging), key trends, white
  spaces, and a category/2x2 map — to get oriented. Use when entering a new
  space, orienting before a strategy or entry decision, briefing leadership on
  an unfamiliar category, or deciding whether a market is worth a deeper look.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/market-landscape-scan/template.md
---

# Scan a Market Landscape

## Purpose
Produce a wide, one-time **orientation scan** of an unfamiliar market or
category: who is in it (grouped into player categories, not enumerated
rival-by-rival), what forces are shaping it, where the visible white spaces are,
and a single map that positions the categories at a glance. The goal is to get
oriented fast so a team can decide where to look deeper — it bounds the space and
names its structure; it does not pick a competitor to beat or a wedge to build.

**When NOT to use:** a rival-by-rival teardown of named competitors (use
`competitor-analysis`), ongoing tracking of moves after you already know the
space (use `competitive-intel-watch`), or numerically sizing the opportunity (use
`market-sizing`). This is the wide *first* pass; those are the deep and recurring
passes that follow it.

## Inputs
- **Required:** the market/category to scan and the boundary that defines it —
  the customer problem or job, buyer type (B2B/B2C, segment), and rough
  geography/scope. If missing, ask for these three before scanning; do not guess
  the boundary, or the scan will be unfocused.
- **Optional:** the orientation question behind the scan (entry? adjacency?
  investment?), known players or reports to seed from (read and cite), the axes
  the reader cares about for the map (default: pick the two axes that most
  separate the categories, e.g. breadth-of-offering × target-segment), and a
  recency window for trends (default: last 2–3 years).

## Output Contract
The deliverable is a **landscape-scan brief** with these sections (see
`template.md`):

1. **Scope** — the market boundary: customer problem/job, buyer type, geography,
   and what is deliberately excluded. One short paragraph.
2. **Player categories** — 3–6 groups (e.g. incumbents, challengers, adjacent
   entrants, emerging/startups), each with a one-line definition, 2–4 example
   players, and the role that group plays in the market. A table.
3. **Key trends** — 3–6 forces shaping the space (demand shifts, tech,
   regulation, business-model moves), each with a direction (rising/declining)
   and a one-line "so what" for a new entrant. Cited or labeled an observation.
4. **White spaces** — 2–4 under-served or unclaimed areas the scan surfaced, each
   tied to the category/trend that reveals it and flagged as a hypothesis to
   validate (not a proven gap).
5. **Category map** — a 2×2 (or simple axis) positioning the player *categories*
   (not individual companies) on two named axes, described in text/ASCII so it
   renders without images, plus one line on what the empty quadrant implies.
6. **Orientation & next step** — 2–3 sentences answering the orientation question
   and naming the single deeper follow-up (which skill / which corner to probe).
7. **Sources** — a table of every external source consulted (reports, analyst
   publications, news, company sites), with type, year, URL or citation, and
   which player claim, trend, or white space it supports.

Format: prose + one category table + one text-rendered map. Length: ~1–2 pages.
Breadth over depth — categories and hypotheses, not verdicts. Every player claim
is cited or labeled an observation; white spaces are explicitly hypotheses.

**GOOD (excerpt):**
> **Player categories:**
> | Category | Definition | Examples | Role |
> |---|---|---|---|
> | Incumbents | Full-suite HR platforms | Workday, SAP | Own enterprise, slow on SMB |
> | Emerging | API-first payroll startups | Deel, Remote | Winning cross-border SMB |
>
> **White space (hypothesis):** No category serves <10-person firms with
> localized compliance — incumbents skip them, emerging players start at ~20 seats.
> *Validate with 15 micro-employer interviews before treating as a real gap.*

**BAD (excerpt):**
> "Competitors: Workday (strong analytics, weak UX, priced 20% above us), SAP
> (…), Deel (…)" — fails: this is a rival-by-rival teardown with feature verdicts
> (that's `competitor-analysis`), not a categorized landscape with a map and
> white-space hypotheses.

## Process
1. **Fix the boundary** — nail problem/job, buyer type, geography, and
   exclusions; if any is missing, ask before scanning.
2. **Sweep wide** — gather players and signals across the whole space; aim for
   coverage, not depth on any one player.
3. **Cluster into categories** — group players into 3–6 meaningful categories;
   define each and note its role. Do not profile individuals.
4. **Read the trends** — name 3–6 shaping forces with direction and a "so what."
5. **Surface white spaces** — cross categories against trends to spot unclaimed
   areas; flag each as a hypothesis to validate.
6. **Draw the category map** — pick two separating axes, place the *categories*,
   and read the empty quadrant.
7. **Orient** — answer the orientation question and name the one deeper follow-up.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **boundary** (problem/job, buyer type, geography, exclusions) is stated up front.
- [ ] Players are grouped into **3–6 categories** with roles — not a flat list and not a per-rival teardown.
- [ ] Trends carry a **direction** and a one-line "so what" for a new entrant.
- [ ] White spaces are framed as **hypotheses to validate**, each tied to a category/trend — never asserted as proven gaps.
- [ ] The map positions **categories** (not individual companies) on two named axes, renders as text, and the empty quadrant is interpreted.
- [ ] The brief ends with an **orientation answer + one named deeper follow-up** (e.g. `competitor-analysis`, `market-sizing`).
- [ ] Every player claim is **cited or labeled an observation**; the scan stays broad, not deep.
- [ ] A **Sources table** is present listing every external source consulted (type, year, URL/citation, and what claim/trend/white space it supports).
- [ ] If written to a file, it follows `template.md` — all 7 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `market-landscape-scan-happy` (happy path) — scan an unfamiliar B2B category with a clear boundary and seed players.
- `market-landscape-scan-edge` (edge) — an emerging/nascent space with few named players, forcing category + trend inference over enumeration.
- `market-landscape-scan-adversarial` (adversarial) — user asks for a competitor teardown; the skill must stay a broad categorized scan and hand off to `competitor-analysis`.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `competitor-analysis` — the deep rival-by-rival brief this scan hands off to once a category is worth probing.
- `competitive-intel-watch` — ongoing monitoring that takes over after the one-time scan establishes the map.
- `market-sizing` — numerically sizes the opportunity this scan bounds qualitatively.

### External Frameworks
- Michael Porter, *Competitive Strategy* (1980) — the Five Forces lens behind the "shaping forces / trends" read of a category's structure.
- W. Chan Kim & Renée Mauborgne, *Blue Ocean Strategy* (2005) — the strategy-canvas / uncontested-space thinking behind the white-space and empty-quadrant reads.
- [a16z — Market analysis and category creation](https://a16z.com/) — investor-lens framing for orienting in and naming a new market category.
