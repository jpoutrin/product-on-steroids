# Shape Matching Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Check a produced document against its skill's `template.md` by comparing structural shape rather than heading text, so a deliverable written in any language is enforced with no markers in it at all.

**Architecture:** A stdlib markdown block parser turns both files into ordered `Section(depth, text, blocks)` records. Consecutive template sections whose headings differ only by a number collapse into one, making repeats a floor of 1 instead of an exact count. Needleman–Wunsch aligns the two sequences on depth and block kinds; template records with no partner are the missing sections, named from the template's own English headings. The document's heading text is never read.

**Tech Stack:** Python 3.10+, stdlib only (hooks run under plain `python3` on an end user's machine — no `uv`, no third-party markdown library). `pytest` for tests, `uv` for the dev env, `just` as the task runner. No new dependencies.

**Spec:** `pm-skills-plan/pm-skills-shape-matching.md`

## Global Constraints

- **Stdlib only in hooks.** `scripts/skel/*.py` and every `pm-*/{scripts,hooks}/*.py` import only the standard library and run under plain `python3`. `mistune` and `markdown-it-py` are unavailable.
- **Shipped hook files must import on Python 3.9.** `pyproject.toml` says `>=3.10`, but that governs the dev env only. The hooks are wired as bare `command: python3` and run on an end user's machine — on stock macOS that is `/Library/Developer/CommandLineTools/usr/bin/python3`, currently **3.9.6**. This machine has both: `python3` is 3.14 inside the repo and 3.9.6 outside it. `X | Y` union syntax in a function signature is evaluated at import time and raises `TypeError` on 3.9, so **every shipped hook file starts with `from __future__ import annotations`**, which makes all annotations lazy and works from 3.7. The two files shipped today already import cleanly on 3.9.6; keep it that way.
- **Fail open.** Any unexpected condition returns exit 0 and emits nothing. The hook must never block an edit.
- **Copies stay byte-identical.** `scripts/skel/<file>` is canonical; each of the five plugins (`pm-strategy`, `pm-discovery`, `pm-gtm`, `pm-execution`, `pm-influence`) carries a copy. `tests/test_hook_copies_identical.py` is the guard. Copy with `/bin/cp`, verify with `cmp`.
- **The document's heading text is never read.** The template's heading text is read only to group repeat families and to name a missing section in the message — both plugin-side, never compared against the document.
- **Repeat cardinality is a floor of 1**, never an exact count, and is not configurable.
- **Alignment scores are fixed:** `+2` same depth and identical block kinds, `+1` same depth with overlapping block kinds, `0` same depth with no overlap, `-3` differing depth, `-1` per gap. A depth mismatch (`-3`) must stay worse than gapping both records (`-2`) so one omitted section cannot drag the rest of the sequence out of register.
- **Anchor removal is the closing commit.** Anchors keep working until shape matching is proven; there is never a commit where nothing is enforced.
- **Commit messages** end with `Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e`.
- **Every commit is green:** `just test` passes (pytest, then the linter).

## Deviations from the spec (deliberate, read before starting)

1. **Two files, not one.** The spec's decision #4 kept everything in `check_output_conformance.py` because each file is copied into five plugins. This plan splits the pure logic into `scripts/skel/md_shape.py` (parse, collapse, align — no I/O) and leaves `check_output_conformance.py` as hook plumbing. The pure half becomes trivially testable, and the copy cost is one more entry in a `COPIES` dict that already exists. Python puts a script's own directory on `sys.path[0]`, so `import md_shape` works with no path manipulation.
2. **Alignment scores corrected.** The spec said depth mismatch and gap are both `-1`, and concluded "a gap is therefore always cheaper than a depth mismatch". That is wrong: in Needleman–Wunsch, aligning two mismatched records costs `-1` once, while gapping both costs `-1` twice, so the mismatch is *cheaper* and the stated property does not hold. This plan uses `-3` for a depth mismatch, which makes gaps genuinely cheaper. The spec has been corrected to match.

## Environment traps (each has cost an implementer time on this machine)

- `cp` → `nocorrect cp -i`: a bare `cp` over an existing file prompts and **silently declines** in a non-interactive shell. Use `/bin/cp`.
- `rm` → an interactive form that **hangs** a non-interactive shell. Use `/bin/rm -f`.
- `grep`, `ls`, `md5` are wrapped by a token-compacting proxy that truncates and reformats. Where exact output matters use `python3`, `diff`, `cmp`, or `git`.
- Use `uv run pytest`, never bare `pytest`.
- BSD `sed` on macOS has no GNU `0,/re/` address form.

## File Structure

**New, canonical:**
- `scripts/skel/md_shape.py` — the whole pure layer: `Section`, `parse_sections`, `collapse_repeats`, `align`. No file I/O, no stdin, no exit codes.

**Modified, canonical:**
- `scripts/skel/check_output_conformance.py` — hook plumbing only: stdin, template resolution (including the project override), calling `md_shape`, rendering the message.

**Per-plugin copies (5×, byte-identical):**
- `pm-<plugin>/scripts/md_shape.py` *(new)*
- `pm-<plugin>/scripts/check_output_conformance.py` *(modified)*

**Removed in Task 6:**
- 816 anchors across 110 `pm-*/skills/*/template.md`
- `scripts/skillkit.py`: `_HEADING_LINE`, `_ANCHOR`, `_FENCE_LINE`, `_fence_mask`, `slugify`, `anchor_template`, `cmd_anchors`, its `COMMANDS` entry
- `tests/validate_plugins.py`: `_FENCE_LINE`, `strip_fenced_blocks`, the anchor presence and uniqueness checks
- `tests/test_skillkit_anchors.py` (whole file), the anchor cases in `tests/test_template_check.py`
- the `anchors` recipe in `justfile`, the anchors and their guidance in `docs/skill-template/template.md`

**Docs, Task 7:**
- `docs/output-language.md`, `docs/SKILL-STANDARD.md`, and the three `market-sizing` eval cards that assert anchors survive.

---

## Task 1: Markdown block parser

**Files:**
- Create: `scripts/skel/md_shape.py`
- Test: `tests/test_md_shape.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `md_shape.Section` — `NamedTuple(depth: int, text: str, blocks: tuple[str, ...])`
  - `md_shape.parse_sections(md: str) -> list[Section]` — one record per `##`/`###` heading, in document order. `blocks` holds the kinds of content between this heading and the next, consecutive duplicates collapsed: `"para"`, `"list"`, `"quote"`, `"code"`, `"table:<n>"` where `<n>` is the column count.

Background: templates across the corpus contain 926 headings, 1152 unordered-list lines, 932 paragraph lines, 782 table rows, 292 ordered-list lines, 49 blockquote lines and 16 fence lines, so every one of those kinds is real and must parse. HTML comments (153 lines) are authoring guidance and must be skipped, not treated as content.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_md_shape.py`:

```python
"""Tests for the pure shape layer used by the output-conformance hook."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "md_shape", ROOT / "scripts" / "skel" / "md_shape.py")
ms = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ms)


def test_headings_become_sections_in_order():
    md = "# Title\n## A\ntext\n## B\nmore\n"
    assert [(s.depth, s.text) for s in ms.parse_sections(md)] == [(2, "A"), (2, "B")]


def test_h1_and_h4_are_not_sections():
    md = "# Title\n## A\n#### Deep\n### B\n"
    assert [(s.depth, s.text) for s in ms.parse_sections(md)] == [(2, "A"), (3, "B")]


def test_preamble_before_first_heading_is_dropped():
    md = "# Title\n**Persona:** someone\n\n## A\ntext\n"
    out = ms.parse_sections(md)
    assert len(out) == 1 and out[0].blocks == ("para",)


def test_block_kinds_are_detected():
    md = ("## A\npara text\n- bullet\n1. numbered\n> quote\n")
    # consecutive list kinds collapse into one "list"
    assert ms.parse_sections(md)[0].blocks == ("para", "list", "quote")


def test_consecutive_same_kind_collapses():
    md = "## A\nline one\nline two\nline three\n"
    assert ms.parse_sections(md)[0].blocks == ("para",)


def test_table_records_its_column_count():
    md = ("## Summary\n"
          "| Metric | Current | Projection |\n"
          "|--------|---------|------------|\n"
          "| TAM    | <...>   | <...>      |\n")
    assert ms.parse_sections(md)[0].blocks == ("table:3",)


def test_table_without_trailing_pipe_counts_the_same():
    md = "## S\n| A | B | C\n"
    assert ms.parse_sections(md)[0].blocks == ("table:3",)


def test_fenced_code_is_one_code_block_and_hides_headings():
    md = "## A\n```\n## not a heading\n```\ntail\n"
    out = ms.parse_sections(md)
    assert len(out) == 1
    assert out[0].blocks == ("code", "para")


def test_tilde_fence_is_handled():
    md = "## A\n~~~\n## not a heading\n~~~\n"
    assert len(ms.parse_sections(md)) == 1


def test_unterminated_fence_is_not_a_fence():
    # A malformed template must not swallow the rest of the file: over-report
    # headings rather than silently exempt them.
    md = "## A\n```\n## Real B\n"
    assert [s.text for s in ms.parse_sections(md)] == ["A", "Real B"]


def test_html_comments_are_skipped():
    md = "## A\n<!-- guidance for the author -->\npara\n"
    assert ms.parse_sections(md)[0].blocks == ("para",)


def test_multiline_html_comment_is_skipped():
    md = "## A\n<!--\nline one\nline two\n-->\npara\n"
    assert ms.parse_sections(md)[0].blocks == ("para",)


def test_blank_lines_produce_no_blocks():
    assert ms.parse_sections("## A\n\n\n") == [ms.Section(2, "A", ())]


def test_real_template_parses(tmp_path):
    md = (ROOT / "pm-strategy" / "skills" / "market-sizing" / "template.md"
          ).read_text(encoding="utf-8")
    out = ms.parse_sections(md)
    assert len(out) == 8
    assert out[0].depth == 2
    assert any(b.startswith("table:") for s in out for b in s.blocks)
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_md_shape.py -q`
Expected: FAIL at collection — `FileNotFoundError` for `scripts/skel/md_shape.py`.

- [ ] **Step 3: Write the parser**

Create `scripts/skel/md_shape.py`:

```python
#!/usr/bin/env python3
"""Structural shape of a markdown document — the pure layer behind the
output-conformance hook.

A produced deliverable is written in the consuming project's language, so its
heading text cannot be matched against an English template. What survives
translation is the document's *shape*: how many sections, at what depth, in what
order, holding what kinds of content. This module extracts that shape and aligns
two of them. It never reads a document's heading text.

Distributed inside each plugin as `<plugin>/scripts/md_shape.py`, next to
`check_output_conformance.py`, which imports it as a sibling (Python puts a
script's own directory on sys.path[0]).

No I/O, no exit codes, no stdin — those live in the hook. Stdlib only, plain
`python3` (no uv) so it runs on an end user's machine — which on stock macOS is
still Python 3.9, hence the `__future__` import: without it the `int | None` in
`align`'s signature is evaluated at import time and raises there.
"""
from __future__ import annotations

import re
from typing import NamedTuple


class Section(NamedTuple):
    depth: int                  # 2 or 3
    text: str                   # heading text; used only on the template side
    blocks: tuple[str, ...]     # "para" | "list" | "quote" | "code" | "table:<n>"


_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_INLINE_COMMENT = re.compile(r"<!--.*?-->")
_FENCE = re.compile(r"^(```+|~~~+)")
_TABLE = re.compile(r"^\s*\|")
_ULIST = re.compile(r"^\s*[-*+]\s")
_OLIST = re.compile(r"^\s*\d+[.)]\s")
_QUOTE = re.compile(r"^\s*>")


def _fence_mask(lines: list[str]) -> list[bool]:
    """`True` for every line inside — or delimiting — a ``` / ~~~ fenced block.

    A `## heading` inside a code example is illustrative content, not a section.
    Info strings (```mermaid) are handled; indented fences and nested fences of
    differing lengths are not (deliberately out of scope).

    A fence that never closes before end of file is not a fence — it is a
    malformed document. The region from its opening delimiter onward is
    reclassified as ordinary prose, so headings in it are still seen. The safe
    failure direction is to over-report headings, never to silently exempt them.
    """
    mask: list[bool] = []
    fence: str | None = None
    fence_start: int | None = None
    for i, line in enumerate(lines):
        m = _FENCE.match(line)
        if m:
            tok = m.group(1)[0]
            if fence is None:
                fence, fence_start = tok, i
            elif fence == tok:
                fence, fence_start = None, None
            mask.append(True)
            continue
        mask.append(fence is not None)
    if fence is not None:
        for i in range(fence_start, len(lines)):
            mask[i] = False
    return mask


def _table_columns(line: str) -> int:
    """Column count of a pipe-table row, tolerant of a missing trailing pipe."""
    return len(line.strip().strip("|").split("|"))


def _kind(line: str) -> str:
    if _TABLE.match(line):
        return "table:%d" % _table_columns(line)
    if _ULIST.match(line) or _OLIST.match(line):
        return "list"
    if _QUOTE.match(line):
        return "quote"
    return "para"


def parse_sections(md: str) -> list[Section]:
    """One `Section` per `##`/`###` heading, in document order.

    Level-3 is included so templates that group sections under `##` buckets with
    the real sections as `###` (e.g. a 9-block canvas) are seen fully. Level-1 is
    the document title and levels 4+ are sub-structure; neither starts a section.
    Content before the first `##` is preamble and is dropped.
    """
    lines = md.split("\n")
    fenced = _fence_mask(lines)
    out: list[Section] = []
    depth: int | None = None
    text = ""
    blocks: list[str] = []
    in_comment = False

    def add(kind: str) -> None:
        if not blocks or blocks[-1] != kind:
            blocks.append(kind)

    for i, line in enumerate(lines):
        if fenced[i]:
            if depth is not None:
                add("code")
            continue
        s = line.strip()
        if in_comment:
            in_comment = "-->" not in s
            continue
        if s.startswith("<!--"):
            in_comment = "-->" not in s
            continue
        if not s:
            continue
        m = _HEADING.match(s)
        if m:
            d = len(m.group(1))
            if 2 <= d <= 3:
                if depth is not None:
                    out.append(Section(depth, text, tuple(blocks)))
                # An inline HTML comment on a heading line is a marker, not part
                # of the name. Stripping it keeps error messages clean while the
                # old anchors are still present (they go in Task 6).
                depth = d
                text = _INLINE_COMMENT.sub("", m.group(2)).strip()
                blocks = []
            continue
        if depth is None:
            continue
        add(_kind(s))

    if depth is not None:
        out.append(Section(depth, text, tuple(blocks)))
    return out
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_md_shape.py -q`
Expected: PASS (14 cases).

- [ ] **Step 5: Sanity-check the parser across the whole corpus**

```bash
uv run python -c "
import importlib.util, glob, pathlib
s = importlib.util.spec_from_file_location('m','scripts/skel/md_shape.py')
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
tot = 0
for f in sorted(glob.glob('pm-*/skills/*/template.md')):
    secs = m.parse_sections(pathlib.Path(f).read_text(encoding='utf-8'))
    assert secs, f
    tot += len(secs)
print('parsed 110 templates,', tot, 'sections')
"
```

Expected: `parsed 110 templates, 816 sections`. That number must equal the 816 anchors currently in the corpus — the parser sees exactly the headings the anchor migration saw. **If it differs, stop and report**: it means the parser disagrees with the shipped `parse_headings` about what a heading is.

- [ ] **Step 6: Verify it imports on Python 3.9**

The hook runs under whatever bare `python3` the end user has. On stock macOS that is 3.9.6, which rejects `X | Y` in a signature at import time.

```bash
/Library/Developer/CommandLineTools/usr/bin/python3 -c "
import importlib.util, sys
print('interpreter:', sys.version.split()[0])
s = importlib.util.spec_from_file_location('m','scripts/skel/md_shape.py')
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
print('md_shape imports OK on', sys.version.split()[0])
"
```

Expected: `md_shape imports OK on 3.9.6`. If that path does not exist on your machine, run the same check under the oldest `python3` you have and say which version in your report. A `TypeError: unsupported operand type(s) for |` means the `from __future__ import annotations` line is missing.

- [ ] **Step 7: Commit**

```bash
git add scripts/skel/md_shape.py tests/test_md_shape.py
git commit -F - <<'EOF'
feat(tooling): markdown block parser for conformance

Turns a markdown document into ordered Section(depth, text, blocks) records —
the shape that survives translation when heading text does not. Handles
paragraphs, lists, tables (with column counts), blockquotes, fenced code and
HTML comments, and treats an unterminated fence as prose rather than letting it
swallow the rest of the file.

Pure and unused so far; the hook is wired to it in a later commit.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 2: Repeat-family collapse

**Files:**
- Modify: `scripts/skel/md_shape.py`
- Modify: `tests/test_md_shape.py`

**Interfaces:**
- Consumes: `md_shape.Section`, `md_shape.parse_sections` from Task 1.
- Produces: `md_shape.collapse_repeats(sections: list[Section]) -> list[Section]` — the same list with the 2nd and later members of each repeat family removed, including their nested children.

Background: twelve templates draw a repeating block a fixed number of times — `storyboard` (5 frames, each with 4 `###` children), `positioning-ideas` (5 concepts), `brainstorm-ideas-existing` (5), `job-stories` (4), `retro` (3), `user-segmentation` (3), `opportunity-solution-tree` (3), `user-story-mapping` (3), `user-story-splitting` (3), `value-prop-statements` (3), `brainstorm-experiments-new` (3), `shipping-artifacts` (4). Matching those by exact count is why a three-frame storyboard currently fails. Collapsing each family to its first member makes the requirement "at least one", because unmatched *document* sections are never reported.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_md_shape.py`:

```python
def test_collapse_keeps_a_non_repeating_template_intact():
    secs = ms.parse_sections("## A\n## B\n## C\n")
    assert ms.collapse_repeats(secs) == secs


def test_collapse_reduces_a_numbered_family_to_one():
    md = "## Frame 1 — <Title>\n## Frame 2 — <Title>\n## Frame 3 — <Title>\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [s.text for s in out] == ["Frame 1 — <Title>"]


def test_collapse_carries_nested_children_with_the_family_head():
    md = ("## Frame 1 — <T>\n### Scene\n### Action\n"
          "## Frame 2 — <T>\n### Scene\n### Action\n"
          "## Takeaways\n")
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [(s.depth, s.text) for s in out] == [
        (2, "Frame 1 — <T>"), (3, "Scene"), (3, "Action"), (2, "Takeaways")]


def test_collapse_needs_three_in_a_row_is_false_two_is_enough():
    md = "## Segment 1: <Name>\n## Segment 2: <Name>\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [s.text for s in out] == ["Segment 1: <Name>"]


def test_collapse_ignores_headings_that_differ_by_more_than_digits():
    md = "## Frame 1 — <T>\n## Summary\n## Frame 2 — <T>\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert len(out) == 3


def test_collapse_requires_matching_child_shape():
    # Same normalised head, but the second unit has a different child depth
    # sequence — not a repeat of the first.
    md = "## Step 1\n### Detail\n## Step 2\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [s.text for s in out] == ["Step 1", "Detail", "Step 2"]


def test_collapse_reaches_repeats_nested_inside_a_unit():
    # The second repeat shape: one `##` bucket whose `###` children repeat.
    # Only the recursion inside collapse_repeats sees these.
    md = "## Themes\n### <Theme 1>\n- a\n### <Theme 2>\n- a\n### <Theme 3>\n- a\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [(s.depth, s.text) for s in out] == [(2, "Themes"), (3, "<Theme 1>")]


def test_collapse_strips_an_inline_anchor_from_the_heading_name():
    # Anchors still exist until Task 6; they must not leak into a section's name.
    md = "## Priority 1: <Theme> <!--#priority-1-theme-->\n- a\n"
    assert ms.parse_sections(md)[0].text == "Priority 1: <Theme>"


def test_collapse_on_the_real_storyboard_template():
    md = (ROOT / "pm-discovery" / "skills" / "storyboard" / "template.md"
          ).read_text(encoding="utf-8")
    full = ms.parse_sections(md)
    out = ms.collapse_repeats(full)
    # 5 frames × (1 head + 4 children) + 1 takeaways = 26 -> 1 frame unit + takeaways
    assert len(full) == 26
    assert len(out) == 6
    assert [s.depth for s in out] == [2, 3, 3, 3, 3, 2]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_md_shape.py -q`
Expected: FAIL with `AttributeError: module 'md_shape' has no attribute 'collapse_repeats'`.

- [ ] **Step 3: Implement the collapse**

Append to `scripts/skel/md_shape.py`:

```python
_DIGITS = re.compile(r"\d+")


def _units(sections: list[Section]) -> list[list[Section]]:
    """Group sections into units: each head plus every deeper section after it."""
    units: list[list[Section]] = []
    for s in sections:
        if not units or s.depth <= units[-1][0].depth:
            units.append([s])
        else:
            units[-1].append(s)
    return units


def _signature(unit: list[Section]) -> tuple:
    """What makes two units the same repeated thing: the head's text with digit
    runs normalised away, plus the depth sequence of its children."""
    return (_DIGITS.sub("N", unit[0].text), tuple(s.depth for s in unit[1:]))


def collapse_repeats(sections: list[Section]) -> list[Section]:
    """Drop the 2nd and later members of each repeat family, at every depth.

    A template draws a repeated block a fixed number of times — five storyboard
    frames, three retro themes — but a real document has as many as it needs.
    Consecutive units whose headings differ only by a number, and whose children
    have the same depth sequence, are one requirement, not N.

    Repeats come in two shapes and both must be caught:

      ## Frame 1        <- repeated units, deduped at this level
      ### Scene
      ## Frame 2
      ### Scene

      ## Themes         <- one unit whose CHILDREN repeat; only the recursion
      ### <Theme 1>        below sees these
      ### <Theme 2>

    Hence recursing into each unit's children before comparing units: seven
    templates in the corpus are the second shape and would otherwise keep
    enforcing an exact count.

    Collapsing to the first member makes the floor 1 and imposes no ceiling,
    because unmatched *document* sections are never reported as errors. This
    mirrors OpenSpec, whose cardinality rules are always `>= 1` and never exact.
    """
    units = [[u[0]] + collapse_repeats(u[1:]) for u in _units(sections)]
    out: list[Section] = []
    prev_sig = None
    for unit in units:
        sig = _signature(unit)
        if sig == prev_sig:
            continue          # a further member of the family already emitted
        out.extend(unit)
        prev_sig = sig
    return out
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_md_shape.py -q`
Expected: PASS (23 cases).

- [ ] **Step 5: Verify the collapse against the whole corpus**

```bash
uv run python -c "
import importlib.util, glob, pathlib
s = importlib.util.spec_from_file_location('m','scripts/skel/md_shape.py')
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
n = 0
for f in sorted(glob.glob('pm-*/skills/*/template.md')):
    secs = m.parse_sections(pathlib.Path(f).read_text(encoding='utf-8'))
    col = m.collapse_repeats(secs)
    if len(col) != len(secs):
        n += 1
        print('%-42s %3d -> %3d' % (f.split('/')[-2], len(secs), len(col)))
print(n, 'templates collapsed')
"
```

Expected: **21 templates collapsed**, and `storyboard` shows `26 -> 6`. Some are units repeating at their own level (storyboard's frames, positioning-ideas' concepts); the rest are `###` siblings repeating inside a single `##` bucket (retro's themes, user-segmentation's segments) and are caught only by the recursion. Spot-check what a few of them dropped — every dropped heading should be an obvious second instance (`Theme 2`, `Gap 2`, `Q2 / Phase 2`). If a template you did not expect appears, or a dropped heading is not plainly a repeat, stop and report: over-collapsing silently weakens enforcement.

Note when writing your own diagnostics: compare by **index**, not with `section not in kept`. Two repeated sections can be byte-identical once their anchor is stripped (`stakeholder-engagement-advisor` is), and `NamedTuple` equality then makes a membership test claim nothing was dropped.

- [ ] **Step 6: Commit**

```bash
git add scripts/skel/md_shape.py tests/test_md_shape.py
git commit -F - <<'EOF'
feat(tooling): shape extraction and repeat-family detection

Consecutive template units whose headings differ only by a number, with
matching child depth sequences, collapse to a single requirement. Cardinality
becomes a floor of one rather than the template's exact count, so a three-frame
storyboard stops being flagged against a five-frame template.

Recursing into each unit's children before comparing units catches both repeat
shapes: repeated `##` units, and `###` siblings repeating inside one `##`
bucket. Measured across the corpus: 21 templates collapse, storyboard from 26
sections to 6.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 3: Sequence alignment

**Files:**
- Modify: `scripts/skel/md_shape.py`
- Modify: `tests/test_md_shape.py`

**Interfaces:**
- Consumes: `md_shape.Section` from Task 1.
- Produces: `md_shape.align(want: list[Section], got: list[Section]) -> list[int | None]` — one entry per `want` index: the matched `got` index, or `None` when that requirement found no partner.

Background: a naive index-by-index comparison is the thing to avoid. If a document omits its third section, every later section shifts by one and a positional comparison reports six failures instead of one. Needleman–Wunsch finds the alignment maximising total score, so one omission costs one gap.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_md_shape.py`:

```python
def S(depth, text="x", blocks=()):
    return ms.Section(depth, text, blocks)


def test_align_identical_sequences_matches_pairwise():
    want = [S(2, "A"), S(2, "B"), S(2, "C")]
    assert ms.align(want, list(want)) == [0, 1, 2]


def test_align_ignores_heading_text_entirely():
    want = [S(2, "Market Definition"), S(2, "TAM")]
    got = [S(2, "Définition du marché"), S(2, "Marché total")]
    assert ms.align(want, got) == [0, 1]


def test_align_reports_one_gap_not_a_cascade():
    # The document dropped the middle section. Exactly one requirement is
    # unmatched; the rest must not shift out of register. Block kinds differ per
    # section so there is exactly one best alignment.
    want = [S(2, "A", ("para",)), S(2, "B", ("list",)),
            S(2, "C", ("table:2",)), S(2, "D", ("quote",))]
    got = [S(2, "a", ("para",)), S(2, "c", ("table:2",)), S(2, "d", ("quote",))]
    assert ms.align(want, got) == [0, None, 1, 2]


def test_align_tolerates_extra_document_sections():
    want = [S(2, "A", ("para",)), S(2, "B", ("list",))]
    got = [S(2, "a", ("para",)), S(2, "extra", ("quote",)), S(2, "b", ("list",))]
    assert ms.align(want, got) == [0, 2]


def test_align_prefers_gaps_over_a_depth_mismatch():
    # Pairing a level-2 requirement with a level-3 section scores -3; gapping
    # both scores -2, so the aligner must choose the gaps.
    want = [S(2, "A")]
    got = [S(3, "b")]
    assert ms.align(want, got) == [None]


def test_align_uses_block_kinds_to_pick_the_right_partner():
    # Two same-depth candidates; the block kinds decide which one the
    # requirement pairs with, so the unrelated section is skipped rather than
    # mismatched. Matching got[1] scores +2 at the cost of one gap (+1 net);
    # matching got[0] scores 0 and then gaps (-1).
    want = [S(2, "Summary", ("table:3",))]
    got = [S(2, "intro", ("para",)), S(2, "tableau", ("table:3",))]
    assert ms.align(want, got) == [1]


def test_align_empty_document_matches_nothing():
    assert ms.align([S(2, "A"), S(2, "B")], []) == [None, None]


def test_align_empty_template_returns_empty():
    assert ms.align([], [S(2, "a")]) == []


def test_align_nested_depths_stay_paired():
    want = [S(2, "A"), S(3, "a1"), S(3, "a2"), S(2, "B")]
    got = [S(2, "x"), S(3, "x1"), S(3, "x2"), S(2, "y")]
    assert ms.align(want, got) == [0, 1, 2, 3]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_md_shape.py -q`
Expected: FAIL with `AttributeError: module 'md_shape' has no attribute 'align'`.

- [ ] **Step 3: Implement the aligner**

Append to `scripts/skel/md_shape.py`:

```python
# Alignment scores. A depth mismatch (-3) must stay worse than gapping both
# records (-1 twice), or one omitted section drags the whole tail of the
# sequence out of register — the failure a naive positional comparison makes.
_SCORE_EXACT = 2       # same depth, identical block kinds
_SCORE_OVERLAP = 1     # same depth, block kinds intersect
_SCORE_DEPTH_ONLY = 0  # same depth, nothing else in common
_SCORE_MISMATCH = -3   # different depth
_SCORE_GAP = -1


def _similarity(a: Section, b: Section) -> int:
    if a.depth != b.depth:
        return _SCORE_MISMATCH
    if a.blocks == b.blocks:
        return _SCORE_EXACT
    if set(a.blocks) & set(b.blocks):
        return _SCORE_OVERLAP
    return _SCORE_DEPTH_ONLY


def align(want: list[Section], got: list[Section]) -> list[int | None]:
    """Needleman–Wunsch. For each `want` index, the `got` index it matched, or
    `None` when nothing partnered it.

    Heading text is never consulted: only depth and block kinds. That is what
    makes a translated document align with its English template.

    Sequences are 8–30 records, so the O(n·m) table costs nothing.
    """
    n, m = len(want), len(got)
    # score[i][j] = best score aligning want[i:] with got[j:]
    score = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        score[i][m] = score[i + 1][m] + _SCORE_GAP
    for j in range(m - 1, -1, -1):
        score[n][j] = score[n][j + 1] + _SCORE_GAP
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            score[i][j] = max(
                _similarity(want[i], got[j]) + score[i + 1][j + 1],
                _SCORE_GAP + score[i + 1][j],      # skip a requirement
                _SCORE_GAP + score[i][j + 1],      # skip a document section
            )

    out: list[int | None] = []
    i = j = 0
    while i < n:
        if j >= m:
            out.append(None)
            i += 1
            continue
        pair = _similarity(want[i], got[j]) + score[i + 1][j + 1]
        skip_want = _SCORE_GAP + score[i + 1][j]
        skip_got = _SCORE_GAP + score[i][j + 1]
        best = max(pair, skip_want, skip_got)
        if best == pair:
            out.append(j)
            i += 1
            j += 1
        elif best == skip_want:
            out.append(None)
            i += 1
        else:
            j += 1
    return out
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_md_shape.py -q`
Expected: PASS (30 cases).

- [ ] **Step 5: Prove the whole pipeline on a translated document**

```bash
uv run python -c "
import importlib.util, pathlib, re
s = importlib.util.spec_from_file_location('m','scripts/skel/md_shape.py')
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
t = pathlib.Path('pm-strategy/skills/market-sizing/template.md').read_text(encoding='utf-8')
want = m.collapse_repeats(m.parse_sections(t))
# Same document with every heading replaced by French, and anchors stripped.
fr = re.sub(r'(?m)^(#{2,3})\s+.*$', r'\1 Section en français', t)
fr = re.sub(r'\s*<!--#[a-z0-9-]+-->', '', fr)
got = m.parse_sections(fr)
print('template sections:', len(want), ' french doc sections:', len(got))
print('alignment:', m.align(want, got))
"
```

Expected: both counts are 8 and the alignment is `[0, 1, 2, 3, 4, 5, 6, 7]` — a fully translated document with **no anchors at all** matches its English template perfectly. That is the whole point of the change; if it does not hold, stop and report.

- [ ] **Step 6: Commit**

```bash
git add scripts/skel/md_shape.py tests/test_md_shape.py
git commit -F - <<'EOF'
feat(tooling): sequence alignment for section matching

Needleman-Wunsch over two shape sequences, scoring on depth and block kinds and
never on heading text. A depth mismatch scores worse than gapping both records,
so one omitted section costs one gap instead of shifting every later section out
of register the way a positional comparison does.

A fully translated market-sizing memo carrying no anchors now aligns 8-for-8
against the English template.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 4: Shape-based conformance in the hook

**Files:**
- Modify: `scripts/skel/check_output_conformance.py`
- Modify: `tests/test_check_conformance.py`
- Modify: `tests/test_hook_copies_identical.py` (add `md_shape.py` to `COPIES`)
- Create/copy: `pm-{strategy,discovery,gtm,execution,influence}/scripts/md_shape.py`
- Modify: `pm-{strategy,discovery,gtm,execution,influence}/scripts/check_output_conformance.py`

**Interfaces:**
- Consumes: `md_shape.Section`, `parse_sections`, `collapse_repeats`, `align`.
- Produces: `check_output_conformance.evaluate(payload: dict, template_path: str) -> tuple[int, str]` — unchanged signature, new behaviour. `ANCHOR_RE`, `parse_headings` and `headings` are removed.

The hook keeps its half-threshold rule, now computed on shape. That rule was unsafe before because translation destroyed the signal it measured; shape survives translation, so a translated deliverable scores near 100% and only genuinely different files fall below the line.

- [ ] **Step 1: Rewrite the hook's tests**

Replace the entire contents of `tests/test_check_conformance.py` with:

```python
"""Tests for the skill-scoped output-conformance hook checker."""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "skel"))   # so the hook finds md_shape
_spec = importlib.util.spec_from_file_location(
    "check_output_conformance", ROOT / "scripts" / "skel" / "check_output_conformance.py")
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)

# Each section has a DIFFERENT block kind, so alignment has exactly one best
# answer and a test can assert which section was reported missing. Four sections
# that all held a bullet list would be interchangeable to a shape matcher — see
# the "coarse shape is coarse" risk in the spec.
TEMPLATE = ("# T\n"
            "## Market Definition\n- a\n"
            "## TAM\nprose\n"
            "## SAM\n| A | B |\n|---|---|\n"
            "## SOM\n> q\n")


def _payload(file_path, tool="Write"):
    return {"tool_name": tool, "tool_input": {"file_path": file_path}}


def _write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return str(p)


def _tmpl(tmp_path):
    return _write(tmp_path, "template.md", TEMPLATE)


def test_conformant_artifact_is_silent(tmp_path):
    art = _write(tmp_path, "memo.md",
                 "## Market Definition\n- a\n## TAM\nprose\n"
                 "## SAM\n| A | B |\n|---|---|\n## SOM\n> q\n")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_french_artifact_with_no_markers_is_silent(tmp_path):
    # The whole point: same shape, entirely different words, nothing to preserve.
    art = _write(tmp_path, "memo.md",
                 "## Définition du marché\n- a\n## Marché total\nprose\n"
                 "## Marché adressable\n| A | B |\n|---|---|\n"
                 "## Marché obtenable\n> q\n")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_missing_section_is_flagged_and_named_from_the_template(tmp_path):
    # The table section is gone; the other three still align by block kind.
    art = _write(tmp_path, "memo.md",
                 "## Définition du marché\n- a\n## Marché total\nprose\n"
                 "## Marché obtenable\n> q\n")
    code, msg = checker.evaluate(_payload(art), _tmpl(tmp_path))
    assert code == 2
    assert "SAM" in msg               # named in English, from the template
    assert "TAM" in msg               # its neighbour, to locate it
    assert "SOM" in msg               # its other neighbour


def test_unrelated_file_stays_silent(tmp_path):
    art = _write(tmp_path, "notes.md", "# Random notes\nnothing structured here\n")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_non_markdown_file_ignored(tmp_path):
    art = _write(tmp_path, "code.py", "print('hi')")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_non_write_tool_ignored(tmp_path):
    art = _write(tmp_path, "memo.md", TEMPLATE)
    assert checker.evaluate(_payload(art, tool="Read"), _tmpl(tmp_path)) == (0, "")


def test_missing_template_is_silent(tmp_path):
    art = _write(tmp_path, "memo.md", TEMPLATE)
    assert checker.evaluate(_payload(art), str(tmp_path / "nope.md")) == (0, "")


def test_repeating_template_accepts_fewer_instances(tmp_path):
    # The regression this change exists to kill: a 5-frame template must not
    # force a 3-frame document.
    tmpl = _write(tmp_path, "template.md",
                  "".join(f"## Frame {i} — <T>\n### Scene\n- s\n### Action\n- a\n"
                          for i in range(1, 6)) + "## Takeaways\n- t\n")
    art = _write(tmp_path, "story.md",
                 "".join(f"## Scène {i}\n### Décor\n- s\n### Action\n- a\n"
                         for i in range(1, 4)) + "## Conclusions\n- t\n")
    assert checker.evaluate(_payload(art), tmpl) == (0, "")


def test_repeating_template_still_requires_one_instance(tmp_path):
    tmpl = _write(tmp_path, "template.md",
                  "".join(f"## Frame {i} — <T>\n### Scene\n- s\n### Action\n- a\n"
                          for i in range(1, 6)) + "## Takeaways\n- t\n")
    art = _write(tmp_path, "story.md", "## Conclusions\n- t\n")
    # Only 1 of 4 collapsed requirements matches -> below half -> not the deliverable.
    assert checker.evaluate(_payload(art), tmpl) == (0, "")


def test_grouped_canvas_missing_level3_is_flagged(tmp_path):
    tmpl = _write(tmp_path, "template.md",
                  "## Create Value\n- x\n### Key Partnerships\n- p\n### Key Activities\n- a\n")
    art = _write(tmp_path, "canvas.md",
                 "## Créer de la valeur\n- x\n### Partenariats\n- p\n")
    code, msg = checker.evaluate(_payload(art), tmpl)
    assert code == 2 and "Key Activities" in msg


def test_extra_document_sections_are_not_errors(tmp_path):
    art = _write(tmp_path, "memo.md",
                 "## Market Definition\n- a\n## Bonus\n- z\n## TAM\nprose\n"
                 "## SAM\n| A | B |\n|---|---|\n## SOM\n> q\n")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_check_conformance.py -q`
Expected: FAIL — the anchor-based `evaluate` flags the French documents and passes the three-frame storyboard test for the wrong reason.

- [ ] **Step 3: Rewrite the hook**

Replace `scripts/skel/check_output_conformance.py` entirely with:

```python
#!/usr/bin/env python3
"""Skill-scoped PostToolUse hook — verify a written artifact follows the skill's template.

Distributed inside each plugin as `<plugin>/scripts/check_output_conformance.py`,
alongside `md_shape.py`, and wired from a skill's frontmatter:

    hooks:
      PostToolUse:
        - matcher: "Write|Edit"
          hooks:
            - type: command
              command: python3
              args:
                - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
                - ${CLAUDE_PLUGIN_ROOT}/skills/<skill>/template.md

The argument is THIS skill's own template.md, so each skill validates against its
own structure. Reads the PostToolUse JSON on stdin, compares the written file's
*shape* against the template's — heading depth, block kinds, table column counts,
never heading text — and if the file looks like the skill's deliverable (matches
at least half the template's sections) but is missing some, exits 2. The stderr
message is fed back to Claude so it revises the file.

Because shape survives translation, a deliverable written in the project's own
language is recognised and enforced with no markers in it at all.

Fail-open everywhere: any unexpected condition returns 0 so authoring is never
blocked. Stdlib only, plain `python3` (no uv) so it runs on an end user's machine
— which on stock macOS is still Python 3.9, hence the `__future__` import.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import md_shape  # noqa: E402  (sibling module, shipped in the same directory)


def _describe(want: list, i: int) -> str:
    """Name a missing requirement using the template's own English headings, with
    its neighbours so it can be located in a document written in another language."""
    s = want[i]
    level = "level-%d" % s.depth
    before = want[i - 1].text if i > 0 else None
    after = want[i + 1].text if i + 1 < len(want) else None
    if before and after:
        where = ' between "%s" and "%s"' % (before, after)
    elif before:
        where = ' after "%s"' % before
    elif after:
        where = ' before "%s"' % after
    else:
        where = ""
    return '"%s" (a %s section%s)' % (s.text, level, where)


def evaluate(payload: dict, template_path: str) -> tuple[int, str]:
    """Return (exit_code, message). Pure — no I/O beyond reading the two files."""
    tmpl = Path(template_path)
    if not tmpl.is_file():
        return 0, ""
    if payload.get("tool_name") not in ("Write", "Edit"):
        return 0, ""
    fpath = (payload.get("tool_input") or {}).get("file_path", "")
    if not fpath or not fpath.endswith(".md"):
        return 0, ""
    f = Path(fpath)
    if not f.is_file():
        return 0, ""

    want = md_shape.collapse_repeats(
        md_shape.parse_sections(tmpl.read_text(encoding="utf-8")))
    if not want:
        return 0, ""
    got = md_shape.parse_sections(f.read_text(encoding="utf-8"))
    pairs = md_shape.align(want, got)

    # Only treat this file as the skill's deliverable if its shape already matches
    # at least half the template's sections — otherwise it's an unrelated file.
    # Unlike text matching, this threshold is reliable: a translated deliverable
    # has the same shape, so it scores near 100% rather than zero.
    matched = sum(1 for p in pairs if p is not None)
    if matched * 2 < len(want):
        return 0, ""

    missing = [i for i, p in enumerate(pairs) if p is None]
    if missing:
        return 2, ("Output does not follow the skill's template.md. Missing: "
                   + "; ".join(_describe(want, i) for i in missing)
                   + ". Add these sections — the headings may be written in this "
                     "project's language, only the structure has to match. "
                     "Disregard if this file is not the skill's deliverable.")
    return 0, ""


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    try:
        if len(sys.argv) < 2:
            return 0
        code, msg = evaluate(payload, sys.argv[1])
        if msg:
            print(msg, file=sys.stderr)
        return code
    except Exception:
        return 0  # fail-open: never block an edit


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_check_conformance.py -q`
Expected: PASS (11 cases).

- [ ] **Step 5: Extend the drift guard and distribute both files**

In `tests/test_hook_copies_identical.py`, replace the `COPIES` dict with:

```python
COPIES = {
    "check_output_conformance.py": "scripts/check_output_conformance.py",
    "md_shape.py": "scripts/md_shape.py",
    "output_language.py": "hooks/output_language.py",
    "hooks.json": "hooks/hooks.json",
}
```

Then distribute:

```bash
for p in pm-strategy pm-discovery pm-gtm pm-execution pm-influence; do
  /bin/cp scripts/skel/check_output_conformance.py "$p/scripts/check_output_conformance.py"
  /bin/cp scripts/skel/md_shape.py "$p/scripts/md_shape.py"
  cmp -s scripts/skel/check_output_conformance.py "$p/scripts/check_output_conformance.py" \
    && cmp -s scripts/skel/md_shape.py "$p/scripts/md_shape.py" \
    && echo "$p OK" || echo "$p DRIFT"
done
```

Expected: five `OK` lines. (`cp` is aliased to an interactive form on this machine — `/bin/cp` is required, and `cmp` is the check, not `md5`.)

- [ ] **Step 6: Verify the hook still works against the anchored corpus**

Anchors are still present at this point and must be harmless — they are HTML comments, which the parser skips.

```bash
uv run python -c "
import importlib.util, sys, pathlib
sys.path.insert(0, 'scripts/skel')
s = importlib.util.spec_from_file_location('c','scripts/skel/check_output_conformance.py')
c = importlib.util.module_from_spec(s); s.loader.exec_module(c)
t = 'pm-strategy/skills/market-sizing/template.md'
p = pathlib.Path('/tmp/selfcheck.md'); p.write_text(pathlib.Path(t).read_text(encoding='utf-8'))
print('template against itself:', c.evaluate({'tool_name':'Write','tool_input':{'file_path':str(p)}}, t))
"
/bin/rm -f /tmp/selfcheck.md
```

Expected: `(0, '')` — a template checked against itself is conformant.

- [ ] **Step 7: Verify both shipped files import on Python 3.9**

```bash
PY39=/Library/Developer/CommandLineTools/usr/bin/python3
for f in scripts/skel/md_shape.py scripts/skel/check_output_conformance.py \
         scripts/skel/output_language.py; do
  $PY39 -c "
import importlib.util, sys
sys.path.insert(0, 'scripts/skel')
s = importlib.util.spec_from_file_location('m', '$f')
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
print('OK  $f')"
done
```

Expected: three `OK` lines. `output_language.py` is included because it ships in the same plugins and must not silently regress.

- [ ] **Step 8: Run the full gate**

Run: `just test`
Expected: pytest passes and the linter reports `✓ ALL CHECKS PASSED (0 warnings)` over 5 plugins / 110 skills. Report the actual test count rather than assuming one.

- [ ] **Step 9: Commit**

```bash
git add scripts/skel/check_output_conformance.py \
        pm-*/scripts/check_output_conformance.py pm-*/scripts/md_shape.py \
        tests/test_check_conformance.py tests/test_hook_copies_identical.py
git commit -F - <<'EOF'
feat(tooling): shape-based output conformance

The hook now compares a produced document's shape against its template's —
heading depth, block kinds, table column counts — and never reads the document's
heading text. A deliverable written in the project's language is recognised and
enforced with no markers in it.

The half-threshold rule stays but stops being a liability: it was unsafe because
translation destroyed the signal it measured, and shape survives translation.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 5: Project-owned template override

**Files:**
- Modify: `scripts/skel/check_output_conformance.py`
- Modify: `tests/test_check_conformance.py`
- Modify: `pm-{strategy,discovery,gtm,execution,influence}/scripts/check_output_conformance.py`

**Interfaces:**
- Consumes: `evaluate` from Task 4.
- Produces:
  - `check_output_conformance.project_root(payload: dict) -> Path` — `CLAUDE_PROJECT_DIR`, else the payload's `cwd`, else the process cwd. Same precedence as `output_language.py`.
  - `check_output_conformance.resolve_template(payload: dict, plugin_template: str) -> Path` — the project's override if it exists, else the plugin's own template.

A team copies a skill's `template.md` to `.config/pm-skills/<skill>/template.md` in their own repo and edits it — translating headings, bullet labels and table headers, dropping sections they never fill in, adding ones they need. There is nothing to learn: it is the same markdown file, and after Task 6 it carries no anchors.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_check_conformance.py`:

```python
def test_project_root_prefers_the_env_var(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path / "env"))
    assert checker.project_root({"cwd": str(tmp_path / "payload")}) == tmp_path / "env"


def test_project_root_falls_back_to_payload_cwd(tmp_path, monkeypatch):
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    assert checker.project_root({"cwd": str(tmp_path)}) == tmp_path


def test_project_root_falls_back_to_process_cwd(monkeypatch):
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    assert checker.project_root({}) == Path.cwd()


def test_resolve_template_returns_the_plugin_template_by_default(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    plugin = _write(tmp_path, "template.md", TEMPLATE)
    assert checker.resolve_template({}, plugin) == Path(plugin)


def test_resolve_template_prefers_a_project_override(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    skill_dir = tmp_path / "plugin" / "skills" / "market-sizing"
    skill_dir.mkdir(parents=True)
    plugin = skill_dir / "template.md"
    plugin.write_text(TEMPLATE, encoding="utf-8")
    override = tmp_path / ".config" / "pm-skills" / "market-sizing" / "template.md"
    override.parent.mkdir(parents=True)
    override.write_text("## Autre\n- x\n", encoding="utf-8")
    assert checker.resolve_template({}, str(plugin)) == override


def test_a_project_override_is_what_gets_enforced(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    skill_dir = tmp_path / "plugin" / "skills" / "market-sizing"
    skill_dir.mkdir(parents=True)
    plugin = skill_dir / "template.md"
    plugin.write_text(TEMPLATE, encoding="utf-8")   # 4 sections
    override = tmp_path / ".config" / "pm-skills" / "market-sizing" / "template.md"
    override.parent.mkdir(parents=True)
    override.write_text("## Un\n- a\n## Deux\n- b\n", encoding="utf-8")  # 2 sections
    art = _write(tmp_path, "memo.md", "## Un\n- a\n## Deux\n- b\n")
    # Conformant to the override, though it has only half the plugin's sections.
    assert checker.evaluate({"tool_name": "Write",
                             "tool_input": {"file_path": art}}, str(plugin)) == (0, "")
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_check_conformance.py -q`
Expected: FAIL with `AttributeError: module 'check_output_conformance' has no attribute 'project_root'`.

- [ ] **Step 3: Implement resolution**

In `scripts/skel/check_output_conformance.py`, add `import os` to the imports, then insert before `evaluate`:

```python
def project_root(payload: dict) -> Path:
    """The consuming project's root: the env var Claude Code sets, else the
    session's cwd from the hook payload, else the process cwd. Same precedence
    as the SessionStart output-language hook."""
    for candidate in (os.environ.get("CLAUDE_PROJECT_DIR"), payload.get("cwd")):
        if candidate:
            return Path(candidate)
    return Path.cwd()


def resolve_template(payload: dict, plugin_template: str) -> Path:
    """The template to enforce: a project's own copy if it has one, else the
    plugin's.

    A team owns its document structure — they copy the skill's template.md to
    `.config/pm-skills/<skill>/template.md` and edit it freely: translate the
    headings, the bullet labels and the table column headers, drop sections they
    never fill in, add ones they need.
    """
    plugin_path = Path(plugin_template)
    skill = plugin_path.parent.name
    override = project_root(payload) / ".config" / "pm-skills" / skill / "template.md"
    return override if override.is_file() else plugin_path
```

Then in `evaluate`, replace the first two lines:

```python
    tmpl = Path(template_path)
    if not tmpl.is_file():
        return 0, ""
```

with:

```python
    if not Path(template_path).is_file():
        return 0, ""
    tmpl = resolve_template(payload, template_path)
    if not tmpl.is_file():
        return 0, ""
```

The plugin's own template must exist for the hook to be meaningful at all; the override is then preferred over it.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_check_conformance.py -q`
Expected: PASS (17 cases).

- [ ] **Step 5: Distribute and verify**

```bash
for p in pm-strategy pm-discovery pm-gtm pm-execution pm-influence; do
  /bin/cp scripts/skel/check_output_conformance.py "$p/scripts/check_output_conformance.py"
  cmp -s scripts/skel/check_output_conformance.py "$p/scripts/check_output_conformance.py" \
    && echo "$p OK" || echo "$p DRIFT"
done
just test
```

Expected: five `OK` lines, then a green gate.

- [ ] **Step 6: Commit**

```bash
git add scripts/skel/check_output_conformance.py \
        pm-*/scripts/check_output_conformance.py tests/test_check_conformance.py
git commit -F - <<'EOF'
feat(tooling): project-owned template override

A project may put its own copy of a skill's template at
.config/pm-skills/<skill>/template.md, and the hook enforces that instead of the
plugin's. Teams translate the headings, bullet labels and table column headers,
drop sections they never fill in, and add ones they need — with nothing new to
learn, since it is the same markdown file.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 6: Remove the anchors

**Files:**
- Modify: all 110 `pm-*/skills/*/template.md`
- Modify: `scripts/skillkit.py` (delete the "Template anchors" section and `cmd_anchors`)
- Modify: `justfile` (delete the `anchors` recipe)
- Modify: `tests/validate_plugins.py` (delete `_FENCE_LINE`, `strip_fenced_blocks`, the anchor checks)
- Modify: `tests/test_template_check.py` (delete the anchor cases, restore plain fixtures)
- Delete: `tests/test_skillkit_anchors.py`
- Modify: `docs/skill-template/template.md`

**Interfaces:**
- Consumes: the shape-based hook from Tasks 4–5, which does not read anchors.
- Produces: nothing new. This task only removes.

This is the closing commit of the design. Everything the anchors did is now done by shape, so leaving them would mean maintaining a second identity mechanism that nothing consults.

- [ ] **Step 1: Strip the anchors from all 110 templates**

```bash
uv run python -c "
import glob, pathlib, re
n = files = 0
for f in sorted(glob.glob('pm-*/skills/*/template.md')):
    p = pathlib.Path(f); old = p.read_text(encoding='utf-8')
    new, k = re.subn(r' <!--#[a-z0-9-]+-->', '', old)
    if k:
        p.write_text(new, encoding='utf-8'); n += k; files += 1
print('removed', n, 'anchors from', files, 'templates')
"
```

Expected: `removed 816 anchors from 110 templates`.

- [ ] **Step 2: Verify the removal changed nothing else**

```bash
uv run python -c "
import re, subprocess
files = subprocess.run(['git','diff','--name-only','--','pm-strategy','pm-discovery',
                        'pm-gtm','pm-execution','pm-influence'],
                       capture_output=True, text=True, check=True).stdout.split()
for f in files:
    head = subprocess.run(['git','show','HEAD:'+f], capture_output=True, text=True,
                          check=True).stdout
    now = open(f, encoding='utf-8').read()
    assert re.sub(r' <!--#[a-z0-9-]+-->', '', head) == now, f
    assert '<!--#' not in now, f
print('OK:', len(files), 'templates, anchor-only removal, none left')
"
```

Expected: `OK: 110 templates, anchor-only removal, none left`. If a file fails the assertion, the edit touched something other than anchors — stop and report.

- [ ] **Step 3: Delete the anchor tooling from `skillkit.py`**

In `scripts/skillkit.py`:
- delete the whole `# ─── Template anchors ───` block: the comment, `_HEADING_LINE`, `_ANCHOR`, `_FENCE_LINE`, `_fence_mask`, `slugify` and `anchor_template`;
- delete the `cmd_anchors` function;
- remove `"anchors": cmd_anchors,` from the `COMMANDS` dict;
- restore the module docstring's subcommand line to `Subcommands: next | scaffold | context | wip | done | progress`.

Delete the test file entirely:

```bash
git rm -q tests/test_skillkit_anchors.py
```

And delete the `anchors` recipe from `justfile` — the comment block and the two lines beginning `anchors target=""`.

- [ ] **Step 4: Delete the anchor checks from the linter**

In `tests/validate_plugins.py`:
- delete `_FENCE_LINE` and `strip_fenced_blocks`;
- inside `validate_template`, revert the two `re.findall` calls to read `body` directly instead of the stripped prose, and delete the two anchor blocks — the `if len(anchors) < headings:` error and the `dupes` error;
- remove the `template.md: every '##'/'###' heading carries a unique '<!--#slug-->' anchor.` bullet from the module docstring's "Checks:" list.

In `tests/test_template_check.py`, delete `test_missing_anchor_is_error`, `test_duplicate_anchor_is_error`, `test_fully_anchored_template_is_clean` and `test_unreferenced_template_is_not_anchor_checked`, and remove the ` <!--#...-->` anchors from the fixtures in `test_fewer_headings_than_contract_warns` and `test_level3_headings_count_toward_sections` so they read as they did before anchors existed:

```python
def test_fewer_headings_than_contract_warns(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE, template_md="# T\n## A\n")
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert not r.errors
    assert any("Output Contract" in w for w in r.warnings)


def test_level3_headings_count_toward_sections(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE, template_md="# T\n## Bucket\n### A\n### B\n")
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert not r.errors and not r.warnings
```

- [ ] **Step 5: De-anchor the scaffold skeleton**

Replace `docs/skill-template/template.md` with:

```markdown
# <Artifact Title>

<!--
The fill-in output template the skill produces. Mirror the Output Contract
sections from SKILL.md exactly. Use placeholders in <angle brackets> and short
inline guidance in comments. Delete this comment block in real templates.

The output-conformance hook checks a produced document against this file by
comparing structure — how many sections, at what heading level, holding what
kinds of content — and never by matching heading text. That is what lets a
deliverable written in the project's own language still be checked, so nothing
needs to be embedded in the output.

A section drawn several times (Frame 1, Frame 2, ...) is understood as a
repeating block: a document may contain as many as it needs, and at least one.
-->

## <Section 1>
<placeholder>

## <Section 2>
<placeholder>

| <col> | <col> |
|-------|-------|
| <...> | <...> |
```

- [ ] **Step 6: Run the full gate**

Run: `just test`
Expected: pytest passes and the linter reports `✓ ALL CHECKS PASSED (0 warnings)` over 5 plugins / 110 skills. The suite shrinks by the 14 `test_skillkit_anchors.py` cases and the 4 deleted linter cases; report the actual number.

- [ ] **Step 7: Confirm nothing still references anchors in code**

```bash
grep -rn '<!--#\|anchor_template\|cmd_anchors\|slugify\|strip_fenced_blocks' \
  scripts/ tests/ justfile pm-*/scripts/ pm-*/skills/ || echo "clean"
```

Expected: `clean`. Remaining references in `docs/` and the eval cards are Task 7's job.

- [ ] **Step 8: Commit**

```bash
git add -A scripts tests justfile docs/skill-template pm-strategy pm-discovery \
          pm-gtm pm-execution pm-influence
git commit -F - <<'EOF'
chore: remove section anchors

Shape matching identifies a section by depth, position and content kind, so the
816 `<!--#slug-->` anchors have nothing left to do. Removes them from all 110
templates along with `just anchors`, the skillkit anchor helpers, the linter's
anchor presence and uniqueness checks, both fence helpers (now inside the
parser) and the skeleton's anchor guidance.

Deliverables no longer carry markers of any kind.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 7: Documentation

**Files:**
- Modify: `docs/output-language.md`
- Modify: `docs/SKILL-STANDARD.md`
- Modify: `pm-strategy/skills/market-sizing/evals/market-sizing-fr-project.md`
- Modify: `pm-strategy/skills/market-sizing/evals/market-sizing-b2b-saas-eu.md`
- Modify: `pm-strategy/skills/market-sizing/evals/market-sizing-consumer-edge.md`

**Interfaces:**
- Consumes: the finished behaviour from Tasks 4–6.
- Produces: nothing code-facing.

- [ ] **Step 1: Rewrite the anchor sections of `docs/output-language.md`**

Replace the section titled `## Why templates carry <!--#anchor--> comments` with:

```markdown
## How a translated document is still checked

A `PostToolUse` hook checks each produced document against its skill's template.
It compares **structure**, not words: how many sections, at what heading level,
in what order, holding what kinds of content — paragraphs, lists, tables and
their column counts.

Structure survives translation; heading text does not. So a memo whose every
heading is in French matches its English template exactly, and the document
carries no markers, comments or frontmatter of any kind.

When a section is missing, the hook names it from the template, in English, along
with its neighbours so it can be located in a document written in another
language:

> Missing: "SAM — Serviceable Addressable Market" (a level-2 section, expected
> between "TAM — Total Addressable Market" and "SOM — Serviceable Obtainable
> Market").

A section a template draws several times — Frame 1, Frame 2, … — is understood as
a repeating block. A document may contain as many as it needs, and at least one.

## Making a template your own

Copy a skill's `template.md` to `.config/pm-skills/<skill>/template.md` in your
project and the hook enforces that instead of the plugin's. Translate the
headings, the bullet labels and the table column headers; drop sections you never
fill in; add ones you need. It is the same markdown file — there is nothing new
to learn, and nothing to keep in sync.
```

Then replace the `## Limitations` section with:

```markdown
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
- Structural checking is deliberately coarse: it verifies that sections exist,
  at the right level, containing the right kind of content. Whether a figure is
  cited or an assumption carries a confidence level is a question of quality, and
  belongs to each skill's eval cards.
```

- [ ] **Step 2: Update the eval-card guidance in the standard**

In `docs/SKILL-STANDARD.md` §4, replace the `**Language:**` paragraph with:

```markdown
**Language:** cards are always written in English, and a skill does not need a
per-language card. Where output language is genuinely load-bearing for a skill,
add one card whose `input.context` declares a non-English project and whose
`expected` traits assert the deliverable is in that language, that PM jargon is
untranslated, and that the section structure is unchanged. `market-sizing`
carries the reference card (`evals/market-sizing-fr-project.md`); see
[`docs/output-language.md`](output-language.md).
```

- [ ] **Step 3: Update the three `market-sizing` eval cards**

In `evals/market-sizing-fr-project.md`, replace the anchor-preservation trait in `expected`:

```yaml
  - "Preserves the template's section structure: same sections, same order, same heading levels"
```

and rewrite the closing note to:

```markdown
Language card: the project declares French, so the memo is French but its
structure is unchanged. Guards against the two failure modes that matter — an
English memo in a French project, and a French memo that reorganises or drops
sections (or translates TAM/SAM/SOM) and so no longer matches the template.

This is the pattern to copy for any skill whose output language is load-bearing;
see docs/output-language.md.
```

In `evals/market-sizing-b2b-saas-eu.md` and `evals/market-sizing-consumer-edge.md`, remove any `expected` trait mentioning `<!--#anchor-->` comments. Read each file first — if a card's only anchor mention is in prose notes rather than `expected`, reword the prose and leave the traits alone.

- [ ] **Step 4: Confirm no anchor references remain**

```bash
grep -rn '<!--#' docs/ pm-*/skills/ README.md CLAUDE.md \
  --include='*.md' | grep -v 'docs/superpowers/' || echo "clean"
```

Expected: `clean`. Matches under `docs/superpowers/` are the historical plan and spec documents and are left alone — they record what was done and why.

- [ ] **Step 5: Run the full gate**

Run: `just test`
Expected: pytest passes, linter `✓ ALL CHECKS PASSED (0 warnings)`, `market-sizing` still reporting 4 eval cards.

- [ ] **Step 6: Commit**

```bash
git add docs/output-language.md docs/SKILL-STANDARD.md \
        pm-strategy/skills/market-sizing/evals/
git commit -F - <<'EOF'
docs: shape matching

Rewrites the anchor sections of docs/output-language.md to describe structural
matching, documents the project template override, and adds the limitation that
a prompt-requested language bypasses the SessionStart hook. Updates the eval
cards to assert structure is preserved rather than that anchors survive.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Self-review notes

**Spec coverage.** Every section of `pm-skills-plan/pm-skills-shape-matching.md` maps to a task: §1 the shape record → Task 1; §2 repeat families → Task 2; §3 alignment → Task 3; §4 identification threshold → Task 4; §5 messages → Task 4 (`_describe`); §6 project-owned templates → Task 5; "What this deletes" → Task 6; the docs implied by it → Task 7. The spec's Out of scope list is respected: no schema DSL, no frontmatter markers, no semantic validation, no cardinality ceilings, and the language-declaration half is untouched.

**Known risks for the executor.**
1. Task 1 Step 5 asserts the parser finds exactly 816 sections. That number is the corpus's current anchor count, so it is a genuine cross-check of the new parser against the shipped one — if it disagrees, the design's premise is wrong somewhere, not the arithmetic.
2. Task 2's signature heuristic is the one piece with no formal specification behind it. Step 5 measures it against all 110 templates and expects exactly 21. That number was verified by running this plan's own code over the corpus on Python 3.9.6 and inspecting what each collapse dropped; earlier estimates of 12 and 20 came from a looser heuristic and from a pre-anchor-stripping run, and both were wrong. Treat a 22nd as a finding, not a rounding error.
3. Task 6 is irreversible in the working tree if run carelessly. Its Step 2 verifier asserts that re-adding the anchors reproduces `HEAD` exactly, which is the only check that proves the edit touched nothing else.
