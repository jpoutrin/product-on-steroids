---
name: strategy-red-team
description: >
  Adversarially stress-test an existing product strategy: surface its hidden
  load-bearing assumptions, steelman then attack each, rank failure modes by
  impact × likelihood × cheapness-to-test, and return a pre-mortem "why this
  fails" plus the falsifying test and kill criterion for each. Use when
  pressure-testing a strategy, challenging assumptions, running a pre-mortem, or
  preparing a strategy doc for executive review.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a9
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/strategy-red-team/template.md
---

# Strategy Red-Team: Attack the Assumptions Before Reality Does

## Purpose
Adversarially stress-test an **existing** product strategy so its load-bearing
assumptions fail on paper this week rather than in market next quarter. Acting as
a sharp, fair adversary, this skill extracts the claims the strategy rests on,
steelmans then attacks each, ranks the failure modes, runs a pre-mortem, and
hands back — for every surviving kill-assumption — the disconfirming evidence to
gather, the cheapest test, and the threshold at which you'd change course. The
job is a sharper decision, not a longer risk list.

**When NOT to use:** this skill **critiques a strategy; it does not author one.**
To *write* the strategy being red-teamed, use `product-strategy-canvas`. For a
one-off market number use `market-sizing`; for competitive teardown use
`competitor-analysis`; for prioritizing a backlog use an execution skill. A
red-team with no strategy to attack has nothing to do — get the strategy first.

## Inputs
- **Required:** the strategy to attack — ideally a `product-strategy-canvas`
  output, PRD, roadmap, or strategy memo. Its bets, target customer, and the
  wedge/mechanism must be stated. If only a vague direction is given, ask for the
  written strategy (or the 3–5 core claims) before red-teaming; do not attack a
  strategy you had to invent.
- **Optional:** the decision at stake and its timeline (shapes "evidence to get
  this week"), known constraints or prior evidence already cited (so the attack
  doesn't re-raise settled points), named competitors (to reason about
  counter-moves), and whether a cross-model second opinion is wanted.

## Output Contract
The deliverable is a **red-team review** with these sections (see `template.md`):

1. **Strategy in one line** — the plan being attacked, restated neutrally so the author agrees it's fair.
2. **Load-bearing assumptions** — the claims that, if false, kill the strategy, separated from cosmetic ones. Only these are attacked.
3. **Top kill-assumptions (ranked, 3–5)** — for each: **Claim** · **Steelman** (strongest case it's true) · **Fails if** (concrete, falsifiable condition) · **Disconfirming evidence to get this week** · **Kill criterion** (the threshold) · **Cheapest test**. Ranked by impact × likelihood-wrong × cheapness-to-test; the top row is what to test first.
4. **Competitor counter-moves** — the most damaging response an incumbent/rival could make, and which assumption it invalidates.
5. **Pre-mortem** — assume it's 12–18 months out and the strategy failed; the single most likely narration of why, traced back to a listed assumption.
6. **What's well-reasoned** — what holds up, and why. State it plainly; do not manufacture doubt.
7. **What I couldn't assess** — gaps where the strategy gave too little to judge.

Format: prose + one ranked block per kill-assumption. Length: ~1–2 pages, 3–5
kill-assumptions max. Every attack is specific to *this* strategy and pairs with
a test — no generic risk lists, no strawmen, no invented weaknesses.

**GOOD (excerpt):**
> **Claim:** Activation is the growth constraint, so onboarding is the wedge.
> **Steelman:** Funnel data shows 60% drop at first-value; fixing it plausibly unlocks the rest.
> **Fails if:** the real constraint is *retention*, not activation — fixing onboarding just pours users into a leaky bucket.
> **Disconfirming evidence this week:** cohort the last 8 weeks — do *activated* users retain at week 4? Pull the query today.
> **Kill criterion:** if W4 retention of activated users < 25%, activation isn't the binding constraint — stop the onboarding bet.
> **Cheapest test:** one SQL cohort query, no build.

**BAD (excerpt):**
> "Risks: execution risk, market risk, competitive risk. The team should be careful and monitor closely."
> — fails: generic risk labels not tied to this strategy's assumptions, no steelman, no falsifiable "fails if", no test, no kill criterion — a longer list, not a sharper decision.

## Process
1. **Extract every claim** the strategy asserts as true (about user, market, constraint, mechanism, timeline); separate **load-bearing** from cosmetic. Only load-bearing claims are worth attacking.
2. **Steelman, then attack** each load-bearing claim — state the strongest case it's true, then attack *that*, never a strawman.
3. **Write each failure mode as "Fails if ___"** — concrete and falsifiable ("fails if activation isn't the constraint" beats "execution risk").
4. **Rank by impact × likelihood-wrong × cheapness-to-test**; surface the top of the list — don't bury it.
5. **Reason about competitor counter-moves** — the most damaging rival response and the assumption it breaks.
6. **Run a pre-mortem** — assume failure 12–18 months out; narrate the single most likely why, traced to a listed assumption.
7. **For each surviving kill-assumption, give the operator something to do:** disconfirming evidence to get this week, kill criterion, cheapest test.
8. **Self-refute, don't fabricate** — default to "this risk is real," but state plainly what's well-reasoned and never invent a weakness the strategy doesn't have.
9. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Load-bearing assumptions are separated from cosmetic ones; only load-bearing ones are attacked.
- [ ] Each attacked claim is **steelmanned first**, then attacked on its strongest version — no strawmen.
- [ ] Each kill-assumption states a concrete, falsifiable **"Fails if ___"** — not a generic risk label.
- [ ] Kill-assumptions are **ranked** by impact × likelihood-wrong × cheapness-to-test, and there are **3–5**, not twenty.
- [ ] Every surviving kill-assumption carries **disconfirming evidence to get this week, a kill criterion, and a cheapest test**.
- [ ] A **competitor counter-move** and a **pre-mortem** are included, each tied to a listed assumption.
- [ ] What's **well-reasoned** is stated plainly and no weakness is fabricated.
- [ ] The output ends with what to **do** (tests/evidence), not just what to fear.
- [ ] If the review is written to a file, it follows `template.md` — all 7 sections present, in order (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `strategy-red-team-happy` (happy path) — a well-specified strategy canvas; the skill extracts load-bearing assumptions, steelmans and attacks, ranks, and returns tests + kill criteria.
- `strategy-red-team-edge` (edge) — a genuinely well-reasoned strategy; the skill must say plainly what holds up and flag gaps rather than manufacture doubt.
- `strategy-red-team-adversarial` (adversarial) — asked to red-team a one-line direction with no written strategy; the skill must refuse to attack an invented strategy and elicit the real one first.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `product-strategy-canvas` — authors the strategy this skill red-teams; its bets, wedge, and target customer are the load-bearing claims attacked here.
- `market-sizing` — when a red-team hinges on an unverified market figure, that skill supplies the defensible number instead of a guessed one.
- `competitor-analysis` — supplies the competitive facts behind the counter-move section.

### External Frameworks
- Gary Klein, *Performing a Project Premortem* (HBR, 2007) — the pre-mortem technique this skill runs in step 6: assume failure, then narrate why.
- Teresa Torres, *Continuous Discovery Habits* — assumption mapping and the "riskiest assumption → cheapest test" discipline behind the ranking.
- [Assumption Prioritization Canvas](https://www.productcompass.pm/p/assumption-prioritization-canvas) — impact × evidence framing for ranking which assumption to test first.
