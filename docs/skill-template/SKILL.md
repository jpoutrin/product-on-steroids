---
name: skill-name
description: >
  One sentence on what this skill produces. Use when <trigger 1>, <trigger 2>,
  or <trigger 3>.
version: 0.1.0
type: component
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/skill-name/template.md
---

# <Human Title of the Skill>

## Purpose
What this skill produces and the decision it supports.

**When NOT to use:** <the adjacent situations this skill should decline and
hand off to a different skill.>

## Inputs
- **Required:** <input> — <how to elicit if the user didn't provide it>
- **Optional:** <input> — <default behavior if absent>

## Output Contract
The deliverable is <artifact>, structured as:

1. **<Section>** — <what goes here, format, length>
2. **<Section>** — <...>

See `template.md` for the fill-in structure.

**GOOD (excerpt):**
> <short filled example that meets the contract>

**BAD (excerpt):**
> <short example that violates the contract> — fails because <one line>.

## Process
1. <step>
2. <step>
3. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] <checkable statement 1>
- [ ] <checkable statement 2>
- [ ] <checkable statement 3>
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References
- <neutral link or framework name>
