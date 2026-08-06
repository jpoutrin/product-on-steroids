# Changelog

All notable changes to this marketplace are documented here. The format loosely
follows [Keep a Changelog](https://keepachangelog.com/); versions follow semver.

## Unreleased

### Added
- Marketplace skeleton: `marketplace.json`, five plugins (`pm-strategy`, `pm-discovery`, `pm-gtm`, `pm-execution`, `pm-influence`) with `plugin.json`, README, MIT LICENSE, `.gitignore`.
- Skill authoring standard (`docs/SKILL-STANDARD.md`) and copy-me `docs/skill-template/`.
- Structural linter `tests/validate_plugins.py` (forked from phuryn/pm-skills, extended to require Output Contract + Validation & Eval sections).
- Skill task ledger `TASKS.md`.
- `pm-strategy/market-sizing` — first skill (gold exemplar), adapted from phuryn/pm-skills.
- Quadrant anchor agents (`cpo`, `product-discovery-specialist`, `gtm-strategist`, `delivery-lead`, `product-influence-partner`) and the `pm-orchestrator` router stub.
