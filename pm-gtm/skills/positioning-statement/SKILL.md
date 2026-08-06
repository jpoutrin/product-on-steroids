---
name: positioning-statement
description: >
  Use when you have chosen a positioning angle and need to formalize it into a
  single canonical positioning statement plus tagline, rationale, and customer
  validation questions. Use when finalizing positioning before writing copy,
  briefing sales, or handing off to marketing.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/positioning-statement/template.md
---

# Write a Positioning Statement

## Purpose
Produce a single, finished positioning statement in the Geoffrey Moore / April
Dunford fill-in-the-blank format — "For [target customer], [product name] is
the [category] that [key benefit] because [reason to believe]" — together with a
3–7-word tagline variant, a rationale that explains why this competitive frame
wins over the alternatives considered, and three customer-facing validation
questions to test resonance before scaling GTM execution.

This skill finalizes the *chosen* positioning angle into a crisp artifact the
whole organization can act on. It does not generate positioning options; it
solidifies the one you have selected.

**When NOT to use:**
- You have not yet chosen a positioning angle — use `positioning-ideas` first to
  generate and score options; come back here once one is selected.
- You need to articulate feature-level benefits — use `value-prop-statements`
  for feature-benefit mapping; positioning is about competitive frame and
  category, not feature inventory.
- You need a full launch plan — use `gtm-strategy`; the positioning statement
  produced here is one input into that broader strategy.
- You are repositioning an existing product with no competitive context — pause
  and run `competitor-analysis` before this skill so the reason-to-believe is
  grounded in real differentiation.

## Inputs
- **Required:** the chosen positioning angle — the competitive frame, the target
  customer, and the primary benefit/differentiator. If the user has not selected
  an angle, ask them to name it or run `positioning-ideas` first; do not invent
  an angle.
- **Required:** product name (or working name).
- **Optional:** ICP details (role, company size, industry, pain points) — used
  to sharpen "For [target customer]". If absent, derive from the angle
  description and flag any assumptions.
- **Optional:** key competitors and their positioning — used to stress-test
  distinctiveness. If absent, note that the reason-to-believe is unverified
  against competitors.
- **Optional:** existing draft statement — refine rather than start from scratch.
- **Optional:** brand voice / tone constraints (e.g., technical, friendly,
  enterprise-formal) — default to plain, direct B2B language.

## Output Contract
The deliverable is a **positioning statement document** with four sections (see
`template.md`):

1. **Positioning Statement** — the canonical fill-in-the-blank form (labeled)
   immediately followed by the completed, single-sentence version. Maximum two
   sentences; no hedging language; no "we believe" preamble.
2. **Tagline Variant** — 3–7 words, customer-facing, distilling the
   positioning into something a prospect could remember and repeat.
3. **Positioning Rationale** — 2–4 sentences explaining why this competitive
   frame was chosen over the alternatives, what makes the reason-to-believe
   credible, and which customer pain it addresses most directly.
4. **Test Questions** — exactly three questions a PM or researcher can ask
   customers to validate whether this positioning resonates. Each question
   targets one of: comprehension (does it land?), differentiation (does it
   separate you?), purchase relevance (does it motivate?).

Format: short prose, no tables. Total output ≤ one page. The statement and
tagline are the most durable artifacts — they must survive copy-paste into a
slide or brief without explanation.

**GOOD (excerpt):**
> **Positioning Statement:**
> For [VP Engineering at a 50–500-person SaaS company], [Observe] is the
> [engineering analytics platform] that [turns deployment data into team
> performance insights] because [it integrates with your existing CI/CD stack in
> under a day and requires no code instrumentation].
>
> **Tagline:** Ship faster, see why.

**BAD (excerpt):**
> "Our platform empowers engineering teams to leverage data-driven synergies
> across the software delivery lifecycle to achieve best-in-class outcomes."
> — fails: no target customer named, no category declared, "synergies" and
> "best-in-class" are generic, no reason to believe, unpasteable into a brief.

## Process
1. **Confirm the angle** — verify the chosen positioning angle is explicit:
   competitive frame, primary target customer, and key differentiator. If any
   of the three is missing, ask before proceeding.
2. **Draft "For [target customer]"** — make the ICP crisp: role, context, and
   acute pain, not a demographic laundry list.
3. **Choose the category** — pick the market category the product *wants to
   own*. Avoid straddling two categories. If the category is new, name it
   plainly and accept that education cost.
4. **Draft the key benefit** — one outcome-oriented claim directly tied to the
   target customer's pain. Avoid feature language ("uses AI") in favor of
   outcome language ("cuts triage time by half").
5. **Draft the reason to believe** — one specific, verifiable proof point
   (integration, data point, methodology, or credential) that makes the benefit
   claim credible. This is the hardest part; flag if it cannot be stated
   concretely.
6. **Assemble and compress** — combine into the fill-in form, then write the
   completed sentence. Read it aloud; it should feel like something a human
   would say.
7. **Write the tagline** — distill to 3–7 words. Test: can a prospect repeat it
   after hearing it once?
8. **Write the rationale** — explain the frame choice in 2–4 sentences. Name
   alternatives considered and why they were rejected.
9. **Write the test questions** — one per dimension: comprehension,
   differentiation, purchase relevance.
10. Run the Quality Bar below; revise any failing items; then return.

## Quality Bar
Before returning, confirm:
- [ ] The statement names a specific target customer (not "teams" or "companies"
  in isolation) — a real job title or situation.
- [ ] The category is declared and is a single category, not a feature list
  or compound noun soup.
- [ ] The key benefit is outcome-oriented (not feature-oriented) and directly
  addresses the named customer's documented pain.
- [ ] The reason to believe is concrete and specific — a real proof point, not
  a vague claim ("industry-leading", "best-in-class").
- [ ] The completed statement would fit in one sentence read aloud in under
  10 seconds.
- [ ] The tagline is 3–7 words and can be understood without the full statement.
- [ ] The rationale names at least one alternative frame considered and why it
  lost.
- [ ] All three test questions address distinct dimensions (comprehension,
  differentiation, purchase relevance) — no two questions test the same thing.
- [ ] Nothing in the statement or tagline uses generic SaaS jargon
  ("synergies", "empower", "leverage", "unlock", "best-in-class") without a
  specific modifier that gives it meaning.
- [ ] If the output is written to a file, it follows `template.md` — all four
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `positioning-statement-happy` — SaaS analytics product with clear ICP and
  named competitors; tests clean end-to-end execution.
- `positioning-statement-edge` — platform product with multiple buyer personas;
  tests whether the skill forces a primary persona choice rather than hedging.
- `positioning-statement-adversarial` — jargon-heavy draft statement that says
  nothing distinctive; tests whether the skill rewrites rather than
  rubber-stamps.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `positioning-ideas` — generates and scores multiple positioning angles; run
  before this skill when the angle is not yet chosen.
- `value-prop-statements` — maps individual features to customer benefits; feeds
  the "key benefit" and "reason to believe" inputs to this skill.
- `gtm-strategy` — the positioning statement produced here is a required input
  to the broader GTM strategy plan.
- `competitor-analysis` — competitive landscape output grounds the category
  choice and reason-to-believe in this skill.

### External Frameworks
- Geoffrey Moore, *Crossing the Chasm* (1991/2014) — source of the canonical
  fill-in-the-blank positioning statement structure this skill implements.
- April Dunford, *Obviously Awesome* (2019) — the five-component positioning
  framework (competitive alternatives, unique attributes, value, target customer,
  market category) that informs the Process steps and Quality Bar here.
- April Dunford, *Sales Pitch* (2023) — positions the positioning statement as
  the foundation of a sales narrative, reinforcing the reason-to-believe as the
  load-bearing element.
