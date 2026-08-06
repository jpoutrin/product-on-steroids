---
name: competitive-battlecard
description: >
  Create sales-ready competitive battlecards comparing your product against
  a specific competitor — positioning, feature comparison, objection handling,
  and win/loss patterns. Use when preparing sales teams, creating competitive
  materials, or responding to "why not competitor X?"
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/competitive-battlecard/template.md
---

# Create Competitive Battlecard

## Purpose
Produce a concise, scannable sales reference card for one specific competitor: their
company overview and positioning, how your product compares feature-by-feature and
on price, where you win and where they win, common prospect objections and your
responses, "landmine" questions to ask prospects that expose competitor weaknesses,
and patterns on when you tend to win or lose in competitive deals. A battlecard is
a **tactical sales tool** — rapid-fire ammo for calls, not a strategic analysis.

**When NOT to use:** broad multi-competitor landscape scan (use `competitive-research-snapshot`
if that skill exists) or deep competitive strategy work (use `competitor-analysis` for
positioning and market-share strategy). A battlecard arms one sales rep in one call; it
does not inform corporate strategy.

## Inputs
- **Required:** the specific competitor's name or product.
- **Optional:** existing sales data (win/loss notes, call transcripts, customer feedback, feature lists) — provide as context; the skill will read and incorporate them.

## Output Contract
The deliverable is a **one-page (or short two-page) markdown battlecard** with these
sections in order:

1. **Company Overview** — founded, HQ, funding/revenue if public, target market, and one-sentence positioning.
2. **Quick Comparison** — table of 5–8 capability areas (features, pricing, support, etc.), your approach vs. theirs, and winner per row.
3. **Where We Win** — 3–4 concrete advantages with proof points or customer quotes.
4. **Where They Win** — 2–3 competitor strengths and how you mitigate the gap.
5. **Common Objections & Responses** — table: prospect says X → you respond with Y (value framing, not dismissal).
6. **Landmines to Plant** — 3–5 questions to ask prospects that highlight competitor weaknesses.
7. **Win/Loss Patterns** — when you tend to win/lose in competitive deals and what tips the scale.

Format: markdown, scannable (tables, bold, short bullets), ~1–2 pages, printable or shareable
in Notion/Confluence.

**GOOD (excerpt):**
> **Where We Win**
> - **Ease of setup**: Zero config, live in 15 min vs. 3-day onboarding. Quote from Acme Inc case study.
> - **Pricing**: $99/mo fixed vs. their tiered model that hits $500+. 60% of deals cite this.

**BAD (excerpt):**
> "They're basically the same product. We're just better."
> — fails because: no specifics, no proof, no actionable comparison, not sales-ready.

## Process
1. **Research the competitor** — use web search or context provided to find: current product features, pricing tiers, target market, positioning, recent launches, customer reviews (G2, Capterra, Reddit).
2. **Build the overview** — company facts, founding date, positioning in one sentence.
3. **Create the comparison table** — 5–8 rows covering product features, pricing, support, onboarding, and any differentiators. Mark winner per row.
4. **List where you win** — 3–4 strengths with proof (customer quotes, hard data, specific capabilities they lack).
5. **Acknowledge where they win** — 2–3 competitor strengths; don't ignore them, reframe how you mitigate.
6. **Build objection responses** — common things a prospect will say; respond with value framing or facts, never dismissal.
7. **Write landmine questions** — 3–5 open questions (not leading) that expose gaps in their product or approach when a prospect answers.
8. **Add win/loss patterns** — summarize: when you close competitive deals vs. when they close, and the key differentiator that tips the scale.
9. **Keep it scannable** — tables, bold key phrases, short bullets. Sales reps should be able to skim it in 60 seconds during a call.
10. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Competitor overview is factual and current (founded, HQ, positioning in one sentence).
- [ ] Comparison table has 5–8 rows, each with your approach, their approach, and a clear winner.
- [ ] "Where We Win" has 3–4 advantages with proof points (customer quotes, data, specific missing features in their product).
- [ ] "Where They Win" acknowledges 2–3 strengths and reframes how you mitigate (not ignored or dismissed).
- [ ] Objection responses use value framing (TCO, ROI, hidden costs, fit) — not dismissal or negativity.
- [ ] Landmine questions are open-ended and expose gaps without leading (not "don't you hate their clunky UI?").
- [ ] Win/loss patterns summarize when you tend to win/lose and name the key differentiator.
- [ ] Format is markdown, scannable (tables, bold, bullets), 1–2 pages, printable.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `competitive-battlecard-happy` (happy path) — well-known competitor, sales team needs quick reference.
- `competitive-battlecard-edge` (edge) — newer or less-known competitor with sparse public information.
- `competitive-battlecard-adversarial` (adversarial) — competitor with significant product strengths in contested areas.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- (None yet in this plugin; adjacent skills in other plugins include `competitor-analysis` in pm-strategy for deep competitive positioning work.)

### External Frameworks
- Sales Hacker, *The Sales Battlecard* — tactical reference-card design for sales teams.
- Gong.io research on objection handling — data-driven responses to common prospect concerns.
