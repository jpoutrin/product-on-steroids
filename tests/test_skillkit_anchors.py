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
