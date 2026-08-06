# product-forge ↔ new PM marketplace — Reconciliation

*The new `pm-skills` marketplace is standalone, so a user can have both it and `product-forge` installed at once. That creates trigger collisions (two `create-prd`, two `discovery`…). This maps every PM-relevant product-forge skill to: SUPERSEDE, COMPLEMENT, or LEAVE ALONE — so nothing fires twice and nothing valuable gets lost.*

Date: 2026-08-05 · Owner: Jeremie · Scope: the `product-design` plugin in product-forge (44 skills). The monorepo's dev/infra skills (django, aws, mcp, dbt, python/ts style, etc.) are other plugins — out of scope, untouched.

## Legend
- **SUPERSEDE** — new marketplace does it better/canonically. Retire or disable the forge version when the new one lands, so it doesn't double-fire.
- **COMPLEMENT** — both stay; they operate at different layers (forge owns lifecycle/tooling; new owns the *content* artifact). Differentiate descriptions so only the intended one triggers.
- **LEAVE ALONE** — not in the 4-quadrant PM scope; the new marketplace never touches it.

---

## SUPERSEDE (new marketplace becomes source of truth)

| product-forge skill | New counterpart | Why | Action |
|---|---|---|---|
| `product-strategy` (passive CPO persona, `user-invocable:false`) | `cpo` **agent** + `pm-strategy/product-strategy` (canvas skill) | Forge's is a mindset injector with no deliverable; the agent carries the persona, the skill produces the canvas | Retire forge persona; seed its text into the `cpo` agent prompt |
| `position-product` (stub pointing at a legacy path) | `pm-gtm`: positioning-ideas / positioning-statement / positioning-workshop | Forge's is a broken wrapper | Retire |
| `create-persona` | `pm-discovery`: user-personas + proto-persona | New split (research-based vs hypothesis-based) is richer + has Output Contract | Supersede (or keep forge name as a thin alias to user-personas) |
| `discovery-session` | `pm-discovery`: discovery-process (+ discovery-interview-prep) | New is a full workflow to the standard | Supersede |
| `brainstorm-solution` | `pm-discovery`: brainstorm-ideas-* / brainstorm-experiments-* | New multi-lens ideation is broader | Supersede |

---

## COMPLEMENT (keep both, different layers — reconcile content, don't double-fire)

| product-forge skill | New counterpart | Division of labor |
|---|---|---|
| `create-prd` | `pm-execution/create-prd` | **Forge owns the PRD lifecycle** (see below); adopt whichever *content template* is stronger (likely merge phuryn's 8-section body into forge's create-prd). One canonical PRD skill, not two |
| `create-prd-feature` (FRD) | — | Forge-only; keep. New marketplace has no FRD skill |
| `generate-tasks` | — | Forge-only; execution tasking. Keep. Pairs with the new PRD content |
| `prd-management`, `prd-status`, `prd-progress`, `prd-archive`, `list-prds` | — | Forge-only PRD **lifecycle**. Keep entirely — the new marketplace deliberately doesn't do lifecycle |
| QA suite: `create-qa-test`, `qa-test-management`, `qa-testing-methodology`, `qa-screenshot-management`, `qa-screenshot-validation`, `qa-element-extraction`, `enrich-qa-test`, `list-qa-tests` | `pm-execution/test-scenarios` (complements) | **Forge owns QA** — neither source repo covers it. `test-scenarios` (generate scenarios from stories) feeds forge's QA tests; keep both, wire them |
| `task-orchestration`, `task-list`, `task-focus` | — | Forge-only execution tasking. Keep |
| `design-system` | (adjacent to a future UX/UI scope) | Forge-only; leave. Could complement a later UX plugin, not in the 4 quadrants now |

---

## LEAVE ALONE (dev/infra tooling — not PM-quadrant, new marketplace never overlaps)

| product-forge skills | Nature |
|---|---|
| `agent-tools`, `ctx`, `forge-help`, `quick-start` | Forge meta/onboarding |
| `browser-debug`, `console-debugging`, `debug-orchestrator`, `install-chrome-devtools-mcp`, `network-inspection` | Web-debug tooling |
| `parallel-agents`, `parallel-decompose`, `parallel-execution`, `parallel-integrate`, `parallel-prompt-generator`, `parallel-run`, `parallel-setup`, `parallel-task-format`, `parallel-validate-prompts` | Multi-agent dev orchestration |

Plus the rest of the monorepo (django/aws/gcp/mcp/dbt/sqlmesh/python/typescript plugins) — entirely separate concern.

---

## Net effect

- **5 forge skills retire** (superseded), their value absorbed by richer, tested marketplace skills — one becomes the `cpo` agent.
- **PRD + QA + tasking stay in forge** as complements — that's your Product Execution strength, and the new `pm-execution` plugin leans on it rather than rebuilding (matches the ledger: pm-execution is mostly reconciliation).
- **Everything else in forge is untouched.**

### Collision-avoidance rule
For every COMPLEMENT pair, make the descriptions mutually exclusive so Cowork triggers only one: forge's PRD skill says "manage the PRD lifecycle / status / tasks," the marketplace's says "draft the PRD content." Same for personas, discovery, brainstorming once the SUPERSEDE retirements land. Simplest safe path: **disable the 5 superseded forge skills** the day the marketplace is installed.

## One decision for you
When the marketplace ships, do you want to **hard-retire** the 5 superseded forge skills (cleanest), or keep them as **thin aliases** that call into the new ones (less breakage if other forge workflows reference them)?
