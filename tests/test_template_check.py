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

def test_unreferenced_template_with_fewer_headings_is_silent(tmp_path):
    # SKILL.md does NOT reference template.md, but a template.md exists with
    # fewer headings than the Output Contract — must stay silent.
    skill = ("---\nname: x\n---\n## Output Contract\n"
             "1. **A** — a\n2. **B** — b\nAdvisory, no template reference.\n"
             "## Validation & Eval\n")
    d = _mk(tmp_path, skill, template_md="# T\n## only-one\n")
    r = vp.validate_template(d, skill)
    assert not r.errors and not r.warnings
