---
name: identify-assumptions-existing
description: >
  Surface risky assumptions for a feature or initiative in an existing product
  across desirability, viability, and feasibility. Use when stress-testing a
  feature idea, doing risk assessment, preparing for assumption mapping, or
  building a business case.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/identify-assumptions-existing/template.md
---

# Surface Assumptions for Existing Product Features

## Purpose
Systematically surface the hidden, risky assumptions embedded in a feature or
initiative for an **existing product** — organized by desirability (do users want
it?), viability (does it make business sense?), and feasibility (can we build it?)
— ranked by uncertainty × impact. Supports go/no-go, prioritization, and de-risking
decisions by exposing what could go wrong before you invest.

**When NOT to use:** zero-to-one product creation (use `identify-assumptions-new`),
ranking assumptions after they've been identified (use `prioritize-assumptions`),
designing specific tests or experiments (use `brainstorm-experiments-existing`), or
general product ideation (use `brainstorm-ideas-existing`).

## Inputs
- **Required:** the feature or initiative — its name, what it aims to do, target
  user segment (or persona), and the problem it solves. If missing, ask for these
  before proceeding.
- **Optional:** product context (maturity, revenue model, user base size), any
  existing designs, PRDs, research, or customer feedback (read and cite it if
  provided).

## Output Contract
The deliverable is a **structured assumption list** organized as follows (see `template.md`):

1. **Feature Context** — name, goal, target segment, and problem it solves (1–3 sentences).
2. **Desirability Assumptions** — will users adopt it? Is it a real pain point?
   - Numbered list; each with category, assumption statement, confidence (High/Medium/Low),
   - and one suggested validation step.
3. **Viability Assumptions** — does it make business sense? (revenue, marketing, legal, support).
   - Same format: numbered, category, statement, confidence, validation.
4. **Feasibility Assumptions** — can it be built? (technical, integration, performance, dependency risks).
   - Same format.
5. **Risk Ranking** — top 3–5 assumptions ranked by **uncertainty × impact** (highest risk first);
   - each with a brief mitigation or next-step suggestion.
6. **Summary** — 1–2 sentence takeaway on go/no-go readiness.

Format: prose list + summary table. Length: ~1–2 pages. Every assumption must have
a confidence level and a falsifiable test.

**GOOD (excerpt):**
> **Desirability Assumption 2 (Medium):** Users will accept in-app notifications as
> a substitute for email digests. — *Test:* Interview 10 existing power users; ask if
> they'd disable email and rely on in-app alerts. Target: 7/10 affirmative.
>
> **Risk Rank #1 (Uncertainty: High, Impact: High):** Feasibility Assumption 1 —
> integrating with legacy payment system will take < 2 weeks. — *Next step:* Spike
> with payment-team lead; block feature sign-off on spike results.

**BAD (excerpt):**
> "Users will love this feature because it's innovative and saves time."
> — fails: vague assumption, no confidence level, no test, emotional language,
> not falsifiable.

## Process
1. **Read the feature brief** (or PRD, design, research). Extract context: problem,
   target segment, business goal.
2. **Assume the worst** — for each category (Desirability, Viability, Feasibility),
   brainstorm 3–5 things that could go wrong. Ask "What would have to be true for
   this to succeed?" — then invert each.
3. **Assign confidence** — for each assumption, rate how certain you are it's true
   (High = near-certain; Low = a big unknown).
4. **Suggest a test** — one concrete way to validate or falsify each assumption
   (interview, experiment, metric, spike, etc.).
5. **Rank by risk** — multiply uncertainty (inverse of confidence: Low=3, Med=2, High=1)
   by impact (how much it matters to go/no-go: e.g., Feasibility Assumption 1 is
   High impact if the spike blocks launch). Highlight top 3–5.
6. **Write the summary** — 1–2 sentences on go/no-go readiness based on the
   assumption landscape.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] All assumptions are organized into **Desirability, Viability, and Feasibility** categories (at least 2–3 per category).
- [ ] Each assumption has a **confidence level** (High/Medium/Low) and is **falsifiable** (testable, not emotional).
- [ ] Each assumption has a **suggested validation step** (interview, experiment, spike, metric, etc.).
- [ ] **Top 3–5 risks are ranked** by uncertainty × impact and have **mitigation or next-step suggestions**.
- [ ] A **summary** (1–2 sentences) on go/no-go readiness is included.
- [ ] If written to a file, the output follows `template.md` — all sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `identify-assumptions-existing-happy` (happy path) — straightforward feature with clear context.
- `identify-assumptions-existing-edge` (edge) — vague or complex feature; skill must ask clarifying questions.
- `identify-assumptions-existing-adversarial` (adversarial) — overly ambitious or greenfield-sounding feature the skill must challenge or scope to existing-product constraints.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `identify-assumptions-new` — for zero-to-one products and new-market entry; surfaces foundational and market-level assumptions.
- `prioritize-assumptions` — ranks assumptions after surfacing, using cost-of-learning and expected-value frameworks.
- `brainstorm-experiments-existing` — designs specific tests and experiments to validate or falsify assumptions.
- `brainstorm-ideas-existing` — ideation for new features or initiatives in existing products (upstream of assumption surfacing).

### External Frameworks
- Ash Maurya, *Running Lean* (2012) — the Lean Canvas and assumption-mapping discipline this skill is built on; Desirability/Viability/Feasibility as the core risk categories.
- Eric Ries, *The Lean Startup* (2011) — build-measure-learn cycle and validated learning; testing assumptions as the core of product de-risking.
- Assumptions in product strategy: Reforge / Product Compass courses on assumption management and de-risking.
