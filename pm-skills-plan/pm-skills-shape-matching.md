# Shape Matching — design

**Status:** proposed design, not yet implemented
**Date:** 2026-09-06
**Supersedes:** the enforcement half of `pm-skills-output-language.md` (merged as `0151c16`).
The language-declaration half of that design — `.config/pm-skills.yaml`, the SessionStart
hook, `docs/output-language.md` — stands unchanged and is not revisited here.

## Problem

`check_output_conformance.py` verifies a produced document against its skill's
`template.md`. It identifies a section by its **text**. Because a deliverable is written in
the consuming project's language, the shipped fix gave every template heading a
language-independent HTML-comment anchor that the document must carry through
translation:

```markdown
## Market Definition <!--#market-definition-->
```

That works, and it is worse than it needs to be:

- **The anchors leak.** 816 comments now live in the templates and must survive into every
  produced document — invisible when rendered, visible in raw markdown.
- **A model that drops them defeats the check silently.** A translated document with no
  anchors matches nothing, falls under the half-threshold, and is treated as an unrelated
  file. That is the exact fail-open the design set out to close, reached by another door.
- **Repeats are enforced by exact count.** A template showing five storyboard frames makes
  a three-frame storyboard fail. Twelve templates hardcode a repeating block. This is a
  regression the anchor migration introduced: under the old text matching, five identical
  `Scene` headings all tested `"Scene" in content` and were accidentally conflated, so
  cardinality was never enforced.

The root cause is not the anchors. It is that **text was chosen as the identity key** for a
document whose text is expected to change.

## What the research established

Two research passes (`scratchpad/research-openspec.md`, `scratchpad/research-prior-art.md`):

- **Structural conformance is deterministic everywhere.** OpenSpec parses markdown into a
  heading tree and checks it with Zod schemas and regex passes; no LLM judges conformance.
  Promptfoo, Braintrust and the LLM-as-judge literature agree: structure is a program's
  job, subjective quality is a judge's. This repo's Langfuse pipeline already owns quality.
- **Identity belongs on a positional handle, not on text.** DocBook, DITA and Schematron
  all place identity on a typed or positional node with text as a *property*. `remark-lint`
  rules key on `node.type` and `node.depth` and never read heading text.
- **Cardinality is a floor, never an exact count.** OpenSpec has no rule anywhere requiring
  exactly N repeated blocks.
- **Do not build a schema DSL.** `mdschema` and `schematter` already exist, and both still
  bind identity back to heading text — there is no better wheel there to reinvent.
- **OpenSpec did not solve translated headings; it declined to.** Its `docs/multi-language.md`
  mandates English structural headings. That option was considered and rejected for this
  repo early on.

## Design

**Compare shapes, not words.** Parse the template and the produced document into ordered
structural records, align the two sequences, and report the template records that found no
partner. The document needs no markers of any kind.

### 1. The shape record

A markdown document becomes an ordered list of one record per `##`/`###` heading:

```python
Section = namedtuple("Section", "depth blocks")
# depth  : 2 or 3
# blocks : the kinds of content between this heading and the next, in order —
#          "para", "list", "table:<n-columns>", "code", "quote"
```

`## Summary` followed by a three-column table is `Section(2, ["table:3"])`. Deliberately
coarse:

- **List and paragraph counts are not recorded.** A template showing two example assumptions
  must not force a document to have exactly two.
- **Table column count is recorded.** It is stable, meaningful, and a wrong column count is a
  real defect.
- **The document's heading text is never read.** Not once. The *template's* heading text is
  read exactly twice, both times on the plugin side and never compared against the document:
  once to group repeat families (§2) and once to name a missing section in the message (§5).
  Since the template is ours and always English, that is not a language dependency.

Fence tracking lives inside the parser, so a `##` line inside a code block is not a heading
— replacing the two bolted-on fence helpers added in `9c38a2a`.

### 2. Repeat families

Consecutive same-depth template headings whose text is identical after replacing digit runs
with `N` form a **repeat family** — `Frame 1 — <Frame Title>`, `Frame 2 — <Frame Title>`.
The family's unit is the head record plus every deeper record before the next family member,
so a storyboard frame's four `###` children travel with it.

A family collapses to a single record with **`min_occurs = 1`**. Always one; no
configuration. A three-frame storyboard passes, so does a nine-frame one. The hook's job is
"did you forget a whole section", not "is this a good storyboard" — that judgment belongs to
the eval cards.

This heuristic was measured against the corpus and identified all twelve repeating templates
(`storyboard`, `positioning-ideas`, `brainstorm-ideas-existing`, `job-stories`, `retro`,
`user-segmentation`, `opportunity-solution-tree`, `user-story-mapping`, `user-story-splitting`,
`value-prop-statements`, `brainstorm-experiments-new`, `shipping-artifacts`) with no false
positives.

### 3. Alignment

Needleman–Wunsch over the two record sequences. Scoring, concretely: `+2` when depths are
equal and every block kind matches, `+1` when depths are equal and the block kinds overlap
at all, `-1` when depths differ, and `-1` for a gap. A gap is therefore always cheaper than
a depth mismatch, which is what stops one omitted section from dragging the rest of the
sequence out of register. These four numbers are pinned by a test, not tuned by feel.
Sequences are 8–30 records, so the O(n·m) table is free.

A naive index-by-index comparison is the thing to avoid: one missing section shifts every
later position and reports six failures instead of one.

Unmatched **template** records are missing sections. Unmatched **document** records are
extra sections and are **not** reported — a team adding a section to their own document is
not an error.

### 4. Is this file the deliverable?

The existing half-threshold rule, computed on shape: if fewer than half the template's
records find a partner, stay silent. "Records" means post-collapse (§2), so a repeat family
counts once however many times the template draws it — otherwise the five frames of a
storyboard would dominate the threshold for a document that has three.

**The threshold becomes reliable rather than a liability.** It was unsafe before because
translation destroyed the signal it measured — a French document matched zero English
headings and looked unrelated. Shape survives translation intact, so a translated
deliverable now scores near 100% and only genuinely different files fall below the line.

**No frontmatter marker.** `schema: <name>` in the deliverable was considered at length and
dropped: it re-introduces the leakage that shape matching removes, it is another thing a
model must remember, and it earns nothing once the threshold is reliable. If strict
identification is ever wanted, it can be added without changing anything here.

### 5. Messages

The template holds English headings, and the hook holds the template, so a missing section
is named without the document containing any marker:

```
Output does not follow the skill's template.md.
Missing: "SAM — Serviceable Addressable Market" (a level-2 section, expected between
"TAM — Total Addressable Market" and "SOM — Serviceable Obtainable Market").
Add it, or disregard if this file is not the skill's deliverable.
```

Naming the neighbours is what makes the message actionable when the heading itself will be
written in another language.

### 6. Project-owned templates

The hook prefers `<project>/.config/pm-skills/<skill>/template.md` over the plugin's, using
the same root resolution as `output_language.py` (`CLAUDE_PROJECT_DIR`, then the payload's
`cwd`, then the process cwd).

A team copies the template, translates the headings *and* the bullet labels and table
headers, drops sections they never fill in, adds ones they need. Nothing to learn: it is the
same markdown file, and there are no anchors to maintain. This also closes a gap the anchor
design never addressed — bullet labels and table column headers are English prose that was
being translated freely and differently in every document.

## What this deletes

- 816 anchors across 110 templates
- anchor mode in `check_output_conformance.py` (all six copies)
- `just anchors`, `skillkit.slugify` / `anchor_template` / `cmd_anchors`, and their 14 tests
- the linter's anchor presence and uniqueness checks, and their tests
- the two fence helpers, absorbed into the parser
- the anchors in `docs/skill-template/template.md` and its authoring guidance about them

Net: less machinery than exists today.

## Costs and risks

**A markdown block parser, stdlib-only.** Hooks run under plain `python3` on an end user's
machine, so `mistune` and `markdown-it-py` are unavailable. Headings, paragraphs, lists,
tables, fences, blockquotes — roughly 150 lines, in the spirit of the hand-rolled YAML
frontmatter parser the repo already ships. With the shape extractor and the aligner,
`check_output_conformance.py` goes from ~110 to roughly ~400 lines. It stays one file: it is
copied verbatim into five plugins and a second file doubles that overhead.

**Coarse shape is coarse.** Two adjacent sections that are both a heading plus a paragraph
are indistinguishable by shape. If a document omits one and the aligner pairs the survivor
with the wrong template record, the reported *name* may be the neighbour's. The count is
still right and the fix is still correct. Accepted: the alternative is reading text, which
is the thing being removed.

**No enforcement gap during rollout.** The anchors keep working until shape matching is
proven, and are deleted in the same branch. There is never a commit where nothing is
enforced.

## Rollout

Anchor removal is the closing commit, not the opening one.

1. `feat(tooling): markdown block parser for conformance` — parser + tests, unused.
2. `feat(tooling): shape extraction and repeat-family detection` — measured against all 110
   templates, including the 12 repeating ones.
3. `feat(tooling): sequence alignment for section matching` — aligner + tests, including the
   cascade case a naive index comparison gets wrong.
4. `feat(tooling): shape-based output conformance` — wire the above into `evaluate()` behind
   the existing anchor path, prove both agree on anchored templates, distribute to five
   plugins.
5. `feat(tooling): project-owned template override` — `.config/pm-skills/<skill>/template.md`.
6. `chore: remove section anchors` — delete the 816 anchors, `just anchors`, the linter
   checks, the fence helpers and the skeleton's anchor guidance, in one commit.
7. `docs: shape matching` — rewrite the anchor sections of `docs/output-language.md`, the
   `market-sizing` French eval card's anchor assertions, and `docs/SKILL-STANDARD.md`.

`just test` passes at every step.

## Out of scope

- A schema DSL or any new file format.
- Frontmatter markers in deliverables (see §4).
- Validating anything semantic — that a figure is cited, that an assumption has a confidence
  level. Deterministic checks stay structural; quality belongs to the eval cards.
- Cardinality ceilings, or any per-template configuration of the repeat floor.
- Changing the language-declaration half: `.config/pm-skills.yaml`, the SessionStart hook and
  its docs are untouched.

## Decisions taken without asking

Flagged for review — each is a real fork:

1. **No frontmatter marker in deliverables** (§4). Reverses a direction discussed at length,
   on the grounds that a reliable threshold makes it unnecessary and it re-adds leakage.
2. **`min_occurs = 1`, not configurable** (§2). A one-frame storyboard passes structurally.
3. **List and paragraph counts excluded from the shape** (§1) — strictness traded for not
   punishing a document that elaborates further than the template.
4. **One file, not two** (§Costs) — `check_output_conformance.py` roughly quadruples rather
   than splitting the parser out, because every file is copied into five plugins.
5. **Leftover `<placeholder>` detection is not included.** It surfaced as a cheap,
   fully language-independent check and is genuinely valuable, but it is a different feature
   from shape matching and belongs in its own change.
