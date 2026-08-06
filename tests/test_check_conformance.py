"""Tests for the skill-scoped output-conformance hook checker."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "check_output_conformance", ROOT / "scripts" / "skel" / "check_output_conformance.py")
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)

TEMPLATE = "# T\n## Market Definition\nx\n## TAM\ny\n## SAM\nz\n## SOM\nw\n"


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
                 "## Market Definition\n## TAM\n## SAM\n## SOM\n")
    code, msg = checker.evaluate(_payload(art), _tmpl(tmp_path))
    assert code == 0 and msg == ""


def test_missing_sections_returns_2_with_names(tmp_path):
    # Has half the sections (Market Definition + TAM) — treated as the artifact — but
    # is missing SAM and SOM.
    art = _write(tmp_path, "memo.md", "## Market Definition\n## TAM\n")
    code, msg = checker.evaluate(_payload(art), _tmpl(tmp_path))
    assert code == 2
    assert "SAM" in msg and "SOM" in msg


def test_unrelated_file_stays_silent(tmp_path):
    # Contains none of the template headings -> not the artifact -> silent.
    art = _write(tmp_path, "notes.md", "# Random notes\nnothing structured here\n")
    code, msg = checker.evaluate(_payload(art), _tmpl(tmp_path))
    assert code == 0 and msg == ""


def test_non_markdown_file_ignored(tmp_path):
    art = _write(tmp_path, "code.py", "print('hi')")
    code, msg = checker.evaluate(_payload(art), _tmpl(tmp_path))
    assert code == 0 and msg == ""


def test_non_write_tool_ignored(tmp_path):
    art = _write(tmp_path, "memo.md", "## Market Definition\n")
    code, msg = checker.evaluate(_payload(art, tool="Read"), _tmpl(tmp_path))
    assert code == 0 and msg == ""


def test_headings_helper():
    assert checker.headings(TEMPLATE) == ["Market Definition", "TAM", "SAM", "SOM"]
