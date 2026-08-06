#!/usr/bin/env python3
"""
product-on-steroids — Structural Skill Linter
=============================================
Validates every plugin/skill against this marketplace's house standard
(docs/SKILL-STANDARD.md). Blocking checks (errors) fail CI; warnings are advisory.

Checks:
- plugin.json: required fields, name == directory, semver.
- SKILL.md frontmatter: name (== directory), description, version, type, source.
    * type in {component, interactive, workflow}
    * source is "original" or "import:<repo>@<sha>"
- SKILL.md body: required sections "## Output Contract" and "## Validation & Eval".
- evals/: at least 3 scenario cards; each card has id, skill (== skill name),
    a non-empty `expected` list, and a non-empty `rubric` map.

Forked from phuryn/pm-skills validate_plugins.py (MIT, © Paweł Huryn) and
extended for the house standard. No third-party dependencies (self-contained
YAML-frontmatter parser — PyYAML is not required).
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Optional


# ─── Configuration ───────────────────────────────────────────────────────────

REQUIRED_MANIFEST_FIELDS = ["name", "version", "description"]
REQUIRED_SKILL_FIELDS = ["name", "description", "version", "type", "source"]
VALID_SKILL_TYPES = {"component", "interactive", "workflow"}
SOURCE_RE = re.compile(r"^(original|import:[\w.\-]+/[\w.\-]+@[\w.\-]+)$")
REQUIRED_BODY_SECTIONS = ["## Output Contract", "## Validation & Eval"]
MIN_EVAL_CARDS = 3


# ─── ANSI Colors ─────────────────────────────────────────────────────────────

class C:
    RED = "\033[91m"; GREEN = "\033[92m"; YELLOW = "\033[93m"
    CYAN = "\033[96m"; BOLD = "\033[1m"; DIM = "\033[2m"; RESET = "\033[0m"


# ─── Frontmatter parser (indentation-aware; scalars, folded/literal, lists, maps) ──

def parse_frontmatter(content: str) -> Optional[dict]:
    """Parse YAML frontmatter between the leading --- markers.

    Supports the subset this repo uses: `key: value`, folded/literal blocks
    (`key: >` / `key: |`), block lists (`- item`), and one level of nested maps.
    """
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    body = content[3:end].strip("\n")
    lines = body.split("\n")

    result: dict = {}
    i = 0
    while i < len(lines):
        raw = lines[i]
        if not raw.strip() or raw.strip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^(\S[^:]*):\s*(.*)$", raw)
        if not m:
            i += 1
            continue
        key, val = m.group(1).strip(), m.group(2).strip()

        if val in (">", "|", ">-", "|-"):  # folded / literal block scalar
            block, i = [], i + 1
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                if lines[i].strip():
                    block.append(lines[i].strip())
                i += 1
            result[key] = " ".join(block)
            continue

        if val == "":  # nested list or map on following indented lines
            i += 1
            items, nested = [], {}
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or not lines[i].strip()):
                if not lines[i].strip():
                    i += 1
                    continue
                s = lines[i].strip()
                if s.startswith("- "):
                    items.append(s[2:].strip().strip('"').strip("'"))
                else:
                    nm = re.match(r"^(\S[^:]*):\s*(.*)$", s)
                    if nm:
                        nested[nm.group(1).strip()] = nm.group(2).strip().strip('"').strip("'")
                i += 1
            result[key] = items if items else (nested if nested else "")
            continue

        result[key] = val.strip('"').strip("'")
        i += 1
    return result


# ─── Result container ────────────────────────────────────────────────────────

class ValidationResult:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def error(self, m): self.errors.append(m)
    def warn(self, m): self.warnings.append(m)
    def note(self, m): self.info.append(m)

    @property
    def ok(self) -> bool:
        return not self.errors


# ─── Validators ──────────────────────────────────────────────────────────────

def validate_manifest(plugin_dir: str) -> ValidationResult:
    r = ValidationResult()
    pj = os.path.join(plugin_dir, ".claude-plugin", "plugin.json")
    if not os.path.isfile(pj):
        r.error("Missing .claude-plugin/plugin.json")
        return r
    try:
        with open(pj) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        r.error(f"Invalid JSON in plugin.json: {e}")
        return r
    for field in REQUIRED_MANIFEST_FIELDS:
        if not data.get(field):
            r.error(f"plugin.json missing required field: {field}")
    dir_name = os.path.basename(plugin_dir)
    if data.get("name") and data["name"] != dir_name:
        r.error(f"plugin.json name '{data['name']}' != directory '{dir_name}'")
    version = data.get("version", "")
    if version and not re.match(r"^\d+\.\d+\.\d+$", version):
        r.warn(f"version '{version}' is not semver (x.y.z)")
    return r


def validate_skill(skill_dir: str) -> ValidationResult:
    r = ValidationResult()
    name = os.path.basename(skill_dir)
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        r.error("Missing SKILL.md")
        return r
    content = Path(skill_md).read_text(encoding="utf-8")

    fm = parse_frontmatter(content)
    if fm is None:
        r.error("Missing YAML frontmatter (must start with ---)")
        return r
    for field in REQUIRED_SKILL_FIELDS:
        if not fm.get(field):
            r.error(f"frontmatter missing required field: {field}")
    if fm.get("name") and fm["name"] != name:
        r.error(f"frontmatter name '{fm['name']}' != directory '{name}'")
    if fm.get("type") and fm["type"] not in VALID_SKILL_TYPES:
        r.error(f"type '{fm['type']}' invalid (use: {', '.join(sorted(VALID_SKILL_TYPES))})")
    if fm.get("source") and not SOURCE_RE.match(str(fm["source"])):
        r.error(f"source '{fm['source']}' invalid (use 'original' or 'import:<owner>/<repo>@<sha>')")
    desc = fm.get("description", "")
    if desc and not any(k in desc.lower() for k in ("use when", "trigger", "use for")):
        r.warn("description lacks trigger phrase ('Use when ...')")

    # Required body sections (case-insensitive)
    low = content.lower()
    for section in REQUIRED_BODY_SECTIONS:
        if section.lower() not in low:
            r.error(f"missing required section: '{section}'")

    # Eval cards
    r_evals = validate_evals(skill_dir, name)
    r.errors += r_evals.errors
    r.warnings += r_evals.warnings
    r.info += r_evals.info

    # Template
    r_tpl = validate_template(skill_dir, content)
    r.errors += r_tpl.errors
    r.warnings += r_tpl.warnings
    return r


def validate_evals(skill_dir: str, skill_name: str) -> ValidationResult:
    r = ValidationResult()
    evals_dir = os.path.join(skill_dir, "evals")
    if not os.path.isdir(evals_dir):
        r.error("Missing evals/ directory (need >= 3 scenario cards)")
        return r
    cards = sorted(p for p in os.listdir(evals_dir) if p.endswith(".md"))
    if len(cards) < MIN_EVAL_CARDS:
        r.error(f"only {len(cards)} eval card(s); need >= {MIN_EVAL_CARDS} (happy + edge + adversarial)")
    seen_ids = set()
    for card in cards:
        fm = parse_frontmatter(Path(evals_dir, card).read_text(encoding="utf-8"))
        if fm is None:
            r.error(f"evals/{card}: missing frontmatter")
            continue
        cid = fm.get("id")
        if not cid:
            r.error(f"evals/{card}: missing 'id'")
        elif cid in seen_ids:
            r.error(f"evals/{card}: duplicate id '{cid}'")
        else:
            seen_ids.add(cid)
        if fm.get("skill") and fm["skill"] != skill_name:
            r.error(f"evals/{card}: skill '{fm['skill']}' != '{skill_name}'")
        if not isinstance(fm.get("expected"), list) or not fm.get("expected"):
            r.error(f"evals/{card}: 'expected' must be a non-empty list")
        if not isinstance(fm.get("rubric"), dict) or not fm.get("rubric"):
            r.error(f"evals/{card}: 'rubric' must be a non-empty map")
    r.note(f"{len(cards)} eval card(s)")
    return r


def _output_contract_item_count(content: str) -> int:
    """Count numbered items under the '## Output Contract' section."""
    low = content.lower()
    start = low.find("## output contract")
    if start == -1:
        return 0
    rest = content[start:]
    nxt = re.search(r"\n##\s", rest[3:])   # next level-2 heading
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
    if references and exists and body:
        headings = len(re.findall(r"(?m)^##\s", body))
        items = _output_contract_item_count(content)
        if items and headings < items:
            r.warn(f"template.md has {headings} '##' headings but the Output "
                   f"Contract lists {items} sections — headings should mirror them")
    return r


# ─── Reporting ───────────────────────────────────────────────────────────────

def print_result(vr: ValidationResult, indent: int):
    p = " " * indent
    for e in vr.errors:
        print(f"{p}{C.RED}✗ ERROR:{C.RESET} {e}")
    for w in vr.warnings:
        print(f"{p}{C.YELLOW}⚠ WARN:{C.RESET}  {w}")


def validate_plugin(plugin_dir: str) -> dict:
    res = {"name": os.path.basename(plugin_dir), "manifest": validate_manifest(plugin_dir), "skills": {}}
    skills_dir = os.path.join(plugin_dir, "skills")
    if os.path.isdir(skills_dir):
        for s in sorted(os.listdir(skills_dir)):
            sp = os.path.join(skills_dir, s)
            if os.path.isdir(sp):
                res["skills"][s] = validate_skill(sp)
    return res


def _default_base() -> str:
    """Repo root relative to this file when run in-tree; otherwise the CWD
    (so the installed `validate-plugins` console script scans the current repo)."""
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        if any(os.path.isdir(os.path.join(here, e, ".claude-plugin")) for e in os.listdir(here)):
            return here
    except OSError:
        pass
    return os.getcwd()


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else _default_base()
    if not os.path.isdir(base):
        print(f"Error: {base} is not a directory")
        sys.exit(2)

    plugin_dirs = [
        os.path.join(base, e) for e in sorted(os.listdir(base))
        if os.path.isdir(os.path.join(base, e, ".claude-plugin"))
    ]
    if not plugin_dirs:
        print(f"No plugins found in {base}")
        sys.exit(1)

    print(f"\n{C.BOLD}{'='*60}\n product-on-steroids — Skill Linter\n{'='*60}{C.RESET}\n")
    total_errors = total_warnings = total_skills = 0

    for pd in plugin_dirs:
        res = validate_plugin(pd)
        p_err = len(res["manifest"].errors) + sum(len(v.errors) for v in res["skills"].values())
        p_warn = len(res["manifest"].warnings) + sum(len(v.warnings) for v in res["skills"].values())
        total_errors += p_err
        total_warnings += p_warn
        total_skills += len(res["skills"])
        status = f"{C.GREEN}✓ PASS{C.RESET}" if p_err == 0 else f"{C.RED}✗ FAIL{C.RESET}"
        print(f"{C.BOLD}{C.CYAN}┌─ {res['name']}{C.RESET}  [{len(res['skills'])} skills]  {status}")
        if res["manifest"].errors or res["manifest"].warnings:
            print("  Manifest:")
            print_result(res["manifest"], 4)
        for sname, vr in res["skills"].items():
            if vr.errors or vr.warnings:
                print(f"  {sname}:")
                print_result(vr, 4)
        print(f"{C.CYAN}└{'─'*59}{C.RESET}\n")

    print(f"{C.BOLD}Summary{C.RESET}: {len(plugin_dirs)} plugins, {total_skills} skills")
    if total_errors == 0:
        print(f"{C.GREEN}{C.BOLD}✓ ALL CHECKS PASSED{C.RESET} ({total_warnings} warnings)\n")
    else:
        print(f"{C.RED}{C.BOLD}✗ {total_errors} ERRORS{C.RESET}, {total_warnings} warnings\n")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
