---
name: marketing-ideas
description: >
  Generate 10–15 diverse marketing campaign and tactic ideas tied to product
  positioning and ICP, organized by funnel stage with channel, effort, and
  impact. Use when brainstorming marketing campaigns, planning multi-channel
  promotion, building growth initiatives, or exploring creative marketing
  tactics.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/marketing-ideas/template.md
---

# Generate Marketing Ideas

## Purpose
Produce a portfolio of 10–15 creative, actionable marketing campaign and tactic
ideas aligned with the product's positioning, target ICP, and funnel stage.
Each idea specifies the channel, effort estimate, expected impact, and
reasoning — enabling the team to prioritize and build a diversified GTM motion
that spans awareness through retention. Distinct from `acquisition-channel-advisor`
(which shapes systemic channel strategy) and organic-only frameworks — marketing-ideas
generates concrete campaign concepts across paid, organic, partnership, and
product-led tactics.

**When NOT to use:** channel strategy architecture (use `acquisition-channel-advisor`),
detailed campaign execution plans (use `go-to-market-motion`), pricing strategy
(use `monetization-canvas`), or organic growth only (use `organic-growth-advisor`).
Marketing ideas defines the tactical toolkit; it does not design the system.

## Inputs
- **Required:** product/offering, target ICP/persona, current market positioning,
  and funnel stage of interest (awareness/consideration/conversion/retention) or
  all stages. If missing, ask for these before generating.
- **Optional:** existing marketing channels, budget constraints, known competitive
  positioning, product maturity (stage: pre-launch/early/growth/mature), geography,
  brand tone or messaging guidelines.

## Output Contract
The deliverable is a **marketing-ideas portfolio** with these sections (see
`template.md`):

1. **Positioning Recap** — the product, ICP, and key positioning pillar(s) the ideas align to.
2. **Awareness Stage** — 3–4 ideas (e.g., content, SEO, partnership, PR, community).
3. **Consideration Stage** — 3–4 ideas (e.g., expert interviews, case studies, webinars, influencer).
4. **Conversion Stage** — 2–3 ideas (e.g., sales enablement, trial campaigns, referral).
5. **Retention & Growth** — 2–3 ideas (e.g., product-led, user-generated content, community, loyalty).
6. **Idea Summary Table** — all ideas in one sortable view: stage, channel, effort (low/med/high),
  impact (low/med/high), and a one-line rationale.

Each idea includes:
- **Channel** — primary medium (content/blog, SEO, social media, partnerships, events, PR, email, product-led, community, influencer, etc.).
- **Core message or hook** — a compelling angle for the target ICP.
- **Why it works** — specific reasoning tied to ICP behavior, positioning, or market gap.
- **Effort estimate** — low (< 1 week), medium (1–3 weeks), high (> 3 weeks).
- **Impact estimate** — low (< 10% reach), medium (10–50%), high (> 50% or high engagement).

Format: prose + one summary table. Length: ~2–3 pages (ideas + summary).

**GOOD (excerpt):**
> **Awareness — LinkedIn thought-leadership series** (channel: content)
> Core message: "How modern ops teams measure feature impact — a playbook."
> Why it works: Our ICP (ops managers at 100–1000-person companies) spend 2–4 hrs/week reading LinkedIn.
> This positions us as pragmatic operators, not just a tool vendor.
> Effort: medium (1 post/week × 4 weeks + light engagement). Impact: high (LinkedIn is primary discovery for this ICP).

**BAD (excerpt):**
> "Do TikTok." — fails because: no rationale, no ICP alignment, no channel details, no effort estimate.

## Process
1. **Anchor to positioning** — confirm product, ICP, positioning, and stage(s) of interest.
2. **Map ICP behavior** — how does the ICP discover / evaluate / adopt / grow usage of this category?
3. **Generate ideas** — brainstorm 3–4 ideas per stage, each with a distinct channel or angle.
4. **Evaluate & refine** — for each idea, validate it touches the ICP, is tied to positioning,
   and is feasible with the stated resources and timeline.
5. **Organize into summary** — build the stage-based portfolio and a sortable table.
6. **Run the Quality Bar** — revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] 10–15 distinct ideas are included across all four stages (or the requested subset).
- [ ] Each idea has a channel, core message/hook, and Why It Works tied to the ICP and positioning.
- [ ] Effort and impact estimates are realistic and labeled (low/med/high).
- [ ] Ideas span diverse channels and tactics (not 15 "do a blog post" variants).
- [ ] At least one idea is product-led or community-driven (not all top-of-funnel paid/content).
- [ ] The summary table covers all ideas in a sortable format (stage, channel, effort, impact, rationale).
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `acquisition-channel-advisor` — designs systematic channel strategy; consumes the channel inventory these ideas define.
- `go-to-market-motion` — plans detailed campaign execution; this skill provides the idea backlog.
- `organic-growth-advisor` — focuses on organic tactics; marketing-ideas is broader (includes paid, partnerships, events).

### External Frameworks
- Reforge, *Marketing Strategy* — funnel-stage thinking and channel diversification (free course intro).
- April Dunford, *Positioning* (2019), § Competitive Positioning — positioning as the anchor for all tactics.
- Traction by Gabriel Weinberg & Justin Mares (2015) — 19 traction channels and the importance of testing across them early.
