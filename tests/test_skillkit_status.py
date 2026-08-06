import pytest
import skillkit

LEDGER = ("## pm-strategy — X\n\n| Skill | Disposition | Priority | Status |\n"
          "|--|--|--|--|\n| product-vision | IMPORT | P1 | todo |\n")

def test_set_status_flips_only_target_row():
    out = skillkit.set_status(LEDGER, "product-vision", "wip")
    assert "| product-vision | IMPORT | P1 | wip |" in out
    assert out.count("wip") == 1

def test_set_status_unknown_raises():
    with pytest.raises(KeyError):
        skillkit.set_status(LEDGER, "nope", "wip")

def test_done_refuses_when_lint_fails(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(skillkit, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(skillkit, "TASKS_PATH", tmp_path / "TASKS.md")
    (tmp_path / "TASKS.md").write_text(LEDGER)
    skilldir = tmp_path / "pm-strategy" / "skills" / "product-vision"
    (skilldir / "evals").mkdir(parents=True)
    (skilldir / "SKILL.md").write_text("---\nname: product-vision\n---\nincomplete\n")
    rc = skillkit.cmd_done(["product-vision"])
    assert rc == 1
    assert "not done" in capsys.readouterr().err.lower()
    # status must NOT have flipped
    assert "| product-vision | IMPORT | P1 | todo |" in (tmp_path / "TASKS.md").read_text()
