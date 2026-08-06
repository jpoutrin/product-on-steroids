import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import validate_one

def test_skill_dir_for_finds_enclosing_skill(tmp_path):
    d = tmp_path / "pm-x" / "skills" / "foo"
    (d / "evals").mkdir(parents=True)
    (d / "SKILL.md").write_text("---\nname: foo\n---\n")
    assert validate_one.skill_dir_for(str(d / "SKILL.md")) == str(d)
    assert validate_one.skill_dir_for(str(d / "evals" / "foo-happy.md")) == str(d)

def test_skill_dir_for_ignores_unrelated_path(tmp_path):
    p = tmp_path / "README.md"
    p.write_text("x")
    assert validate_one.skill_dir_for(str(p)) is None

def test_run_is_fail_open_on_garbage():
    assert validate_one.run({}) == 0
    assert validate_one.run({"tool_input": {"file_path": "/nope/x.md"}}) == 0
