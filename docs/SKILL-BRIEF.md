# SKILL-BRIEF — build one skill fast

Operational quick-reference. Authoritative long-form: `docs/SKILL-STANDARD.md`.
Gold exemplar (read once per session, not per skill):
`pm-strategy/skills/market-sizing/SKILL.md`.

## Frontmatter (all required)
- `name`: kebab-case == directory name
- `description`: `>` block; MUST contain a trigger phrase ("Use when …")
- `version`: `0.1.0` (semver)
- `type`: `component` | `interactive` | `workflow`
- `source`: `original` or `import:phuryn/pm-skills@<sha>` (scaffold pre-fills this)

## Required body sections
- `## Purpose` (+ a **When NOT to use**)
- `## Inputs` (required vs optional; how to elicit if missing)
- `## Output Contract` ⭐ linter-checked — sections + format/length + a GOOD and a BAD excerpt
- `## Process` (numbered; last step = run the Quality Bar)
- `## Quality Bar` (checkbox self-check run before returning)
- `## Validation & Eval` ⭐ linter-checked — points at evals/, states pass bar (≥0.8; −0.05 regression fails)
- `## References`

## template.md
Required when the Output Contract is a structured artifact. `##` headings mirror
the Output Contract sections. Fill it — don't leave scaffold placeholders.

## evals/ (≥ 3 cards: happy + edge + adversarial)
Each card frontmatter: unique `id`, `skill` (== skill name), non-empty `expected`
list, non-empty `rubric` map (weights sum to 1.0).

## IMPORT vs GENERATE
- IMPORT: adapt the phuryn source below (MIT). Restructure into the sections above;
  add Output Contract GOOD/BAD, Quality Bar, evals. Keep `source` SHA as scaffolded.
- GENERATE: write original. `deanpeters` is idea-reference only — never copy its text.

## Done
`just test` passes (or the edit hook is green) AND ≥3 eval cards → `just done <skill>`.
