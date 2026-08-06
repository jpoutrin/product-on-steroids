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
