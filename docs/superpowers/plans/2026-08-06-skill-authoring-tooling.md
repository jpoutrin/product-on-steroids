# Skill-Authoring Tooling Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a stdlib-only CLI (`scripts/skillkit.py`) + `just` recipes + a linter extension + a PostToolUse hook that cut the per-skill token cost of authoring the ~100 remaining `TASKS.md` skills and make malformed skills impossible to commit.

**Architecture:** One consolidated CLI parses `TASKS.md` and exposes `next / scaffold / context / wip / done / progress`, wired as `just` recipes. Pure helper functions (parse, select, status-edit, pack-build) are unit-tested; thin CLI wrappers do I/O. The existing linter (`tests/validate_plugins.py`) gains a `template.md` check and is auto-run on skill edits via a committed `.claude/settings.json` hook.

**Tech Stack:** Python 3.10+ stdlib only, `uv` (venv + run), `just` (task runner), `pytest` (dev dependency, already present).

## Global Constraints

- **No new runtime dependencies.** Python **stdlib only** for all scripts. `pyproject.toml` `dependencies = []` stays empty; `pytest` stays the only dev dep.
- **Python floor:** `requires-python = ">=3.10"` (type hints like `list[str]` are fine).
- **Pinned phuryn SHA:** `18468a9` — scaffold writes `source: import:phuryn/pm-skills@18468a9` for IMPORT rows, `source: original` for GENERATE. Never invent a different SHA.
- **Source-name alias:** exactly one IMPORT name differs from its phuryn source dir: `product-strategy-canvas → product-strategy`. All other 63 imports match 1:1.
- **Build order:** `pm-strategy → pm-discovery → pm-gtm → pm-execution → pm-influence`, P1 before P2 before P3 within a plugin.
- **Provenance:** never copy text from `deanpeters` (CC BY-NC-SA); GENERATE skills are original. IMPORT adapts phuryn (MIT).
- **Commits:** one logical change per commit, conventional messages. The repo owner normally commits via their git-workflow skill; if executing manually, use the messages given in each task.
- **Frontmatter parser reuse:** import `parse_frontmatter` / `validate_skill` from `validate_plugins` rather than re-implementing.

---

### Task 1: `skillkit.py` core — TASKS parser, `next`, `progress`

**Files:**
- Create: `scripts/skillkit.py`
- Create: `tests/conftest.py`
- Test: `tests/test_skillkit_parse.py`

**Interfaces:**
- Produces: `load_tasks(text: str) -> list[dict]` where each dict has keys
  `skill, plugin, disposition, priority, status, line_no` (0-based index into `text.splitlines()`).
  `select_next(tasks: list[dict]) -> dict | None`.
  `progress_report(tasks: list[dict]) -> str`.
  Module constants `PHURYN_SHA`, `SOURCE_ALIAS`, `BUILD_ORDER`, `PRIORITY_ORDER`,
  `REPO_ROOT`, `TASKS_PATH`, `TEMPLATE_DIR`, `BRIEF_PATH`, `PHURYN_ROOT`.

- [ ] **Step 1: Write `tests/conftest.py`** so tests can import the script.

```python
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))   # import skillkit
sys.path.insert(0, str(ROOT / "tests"))      # import validate_plugins in-tree
```

- [ ] **Step 2: Write the failing test** `tests/test_skillkit_parse.py`

```python
import skillkit

FIXTURE = """\
## pm-strategy — Product Strategy

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| market-sizing | IMPORT | P1 | done |
| product-vision | IMPORT | P1 | todo |
| roadmap-planning | GENERATE | P1 | todo |
| lean-canvas | IMPORT | P2 | todo |

## pm-discovery — Customer Insight

| Skill | Disposition | Priority | Status |
|-------|-------------|----------|--------|
| interview-script | IMPORT | P1 | todo |

## Cross-cutting

| Item | Disposition | Priority | Status |
|------|-------------|----------|--------|
| workshop-facilitation (shared) | GENERATE | P1 | todo |
"""

def test_load_tasks_extracts_plugin_rows_only():
    tasks = skillkit.load_tasks(FIXTURE)
    names = [t["skill"] for t in tasks]
    assert names == [
        "market-sizing", "product-vision", "roadmap-planning",
        "lean-canvas", "interview-script",
    ]  # Cross-cutting row excluded (no pm- plugin)
    ms = tasks[0]
    assert ms["plugin"] == "pm-strategy"
    assert ms["disposition"] == "IMPORT"
    assert ms["priority"] == "P1"
    assert ms["status"] == "done"

def test_select_next_skips_done_and_respects_priority():
    tasks = skillkit.load_tasks(FIXTURE)
    nxt = skillkit.select_next(tasks)
    assert nxt["skill"] == "product-vision"  # first todo, P1, pm-strategy

def test_progress_report_counts():
    report = skillkit.progress_report(skillkit.load_tasks(FIXTURE))
    assert "pm-strategy" in report
    assert "1/4 done" in report  # 1 done of 4 pm-strategy skills
```

- [ ] **Step 3: Run test to verify it fails**

Run: `uv run pytest tests/test_skillkit_parse.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'skillkit'`

- [ ] **Step 4: Write `scripts/skillkit.py`** (core only)

```python
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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_skillkit_parse.py -v`
Expected: PASS (3 tests)

- [ ] **Step 6: Smoke-test against the real ledger**

Run: `uv run python scripts/skillkit.py next` then `uv run python scripts/skillkit.py progress`
Expected: `next` prints `product-vision   IMPORT  pm-strategy  P1`; `progress` shows `pm-strategy 1/37 done` and a `TOTAL` line.

- [ ] **Step 7: Commit**

```bash
git add scripts/skillkit.py tests/conftest.py tests/test_skillkit_parse.py
git commit -m "feat(tooling): skillkit core — TASKS parser, next, progress"
```

---

### Task 2: `scaffold` — generate a skill dir from a TASKS row

**Files:**
- Modify: `scripts/skillkit.py` (add `find_task`, `import_source`, `cmd_scaffold`; register command)
- Test: `tests/test_skillkit_scaffold.py`

**Interfaces:**
- Consumes: `load_tasks`, module constants from Task 1.
- Produces: `find_task(tasks, skill) -> dict` (raises `KeyError` if absent).
  `import_source(disposition, skill) -> str` returning the frontmatter `source` value.
  `cmd_scaffold(args)` creating `<plugin>/skills/<skill>/`.

- [ ] **Step 1: Write the failing test** `tests/test_skillkit_scaffold.py`

```python
import shutil
import skillkit

def test_import_source_values():
    assert skillkit.import_source("GENERATE", "roadmap-planning") == "original"
    assert skillkit.import_source("IMPORT", "product-vision") == \
        "import:phuryn/pm-skills@18468a9"

def test_scaffold_creates_filled_skill(tmp_path, monkeypatch):
    # Redirect the repo layout into tmp_path
    monkeypatch.setattr(skillkit, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(skillkit, "TASKS_PATH", tmp_path / "TASKS.md")
    tmpl = tmp_path / "docs" / "skill-template"
    monkeypatch.setattr(skillkit, "TEMPLATE_DIR", tmpl)
    # Minimal template mirroring docs/skill-template/
    (tmpl / "evals").mkdir(parents=True)
    (tmpl / "SKILL.md").write_text(
        "---\nname: skill-name\nversion: 0.1.0\ntype: component\nsource: original\n---\n# T\n")
    (tmpl / "template.md").write_text("# <Artifact Title>\n## <Section 1>\n")
    (tmpl / "evals" / "example.md").write_text(
        "---\nid: skill-name-happy\nskill: skill-name\n---\nnote\n")
    (tmp_path / "TASKS.md").write_text(
        "## pm-strategy — X\n\n| Skill | Disposition | Priority | Status |\n"
        "|--|--|--|--|\n| product-vision | IMPORT | P1 | todo |\n")

    rc = skillkit.cmd_scaffold(["product-vision"])
    assert rc == 0
    dest = tmp_path / "pm-strategy" / "skills" / "product-vision"
    skill_md = (dest / "SKILL.md").read_text()
    assert "name: product-vision" in skill_md
    assert "source: import:phuryn/pm-skills@18468a9" in skill_md
    evals = sorted(p.name for p in (dest / "evals").iterdir())
    assert evals == ["product-vision-adversarial.md",
                     "product-vision-edge.md", "product-vision-happy.md"]
    happy = (dest / "evals" / "product-vision-happy.md").read_text()
    assert "id: product-vision-happy" in happy
    assert "skill: product-vision" in happy
    assert not (dest / "evals" / "example.md").exists()

def test_scaffold_refuses_existing(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(skillkit, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(skillkit, "TASKS_PATH", tmp_path / "TASKS.md")
    (tmp_path / "TASKS.md").write_text(
        "## pm-strategy — X\n\n| Skill | Disposition | Priority | Status |\n"
        "|--|--|--|--|\n| product-vision | IMPORT | P1 | todo |\n")
    dest = tmp_path / "pm-strategy" / "skills" / "product-vision"
    dest.mkdir(parents=True)
    rc = skillkit.cmd_scaffold(["product-vision"])
    assert rc == 1
    assert "exists" in capsys.readouterr().err
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_skillkit_scaffold.py -v`
Expected: FAIL with `AttributeError: module 'skillkit' has no attribute 'import_source'`

- [ ] **Step 3: Add to `scripts/skillkit.py`** (above `COMMANDS`)

```python
import shutil

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
    skill_md.write_text(text, encoding="utf-8")

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
```

- [ ] **Step 4: Register the command** — change the `COMMANDS` dict:

```python
COMMANDS = {"next": cmd_next, "progress": cmd_progress, "scaffold": cmd_scaffold}
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_skillkit_scaffold.py -v`
Expected: PASS (3 tests)

- [ ] **Step 6: Commit**

```bash
git add scripts/skillkit.py tests/test_skillkit_scaffold.py
git commit -m "feat(tooling): skillkit scaffold — generate skill dir from ledger row"
```

---

### Task 3: `context` + `docs/SKILL-BRIEF.md` — the one-command build pack

**Files:**
- Create: `docs/SKILL-BRIEF.md`
- Modify: `scripts/skillkit.py` (add `phuryn_source_path`, `build_pack`, `cmd_context`; register)
- Test: `tests/test_skillkit_context.py`

**Interfaces:**
- Consumes: `find_task`, `load_tasks`, `SOURCE_ALIAS`, `PHURYN_ROOT`, `BRIEF_PATH`.
- Produces: `phuryn_source_path(skill) -> Path | None`.
  `build_pack(task, brief, source_text) -> str` (pure; `source_text` is the phuryn
  SKILL.md text for IMPORT, else `None`).
  `cmd_context(args)`.

- [ ] **Step 1: Write `docs/SKILL-BRIEF.md`** — the embedded cheat-sheet (keep it ~40 lines)

```markdown
# SKILL-BRIEF — build one skill fast

Operational quick-reference. Authoritative long-form: `docs/SKILL-STANDARD.md`.
Gold exemplar (read once per session, not per skill):
`pm-strategy/skills/market-sizing/SKILL.md`.

## Frontmatter (all required)
- `name`: kebab-case == directory name
- `description`: `>` block; MUST contain a trigger phrase ("Use when …")
- `version`: `0.1.0` (semver)
- `type`: `component` | `interactive` | `workflow`
- `source`: `original` or `import:phuryn/pm-skills@<sha>` (scaffold pre-fills this)

## Required body sections
- `## Purpose` (+ a **When NOT to use**)
- `## Inputs` (required vs optional; how to elicit if missing)
- `## Output Contract` ⭐ linter-checked — sections + format/length + a GOOD and a BAD excerpt
- `## Process` (numbered; last step = run the Quality Bar)
- `## Quality Bar` (checkbox self-check run before returning)
- `## Validation & Eval` ⭐ linter-checked — points at evals/, states pass bar (≥0.8; −0.05 regression fails)
- `## References`

## template.md
Required when the Output Contract is a structured artifact. `##` headings mirror
the Output Contract sections. Fill it — don't leave scaffold placeholders.

## evals/ (≥ 3 cards: happy + edge + adversarial)
Each card frontmatter: unique `id`, `skill` (== skill name), non-empty `expected`
list, non-empty `rubric` map (weights sum to 1.0).

## IMPORT vs GENERATE
- IMPORT: adapt the phuryn source below (MIT). Restructure into the sections above;
  add Output Contract GOOD/BAD, Quality Bar, evals. Keep `source` SHA as scaffolded.
- GENERATE: write original. `deanpeters` is idea-reference only — never copy its text.

## Done
`just test` passes (or the edit hook is green) AND ≥3 eval cards → `just done <skill>`.
```

- [ ] **Step 2: Write the failing test** `tests/test_skillkit_context.py`

```python
import skillkit

TASK_IMPORT = {"skill": "product-vision", "plugin": "pm-strategy",
               "disposition": "IMPORT", "priority": "P1", "status": "todo", "line_no": 4}
TASK_GEN = {"skill": "roadmap-planning", "plugin": "pm-strategy",
            "disposition": "GENERATE", "priority": "P1", "status": "todo", "line_no": 5}

def test_build_pack_import_includes_source():
    pack = skillkit.build_pack(TASK_IMPORT, "BRIEF-BODY", "PHURYN-SOURCE-TEXT")
    assert "BRIEF-BODY" in pack
    assert "product-vision" in pack
    assert "PHURYN-SOURCE-TEXT" in pack
    assert "IMPORT" in pack

def test_build_pack_generate_has_reminder_no_source():
    pack = skillkit.build_pack(TASK_GEN, "BRIEF-BODY", None)
    assert "original" in pack.lower()
    assert "deanpeters" in pack.lower()

def test_alias_resolves_product_strategy_canvas():
    # even without the work/ repo present, the resolver applies the alias to the name
    assert skillkit.SOURCE_ALIAS["product-strategy-canvas"] == "product-strategy"
```

- [ ] **Step 3: Run test to verify it fails**

Run: `uv run pytest tests/test_skillkit_context.py -v`
Expected: FAIL with `AttributeError: module 'skillkit' has no attribute 'build_pack'`

- [ ] **Step 4: Add to `scripts/skillkit.py`**

```python
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
```

- [ ] **Step 5: Register the command**

```python
COMMANDS = {"next": cmd_next, "progress": cmd_progress,
            "scaffold": cmd_scaffold, "context": cmd_context}
```

- [ ] **Step 6: Run tests + real smoke test**

Run: `uv run pytest tests/test_skillkit_context.py -v`
Expected: PASS (3 tests)
Run: `uv run python scripts/skillkit.py context product-vision | head -40`
Expected: prints the brief, the row, and the phuryn `product-vision` source text.

- [ ] **Step 7: Commit**

```bash
git add docs/SKILL-BRIEF.md scripts/skillkit.py tests/test_skillkit_context.py
git commit -m "feat(tooling): skillkit context pack + SKILL-BRIEF cheat-sheet"
```

---

### Task 4: `wip` / `done` — ledger status with a lint gate

**Files:**
- Modify: `scripts/skillkit.py` (add `set_status`, `cmd_wip`, `cmd_done`; register)
- Test: `tests/test_skillkit_status.py`

**Interfaces:**
- Consumes: `find_task`, `load_tasks`, and `validate_skill` (imported from `validate_plugins`).
- Produces: `set_status(text: str, skill: str, status: str) -> str` (pure; raises
  `KeyError` if the row is absent). `cmd_wip(args)`, `cmd_done(args)`.

- [ ] **Step 1: Write the failing test** `tests/test_skillkit_status.py`

```python
import pytest
import skillkit

LEDGER = ("## pm-strategy — X\n\n| Skill | Disposition | Priority | Status |\n"
          "|--|--|--|--|\n| product-vision | IMPORT | P1 | todo |\n")

def test_set_status_flips_only_target_row():
    out = skillkit.set_status(LEDGER, "product-vision", "wip")
    assert "| product-vision | IMPORT | P1 | wip |" in out
    assert out.count("wip") == 1

def test_set_status_unknown_raises():
    with pytest.raises(KeyError):
        skillkit.set_status(LEDGER, "nope", "wip")

def test_done_refuses_when_lint_fails(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(skillkit, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(skillkit, "TASKS_PATH", tmp_path / "TASKS.md")
    (tmp_path / "TASKS.md").write_text(LEDGER)
    skilldir = tmp_path / "pm-strategy" / "skills" / "product-vision"
    (skilldir / "evals").mkdir(parents=True)
    (skilldir / "SKILL.md").write_text("---\nname: product-vision\n---\nincomplete\n")
    rc = skillkit.cmd_done(["product-vision"])
    assert rc == 1
    assert "not done" in capsys.readouterr().err.lower()
    # status must NOT have flipped
    assert "| product-vision | IMPORT | P1 | todo |" in (tmp_path / "TASKS.md").read_text()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_skillkit_status.py -v`
Expected: FAIL with `AttributeError: module 'skillkit' has no attribute 'set_status'`

- [ ] **Step 3: Add to `scripts/skillkit.py`** (near the top add the import; add functions above `COMMANDS`)

```python
# add with the other imports at the top of the file:
try:
    from validate_plugins import validate_skill
except ImportError:  # in-tree fallback when not installed as a module
    sys.path.insert(0, str(REPO_ROOT / "tests"))
    from validate_plugins import validate_skill
```

```python
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
```

- [ ] **Step 4: Register the commands**

```python
COMMANDS = {"next": cmd_next, "progress": cmd_progress, "scaffold": cmd_scaffold,
            "context": cmd_context, "wip": cmd_wip, "done": cmd_done}
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_skillkit_status.py -v`
Expected: PASS (3 tests). `validate_skill` errors on the incomplete SKILL.md (missing sections + <3 evals), so `done` refuses.

- [ ] **Step 6: Full suite green**

Run: `uv run pytest -q`
Expected: all tests pass.

- [ ] **Step 7: Commit**

```bash
git add scripts/skillkit.py tests/test_skillkit_status.py
git commit -m "feat(tooling): skillkit wip/done with linter gate on done"
```

---

### Task 5: Wire `just` recipes

**Files:**
- Modify: `justfile`

**Interfaces:**
- Consumes: `scripts/skillkit.py` CLI from Tasks 1–4.

- [ ] **Step 1: Append recipes to `justfile`**

```make
# ── Skill authoring (token-lean helpers; see docs/SKILL-BRIEF.md) ──

# Print the next todo skill in build order
next:
    uv run python scripts/skillkit.py next

# Show build progress per plugin
progress:
    uv run python scripts/skillkit.py progress

# Scaffold a skill dir from its TASKS.md row: just scaffold market-sizing
scaffold skill:
    uv run python scripts/skillkit.py scaffold {{skill}}

# Print the one-shot build pack for a skill: just context market-sizing
context skill:
    uv run python scripts/skillkit.py context {{skill}}

# Mark a skill in-progress in TASKS.md
wip skill:
    uv run python scripts/skillkit.py wip {{skill}}

# Mark a skill done (runs the linter gate first)
done skill:
    uv run python scripts/skillkit.py done {{skill}}
```

- [ ] **Step 2: Verify recipes resolve**

Run: `just --list`
Expected: shows `next`, `progress`, `scaffold`, `context`, `wip`, `done` alongside `setup`/`test`.
Run: `just next`
Expected: `product-vision   IMPORT  pm-strategy  P1`

- [ ] **Step 3: Commit**

```bash
git add justfile
git commit -m "build: just recipes for skillkit (next/scaffold/context/wip/done/progress)"
```

---

### Task 6: Linter extension — enforce `template.md` layout

**Files:**
- Modify: `tests/validate_plugins.py` (add `validate_template`, call it from `validate_skill`)
- Test: `tests/test_template_check.py`

**Interfaces:**
- Consumes: `ValidationResult`, `validate_skill` from `validate_plugins`.
- Produces: `validate_template(skill_dir, content) -> ValidationResult` where `content`
  is the SKILL.md text. Error if the body references `template.md` but the file is
  missing/empty; warn if `template.md` has fewer `##` headings than the Output
  Contract has numbered items.

- [ ] **Step 1: Write the failing test** `tests/test_template_check.py`

```python
import validate_plugins as vp

SKILL_WITH_TEMPLATE = (
    "---\nname: x\n---\n## Output Contract\n"
    "1. **A** — a\n2. **B** — b\nSee `template.md`.\n## Validation & Eval\n")

def _mk(tmp_path, skill_md, template_md=None):
    d = tmp_path / "x"
    (d / "evals").mkdir(parents=True)
    (d / "SKILL.md").write_text(skill_md)
    if template_md is not None:
        (d / "template.md").write_text(template_md)
    return str(d)

def test_missing_template_when_referenced_is_error(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE, template_md=None)
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert any("template.md" in e for e in r.errors)

def test_empty_template_is_error(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE, template_md="   \n")
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert any("template.md" in e for e in r.errors)

def test_fewer_headings_than_contract_warns(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE, template_md="# T\n## A\n")  # 1 heading, 2 items
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert not r.errors
    assert any("Output Contract" in w for w in r.warnings)

def test_no_template_reference_is_silent(tmp_path):
    skill = "---\nname: x\n---\n## Output Contract\nAdvisory only.\n## Validation & Eval\n"
    d = _mk(tmp_path, skill, template_md=None)
    r = vp.validate_template(d, skill)
    assert not r.errors and not r.warnings
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_template_check.py -v`
Expected: FAIL with `AttributeError: module 'validate_plugins' has no attribute 'validate_template'`

- [ ] **Step 3: Add `validate_template` to `tests/validate_plugins.py`** (after `validate_evals`)

```python
def _output_contract_item_count(content: str) -> int:
    """Count numbered items under the '## Output Contract' section."""
    low = content.lower()
    start = low.find("## output contract")
    if start == -1:
        return 0
    rest = content[start:]
    nxt = re.search(r"\n##\s", rest[3:])   # next top-level heading
    section = rest[: nxt.start() + 3] if nxt else rest
    return len(re.findall(r"(?m)^\d+\.\s+\*\*", section))


def validate_template(skill_dir: str, content: str) -> ValidationResult:
    r = ValidationResult()
    references = "template.md" in content
    tpath = os.path.join(skill_dir, "template.md")
    exists = os.path.isfile(tpath)
    body = Path(tpath).read_text(encoding="utf-8").strip() if exists else ""
    if references and (not exists or not body):
        r.error("body references template.md but it is missing or empty")
        return r
    if exists and body:
        headings = len(re.findall(r"(?m)^##\s", body))
        items = _output_contract_item_count(content)
        if items and headings < items:
            r.warn(f"template.md has {headings} '##' headings but the Output "
                   f"Contract lists {items} sections — headings should mirror them")
    return r
```

- [ ] **Step 4: Call it from `validate_skill`** — in `tests/validate_plugins.py`, just before `return r` in `validate_skill`, add:

```python
    r_tpl = validate_template(skill_dir, content)
    r.errors += r_tpl.errors
    r.warnings += r_tpl.warnings
```

- [ ] **Step 5: Run tests + full-repo lint**

Run: `uv run pytest tests/test_template_check.py -v`
Expected: PASS (4 tests)
Run: `just test`
Expected: still `✓ ALL CHECKS PASSED` — `market-sizing` references and ships a filled `template.md` with headings mirroring its contract, so no new errors/warnings on it.

- [ ] **Step 6: Commit**

```bash
git add tests/validate_plugins.py tests/test_template_check.py
git commit -m "feat(linter): enforce template.md presence + heading parity"
```

---

### Task 7: PostToolUse validation hook

**Files:**
- Create: `scripts/validate_one.py`
- Create: `.claude/settings.json`
- Test: `tests/test_validate_one.py`

**Interfaces:**
- Consumes: `validate_skill` from `validate_plugins`.
- Produces: `skill_dir_for(path: str) -> str | None` (walk up to the dir containing a
  SKILL.md sibling). `run(stdin_json: dict) -> int` (always returns 0 — fail-open).

- [ ] **Step 1: Write the failing test** `tests/test_validate_one.py`

```python
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import validate_one

def test_skill_dir_for_finds_enclosing_skill(tmp_path):
    d = tmp_path / "pm-x" / "skills" / "foo"
    (d / "evals").mkdir(parents=True)
    (d / "SKILL.md").write_text("---\nname: foo\n---\n")
    assert validate_one.skill_dir_for(str(d / "SKILL.md")) == str(d)
    assert validate_one.skill_dir_for(str(d / "evals" / "foo-happy.md")) == str(d)

def test_skill_dir_for_ignores_unrelated_path(tmp_path):
    p = tmp_path / "README.md"
    p.write_text("x")
    assert validate_one.skill_dir_for(str(p)) is None

def test_run_is_fail_open_on_garbage():
    assert validate_one.run({}) == 0
    assert validate_one.run({"tool_input": {"file_path": "/nope/x.md"}}) == 0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_validate_one.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'validate_one'`

- [ ] **Step 3: Write `scripts/validate_one.py`**

```python
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
```

- [ ] **Step 4: Write `.claude/settings.json`** (committed, repo-level)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "uv run --project \"$CLAUDE_PROJECT_DIR\" python \"$CLAUDE_PROJECT_DIR/scripts/validate_one.py\""
          }
        ]
      }
    ]
  }
}
```

- [ ] **Step 5: Run tests + a manual pipe check**

Run: `uv run pytest tests/test_validate_one.py -v`
Expected: PASS (3 tests)
Run: `echo '{"tool_input":{"file_path":"'$PWD'/pm-strategy/skills/market-sizing/SKILL.md"}}' | uv run python scripts/validate_one.py; echo "exit=$?"`
Expected: no error output (market-sizing is clean), `exit=0`.

- [ ] **Step 6: Commit**

```bash
git add scripts/validate_one.py .claude/settings.json tests/test_validate_one.py
git commit -m "feat(tooling): PostToolUse hook lints edited skills (fail-open)"
```

---

### Task 8: Document the workflow in CLAUDE.md

**Files:**
- Modify: `CLAUDE.md` (add subsection under "Authoring a skill")

**Interfaces:**
- Consumes: all recipes from Task 5; the hook from Task 7.

- [ ] **Step 1: Add this subsection** to `CLAUDE.md`, immediately after the
"Authoring a skill (the core workflow)" section's directory-layout block:

```markdown
### Efficient authoring workflow (token-lean)

Tooling lives in `scripts/skillkit.py`, exposed as `just` recipes. Use it instead of
re-reading the standard/exemplar every time — read `docs/SKILL-STANDARD.md` and the
gold exemplar **at most once per session**; `just context` carries the rest.

**Per-skill loop:**
1. `just next` — pick the next `todo` skill in build order.
2. `just scaffold <skill>` — generate the dir with frontmatter (incl. pinned `source`
   SHA), `template.md`, and three eval stubs. Idempotent; refuses to overwrite.
3. `just context <skill>` — print the one-shot build pack: the `SKILL-BRIEF` cheat-sheet,
   the ledger row, and (for IMPORT) the raw phuryn source to adapt. This replaces
   reading the standard + exemplar + template + hunting the source.
4. Author the skill (IMPORT = restructure/enrich phuryn into the house sections;
   GENERATE = original, `deanpeters` is idea-reference only).
5. `just test` (the PostToolUse hook also lints each SKILL.md/eval edit automatically).
6. `just done <skill>` — runs the linter gate, then flips the TASKS.md row to `done`.
7. Commit: `feat(<plugin>): <skill> skill`.

**Batch loop (parallel, keeps main context small):** skills are independent, so dispatch
**one subagent per skill** (`superpowers:dispatching-parallel-agents`). Each subagent
runs `just context <skill>` for its own tiny self-contained context, authors, validates,
`just done`s, and commits its single skill. The main thread never loads reference
material — that's where the savings compound.

`just progress` shows done/wip/todo per plugin at a glance.
```

- [ ] **Step 2: Verify the recipes named in the doc all exist**

Run: `just --list`
Expected: `next`, `scaffold`, `context`, `test`, `done`, `progress` all present (names match the doc).

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: efficient token-lean skill-authoring workflow"
```

---

## Self-Review

**Spec coverage** (against `2026-08-06-skill-authoring-tooling-design.md`):
- Component 1 (`skillkit.py`, 6 subcommands) → Tasks 1–4, recipes in Task 5. ✓
- Component 2 (`SKILL-BRIEF.md`) → Task 3. ✓
- Component 3 (linter `template.md` extension) → Task 6. ✓
- Component 4 (PostToolUse hook, committed `.claude/settings.json`) → Task 7. ✓
- Component 5 (CLAUDE.md workflow subsection, per-skill + batch loops) → Task 8. ✓
- Resolved decisions: scaffold auto-sets `source` (Task 2, `import_source`); `just done`
  enforces lint gate (Task 4, `cmd_done`); cheat-sheet is a new file embedded by
  `context` (Tasks 3); single consolidated CLI (Tasks 1–4). ✓
- Error handling from the spec: scaffold-on-existing (Task 2 test), skill-absent
  (Tasks 2/3/4), phuryn-source-missing (Task 3, `cmd_context`), done-refusal (Task 4),
  hook fail-open (Task 7). ✓

**Placeholder scan:** no "TBD/TODO/handle edge cases"; every code step is complete and
runnable; tests carry real assertions. ✓

**Type consistency:** `load_tasks` dict keys (`skill/plugin/disposition/priority/status/
line_no`) are used identically in `select_next`, `find_task`, `set_status`, `cmd_scaffold`,
`cmd_context`, `cmd_done`. `validate_skill(str)` returns an object with `.errors`/`.warnings`
(matches `validate_plugins.py`). `import_source(disposition, skill)`, `build_pack(task,
brief, source_text)`, `set_status(text, skill, status)`, `skill_dir_for(path)`,
`validate_template(skill_dir, content)` signatures are consistent between definition,
tests, and call sites. ✓
```
