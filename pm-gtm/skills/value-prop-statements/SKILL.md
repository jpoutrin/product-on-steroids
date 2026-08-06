---
name: value-prop-statements
description: >
  Generate targeted value proposition statements that connect product features
  to customer outcomes, crafted for specific audience segments. Use when writing
  marketing copy, briefing sales, or developing segment-specific messaging.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/value-prop-statements/template.md
---

# Value Proposition Statements

## Purpose
Produce 3–5 distinct value proposition statements that translate product
capabilities into customer outcomes for specific audience segments. Each
statement connects a feature, its benefit, and the desired outcome in a way that
resonates with the target persona. Supports GTM execution by providing the core
messages that marketing campaigns run and sales teams deliver.

**When NOT to use:**
- You need a single competitive positioning statement — use `positioning-statement`
  (positioning is about competitive frame and category; value props are feature-
  benefit-outcome connections for specific personas).
- You are generating campaign ideas or promotional concepts — use `marketing-ideas`
  (marketing generates campaign angles; value props are the core messages marketing
  runs).
- You have not yet identified target audience segments — pause and define personas
  or segments first; value props are persona-specific by design.

## Inputs
- **Required:** core product value or core positioning angle — the key benefit or
  capability to communicate (e.g., "reduces design time by 10x").
- **Required:** target audience segments or personas — at least 2–3 distinct
  segments (e.g., "social media marketers", "small business owners", "content
  creators"). If absent, ask the user to name them; do not guess.
- **Optional:** product features or differentiators that enable the value — used
  to make value props credible and specific. If absent, infer from the core value.
- **Optional:** existing positioning statement or brand voice guidelines — used to
  keep value props on-brand. If absent, adopt a clear, benefit-focused tone.
- **Optional:** pain points or desired outcomes for each segment — sharpens the
  outcome part of each statement. If absent, derive from typical segment needs.

## Output Contract
The deliverable is a **value propositions document** with 3–5 distinct statements,
one per target segment, structured as:

1. **Segment Overview** — brief description of the target audience and their job.
2. **Value Propositions** — 3–5 statements, each structured as: "We help [segment]
   [do job] so they can [outcome], unlike [alternative] which [limitation]."
   Each statement includes: feature(s) that enable it, primary benefit, and the
   outcome the customer can measure.
3. **Key Messages** — a bulleted summary of the core differentiator and proof
   points for each segment.

See `template.md` for the fill-in structure.

**GOOD (excerpt):**
> **For Social Media Marketers:** We help social media marketers create on-brand
> graphics 10x faster, so they can focus on audience engagement instead of design
> logistics, unlike Photoshop which requires expertise and takes hours per post.
> The drag-and-drop template library and pre-sized social formats save 20–30
> minutes per piece.

**BAD (excerpt):**
> "Canva is a design tool that lets you make graphics." — fails because: no target
> segment, no outcome, no differentiator, no feature-benefit-outcome chain.

## Process
1. **Segment clarity** — if the user has named segments, map them. If not, ask for
   2–3 distinct audience groups and their core job or use case.
2. **Feature-benefit audit** — list the 3–5 key product features or capabilities
   that enable customer outcomes. If no features are available, derive them from
   the core positioning angle.
3. **Outcome mapping** — for each segment, define what success looks like and what
   they are trying to accomplish.
4. **Alternatives & differentiation** — for each segment, name the alternative
   (existing solution, manual workaround, or competitor) and articulate the key
   limitation it has vs. the product.
5. **Draft statements** — write 3–5 value prop statements following the template,
   one per segment, embedding feature → benefit → outcome → differentiation.
6. **Tone & credibility check** — confirm each statement is specific, measurable
   (or includes a concrete proof point), and on-brand.
7. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] 3–5 distinct value propositions are written, one per target segment.
- [ ] Each statement embeds the feature-benefit-outcome-differentiation chain;
      none is generic or positioning-only (no "we're the leader in" without a
      concrete outcome).
- [ ] Segments are distinct and named; each value prop is tailored to that
      segment's job and pain point, not identical to others.
- [ ] Statements are measurable or include concrete proof points (e.g., "10x
      faster", "30 minutes saved", "on-brand without hiring a designer").
- [ ] Alternatives and key limitations are named for each segment, so the
      differentiation is explicit.
- [ ] Tone is benefit-focused and on-brand; no jargon or feature-only language.
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped
      hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`. Ship with ≥ 3 (happy + edge + adversarial).
Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `positioning-statement` — formalizes a chosen competitive positioning angle
  (category, reason to believe, tagline) for the whole product. Consumes the
  value props here as input to sales briefings.
- `marketing-ideas` — generates campaign concepts and promotional angles. Uses
  value props as the core messaging to build campaign around.

### External Frameworks
- Steve Blank, *The Four Steps to the Epiphany* (2005) — market segmentation and
  segment-specific value articulation for new ventures.
- Geoffrey Moore, *Crossing the Chasm* (1991) — the Geoffrey Moore positioning
  template and the role of value props in crossing different segments.
- April Dunford, *Obviously Awesome* (2019) — positioning beyond category and the
  importance of customer outcome articulation in messaging.
