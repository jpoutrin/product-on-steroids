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
skill's deliverable (already contains >= half the template's `##`/`###` headings) but is
missing some, exits 2 — the stderr message is fed back to Claude so it revises the file.

Fail-open everywhere: any unexpected condition returns 0 so authoring is never blocked.
Stdlib only, plain `python3` (no uv) so it runs on an end user's machine.
"""
import json
import re
import sys
from pathlib import Path


def headings(md: str) -> list[str]:
    """The text of every level-2 (`## `) and level-3 (`### `) heading, in order.

    Level-3 is included so templates that group sections under `##` buckets with
    the real sections as `###` (e.g. a 9-block canvas) are enforced fully.
    """
    return [h.strip() for h in re.findall(r"(?m)^#{2,3}\s+(.+?)\s*$", md)]


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
    want = headings(tmpl.read_text(encoding="utf-8"))
    if not want:
        return 0, ""
    content = f.read_text(encoding="utf-8")
    present = [h for h in want if h in content]
    # Only treat this file as the skill's deliverable if it already matches at least
    # half the template's sections — otherwise it's an unrelated file; stay silent.
    if len(present) * 2 < len(want):
        return 0, ""
    missing = [h for h in want if h not in content]
    if missing:
        return 2, (
            "Output does not follow the skill's template.md. Missing sections: "
            + "; ".join(missing)
            + ". Add these sections (matching the template headings), or disregard "
            "if this file is not the skill's deliverable."
        )
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
