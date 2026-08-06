#!/usr/bin/env python3
"""skillkit — token-lean helpers for authoring product-on-steroids skills.

Subcommands: next | scaffold | context | wip | done | progress
Run via `just <recipe>` or `uv run python scripts/skillkit.py <cmd> [skill]`.
Stdlib only; reuses validate_plugins for linting.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TASKS_PATH = REPO_ROOT / "TASKS.md"
TEMPLATE_DIR = REPO_ROOT / "docs" / "skill-template"
BRIEF_PATH = REPO_ROOT / "docs" / "SKILL-BRIEF.md"
PHURYN_ROOT = REPO_ROOT / "work" / "phuryn-pm-skills"

PHURYN_SHA = "18468a9"
SOURCE_ALIAS = {"product-strategy-canvas": "product-strategy"}
BUILD_ORDER = ["pm-strategy", "pm-discovery", "pm-gtm", "pm-execution", "pm-influence"]
PRIORITY_ORDER = {"P1": 0, "P2": 1, "P3": 2}

_PLUGIN_HEADING = re.compile(r"^##\s+(pm-[\w-]+)\b")
_ROW = re.compile(r"^\|(.+)\|\s*$")


def load_tasks(text: str) -> list[dict]:
    """Parse buildable skill rows (those under a `## pm-*` heading) from TASKS.md."""
    tasks: list[dict] = []
    plugin: str | None = None
    for line_no, line in enumerate(text.splitlines()):
        h = _PLUGIN_HEADING.match(line)
        if h:
            plugin = h.group(1)
            continue
        if line.startswith("## "):        # left the plugin sections (Cross-cutting, Agents, ...)
            plugin = None
            continue
        if plugin is None:
            continue
        m = _ROW.match(line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(1).split("|")]
        if len(cells) != 4:
            continue
        skill, disposition, priority, status = cells
        if disposition not in ("IMPORT", "GENERATE"):   # header / separator / other
            continue
        tasks.append({
            "skill": skill, "plugin": plugin, "disposition": disposition,
            "priority": priority, "status": status, "line_no": line_no,
        })
    return tasks


def select_next(tasks: list[dict]) -> dict | None:
    todo = [t for t in tasks if t["status"] == "todo"]
    if not todo:
        return None
    todo.sort(key=lambda t: (
        BUILD_ORDER.index(t["plugin"]) if t["plugin"] in BUILD_ORDER else 99,
        PRIORITY_ORDER.get(t["priority"], 9),
        t["line_no"],
    ))
    return todo[0]


def progress_report(tasks: list[dict]) -> str:
    lines = []
    for plugin in BUILD_ORDER:
        rows = [t for t in tasks if t["plugin"] == plugin]
        if not rows:
            continue
        done = sum(1 for t in rows if t["status"] == "done")
        wip = sum(1 for t in rows if t["status"] == "wip")
        todo = sum(1 for t in rows if t["status"] == "todo")
        lines.append(f"{plugin:14} {done}/{len(rows)} done ({wip} wip, {todo} todo)")
    total = len(tasks)
    tdone = sum(1 for t in tasks if t["status"] == "done")
    lines.append(f"{'TOTAL':14} {tdone}/{total} done")
    return "\n".join(lines)


def _tasks() -> list[dict]:
    return load_tasks(TASKS_PATH.read_text(encoding="utf-8"))


def cmd_next(_: list[str]) -> int:
    nxt = select_next(_tasks())
    if nxt is None:
        print("all skills done")
        return 0
    print(f"{nxt['skill']}\t{nxt['disposition']}\t{nxt['plugin']}\t{nxt['priority']}")
    return 0


def cmd_progress(_: list[str]) -> int:
    print(progress_report(_tasks()))
    return 0


COMMANDS = {"next": cmd_next, "progress": cmd_progress}


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in COMMANDS:
        print(f"usage: skillkit.py {{{'|'.join(COMMANDS)}}} [skill]", file=sys.stderr)
        return 2
    return COMMANDS[argv[0]](argv[1:])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
