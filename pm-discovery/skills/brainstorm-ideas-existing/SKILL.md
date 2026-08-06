---
name: brainstorm-ideas-existing
description: >
  Generate product improvement ideas for an existing product using structured
  multi-perspective ideation from PM, Designer, and Engineer viewpoints. Use
  when brainstorming feature ideas, generating solutions for an identified
  opportunity, or ideating with a product trio.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/brainstorm-ideas-existing/template.md
---

# Generate Product Ideas for Existing Product

## Purpose
Produce a prioritized list of product improvement ideas for an existing product,
generated from three complementary perspectives (Product Manager, Designer,
Engineer). Each idea is grounded in the product's current state, the stated
opportunity, and constraints. Supports continuous product discovery cycles,
feature prioritization, and product trio collaboration.

**When NOT to use:** ideating for a new product or market entry (use
`brainstorm-ideas-new`), designing experiments to test assumptions (use
`brainstorm-experiments-existing`), or selecting a first target segment (use
`beachhead-segment`).

## Inputs
- **Required:** the existing product (name, current state), the opportunity or
  objective to address, and the target customer segment. If missing, ask before
  proceeding; do not assume product context.
- **Optional:** research data (user interviews, analytics, feedback logs, PRDs),
  product URL (to understand current feature set), past ideas or failed
  experiments (to avoid redundant suggestions), constraints (budget, timeline,
  platform, technical debt).

## Output Contract
The deliverable is a **structured idea list** with these sections (see
`template.md`):

1. **Opportunity & Context** — the product, objective, target segment, and key
   constraints or discoveries.
2. **Ideas from Product Manager perspective** — 5 ideas emphasizing business
   value, strategic alignment, revenue impact, and competitive positioning.
3. **Ideas from Designer perspective** — 5 ideas emphasizing UX, usability,
   delight, accessibility, and user need satisfaction.
4. **Ideas from Engineer perspective** — 5 ideas emphasizing technical
   feasibility, data leverage, scalability, existing infrastructure reuse, and
   novel technical possibilities.
5. **Top 5 Prioritized Ideas** — the highest-impact ideas selected across all
   perspectives, ranked by feasibility-to-impact ratio.
6. **For each prioritized idea:** name, one-sentence description, why it was
   selected, key assumptions to validate, and preliminary feasibility/impact
   tags.

Format: prose + structured idea list. Length: ~2–3 pages. Each idea statement
is concise and actionable.

**GOOD (excerpt):**
> **Idea:** Smart notification timing by day-of-week patterns
>
> **From:** Engineer perspective
>
> **Why selected:** Leverages existing behavioral analytics we already collect;
> 40% of engagement is concentrated in M–W; low-effort personalization with
> high retention impact.
>
> **Key assumptions:** Users have consistent weekly patterns; notification time
> alone drives 2–5% engagement uplift.
>
> **Feasibility tags:** Backend-only; leverage existing event stream; 1–2 weeks

**BAD (excerpt):**
> "Add a feature users ask for all the time" — fails because it lacks:
> concrete idea, cross-perspective thinking, feasibility assessment, or
> assumption clarity. Too vague to act on.

## Process
1. **Clarify the opportunity** — confirm product name, current state, objective,
   target segment, and key constraints. Read any provided research/data/URLs.
2. **Ideate from PM perspective** — generate 5 ideas emphasizing business
   value, strategy, revenue, competitive edge, and GTM fit.
3. **Ideate from Designer perspective** — generate 5 ideas emphasizing UX,
   usability, delight, accessibility, and user need satisfaction.
4. **Ideate from Engineer perspective** — generate 5 ideas emphasizing technical
   feasibility, data reuse, scalability, infrastructure, and technical
   innovation.
5. **Prioritize across perspectives** — select the top 5 ideas using a
   feasibility-to-impact lens; balance quick wins with longer-term bets.
6. **For each prioritized idea**, articulate the name, one-sentence description,
   selection reasoning, key assumptions, and preliminary tags (feasibility,
   impact, effort).
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] All three perspectives (PM, Designer, Engineer) are represented with 5
  ideas each.
- [ ] Ideas are specific and actionable—not vague platitudes.
- [ ] Each prioritized idea includes name, description, selection reasoning, key
  assumptions, and preliminary feasibility/impact tags.
- [ ] The top 5 ideas span at least two perspectives (no single-perspective
  dominance).
- [ ] Feasibility and impact tags are grounded in the product context (not
  generic "high/medium/low").
- [ ] Key assumptions are testable and named (e.g., "retention uplift > 2%").
- [ ] If the output is written to a file, it follows `template.md` (a
  skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `brainstorm-ideas-existing-happy` (happy path) — clear product opportunity
  with some research context.
- `brainstorm-ideas-existing-edge` (edge) — sparse context or ambiguous
  objective; skill must clarify before ideating.
- `brainstorm-ideas-existing-adversarial` (adversarial) — vague or unfocused
  request ("brainstorm some ideas") the skill must decline and ask for product
  context.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `brainstorm-ideas-new` — ideate for a new product or market entry.
- `brainstorm-experiments-existing` — design experiments to test ideas.
- `opportunity-analysis` — structure and prioritize customer opportunities.

### External Frameworks
- Teresa Torres, *Continuous Discovery Habits* (2021) — Product Trio
  collaboration and discovery loop discipline; the foundation for this skill's
  multi-perspective approach.
- The Opportunity Solution Tree (Torres) — how to map opportunities → solutions
  → experiments and loop back on failures.
- [Product Compass: What Is Product Discovery?](https://www.productcompass.pm/p/what-exactly-is-product-discovery)
- [Product Compass: Product Trio: Beyond the Obvious](https://www.productcompass.pm/p/product-trio)
- [Product Compass: The Extended Opportunity Solution Tree](https://www.productcompass.pm/p/the-extended-opportunity-solution-tree)
