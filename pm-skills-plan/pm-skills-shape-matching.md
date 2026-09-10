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
  a three-frame storyboard fail. Twenty-one templates hardcode a repeating block. This is a
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
class Section(NamedTuple):
    depth: int                  # 2 or 3
    text: str                   # heading text — template side only, never compared
    blocks: tuple[str, ...]     # content between this heading and the next, in order:
                                # "para", "list", "table:<n>", "code", "quote"
```

`## Summary` followed by a three-column table is `Section(2, "Summary", ("table:3",))`.
`text` is carried so the template side can group repeat families and name a missing section;
it is never read on the document side. Deliberately coarse:

- **List and paragraph counts are not recorded.** A template showing two example assumptions
  must not force a document to have exactly two.
- **Table column count is recorded.** It is stable and meaningful. Note what it is *for*:
  block kinds steer which document section a template record pairs with (§3) and gate whether
  the file is recognised as the deliverable at all (§4). They never make a record unmatched,
  so a wrong column count is not reported as a missing section. An earlier draft of this
  paragraph called it "a real defect", implying enforcement that does not exist.
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
so a storyboard frame's four `###` children travel with it. The comparison recurses into
each unit's children before comparing units, because repeats come in two shapes: repeated
`##` units (storyboard's frames), and `###` siblings repeating inside one `##` bucket
(retro's themes). Only the recursion sees the second.

A family collapses to a single record with **`min_occurs = 1`**. Always one; no
configuration. A three-frame storyboard passes, so does a nine-frame one. The hook's job is
"did you forget a whole section", not "is this a good storyboard" — that judgment belongs to
the eval cards.

Measured against the corpus by running the implementation over all 110 templates: **21
collapse**, and every dropped heading is plainly a second instance (`Theme 2`, `Gap 2`,
`Q2 / Phase 2`, `Priority 2`). No false positives. An earlier estimate of twelve came from a
looser heuristic that counted only headings repeated three or more times, and missed both
two-instance repeats and nested `###` siblings.

### 3. Alignment

Needleman–Wunsch over the two record sequences. Scoring, concretely: `+2` when depths are
equal and every block kind matches, `+1` when depths are equal and the block kinds overlap
at all, `0` when only the depths match, `-3` when the depths differ, and `-1` for a gap.
Pairing two mismatched records must cost more than gapping both (`-2`), or the aligner
prefers the mismatch and one omitted section drags the rest of the sequence out of register
— which is why the mismatch penalty is `-3` and not `-1`. These five numbers are pinned by
a test, not tuned by feel. Sequences are 8–30 records, so the O(n·m) table is free.

A naive index-by-index comparison is the thing to avoid: one missing section shifts every
later position and reports six failures instead of one.

Unmatched **template** records are missing sections. Unmatched **document** records are
extra sections and are **not** reported — a team adding a section to their own document is
not an error.

### 4. Is this file the deliverable?

The existing half-threshold rule, computed on shape: if fewer than half the template's
records are present, stay silent. "Records" means post-collapse (§2), so a repeat family
counts once however many times the template draws it — otherwise the five frames of a
storyboard would dominate the threshold for a document that has three.

**"Present" must mean an exact block-kind match, not merely "the aligner paired it."**
This is the correction that matters, and the original text of this section got it wrong:

> ~~The threshold becomes reliable rather than a liability. It was unsafe before because
> translation destroyed the signal it measured — a French document matched zero English
> headings and looked unrelated. Shape survives translation intact, so a translated
> deliverable now scores near 100% and only genuinely different files fall below the line.~~

That argument only examined the **false-negative** direction — will a real deliverable still
be recognised. The **false-positive** direction was never analysed, and measurement refuted
the premise. Counting any non-`None` pair recognises almost everything: two same-depth
records *always* pair, because a bare depth match scores 0 while gapping both costs −2, and
66 of the 110 templates are entirely depth-2. The threshold degenerates into "does this `.md`
file have roughly half as many `##` headings as the template". Measured over 110 templates ×
5 unrelated repo documents (550 pairs):

| criterion for "present" | recognised as the deliverable | spurious exit-2 blocks |
|---|---|---|
| any pair | 517 / 550 | 276 / 550 |
| block kinds overlap (≥ +1) | 247 / 550 | 79 / 550 |
| **block kinds identical (== +2)** | **7 / 550** | **0 / 550** |

The hook is wired `matcher: "Write|Edit"` with no path filter, so it fires on every `.md`
write while a PM skill is loaded. A false positive does not merely produce a noisy message:
exit 2 feeds it back to the model, which is then told to add "TAM — Total Addressable Market"
to the user's meeting notes. The harm is asymmetric — a false block corrupts a user's file, a
false negative leaves one deliverable unchecked — so the criterion is the exact one, and the
threshold is where the coarse block-kind data earns its keep. Against a harsh simulation of a
real deliverable (all headings translated, one block kind rewritten in 34% of sections)
recognition still holds for 91–103 of the 110 templates depending on which sections the
simulation perturbs; a document that actually follows its template is recognised 110/110.

**No frontmatter marker.** `schema: <name>` in the deliverable was considered at length and
dropped: it re-introduces the leakage that shape matching removes, and it is another thing a
model must remember. The original reasoning added "and it earns nothing once the threshold is
reliable" — that premise did not survive contact with the corpus, and the decision must not
rest on it. It stands on the two remaining reasons, plus the measurement above: with the
exact criterion the threshold is a working discriminator (0 false blocks in 550), so a marker
would buy accuracy that is already there at a cost the design set out to remove. Should the
false-negative rate ever become the binding problem — a project whose deliverables diverge
structurally enough to fall under the line — a marker is the answer, and it can be added
without changing anything here.

### 5. Messages

The template holds English headings, and the hook holds the template, so a missing section
can be located without the document containing any marker:

```
Output does not follow the skill's template.md.
A section is missing: a level-2 section between "TAM — Total Addressable Market" and
"SOM — Serviceable Obtainable Market" — probably "SAM — Serviceable Addressable Market".
The level and the neighbours are reliable; the quoted name is the template's best guess
at which section was dropped, not a certainty — check before adding one, so you do not
duplicate a section that is already there. ...
```

Naming the neighbours is what makes the message actionable when the heading itself will be
written in another language.

**The name is hedged on purpose.** Measured over 750 single-deletion trials across all 110
templates: the *count* of missing sections is right 750/750, but the section *named* is right
only 537/750 (72%). Structurally identical sections are interchangeable to a shape matcher,
so when one of a pair of lookalikes is dropped the aligner cannot tell which. Asserting the
name flatly at 72% invites the worst repair available — adding a duplicate of a section that
is already in the document. The level, the neighbours and the count are stated plainly; the
name is offered as a candidate.

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
is the thing being removed. This was accepted qualitatively and later measured — 537/750,
see §5 — which is why the message hedges the name instead of asserting it.

Coarseness has a second consequence, which the original draft of §4 missed: it makes
"the aligner paired these two" nearly meaningless as evidence, and so it constrains the
recognition threshold as well as the message. See §4.

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
