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
> untranslated. Skill instructions and eval cards stay English.

## How a translated document is still checked

A `PostToolUse` hook checks each produced document against its skill's template.
It compares **structure**, not words: it reports the sections the template has
and the document does not, matching them by heading level and order. It also
reads what kind of content each section holds — paragraph, list, table and its
column count — but only to work out whether the file it is looking at is the
skill's deliverable at all (see below); it never reports a section for holding
the wrong kind of content.

Structure survives translation; heading text does not. So a memo whose every
heading is in French matches its English template exactly, and the document
carries no markers, comments or frontmatter of any kind.

When a section is missing, the hook locates it by heading level and by its
neighbours — which is what makes the message usable in a document written in
another language — and offers the template's English heading as a candidate
name:

> A section is missing: a level-2 section between "TAM — Total Addressable
> Market" and "SOM — Serviceable Obtainable Market" — probably "SAM —
> Serviceable Addressable Market".

The level and the neighbours are reliable. The name is a best guess and is worded
as one: two sections with the same shape are interchangeable to a shape check, so
when one of a pair of lookalikes is dropped the hook cannot always tell which.
Over the whole corpus the *number* of missing sections is right every time and
the name about three times in four.

A section a template draws several times — Frame 1, Frame 2, … — is understood as
a repeating block. A document may contain as many as it needs, and at least one.

### When the hook decides to speak at all

The hook runs on every markdown file you write while a PM skill is loaded, and
most of them are not that skill's deliverable. So before reporting anything it
asks whether this file *is* the deliverable, and it only says yes when **at least
half the template's sections are already present with an exactly matching shape**
— same heading level, and the same kinds of content in the same order. A README
or a page of meeting notes does not clear that bar, whatever it is called and
whatever language it is in, so nothing is reported for it.

That is the one place content kinds are decisive. Once a file is recognised, a
section counts as present on a much weaker match, so a wrong table width or a
list where the template shows a paragraph is not reported as an error.

## Making a template your own

Copy a skill's `template.md` to `.config/pm-skills/<skill>/template.md` in your
project and the hook enforces that instead of the plugin's. Translate the
headings, the bullet labels and the table column headers; drop sections you never
fill in; add ones you need. It is the same markdown file — there is nothing new
to learn, and nothing to keep in sync.

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
- A language asked for in the prompt (resolution rule 1) does not go through the
  `SessionStart` hook, so it gets no directive — only the prose language changes,
  and PM jargon may be translated when it should not be. Declaring the language
  in `.config/pm-skills.yaml` is the reliable path.
- Structural checking is deliberately coarse: it verifies that sections exist, at
  the right level, in the right order. Content kinds decide only whether the file
  is the deliverable at all — they never make a section count as missing, so a
  section holding the wrong kind of content is not reported. Whether a figure is
  cited or an assumption carries a confidence level is a question of quality, and
  belongs to each skill's eval cards.
- The reported *name* of a missing section is a candidate, not a finding: right
  about three times in four. The count, the level and the neighbours are right.
