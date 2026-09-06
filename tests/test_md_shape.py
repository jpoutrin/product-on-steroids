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


def test_collapse_keeps_a_non_repeating_template_intact():
    secs = ms.parse_sections("## A\n## B\n## C\n")
    assert ms.collapse_repeats(secs) == secs


def test_collapse_reduces_a_numbered_family_to_one():
    md = "## Frame 1 — <Title>\n## Frame 2 — <Title>\n## Frame 3 — <Title>\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [s.text for s in out] == ["Frame 1 — <Title>"]


def test_collapse_carries_nested_children_with_the_family_head():
    md = ("## Frame 1 — <T>\n### Scene\n### Action\n"
          "## Frame 2 — <T>\n### Scene\n### Action\n"
          "## Takeaways\n")
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [(s.depth, s.text) for s in out] == [
        (2, "Frame 1 — <T>"), (3, "Scene"), (3, "Action"), (2, "Takeaways")]


def test_collapse_needs_three_in_a_row_is_false_two_is_enough():
    md = "## Segment 1: <Name>\n## Segment 2: <Name>\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [s.text for s in out] == ["Segment 1: <Name>"]


def test_collapse_ignores_headings_that_differ_by_more_than_digits():
    md = "## Frame 1 — <T>\n## Summary\n## Frame 2 — <T>\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert len(out) == 3


def test_collapse_requires_matching_child_shape():
    # Same normalised head, but the second unit has a different child depth
    # sequence — not a repeat of the first.
    md = "## Step 1\n### Detail\n## Step 2\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [s.text for s in out] == ["Step 1", "Detail", "Step 2"]


def test_collapse_reaches_repeats_nested_inside_a_unit():
    # The second repeat shape: one `##` bucket whose `###` children repeat.
    # Only the recursion inside collapse_repeats sees these.
    md = "## Themes\n### <Theme 1>\n- a\n### <Theme 2>\n- a\n### <Theme 3>\n- a\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [(s.depth, s.text) for s in out] == [(2, "Themes"), (3, "<Theme 1>")]


def test_collapse_strips_an_inline_anchor_from_the_heading_name():
    # Anchors still exist until Task 6; they must not leak into a section's name.
    md = "## Priority 1: <Theme> <!--#priority-1-theme-->\n- a\n"
    assert ms.parse_sections(md)[0].text == "Priority 1: <Theme>"


def test_collapse_on_the_real_storyboard_template():
    md = (ROOT / "pm-discovery" / "skills" / "storyboard" / "template.md"
          ).read_text(encoding="utf-8")
    full = ms.parse_sections(md)
    out = ms.collapse_repeats(full)
    # 5 frames × (1 head + 4 children) + 1 takeaways = 26 -> 1 frame unit + takeaways
    assert len(full) == 26
    assert len(out) == 6
    assert [s.depth for s in out] == [2, 3, 3, 3, 3, 2]


def test_collapse_merges_headings_differing_only_by_a_non_index_digit():
    """Known limitation, deliberately accepted.

    `_signature` normalises every digit run, so two adjacent sections whose
    headings differ only by a number merge even when the number is content
    rather than an index. Tightening this to require a 1,2,3 sequence would
    break real templates: user-story-mapping and user-story-splitting both
    pair "Release 2 / Release N" and "Story 2 / Story N", where N is a literal
    "and so on" placeholder and the family is genuine.

    The failure direction is under-enforcement of one section, never a false
    error. Pinned here so any future tightening is a deliberate change.
    """
    md = "## Top 10 Risks\n- a\n## Top 3 Risks\n- a\n"
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [s.text for s in out] == ["Top 10 Risks"]


def test_collapse_handles_the_and_so_on_placeholder_idiom():
    # "Release 2" followed by "Release N" is a genuine family: N is a literal
    # placeholder meaning "and so on". Two shipped templates rely on this.
    md = ("## Release 1 — <Scope>\n- a\n## Release 2 — <Scope>\n- a\n"
          "## Release N — <Scope>\n- a\n")
    out = ms.collapse_repeats(ms.parse_sections(md))
    assert [s.text for s in out] == ["Release 1 — <Scope>"]
