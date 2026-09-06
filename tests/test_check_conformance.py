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


def test_headings_helper_captures_level3():
    md = "# T\n## Create Value\n### Key Partnerships\n### Key Activities\n#### too-deep\n"
    # h2 + h3 captured, in order; h1 and h4 ignored.
    assert checker.headings(md) == ["Create Value", "Key Partnerships", "Key Activities"]


def test_grouped_canvas_artifact_is_silent(tmp_path):
    # Template groups sections as `###` under `##` buckets; a conformant artifact
    # containing all of them (h2 + h3) must stay silent.
    tmpl = _write(tmp_path, "template.md",
                  "## Create Value\n### Key Partnerships\n### Key Activities\n")
    art = _write(tmp_path, "canvas.md",
                 "## Create Value\n### Key Partnerships\n### Key Activities\n")
    code, msg = checker.evaluate(_payload(art), tmpl)
    assert code == 0 and msg == ""


def test_grouped_canvas_missing_level3_is_flagged(tmp_path):
    # Artifact has the bucket + one block but drops a `###` block -> flagged.
    tmpl = _write(tmp_path, "template.md",
                  "## Create Value\n### Key Partnerships\n### Key Activities\n")
    art = _write(tmp_path, "canvas.md", "## Create Value\n### Key Partnerships\n")
    code, msg = checker.evaluate(_payload(art), tmpl)
    assert code == 2
    assert "Key Activities" in msg


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


def test_anchor_mode_flags_english_headings_without_anchors(tmp_path):
    # An English artifact that dropped the anchors IS recognised — the threshold
    # counts a section by anchor or by heading text — and every anchorless section
    # is reported, so the next edit restores the anchors.
    art = _write(tmp_path, "memo.md",
                 "## Market Definition\n## TAM\n## SAM <!--#sam-->\n")
    code, msg = checker.evaluate(_payload(art), _anchored_tmpl(tmp_path))
    assert code == 2
    assert "Market Definition" in msg and "TAM" in msg and "SOM" in msg
    assert "anchor" in msg.lower()


def test_legacy_english_deliverable_without_anchors_is_flagged(tmp_path):
    # A document produced before the template gained anchors: every English heading
    # matches textually, none carries an anchor. It must not fall silently out of
    # enforcement — it is recognised and told to copy every anchor.
    art = _write(tmp_path, "memo.md",
                 "# Memo\n## Market Definition\nx\n## TAM\ny\n"
                 "## SAM\nz\n## SOM\nw\n")
    code, msg = checker.evaluate(_payload(art), _anchored_tmpl(tmp_path))
    assert code == 2
    for section in ("Market Definition", "TAM", "SAM", "SOM"):
        assert section in msg
    assert "anchor" in msg.lower()


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
