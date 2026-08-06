import shutil
import skillkit

def test_import_source_values():
    assert skillkit.import_source("GENERATE", "roadmap-planning") == "original"
    assert skillkit.import_source("IMPORT", "product-vision") == \
        "import:phuryn/pm-skills@18468a9"

def test_scaffold_creates_filled_skill(tmp_path, monkeypatch):
    # Redirect the repo layout into tmp_path
    monkeypatch.setattr(skillkit, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(skillkit, "TASKS_PATH", tmp_path / "TASKS.md")
    tmpl = tmp_path / "docs" / "skill-template"
    monkeypatch.setattr(skillkit, "TEMPLATE_DIR", tmpl)
    # Minimal template mirroring docs/skill-template/
    (tmpl / "evals").mkdir(parents=True)
    (tmpl / "SKILL.md").write_text(
        "---\nname: skill-name\nversion: 0.1.0\ntype: component\nsource: original\n---\n# T\n")
    (tmpl / "template.md").write_text("# <Artifact Title>\n## <Section 1>\n")
    (tmpl / "evals" / "example.md").write_text(
        "---\nid: skill-name-happy\nskill: skill-name\n---\nnote\n")
    (tmp_path / "TASKS.md").write_text(
        "## pm-strategy — X\n\n| Skill | Disposition | Priority | Status |\n"
        "|--|--|--|--|\n| product-vision | IMPORT | P1 | todo |\n")

    rc = skillkit.cmd_scaffold(["product-vision"])
    assert rc == 0
    dest = tmp_path / "pm-strategy" / "skills" / "product-vision"
    skill_md = (dest / "SKILL.md").read_text()
    assert "name: product-vision" in skill_md
    assert "source: import:phuryn/pm-skills@18468a9" in skill_md
    evals = sorted(p.name for p in (dest / "evals").iterdir())
    assert evals == ["product-vision-adversarial.md",
                     "product-vision-edge.md", "product-vision-happy.md"]
    happy = (dest / "evals" / "product-vision-happy.md").read_text()
    assert "id: product-vision-happy" in happy
    assert "skill: product-vision" in happy
    assert not (dest / "evals" / "example.md").exists()

def test_scaffold_refuses_existing(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(skillkit, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(skillkit, "TASKS_PATH", tmp_path / "TASKS.md")
    (tmp_path / "TASKS.md").write_text(
        "## pm-strategy — X\n\n| Skill | Disposition | Priority | Status |\n"
        "|--|--|--|--|\n| product-vision | IMPORT | P1 | todo |\n")
    dest = tmp_path / "pm-strategy" / "skills" / "product-vision"
    dest.mkdir(parents=True)
    rc = skillkit.cmd_scaffold(["product-vision"])
    assert rc == 1
    assert "exists" in capsys.readouterr().err
