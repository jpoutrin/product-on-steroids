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
never heading text — and reports the template sections that found no partner.

Two different questions, answered by two different rules:

  * *Is this file the skill's deliverable at all?* Only if at least half the
    template's sections are present with an **exact** shape match — same depth
    and the same block kinds in the same order. Content kinds are what makes
    this question answerable; a weaker rule recognises any markdown file with
    enough `##` headings and starts rewriting the user's meeting notes.
  * *Which sections are missing?* Any template section the aligner left
    unpartnered. Content kinds only steer *which* document section a template
    section pairs with here; they can never make a section missing on their own.

If the file is the deliverable and sections are missing, exits 2. The stderr
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


def _describe(want: list[md_shape.Section], i: int) -> str:
    """Locate a missing requirement by level and neighbours, and offer the
    template's own English heading as a *candidate* name.

    The level and the neighbours are reliable; the name is not. Sections that
    are structurally identical are interchangeable to a shape matcher, so when
    one of two lookalikes is dropped the aligner cannot tell which — measured
    over the corpus, the count is right every time but the name only about
    three times in four. Hence the hedge: the reader must not be told to add
    "Growth Drivers & Trends" as a certainty when that section is present and
    its neighbour is the one that went missing.
    """
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
    return 'a %s section%s — probably "%s"' % (level, where, s.text)


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
    """Return (exit_code, message).

    Side-effect free, but not I/O free: it reads `CLAUDE_PROJECT_DIR` from the
    environment (via `project_root`), stats the plugin template, the possible
    project override and the written file, and reads the two markdown files it
    ends up comparing. It writes nothing and exits nothing — the caller owns
    stderr and the exit code.
    """
    if not Path(template_path).is_file():
        return 0, ""
    # No second `is_file()` on the result: `resolve_template` returns either the
    # override (which it just stat'd) or `template_path` (stat'd on the line
    # above), so both branches are already known to exist.
    tmpl = resolve_template(payload, template_path)
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

    # Is this file the skill's deliverable, or an unrelated markdown file this
    # hook must stay silent about? It fires on every `.md` write while the skill
    # is loaded, so a false yes means rewriting someone's notes: the bar is at
    # least half the template's sections present with an *exact* shape match.
    #
    # Merely being paired proves nothing. Two same-depth records always pair —
    # a bare depth match scores 0, gapping both costs -2 — and 66 of the 110
    # templates are entirely depth-2, so counting non-`None` pairs degenerates
    # into "does this file have half as many `##` headings as the template".
    # Measured over 110 templates x 5 unrelated repo documents: counting any
    # pair blocked 276 of 550, requiring exact block kinds blocked 0.
    matched = sum(1 for i, p in enumerate(pairs)
                  if p is not None and md_shape.is_exact_match(want[i], got[p]))
    if matched * 2 < len(want):
        return 0, ""

    # Missing is a weaker test than recognition, deliberately: a section counts
    # as present on any pairing at all. Block kinds decide whether to speak;
    # they never decide that a section is absent.
    missing = [i for i, p in enumerate(pairs) if p is None]
    if missing:
        lead = ("A section is missing" if len(missing) == 1
                else "%d sections are missing" % len(missing))
        return 2, ("Output does not follow the skill's template.md. %s: " % lead
                   + "; ".join(_describe(want, i) for i in missing)
                   + ". The level and the neighbours are reliable; the quoted name "
                     "is the template's best guess at which section was dropped, "
                     "not a certainty — check before adding one, so you do not "
                     "duplicate a section that is already there. Headings may be "
                     "written in this project's language; only the structure has "
                     "to match. Disregard if this file is not the skill's "
                     "deliverable.")
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
