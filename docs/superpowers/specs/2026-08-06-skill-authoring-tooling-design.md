# Skill-Authoring Tooling — Design

**Date:** 2026-08-06
**Status:** Approved (design), pending spec review
**Goal:** Cut the per-skill token cost of building out the ~100 remaining skills in
`TASKS.md`, and make malformed skills impossible to commit.

## Problem

Building one skill today re-incurs a fixed token cost every time: re-reading
`docs/SKILL-STANDARD.md` + the gold exemplar + `docs/skill-template/`, hunting the
right phuryn source, hand-typing frontmatter/eval boilerplate, and hand-editing the
`TASKS.md` status table. Multiplied across ~100 skills, that repeated context is the
dominant cost. Two structural gaps compound it:

1. Validation (`validate_plugins.py`) only runs when someone remembers `just test`,
   and it **does not check `template.md` at all** — a skill can ship an empty or
   malformed template and still pass.
2. Nothing gives immediate feedback while authoring; layout errors surface only at a
   later `just test`, costing a correction round-trip.

## Non-goals

- No orchestration engine. The parallel-build story is a documented pattern, not code.
- No validation of a skill's **runtime output** (the memo a skill produces in a user's
  session) — that is produced elsewhere and remains the Quality Bar + eval cards' job.
- No new runtime dependencies. All scripts are Python stdlib only.

## Components

### 1. `scripts/skillkit.py` — single stdlib CLI

One file, subcommands, wired as `just` recipes. Shared internals:

- **TASKS.md row parser** — skill name → `(plugin, disposition, priority, status)`.
- **Section-heading → plugin-dir map** — `## pm-strategy — Product Strategy` → `pm-strategy`.
- **Pinned constants** — `PHURYN_SHA = "18468a9"`; alias map
  `{ "product-strategy-canvas": "product-strategy" }` (the only IMPORT name that does
  not match a phuryn source dir 1:1; all other 63 imports match exactly).

| Recipe | Behavior | Token win |
|---|---|---|
| `just next` | Print the next `todo` skill in build order (pm-strategy→discovery→gtm→execution→influence, P1 first) with its disposition. | No full-ledger re-read to choose work. |
| `just scaffold <skill>` | Copy `docs/skill-template/` into `<plugin>/skills/<skill>/`. Fill frontmatter: `name` (== dir), `version 0.1.0`, `type component`, `source` = `import:phuryn/pm-skills@18468a9` (IMPORT) or `original` (GENERATE). Rename eval stubs to `<skill>-{happy,edge,adversarial}.md` with `id`/`skill` prefilled. Idempotent — refuse if the dir already exists. | Eliminates boilerplate typing. |
| `just context <skill>` | Print ONE self-contained build pack to stdout: (a) the `docs/SKILL-BRIEF.md` cheat-sheet, (b) the TASKS row, (c) for IMPORT — the raw phuryn `SKILL.md` (resolved by name + alias); for GENERATE — the "write original; deanpeters = idea-reference only, never copy text" reminder. | Replaces reading standard + exemplar + template + source-hunt with one command. Primary saver. |
| `just wip <skill>` | Flip that row's Status cell to `wip` via targeted regex on the TASKS.md table row. | No hand-editing the table. |
| `just done <skill>` | **Enforced:** run `validate_plugins.py` on the skill and confirm ≥3 eval cards; only then flip the cell to `done`. Refuse (non-zero exit, explain) otherwise. | Prevents false "done"; encodes the repo's done-definition. |
| `just progress` | Print done/wip/todo counts per plugin + totals. | State at a glance, no full-file read. |

The gold exemplar (`market-sizing`) stays **out** of the per-skill pack — the
cheat-sheet points to its path; read it at most once per session, not once per skill.

### 2. `docs/SKILL-BRIEF.md` — the embedded cheat-sheet

A new ~40-line distillation of `SKILL-STANDARD.md`: frontmatter schema, the required
section list, the linter-enforced rules, and the eval-card shape. `just context`
embeds it so the build pack is small and self-contained. `SKILL-STANDARD.md` remains
the authoritative long-form; `SKILL-BRIEF.md` is the operational quick-reference.

### 3. Linter extension — close the `template.md` gap

Extend `tests/validate_plugins.py` so that, for a skill whose body declares a
structured Output Contract:

- `template.md` **must exist and be non-empty** (error if missing).
- Its `##` headings should **mirror the `## Output Contract` sections** in `SKILL.md`
  (warning on mismatch — advisory, since wording may differ, but flags drift).

This makes "the generated artifact's layout" genuinely enforced rather than assumed.

### 4. Repo-level PostToolUse validation hook

A **committed** `.claude/settings.json` (distinct from the personal
`.claude/settings.local.json`) with a PostToolUse hook: when a `SKILL.md` or an
`evals/*.md` file is Written/Edited, auto-run the linter scoped to that skill and
surface any error inline. One hook at repo level — not per-skill. Immediate feedback,
no manual `just test`, no wasted correction cycle.

### 5. CLAUDE.md — "Efficient authoring workflow" subsection

Add under *Authoring a skill*:

- **Per-skill loop:** `just next` → `just scaffold <s>` → `just context <s>` → author
  the transform+enrich → `just test` (or rely on the auto-hook) → `just done <s>` →
  commit. Read the full standard/exemplar **at most once per session**; rely on
  `just context` thereafter.
- **Batch loop:** skills are independent → dispatch **one subagent per skill**
  (`superpowers:dispatching-parallel-agents`). Each subagent runs `just context <s>`
  for its tiny self-contained context, authors, validates, `just done`, commits. The
  main thread never loads reference material — where savings compound at scale.
- Note the pinned phuryn SHA is set automatically by `scaffold`.

## Data flow (per-skill loop)

```
TASKS.md ──parse──> skillkit next ──> <skill,disposition>
                    skillkit scaffold ──copies──> docs/skill-template/ ──> <plugin>/skills/<skill>/
                    skillkit context  ──reads──> SKILL-BRIEF.md + TASKS row + work/phuryn .../SKILL.md
                                                   └──> single stdout build pack ──> author
author writes SKILL.md/evals ──PostToolUse hook──> validate_plugins.py (scoped) ──> inline pass/fail
                    skillkit done ──gate: lint + >=3 evals──> flip TASKS.md status ──> commit
```

## Error handling

- `scaffold` on an existing dir → refuse, non-zero exit, no mutation.
- `context`/`scaffold`/`wip`/`done` on a skill absent from TASKS.md → error naming the
  skill and the closest matches.
- `context` for an IMPORT whose source is not found under `work/phuryn-pm-skills`
  (after alias) → error telling the user to clone/refresh `work/` (gitignored).
- `done` when the linter fails or eval cards < 3 → refuse with the specific reason;
  the status cell is left untouched.
- Hook: if the linter binary/venv is unavailable, the hook warns but never blocks the
  edit (fail-open, so authoring is never wedged).

## Testing

- `skillkit.py` gets unit coverage for: TASKS parsing, plugin mapping, alias
  resolution, `next` ordering, idempotent `scaffold`, `done` gating (pass and refuse),
  and status-cell regex round-trips — run against a fixture TASKS.md.
- Linter extension: fixtures for missing `template.md`, empty `template.md`, and
  heading mismatch.
- Manual: scaffold + context one real IMPORT (e.g. `product-vision`) and one GENERATE
  (e.g. `roadmap-planning`) end-to-end; confirm `just done` refuses until evals exist.

## Decisions (resolved)

- Scaffold **auto-sets** `source` to the pinned SHA / `original` — SHA is known and constant.
- `just done` **enforces** the done-definition (lint + ≥3 evals) before flipping status.
- Cheat-sheet lives in a **new `docs/SKILL-BRIEF.md`**, embedded by `context`, keeping
  the pack small; `SKILL-STANDARD.md` stays the authoritative long-form.
- One consolidated CLI (`skillkit.py`), not per-function scripts — single TASKS parser.
