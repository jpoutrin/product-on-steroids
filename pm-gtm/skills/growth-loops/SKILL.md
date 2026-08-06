---
name: growth-loops
description: >
  Identify growth loops (flywheels) by mapping self-reinforcing cycles that
  compound user acquisition, retention, or monetization over time. Use when
  designing growth mechanisms, reducing paid-acquisition reliance, or analyzing
  how a product can grow organically through built-in loops.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/growth-loops/template.md
---

# Identify Growth Loops (Flywheels)

## Purpose
Map self-reinforcing cycles (viral, usage, collaboration, referral, community,
or data loops) that compound acquisition, retention, or monetization. Each loop
has a trigger, action, output, re-entry mechanism, and a loop coefficient
(invites/shares per user per cycle × conversion rate). Supports growth strategy,
product roadmapping, and GTM prioritization — helps decide which loop to
strengthen first and how to compound results.

**When NOT to use:** choosing a GTM motion/channel (use `gtm-motions`), analyzing
organic-growth tactics in isolation (use `organic-growth-advisor`), or financial
forecasting (use finance skills). Growth loops are the compounding mechanisms
within motions and within organic strategies; this skill focuses on identifying
and analyzing the loop itself, not the channel or tactic.

## Inputs
- **Required:** product description, core user action, target user behavior (how
  users share/invite/refer). If missing, ask before proceeding.
- **Optional:** existing features for sharing/collaboration, current traction
  metrics, competitive loops, time horizon (default: next 3–6 months).

## Output Contract
The deliverable is a **growth-loops analysis** with these sections (see
`template.md`):

1. **Loop Inventory** — each identified loop (type, trigger, action, output, re-entry, bottleneck).
2. **Loop Diagrams** — text-based description of how each loop compounds (trigger → action → new user).
3. **Loop Coefficients** — invites/shares per user per cycle, conversion rate, net new per cycle, time per iteration.
4. **Bottleneck Analysis** — which step in each loop is the constraint (sharing friction, low conversion, slow re-entry).
5. **Prioritization & Next Steps** — recommended loop to strengthen first, 30-60-90 day roadmap.

Format: prose + tables. Length: ~2–3 pages. Every coefficient is estimated or flagged as unknown.

**GOOD (excerpt):**
> **Viral Loop (Figma designs):** Trigger = user creates design; Action = clicks "share link"; Output = shareable URL; Re-entry = new user receives link, signs up, can view + remix. Invites/user/cycle: ~2. Conversion: 15%. Bottleneck: remix flow not obvious to new users (low conversion). *Time to remove bottleneck: 2 sprints.*

**BAD (excerpt):**
> "The product has viral potential." — fails: no loop identified, no trigger/action/output mapped, no coefficient, no bottleneck named, no roadmap.

## Process
1. **Inventory loops** — identify each self-reinforcing cycle present or possible in the product (viral, usage, collaboration, referral, community, data).
2. **Map each loop** — trigger, action, output (value created), re-entry mechanism (how new user loops back).
3. **Estimate coefficients** — invites/shares per user per cycle, conversion rate, net new per cycle, time per iteration.
4. **Identify bottlenecks** — which step constrains the loop (sharing friction, low conversion, re-engagement delay).
5. **Prioritize** — which loop compounds fastest, which is easiest to activate, which builds competitive moat.
6. **Design roadmap** — 30-60-90 day plan to strengthen the top-priority loop.
7. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] At least 2–3 loops identified and mapped (trigger, action, output, re-entry for each).
- [ ] Loop diagrams describe the compounding mechanism in text (how trigger → action → new user → re-entry).
- [ ] Loop coefficients are estimated or explicitly flagged as "unknown" — never omitted.
- [ ] At least one bottleneck per loop identified (the constraint step).
- [ ] Prioritization is explicit — which loop first, why, and what 30-60-90 roadmap looks like.
- [ ] If the output is written to a file, it follows `template.md` — all 5 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `growth-loops-happy` — product with one obvious loop (e.g., referral, viral); user asks to identify and prioritize.
- `growth-loops-edge` — product with multiple competing loops; skill must map all and prioritize trade-offs.
- `growth-loops-adversarial` — vague product description; skill scopes the conversation and refuses to guess loop coefficients.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `gtm-motions` — the acquisition channel architecture; loops are the compounding mechanisms within a motion.
- `organic-growth-advisor` — organic-growth tactics and experiments; loops are one tool to scale organic growth.

### External Frameworks
- Ognjen Bošković — Growth loops research; focuses on compounding user acquisition through product-native sharing.
- Reforge, *Growth Loops* course — five loop types (viral, usage, collaboration, referral, community) and coefficient calculations.
- [Andrew Chen — The Viral Loop](https://andrewchen.com/) — seminal work on viral mechanisms and k-factors in networks.
