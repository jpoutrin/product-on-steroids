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

def test_no_template_reference_is_silent(tmp_path):
    skill = "---\nname: x\n---\n## Output Contract\nAdvisory only.\n## Validation & Eval\n"
    d = _mk(tmp_path, skill, template_md=None)
    r = vp.validate_template(d, skill)
    assert not r.errors and not r.warnings

def test_unreferenced_template_with_fewer_headings_is_silent(tmp_path):
    # SKILL.md does NOT reference template.md, but a template.md exists with
    # fewer headings than the Output Contract — must stay silent.
    skill = ("---\nname: x\n---\n## Output Contract\n"
             "1. **A** — a\n2. **B** — b\nAdvisory, no template reference.\n"
             "## Validation & Eval\n")
    d = _mk(tmp_path, skill, template_md="# T\n## only-one\n")
    r = vp.validate_template(d, skill)
    assert not r.errors and not r.warnings


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


def test_heading_inside_fence_is_not_counted_or_anchored(tmp_path):
    # A fenced markdown example containing `## ...` is illustrative content. It
    # must not be counted as a heading, so it must not be demanded an anchor.
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md=("# T\n## A <!--#a-->\n## B <!--#b-->\n"
                         "```markdown\n## Example Heading\n```\n"))
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert not r.errors and not r.warnings


def test_duplicate_anchor_inside_fence_is_not_flagged(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md=("# T\n## A <!--#a-->\n## B <!--#b-->\n"
                         "~~~\n## A <!--#a-->\n~~~\n"))
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert not r.errors and not r.warnings


def test_unanchored_heading_outside_fences_is_still_an_error(tmp_path):
    # Guard the guard: fence-awareness must not disable the anchor rule itself.
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md=("# T\n## A <!--#a-->\n## B\n"
                         "```markdown\n## Example Heading\n```\n"))
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert any("anchor" in e for e in r.errors)


def test_unterminated_backtick_fence_headings_are_still_counted(tmp_path):
    # An unclosed ``` fence is a malformed template, not a real fence: a heading
    # after it must still be counted (and demanded an anchor) rather than being
    # silently swallowed into the "fenced" region for the rest of the file.
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md=("# T\n## A <!--#a-->\n"
                         "```\n## Inside unterminated fence\n## B\n"))
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert any("anchor" in e for e in r.errors)


def test_unterminated_tilde_fence_headings_are_still_counted(tmp_path):
    d = _mk(tmp_path, SKILL_WITH_TEMPLATE,
            template_md=("# T\n## A <!--#a-->\n"
                         "~~~\n## Inside unterminated fence\n## B\n"))
    r = vp.validate_template(d, SKILL_WITH_TEMPLATE)
    assert any("anchor" in e for e in r.errors)
