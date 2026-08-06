#!/usr/bin/env python3
"""PostToolUse hook: lint the skill enclosing an edited SKILL.md / eval card.

Reads the hook JSON on stdin, finds the skill dir, runs the structural linter
scoped to it, and prints any errors. Fail-open: always exits 0 so authoring is
never blocked.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
try:
    from validate_plugins import validate_skill
except ImportError:
    sys.path.insert(0, str(REPO_ROOT / "tests"))
    from validate_plugins import validate_skill


def skill_dir_for(path: str) -> str | None:
    p = Path(path).resolve()
    for d in [p] + list(p.parents):
        if (d / "SKILL.md").is_file() and d.parent.name == "skills":
            return str(d)
    return None


def run(payload: dict) -> int:
    try:
        path = (payload.get("tool_input") or {}).get("file_path", "")
        if not path or Path(path).name != "SKILL.md" and "/evals/" not in path.replace(os.sep, "/"):
            return 0
        sdir = skill_dir_for(path)
        if not sdir:
            return 0
        result = validate_skill(sdir)
        if result.errors:
            name = Path(sdir).name
            print(f"⚠ skill lint ({name}): {len(result.errors)} error(s) — fix before `just done`:",
                  file=sys.stderr)
            for e in result.errors:
                print(f"  - {e}", file=sys.stderr)
    except Exception:
        pass  # never block an edit
    return 0


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    return run(payload)


if __name__ == "__main__":
    raise SystemExit(main())
