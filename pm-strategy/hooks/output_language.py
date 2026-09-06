#!/usr/bin/env python3
"""SessionStart hook — declare the project's deliverable language to the model.

Distributed inside each plugin as `<plugin>/hooks/output_language.py` and wired
from `<plugin>/hooks/hooks.json`:

    python3 "${CLAUDE_PLUGIN_ROOT}/hooks/output_language.py"

Reads `.config/pm-skills.yaml` at the project root and, when it declares a
non-English `language:`, injects a one-paragraph directive as additionalContext.
Every PM skill in the session then writes its deliverable in that language —
without a language rule having to be repeated in 110 SKILL.md files.

Language is DECLARED, never inferred: nothing is read from the language of
existing docs, and CLAUDE.md is not a source. Two sources that can disagree
reintroduce the inconsistency this exists to remove.

Parsing is a regex, not PyYAML: hooks are stdlib-only `python3` so they run on an
end user's machine. Fail-open everywhere: anything unexpected emits nothing and
exits 0, so session start is never disturbed.
"""
import json
import os
import re
import sys
from pathlib import Path

SETTINGS_REL = Path(".config") / "pm-skills.yaml"
# Top-level key only — an indented `language:` belongs to some other key.
# The trailing (?:#.*)? tolerates a YAML inline comment after the value.
LANGUAGE_RE = re.compile(r"(?m)^language:[ \t]*(\S+)[ \t]*(?:#.*)?$")
ENGLISH = {"en", "en-us", "en-gb", "eng", "english"}

# Codes worth naming in prose; anything else is passed through as-is.
LANGUAGE_NAMES = {
    "fr": "French", "de": "German", "es": "Spanish", "it": "Italian",
    "pt": "Portuguese", "nl": "Dutch", "pl": "Polish", "sv": "Swedish",
    "da": "Danish", "fi": "Finnish", "ja": "Japanese", "ko": "Korean",
    "zh": "Chinese", "ar": "Arabic", "tr": "Turkish", "ru": "Russian",
}


def project_root(payload: dict) -> Path:
    """The consuming project's root: the env var Claude Code sets, else the
    session's cwd from the hook payload, else the process cwd."""
    for candidate in (os.environ.get("CLAUDE_PROJECT_DIR"), payload.get("cwd")):
        if candidate:
            return Path(candidate)
    return Path.cwd()


def read_language(root: Path) -> str:
    """The declared language code, lowercased.

    Returns "" when no settings file exists, no `language:` key is present, or the
    declared language is English — in all three cases the hook stays silent and
    output defaults to English at no context cost.
    """
    f = root / SETTINGS_REL
    if not f.is_file():
        return ""
    m = LANGUAGE_RE.search(f.read_text(encoding="utf-8"))
    if not m:
        return ""
    lang = m.group(1).strip().strip("\"'").lower()
    return "" if lang in ENGLISH else lang


def directive(lang: str) -> str:
    name = LANGUAGE_NAMES.get(lang, lang)
    return (f"Deliverables produced by PM skills in this project are written in "
            f"**{name}**. Keep established PM terms (TAM/SAM/SOM, RICE, JTBD, NPS, "
            f"ICP, OKR) untranslated, and preserve template `<!--#anchor-->` "
            f"comments verbatim. Skill instructions and eval cards stay English.")


def emit(text: str) -> None:
    """Print the context-injection JSON in the shape the current host consumes.

    Claude Code reads BOTH `additional_context` and `hookSpecificOutput` without
    deduplication, so exactly one field is emitted. Ported from superpowers'
    hooks/session-start.
    """
    if os.environ.get("CURSOR_PLUGIN_ROOT"):
        print(json.dumps({"additional_context": text}))
    elif os.environ.get("CLAUDE_PLUGIN_ROOT") and not os.environ.get("COPILOT_CLI"):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "SessionStart", "additionalContext": text}}))
    else:
        print(json.dumps({"additionalContext": text}))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    try:
        lang = read_language(project_root(payload))
        if lang:
            emit(directive(lang))
    except Exception:
        pass  # fail-open: never disturb session start
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
