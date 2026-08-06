---
name: pestel-delta-monitor
description: >
  Compare a prior PESTEL/PESTLE baseline scan against fresh macro-environment
  signals and report what changed — per factor: direction, magnitude,
  new/retired factors, revised impact/likelihood, and which product decisions to
  revisit. Use when refreshing a macro scan, monitoring PESTEL drift since a
  baseline, reacting to a regulatory or economic shift, or deciding whether a
  strategy assumption still holds.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/pestel-delta-monitor/template.md
---

# PESTEL Delta Monitor (What Changed Since the Baseline)

## Purpose
Produce a **change report** on the macro-environment: given a prior PESTEL/PESTLE
baseline and a set of newer signals, identify what actually moved in each of the
six factors (Political, Economic, Social, Technological, Environmental, Legal),
the **direction and magnitude** of each shift, any **new** factors that appeared
or **retired** factors that no longer bind, the resulting change in
**impact/likelihood**, and — the payload — **which product/strategy decisions to
revisit** as a result. It turns a static scan into a monitored signal so teams
notice drift before it invalidates the plan.

**When NOT to use:** building the first-ever scan from scratch when there is no
prior baseline — use the point-in-time `pestle-analysis` skill to create the
baseline, then feed its output here. Also not for competitor-specific moves (use
`competitor-analysis`) or for re-sizing the market (use `market-sizing`). This
skill only reports *change relative to a baseline*; without a baseline it has
nothing to diff against.

## Inputs
- **Required:** the **prior PESTEL/PESTLE baseline** (the earlier scan, with its
  date) *and* the **new signals** to diff against it (news, regulation,
  economic data, analyst notes, internal telemetry). If the baseline is missing,
  do not invent one — ask for it or route to `pestle-analysis` to create it
  first. If new signals are missing, ask what changed or which sources to read.
- **Optional:** the **product/strategy decisions** currently riding on the
  baseline (roadmap bets, pricing, GTM, market choice) — enables the
  "decisions to revisit" mapping; if absent, flag the shifts and ask which bets
  they touch. Also optional: the review window (default: baseline date → today),
  and a materiality threshold (which shifts are big enough to report).

## Output Contract
The deliverable is a **PESTEL delta report** with these sections (see
`template.md`):

1. **Baseline & Window** — the baseline scan referenced (with its date) and the
   review window covered; one line on the signals/sources diffed in.
2. **Per-Factor Deltas** — one row per PESTEL factor in a table: prior state →
   current state, **direction** (↑ rising / ↓ easing / → stable / ⤨ reversed),
   **magnitude** (minor / moderate / major), and the signal that evidences it.
   A factor with no material change is marked *stable* — not omitted.
3. **New & Retired Factors** — factors that appeared since the baseline (with why
   they now matter) and baseline factors that no longer bind (with why).
4. **Impact / Likelihood Shifts** — for each *material* delta, how impact and/or
   likelihood moved versus the baseline rating, stated as before → after.
5. **Decisions to Revisit** — the payload: each material shift mapped to the
   specific product/strategy decision it puts in question, plus the recommended
   action (hold / monitor / re-examine / act now) and an owner or trigger.
6. **Watch List** — signals that are moving but not yet material, with the
   threshold that would make them material.

Format: prose + one per-factor delta table. Length: ~1–2 pages. Every reported
change is tied to a **signal/source** and a **prior-state reference** — never an
unanchored "things are changing." Stable factors are stated as stable, not
dropped, so the report is a true diff.

**GOOD (excerpt):**
> **Legal — ↑ major.** Baseline (2025-11): "EU AI Act obligations distant, 2027+."
> Current: high-risk-system obligations confirmed to apply from Aug 2026 (Signal 4, EU OJ). Likelihood high→certain; impact med→high.
> *Decision to revisit:* the Q3 roadmap deprioritized model-documentation tooling — **re-examine now**; owner: Compliance PM. Trigger already tripped.

**BAD (excerpt):**
> "The regulatory environment has gotten more challenging and the economy is uncertain, so we should keep an eye on things."
> — fails: no baseline reference, no direction/magnitude, no signal cited, no decision mapped, and omits the four factors that didn't change (not a diff).

## Process
1. **Anchor the baseline** — load the prior scan; note its date and each factor's
   prior state and impact/likelihood rating. If no baseline exists, stop and route
   to `pestle-analysis`.
2. **Ingest signals** — gather the new signals across the window; attribute each
   to a source.
3. **Diff each factor** — for all six PESTEL factors, compare prior vs current;
   assign direction and magnitude; mark unchanged factors *stable* (do not omit).
4. **Detect new/retired** — flag factors that emerged since the baseline and
   baseline factors that no longer bind.
5. **Re-rate impact/likelihood** — for each material delta, restate impact and
   likelihood as before → after.
6. **Map to decisions** — tie each material shift to the product/strategy decision
   it affects; assign an action (hold / monitor / re-examine / act now) and an
   owner or trigger. If decisions weren't provided, name the shift and ask which
   bets it touches.
7. **Build the watch list** — record sub-threshold movers and the threshold that
   would escalate them.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The report references a **named, dated baseline** and diffs against it — it is a change report, not a fresh scan.
- [ ] **All six PESTEL factors** appear; unchanged ones are explicitly marked *stable*, never dropped.
- [ ] Every reported change carries a **direction** and a **magnitude** and cites the **signal/source** evidencing it.
- [ ] **New** and **retired** factors are called out separately from same-factor shifts.
- [ ] Material deltas restate **impact/likelihood** as before → after against the baseline rating.
- [ ] Each material shift maps to a **specific decision to revisit** with an action and an owner/trigger — not a generic "monitor."
- [ ] A **watch list** distinguishes sub-threshold movers from material changes.
- [ ] If the report is written to a file, it follows `template.md` — all 6 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `pestel-delta-monitor-happy` (happy path) — a baseline plus clear new signals; produces a full per-factor diff and decision mapping.
- `pestel-delta-monitor-edge` (edge) — most factors stable, one sharp legal shift; must report the stable factors as stable rather than only the mover.
- `pestel-delta-monitor-adversarial` (adversarial) — asked to "just update the PESTEL" with no baseline provided; must refuse to fabricate a diff and route to baseline creation.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `pestle-analysis` — creates the point-in-time PESTLE baseline this skill consumes and diffs against; run it first when no baseline exists.
- `market-sizing` — when a macro shift changes the addressable opportunity, hand the affected factors here to re-size rather than re-rating in place.
- `competitor-analysis` — company-specific moves belong there; this skill stays at the macro-environment altitude.

### External Frameworks
- Francis Aguilar, *Scanning the Business Environment* (1967) — origin of ETPS/PEST environmental scanning; this skill operationalizes the *continuous scanning* intent (monitoring drift), not just a one-time scan.
- Gerry Johnson, Kevan Scholes & Richard Whittington, *Exploring Corporate Strategy* — PESTEL as a periodic-review tool where impact and likelihood are re-rated over time; the basis for the before→after re-rating here.
