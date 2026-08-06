---
name: positioning-ideas
description: >
  Generates multiple positioning angle options for a product — category creation,
  competitive repositioning, problem reframing, audience reframing, and value
  reframing — so the team can evaluate and choose before committing to a single
  positioning statement. Use when exploring product positioning, differentiating
  from competitors, identifying an unclaimed market frame, or deciding how to
  enter a crowded category.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/positioning-ideas/template.md
---

# Brainstorm Positioning Ideas

## Purpose
Generate 5–8 distinct positioning concepts for a product, each exploring a
different strategic angle (category creation, competitive repositioning, problem
reframing, audience reframing, value reframing). For each concept the skill
provides a tagline sketch, a strategic rationale, and explicit trade-offs, so the
team can evaluate options before committing to one. The output is a
**decision-enabling menu**, not a finished positioning statement.

**When NOT to use:**
- You have already chosen a positioning angle and need a polished one-paragraph
  artifact → use `positioning-statement` (it formalizes the chosen direction).
- You need to describe what the product *does* or its benefit hierarchy →
  use `value-prop-statements` (value props describe product benefits; positioning
  is about competitive frame and mental category).
- You are building a full go-to-market plan across channels, pricing, and launch
  sequencing → use `gtm-strategy` (positioning is one component of GTM strategy,
  not its entirety).
- You need hard market-size data to back a positioning claim →
  use `market-sizing` first, then return here.

## Inputs
- **Required:** product description — what it does, who it is for, and the
  primary problem it solves. If the user omits any of these three, ask before
  proceeding; do not guess the product scope.
- **Required:** competitive context — who the main competitors are and how they
  currently position. If not provided, ask the user to name 2–4 competitors or
  describe the category the product is entering.
- **Optional:** current positioning or working hypothesis — if the team already
  has a direction, note it and treat it as one candidate angle, not the only one.
- **Optional:** target audience profile and their core jobs-to-be-done. If absent,
  infer from the product description and flag the assumption.
- **Optional:** strategic constraints (e.g., enterprise-only, no "AI" messaging,
  price anchor). Apply these as filters across all concepts.

## Output Contract
The deliverable is a **positioning ideas brief** (see `template.md`) with these
sections:

1. **Context Summary** — a one-paragraph synthesis of the product, competitive
   landscape, and any constraints. Confirms the skill understood the input before
   generating ideas.
2. **Positioning Concepts** — 5–8 concepts, each as a level-2 heading, covering:
   angle type, tagline sketch, strategic rationale (why this frame is credible and
   differentiated), and trade-offs (what this angle makes harder or sacrifices).
3. **Recommendation** — the single concept the skill judges strongest given the
   stated context, with a one-paragraph explanation of the reasoning. The team may
   choose differently; the recommendation is a starting point, not a mandate.

Format: prose per concept + a recommendation paragraph. Length: ~1–2 pages.
Every concept must be genuinely distinct — do not pad with minor variations of
the same angle.

**GOOD (excerpt):**
> **Concept 3 — Problem Reframe: "The Compliance Tax Eliminator"**
> *Angle type: problem reframing*
> *Tagline sketch: "Stop paying the compliance tax."*
> **Rationale:** Mid-market CFOs experience compliance overhead as an unpredictable
> cost center, not a tooling gap. Framing the product around eliminating that cost
> (rather than "better audit software") triggers a CFO-level buying conversation
> that competitors anchored in IT tooling cannot easily copy.
> **Trade-offs:** Requires proof-points on actual cost reduction; may alienate
> compliance officers who see their function as strategic, not a tax.

**BAD (excerpt):**
> "Position as the best, most user-friendly compliance tool on the market."
> — fails: no competitive frame, no angle type, no trade-offs, and "best/most
> user-friendly" is an undifferentiated claim any competitor can copy.

## Process
1. **Synthesize the context** — read all inputs, map the competitive landscape,
   and identify the positioning white space (frames no major competitor owns).
2. **Generate five angle archetypes** — produce at least one concept per archetype:
   category creation, competitive repositioning, problem reframing, audience
   reframing, value reframing. Add further concepts if the space supports them
   (up to 8 total).
3. **Develop each concept** — for every concept write the angle type, a tagline
   sketch (4–8 words), a strategic rationale (2–4 sentences), and explicit
   trade-offs (1–3 bullet points).
4. **Check distinctness** — confirm that no two concepts are minor variations of
   each other. If any overlap, collapse or replace.
5. **Apply constraints** — if the user stated strategic constraints (audience,
   messaging rules, price anchor), filter or flag any concept that violates them.
6. **Write the Recommendation** — select the strongest concept given the context
   and explain the reasoning in one paragraph. Name the runner-up if the choice
   is close.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The output contains **5–8 positioning concepts**, each as a distinct
  level-2 heading.
- [ ] Every concept includes **all four elements**: angle type, tagline sketch,
  rationale, and trade-offs.
- [ ] All five angle archetypes (category creation, competitive repositioning,
  problem reframing, audience reframing, value reframing) are represented across
  the concepts.
- [ ] No two concepts are **minor variations** of the same angle — each opens a
  genuinely different competitive frame.
- [ ] The **Context Summary** accurately reflects the product and competitive
  landscape as understood; any inferred assumptions are flagged.
- [ ] The **Recommendation** names a single concept and gives a one-paragraph
  rationale; it does not hedge by listing multiple "equal" options.
- [ ] No concept uses generic, uncopyable claims like "best," "most
  user-friendly," or "innovative" without substantiation.
- [ ] If the output is written to a file, it follows `template.md` — all three
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `positioning-ideas-happy` (happy path) — established SaaS product in a crowded
  market; generates 5+ genuinely distinct angles.
- `positioning-ideas-edge` (edge) — product with no clear differentiation yet;
  skill must surface the tension honestly rather than paper over it.
- `positioning-ideas-adversarial` (adversarial) — team is anchored on one
  positioning angle and explicitly asks for validation, not exploration; skill
  must still deliver the full idea set and resist the framing pressure.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `positioning-statement` — takes the chosen concept from this skill and
  formalizes it into a single, polished positioning paragraph.
- `value-prop-statements` — produces a benefit-led value proposition hierarchy;
  complements but does not replace positioning (positioning sets the competitive
  frame; value props populate it).
- `gtm-strategy` — consumes the chosen positioning as one of its inputs to build
  the full launch plan.
- `competitor-analysis` — provides the competitive landscape data that feeds the
  white-space identification in Step 1.
- `beachhead-segment` — narrows the initial target audience, which sharpens the
  audience-reframing angle.

### External Frameworks
- Al Ries & Jack Trout, *Positioning: The Battle for Your Mind* (1981) — the
  canonical source for competitive frame, mental category ownership, and the
  "ladder" model that underpins all five angle archetypes used in this skill.
- April Dunford, *Obviously Awesome* (2019) — the five-component positioning
  framework (competitive alternatives, unique attributes, value, customer
  characteristics, market category) that structures the rationale and trade-offs
  in each concept.
- Geoffrey Moore, *Crossing the Chasm* (1991) — beachhead positioning and the
  whole-product model; especially relevant for the audience-reframing archetype.
- Peep Laja, CXL — [Positioning Strategy: A Guide to Better Market Positioning](https://cxl.com/blog/positioning-strategy/) — practitioner overview of positioning archetypes and common failure modes.
