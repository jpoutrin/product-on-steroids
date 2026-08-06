---
name: competitive-intel-watch
description: >
  Run an ongoing competitive-intelligence watch: maintain a watchlist of
  competitors and signal sources (releases, pricing, hiring, funding,
  messaging), then produce a periodic digest of moves since the last check with
  a "so what / recommended response" and threat level per material move. Use
  when standing up or running recurring competitor monitoring, producing a
  weekly/monthly competitive digest, tracking rival moves over time, or setting
  up a competitive-signal watchlist.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/competitive-intel-watch/template.md
---

# Competitive Intelligence Watch (Recurring Digest)

## Purpose
Stand up and run an **ongoing** competitive-intelligence cadence: a durable
watchlist of competitors and signal sources, plus a **periodic digest** that
reports only what has *changed since the last check*, triages each material move
by threat level, and attaches a "so what / recommended response" so the team can
act. Supports staying ahead of rivals between planning cycles — catching pricing
changes, launches, funding, hiring surges, and messaging pivots while they are
still fresh.

**When NOT to use:** a one-time, deep single-competitor teardown (use
`competitor-analysis`); a broad first-pass survey to discover who the players
even are (use `market-landscape-scan`); or sizing the market itself (use
`market-sizing`). This skill assumes the players are already known and the goal
is **continuous monitoring**, not a first inventory or a deep dive.

## Inputs
- **Required:** the set of competitors to watch (2–8 is workable) and the *last
  check date* (the digest reports moves **since** it). If the watch does not yet
  exist, elicit the competitor list and, for the first run, treat "since" as the
  agreed lookback window (default 30 days). If no competitors are named, ask for
  them before running — do not invent rivals.
- **Optional:** signal sources to prioritize (default: product/changelog,
  pricing page, careers/hiring, funding/press, public messaging/positioning),
  cadence (default: monthly), our own product's position/priorities (sharpens the
  "so what"), and any prior digest to diff against.

## Output Contract
The deliverable is a **competitive watch digest** with these sections (see
`template.md`):

1. **Watch Header** — competitors covered, signal sources checked, the period
   (`since <date>` → `<today>`), and cadence.
2. **Moves Since Last Check** — a table, one row per detected move:
   competitor · signal type · what changed · source/date · **threat level**
   (High / Medium / Low / Noise) · **so what & recommended response**. Only
   *material* moves — no filler; explicitly mark "No material moves" per
   competitor when true.
3. **Threat Triage** — the High/Medium moves called out with why they rate that
   level (impact × proximity to our roadmap/customers) and an owner-ready action.
4. **Watchlist State** — the current watchlist and sources carried forward, plus
   any additions/removals, so the next run can diff against it.
5. **Watch This Next** — leading indicators or unconfirmed rumors to confirm on
   the next cycle.
6. **Sources** — a table of every signal source checked this cycle: competitor,
   source name, type (product page / pricing / job board / press / analyst),
   date checked, and URL or reference. Gives an audit trail of coverage.

Format: prose header + one Moves table + short triage/action lines. Length:
~1 page. Every move cites a **source and date**; unverified items are labeled
*unconfirmed*. Threat level is justified, never bare.

**GOOD (excerpt):**
> | Acme | Pricing | Dropped Starter tier €29→€19/mo + added usage cap | acme.com/pricing, 2026-07-28 | **High** | Undercuts our €25 entry and reframes value as usage. **Response:** model margin impact this week; brief sales on the cap ceiling as our counter. |
>
> *Threat = High: directly hits our entry price point and our two largest at-risk accounts renew in Q3.*

**BAD (excerpt):**
> "Acme has been busy lately and seems to be doing a lot with pricing and AI. We should keep an eye on them."
> — fails: no dated source, no specific change, no threat level, no recommended response, not scoped to moves *since last check*.

## Process
1. **Load or build the watchlist** — confirm competitors + signal sources; if
   none exists, elicit them and set the lookback window.
2. **Fix the window** — set `since <last-check date>` → today; everything before
   `since` is out of scope for this digest.
3. **Sweep each source per competitor** — product/changelog, pricing, hiring,
   funding/press, messaging — capturing only what changed in the window, with a
   source URL and date.
4. **Filter to material moves** — drop noise; a move is material if it plausibly
   affects our customers, positioning, pricing, or roadmap. Mark "No material
   moves" where true rather than padding.
5. **Triage threat level** — rate each move High/Medium/Low/Noise by impact ×
   proximity to our roadmap and customers; state the reason.
6. **Write "so what & recommended response"** — a concrete, owner-ready action
   per material move (not "monitor").
7. **Carry the watchlist forward** — record additions/removals and set up the
   next window so runs diff cleanly.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The digest reports **only moves since the last check** — the window
      (`since <date>` → today) is stated and honored.
- [ ] Every move has a **dated source**; unverified items are labeled *unconfirmed*.
- [ ] Every material move carries a **threat level** (High/Medium/Low/Noise)
      with a one-line justification — never a bare label.
- [ ] Every High/Medium move has a **concrete recommended response** with an
      implied owner — not "keep an eye on it".
- [ ] Competitors with nothing material are explicitly marked **"No material
      moves"**, not omitted or padded.
- [ ] The **watchlist state** (competitors + sources, and any changes) is carried
      forward so the next run can diff against it.
- [ ] The digest stays scoped to **monitoring** — it does not turn into a
      one-time deep teardown or a market-discovery survey.
- [ ] A **Sources table** is present listing every signal source checked this
      cycle (competitor, source name, type, date checked, URL/reference) — so
      coverage is auditable.
- [ ] If the digest is written to a file, it follows `template.md` — all 6
      sections present, in order, headings matching (a skill-scoped hook
      re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `competitive-intel-watch-happy` (happy path) — a monthly run over a known
  watchlist that surfaces dated moves, triages threat, and recommends responses.
- `competitive-intel-watch-edge` (edge) — a quiet period where most competitors
  had no material moves; the skill must say so cleanly and not pad.
- `competitive-intel-watch-adversarial` (adversarial) — pressure to include
  everything / unsourced rumor as fact; the skill must filter noise, label
  unconfirmed items, and refuse to drift into a full teardown.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `competitor-analysis` — the one-time deep single-competitor teardown; this watch
  hands off to it when a High move warrants a full dive.
- `market-landscape-scan` — the broad first-pass survey that discovers the players;
  its output seeds this watch's initial watchlist.
- `market-sizing` — sizing context that helps weight a move's threat by the
  segment it touches.

### External Frameworks
- Michael Porter, *Competitive Strategy* (1980) — competitor-response profiles
  (goals, assumptions, capabilities) that inform threat triage and "so what".
- OODA loop (John Boyd) — Observe→Orient→Decide→Act; the recurring
  observe-and-respond cadence this watch operationalizes.
- SCIP (Strategic & Competitive Intelligence Professionals) code of ethics —
  gathering intelligence from public/legitimate sources only.
