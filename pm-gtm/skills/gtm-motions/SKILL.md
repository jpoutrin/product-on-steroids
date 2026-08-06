---
name: gtm-motions
description: >
  Identify and define the primary GTM motion(s) for a product (PLG, SLG, MLG,
  community-led, or hybrid). Use when designing a go-to-market strategy,
  selecting acquisition channels, or building a motion stack for a product.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/gtm-motions/template.md
---

# Identify GTM Motions

## Purpose
Produce a defensible selection and rationale for the primary GTM motion(s) that
drive customer acquisition for a product — whether PLG (product-led growth), SLG
(sales-led), MLG (marketing-led), community-led, or a hybrid blend. Maps each
motion to the buyer journey and specifies activation playbooks and success
metrics. Supports go-to-market design and resource allocation decisions.

**When NOT to use:** overall go-to-market strategy positioning (use `gtm-strategy`
for the umbrella strategy), growth-loop design (use `growth-loops` for viral
and retention mechanics), or generic marketing channel selection (use
`marketing-channels` for ad-spend tactics). GTM motions focus on the primary
acquisition *motion architecture*, not the full strategy or channel details.

## Inputs
- **Required:** the product's characteristics — ACV (annual contract value),
  sales cycle length, buyer type (individual, team, enterprise), product
  complexity and self-serve viability, target market size and concentration.
  If missing, ask before proceeding; do not guess.
- **Optional:** market maturity, competitive intensity, team size and GTM
  experience, budget constraints, timeline to revenue, existing customer
  validation or traction. Defaults: assume greenfield, moderate competition,
  bootstrap-stage team, 6–12 month revenue target.

## Output Contract
The deliverable is a **GTM motions memo** with these sections (see `template.md`):

1. **Product Profile** — ACV, sales cycle, buyer type, complexity, addressable market size, market maturity.
2. **Motion Evaluation** — scoring of the 7 motion types (Inbound, Outbound, Paid, Community, Partners, ABM, PLG) on a 1–10 scale with fit justification for each.
3. **Recommended Motion Stack** — primary motion (1–2), secondary motions (1–2), and sequencing/rationale. Explicitly state why each motion was selected or rejected.
4. **Buyer Journey Mapping** — how the recommended motions map to awareness → consideration → decision → retention stages.
5. **Activation Playbooks** — per motion, a 90-day sprint with quick wins, key deliverables, team/tool requirements, and go/no-go gates.
6. **Success Metrics & Measurement** — per motion, leading and lagging metrics (e.g., CAC, payback period, MRR velocity).
7. **Key Assumptions & Risks** — numbered, each with confidence level (high/med/low) and validation method.

Format: prose + scoring table + playbook outlines. Length: ~2–3 pages. Every
recommendation is tied to the product profile, not generic.

**GOOD (excerpt):**
> **Primary Motion: PLG.** ACV $50/mo, self-serve product, SMB market of 100k+ addressable accounts, team of 2. Product-led aligns with low-friction buyer journey and scales with minimal headcount. 90-day sprint: free trial flow, onboarding analytics, viral loop via shared docs. CAC target $15.
> **Secondary Motion: Community.** Developer audience clusters in Discord/GitHub. Low-cost brand builder; launch 30-day community sprint week 2.

**BAD (excerpt):**
> "Use all 7 motions — inbound, outbound, paid, community, partners, ABM, and PLG. Each is important."
> — fails: undifferentiated, no fit justification, no sequencing, ignores ACV/team constraints, treats all motions equally.

## Process
1. **Capture product profile** — extract or elicit ACV, sales cycle, buyer type, complexity, market size, maturity.
2. **Score each of the 7 motions** — Inbound, Outbound, Paid Digital, Community, Partners, ABM, PLG. Rate fit (1–10) based on product profile; note constraints and strengths per motion.
3. **Select the stack** — pick 1–2 primary motions; 1–2 secondary motions. Explain trade-offs and why others were rejected.
4. **Map the buyer journey** — for each motion in the stack, show how it covers awareness/consideration/decision/retention.
5. **Draft 90-day playbooks** — per motion, outline quick wins, key deliverables, team/tools, gates.
6. **Define metrics** — CAC, payback, MRR velocity, activation rate, churn. Link to motion success criteria.
7. **Name assumptions** — list product/market/team assumptions tied to motion selection; rate confidence.
8. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Product profile is captured with **concrete numbers** (ACV, cycle, market size, team) — not vague.
- [ ] Each of the 7 motions receives a **1–10 score with explicit fit justification** tied to the product profile.
- [ ] Primary and secondary motions are clearly differentiated with **stated rationale** (why selected, why others rejected).
- [ ] Buyer journey is **mapped per motion** (not generic) to awareness, consideration, decision, and retention stages.
- [ ] 90-day playbooks include **quick wins, key deliverables, team/tool requirements, and go/no-go gates** — specific and actionable.
- [ ] Success metrics per motion are tied to **motion-specific KPIs** (CAC for paid; activation rate for PLG; etc.), not generic.
- [ ] Key assumptions are **numbered with confidence levels** and validation methods.
- [ ] If the memo is written to a file, it follows `template.md` — all 7 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `gtm-motions-happy` (happy path) — well-defined B2B SaaS product with clear fit for PLG-primary stack.
- `gtm-motions-edge` (edge) — hybrid motion scenario requiring balance (e.g., enterprise ACV + SMB market segments).
- `gtm-motions-adversarial` (adversarial) — vague product ask or conflicting constraints (high ACV + no sales team) that require skill to resolve.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `gtm-strategy` — the umbrella go-to-market strategy; GTM motions is one execution component within it.
- `growth-loops` — focuses on viral/retention mechanics, not acquisition motion architecture.
- `beachhead-segment` — picks the first target segment; consumes motion stack decisions.

### External Frameworks
- Kevin Kwok, "No Love for the Three-Year Plan" (2019) — on motion-market fit as the driver of early-stage growth strategy.
- Ansatz, "The Product-Led Growth Handbook" (2022) — positioning and playbooks for PLG as a primary motion.
- Jason Lemkin, "SaaS Go-to-Market" (2018) — enterprise-to-SMB motion stacking and sequencing discipline.
- [Product Compass: 5 GTM Principles](https://www.productcompass.pm/p/5-gtm-principles-with-frameworks-templates) — practical motion evaluation framework.
