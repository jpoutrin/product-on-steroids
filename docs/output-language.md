# Output language

Skills in this marketplace are written in English. The **deliverables they
produce** follow the language of the project they run in.

## Declaring the language

Create `.config/pm-skills.yaml` at the root of the project where you use the
skills:

```yaml
language: fr
```

Use a short language code (`fr`, `de`, `es`, `ja`, …). `en` — or no file at all —
means English, and nothing is injected.

`.config/` is a convention with room to grow: further per-project settings can be
added there later without a new dotfile in the repo root for each one. Today
`language` is the only key this marketplace reads.

## Resolution order

1. A language the user explicitly asks for in the prompt — always wins.
2. `language:` in `.config/pm-skills.yaml`.
3. English.

The language is **declared, never inferred**. Nothing is read from the language of
existing docs, and `CLAUDE.md` is not a source: two sources that can disagree
reintroduce exactly the inconsistency this removes.

## How it works

Each plugin ships a `SessionStart` hook (`hooks/output_language.py`, wired by
`hooks/hooks.json`). Once per session it reads the settings file and, only when a
non-English language is declared, injects:

> Deliverables produced by PM skills in this project are written in **French**.
> Keep established PM terms (TAM/SAM/SOM, RICE, JTBD, NPS, ICP, OKR)
> untranslated, and preserve template `<!--#anchor-->` comments verbatim. Skill
> instructions and eval cards stay English.

## Why templates carry `<!--#anchor-->` comments

Each `##`/`###` heading in a `template.md` ends with an anchor:

```markdown
## Market Definition <!--#market-definition-->
```

The `PostToolUse` conformance hook checks a produced document against its
skill's template. Matching on English heading text would silently pass any
translated document; matching on the anchor works in any language. The anchor
therefore has to survive into the deliverable. It is invisible in every rendered
view (GitHub, Notion, Confluence, PDF) and visible only when reading raw
markdown — the accepted cost of keeping the structural gate.

Anchors are generated, never hand-written: `just anchors [plugin]`. The linter
rejects a template whose headings lack anchors or whose anchors collide.
Renaming a heading keeps its existing anchor — the slug is an opaque identifier,
and regenerating it would orphan every document already produced from that
template.

## What stays English

`SKILL.md` bodies, eval cards, `template.md` sources, the linter, hooks, and
`scripts/`. Only the produced deliverable is translated.

## Limitations

- With hooks disabled, or a skill used outside Claude Code, no directive is
  injected and output defaults to English. The setting has no effect without the
  hook.
- With all five plugins installed, a non-English project gets the directive five
  times (~4 lines each). The hooks are separate processes racing at startup, so
  there is no clean dedupe.
- A deliverable that translates its headings **and** drops every anchor is
  indistinguishable from an unrelated file, and passes silently. This is
  unavoidable: the hook only speaks up once a file matches at least half the
  template, and with no anchors and no English headings nothing matches. It is
  mitigated, not closed — the injected directive says to preserve anchors, the
  hook repeats that instruction whenever it fires, and `market-sizing`'s French
  eval card asserts the anchors survive. A document that keeps its English
  headings *is* caught: heading text still counts toward the recognition
  threshold, so the missing anchors are reported and restored on the next edit.
- The directive is carried by the `SessionStart` hook, which fires only for a
  language declared in `.config/pm-skills.yaml`. Asking for a language in the
  prompt (resolution rule 1) inside an English-configured project therefore
  translates the deliverable with **no** preserve-anchors instruction — straight
  into the fail-open above. Declare the language in `.config/pm-skills.yaml` for
  the reliable path.
