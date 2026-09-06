#!/usr/bin/env python3
"""Skill-scoped PostToolUse hook — verify a written artifact follows the skill's template.

Distributed inside each plugin as `<plugin>/scripts/check_output_conformance.py` and
wired from a skill's frontmatter:

    hooks:
      PostToolUse:
        - matcher: "Write|Edit"
          hooks:
            - type: command
              command: python3
              args:
                - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
                - ${CLAUDE_PLUGIN_ROOT}/skills/<skill>/template.md

The argument is THIS skill's own template.md, so each skill validates against its own
structure. Reads the PostToolUse JSON on stdin, and if the written file looks like the
skill's deliverable (already matches >= half the template's sections, by
`<!--#anchor-->` comment OR by heading text) but is missing some, exits 2 — the
stderr message is fed back to Claude so it revises the file.

Fail-open everywhere: any unexpected condition returns 0 so authoring is never blocked.
Stdlib only, plain `python3` (no uv) so it runs on an end user's machine.
"""
import json
import re
import sys
from pathlib import Path


ANCHOR_RE = re.compile(r"<!--#([a-z0-9-]+)-->")


def parse_headings(md: str) -> list[tuple[str, str]]:
    """`(anchor, text)` for every level-2 (`## `) and level-3 (`### `) heading.

    `anchor` is the slug inside a trailing `<!--#slug-->` comment, or `""` when the
    heading carries none. `text` always has the comment stripped, so the two modes
    below share one parse and error messages stay readable.

    Level-3 is included so templates that group sections under `##` buckets with
    the real sections as `###` (e.g. a 9-block canvas) are enforced fully.
    """
    out: list[tuple[str, str]] = []
    for raw in re.findall(r"(?m)^#{2,3}\s+(.+?)\s*$", md):
        m = ANCHOR_RE.search(raw)
        out.append((m.group(1) if m else "", ANCHOR_RE.sub("", raw).strip()))
    return out


def headings(md: str) -> list[str]:
    """The anchor-stripped text of every level-2/level-3 heading, in order."""
    return [text for _, text in parse_headings(md)]


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
    want = parse_headings(tmpl.read_text(encoding="utf-8"))
    if not want:
        return 0, ""
    content = f.read_text(encoding="utf-8")

    # Anchor mode as soon as the template carries any `<!--#slug-->`: the anchor is
    # language-independent, so a translated deliverable is still recognised and
    # still enforced. A template with no anchors keeps today's text matching, which
    # is what makes the migration incremental.
    anchored = any(anchor for anchor, _ in want)

    def found(anchor: str, text: str) -> bool:
        if anchored and anchor:
            return f"<!--#{anchor}-->" in content
        return text in content

    # Recognition is deliberately wider than enforcement: a section counts toward the
    # threshold by anchor OR by heading text, but only the anchor satisfies it. So a
    # document produced before the template gained anchors (all English headings, no
    # anchors) is still recognised as the deliverable, flagged for every section, and
    # told below to copy the anchors — it self-migrates on the next edit instead of
    # silently dropping out of enforcement.
    present = sum(1 for anchor, text in want if found(anchor, text) or text in content)
    # Only treat this file as the skill's deliverable if it already matches at least
    # half the template's sections — otherwise it's an unrelated file; stay silent.
    if present * 2 < len(want):
        return 0, ""
    missing = [text for anchor, text in want if not found(anchor, text)]
    if missing:
        msg = ("Output does not follow the skill's template.md. Missing sections: "
               + "; ".join(missing)
               + ". Add these sections (matching the template headings), or disregard "
                 "if this file is not the skill's deliverable.")
        if anchored:
            msg += (" Copy each section's `<!--#anchor-->` comment from template.md "
                    "verbatim — that is how the section is identified, whatever "
                    "language the heading is written in.")
        return 2, msg
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
