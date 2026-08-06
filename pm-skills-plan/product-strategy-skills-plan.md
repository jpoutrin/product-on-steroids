# Product Strategy — Skills Plan

*Planning the agent-skill coverage for the "Product Strategy" quadrant of the Peak Product Manager framework (Ravi Mehta). Scope: skills that help you do the **daily strategy work** of a PM, delivered as `SKILL.md` files in the `product-forge` plugin ecosystem.*

Date: 2026-08-05 · Owner: Jeremie

---

## 1. How I broke down the quadrant

The framework splits **Product Strategy** into three sub-competencies. I've expanded each into the concrete, recurring tasks a PM actually performs, because that's the right granularity for a skill (one skill = one deliverable or one guided decision).

| Sub-competency | What it means day-to-day | Concrete skill needs |
|---|---|---|
| **Business Outcome Ownership** | Owning the P&L / metrics the product moves, not just shipping features | North Star + input metrics, OKRs, business/monetization/pricing model, unit economics, business-health diagnostic, feature ROI/investment cases |
| **Product Vision & Roadmapping** | Setting direction and sequencing bets over time | Product vision, product-strategy canvas, outcome roadmap, prioritization frameworks, opportunity–solution tree, now/next/later communication |
| **Strategic Impact** | Positioning the product to win in its market | Market sizing (TAM/SAM/SOM), competitive analysis + battlecards, positioning, macro/industry analysis (SWOT/PESTEL/Porter/Ansoff), GTM strategy, build-vs-buy / strategic bets |

---

## 2. What you already have in `product-forge`

Coverage today is **thin and mostly passive**. The relevant existing skills:

- `product-strategy` — a *passive persona* skill (`user-invocable: false`). It injects "CPO mindset" + frameworks (JTBD, Lean Startup, PMF, TAM/SAM/SOM) into any strategy conversation, but it produces **no structured deliverable** and can't be invoked on demand.
- `position-product` — an interactive positioning Q&A, but it points at a legacy source path (`claude_settings/python/processes/product-positioning.md`) and is more of a command wrapper than a self-contained skill.
- `discovery-session`, `create-persona`, `create-prd`, `brainstorm-solution` — support strategy indirectly (customer insight / execution), not core strategy artifacts.

**Takeaway:** you have a *mindset* skill and a *positioning* stub. Almost every concrete strategy deliverable (vision, roadmap, prioritization, market sizing, OKRs, metrics, competitive analysis) is currently **uncovered**.

---

## 3. What's importable vs. what to generate

I found two mature open-source PM skill libraries plus several catalogs. The two that matter:

### ⭐ `phuryn/pm-skills` — **MIT licensed**, best import candidate
65+ skills, structured exactly like your repo (plugin folders → `/skills/<name>/SKILL.md`), explicitly built for Claude Code **and Cowork** import. MIT means you can import, adapt, redistribute, and use commercially with only attribution. Relevant plugins: `pm-product-strategy`, `pm-execution`, plus market/competitive and metrics skills. This is the one to lean on.

### `deanpeters/Product-Manager-Skills` — **CC BY-NC-SA 4.0** (caution)
49 well-crafted skills (Altitude-Horizon, Opportunity-Solution Tree, TAM/SAM/SOM, PESTEL, Prioritization Advisor, Roadmap Planning, Finance metrics quickrefs, etc.). Excellent **reference material**, but the license is **non-commercial + share-alike** — if `product-forge` is ever distributed or used commercially, you cannot ship derivatives of it. Use for inspiration/structure, not direct copy, unless you confirm the license is acceptable for your use.

Other catalogs (Snyk "Top 7", Enterpret guide, mcpmarket, ChatGPT-prompts library) mostly re-package these two or offer thinner single-file skills — not worth importing over `phuryn/pm-skills`.

---

## 4. The plan: skill-by-skill for Product Strategy

Legend — **Status**: `HAVE` (exists, usable) · `UPGRADE` (exists but weak, rework) · `IMPORT` (bring in from phuryn/pm-skills, MIT) · `GENERATE` (build new). Priority: **P1** = core daily use, **P2** = frequent, **P3** = situational.

### A. Business Outcome Ownership

| Skill | Purpose | Status | Source / Note | Pri |
|---|---|---|---|---|
| `north-star-metric` | Define North Star + input metrics, business-game classification | IMPORT | phuryn | P1 |
| `metrics-dashboard` | Design a product metrics dashboard (NSM, inputs, thresholds) | IMPORT | phuryn | P2 |
| `brainstorm-okrs` | Draft team OKRs aligned to company objectives | IMPORT | phuryn | P1 |
| `business-model` / `lean-canvas` | Business Model Canvas / Lean Canvas | IMPORT | phuryn | P2 |
| `monetization-strategy` | 3–5 monetization approaches + validation | IMPORT | phuryn | P2 |
| `pricing-strategy` | Pricing models, willingness-to-pay, elasticity | IMPORT | phuryn | P2 |
| `feature-investment-case` | Evaluate a feature/bet by ROI + strategic value | GENERATE | tailor to your metrics stack | P2 |
| `business-health-diagnostic` | Growth/retention/efficiency read on the product | IMPORT/adapt | phuryn + deanpeters ref | P3 |

### B. Product Vision & Roadmapping

| Skill | Purpose | Status | Source / Note | Pri |
|---|---|---|---|---|
| `product-vision` | Craft an inspiring, achievable vision statement | IMPORT | phuryn | P1 |
| `product-strategy-canvas` | 9-section strategy canvas (vision → defensibility) | IMPORT | phuryn (`product-strategy`) — rename to avoid clash with your passive skill | P1 |
| `outcome-roadmap` | Turn a feature list into an outcome-based roadmap | IMPORT | phuryn | P1 |
| `roadmap-communication` | Now/Next/Later view for stakeholders/exec | GENERATE | your format + tie to `prd`/`generate-tasks` | P1 |
| `prioritize-features` | Prioritize backlog by impact/effort/risk/alignment | IMPORT | phuryn | P1 |
| `prioritization-frameworks` | Reference: RICE, ICE, Kano, MoSCoW, Opp. Score | IMPORT | phuryn | P2 |
| `opportunity-solution-tree` | Torres: outcome → opportunities → solutions → tests | IMPORT | phuryn | P2 |
| `product-strategy` (existing) | Keep as passive CPO-mindset layer | HAVE | already active | — |

### C. Strategic Impact

| Skill | Purpose | Status | Source / Note | Pri |
|---|---|---|---|---|
| `market-sizing` | TAM/SAM/SOM, top-down + bottom-up | IMPORT | phuryn | P1 |
| `competitor-analysis` | Strengths/weaknesses/differentiation map | IMPORT | phuryn | P1 |
| `competitive-battlecard` | Sales-ready battlecard + objection handling | IMPORT | phuryn | P2 |
| `positioning` | Positioning statement + workshop | UPGRADE | replace stub `position-product` with self-contained skill (phuryn base) | P1 |
| `swot-analysis` | SWOT + actionable recommendations | IMPORT | phuryn | P3 |
| `pestle-analysis` | Macro-environment scan | IMPORT | phuryn | P3 |
| `porters-five-forces` | Industry competitive-forces read | IMPORT | phuryn | P3 |
| `ansoff-matrix` | Growth-strategy mapping (market × product) | IMPORT | phuryn | P3 |
| `gtm-strategy` | Channels, messaging, metrics, launch plan | IMPORT | phuryn | P2 |
| `build-vs-buy` | Structured build/buy/partner decision | GENERATE | not well covered upstream | P3 |

---

## 5. Suggested sequencing

**Wave 1 — the daily core (P1, ~10 skills).** Import from phuryn and wire in: `product-vision`, `product-strategy-canvas`, `outcome-roadmap`, `prioritize-features`, `north-star-metric`, `brainstorm-okrs`, `market-sizing`, `competitor-analysis`, upgrade `positioning`; generate `roadmap-communication`. This alone takes you from ~10% to ~70% coverage of the quadrant.

**Wave 2 — the frequent supporting set (P2).** Metrics dashboard, prioritization-frameworks reference, opportunity-solution tree, monetization/pricing, business model, battlecard, GTM, feature-investment case.

**Wave 3 — situational analysis (P3).** SWOT / PESTEL / Porter / Ansoff, business-health diagnostic, build-vs-buy.

**Net new to *generate* (not importable well):** `roadmap-communication`, `feature-investment-case`, `build-vs-buy` — plus any that must be tailored to your metrics/PRD conventions.

---

## 6. Two decisions before we build

1. **Import mechanics.** Do you want to (a) add `phuryn/pm-skills` as a *marketplace* and consume it as-is, or (b) copy + adapt individual skills into `product-forge` so they match your house style (frontmatter conventions, `forge-help` index, links to `create-prd`/`generate-tasks`)? Option (b) is more work but keeps everything coherent and under your control.
2. **License posture.** Confirm whether `product-forge` is private/internal (then CC-NC deanpeters material is fine to adapt) or distributed/commercial (then stay MIT-only = phuryn, and treat deanpeters as read-only inspiration).

Once you pick, I can start generating the Wave 1 skills — adapted to your `product-forge` conventions — one at a time.
