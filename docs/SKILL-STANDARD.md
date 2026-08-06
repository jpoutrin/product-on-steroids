# Skill Authoring Standard

Every skill in this marketplace follows this standard. It exists to make skills
**predictable to use** (an explicit Output Contract), **self-correcting** (a
Quality Bar the skill runs before returning), and **testable** (eval scenario
cards). The structural linter (`tests/validate_plugins.py`) enforces the
machine-checkable parts; reviewers enforce the rest.

To create a new skill, copy [`skill-template/`](skill-template/) into
`<plugin>/skills/<skill-name>/` and fill it in.

---

## 1. Directory layout

```
<plugin>/skills/<skill-name>/
├── SKILL.md          # the skill (frontmatter + body)
├── template.md       # the fill-in output template the skill produces
└── evals/
    ├── <id>-happy.md
    ├── <id>-edge.md
    └── <id>-adversarial.md
```

`template.md` is optional for pure-advisory skills but required for any skill
whose Output Contract is a structured artifact (memo, canvas, table, plan).

## 2. Frontmatter schema

```yaml
---
name: market-sizing                 # REQUIRED. kebab-case, MUST equal the directory name
description: >                       # REQUIRED. what it does + explicit "Use when ..." triggers
  Estimate market size (TAM/SAM/SOM) with top-down and bottom-up methods.
  Use when sizing an opportunity, estimating addressable market, or preparing
  a business case or investor pitch.
version: 0.1.0                       # REQUIRED. semver; bump on behavioral change
type: component                      # REQUIRED. component | interactive | workflow
source: import:phuryn/pm-skills@18468a9   # REQUIRED. "original" or "import:<repo>@<sha>"
---
```

- **`description`** must contain trigger language ("Use when …", "Triggers: …")
  so Claude auto-loads the skill at the right moment. It is always in context —
  keep it lean; put detail in the body (progressive disclosure).
- **`type`**:
  - `component` — single-shot artifact from context (canvas, memo, analysis). Eval one-shot.
  - `interactive` — asks the user questions before producing output (workshops, briefs). Eval the final artifact.
  - `workflow` — multi-step / multi-skill orchestration. Eval the final artifact.
- **`source`** records provenance. Imports from phuryn (MIT) cite the commit SHA.
  Original skills use `original`. Never copy text from CC BY-NC-SA sources
  (e.g. deanpeters) — reference ideas only.

## 3. Required body sections

Sections marked ⭐ are **required and linter-checked**. Others are required by
convention and checked in review.

1. **`## Purpose`** — what this produces and the decision it supports. Include a
   short **"When NOT to use"** so the skill declines out-of-scope asks.
2. **`## Inputs`** — required vs optional inputs, and *how to elicit* each if
   missing (for interactive skills, the questions to ask).
3. ⭐ **`## Output Contract`** — the exact deliverable:
   - a section-by-section template (or link to `template.md`),
   - format and length expectations,
   - a **GOOD** example (filled, brief),
   - a **BAD** example + one line on why it fails.
4. **`## Process`** — numbered steps the skill follows to produce the output.
5. **`## Quality Bar`** — a self-check rubric the skill runs **before returning**;
   if any item fails, it revises rather than returns. Written as checkable
   statements (these become the eval judge criteria).
6. ⭐ **`## Validation & Eval`** — points to `evals/*.md` and states the pass bar
   (baseline overall ≥ 0.8; regression fails if overall drops > 0.05).
7. **`## References`** — neutral links / frameworks. No promotional language.

## 4. Eval scenario cards

One markdown file per scenario in `evals/`. Cards are the source of truth: they
live in git, are reviewed like code, and (later) sync into a Langfuse dataset
named `skill:<name>` keyed by `id`.

```markdown
---
id: market-sizing-b2b-saas-eu          # stable, unique — Langfuse dataset-item key
skill: market-sizing                    # must equal the skill name
input:
  prompt: "Size the market for an EU SMB e-signature tool."
  context: "Bottom-up preferred. ~24M EU SMBs. Anchor pricing €15/mo."
expected:                               # traits good output MUST have (feeds the judge)
  - "Reports TAM, SAM, SOM as three distinct numbers"
  - "Shows both top-down AND bottom-up, and reconciles them"
  - "States every key assumption explicitly with source or caveat"
  - "SOM is a defensible fraction of SAM, not a round guess"
rubric:                                 # scored criteria → weight, weights sum to 1.0
  correctness: 0.35
  completeness: 0.25
  assumptions_explicit: 0.25
  actionability: 0.15
weight: 1.0                             # this scenario's importance within the suite
---

Optional free-text notes for reviewers: why this scenario exists, what it guards
against.
```

**Coverage:** every skill ships with **≥ 3 cards** — at least one *happy path*,
one *edge case*, and one *adversarial* (ambiguous, under-specified, or a trap the
skill must not fall for).

## 5. Definition of "done" for a skill

A skill can be committed when:

1. `python tests/validate_plugins.py` passes (structural lint).
2. It has ≥ 3 eval cards (happy + edge + adversarial).
3. Its baseline overall eval score clears the bar (≥ 0.8) — *enforced once the
   Langfuse pipeline is wired; until then, reviewers judge against the Quality Bar.*

Each skill is a **single commit**: `feat(<plugin>): <skill> skill`.
