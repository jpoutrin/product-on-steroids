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
import os
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


def evaluate(payload: dict, template_path: str) -> tuple[int, str]:
    """Return (exit_code, message). Pure — no I/O beyond reading the two files."""
    if not Path(template_path).is_file():
        return 0, ""
    tmpl = resolve_template(payload, template_path)
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
