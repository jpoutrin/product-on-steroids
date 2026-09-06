"""Tests for the pure shape layer used by the output-conformance hook."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "md_shape", ROOT / "scripts" / "skel" / "md_shape.py")
ms = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ms)


def test_headings_become_sections_in_order():
    md = "# Title\n## A\ntext\n## B\nmore\n"
    assert [(s.depth, s.text) for s in ms.parse_sections(md)] == [(2, "A"), (2, "B")]


def test_h1_and_h4_are_not_sections():
    md = "# Title\n## A\n#### Deep\n### B\n"
    assert [(s.depth, s.text) for s in ms.parse_sections(md)] == [(2, "A"), (3, "B")]


def test_preamble_before_first_heading_is_dropped():
    md = "# Title\n**Persona:** someone\n\n## A\ntext\n"
    out = ms.parse_sections(md)
    assert len(out) == 1 and out[0].blocks == ("para",)


def test_block_kinds_are_detected():
    md = ("## A\npara text\n- bullet\n1. numbered\n> quote\n")
    # consecutive list kinds collapse into one "list"
    assert ms.parse_sections(md)[0].blocks == ("para", "list", "quote")


def test_consecutive_same_kind_collapses():
    md = "## A\nline one\nline two\nline three\n"
    assert ms.parse_sections(md)[0].blocks == ("para",)


def test_table_records_its_column_count():
    md = ("## Summary\n"
          "| Metric | Current | Projection |\n"
          "|--------|---------|------------|\n"
          "| TAM    | <...>   | <...>      |\n")
    assert ms.parse_sections(md)[0].blocks == ("table:3",)


def test_table_without_trailing_pipe_counts_the_same():
    md = "## S\n| A | B | C\n"
    assert ms.parse_sections(md)[0].blocks == ("table:3",)


def test_fenced_code_is_one_code_block_and_hides_headings():
    md = "## A\n```\n## not a heading\n```\ntail\n"
    out = ms.parse_sections(md)
    assert len(out) == 1
    assert out[0].blocks == ("code", "para")


def test_tilde_fence_is_handled():
    md = "## A\n~~~\n## not a heading\n~~~\n"
    assert len(ms.parse_sections(md)) == 1


def test_unterminated_fence_is_not_a_fence():
    # A malformed template must not swallow the rest of the file: over-report
    # headings rather than silently exempt them.
    md = "## A\n```\n## Real B\n"
    assert [s.text for s in ms.parse_sections(md)] == ["A", "Real B"]


def test_html_comments_are_skipped():
    md = "## A\n<!-- guidance for the author -->\npara\n"
    assert ms.parse_sections(md)[0].blocks == ("para",)


def test_multiline_html_comment_is_skipped():
    md = "## A\n<!--\nline one\nline two\n-->\npara\n"
    assert ms.parse_sections(md)[0].blocks == ("para",)


def test_blank_lines_produce_no_blocks():
    assert ms.parse_sections("## A\n\n\n") == [ms.Section(2, "A", ())]


def test_table_with_doubled_boundary_pipe_counts_empty_cell():
    md = "## S\n|| B | C |\n"
    assert ms.parse_sections(md)[0].blocks == ("table:3",)


def test_table_with_escaped_pipe_does_not_add_a_column():
    md = "## S\n| A | B\\| esc | C |\n"
    assert ms.parse_sections(md)[0].blocks == ("table:3",)


def test_unterminated_html_comment_does_not_swallow_a_heading():
    # Same failure class as an unterminated fence: a stray `<!--` must not
    # silently drop the rest of the document.
    md = "## A\n<!-- never closes\n## B\n"
    assert [s.text for s in ms.parse_sections(md)] == ["A", "B"]


def test_real_template_parses(tmp_path):
    md = (ROOT / "pm-strategy" / "skills" / "market-sizing" / "template.md"
          ).read_text(encoding="utf-8")
    out = ms.parse_sections(md)
    assert len(out) == 8
    assert out[0].depth == 2
    assert any(b.startswith("table:") for s in out for b in s.blocks)
