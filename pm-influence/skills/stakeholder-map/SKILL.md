---
name: stakeholder-map
description: >
  Build a structured Power × Interest stakeholder map with engagement strategies
  and a communication plan for each quadrant. Use when managing stakeholders for
  a product or initiative, preparing for a launch, aligning cross-functional
  teams, or planning stakeholder engagement at the start of a new project.
version: 0.1.0
type: workflow
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/stakeholder-map/template.md
---

# Stakeholder Map

## Purpose
Produce a structured Power × Interest stakeholder map for a product or initiative
— placing every relevant stakeholder in the correct quadrant, assigning a tailored
engagement strategy to each, surfacing conflict risks, and generating a
communication plan table that a PM can act on immediately.

This skill creates the **baseline map**. Use it to establish who matters and how
to reach them. It is distinct from:

**When NOT to use:**
- Discovering who the stakeholders are in the first place — use `stakeholder-identification` to enumerate stakeholders before mapping.
- Getting detailed engagement tactics for a specific relationship — use `stakeholder-engagement-advisor` once the map exists.
- Generating narrative alignment content — use `alignment-narrative` or `exec-update` once strategy is set.

## Inputs
- **Required:** the product or initiative being mapped — name, scope, and rough stage (early discovery, pre-launch, post-launch). If missing, ask before proceeding; a map without scope is not actionable.
- **Optional:** a list of known stakeholders (names, roles, teams); any org chart, project brief, or team roster provided as files (read them first); prior mapping notes; geography or regulatory context that affects power dynamics.

## Output Contract
The deliverable is a **stakeholder map document** with these sections (see
`template.md`):

1. **Stakeholder Roster** — a numbered list of all stakeholders with name/role and their Power (High/Low) and Interest (High/Low) ratings plus one-sentence rationale for each rating.
2. **Power × Interest Grid** — a four-quadrant table placing each stakeholder in the correct cell: Manage Closely (High Power, High Interest), Keep Satisfied (High Power, Low Interest), Keep Informed (Low Power, High Interest), Monitor (Low Power, Low Interest).
3. **Engagement Strategy by Quadrant** — for each quadrant: recommended communication frequency, preferred channel(s), key messages and framing, and the risk if this quadrant is neglected.
4. **Communication Plan Table** — one row per stakeholder with columns: Stakeholder, Role, Quadrant, Frequency, Channel, Key Message.
5. **Conflict Risks & Alignment Gaps** — pairs of stakeholders with competing interests, the nature of the tension, and a suggested alignment approach.

Format: prose introduction + tables. Length: ~1–2 pages depending on stakeholder count. Every Power/Interest rating must have a stated rationale — no undefended placements.

**GOOD (excerpt):**
> **Sarah Chen — VP Engineering** | Power: High | Interest: High → *Manage Closely*
> Rationale: controls engineering headcount (High Power); feature directly increases her team's toil if not designed well (High Interest).
> Engagement: weekly 1:1, async Slack updates on spec changes, early involvement in technical trade-off decisions.

**BAD (excerpt):**
> "Stakeholders: VP Engineering (important), Marketing (medium), Legal (low)"
> — fails: no Power/Interest dimension, no quadrant placement, no engagement strategy, no rationale for any rating.

## Process
1. **Gather context** — read any provided files (org chart, brief, roster). If the initiative scope is ambiguous, ask one clarifying question before mapping.
2. **Identify stakeholders** — enumerate all relevant individuals and groups: executives, engineering leads, designers, marketing, sales, support, legal, finance, external partners, and end users. Err on the side of inclusion; it is easier to merge than to discover gaps later.
3. **Rate Power and Interest** — for each stakeholder, assign High/Low on both dimensions with a one-sentence rationale.
4. **Place in grid** — classify each into the correct quadrant and populate the Power × Interest Grid table.
5. **Assign engagement strategies** — for each quadrant, define frequency, channel(s), key messages, and neglect risk.
6. **Build communication plan table** — one row per stakeholder, pulling from the quadrant strategy.
7. **Flag conflicts** — identify pairs with competing interests and suggest alignment approaches.
8. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every stakeholder has an explicit Power rating (High/Low) and Interest rating (High/Low) with a stated rationale — no undefended placements.
- [ ] Every stakeholder is placed in exactly one quadrant of the Power × Interest Grid.
- [ ] All four quadrants have an engagement strategy defined (even if no stakeholders currently fall in a quadrant, note it as empty).
- [ ] The communication plan table has one row per stakeholder with frequency, channel, and key message populated.
- [ ] At least one conflict risk or alignment gap is identified, or the output explicitly states none were found with reasoning.
- [ ] No stakeholder group that could block the initiative is left in the Monitor quadrant without a note explaining the low-power rating.
- [ ] If the output is written to a file, it follows `template.md` — all 5 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `stakeholder-map-happy` (happy path) — well-scoped B2B SaaS initiative with a clear stakeholder list.
- `stakeholder-map-edge` (edge) — external-facing initiative with ambiguous power dynamics (e.g., a partner with veto power not on the org chart).
- `stakeholder-map-adversarial` (adversarial) — user asks for a stakeholder map but provides only "all our stakeholders" with no context; skill must ask for scope rather than fabricate placements.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `stakeholder-identification` — discovers WHO the stakeholders are; run before this skill when the stakeholder list is unknown.
- `stakeholder-engagement-advisor` — provides deep engagement tactics for individual relationships; consume the map this skill produces as its input.
- `alignment-narrative` — builds narrative alignment content; use after the map is established to craft targeted messaging per quadrant.
- `raci-decision-rights` — defines roles and accountability; complements the Power dimension of the map.

### External Frameworks
- Eden and Ackermann, *Making Strategy* (1998) — the Power/Interest matrix and Manage Closely / Keep Satisfied / Keep Informed / Monitor quadrant labels this skill is built on.
- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium) — overview of stakeholder mapping in the broader PM frameworks landscape.
- [Team Topologies: A Handbook to Set and Scale Product Teams](https://www.productcompass.pm/p/team-topologies-a-handbook-to-set) — team interaction modes that inform power and interest dynamics in cross-functional product work.
