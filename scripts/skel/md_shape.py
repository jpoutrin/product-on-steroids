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
