# Output Language Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let a consuming project declare `language: fr` in `.config/pm-skills.yaml` and get PM-skill deliverables in that language, without losing the structural conformance gate that today matches English heading text.

**Architecture:** Every `template.md` heading gains a language-independent HTML-comment anchor (`## Market Definition <!--#market-definition-->`). The PostToolUse conformance hook matches anchors instead of prose when the template carries any, falling back to today's text matching when it does not — so the migration is incremental and no skill is rewritten. A new plugin-level SessionStart hook reads `.config/pm-skills.yaml` and injects a one-paragraph language directive into the session, so the language rule lives in one place instead of in 110 `SKILL.md` files.

**Tech Stack:** Python 3.10+, stdlib only (hooks must run on an end user's machine with plain `python3`, no `uv`). `pytest` for tests, `uv` for the dev env, `just` as the task runner. No new dependencies.

**Spec:** `pm-skills-plan/pm-skills-output-language.md`

## Global Constraints

- **Stdlib only in hooks.** `scripts/skel/*.py` and every `pm-*/{scripts,hooks}/*.py` must import only the standard library and run under plain `python3` — no `uv`, no PyYAML. The repo hand-rolls its YAML parsing on purpose.
- **Fail open.** Any unexpected condition in a hook returns exit 0 and emits nothing. A hook must never block an edit or a session start.
- **Six copies stay byte-identical.** `scripts/skel/<file>` is canonical; `pm-strategy`, `pm-discovery`, `pm-gtm`, `pm-execution`, `pm-influence` each carry a copy. All six change in the same commit or the plugins diverge.
- **Slug rule (frozen once shipped):** lowercase the English heading text, replace every run of `[^a-z0-9]` with `-`, strip leading/trailing `-`; empty result becomes `section`. Within one template, a repeated slug gets `-2`, `-3`, … appended.
- **Anchor syntax:** `<!--#slug-->`, placed at the end of the heading line after a single space. Slug charset is `[a-z0-9-]` only.
- **Always English, in every project:** `SKILL.md` bodies, eval cards, `template.md` source, the linter, hooks, and `scripts/`. Only the produced deliverable is translated.
- **Untranslated PM jargon:** TAM/SAM/SOM, RICE, JTBD, NPS, ICP, OKR.
- **Only key in `.config/pm-skills.yaml` is `language`.** No other key is in scope.
- **Commit messages** end with `Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e`.
- **Every commit is green:** `just test` passes at every step.

## Deviations from the spec (deliberate, read before starting)

Three changes to the spec's rollout, made while planning:

1. **Task order.** The spec ordered the linter's anchor check (its commit 2) *before* the migration, landing it as a warning and promoting it to an error in commit 9. That would leave `just test` printing 816 warnings for the whole middle of the rollout. This plan runs the migration first and lands the linter check directly at **error** level afterwards, where it is immediately clean. Same nine commits, same end state, no warning window.
2. **Hook filename.** The spec says `hooks/session-start` (a bash script, mirroring superpowers). This plan uses `hooks/output_language.py` invoked as `python3 "${CLAUDE_PLUGIN_ROOT}/hooks/output_language.py"`. Python gives correct JSON escaping via `json.dumps` for free, matches the existing `check_output_conformance.py` hook, and keeps the "stdlib-only python3" constraint uniform. The emitted JSON shape (and its Cursor/Copilot fallbacks) is a faithful port of superpowers' `hooks/session-start`.
3. **`just test` now runs pytest too.** Today `just test` runs only the structural linter, so the `tests/*.py` suite is not in the gate — which would make the tests this plan adds decorative. Task 1 changes `just test` to run `pytest` and then the linter, and updates `CLAUDE.md` to match.

## File Structure

**Canonical hook sources** (`scripts/skel/`) — the single place each hook is edited:
- `scripts/skel/check_output_conformance.py` *(modified)* — PostToolUse deliverable-structure checker; gains anchor mode.
- `scripts/skel/output_language.py` *(new)* — SessionStart language-directive injector.
- `scripts/skel/hooks.json` *(new)* — the plugin-level hook declaration that wires the above.

**Per-plugin copies** (5×, byte-identical to the canonical source):
- `pm-<plugin>/scripts/check_output_conformance.py` *(modified)*
- `pm-<plugin>/hooks/output_language.py` *(new)*
- `pm-<plugin>/hooks/hooks.json` *(new)*

**Authoring tooling:**
- `scripts/skillkit.py` *(modified)* — gains `slugify`, `anchor_template`, `cmd_anchors`.
- `justfile` *(modified)* — `anchors` recipe; `test` recipe runs pytest + linter.
- `docs/skill-template/template.md` *(modified)* — skeleton emits anchors.

**Linter:**
- `tests/validate_plugins.py` *(modified)* — `validate_template` gains the anchor presence + uniqueness checks.

**Content (110 templates, scripted):**
- `pm-strategy/skills/*/template.md` (36), `pm-discovery` (29), `pm-gtm` (16), `pm-execution` (17), `pm-influence` (12).

**Docs:**
- `docs/output-language.md` *(new)*, `README.md` *(modified)*, `CLAUDE.md` *(modified)*, `docs/SKILL-STANDARD.md` *(modified)*.

**Tests:**
- `tests/test_check_conformance.py` *(modified)*, `tests/test_template_check.py` *(modified)*
- `tests/test_hook_copies_identical.py` *(new)*, `tests/test_skillkit_anchors.py` *(new)*, `tests/test_output_language_hook.py` *(new)*

---

## Task 1: Anchor-aware conformance hook

**Files:**
- Modify: `scripts/skel/check_output_conformance.py`
- Modify: `tests/test_check_conformance.py`
- Create: `tests/test_hook_copies_identical.py`
- Modify: `pm-strategy/scripts/check_output_conformance.py` (copy of skel)
- Modify: `pm-discovery/scripts/check_output_conformance.py` (copy of skel)
- Modify: `pm-gtm/scripts/check_output_conformance.py` (copy of skel)
- Modify: `pm-execution/scripts/check_output_conformance.py` (copy of skel)
- Modify: `pm-influence/scripts/check_output_conformance.py` (copy of skel)
- Modify: `justfile:11-13` (the `test` recipe)
- Modify: `CLAUDE.md` (the `just test` line under "## Commands")

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces:
  - `check_output_conformance.ANCHOR_RE` — `re.Pattern`, matches `<!--#slug-->`, group 1 is the slug.
  - `check_output_conformance.parse_headings(md: str) -> list[tuple[str, str]]` — `(anchor, text)` per `##`/`###` heading, in order; `anchor` is `""` when the heading has none; `text` has the anchor comment stripped.
  - `check_output_conformance.headings(md: str) -> list[str]` — unchanged public behaviour, now `[text for _, text in parse_headings(md)]`.
  - `check_output_conformance.evaluate(payload: dict, template_path: str) -> tuple[int, str]` — unchanged signature.

Background: the file is the PostToolUse hook wired from every skill's frontmatter with the skill's own `template.md` as its argument. It currently decides whether a written `.md` file is the skill's deliverable by counting how many template heading *strings* appear in it, and reports missing ones. A translated deliverable matches zero headings, falls under the half threshold, and passes silently — that silent fail-open is the whole problem this plan solves.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_check_conformance.py`:

```python
ANCHORED = ("# T\n"
            "## Market Definition <!--#market-definition-->\nx\n"
            "## TAM <!--#tam-->\ny\n"
            "## SAM <!--#sam-->\nz\n"
            "## SOM <!--#som-->\nw\n")


def _anchored_tmpl(tmp_path):
    return _write(tmp_path, "template.md", ANCHORED)


def test_parse_headings_splits_anchor_from_text():
    assert checker.parse_headings(ANCHORED) == [
        ("market-definition", "Market Definition"),
        ("tam", "TAM"),
        ("sam", "SAM"),
        ("som", "SOM"),
    ]


def test_parse_headings_without_anchors_yields_empty_anchor():
    assert checker.parse_headings(TEMPLATE) == [
        ("", "Market Definition"), ("", "TAM"), ("", "SAM"), ("", "SOM")]


def test_headings_helper_strips_anchors():
    assert checker.headings(ANCHORED) == ["Market Definition", "TAM", "SAM", "SOM"]


def test_french_artifact_with_all_anchors_is_silent(tmp_path):
    art = _write(tmp_path, "memo.md",
                 "## Definition du marche <!--#market-definition-->\n"
                 "## TAM <!--#tam-->\n"
                 "## SAM <!--#sam-->\n"
                 "## SOM <!--#som-->\n")
    code, msg = checker.evaluate(_payload(art), _anchored_tmpl(tmp_path))
    assert code == 0 and msg == ""


def test_french_artifact_missing_anchors_is_flagged_with_english_names(tmp_path):
    # Two of four anchors present -> passes the half threshold -> is the deliverable.
    art = _write(tmp_path, "memo.md",
                 "## Definition du marche <!--#market-definition-->\n"
                 "## TAM <!--#tam-->\n")
    code, msg = checker.evaluate(_payload(art), _anchored_tmpl(tmp_path))
    assert code == 2
    # Names the ENGLISH heading text, not the slug, so the feedback is readable.
    assert "SAM" in msg and "SOM" in msg
    assert "#sam" not in msg
    # Tells the model to keep the anchors it just learned about.
    assert "anchor" in msg.lower()


def test_french_unrelated_file_stays_silent_in_anchor_mode(tmp_path):
    art = _write(tmp_path, "notes.md", "# Notes diverses\nrien de structure ici\n")
    code, msg = checker.evaluate(_payload(art), _anchored_tmpl(tmp_path))
    assert code == 0 and msg == ""


def test_anchor_mode_ignores_english_headings_without_anchors(tmp_path):
    # An English artifact that dropped the anchors is NOT recognised: in anchor
    # mode the anchor is the handle, and only one of four is present.
    art = _write(tmp_path, "memo.md",
                 "## Market Definition\n## TAM\n## SAM <!--#sam-->\n")
    code, msg = checker.evaluate(_payload(art), _anchored_tmpl(tmp_path))
    assert code == 0 and msg == ""


def test_partially_anchored_template_falls_back_per_heading(tmp_path):
    # Template has one anchored and one bare heading -> anchor mode is on, but the
    # bare heading still matches on its text.
    tmpl = _write(tmp_path, "template.md",
                  "## Market Definition <!--#market-definition-->\n## Sources\n")
    art = _write(tmp_path, "memo.md",
                 "## Definition du marche <!--#market-definition-->\n## Sources\n")
    code, msg = checker.evaluate(_payload(art), tmpl)
    assert code == 0 and msg == ""


def test_unanchored_template_uses_text_mode(tmp_path):
    # Regression guard: a template that has not been migrated behaves exactly as
    # it does today — a French artifact is unrecognised, not flagged.
    art = _write(tmp_path, "memo.md",
                 "## Definition du marche\n## TAM\n## SAM\n## SOM\n")
    code, msg = checker.evaluate(_payload(art), _tmpl(tmp_path))
    # "TAM"/"SAM"/"SOM" happen to be untranslated, so 3 of 4 match -> flagged on
    # the one missing English heading. No anchors are involved.
    assert code == 2 and "Market Definition" in msg
```

Create `tests/test_hook_copies_identical.py`:

```python
"""Each plugin ships its own copy of the hook scripts in scripts/skel/.

A drifted copy means one plugin silently enforces different rules than the
others. This test is the guard that keeps the six copies in lockstep.
"""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ["pm-strategy", "pm-discovery", "pm-gtm", "pm-execution", "pm-influence"]

# canonical file in scripts/skel/  ->  its path inside each plugin
COPIES = {
    "check_output_conformance.py": "scripts/check_output_conformance.py",
}


def _digest(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def test_every_plugin_copy_matches_skel():
    for src_name, rel in COPIES.items():
        src = ROOT / "scripts" / "skel" / src_name
        assert src.is_file(), f"canonical source missing: {src}"
        want = _digest(src)
        for plugin in PLUGINS:
            dst = ROOT / plugin / rel
            assert dst.is_file(), f"missing: {dst} — copy it from {src}"
            assert _digest(dst) == want, (
                f"{dst} has drifted from {src}. Re-copy it:\n"
                f"  for p in pm-*/; do cp {src.relative_to(ROOT)} "
                f"\"$p\"{rel}; done")
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_check_conformance.py tests/test_hook_copies_identical.py -q`

Expected: FAIL. `parse_headings` raises `AttributeError: module 'check_output_conformance' has no attribute 'parse_headings'`; the anchor-mode tests fail; `test_every_plugin_copy_matches_skel` passes already (the six copies are identical today, md5 `0e5f620c03e34860316fda32a4607c50`).

- [ ] **Step 3: Add `ANCHOR_RE` and `parse_headings` to the canonical hook**

In `scripts/skel/check_output_conformance.py`, replace the `headings` function with:

```python
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
```

- [ ] **Step 4: Switch `evaluate` to anchor-first matching**

In the same file, replace the body of `evaluate` from `want = headings(...)` to the end with:

```python
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

    present = sum(1 for anchor, text in want if found(anchor, text))
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
```

Also update the module docstring's third paragraph (currently "already contains >= half the template's `##`/`###` headings") to read:

```
skill's deliverable (already matches >= half the template's sections — by
`<!--#anchor-->` comment when the template carries them, else by heading text) but
is missing some, exits 2 — the stderr message is fed back to Claude so it revises
the file.
```

- [ ] **Step 5: Run the hook tests to verify they pass**

Run: `uv run pytest tests/test_check_conformance.py -q`
Expected: PASS (all cases, old and new).

- [ ] **Step 6: Copy the canonical hook into all five plugins**

```bash
for p in pm-strategy pm-discovery pm-gtm pm-execution pm-influence; do
  cp scripts/skel/check_output_conformance.py "$p/scripts/check_output_conformance.py"
done
md5 scripts/skel/check_output_conformance.py pm-*/scripts/check_output_conformance.py
```

Expected: six identical md5 sums.

- [ ] **Step 7: Put pytest into the `just test` gate**

In `justfile`, replace the `test` recipe:

```just
# Run the full gate: unit tests + the structural skill linter (blocking)
test:
    uv run pytest -q
    uv run validate-plugins
```

In `CLAUDE.md`, under "## Commands", change the `just test` line to:

```
just test             # run pytest + the structural linter (blocking; non-zero exit on any error)
```

and change the sentence below the code block from "`just test` is the only gate; run it before every commit. It scans every directory containing `.claude-plugin/`…" to:

```
`just test` is the only gate; run it before every commit. It runs the `tests/` unit
suite, then the structural linter, which scans every directory containing
`.claude-plugin/` and validates manifests, `SKILL.md` frontmatter/body, and eval cards.
Warnings are advisory; **errors fail** (exit 1).
```

- [ ] **Step 8: Run the full gate**

Run: `just test`
Expected: pytest reports 42 passed (32 existing + 9 new conformance cases + 1 copy-identity case); linter prints `✓ ALL CHECKS PASSED (0 warnings)`.

- [ ] **Step 9: Commit**

```bash
git add scripts/skel/check_output_conformance.py \
        pm-*/scripts/check_output_conformance.py \
        tests/test_check_conformance.py tests/test_hook_copies_identical.py \
        justfile CLAUDE.md
git commit -F - <<'EOF'
feat(tooling): anchor-aware output conformance hook

Match template sections by `<!--#slug-->` anchor when the template carries
any, falling back to today's heading-text matching when it does not. A
translated deliverable keeps its anchors, so it stays recognised and stays
enforced instead of failing open silently.

Also puts the tests/ suite into `just test`, and adds a guard that the five
per-plugin hook copies stay byte-identical to scripts/skel/.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 2: `skillkit anchors` subcommand and anchored skeleton

**Files:**
- Modify: `scripts/skillkit.py` (add `slugify`, `anchor_template`, `cmd_anchors`; register in `COMMANDS` at line 279)
- Modify: `docs/skill-template/template.md`
- Modify: `justfile` (add an `anchors` recipe)
- Create: `tests/test_skillkit_anchors.py`

**Interfaces:**
- Consumes: `check_output_conformance.ANCHOR_RE` semantics from Task 1 — the anchor syntax `<!--#slug-->` with charset `[a-z0-9-]`. `skillkit` re-declares its own compiled pattern rather than importing across the skel boundary (skel files ship inside plugins and must not depend on repo tooling).
- Produces:
  - `skillkit.slugify(text: str) -> str`
  - `skillkit.anchor_template(text: str) -> str` — idempotent; returns `text` unchanged when every heading already has an anchor.
  - `skillkit.cmd_anchors(args: list[str]) -> int` — CLI entry, `skillkit.py anchors [<plugin>|<path> ...]`.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_skillkit_anchors.py`:

```python
import skillkit


def test_slugify_basic():
    assert skillkit.slugify("Market Definition") == "market-definition"


def test_slugify_collapses_punctuation_and_strips_edges():
    assert skillkit.slugify("TAM — Total Addressable Market") == \
        "tam-total-addressable-market"
    assert skillkit.slugify("Key sections:") == "key-sections"
    assert skillkit.slugify("<Name / Role> — <Influence>, <Stance>") == \
        "name-role-influence-stance"


def test_slugify_empty_result_falls_back_to_section():
    assert skillkit.slugify("###") == ""   # raw slug is empty
    # anchor_template is what applies the fallback:
    out = skillkit.anchor_template("## ---\n")
    assert out == "## --- <!--#section-->\n"


def test_anchor_template_adds_anchors_to_h2_and_h3():
    src = "# Title\n## Market Definition\ntext\n### Sub Section\n"
    assert skillkit.anchor_template(src) == (
        "# Title\n"
        "## Market Definition <!--#market-definition-->\n"
        "text\n"
        "### Sub Section <!--#sub-section-->\n")


def test_anchor_template_leaves_h1_and_h4_alone():
    src = "# Title\n#### Deep\n"
    assert skillkit.anchor_template(src) == src


def test_anchor_template_is_idempotent():
    once = skillkit.anchor_template("## Market Definition\n## Sources\n")
    assert skillkit.anchor_template(once) == once


def test_anchor_template_disambiguates_duplicate_headings():
    src = "## Scene\n## Scene\n## Scene\n"
    assert skillkit.anchor_template(src) == (
        "## Scene <!--#scene-->\n"
        "## Scene <!--#scene-2-->\n"
        "## Scene <!--#scene-3-->\n")


def test_anchor_template_does_not_reuse_an_existing_anchor():
    # `scene` is already taken by a hand-written anchor, so the new one skips it.
    src = "## Décor <!--#scene-->\n## Scene\n"
    assert skillkit.anchor_template(src) == (
        "## Décor <!--#scene-->\n"
        "## Scene <!--#scene-2-->\n")


def test_cmd_anchors_rewrites_a_named_file(tmp_path, capsys):
    t = tmp_path / "template.md"
    t.write_text("## A\n## B\n", encoding="utf-8")
    assert skillkit.cmd_anchors([str(t)]) == 0
    assert t.read_text(encoding="utf-8") == "## A <!--#a-->\n## B <!--#b-->\n"
    assert "anchored 1/1" in capsys.readouterr().out


def test_cmd_anchors_second_run_reports_no_change(tmp_path, capsys):
    t = tmp_path / "template.md"
    t.write_text("## A <!--#a-->\n", encoding="utf-8")
    assert skillkit.cmd_anchors([str(t)]) == 0
    assert "anchored 0/1" in capsys.readouterr().out


def test_cmd_anchors_walks_a_plugin_dir(tmp_path, capsys):
    d = tmp_path / "pm-x" / "skills" / "s1"
    d.mkdir(parents=True)
    (d / "template.md").write_text("## A\n", encoding="utf-8")
    assert skillkit.cmd_anchors([str(tmp_path / "pm-x")]) == 0
    assert (d / "template.md").read_text(encoding="utf-8") == "## A <!--#a-->\n"


def test_cmd_anchors_unknown_target_errors(tmp_path):
    assert skillkit.cmd_anchors([str(tmp_path / "nope")]) == 1


def test_anchors_is_registered():
    assert "anchors" in skillkit.COMMANDS


def test_skeleton_template_ships_anchors():
    from pathlib import Path
    body = (Path(skillkit.TEMPLATE_DIR) / "template.md").read_text(encoding="utf-8")
    assert skillkit.anchor_template(body) == body, \
        "docs/skill-template/template.md must already carry anchors"
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_skillkit_anchors.py -q`
Expected: FAIL with `AttributeError: module 'skillkit' has no attribute 'slugify'`.

- [ ] **Step 3: Implement the anchor helpers in `scripts/skillkit.py`**

Insert after the `_ROW` definition (line 37), before `load_tasks`:

```python
# ─── Template anchors ────────────────────────────────────────────────────────
# Deliverables are written in the consuming project's language, so the output
# conformance hook cannot match sections on English heading text. Each template
# heading carries a language-independent `<!--#slug-->` anchor instead; the
# deliverable copies it, and the hook matches on that.

# `[ \t]*$`, not `\s*$`: under re.sub, a greedy `\s*` swallows the trailing
# newline of a heading that is the file's last line, because `$` also matches at
# end-of-string. That would silently strip the final newline from every template
# ending in a heading.
_HEADING_LINE = re.compile(r"(?m)^(#{2,3})\s+(.+?)[ \t]*$")
_ANCHOR = re.compile(r"<!--#([a-z0-9-]+)-->")


def slugify(text: str) -> str:
    """`Market Definition` -> `market-definition`. May return "" (see anchor_template)."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def anchor_template(text: str) -> str:
    """Append `<!--#slug-->` to every `##`/`###` heading that lacks one.

    Idempotent: headings that already carry an anchor are returned untouched, and
    their slugs are reserved so a newly generated one never collides with them.
    Duplicate headings within one template get `-2`, `-3`, ... appended.
    """
    used = {m.group(1) for m in _ANCHOR.finditer(text)}

    def repl(m: re.Match) -> str:
        hashes, body = m.group(1), m.group(2)
        if _ANCHOR.search(body):
            return m.group(0)
        base = slugify(body) or "section"
        slug, n = base, 2
        while slug in used:
            slug = f"{base}-{n}"
            n += 1
        used.add(slug)
        return f"{hashes} {body} <!--#{slug}-->"

    return _HEADING_LINE.sub(repl, text)
```

- [ ] **Step 4: Implement `cmd_anchors`**

Insert after `cmd_scaffold` (after line 178):

```python
def cmd_anchors(args: list[str]) -> int:
    """Add `<!--#slug-->` anchors to template.md headings. Idempotent.

    usage: skillkit.py anchors [<plugin-dir>|<template.md> ...]
    With no arguments, processes every pm-*/skills/*/template.md in the repo.
    """
    targets: list[Path] = []
    if args:
        for a in args:
            p = Path(a)
            if not p.is_absolute():
                p = REPO_ROOT / a
            if p.is_file():
                targets.append(p)
            elif p.is_dir():
                targets.extend(sorted(p.glob("skills/*/template.md")))
            else:
                print(f"error: no such plugin dir or file: {a}", file=sys.stderr)
                return 1
    else:
        targets = sorted(REPO_ROOT.glob("pm-*/skills/*/template.md"))
    changed = 0
    for t in targets:
        old = t.read_text(encoding="utf-8")
        new = anchor_template(old)
        if new != old:
            t.write_text(new, encoding="utf-8")
            changed += 1
    print(f"anchored {changed}/{len(targets)} template(s)")
    return 0
```

Then register it — replace line 279:

```python
COMMANDS = {"next": cmd_next, "progress": cmd_progress, "scaffold": cmd_scaffold, "context": cmd_context, "anchors": cmd_anchors, "wip": cmd_wip, "done": cmd_done}
```

And update the module docstring's second line (line 4) to:

```
Subcommands: next | scaffold | context | anchors | wip | done | progress
```

- [ ] **Step 5: Anchor the scaffold skeleton**

Replace `docs/skill-template/template.md` with:

```markdown
# <Artifact Title>

<!--
The fill-in output template the skill produces. Mirror the Output Contract
sections from SKILL.md exactly. Use placeholders in <angle brackets> and short
inline guidance in comments. Delete this comment block in real templates.

Every `##`/`###` heading carries a `<!--#slug-->` anchor. That anchor — not the
heading text — is how the output-conformance hook identifies a section, so a
deliverable written in the project's own language is still checked. When you
rename a heading, DELETE its placeholder anchor and run `just anchors <plugin>`
to regenerate one that matches the new text.
-->

## <Section 1> <!--#section-1-->
<placeholder>

## <Section 2> <!--#section-2-->
<placeholder>

| <col> | <col> |
|-------|-------|
| <...> | <...> |
```

- [ ] **Step 6: Add the `just anchors` recipe**

In `justfile`, after the `context` recipe, add:

```just
# Add <!--#slug--> anchors to template.md headings (idempotent).
# No argument = every template in the repo: just anchors
# Or scope it:  just anchors pm-strategy
anchors target="":
    uv run python scripts/skillkit.py anchors {{target}}
```

- [ ] **Step 7: Run the tests to verify they pass**

Run: `uv run pytest tests/test_skillkit_anchors.py -q`
Expected: PASS (14 cases).

- [ ] **Step 8: Verify the tool is a no-op on the scaffold path**

Run: `uv run python scripts/skillkit.py anchors docs/skill-template/template.md`
Expected: `anchored 0/1 template(s)` — the skeleton is already anchored, and `git status` shows no change to that file.

- [ ] **Step 9: Run the full gate**

Run: `just test`
Expected: pytest 56 passed; linter `✓ ALL CHECKS PASSED (0 warnings)`. The 110 plugin templates are untouched at this point.

- [ ] **Step 10: Commit**

```bash
git add scripts/skillkit.py justfile docs/skill-template/template.md \
        tests/test_skillkit_anchors.py
git commit -F - <<'EOF'
feat(tooling): skillkit anchors subcommand

`just anchors [target]` appends a `<!--#slug-->` anchor to every `##`/`###`
heading in a template.md — idempotent, collision-safe within a template, and
scopable to one plugin or one file. The scaffold skeleton now ships anchors so
new skills inherit the convention.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 3: Migrate all 110 templates (five commits)

**Files:**
- Modify: `pm-strategy/skills/*/template.md` (36 files, 257 headings)
- Modify: `pm-discovery/skills/*/template.md` (29 files, 224 headings)
- Modify: `pm-gtm/skills/*/template.md` (16 files, 121 headings)
- Modify: `pm-execution/skills/*/template.md` (17 files, 127 headings)
- Modify: `pm-influence/skills/*/template.md` (12 files, 87 headings)

**Interfaces:**
- Consumes: `just anchors <plugin>` from Task 2; anchor-mode matching from Task 1.
- Produces: 110 anchored templates — the precondition for Task 4's linter check landing at error level, and for the hook running in anchor mode in production.

Nothing is hand-edited. Every heading in every plugin is rewritten by the same tool, one plugin per commit so the diff stays reviewable per quadrant. Expected totals: 816 headings anchored, of which 26 need a `-2`/`-3` suffix (they live in `pm-discovery/skills/storyboard`, `pm-discovery/skills/user-personas`, `pm-execution/skills/shipping-artifacts`, and `pm-influence/skills/stakeholder-engagement-advisor`).

- [ ] **Step 1: Write the diff verifier**

A grep over the diff is not enough: a removed `-## Market Definition` line contains no
anchor, so it cannot be filtered by "does it mention an anchor". The check has to be
"strip the anchors back out and you get exactly what was committed". Write it once to
`/tmp/verify_anchors.py` and reuse it for all five plugins:

```bash
cat > /tmp/verify_anchors.py <<'PY'
"""Assert the only change under <plugin> is headings gaining <!--#slug--> anchors."""
import re, subprocess, sys

plugin = sys.argv[1]
files = subprocess.run(["git", "diff", "--name-only", "--", plugin],
                       capture_output=True, text=True, check=True).stdout.split()
assert files, f"no changes under {plugin}"
added = 0
for f in files:
    head = subprocess.run(["git", "show", f"HEAD:{f}"],
                          capture_output=True, text=True, check=True).stdout
    now = open(f, encoding="utf-8").read()
    added += (len(re.findall(r"<!--#[a-z0-9-]+-->", now))
              - len(re.findall(r"<!--#[a-z0-9-]+-->", head)))
    assert re.sub(r" <!--#[a-z0-9-]+-->", "", now) == head, \
        f"{f}: change is NOT anchor-only"
print(f"OK {plugin}: {len(files)} files, {added} anchors added, nothing else changed")
PY
```

- [ ] **Step 2: Migrate and verify pm-strategy**

```bash
just anchors pm-strategy
python3 /tmp/verify_anchors.py pm-strategy
```

Expected: `anchored 36/36 template(s)`, then
`OK pm-strategy: 36 files, 257 anchors added, nothing else changed`.

- [ ] **Step 3: Spot-check one template by eye**

```bash
head -12 pm-strategy/skills/market-sizing/template.md
```

Expected:

```markdown
# Market Sizing: <Product / Opportunity>

## Market Definition <!--#market-definition-->
- **Problem space & customer need:** <...>
- **Segment & geographic boundaries:** <...>
- **Scoping decisions / exclusions:** <...>

## TAM — Total Addressable Market <!--#tam-total-addressable-market-->
```

- [ ] **Step 4: Run the gate and commit pm-strategy**

```bash
just test
git add pm-strategy/skills
git commit -F - <<'EOF'
chore(pm-strategy): add section anchors to templates

Scripted with `just anchors pm-strategy` — 257 headings across 36 templates.
The anchor is the language-independent handle the output-conformance hook
matches on, so deliverables written in the project's language stay enforced.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

- [ ] **Step 5: Migrate, verify and commit pm-discovery**

```bash
just anchors pm-discovery                       # expect: anchored 29/29
python3 /tmp/verify_anchors.py pm-discovery     # expect: 29 files, 224 anchors added
grep -n '<!--#scene' pm-discovery/skills/storyboard/template.md
```

The last command must show `#scene`, `#scene-2`, `#scene-3`, `#scene-4`, `#scene-5` — the collision rule doing its job on the five repeated `Scene` headings.

```bash
just test
git add pm-discovery/skills
git commit -F - <<'EOF'
chore(pm-discovery): add section anchors to templates

Scripted with `just anchors pm-discovery` — 224 headings across 29 templates.
Repeated headings (storyboard's Scene/Action/Emotion/Annotation, user-personas'
paired blocks) get -2/-3 suffixes so anchors stay unique per template.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

- [ ] **Step 6: Migrate, verify and commit pm-gtm**

```bash
just anchors pm-gtm                             # expect: anchored 16/16
python3 /tmp/verify_anchors.py pm-gtm           # expect: 16 files, 121 anchors added
just test
git add pm-gtm/skills
git commit -F - <<'EOF'
chore(pm-gtm): add section anchors to templates

Scripted with `just anchors pm-gtm` — 121 headings across 16 templates.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

- [ ] **Step 7: Migrate, verify and commit pm-execution**

```bash
just anchors pm-execution                       # expect: anchored 17/17
python3 /tmp/verify_anchors.py pm-execution     # expect: 17 files, 127 anchors added
just test
git add pm-execution/skills
git commit -F - <<'EOF'
chore(pm-execution): add section anchors to templates

Scripted with `just anchors pm-execution` — 127 headings across 17 templates.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

- [ ] **Step 8: Migrate, verify and commit pm-influence**

```bash
just anchors pm-influence                       # expect: anchored 12/12
python3 /tmp/verify_anchors.py pm-influence     # expect: 12 files, 87 anchors added
just test
git add pm-influence/skills
git commit -F - <<'EOF'
chore(pm-influence): add section anchors to templates

Scripted with `just anchors pm-influence` — 87 headings across 12 templates.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

- [ ] **Step 9: Confirm the migration is complete**

```bash
uv run python scripts/skillkit.py anchors
```

Expected: `anchored 0/110 template(s)` and a clean `git status` — every heading in the repo already carries an anchor.

---

## Task 4: Linter enforces anchors

**Files:**
- Modify: `tests/validate_plugins.py:240-258` (`validate_template`)
- Modify: `tests/test_template_check.py` (fixtures need anchors; add three cases)

**Interfaces:**
- Consumes: the anchored templates from Task 3, and the same `<!--#slug-->` syntax as Tasks 1–2.
- Produces: two blocking errors on `template.md` — a missing anchor and a duplicate anchor — so the ~40 skills still `todo` in `TASKS.md` cannot reintroduce the untranslatable-heading problem.

The check lands at **error** level directly rather than as a warning first (see "Deviations" above): Task 3 already migrated every template, so it is clean the moment it is added.

- [ ] **Step 1: Update the existing fixtures and write the failing tests**

In `tests/test_template_check.py`, two existing fixtures use unanchored templates and assert no errors — they must adopt the convention they are now being checked against:

```python
def test_fewer_headings_than_contract_warns(tmp_path):
    # 1 heading, 2 contract items
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE, template_md="# T\n## A <!--#a-->\n")
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert not r.errors
    assert any("Output Contract" in w for w in r.warnings)


def test_level3_headings_count_toward_sections(tmp_path):
    # 2 items in the contract; template groups them as `###` under one `##` bucket.
    # h2 + h3 = 3 headings >= 2 items, so it must NOT warn.
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md="# T\n## Bucket <!--#bucket-->\n### A <!--#a-->\n### B <!--#b-->\n")
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert not r.errors and not r.warnings
```

Then append the new cases:

```python
def test_missing_anchor_is_error(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md="# T\n## A <!--#a-->\n## B\n### C <!--#c-->\n")
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert any("anchor" in e for e in r.errors)
    assert any("1 of 3" in e for e in r.errors)


def test_duplicate_anchor_is_error(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md="# T\n## A <!--#a-->\n## Autre <!--#a-->\n")
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert any("duplicate anchor" in e for e in r.errors)
    assert any("#a" in e for e in r.errors)


def test_fully_anchored_template_is_clean(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md="# T\n## A <!--#a-->\n## B <!--#b-->\n")
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert not r.errors and not r.warnings


def test_unreferenced_template_is_not_anchor_checked(tmp_path):
    # No `template.md` mention in SKILL.md -> the template is not this skill's
    # contract, so anchors are not required of it.
    skill = ("---\nname: x\n---\n## Output Contract\nAdvisory only.\n"
             "## Validation & Eval\n")
    d = _mk(tmp_path, skill, template_md="# T\n## A\n")
    r = vp.validate_template(d, skill)
    assert not r.errors
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_template_check.py -q`
Expected: FAIL — `test_missing_anchor_is_error` and `test_duplicate_anchor_is_error` fail on empty `r.errors`. The other cases pass.

- [ ] **Step 3: Add the checks to `validate_template`**

In `tests/validate_plugins.py`, inside the `if references and exists and body:` block, after the existing `if items and headings < items:` warning, append:

```python
        # Anchors are what make the output-conformance hook language-independent:
        # it matches `<!--#slug-->`, not English heading text, so a deliverable
        # written in the project's language is still structurally enforced.
        anchors = re.findall(r"(?m)^#{2,3}\s+.*<!--#([a-z0-9-]+)-->\s*$", body)
        if len(anchors) < headings:
            r.error(f"template.md: {headings - len(anchors)} of {headings} "
                    f"'##'/'###' headings lack a '<!--#slug-->' anchor "
                    f"(fix: just anchors)")
        dupes = sorted({a for a in anchors if anchors.count(a) > 1})
        if dupes:
            r.error("template.md: duplicate anchor(s): "
                    + ", ".join(f"#{d}" for d in dupes))
```

Also extend the module docstring's "Checks:" list (around line 16) — after the `SKILL.md body` bullet, add:

```
- template.md: every '##'/'###' heading carries a unique '<!--#slug-->' anchor.
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `uv run pytest tests/test_template_check.py -q`
Expected: PASS (10 cases).

- [ ] **Step 5: Confirm the whole repo is clean under the new check**

Run: `just test`
Expected: pytest 60 passed; linter `✓ ALL CHECKS PASSED (0 warnings)` over 5 plugins / 110 skills. If the linter reports a missing-anchor error, a template was missed in Task 3 — run `uv run python scripts/skillkit.py anchors` and re-run.

- [ ] **Step 6: Prove the check actually bites**

Strip one anchor, confirm the linter fails, restore. (BSD `sed` has no `0,/re/` address,
so do the edit in Python — pick whatever template exists under `pm-gtm/skills/`.)

```bash
VICTIM=$(ls pm-gtm/skills/*/template.md | head -1)
cp "$VICTIM" /tmp/victim.bak
python3 -c "import re,sys; p=sys.argv[1]; s=open(p).read(); open(p,'w').write(re.sub(r' <!--#[a-z0-9-]+-->','',s,count=1))" "$VICTIM"
uv run validate-plugins; echo "exit=$?"
cp /tmp/victim.bak "$VICTIM" && rm /tmp/victim.bak
git status --porcelain pm-gtm
```

Expected: the linter prints an `✗ ERROR` mentioning `template.md` and `anchor` for that
skill, and `exit=1`. After the restore, `git status --porcelain` prints nothing.

- [ ] **Step 7: Commit**

```bash
git add tests/validate_plugins.py tests/test_template_check.py
git commit -F - <<'EOF'
feat(tooling): require unique anchors on template headings

Errors when a template.md heading lacks a `<!--#slug-->` anchor or when two
headings share one. Lands at error level because every template is already
migrated — this is what stops the skills still on the backlog from shipping
sections the conformance hook cannot match in a translated deliverable.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

---

## Task 5: Output-language SessionStart hook

**Files:**
- Create: `scripts/skel/output_language.py`
- Create: `scripts/skel/hooks.json`
- Create: `pm-strategy/hooks/output_language.py`, `pm-strategy/hooks/hooks.json`
- Create: `pm-discovery/hooks/output_language.py`, `pm-discovery/hooks/hooks.json`
- Create: `pm-gtm/hooks/output_language.py`, `pm-gtm/hooks/hooks.json`
- Create: `pm-execution/hooks/output_language.py`, `pm-execution/hooks/hooks.json`
- Create: `pm-influence/hooks/output_language.py`, `pm-influence/hooks/hooks.json`
- Create: `tests/test_output_language_hook.py`
- Modify: `tests/test_hook_copies_identical.py` (add the two new files to `COPIES`)
- Create: `docs/output-language.md`
- Modify: `README.md` (new "Output language" section)
- Modify: `docs/SKILL-STANDARD.md` (§4, the language-eval pattern)
- Create: `pm-strategy/skills/market-sizing/evals/market-sizing-fr-project.md`

**Interfaces:**
- Consumes: the `<!--#anchor-->` convention from Tasks 2–4 (the injected directive tells the model to preserve them), and `tests/test_hook_copies_identical.py:COPIES` from Task 1.
- Produces:
  - `output_language.SETTINGS_REL` — `Path(".config") / "pm-skills.yaml"`
  - `output_language.project_root(payload: dict) -> Path`
  - `output_language.read_language(root: Path) -> str` — the declared code lowercased, or `""` when absent/unparseable/English.
  - `output_language.directive(lang: str) -> str`
  - `output_language.emit(text: str) -> None` — prints the platform-appropriate JSON.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_output_language_hook.py`:

```python
"""Tests for the SessionStart output-language hook."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "output_language", ROOT / "scripts" / "skel" / "output_language.py")
hook = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hook)


def _settings(tmp_path, text):
    d = tmp_path / ".config"
    d.mkdir(exist_ok=True)
    (d / "pm-skills.yaml").write_text(text, encoding="utf-8")
    return tmp_path


def test_no_settings_file_declares_nothing(tmp_path):
    assert hook.read_language(tmp_path) == ""


def test_french_is_declared(tmp_path):
    assert hook.read_language(_settings(tmp_path, "language: fr\n")) == "fr"


def test_quoted_and_uppercased_value_is_normalised(tmp_path):
    assert hook.read_language(_settings(tmp_path, 'language: "FR"\n')) == "fr"


def test_english_declares_nothing(tmp_path):
    for value in ("en", "EN", "en-US", "english"):
        assert hook.read_language(_settings(tmp_path, f"language: {value}\n")) == "", value


def test_other_keys_are_ignored(tmp_path):
    root = _settings(tmp_path, "currency: EUR\nregion: emea\n")
    assert hook.read_language(root) == ""


def test_language_key_found_among_other_keys(tmp_path):
    root = _settings(tmp_path, "# project settings\ncurrency: EUR\nlanguage: de\n")
    assert hook.read_language(root) == "de"


def test_indented_language_key_is_not_a_declaration(tmp_path):
    # Only a top-level `language:` counts; a nested one belongs to another key.
    root = _settings(tmp_path, "other:\n  language: fr\n")
    assert hook.read_language(root) == ""


def test_directive_names_the_language_and_the_rules():
    d = hook.directive("fr")
    assert "**French**" in d
    assert "TAM/SAM/SOM" in d and "RICE" in d and "OKR" in d
    assert "<!--#anchor-->" in d
    assert "stay English" in d


def test_directive_falls_back_to_the_raw_code():
    assert "**nb**" in hook.directive("nb")


def test_project_root_prefers_the_env_var(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path / "env"))
    assert hook.project_root({"cwd": str(tmp_path / "payload")}) == tmp_path / "env"


def test_project_root_falls_back_to_payload_cwd(tmp_path, monkeypatch):
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    assert hook.project_root({"cwd": str(tmp_path)}) == tmp_path


def test_project_root_falls_back_to_cwd(monkeypatch):
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    assert hook.project_root({}) == Path.cwd()


def test_emit_uses_claude_code_shape(monkeypatch, capsys):
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", "/x")
    monkeypatch.delenv("CURSOR_PLUGIN_ROOT", raising=False)
    monkeypatch.delenv("COPILOT_CLI", raising=False)
    hook.emit("hello")
    out = json.loads(capsys.readouterr().out)
    assert out["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    assert out["hookSpecificOutput"]["additionalContext"] == "hello"


def test_emit_uses_cursor_shape(monkeypatch, capsys):
    monkeypatch.setenv("CURSOR_PLUGIN_ROOT", "/x")
    hook.emit("hello")
    assert json.loads(capsys.readouterr().out) == {"additional_context": "hello"}


def test_emit_uses_sdk_shape_for_copilot(monkeypatch, capsys):
    monkeypatch.delenv("CURSOR_PLUGIN_ROOT", raising=False)
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", "/x")
    monkeypatch.setenv("COPILOT_CLI", "1")
    hook.emit("hello")
    assert json.loads(capsys.readouterr().out) == {"additionalContext": "hello"}


def test_hooks_json_wires_the_script():
    cfg = json.loads((ROOT / "scripts" / "skel" / "hooks.json").read_text())
    entry = cfg["hooks"]["SessionStart"][0]["hooks"][0]
    assert entry["type"] == "command"
    assert "hooks/output_language.py" in entry["command"]
    assert "${CLAUDE_PLUGIN_ROOT}" in entry["command"]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `uv run pytest tests/test_output_language_hook.py -q`
Expected: FAIL at collection — `FileNotFoundError` for `scripts/skel/output_language.py`.

- [ ] **Step 3: Write the canonical hook**

Create `scripts/skel/output_language.py`:

```python
#!/usr/bin/env python3
"""SessionStart hook — declare the project's deliverable language to the model.

Distributed inside each plugin as `<plugin>/hooks/output_language.py` and wired
from `<plugin>/hooks/hooks.json`:

    python3 "${CLAUDE_PLUGIN_ROOT}/hooks/output_language.py"

Reads `.config/pm-skills.yaml` at the project root and, when it declares a
non-English `language:`, injects a one-paragraph directive as additionalContext.
Every PM skill in the session then writes its deliverable in that language —
without a language rule having to be repeated in 110 SKILL.md files.

Language is DECLARED, never inferred: nothing is read from the language of
existing docs, and CLAUDE.md is not a source. Two sources that can disagree
reintroduce the inconsistency this exists to remove.

Parsing is a regex, not PyYAML: hooks are stdlib-only `python3` so they run on an
end user's machine. Fail-open everywhere: anything unexpected emits nothing and
exits 0, so session start is never disturbed.
"""
import json
import os
import re
import sys
from pathlib import Path

SETTINGS_REL = Path(".config") / "pm-skills.yaml"
# Top-level key only — an indented `language:` belongs to some other key.
LANGUAGE_RE = re.compile(r"(?m)^language:[ \t]*(\S+)[ \t]*$")
ENGLISH = {"en", "en-us", "en-gb", "eng", "english"}

# Codes worth naming in prose; anything else is passed through as-is.
LANGUAGE_NAMES = {
    "fr": "French", "de": "German", "es": "Spanish", "it": "Italian",
    "pt": "Portuguese", "nl": "Dutch", "pl": "Polish", "sv": "Swedish",
    "da": "Danish", "fi": "Finnish", "ja": "Japanese", "ko": "Korean",
    "zh": "Chinese", "ar": "Arabic", "tr": "Turkish", "ru": "Russian",
}


def project_root(payload: dict) -> Path:
    """The consuming project's root: the env var Claude Code sets, else the
    session's cwd from the hook payload, else the process cwd."""
    for candidate in (os.environ.get("CLAUDE_PROJECT_DIR"), payload.get("cwd")):
        if candidate:
            return Path(candidate)
    return Path.cwd()


def read_language(root: Path) -> str:
    """The declared language code, lowercased.

    Returns "" when no settings file exists, no `language:` key is present, or the
    declared language is English — in all three cases the hook stays silent and
    output defaults to English at no context cost.
    """
    f = root / SETTINGS_REL
    if not f.is_file():
        return ""
    m = LANGUAGE_RE.search(f.read_text(encoding="utf-8"))
    if not m:
        return ""
    lang = m.group(1).strip().strip("\"'").lower()
    return "" if lang in ENGLISH else lang


def directive(lang: str) -> str:
    name = LANGUAGE_NAMES.get(lang, lang)
    return (f"Deliverables produced by PM skills in this project are written in "
            f"**{name}**. Keep established PM terms (TAM/SAM/SOM, RICE, JTBD, NPS, "
            f"ICP, OKR) untranslated, and preserve template `<!--#anchor-->` "
            f"comments verbatim. Skill instructions and eval cards stay English.")


def emit(text: str) -> None:
    """Print the context-injection JSON in the shape the current host consumes.

    Claude Code reads BOTH `additional_context` and `hookSpecificOutput` without
    deduplication, so exactly one field is emitted. Ported from superpowers'
    hooks/session-start.
    """
    if os.environ.get("CURSOR_PLUGIN_ROOT"):
        print(json.dumps({"additional_context": text}))
    elif os.environ.get("CLAUDE_PLUGIN_ROOT") and not os.environ.get("COPILOT_CLI"):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "SessionStart", "additionalContext": text}}))
    else:
        print(json.dumps({"additionalContext": text}))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    try:
        lang = read_language(project_root(payload))
        if lang:
            emit(directive(lang))
    except Exception:
        pass  # fail-open: never disturb session start
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Write the canonical hooks manifest**

Create `scripts/skel/hooks.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/output_language.py\"",
            "async": false
          }
        ]
      }
    ]
  }
}
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `uv run pytest tests/test_output_language_hook.py -q`
Expected: PASS (16 cases).

- [ ] **Step 6: Distribute both files to all five plugins and extend the drift guard**

```bash
for p in pm-strategy pm-discovery pm-gtm pm-execution pm-influence; do
  mkdir -p "$p/hooks"
  cp scripts/skel/output_language.py "$p/hooks/output_language.py"
  cp scripts/skel/hooks.json "$p/hooks/hooks.json"
done
```

In `tests/test_hook_copies_identical.py`, replace the `COPIES` dict with:

```python
COPIES = {
    "check_output_conformance.py": "scripts/check_output_conformance.py",
    "output_language.py": "hooks/output_language.py",
    "hooks.json": "hooks/hooks.json",
}
```

Run: `uv run pytest tests/test_hook_copies_identical.py -q`
Expected: PASS — all three files identical across all five plugins.

- [ ] **Step 7: Smoke-test the hook end to end**

```bash
mkdir -p /tmp/fr-project/.config
printf 'language: fr\n' > /tmp/fr-project/.config/pm-skills.yaml
echo '{"hook_event_name":"SessionStart","cwd":"/tmp/fr-project"}' \
  | CLAUDE_PLUGIN_ROOT=/x python3 pm-strategy/hooks/output_language.py
```

Expected: one line of JSON —
`{"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "Deliverables produced by PM skills in this project are written in **French**. ..."}}`

Then confirm silence for an English project:

```bash
printf 'language: en\n' > /tmp/fr-project/.config/pm-skills.yaml
echo '{"cwd":"/tmp/fr-project"}' | CLAUDE_PLUGIN_ROOT=/x python3 pm-strategy/hooks/output_language.py; echo "exit=$?"
echo '{"cwd":"/tmp/nonexistent"}' | CLAUDE_PLUGIN_ROOT=/x python3 pm-strategy/hooks/output_language.py; echo "exit=$?"
rm -rf /tmp/fr-project
```

Expected: no output at all from either, `exit=0` both times.

- [ ] **Step 8: Write `docs/output-language.md`**

Create `docs/output-language.md` (the outer fence here is four backticks because the
content itself contains fenced blocks — write the file without it):

````markdown
# Output language

Skills in this marketplace are written in English. The **deliverables they
produce** follow the language of the project they run in.

## Declaring the language

Create `.config/pm-skills.yaml` at the root of the project where you use the
skills:

```yaml
language: fr
```

Use a short language code (`fr`, `de`, `es`, `ja`, …). `en` — or no file at all —
means English, and nothing is injected.

`.config/` is a convention with room to grow: further per-project settings can be
added there later without a new dotfile in the repo root for each one. Today
`language` is the only key this marketplace reads.

## Resolution order

1. A language the user explicitly asks for in the prompt — always wins.
2. `language:` in `.config/pm-skills.yaml`.
3. English.

The language is **declared, never inferred**. Nothing is read from the language of
existing docs, and `CLAUDE.md` is not a source: two sources that can disagree
reintroduce exactly the inconsistency this removes.

## How it works

Each plugin ships a `SessionStart` hook (`hooks/output_language.py`, wired by
`hooks/hooks.json`). Once per session it reads the settings file and, only when a
non-English language is declared, injects:

> Deliverables produced by PM skills in this project are written in **French**.
> Keep established PM terms (TAM/SAM/SOM, RICE, JTBD, NPS, ICP, OKR)
> untranslated, and preserve template `<!--#anchor-->` comments verbatim. Skill
> instructions and eval cards stay English.

## Why templates carry `<!--#anchor-->` comments

Each `##`/`###` heading in a `template.md` ends with an anchor:

```markdown
## Market Definition <!--#market-definition-->
```

The `PostToolUse` conformance hook checks a produced document against its
skill's template. Matching on English heading text would silently pass any
translated document; matching on the anchor works in any language. The anchor
therefore has to survive into the deliverable. It is invisible in every rendered
view (GitHub, Notion, Confluence, PDF) and visible only when reading raw
markdown — the accepted cost of keeping the structural gate.

Anchors are generated, never hand-written: `just anchors [plugin]`. The linter
rejects a template whose headings lack anchors or whose anchors collide.

## What stays English

`SKILL.md` bodies, eval cards, `template.md` sources, the linter, hooks, and
`scripts/`. Only the produced deliverable is translated.

## Limitations

- With hooks disabled, or a skill used outside Claude Code, no directive is
  injected and output defaults to English. The setting has no effect without the
  hook.
- With all five plugins installed, a non-English project gets the directive five
  times (~4 lines each). The hooks are separate processes racing at startup, so
  there is no clean dedupe.
````

- [ ] **Step 9: Add the README section**

In `README.md`, insert a new section between "## How skills are built" and "## Quality
gates" (four-backtick outer fence again — the section contains a fenced block):

````markdown
## Output language

Skills are authored in English; the documents they produce follow your project's
language. Declare it once at your project root:

```yaml
# .config/pm-skills.yaml
language: fr
```

Established PM terms (TAM/SAM/SOM, RICE, JTBD, NPS, ICP, OKR) stay untranslated.
No file, or `language: en`, means English. See
[`docs/output-language.md`](docs/output-language.md).
````

And in the "## Repository layout" code block, add after the `pm-<quadrant>/` block's `agents/` line:

```
  hooks/hooks.json                 # SessionStart output-language hook
```

- [ ] **Step 10: Document the language-eval pattern in the standard**

In `docs/SKILL-STANDARD.md`, immediately after the "**Coverage:** every skill ships with ≥ 3 cards…" paragraph in §4, add:

```markdown
**Language:** cards are always written in English, and a skill does not need a
per-language card. Where output language is genuinely load-bearing for a skill,
add one card whose `input.context` declares a non-English project and whose
`expected` traits assert the deliverable is in that language, that PM jargon is
untranslated, and that template anchors survive. `market-sizing` carries the
reference card (`evals/market-sizing-fr-project.md`); see
[`docs/output-language.md`](output-language.md).
```

- [ ] **Step 11: Add the reference eval card**

Create `pm-strategy/skills/market-sizing/evals/market-sizing-fr-project.md`:

```markdown
---
id: market-sizing-fr-project
skill: market-sizing
input:
  prompt: "Dimensionne le marché d'un outil de signature électronique pour PME."
  context: "The project declares `language: fr` in .config/pm-skills.yaml. Bottom-up preferred. ~24M EU SMBs. Anchor pricing €15/mo. B2B SaaS, EU-only."
expected:
  - "The whole deliverable — headings, prose, table labels — is written in French"
  - "Keeps TAM, SAM and SOM untranslated as the section labels for the three figures"
  - "Preserves every <!--#anchor--> comment from template.md verbatim on its heading line"
  - "Still reports TAM, SAM and SOM as three distinct numbers with a top-down and a bottom-up TAM reconciled"
  - "States every key assumption explicitly with a source or a caveat and a confidence level"
rubric:
  language_fidelity: 0.30
  structure_preserved: 0.25
  correctness: 0.25
  assumptions_explicit: 0.20
weight: 1.0
---

Language card: the project declares French, so the memo is French but its
structure is unchanged. Guards against the two failure modes that matter — an
English memo in a French project, and a French memo that drops the anchors (or
translates TAM/SAM/SOM) and so escapes the output-conformance hook.

This is the pattern to copy for any skill whose output language is load-bearing;
see docs/output-language.md.
```

- [ ] **Step 12: Run the full gate**

Run: `just test`
Expected: pytest 76 passed; linter `✓ ALL CHECKS PASSED (0 warnings)` — `market-sizing` now reports 4 eval cards, still `>= 3`.

- [ ] **Step 13: Commit**

```bash
git add scripts/skel/output_language.py scripts/skel/hooks.json \
        pm-*/hooks/ \
        tests/test_output_language_hook.py tests/test_hook_copies_identical.py \
        docs/output-language.md README.md docs/SKILL-STANDARD.md \
        pm-strategy/skills/market-sizing/evals/market-sizing-fr-project.md
git commit -F - <<'EOF'
feat(tooling): output-language SessionStart hook

Each plugin now reads `.config/pm-skills.yaml` once per session and, when the
project declares a non-English `language:`, injects a directive telling skills
to write their deliverable in that language, keep PM jargon untranslated, and
preserve template anchors. English projects pay no context cost.

Language is declared, never inferred — one source, no disagreement. Injecting
it beats repeating a language rule across 110 SKILL.md files: it cannot be
forgotten by a skill and costs nothing at generation time.

Adds docs/output-language.md, the README section, the eval pattern in the
standard, and market-sizing's reference French card.

Claude-Session: https://claude.ai/code/session_011SXmVpuW89y4NwJHGgiv5e
EOF
```

- [ ] **Step 14: Final verification**

```bash
git log --oneline -9
just test
uv run python scripts/skillkit.py anchors
```

Expected: nine commits (1 hook + 1 tooling + 5 migration + 1 linter + 1 SessionStart), a green gate, and `anchored 0/110 template(s)` with a clean working tree.

---

## Self-review notes

**Spec coverage.** Every section of `pm-skills-plan/pm-skills-output-language.md` maps to a task: §1 Language resolution → Task 5 (`read_language`, `docs/output-language.md`); §1a SessionStart delivery → Task 5; §2 Anchors in templates → Tasks 2 and 3; §3 Anchor-first conformance hook → Task 1; §4 Linter checks → Task 4; §5 Evals → Task 5 steps 10–11. The spec's "Out of scope" list is respected: no `SKILL.md`/eval/template translation, no per-language variants, no dictionary, no language source beyond the settings file and the prompt, no second settings key.

**Known open items for the reviewer.**
1. The slug rule is effectively frozen the moment Task 3 ships — 816 anchors will exist in git and in already-produced deliverables. Changing it later means a re-migration plus stale anchors in customers' documents.
2. Anchors leak into deliverables by design (spec's "Accepted cost"). Task 3 makes that visible in 110 files at once.
3. Task 3's five migration commits are mechanical and identical in kind; a reviewer approving pm-strategy's diff is effectively approving all five.
