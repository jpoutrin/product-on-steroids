---
name: build-vs-buy
description: >
  Produce a structured BUILD vs BUY vs PARTNER decision memo — core-differentiation
  test, total cost of ownership, time-to-value, lock-in risk, opportunity cost, a
  weighted scorecard, and a recommendation with the conditions that would flip it.
  Use when deciding whether to build in-house or buy a vendor/off-the-shelf tool,
  evaluating a make-or-buy tradeoff, choosing between adopting a platform and building
  it, or justifying a build/buy/partner call to leadership.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/build-vs-buy/template.md
---

# Build vs Buy vs Partner Decision Memo

## Purpose
Produce a defensible **BUILD vs BUY vs PARTNER** recommendation for a specific
capability the team needs — grounded in a core-differentiation test, a total-cost-of-
ownership comparison (build + maintenance vs license + integration), time-to-value,
switching/lock-in risk, and opportunity cost — resolved through a weighted scorecard
and a single recommendation that names the conditions that would flip it. Supports the
"should we build this ourselves or acquire it?" decision at feature, component, or
platform level.

**When NOT to use:** picking *which* vendor once you've already decided to buy (use a
vendor-selection / RFP process), estimating market size (use `market-sizing`),
sequencing an already-approved build on the roadmap (use a prioritization skill), or a
pure company-acquisition / M&A analysis. This skill decides the make-or-buy *mode*, not
the downstream execution.

## Inputs
- **Required:** the **capability** in question (what it must do and for whom) and the
  **business context** — is this the product's core differentiator or a commodity
  supporting function? If the user hasn't stated whether it's core, ask before scoring;
  the core-differentiation test drives the whole memo.
- **Optional:** rough build estimate (eng cost / calendar time), known vendor options and
  their pricing, the deadline or time-to-value pressure, in-house skill availability,
  data-sensitivity / compliance constraints, and decision-maker priorities (used to set
  scorecard weights). If absent, state the assumptions you used and mark them for
  validation.

## Output Contract
The deliverable is a **build-vs-buy decision memo** with these sections (see
`template.md`):

1. **Capability & Decision Framing** — what capability is needed, why now, and the
   three options actually on the table (Build / Buy / Partner — drop any that are
   genuinely N/A and say why).
2. **Core-Differentiation Test** — is this capability a source of competitive
   differentiation or a commodity? State the verdict and the reasoning; this sets the
   prior (differentiators lean Build, commodities lean Buy/Partner).
3. **Option Analysis** — for each live option, a short assessment across: **TCO**
   (Build = eng build cost + ongoing maintenance/opex; Buy = license + integration +
   admin; over a stated horizon, e.g. 3 years), **time-to-value**, **switching /
   lock-in risk**, and **opportunity cost** (what the team can't build while doing this).
4. **Weighted Scorecard** — a table scoring each option (1–5) against weighted criteria
   (weights sum to 1.0), with a weighted total per option. Criteria and weights are
   stated, not implied.
5. **Recommendation** — one clear call (Build / Buy / Partner), the 2–3 reasons it wins,
   and the **flip conditions**: the specific facts that, if true, would change the
   recommendation.
6. **Key Assumptions & Risks** — numbered, each with a confidence level (high/med/low)
   and how to validate the most load-bearing ones (especially the cost and time
   estimates).

Format: prose + one scorecard table. Length: ~1–2 pages. Every cost or time figure is
either sourced or explicitly labeled an estimate/assumption — never an unsupported number.

**GOOD (excerpt):**
> **Core-differentiation test:** Auth is table-stakes, not a differentiator — customers
> never chose us for login. → leans **Buy**.
> **TCO (3-yr):** Build ≈ €480k (2 eng × 9mo build €280k + €65k/yr maintenance).
> Buy (Auth0) ≈ €190k (€45k/yr license + €55k one-time integration). Buy is ~2.5× cheaper.
> **Recommendation: Buy.** Non-core, cheaper, live in 6 weeks vs 9 months.
> *Flip to Build if: vendor pricing exceeds €120k/yr at our scale, or a compliance
> regime forces data on-prem that no vendor supports.*

**BAD (excerpt):**
> "We should build it — we're engineers and we can do it better, and buying is expensive."
> — fails: no core test, no TCO (build's maintenance cost ignored), no time-to-value, no
> scorecard, no flip conditions; "expensive" is asserted with no numbers on either side.

## Process
1. **Frame the decision** — pin down the capability, why now, and which of Build / Buy /
   Partner are genuinely on the table (drop N/A options with a reason).
2. **Run the core-differentiation test** — decide whether this is a differentiator or a
   commodity; record the verdict as the prior.
3. **Estimate TCO per option** over a stated horizon — Build = build cost + ongoing
   maintenance/opex; Buy/Partner = license + integration + admin. Label estimates.
4. **Assess the non-cost factors** — time-to-value, switching/lock-in risk, and
   opportunity cost for each live option.
5. **Score** — set weighted criteria (weights sum to 1.0), score each option 1–5,
   compute weighted totals.
6. **Recommend** — name the winning option, the reasons, and the flip conditions that
   would reverse it.
7. **Map assumptions** — number the load-bearing assumptions (especially costs/timeline),
   rate confidence, name validation steps.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The **core-differentiation test** is explicit and its verdict is used to set the prior.
- [ ] **TCO is compared like-for-like** over a stated horizon, and the **Build side includes ongoing maintenance** (not just initial build cost).
- [ ] **Time-to-value, lock-in/switching risk, and opportunity cost** are each addressed for every live option.
- [ ] The **scorecard** shows criteria + weights (summing to 1.0), a 1–5 score per option, and a weighted total.
- [ ] The recommendation is **one clear call** that is consistent with the scorecard (or explains any override).
- [ ] **Flip conditions** are stated — the specific facts that would change the recommendation.
- [ ] Every cost/time figure is **sourced or labeled an estimate**; key assumptions are numbered with confidence + validation.
- [ ] If the memo is written to a file, it follows `template.md` — all 6 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `build-vs-buy-commodity-auth` (happy path) — a commodity capability (auth) with cost
  and vendor anchors; the skill should run the core test, build a like-for-like TCO, and
  recommend Buy with flip conditions.
- `build-vs-buy-core-differentiator-edge` (edge) — a capability that *is* the product's
  differentiator, where the cheaper/faster option is Buy but the right call is Build;
  tests that the core test overrides raw cost.
- `build-vs-buy-adversarial` (adversarial) — a pre-decided "just tell me to build it"
  ask with no cost data; the skill must still run the test, surface TCO/opportunity cost,
  and refuse to rubber-stamp without a scorecard and flip conditions.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `market-sizing` — sizes the opportunity a capability serves; a large SOM can justify a
  Build that TCO alone would not.
- `product-vision` — the vision defines what is genuinely core, which feeds this skill's
  core-differentiation test.

### External Frameworks
- Geoffrey Moore, *Dealing with Darwin* — **core vs context**: invest scarce resources in
  core (differentiating) activities and outsource/buy context (everything else). The
  backbone of the core-differentiation test here.
- Total Cost of Ownership (Gartner) — the discipline of counting build's ongoing
  maintenance and buy's integration/admin, not just the sticker price.
- Marc Andreessen, *"Build vs. Buy"* essays — the strategic-leverage lens: build where it
  compounds your advantage, buy where the market has already commoditized the capability.
