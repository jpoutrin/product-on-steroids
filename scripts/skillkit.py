#!/usr/bin/env python3
"""skillkit — token-lean helpers for authoring product-on-steroids skills.

Subcommands: next | scaffold | context | wip | done | progress
Run via `just <recipe>` or `uv run python scripts/skillkit.py <cmd> [skill]`.
Stdlib only; reuses validate_plugins for linting.
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

try:
    from validate_plugins import validate_skill
except ImportError:  # in-tree fallback when not installed as a module
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tests"))
    from validate_plugins import validate_skill

REPO_ROOT = Path(__file__).resolve().parent.parent
TASKS_PATH = REPO_ROOT / "TASKS.md"
TEMPLATE_DIR = REPO_ROOT / "docs" / "skill-template"
BRIEF_PATH = REPO_ROOT / "docs" / "SKILL-BRIEF.md"
PHURYN_ROOT = REPO_ROOT / "work" / "phuryn-pm-skills"
# Canonical output-conformance hook script, copied into each plugin's scripts/ dir
# so the skill-scoped hook resolves it via ${CLAUDE_PLUGIN_ROOT}/scripts/ once installed.
CHECKER_SRC = REPO_ROOT / "scripts" / "skel" / "check_output_conformance.py"
CHECKER_REL = Path("scripts") / "check_output_conformance.py"

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


_VARIANTS = ("happy", "edge", "adversarial")


def find_task(tasks: list[dict], skill: str) -> dict:
    for t in tasks:
        if t["skill"] == skill:
            return t
    raise KeyError(skill)


def import_source(disposition: str, skill: str) -> str:
    if disposition == "IMPORT":
        return f"import:phuryn/pm-skills@{PHURYN_SHA}"
    return "original"


def cmd_scaffold(args: list[str]) -> int:
    if not args:
        print("usage: skillkit.py scaffold <skill>", file=sys.stderr)
        return 2
    skill = args[0]
    try:
        task = find_task(load_tasks(TASKS_PATH.read_text(encoding="utf-8")), skill)
    except KeyError:
        print(f"error: '{skill}' not found in TASKS.md", file=sys.stderr)
        return 1
    dest = REPO_ROOT / task["plugin"] / "skills" / skill
    if dest.exists():
        print(f"error: {dest} already exists — refusing to overwrite", file=sys.stderr)
        return 1
    shutil.copytree(TEMPLATE_DIR, dest)

    # Fill frontmatter
    skill_md = dest / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    text = re.sub(r"(?m)^name:\s*skill-name$", f"name: {skill}", text)
    text = re.sub(r"(?m)^source:\s*original$",
                  f"source: {import_source(task['disposition'], skill)}", text)
    # Point the skill-scoped conformance hook at THIS skill's own template.md.
    text = text.replace("skills/skill-name/template.md", f"skills/{skill}/template.md")
    skill_md.write_text(text, encoding="utf-8")

    # Ensure the plugin ships the conformance checker the frontmatter hook references.
    checker_dst = REPO_ROOT / task["plugin"] / CHECKER_REL
    if not checker_dst.exists() and CHECKER_SRC.is_file():
        checker_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(CHECKER_SRC, checker_dst)

    # Expand the single example eval card into happy/edge/adversarial
    example = dest / "evals" / "example.md"
    proto = example.read_text(encoding="utf-8") if example.exists() else \
        "---\nid: skill-name-happy\nskill: skill-name\n---\n"
    for variant in _VARIANTS:
        card = proto
        card = re.sub(r"(?m)^id:\s*skill-name-\w+$", f"id: {skill}-{variant}", card)
        card = re.sub(r"(?m)^id:\s*skill-name$", f"id: {skill}-{variant}", card)
        card = re.sub(r"(?m)^skill:\s*skill-name$", f"skill: {skill}", card)
        (dest / "evals" / f"{skill}-{variant}.md").write_text(card, encoding="utf-8")
    if example.exists():
        example.unlink()

    print(f"scaffolded {dest.relative_to(REPO_ROOT)}")
    return 0


def phuryn_source_path(skill: str) -> Path | None:
    name = SOURCE_ALIAS.get(skill, skill)
    matches = sorted(PHURYN_ROOT.glob(f"*/skills/{name}/SKILL.md"))
    return matches[0] if matches else None


def build_pack(task: dict, brief: str, source_text: str | None) -> str:
    row = (f"skill: {task['skill']}  |  plugin: {task['plugin']}  |  "
           f"disposition: {task['disposition']}  |  priority: {task['priority']}")
    parts = [f"# BUILD PACK — {task['skill']}", "", row, "", "=== SKILL-BRIEF ===",
             brief]
    if task["disposition"] == "IMPORT":
        if source_text is not None:
            parts += ["", "=== PHURYN SOURCE (adapt this — MIT) ===", source_text]
    else:
        parts += ["", "=== GENERATE ===",
                  "Write an original skill. deanpeters is idea-reference only — "
                  "never copy its text. Set source: original (scaffold did this)."]
    return "\n".join(parts)


def cmd_context(args: list[str]) -> int:
    if not args:
        print("usage: skillkit.py context <skill>", file=sys.stderr)
        return 2
    skill = args[0]
    try:
        task = find_task(load_tasks(TASKS_PATH.read_text(encoding="utf-8")), skill)
    except KeyError:
        print(f"error: '{skill}' not found in TASKS.md", file=sys.stderr)
        return 1
    brief = BRIEF_PATH.read_text(encoding="utf-8")
    source_text = None
    if task["disposition"] == "IMPORT":
        src = phuryn_source_path(skill)
        if src is None:
            print(f"error: phuryn source for '{skill}' not found under {PHURYN_ROOT}. "
                  f"Clone/refresh work/phuryn-pm-skills (gitignored).", file=sys.stderr)
            return 1
        source_text = src.read_text(encoding="utf-8")
    print(build_pack(task, brief, source_text))
    return 0


def set_status(text: str, skill: str, status: str) -> str:
    lines = text.splitlines(keepends=True)
    for task in load_tasks(text):
        if task["skill"] != skill:
            continue
        i = task["line_no"]
        eol = "\n" if lines[i].endswith("\n") else ""
        m = _ROW.match(lines[i].rstrip("\n"))
        cells = [c.strip() for c in m.group(1).split("|")]
        cells[-1] = status
        lines[i] = "| " + " | ".join(cells) + " |" + eol
        return "".join(lines)
    raise KeyError(skill)


def cmd_wip(args: list[str]) -> int:
    if not args:
        print("usage: skillkit.py wip <skill>", file=sys.stderr)
        return 2
    skill = args[0]
    text = TASKS_PATH.read_text(encoding="utf-8")
    try:
        TASKS_PATH.write_text(set_status(text, skill, "wip"), encoding="utf-8")
    except KeyError:
        print(f"error: '{skill}' not found in TASKS.md", file=sys.stderr)
        return 1
    print(f"{skill} -> wip")
    return 0


def cmd_done(args: list[str]) -> int:
    if not args:
        print("usage: skillkit.py done <skill>", file=sys.stderr)
        return 2
    skill = args[0]
    text = TASKS_PATH.read_text(encoding="utf-8")
    try:
        task = find_task(load_tasks(text), skill)
    except KeyError:
        print(f"error: '{skill}' not found in TASKS.md", file=sys.stderr)
        return 1
    skill_dir = REPO_ROOT / task["plugin"] / "skills" / skill
    result = validate_skill(str(skill_dir))
    if result.errors:
        print(f"error: '{skill}' not done — linter found {len(result.errors)} error(s):",
              file=sys.stderr)
        for e in result.errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    TASKS_PATH.write_text(set_status(text, skill, "done"), encoding="utf-8")
    print(f"{skill} -> done")
    return 0


COMMANDS = {"next": cmd_next, "progress": cmd_progress, "scaffold": cmd_scaffold, "context": cmd_context, "wip": cmd_wip, "done": cmd_done}


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in COMMANDS:
        print(f"usage: skillkit.py {{{'|'.join(COMMANDS)}}} [skill]", file=sys.stderr)
        return 2
    return COMMANDS[argv[0]](argv[1:])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
