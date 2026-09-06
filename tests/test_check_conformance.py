"""Tests for the skill-scoped output-conformance hook checker."""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "skel"))   # so the hook finds md_shape
_spec = importlib.util.spec_from_file_location(
    "check_output_conformance", ROOT / "scripts" / "skel" / "check_output_conformance.py")
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)

# Each section has a DIFFERENT block kind, so alignment has exactly one best
# answer and a test can assert which section was reported missing. Four sections
# that all held a bullet list would be interchangeable to a shape matcher — see
# the "coarse shape is coarse" risk in the spec.
TEMPLATE = ("# T\n"
            "## Market Definition\n- a\n"
            "## TAM\nprose\n"
            "## SAM\n| A | B |\n|---|---|\n"
            "## SOM\n> q\n")


def _payload(file_path, tool="Write"):
    return {"tool_name": tool, "tool_input": {"file_path": file_path}}


def _write(tmp_path, name, text):
    p = tmp_path / name
    p.write_text(text, encoding="utf-8")
    return str(p)


def _tmpl(tmp_path):
    return _write(tmp_path, "template.md", TEMPLATE)


def test_conformant_artifact_is_silent(tmp_path):
    art = _write(tmp_path, "memo.md",
                 "## Market Definition\n- a\n## TAM\nprose\n"
                 "## SAM\n| A | B |\n|---|---|\n## SOM\n> q\n")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_french_artifact_with_no_markers_is_silent(tmp_path):
    # The whole point: same shape, entirely different words, nothing to preserve.
    art = _write(tmp_path, "memo.md",
                 "## Définition du marché\n- a\n## Marché total\nprose\n"
                 "## Marché adressable\n| A | B |\n|---|---|\n"
                 "## Marché obtenable\n> q\n")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_missing_section_is_flagged_and_named_from_the_template(tmp_path):
    # The table section is gone; the other three still align by block kind.
    art = _write(tmp_path, "memo.md",
                 "## Définition du marché\n- a\n## Marché total\nprose\n"
                 "## Marché obtenable\n> q\n")
    code, msg = checker.evaluate(_payload(art), _tmpl(tmp_path))
    assert code == 2
    assert "SAM" in msg               # named in English, from the template
    assert "TAM" in msg               # its neighbour, to locate it
    assert "SOM" in msg               # its other neighbour


def test_unrelated_file_stays_silent(tmp_path):
    art = _write(tmp_path, "notes.md", "# Random notes\nnothing structured here\n")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_non_markdown_file_ignored(tmp_path):
    art = _write(tmp_path, "code.py", "print('hi')")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_non_write_tool_ignored(tmp_path):
    art = _write(tmp_path, "memo.md", TEMPLATE)
    assert checker.evaluate(_payload(art, tool="Read"), _tmpl(tmp_path)) == (0, "")


def test_missing_template_is_silent(tmp_path):
    art = _write(tmp_path, "memo.md", TEMPLATE)
    assert checker.evaluate(_payload(art), str(tmp_path / "nope.md")) == (0, "")


def test_repeating_template_accepts_fewer_instances(tmp_path):
    # The regression this change exists to kill: a 5-frame template must not
    # force a 3-frame document.
    tmpl = _write(tmp_path, "template.md",
                  "".join(f"## Frame {i} — <T>\n### Scene\n- s\n### Action\n- a\n"
                          for i in range(1, 6)) + "## Takeaways\n- t\n")
    art = _write(tmp_path, "story.md",
                 "".join(f"## Scène {i}\n### Décor\n- s\n### Action\n- a\n"
                         for i in range(1, 4)) + "## Conclusions\n- t\n")
    assert checker.evaluate(_payload(art), tmpl) == (0, "")


def test_repeating_template_still_requires_one_instance(tmp_path):
    tmpl = _write(tmp_path, "template.md",
                  "".join(f"## Frame {i} — <T>\n### Scene\n- s\n### Action\n- a\n"
                          for i in range(1, 6)) + "## Takeaways\n- t\n")
    art = _write(tmp_path, "story.md", "## Conclusions\n- t\n")
    # Only 1 of 4 collapsed requirements matches -> below half -> not the deliverable.
    assert checker.evaluate(_payload(art), tmpl) == (0, "")


def test_grouped_canvas_missing_level3_is_flagged(tmp_path):
    tmpl = _write(tmp_path, "template.md",
                  "## Create Value\n- x\n### Key Partnerships\n- p\n### Key Activities\n- a\n")
    art = _write(tmp_path, "canvas.md",
                 "## Créer de la valeur\n- x\n### Partenariats\n- p\n")
    code, msg = checker.evaluate(_payload(art), tmpl)
    assert code == 2 and "Key Activities" in msg


def test_extra_document_sections_are_not_errors(tmp_path):
    art = _write(tmp_path, "memo.md",
                 "## Market Definition\n- a\n## Bonus\n- z\n## TAM\nprose\n"
                 "## SAM\n| A | B |\n|---|---|\n## SOM\n> q\n")
    assert checker.evaluate(_payload(art), _tmpl(tmp_path)) == (0, "")


def test_project_root_prefers_the_env_var(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path / "env"))
    assert checker.project_root({"cwd": str(tmp_path / "payload")}) == tmp_path / "env"


def test_project_root_falls_back_to_payload_cwd(tmp_path, monkeypatch):
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    assert checker.project_root({"cwd": str(tmp_path)}) == tmp_path


def test_project_root_falls_back_to_process_cwd(monkeypatch):
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    assert checker.project_root({}) == Path.cwd()


def test_resolve_template_returns_the_plugin_template_by_default(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    plugin = _write(tmp_path, "template.md", TEMPLATE)
    assert checker.resolve_template({}, plugin) == Path(plugin)


def test_resolve_template_prefers_a_project_override(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    skill_dir = tmp_path / "plugin" / "skills" / "market-sizing"
    skill_dir.mkdir(parents=True)
    plugin = skill_dir / "template.md"
    plugin.write_text(TEMPLATE, encoding="utf-8")
    override = tmp_path / ".config" / "pm-skills" / "market-sizing" / "template.md"
    override.parent.mkdir(parents=True)
    override.write_text("## Autre\n- x\n", encoding="utf-8")
    assert checker.resolve_template({}, str(plugin)) == override


def test_a_project_override_is_what_gets_enforced(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path))
    skill_dir = tmp_path / "plugin" / "skills" / "market-sizing"
    skill_dir.mkdir(parents=True)
    plugin = skill_dir / "template.md"
    plugin.write_text(TEMPLATE, encoding="utf-8")   # 4 sections
    override = tmp_path / ".config" / "pm-skills" / "market-sizing" / "template.md"
    override.parent.mkdir(parents=True)
    override.write_text("## Un\n- a\n## Deux\n- b\n", encoding="utf-8")  # 2 sections
    art = _write(tmp_path, "memo.md", "## Un\n- a\n## Deux\n- b\n")
    # Conformant to the override, though it has only half the plugin's sections.
    assert checker.evaluate({"tool_name": "Write",
                             "tool_input": {"file_path": art}}, str(plugin)) == (0, "")
