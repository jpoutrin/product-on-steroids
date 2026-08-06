# product-on-steroids — task runner (https://github.com/casey/just)
# Tooling is managed with uv. Run `just` to list recipes.

# Show available recipes
default:
    @just --list

# Create the uv-managed virtualenv and install project + dev deps
setup:
    uv sync

# Run the structural skill linter (blocking; exits non-zero on any error)
test:
    uv run validate-plugins

# ── Skill authoring (token-lean helpers; see docs/SKILL-BRIEF.md) ──

# Print the next todo skill in build order
next:
    uv run python scripts/skillkit.py next

# Show build progress per plugin
progress:
    uv run python scripts/skillkit.py progress

# Scaffold a skill dir from its TASKS.md row: just scaffold market-sizing
scaffold skill:
    uv run python scripts/skillkit.py scaffold {{skill}}

# Print the one-shot build pack for a skill: just context market-sizing
context skill:
    uv run python scripts/skillkit.py context {{skill}}

# Mark a skill in-progress in TASKS.md
wip skill:
    uv run python scripts/skillkit.py wip {{skill}}

# Mark a skill done (runs the linter gate first)
done skill:
    uv run python scripts/skillkit.py done {{skill}}
