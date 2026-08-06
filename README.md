# product-on-steroids

A **Claude Code plugin marketplace dedicated to product-management best practice**. It packages structured PM workflows as skills and agents, organized on the four quadrants of the Peak Product Manager framework (Ravi Mehta), across five plugins.

## Plugins

| Plugin | Quadrant | What it covers |
|--------|----------|----------------|
| `pm-strategy` | Product Strategy | Business outcomes, vision & roadmap, market sizing, competitive analysis, positioning, macro frameworks |
| `pm-discovery` | Customer Insight | Interviews & synthesis, opportunity-solution trees, assumptions & experiments, personas, journeys, analytics |
| `pm-gtm` | Go-to-Market | GTM strategy & motions, ICP & beachhead, positioning, growth loops, battlecards |
| `pm-execution` | Product Execution | PRDs, user stories, story mapping/splitting, sprint planning, pre-mortems, retros, test scenarios |
| `pm-influence` | Influencing People | Managing up, stakeholder management, team leadership, exec updates, decision memos, escalation |

Each plugin exposes **skills** (auto-loaded when the topic matches) and an **anchor agent** for that quadrant. A cross-cutting `pm-orchestrator` routes multi-quadrant work.

## Install

```bash
# From within Claude Code
/plugin marketplace add /path/to/product-on-steroids
/plugin install pm-strategy@product-on-steroids
```

Or add the remote once published:

```bash
/plugin marketplace add jpoutrin/product-on-steroids
```

## How skills are built

- **Imports** are adapted from the MIT-licensed [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills); each records its provenance in the SKILL.md `source:` field.
- **Original** skills are written to this repo's house standard. `deanpeters/Product-Manager-Skills` is used as *idea reference only* (its CC BY-NC-SA license means no text is copied).
- Every skill follows [`docs/SKILL-STANDARD.md`](docs/SKILL-STANDARD.md): an explicit **Output Contract**, a self-check **Quality Bar**, and `evals/` scenario cards.
- Skills ship **one commit at a time**. Progress is tracked in [`TASKS.md`](TASKS.md).

## Quality gates

Tooling is managed with [`uv`](https://docs.astral.sh/uv/). From the repo root:

```bash
uv run validate-plugins            # structural lint (or: uv run python tests/validate_plugins.py)
```

- **Structural lint** — blocking; checks manifests, frontmatter, and required skill sections. Exits non-zero on any error.
- **Output eval** (Langfuse) — regression gate over each skill's `evals/` cards. *Wiring deferred until credentials are provided.*

## Repository layout

```
.claude-plugin/marketplace.json   # lists the 5 plugins
pm-<quadrant>/
  .claude-plugin/plugin.json
  skills/<skill>/SKILL.md          # + template.md + evals/*.md
  agents/<anchor-agent>.md
docs/SKILL-STANDARD.md             # house authoring standard + skill-template/
tests/validate_plugins.py          # structural linter
TASKS.md                           # skill-by-skill ledger
pm-skills-plan/                    # design docs
work/                              # cloned source repos (gitignored, not shipped)
```

## License

MIT — see [LICENSE](LICENSE).
