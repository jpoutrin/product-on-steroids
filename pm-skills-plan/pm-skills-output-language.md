# Output Language — design

**Status:** approved design, not yet implemented
**Date:** 2026-09-05

## Problem

Every `template.md` in this repo is written in English, and skills produce deliverables that
mirror their template. A French team using `pm-strategy` gets an English market-sizing memo.
The deliverable should follow the language of the project it is produced in; the skill
instructions should not.

The obstacle is not the prose — a model translates a template happily. It is
`check_output_conformance.py`, the PostToolUse hook wired into 110 skills. It enforces
structure by literal string matching on English `##`/`###` headings:

```python
present = [h for h in want if h in content]
if len(present) * 2 < len(want):
    return 0, ""          # treated as an unrelated file — silent pass
```

A French deliverable matches zero headings, falls under the half threshold, and the hook
**fails open silently**. Telling the model to translate therefore costs us the only automated
structural gate the repo has, with no error to signal it.

## Options considered

| Option | Files added per language | Enforcement survives | Drift risk | Verdict |
|--------|--------------------------|----------------------|------------|---------|
| A — `template.fr.md` per skill | 110 | only with extra path plumbing | high | rejected |
| B — translate, no other change | 0 | **no** (silent fail-open) | none | rejected |
| C — language-agnostic anchors | 0 | yes | none | **chosen** |
| D — per-language heading dictionary | 1 | yes | low | rejected on measurement |

**A** was rejected on maintenance: 110 mirrored files per language, and every template edit
(four "add sources table" commits shipped in one week) doubles. **B** is free and guts the
gate. **D** was rejected on a measurement: the 816 template headings are **719 unique** — only
17 appear three or more times — so a heading dictionary is ~719 entries per language, not the
~40 the idea assumed.

**C** was chosen: give each template heading a stable, language-independent id, and match on
that instead of on prose.

### Accepted cost

Anchors must survive into the produced document, because the hook inspects the document. A
generated memo therefore carries `<!--#market-definition-->` next to each heading — invisible
in every rendered view (GitHub, Notion, Confluence, PDF), visible when reading raw markdown.
The alternative considered and declined was a count-and-order check: no leakage and no
migration, but it cannot name the missing section and passes a document with the right shape
and the wrong content.

## Design

### 1. Language resolution

The language is **declared**, never inferred. A consuming project sets it in
`.config/pm-skills.yaml` at its repo root:

```yaml
language: fr
```

`.config/` is a deliberate convention rather than a single dotfile: it scales to further
per-project settings (default currency, region, org name) without adding a file to the repo
root for each one.

Resolution order, in full:

1. a language the user explicitly asks for in the prompt — always wins;
2. `language:` in `.config/pm-skills.yaml`;
3. English.

Nothing is inferred from the language of existing docs, and `CLAUDE.md` is not a source.
Two sources that can disagree reintroduce exactly the inconsistency this design removes.

### 1a. Delivery: a SessionStart hook

Each plugin ships `hooks/hooks.json` with a `SessionStart` hook that reads the settings file
once per session and injects the directive as `hookSpecificOutput.additionalContext`. The
mechanism is confirmed working in Claude Code — `superpowers` uses it to inject
`using-superpowers` at startup (`hooks/session-start` in that plugin is the reference
implementation for the JSON output shape, including its Cursor/Copilot fallbacks).

Injected text, when and only when a non-English language is declared:

> Deliverables produced by PM skills in this project are written in **<language>**. Keep
> established PM terms (TAM/SAM/SOM, RICE, JTBD, NPS, ICP, OKR) untranslated, and preserve
> template `<!--#anchor-->` comments verbatim. Skill instructions and eval cards stay English.

If the file is absent or declares `language: en`, the hook emits nothing. English projects
pay no context cost and see no behaviour change.

**Parsing:** a `^language:\s*(\S+)` regex, not PyYAML. The repo already hand-rolls a
frontmatter parser to avoid a YAML dependency, and hooks are stdlib-only `python3` so they
run on an end user's machine.

Always English, in every project: `SKILL.md` bodies, eval cards, `template.md` source,
linter, hooks, and `scripts/`. Only the produced deliverable is translated.

**Why not a rule in each `## Output Contract`.** The earlier draft repeated a two-line
language rule across all 110 `SKILL.md` files. Injected context is deterministic, costs
nothing at generation time, cannot be forgotten by a skill, and removes a 110-file edit from
the rollout.

**Accepted caveat.** With hooks disabled, or a skill used outside Claude Code, no directive is
injected and output defaults to English. That degrades to the current behaviour rather than to
a wrong-language document, but it does mean the setting has no effect without the hook. A user
with all five plugins installed gets the block five times (~4 lines each, non-English projects
only); the hooks are separate processes racing at startup, so there is no clean dedupe.

### 2. Anchors in templates

Each `##`/`###` heading in a `template.md` gains a trailing anchor comment:

```markdown
## Market Definition <!--#market-definition-->
```

- Slug is derived from the English heading: lowercase, non-alphanumerics collapsed to `-`,
  leading/trailing `-` stripped.
- Slugs are unique within a template; a collision appends `-2`, `-3`.
- Applied by a new `scripts/skillkit.py anchors` subcommand across all 110 templates. No
  hand-editing.
- `docs/skill-template/template.md` and `cmd_scaffold` emit anchors, so new skills inherit
  the convention.

### 3. Anchor-first conformance hook

`check_output_conformance.py` changes from text matching to anchor matching, with a text
fallback:

1. Parse each template heading into `(anchor, text)`, where `anchor` is the
   `<!--#slug-->` comment if present.
2. If **any** template heading carries an anchor, run in anchor mode: `present` is the set of
   `<!--#slug-->` strings found in the written file. Otherwise run in text mode — today's
   behaviour, unchanged.
3. The half-threshold gate is unchanged in both modes, so an unrelated file still passes
   silently.
4. The "missing sections" message names the **English heading text**, not the slug, so the
   feedback stays readable.

The text fallback is what makes the rollout incremental: a template that has not been
migrated yet behaves exactly as it does today.

**The script exists as five byte-identical copies** (`pm-*/scripts/check_output_conformance.py`,
md5 `0e5f620c…`). All five must be updated in the same commit or the plugins diverge.

### 4. Linter checks

`tests/validate_plugins.py` gains two checks over each skill's `template.md`:

- every `##`/`###` heading carries an anchor;
- anchors are unique within the template.

Both land as **warnings** first and are promoted to **errors** once migration completes. This
is what stops the ~40 skills still `todo` in `TASKS.md` from reintroducing the problem.

### 5. Evals

No per-skill language eval. Adding a fourth card to 110 skills is disproportionate to the
risk. Instead, `market-sizing` — the gold exemplar — gains one eval card covering a
French-language project, and `docs/SKILL-STANDARD.md` documents it as the pattern to copy if
a skill has language-sensitive output.

## Rollout

Nine commits, no skill rewrites.

1. `feat(tooling): anchor-aware output conformance hook` — all five hook copies, plus unit
   coverage for anchor mode, text fallback, and the threshold gate.
2. `feat(tooling): warn on template headings without anchors` — linter check at warning level.
3. `feat(tooling): skillkit anchors subcommand` — the migration tool, plus `scaffold` and
   `docs/skill-template/template.md` emitting anchors.
4–8. `chore(<plugin>): add section anchors to templates` — one commit per plugin (five
   plugins), scripted.
9. `feat(tooling): output-language SessionStart hook` — `hooks/hooks.json` and
   `hooks/session-start` in all five plugins, `.config/pm-skills.yaml` documented in
   `README.md` and `docs/output-language.md`, the `market-sizing` eval card, and the linter
   check promoted from warning to error.

`just test` must pass at every step.

## Out of scope

- Translating `SKILL.md`, eval cards, or templates themselves.
- Any per-language template variant.
- A heading dictionary or translation-memory layer.
- Any language source beyond `.config/pm-skills.yaml` and an explicit request in the prompt —
  no inference from repo contents, no `CLAUDE.md` key, no plugin-wide setting.
- Any `.config/pm-skills.yaml` key other than `language`. The directory is chosen so more keys
  can be added later; none are in scope now.
