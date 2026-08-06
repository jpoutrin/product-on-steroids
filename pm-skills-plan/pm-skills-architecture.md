# PM Skills — Architecture & Build Plan (v2, decisions locked)

*A coherent, testable PM skill system on the four quadrants of the Peak Product Manager framework — built as a standalone marketplace, safe to distribute to clients.*

Date: 2026-08-05 · Owner: Jeremie

---

## Locked decisions

1. **License posture → MIT-only for anything shipped.** You'll distribute to clients for professional use (no fee). That is still almost certainly "commercial/professional use" under CC **NonCommercial**, and **ShareAlike** would force derivatives to stay CC-NC — incompatible with a client deliverable. So: **ship only MIT (`phuryn`) + originally-written skills.** Use `deanpeters` for *framework ideas and structure only* (frameworks aren't copyrightable; their wording is) — never copy its text. *(Not legal advice — if you want specific deanpeters skills verbatim, ask Dean for permission/relicense.)*
2. **Five plugins** — add `pm-gtm` so `pm-strategy` isn't overloaded.
3. **Standalone marketplace** — a separate `pm-skills`-style repo you add to Cowork, not inside `product-forge`.
4. **Start point** — refine the plan before building the exemplar.

**Consequence of #1:** the build shifts toward *import-MIT + generate-original*. deanpeters stops being a source of shippable text and becomes a reference bookshelf. Net: a bit more generation, zero license risk.

---

## 0. Verified repo facts

| Repo | License | Real size | Structure | Output clarity | Validation |
|---|---|---|---|---|---|
| `phuryn/pm-skills` | **MIT** ✅ ship | 68 skills / 9 plugins | plugin-per-domain, `validate_plugins.py` + CI consistency tests | light (qualities, no template) | structural only |
| `deanpeters/PM-Skills` | **CC BY-NC-SA** ⚠️ ideas-only | 70 skills, flat | richer (`intent`, `type`, anti-patterns, `template.md`, workshop protocol) | better (templates) | structural only |

Neither validates *output quality* — the gap we design out (§2).

---

## 1. Target architecture: 5 plugins on the quadrant

| Plugin | Quadrant | MIT imports (phuryn) | Generate-original (deanpeters = idea reference only) |
|---|---|---|---|
| **`pm-discovery`** | Customer Insight | interview-script, summarize-interview, jtbd-adjacent, opportunity-solution-tree, assumptions×2, experiments×2, brainstorm-ideas×2, analyze-feature-requests, prioritize-assumptions, personas, journey-map, segmentation, sentiment, sql/cohort/ab-test | voice-of-customer-miner, problem-framing-canvas, lean-ux-canvas, discovery-process workflow |
| **`pm-strategy`** | Product Strategy | product-vision, product-strategy(canvas), value-proposition, business-model, lean-canvas, startup-canvas, monetization, pricing, swot, pestle, porters, ansoff, market-sizing, competitor-analysis, north-star, metrics-dashboard, brainstorm-okrs, outcome-roadmap, prioritize-features, prioritization-frameworks, feature-investment (via advisor) | roadmap-planning workflow, product-strategy-session workflow, saas metrics quickrefs, competitive-intel-watch, build-vs-buy (net-new) |
| **`pm-gtm`** | Product Strategy / GTM | gtm-strategy, gtm-motions, beachhead-segment, ideal-customer-profile, growth-loops, competitive-battlecard, positioning-ideas, value-prop-statements, product-name, marketing-ideas | positioning-workshop, press-release (Working-Backwards) — write original |
| **`pm-execution`** | Product Execution | create-prd, user-stories, job-stories, sprint-plan, release-notes, pre-mortem, retro, strategy-red-team, test-scenarios, summarize-meeting, intended-vs-implemented, shipping-artifacts | epic-hypothesis/breakdown, storyboard, user-story-splitting patterns. **Reconcile with existing product-forge PRD/QA suite — dedupe, don't double** |
| **`pm-influence`** | Influencing People | stakeholder-map (thin) | **mostly GENERATE**: exec-update, alignment-narrative, decision-memo, managing-up-brief, stakeholder-mapping, RACI, escalation, 30-60-90. Tailor to your org |

Dropped (out of PM scope): `pm-toolkit` (NDA, resume, grammar, privacy).

---

## 2. Quality standard (unchanged — this is the point)

Every skill conforms to this; the two starred sections fix your named weakness.

```markdown
---
name: <kebab>            # == directory
description: <what + when-to-use triggers>
version: 0.1.0
type: component | interactive | workflow
inputs: [...]
outputs: <artifact>
source: original | import:phuryn/pm-skills@<sha>
---
# <Skill>
## Purpose · when to use / when NOT to use
## Inputs (required/optional; how to elicit if missing)
## Output Contract              ★ FIX #1 output clarity
   - section-by-section template · format & length · GOOD example (filled) · BAD example + why
## Process (numbered)
## Quality Bar                  ★ FIX #2a — self-check rubric run BEFORE returning; revise if failing
## Validation & Eval            ★ FIX #2b — evals/*.md scenario cards {input, expected, rubric}, LLM-judge scored, regression gate
## References
```

Two validation layers: **structural lint** (fork phuryn's `validate_plugins.py`, extend to *require* Output Contract + Validation sections; runs in CI) + **output eval on Langfuse** — each skill's `evals/*.md` scenario cards map to a Langfuse **dataset**; a run invokes the skill over the dataset as a **dataset experiment**; the skill's Quality-Bar rubric becomes an **LLM-as-a-judge evaluator** that writes **scores**; comparing run scores across edits is the regression gate. (The `skill-creator` eval/variance tooling can drive local spot-checks; Langfuse is the system of record.)

---

## 3. Overlap resolution (simplified by the MIT-only call)

The ~11 head-to-head pairs are no longer "synthesize two texts." Now: **adopt the phuryn (MIT) version → elevate to the §2 standard with original writing** (add Output Contract, gold example, eval cards). deanpeters informs *what good looks like* structurally, nothing is copied. Fast and clean.

---

## 4. Agents (one anchor per quadrant + router)

| Agent | Plugin(s) | Job |
|---|---|---|
| `cpo` | pm-strategy | Set & pressure-test strategy, own outcomes (seeded from your existing passive `product-strategy` persona) |
| `product-discovery-specialist` | pm-discovery | Ambiguity → validated opportunities |
| `gtm-strategist` | pm-gtm | Positioning, segments, launch, growth |
| `delivery-lead` | pm-execution | Strategy → shippable, well-specified work |
| `product-influence-partner` / `chief-of-staff` | pm-influence | Drive alignment; communicate up & across |
| `pm-orchestrator` *(core)* | all | Single entry point; routes to the right specialist + skill, sequences multi-quadrant work |

Each agent = system prompt (persona + principles) + allowed-skills list + default output expectations.

---

## 5. Standalone marketplace scaffold

```
pm-skills/                         # your new repo, add to Cowork as a marketplace
  .claude-plugin/marketplace.json  # lists the 5 plugins
  pm-discovery/
    .claude-plugin/plugin.json
    skills/<skill>/SKILL.md (+ template.md, evals/*.md)
    agents/product-discovery-specialist.md
  pm-strategy/   … cpo agent
  pm-gtm/        … gtm-strategist agent
  pm-execution/  … delivery-lead agent
  pm-influence/  … product-influence-partner agent
  tests/         # structural lint (forked) + output-eval harness
  validate_plugins.py
  README.md  CHANGELOG.md  LICENSE(MIT)
```

---

## 6. Roadmap

- **Phase 0** — lock standard + build ONE exemplar (`market-sizing`: phuryn base → standard, gold example, 3 runnable eval cards). *Deferred per your call until plan is refined.*
- **Phase 1** — `pm-strategy` (your original focus) + `cpo`.
- **Phase 2** — `pm-discovery` + specialist (richest import material).
- **Phase 3** — `pm-gtm` + `gtm-strategist`.
- **Phase 4** — `pm-execution`, reconciled with product-forge; `delivery-lead`.
- **Phase 5** — `pm-influence` (mostly generate); `product-influence-partner`.
- Cross-cutting: `pm-orchestrator` is core, not optional — stand up a minimal router in Phase 1 and extend it as each plugin lands so there's always one entry point. Linter in CI from Phase 0; eval harness grows per skill.

---

## 7. Refinement tracks

**Delivered as companion docs:**
- ✅ **Full skill ledger** → `pm-skills-ledger.md` — all 138 skills tagged KEEP-IMPORT / GENERATE / DEDUPE / DROP per plugin.
- ✅ **`pm-influence` skill list** → `pm-influence-plugin.md` — 10 core skills, each with an Output Contract + sample eval.
- ✅ **Eval harness design** → `pm-skills-eval-pipeline.md` — Langfuse dataset/experiment/judge pipeline + scenario-card schema + CI flow.
- ✅ **product-forge reconciliation** → `pm-forge-reconciliation.md` — supersede / complement / leave-alone map.

**Still open:**
- **Agent specs** — draft the `cpo` (and peers) system prompts + allowed-skill lists.
- **Phase 0 exemplar** — build one skill (`market-sizing`) end-to-end to the standard, with runnable Langfuse eval cards.

<details><summary>original open questions (superseded by the docs above)</summary>

- **Full skill ledger** — a per-plugin table of all ~127 skills tagged KEEP-IMPORT / GENERATE / DROP / DEDUPE, so nothing's hand-wavy before we build?
- **`pm-influence` skill list** — nail down the ~8–10 net-new influence skills (this is the highest-value, most-original plugin)?
- **Eval harness design** — concretely spec the scenario-card format + judge rubric + how it runs. **Backend: Langfuse** (you have it at work) — scenario cards → Langfuse *datasets*, each skill run → a *dataset experiment/run*, the Quality-Bar rubric → an *LLM-as-a-judge evaluator* emitting *scores*; regression = compare run scores over time. Local structural lint stays in CI; Langfuse owns output-quality evals.
- **Agent specs** — draft the `cpo` (and peers) system prompts + allowed-skill lists?
- **product-forge reconciliation** — map which existing product-forge skills the new marketplace supersedes, complements, or leaves alone?

</details>
