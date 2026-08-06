# Skill Task Ledger

Working source of truth for building out the marketplace, **one skill per commit**.
Allocations follow `pm-skills-plan/pm-skills-ledger.md` and `pm-skills-architecture.md`;
adjust rows as reality dictates.

**Legend**
- **Disposition:** `IMPORT` = adapt from MIT [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills) (record `source: import:phuryn/pm-skills@<sha>`) · `GENERATE` = write original (deanpeters = idea reference only, never copied text).
- **Priority:** `P1` daily core (Wave 1) · `P2` frequent support · `P3` situational.
- **Status:** `todo` · `wip` · `done`.
- Each shipped skill must pass `python tests/validate_plugins.py` and carry ≥ 3 eval cards.

Build order: **pm-strategy → pm-discovery → pm-gtm → pm-execution → pm-influence**, P1 first within each.

---

## pm-strategy — Product Strategy

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| market-sizing | IMPORT | P1 | done |
| product-vision | IMPORT | P1 | done |
| product-strategy-canvas | IMPORT | P1 | done |
| outcome-roadmap | IMPORT | P1 | done |
| prioritize-features | IMPORT | P1 | done |
| north-star-metric | IMPORT | P1 | done |
| brainstorm-okrs | IMPORT | P1 | done |
| competitor-analysis | IMPORT | P1 | done |
| roadmap-planning | GENERATE | P1 | done |
| roadmap-communication | GENERATE | P1 | done |
| value-proposition | IMPORT | P2 | done |
| business-model | IMPORT | P2 | done |
| lean-canvas | IMPORT | P2 | done |
| monetization-strategy | IMPORT | P2 | done |
| pricing-strategy | IMPORT | P2 | done |
| metrics-dashboard | IMPORT | P2 | done |
| prioritization-frameworks | IMPORT | P2 | done |
| market-segments | IMPORT | P2 | done |
| feature-investment-advisor | GENERATE | P2 | done |
| product-strategy-session | GENERATE | P2 | done |
| press-release | GENERATE | P2 | done |
| saas-revenue-growth-metrics | GENERATE | P2 | done |
| saas-economics-efficiency-metrics | GENERATE | P2 | done |
| finance-metrics-quickref | GENERATE | P2 | done |
| finance-based-pricing-advisor | GENERATE | P2 | done |
| startup-canvas | IMPORT | P3 | done |
| swot-analysis | IMPORT | P3 | done |
| pestle-analysis | IMPORT | P3 | done |
| porters-five-forces | IMPORT | P3 | done |
| ansoff-matrix | IMPORT | P3 | done |
| strategy-red-team | IMPORT | P3 | done |
| business-health-diagnostic | GENERATE | P3 | done |
| build-vs-buy | GENERATE | P3 | done |
| market-landscape-scan | GENERATE | P3 | done |
| pestel-delta-monitor | GENERATE | P3 | done |
| competitive-intel-watch | GENERATE | P3 | todo |

## pm-discovery — Customer Insight

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| interview-script | IMPORT | P1 | todo |
| summarize-interview | IMPORT | P1 | todo |
| opportunity-solution-tree | IMPORT | P1 | todo |
| user-personas | IMPORT | P1 | todo |
| customer-journey-map | IMPORT | P1 | todo |
| jobs-to-be-done | GENERATE | P1 | todo |
| problem-statement | GENERATE | P1 | todo |
| discovery-process | GENERATE | P1 | todo |
| analyze-feature-requests | IMPORT | P2 | todo |
| brainstorm-ideas-existing | IMPORT | P2 | todo |
| brainstorm-ideas-new | IMPORT | P2 | todo |
| brainstorm-experiments-existing | IMPORT | P2 | todo |
| brainstorm-experiments-new | IMPORT | P2 | todo |
| identify-assumptions-existing | IMPORT | P2 | todo |
| identify-assumptions-new | IMPORT | P2 | todo |
| prioritize-assumptions | IMPORT | P2 | todo |
| user-segmentation | IMPORT | P2 | todo |
| sentiment-analysis | IMPORT | P2 | todo |
| ab-test-analysis | IMPORT | P2 | todo |
| cohort-analysis | IMPORT | P2 | todo |
| sql-queries | IMPORT | P2 | todo |
| proto-persona | GENERATE | P2 | todo |
| problem-framing-canvas | GENERATE | P2 | todo |
| lean-ux-canvas | GENERATE | P2 | todo |
| voice-of-customer-miner | GENERATE | P2 | todo |
| discovery-interview-prep | GENERATE | P2 | todo |
| pol-probe | GENERATE | P3 | todo |
| storyboard | GENERATE | P3 | todo |
| derisk-measurement-advisor | GENERATE | P3 | todo |

## pm-gtm — Go-to-Market

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| gtm-strategy | IMPORT | P1 | todo |
| ideal-customer-profile | IMPORT | P1 | todo |
| beachhead-segment | IMPORT | P1 | todo |
| positioning-ideas | IMPORT | P1 | todo |
| positioning-statement | GENERATE | P1 | todo |
| gtm-motions | IMPORT | P2 | todo |
| growth-loops | IMPORT | P2 | todo |
| competitive-battlecard | IMPORT | P2 | todo |
| value-prop-statements | IMPORT | P2 | todo |
| product-name | IMPORT | P2 | todo |
| marketing-ideas | IMPORT | P2 | todo |
| positioning-workshop | GENERATE | P2 | todo |
| competitive-research-snapshot | GENERATE | P2 | todo |
| acquisition-channel-advisor | GENERATE | P2 | todo |
| organic-growth-advisor | GENERATE | P3 | todo |
| pricing-packaging-tracker | GENERATE | P3 | todo |

## pm-execution — Product Execution

Reconcile with the existing `product-design` (Product Forge) PRD/QA/tasking suite:
Forge owns PRD **lifecycle** + QA; here we own PRD/story **content**. See
`pm-skills-plan/pm-forge-reconciliation.md`.

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| create-prd | IMPORT | P1 | todo |
| user-stories | IMPORT | P1 | todo |
| test-scenarios | IMPORT | P1 | todo |
| job-stories | IMPORT | P2 | todo |
| wwas | IMPORT | P2 | todo |
| sprint-plan | IMPORT | P2 | todo |
| release-notes | IMPORT | P2 | todo |
| pre-mortem | IMPORT | P2 | todo |
| retro | IMPORT | P2 | todo |
| summarize-meeting | IMPORT | P2 | todo |
| dummy-dataset | IMPORT | P2 | todo |
| intended-vs-implemented | IMPORT | P2 | todo |
| shipping-artifacts | IMPORT | P2 | todo |
| user-story-mapping | GENERATE | P2 | todo |
| user-story-splitting | GENERATE | P2 | todo |
| epic-hypothesis | GENERATE | P2 | todo |
| epic-breakdown-advisor | GENERATE | P3 | todo |

## pm-influence — Influencing People

Build-heavy: almost nothing importable, highest originality. See
`pm-skills-plan/pm-influence-plugin.md`.

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| stakeholder-map | IMPORT | P1 | todo |
| exec-update | GENERATE | P1 | todo |
| decision-memo | GENERATE | P1 | todo |
| managing-up-brief | GENERATE | P1 | todo |
| stakeholder-identification | GENERATE | P2 | todo |
| stakeholder-engagement-advisor | GENERATE | P2 | todo |
| incoming-request-advisor | GENERATE | P2 | todo |
| alignment-narrative | GENERATE | P2 | todo |
| raci-decision-rights | GENERATE | P2 | todo |
| feedback-note | GENERATE | P2 | todo |
| escalation | GENERATE | P3 | todo |
| executive-onboarding-playbook | GENERATE | P3 | todo |

## Cross-cutting

| Item | Disposition | Priority | Status |
|------|-------------|----------|--------|
| workshop-facilitation (shared interaction protocol) | GENERATE | P1 | todo |

---

## Agents (one anchor per quadrant + router)

| Agent | Plugin | Status |
|-------|--------|--------|
| cpo | pm-strategy | seeded |
| product-discovery-specialist | pm-discovery | seeded |
| gtm-strategist | pm-gtm | seeded |
| delivery-lead | pm-execution | seeded |
| product-influence-partner | pm-influence | seeded |
| pm-orchestrator (router) | pm-strategy (cross-cutting) | seeded |

---

## Deferred (later passes, not counted above)

- **Langfuse eval pipeline** — `sync_evals.py`, `run_evals.py`, `gate.py`, GitHub Action. Needs `LANGFUSE_HOST` + public/secret keys + judge-model choice.
- **Forge reconciliation actions** — retire/alias the 5 superseded `product-design` skills (`product-strategy`, `position-product`, `create-persona`, `discovery-session`, `brainstorm-solution`) when this marketplace installs alongside Forge.
- **Dropped (out of PM scope):** pm-toolkit (NDA, resume, grammar, privacy), interview-prep/job-hunting, AI-product meta, career-transition coaching, intel plumbing.
