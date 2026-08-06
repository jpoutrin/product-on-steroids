# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **Claude Code plugin marketplace for product-management skills**. It is a content-authoring
repo, not an application: the "code" is a structural linter, and the deliverables are **skills**
(`SKILL.md` + `template.md` + `evals/`) and **agents** (`agents/*.md`) organized across five
plugins on the four Peak Product Manager quadrants (Ravi Mehta):

- `pm-strategy` — Product Strategy (also hosts the cross-cutting `pm-orchestrator` router)
- `pm-discovery` — Customer Insight
- `pm-gtm` — Go-to-Market
- `pm-execution` — Product Execution
- `pm-influence` — Influencing People

`.claude-plugin/marketplace.json` lists the five plugins; each plugin has its own
`.claude-plugin/plugin.json`, `skills/`, and `agents/`. Only `market-sizing` (in `pm-strategy`)
is currently built out — it is the **gold exemplar** to copy conventions from. The full backlog
lives in `TASKS.md`.

## Commands

Tooling is managed with [`uv`](https://docs.astral.sh/uv/) and run via [`just`](https://github.com/casey/just):

```bash
just setup            # uv sync — create the venv, install deps
just test             # run the structural linter (blocking; non-zero exit on any error)

uv run validate-plugins          # the linter directly (equivalent to `just test`)
uv run python tests/validate_plugins.py [path]   # run without the installed console script
```

There is no build step and no runtime app. `just test` is the only gate; run it before every
commit. It scans every directory containing `.claude-plugin/` and validates manifests, `SKILL.md`
frontmatter/body, and eval cards. Warnings are advisory; **errors fail** (exit 1).

## Authoring a skill (the core workflow)

Every skill follows `docs/SKILL-STANDARD.md`. To create one, **copy `docs/skill-template/` into
`<plugin>/skills/<skill-name>/`** and fill it in. The layout is fixed:

```
<plugin>/skills/<skill-name>/
├── SKILL.md          # frontmatter + body
├── template.md       # fill-in output template (required if the Output Contract is a structured artifact)
└── evals/            # ≥ 3 scenario cards: happy + edge + adversarial
```

### Efficient authoring workflow (token-lean)

Tooling lives in `scripts/skillkit.py`, exposed as `just` recipes. Use it instead of
re-reading the standard/exemplar every time — read `docs/SKILL-STANDARD.md` and the
gold exemplar **at most once per session**; `just context` carries the rest.

**Per-skill loop:**
1. `just next` — pick the next `todo` skill in build order.
2. `just scaffold <skill>` — generate the dir with frontmatter (incl. pinned `source`
   SHA), `template.md`, and three eval stubs. Idempotent; refuses to overwrite.
3. `just context <skill>` — print the one-shot build pack: the `SKILL-BRIEF` cheat-sheet,
   the ledger row, and (for IMPORT) the raw phuryn source to adapt. This replaces
   reading the standard + exemplar + template + hunting the source.
4. Author the skill (IMPORT = restructure/enrich phuryn into the house sections;
   GENERATE = original, `deanpeters` is idea-reference only).
5. `just test` (the PostToolUse hook also lints each SKILL.md/eval edit automatically).
6. `just done <skill>` — runs the linter gate, then flips the TASKS.md row to `done`.
7. Commit: `feat(<plugin>): <skill> skill`.

**Batch loop (parallel, keeps main context small):** skills are independent, so dispatch
**one subagent per skill** (`superpowers:dispatching-parallel-agents`). Each subagent
runs `just context <skill>` for its own tiny self-contained context, authors, validates,
`just done`s, and commits its single skill. The main thread never loads reference
material — that's where the savings compound.

`just progress` shows done/wip/todo per plugin at a glance.

**Linter-enforced requirements** (from `tests/validate_plugins.py`):
- Frontmatter must have `name` (== directory name), `description`, `version` (semver), `type`, `source`.
  - `type` ∈ `{component, interactive, workflow}`.
  - `source` is `original` or `import:<owner>/<repo>@<sha>` (regex-checked).
  - `description` should contain a trigger phrase ("Use when …") so Claude auto-loads the skill — missing it is a warning.
- Body must contain the sections `## Output Contract` and `## Validation & Eval` (case-insensitive).
- `evals/` must exist with **≥ 3 cards**; each card needs a unique `id`, `skill` (== skill name),
  a non-empty `expected` list, and a non-empty `rubric` map.

By convention (reviewed, not linted) the body also carries `## Purpose` (with a "When NOT to use"),
`## Inputs`, `## Process`, `## Quality Bar` (a self-check the skill runs *before returning*), and
`## References`. See `pm-strategy/skills/market-sizing/SKILL.md` for the pattern to match.

## Provenance & licensing rules (do not violate)

`TASKS.md` marks each skill `IMPORT` or `GENERATE`:
- **IMPORT** — adapt from the MIT-licensed [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills);
  record `source: import:phuryn/pm-skills@<sha>` with the actual commit SHA.
- **GENERATE** — write original; set `source: original`.
- `deanpeters/Product-Manager-Skills` is **idea reference only** — its CC BY-NC-SA license means
  **never copy its text**.

Source repos are cloned into `work/` (gitignored, never shipped).

## Commit discipline

Ship **one skill per commit**: `feat(<plugin>): <skill> skill`. Update the skill's row in `TASKS.md`
(`todo` → `wip` → `done`) in the same commit. A skill is "done" only when `just test` passes and it
carries ≥ 3 eval cards. Build order is `pm-strategy → pm-discovery → pm-gtm → pm-execution →
pm-influence`, P1 priority first within each.

## Notes

- The linter ships a **self-contained YAML frontmatter parser** (no PyYAML dependency) supporting the
  subset this repo uses: scalars, folded/literal blocks, block lists, and one level of nested maps.
  If frontmatter fails to parse, check it against that subset rather than assuming full YAML.
- The Langfuse **output-eval pipeline** referenced in the standard is deferred (no credentials yet);
  until it is wired, reviewers judge output against each skill's Quality Bar and eval cards.
- Design docs and rationale live in `pm-skills-plan/` (architecture, ledger, per-plugin plans,
  eval-pipeline design, and Product Forge reconciliation).
