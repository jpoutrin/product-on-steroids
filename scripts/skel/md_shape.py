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


def _comment_mask(lines: list[str], fenced: list[bool]) -> list[bool]:
    """`True` for every line consumed by an HTML comment (`<!-- ... -->`).

    Lines inside a fenced code block are not inspected — a `<!--` inside a code
    sample is illustrative content, not a real comment marker, and fenced
    lines are already handled by `_fence_mask`.

    An HTML comment that opens and never closes before end of file is not a
    comment — it is a malformed document. Same rule as `_fence_mask`: the
    region from its opening marker onward is reclassified as ordinary prose,
    so headings inside it are still seen rather than silently lost.
    """
    mask: list[bool] = []
    in_comment = False
    comment_start: int | None = None
    for i, line in enumerate(lines):
        if fenced[i]:
            mask.append(False)
            continue
        s = line.strip()
        if in_comment:
            mask.append(True)
            if "-->" in s:
                in_comment = False
            continue
        if s.startswith("<!--"):
            comment_start = i
            in_comment = "-->" not in s
            mask.append(True)
            continue
        mask.append(False)
    if in_comment:
        for i in range(comment_start, len(lines)):
            mask[i] = False
    return mask


def _table_columns(line: str) -> int:
    """Column count of a pipe-table row, tolerant of a missing trailing pipe.

    Strips at most one boundary pipe per side: `|| B | C |` is an empty first
    cell, not a doubled delimiter. An escaped `\\|` is literal content, not a
    separator, so it is neutralised before the split.
    """
    s = line.strip().replace(r"\|", "\0")
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return len(s.split("|"))


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
    commented = _comment_mask(lines, fenced)
    out: list[Section] = []
    depth: int | None = None
    text = ""
    blocks: list[str] = []

    def add(kind: str) -> None:
        if not blocks or blocks[-1] != kind:
            blocks.append(kind)

    for i, line in enumerate(lines):
        if fenced[i]:
            if depth is not None:
                add("code")
            continue
        if commented[i]:
            continue
        s = line.strip()
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
    runs normalised away, plus the depth sequence of its children.

    Accepted limitation: normalising *every* digit run means two adjacent
    sections that differ only in a number merge even when the number is
    content, not an index ("Top 10 Risks" / "Top 3 Risks" would collapse to
    one). Tightening this to require a strict 1,2,3 sequence was considered
    and rejected — `user-story-mapping` and `user-story-splitting` both pair
    a numbered heading with a literal "N" placeholder ("Release 2" / "Release
    N", "Story 2" / "Story N") meaning "and so on"; a sequential-index rule
    would break those two shipped templates to guard against a shape that
    does not occur anywhere in the corpus. Left coarse deliberately; see
    test_collapse_merges_headings_differing_only_by_a_non_index_digit and
    test_collapse_handles_the_and_so_on_placeholder_idiom.
    """
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
