"""Tests for the SessionStart output-language hook."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "output_language", ROOT / "scripts" / "skel" / "output_language.py")
hook = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hook)


def _settings(tmp_path, text):
    d = tmp_path / ".config"
    d.mkdir(exist_ok=True)
    (d / "pm-skills.yaml").write_text(text, encoding="utf-8")
    return tmp_path


def test_no_settings_file_declares_nothing(tmp_path):
    assert hook.read_language(tmp_path) == ""


def test_french_is_declared(tmp_path):
    assert hook.read_language(_settings(tmp_path, "language: fr\n")) == "fr"


def test_quoted_and_uppercased_value_is_normalised(tmp_path):
    assert hook.read_language(_settings(tmp_path, 'language: "FR"\n')) == "fr"


def test_english_declares_nothing(tmp_path):
    for value in ("en", "EN", "en-US", "english"):
        assert hook.read_language(_settings(tmp_path, f"language: {value}\n")) == "", value


def test_other_keys_are_ignored(tmp_path):
    root = _settings(tmp_path, "currency: EUR\nregion: emea\n")
    assert hook.read_language(root) == ""


def test_language_key_found_among_other_keys(tmp_path):
    root = _settings(tmp_path, "# project settings\ncurrency: EUR\nlanguage: de\n")
    assert hook.read_language(root) == "de"


def test_indented_language_key_is_not_a_declaration(tmp_path):
    # Only a top-level `language:` counts; a nested one belongs to another key.
    root = _settings(tmp_path, "other:\n  language: fr\n")
    assert hook.read_language(root) == ""


def test_trailing_comment_is_stripped(tmp_path):
    root = _settings(tmp_path, "language: fr  # comment\n")
    assert hook.read_language(root) == "fr"


def test_directive_names_the_language_and_the_rules():
    d = hook.directive("fr")
    assert "**French**" in d
    assert "TAM/SAM/SOM" in d and "RICE" in d and "OKR" in d
    assert "stay English" in d


def test_directive_falls_back_to_the_raw_code():
    assert "**nb**" in hook.directive("nb")


def test_project_root_prefers_the_env_var(tmp_path, monkeypatch):
    monkeypatch.setenv("CLAUDE_PROJECT_DIR", str(tmp_path / "env"))
    assert hook.project_root({"cwd": str(tmp_path / "payload")}) == tmp_path / "env"


def test_project_root_falls_back_to_payload_cwd(tmp_path, monkeypatch):
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    assert hook.project_root({"cwd": str(tmp_path)}) == tmp_path


def test_project_root_falls_back_to_cwd(monkeypatch):
    monkeypatch.delenv("CLAUDE_PROJECT_DIR", raising=False)
    assert hook.project_root({}) == Path.cwd()


def test_emit_uses_claude_code_shape(monkeypatch, capsys):
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", "/x")
    monkeypatch.delenv("CURSOR_PLUGIN_ROOT", raising=False)
    monkeypatch.delenv("COPILOT_CLI", raising=False)
    hook.emit("hello")
    out = json.loads(capsys.readouterr().out)
    assert out["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    assert out["hookSpecificOutput"]["additionalContext"] == "hello"


def test_emit_uses_cursor_shape(monkeypatch, capsys):
    monkeypatch.setenv("CURSOR_PLUGIN_ROOT", "/x")
    hook.emit("hello")
    assert json.loads(capsys.readouterr().out) == {"additional_context": "hello"}


def test_emit_uses_sdk_shape_for_copilot(monkeypatch, capsys):
    monkeypatch.delenv("CURSOR_PLUGIN_ROOT", raising=False)
    monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", "/x")
    monkeypatch.setenv("COPILOT_CLI", "1")
    hook.emit("hello")
    assert json.loads(capsys.readouterr().out) == {"additionalContext": "hello"}


def test_hooks_json_wires_the_script():
    cfg = json.loads((ROOT / "scripts" / "skel" / "hooks.json").read_text())
    entry = cfg["hooks"]["SessionStart"][0]["hooks"][0]
    assert entry["type"] == "command"
    assert "hooks/output_language.py" in entry["command"]
    assert "${CLAUDE_PLUGIN_ROOT}" in entry["command"]
