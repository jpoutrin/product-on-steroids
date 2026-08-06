# PM Skills — Full Skill Ledger

*Every skill across `phuryn/pm-skills` (68, MIT) + `deanpeters/Product-Manager-Skills` (70, CC-NC ideas-only) + relevant `product-forge` skills, allocated to the 5 plugins and tagged for disposition. Built from the actual `SKILL.md` descriptions, not summaries.*

Date: 2026-08-05 · Owner: Jeremie

## Legend

- **KEEP-IMPORT** — phuryn (MIT), adopt as-is then elevate to our standard (Output Contract + evals). Shippable.
- **GENERATE** — write original. Either net-new, or a capability only deanpeters has (we use its *idea/structure*, never its text — license).
- **DEDUPE** — overlaps an existing `product-forge` skill; pick a winner, don't ship both.
- **DROP / DEFER** — out of the 4-quadrant PM scope, or redundant.
- **(ref: X)** — a deanpeters skill whose idea folds into item X rather than shipping standalone.

## Tally

| Plugin | KEEP-IMPORT | GENERATE | Total to build |
|---|---|---|---|
| pm-discovery | 19 | 11 | 30 |
| pm-strategy | 21 | 13 | 34 |
| pm-gtm | 10 | 6 | 16 |
| pm-execution | 13 | 4 | 17 (– dedupe vs forge) |
| pm-influence | 1 | 9 | 10 |
| cross-cutting | — | 1 | 1 |
| **Total** | **64** | **44** | **~108** |

Dropped/deferred: ~18 (toolkit, interview-prep-for-jobs, AI-product meta, exec-career coaching, meta skill-creators, intel plumbing).

---

## pm-discovery — Customer Insight (Data · VoC · UX)

### KEEP-IMPORT (phuryn, MIT)
| Skill | What it does |
|---|---|
| interview-script | Structured customer interview script, Mom Test / JTBD probes |
| summarize-interview | Interview transcript → JTBD, satisfaction signals, actions |
| opportunity-solution-tree | Torres OST: outcome → opportunities → solutions → experiments *(ref: dean opportunity-solution-tree)* |
| analyze-feature-requests | Cluster + prioritize feature requests by theme/impact/effort |
| brainstorm-ideas-existing / -new | Multi-lens (PM/Design/Eng) ideation |
| brainstorm-experiments-existing / -new | Design validation experiments / pretotypes |
| identify-assumptions-existing / -new | Risky-assumption surfacing (VUFV / 8 risk cats) |
| prioritize-assumptions | Impact × Risk triage + experiment suggestions |
| prioritize-features | Backlog prioritization, top-5 recs |
| customer-journey-map | Stages, touchpoints, emotions, pain, opportunities *(ref: dean customer-journey-map + workshop)* |
| user-personas | 3 research-based personas w/ JTBD/pains/gains |
| user-segmentation | User-level segments from feedback |
| sentiment-analysis | Feedback sentiment + segment insights |
| ab-test-analysis | Significance, sample-size, ship/extend/stop |
| cohort-analysis | Retention curves, adoption trends |
| sql-queries | NL → SQL across dialects (Fluency-with-Data) |

### GENERATE (original; deanpeters = idea ref only)
| Skill | Why generate |
|---|---|
| jobs-to-be-done | Standalone JTBD artifact — phuryn only embeds JTBD elsewhere |
| proto-persona | Hypothesis-based persona *before* research (distinct from user-personas) |
| problem-statement | User-centered problem framing |
| problem-framing-canvas | MITRE canvas — no phuryn equivalent |
| lean-ux-canvas | Lean UX v2 assumptions/learning canvas |
| voice-of-customer-miner | Mine reviews/forums for unmet needs — core VoC sub-competency, missing in phuryn |
| discovery-interview-prep | Plan the interview (goal/segment/method) — complements interview-script |
| discovery-process | End-to-end discovery workflow |
| pol-probe | Savoia proof-of-life / pretotype probe *(ref: dean pol-probe-advisor)* |
| storyboard | Six-frame narrative for alignment |
| derisk-measurement-advisor | What to measure/test to de-risk *(P3)* |

### DEDUPE vs product-forge
- `create-persona` (forge) ↔ user-personas / proto-persona → keep one research + one proto variant.
- `discovery-session` (forge) ↔ discovery-process → pick the stronger workflow.
- `brainstorm-solution` (forge) ↔ brainstorm-ideas-* → likely fold forge's into the phuryn pair.

---

## pm-strategy — Product Strategy (Outcomes · Vision/Roadmap · Strategic Impact)

### KEEP-IMPORT (phuryn, MIT)
| Skill | What it does |
|---|---|
| product-vision | Inspiring/achievable/emotional vision |
| product-strategy | 9-section Product Strategy Canvas |
| value-proposition | 6-part JTBD value prop |
| business-model | Business Model Canvas (9 blocks) |
| lean-canvas | Lean Canvas |
| startup-canvas | Strategy + business model combo |
| monetization-strategy | 3–5 monetization models + validation |
| pricing-strategy | Models, WTP, elasticity |
| swot-analysis | SWOT + actions *(ref: dean swot evidence-cited)* |
| pestle-analysis | Macro factors *(ref: dean pestel)* |
| porters-five-forces | Industry structure *(ref: dean porters → profit pool)* |
| ansoff-matrix | Growth-strategy mapping *(ref: dean ansoff risk-rated)* |
| market-sizing | TAM/SAM/SOM top-down + bottom-up *(ref: dean tam-sam-som-calculator)* |
| competitor-analysis | Competitor strengths/weaknesses/differentiation *(ref: dean competitive-analysis-process)* |
| north-star-metric | NSM + input-metric constellation |
| metrics-dashboard | Dashboard: metrics, sources, thresholds (Outcomes) |
| brainstorm-okrs | Team OKRs aligned to company objectives |
| outcome-roadmap | Output→outcome roadmap rewrite |
| prioritization-frameworks | 9-framework reference (RICE/ICE/Kano…) *(ref: dean prioritization-advisor)* |
| market-segments | 3–5 market segments w/ fit |
| strategy-red-team | Attack load-bearing assumptions of a strategy/PRD |

### GENERATE (original; deanpeters = idea ref only)
| Skill | Why generate |
|---|---|
| roadmap-planning | Full roadmap workflow (prioritize→epics→align→sequence), richer than outcome-roadmap |
| product-strategy-session | End-to-end multi-week strategy workflow |
| feature-investment-advisor | Feature ROI / investment case — missing in phuryn |
| business-health-diagnostic | SaaS health across growth/retention/efficiency/capital |
| saas-revenue-growth-metrics | MRR/ARR, churn, NRR, expansion calcs |
| saas-economics-efficiency-metrics | CAC/LTV/payback/margins |
| finance-metrics-quickref | Fast SaaS metric definitions/benchmarks reference |
| finance-based-pricing-advisor | Ship-a-pricing-move decision via ARPU/NRR/payback *(P2)* |
| press-release | Amazon Working-Backwards PR (vision/value framing) |
| market-landscape-scan | Cited market map before sizing *(P3)* |
| pestel-delta-monitor | Quarterly PESTEL re-scan *(P3)* |
| competitive-intel-watch | Cadence delta-monitoring of competitors *(P3)* |
| build-vs-buy | Structured build/buy/partner decision — net-new, no upstream |

### DEDUPE vs product-forge
- `product-strategy` (forge passive persona) → becomes the seed for the **`cpo` agent**; the phuryn `product-strategy` *canvas* stays as the active deliverable skill. Different roles, keep both.
- `position-product` (forge stub) → superseded by pm-gtm positioning skills.

---

## pm-gtm — Go-to-Market / Positioning / Growth

### KEEP-IMPORT (phuryn, MIT)
| Skill | What it does |
|---|---|
| gtm-strategy | Channels, messaging, metrics, launch timeline |
| gtm-motions | 7 motion types (Inbound…PLG) |
| beachhead-segment | First launch segment by pain/WTP/winnability |
| ideal-customer-profile | ICP from research |
| growth-loops | 5 loop types / flywheels |
| competitive-battlecard | Sales-ready battlecard *(ref: dean battle-card-builder — evidence-sourced)* |
| positioning-ideas | Brainstorm differentiated positioning |
| value-prop-statements | Marketing/sales/onboarding copy from value props |
| product-name | 5 name options + rationale |
| marketing-ideas | 5 cost-effective campaign ideas |

### GENERATE (original; deanpeters = idea ref only)
| Skill | Why generate |
|---|---|
| positioning-statement | Geoffrey Moore statement (distinct artifact from brainstorm) |
| positioning-workshop | Guided positioning session |
| competitive-research-snapshot | Cited landscape + comparison matrix *(ref: dean company-research/company-intel)* |
| acquisition-channel-advisor | Scale/test/kill a channel via unit economics *(P2)* |
| organic-growth-advisor | Which organic growth path to pursue *(P3)* |
| pricing-packaging-tracker | Diffable competitor pricing/packaging time series *(P3)* |

---

## pm-execution — Product Execution (Spec · Delivery · QA)

### KEEP-IMPORT (phuryn, MIT)
| Skill | What it does |
|---|---|
| create-prd | 8-section PRD *(DEDUPE — see below)* |
| user-stories | 3 C's + INVEST |
| job-stories | When/I want/So I can + acceptance |
| wwas | Why-What-Acceptance backlog items |
| sprint-plan | Capacity, story selection, dependencies, risk |
| release-notes | User-facing notes from tickets/PRDs |
| pre-mortem | Tigers/Paper-Tigers/Elephants risk analysis |
| retro | Structured retrospective |
| test-scenarios | Test scenarios from user stories |
| summarize-meeting | Transcript → decisions + action items |
| dummy-dataset | Realistic test data generator (utility) |
| intended-vs-implemented | Gap between spec and actual code (AI-built apps) |
| shipping-artifacts | Minimum durable docs to review a vibe-coded app |

### GENERATE (original; deanpeters = idea ref only)
| Skill | Why generate |
|---|---|
| epic-hypothesis | Frame an epic as a testable hypothesis |
| epic-breakdown-advisor | Split epics via Humanizing Work patterns |
| user-story-mapping | Activities→steps→tasks→release slices |
| user-story-splitting | Split large stories via proven patterns |

### DEDUPE vs product-forge (forge is already strong here — reconcile, don't double)
- **PRD:** forge has `create-prd`, `create-prd-feature` (FRD), `generate-tasks`, `prd-management/-status/-progress/-archive`, `list-prds` (full lifecycle) + phuryn `create-prd` + dean `prd-development`. → Keep forge's **lifecycle**; adopt whichever PRD *content template* is best (likely merge phuryn's 8-section into forge's create-prd).
- **QA:** forge owns this (`create-qa-test`, `qa-test-management`, `qa-testing-methodology`, `qa-screenshot-*`, `enrich-qa-test`, `list-qa-tests`). Neither repo covers QA → **keep forge as-is**; phuryn `test-scenarios` complements.
- **Tasking:** forge `task-orchestration/-list/-focus`, `generate-tasks` → keep forge.

---

## pm-influence — Influencing People (Managing Up · Team Leadership · Stakeholder Mgmt)

*The build-heavy plugin: almost nothing importable, highest originality/value, most worth tailoring to your org.*

### KEEP-IMPORT (phuryn, MIT)
| Skill | What it does |
|---|---|
| stakeholder-map | Power/interest grid + per-quadrant comms plan |

### GENERATE (original; deanpeters = idea ref only, + net-new)
| Skill | Why generate |
|---|---|
| stakeholder-identification | Enumerate all stakeholders before engaging |
| stakeholder-engagement-advisor | Plan engagement for one critical stakeholder / navigate resistance |
| incoming-request-advisor | Decode an incoming ask: literal request vs JTBD (managing up) |
| exec-update | Recurring exec/leadership status narrative — *net-new* |
| alignment-narrative | Written narrative to align cross-functional stakeholders — *net-new* |
| decision-memo | One-page decision doc (context/options/recommendation) — *net-new* |
| managing-up-brief | Prep brief for managing up / 1:1s with leadership — *net-new* |
| escalation | Structured escalation when blocked — *net-new (P3)* |
| executive-onboarding-playbook | 30-60-90 diagnostic for a new product leader |

*(Consider merging phuryn `stakeholder-map` + generated `stakeholder-identification`/`-mapping` into a single coherent stakeholder trio.)*

---

## Cross-cutting (shared infra, not a quadrant plugin)

| Skill | Disposition | Note |
|---|---|---|
| workshop-facilitation | GENERATE | Shared interaction protocol every interactive/workshop skill imports (pacing, one-question turns, progress labels). Highest-leverage shared asset. |

---

## DROP / DEFER (out of the 4-quadrant PM scope)

| Skill(s) | Source | Reason |
|---|---|---|
| draft-nda, grammar-check, privacy-policy | phuryn pm-toolkit | Legal/writing utilities, not PM-quadrant |
| review-resume, product-sense-interview-answer | both | Job-hunting / interview prep |
| ai-shaped-readiness-advisor, context-engineering-advisor, agent-orchestration-advisor, recommendation-canvas, autonomous-investigation | dean | AI-product/agent meta — candidate for a *future* separate `pm-ai` plugin, not the 4 quadrants |
| pm-skill-creator, skill-authoring-workflow | dean | Meta skill-authoring — we use the existing `skill-creator` tooling instead |
| intelligence-collection-disciplines, intel-discipline-advisor, company-intel | dean | Competitive-intel plumbing — folds into `competitive-research-snapshot` |
| director-readiness-advisor, vp-cpo-readiness-advisor, altitude-horizon-framework | dean | Career-transition coaching, not daily PM work *(reconsider for a leadership add-on later)* |
| eol-message | dean | Niche product-comms; revisit under pm-execution/pm-gtm if needed |

---

## What this tells us about the build

- **~64 skills import cleanly from MIT phuryn** — the bulk of the surface, low-risk.
- **~44 need original authoring** — concentrated in `pm-influence` (9 of 10) and the strategy *workflows/finance* set. This is where your time and org-specific knowledge matter most.
- **`pm-execution` is mostly a reconciliation exercise**, not new building — you already own PRD lifecycle + QA in product-forge.
- The **critical path to value** is still: standard + eval harness (Phase 0) → `pm-strategy` → `pm-discovery` → `pm-gtm` → reconcile `pm-execution` → build `pm-influence`.
