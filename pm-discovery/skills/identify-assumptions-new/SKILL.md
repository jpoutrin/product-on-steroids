---
name: identify-assumptions-new
description: >
  Uncover risky assumptions for a new product across 8 risk categories (Value, Usability,
  Viability, Feasibility, Ethics, Go-to-Market, Strategy & Objectives, Team). Use when
  evaluating startup risks, assessing a new product concept, mapping assumptions for a
  venture, or stress-testing a zero-to-one idea.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/identify-assumptions-new/template.md
---

# Surface Hidden Assumptions (New Product)

## Purpose
Identify and prioritize risky assumptions for a new product or zero-to-one initiative
across eight risk categories — extending the four core product risks (Value, Usability,
Viability, Feasibility) with Ethics, Go-to-Market, Strategy & Objectives, and Team risks.
The output ranks assumptions by uncertainty × impact, flags the riskiest leap-of-faith
bet, and supports go/no-go decisions and prioritization of validation experiments.

**When NOT to use:** enhancements to existing products (use `identify-assumptions-existing`),
designing and running experiments (use `brainstorm-experiments-new`), or validating one
assumption in isolation (those are one-off research tasks). This skill surfaces the full
assumption landscape for a new venture; it does not execute the tests.

## Inputs
- **Required:** the product concept and its market context — problem being solved, target
  customer segment, rough positioning/features, and where it fits in the existing landscape.
  If missing, ask before proceeding; do not invent assumptions.
- **Optional:** supporting materials (customer research, competitive landscape, team
  composition) — read and cite them. Business plans, pitch decks, and design artifacts.
  Priority ranking framework (default: uncertainty × impact). Time horizon (default: launch + 1 year).

## Output Contract
The deliverable is an **assumption canvas** (see `template.md`), structured as:

1. **Opportunity Statement** — problem, target segment, and strategic intent (1–2 sentences).
2. **Assumptions by Risk Category** — four tables (one per category pair), each assumption
   with a confidence level (high/med/low), impact (high/med/low), and uncertainty × impact
   score (1–9). Rows sorted by score, highest first.
3. **Top Leap-of-Faith Assumption** — the single riskiest assumption (highest score) with
   a one-sentence description of why it is existential.
4. **Validation Approach** — for the top 3 assumptions, suggest a lightweight test or
   signal that would reduce uncertainty (not a full experiment, just the probe).

Format: prose intro + six tables + narrative notes. Length: ~1–2 pages. Every assumption
is sourced from a specific risk perspective; never a generic worry.

**GOOD (excerpt):**
> **Value → Desirability:** "Doctors will adopt AI for patient intake if it saves >2 hrs/week."
> Confidence: low. Impact: high. Score: 8. *Validate: interview 10 clinics on workflow friction.*
>
> **Go-to-Market → Positioning:** "Sales will be effective through vertical partners (e.g., EHR vendors)."
> Confidence: med. Impact: high. Score: 6. *Validate: 3 partnership conversations with key EHRs.*

**BAD (excerpt):**
> "People will use it" — too vague (desirability? viability? adoption?). No risk category.
> No confidence or impact. Fails: ambiguous assumption, no scoring, no test proposal.

## Process
1. **Read the concept and context** — understand the problem, customer, and go-to-market
   framing. If any are missing, ask.
2. **Adopt three perspectives** — think through why this venture might fail from a Product
   Manager's lens (market demand, monetization, competition), Designer's lens (UX friction,
   onboarding, engagement), and Engineer's lens (build vs. buy, scalability, integration).
3. **Map assumptions to 8 risk categories:**
   - **Value:** Will it create value? Will customers keep using it? (desirability + retention)
   - **Usability:** Can users figure it out? Can you onboard fast enough? Will it increase cognitive load?
   - **Viability:** Can you sell/monetize/finance it? Is the CAC justified? Can you scale operations and support?
   - **Feasibility:** Can you build it with current tech? Are integrations possible? Can it be efficient?
   - **Ethics:** Should you do it? Regulatory/legal risks? Customer privacy/safety implications?
   - **Go-to-Market:** Do you have launch channels? Can you convince customers to try? Right messaging for the channel? Right timing? Right sequencing?
   - **Strategy & Objectives:** What are the strategic bets? Can others copy it? PESTLE risks (political, economic, legal, tech, environmental)?
   - **Team:** Right skills? Right chemistry? Retention risk? Do they have the tools?
4. **For each assumption, estimate:**
   - **Confidence:** How sure are you? (high: 90%+ conviction; med: 50–90%; low: <50%)
   - **Impact:** If wrong, does it kill the venture? (high: venture ends; med: major pivot needed; low: a course correction)
   - **Score:** Confidence × Impact on a 1–9 scale (low conf + high impact = 8–9; high conf + low impact = 1–2).
5. **Rank by score, highest first.** Highlight the top leap-of-faith assumption (the single
   riskiest bet).
6. **Suggest lightweight validation** for the top 3 assumptions — a signal (interview, usage
   pattern, partnership conversation) that would reduce uncertainty without running a full experiment.
7. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] All eight risk categories are covered; each has ≥ 2 assumptions.
- [ ] Every assumption is **specific and testable** (not vague — e.g., "users find it hard to add photos" not "UX is bad").
- [ ] Confidence and impact are **rated independently** (not collapsed into a single "risk" score).
- [ ] Assumptions are **ranked by uncertainty × impact score** (highest first).
- [ ] The **top leap-of-faith assumption** is clearly called out and justified as existential.
- [ ] **Validation approaches** for the top 3 are lightweight and specific (a named test or signal, not "more research needed").
- [ ] If the output is written to a file, it follows `template.md` — all 6 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `identify-assumptions-new-happy` (happy path) — B2B SaaS new product with mature market.
- `identify-assumptions-new-edge` (edge) — consumer app in emerging/cultural context, sparse data.
- `identify-assumptions-new-adversarial` (adversarial) — vague concept ("an AI tool for productivity") the skill must scope down or decline.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `identify-assumptions-existing` — assumptions for enhancements/iterations to established products (different risk balance).
- `brainstorm-experiments-new` — design and run tests to validate assumptions identified by this skill.
- `discovery-interview-prep` — structure customer conversations to probe specific assumptions.

### External Frameworks
- Eric Ries, *The Lean Startup* (2011) — leap-of-faith assumptions and their prioritization by risk.
- Teresa Torres, *Continuous Discovery Habits* (2021) — four core product risks (Value, Usability, Viability, Feasibility).
- Product Compass, *[Assumption Prioritization Canvas](https://www.productcompass.pm/p/assumption-prioritization-canvas)* — structured assumption mapping and scoring.
