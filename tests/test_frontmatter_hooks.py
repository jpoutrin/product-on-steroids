"""The mini frontmatter parser must survive a nested `hooks:` block without losing
the required scalar fields — skills now ship a skill-scoped conformance hook."""
import validate_plugins as vp

SKILL_WITH_HOOKS = """---
name: market-sizing
description: >
  Estimate market size. Use when sizing a market.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a9
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/market-sizing/template.md
---
# body
"""


def test_scalar_fields_survive_hooks_block():
    fm = vp.parse_frontmatter(SKILL_WITH_HOOKS)
    assert fm is not None
    assert fm["name"] == "market-sizing"
    assert fm["type"] == "component"
    assert fm["source"] == "import:phuryn/pm-skills@18468a9"
    assert fm["description"]  # non-empty folded block still captured
