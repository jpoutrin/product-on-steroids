---
name: product-name
description: >
  Generate 8–12 product name candidates across multiple styles (descriptive,
  invented, metaphorical, compound, abbreviation) with memorability scores,
  trademark/domain flags, and rationale. Use when naming a new product,
  rebranding, exploring name options before launch, or testing names against
  positioning.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/product-name/template.md
---

# Generate Product Name Candidates

## Purpose
Produce a diverse set of 8–12 product name candidates across distinct naming
styles (descriptive, invented, metaphorical, compound, abbreviation) — each
scored for memorability, pronounceability, distinctiveness, and availability
(domain/trademark flags) — so you can evaluate and pitch names that align with
product positioning, target audience, and brand voice. Supports naming
decisions pre-launch and informs brand architecture strategy.

**When NOT to use:** deep legal trademark search (this skill flags only .com
availability; requires legal counsel), competitive feature teardown (use
`competitor-analysis`), or brand identity beyond naming (use positioning or
messaging skills). This skill generates options; it does not pick the final
name.

## Inputs
- **Required:** the product/opportunity, its core value proposition, target
  audience (B2B segment / B2C demographic), and desired brand tone/personality
  (e.g., trustworthy, playful, technical, premium). If incomplete, ask for
  these before generating; do not guess positioning.
- **Optional:** competitor names to differentiate from, geographic markets or
  languages to consider, naming patterns already used by the company (if
  refreshing a portfolio), any hard constraints (e.g., must start with a
  letter, avoid certain phonemes, must fit a URL convention).

## Output Contract
The deliverable is a **product-name memo** with these sections (see
`template.md`):

1. **Naming Criteria** — the product's core value, target audience, desired tone, and differentiation goals.
2. **Name Candidates** — 8–12 names organized by style (descriptive, invented, metaphorical, compound, abbreviation), each with:
   - The name itself
   - Naming style / etymology
   - Rationale (how it connects to value/audience/tone)
   - Memorability score (1–10, with why)
   - Pronounceability (easy/moderate/challenging)
   - Distinctiveness (how it differs from competitors)
   - .com domain availability flag (if checked)
   - Trademark risk note (subjective; requires legal search)
3. **Recommendation Section** — top 2–3 names based on criteria, with reasoning.
4. **Legal & Compliance Note** — reminder that formal trademark search and domain verification must occur before committing.

Format: prose + structured table/list. Length: ~1–2 pages. Every score is reasoned,
never unsupported.

**GOOD (excerpt):**
> **Name:** Lumina  
> **Style:** Invented (Latin-inspired)  
> **Rationale:** Evokes "light" and clarity, appeals to knowledge-worker audience; premium tone aligns with positioning.  
> **Memorability:** 8 — uncommon, easy to spell, evokes a clear metaphor.  
> **Domain:** lumina.com appears registered; alternatives: luminaapp.com available.  
> **Trademark risk:** "Lumina" exists in academic contexts (likely different goods/services); low conflict risk, but search required.

**BAD (excerpt):**
> "Name: Smart App. Very memorable, available, no issues."
> — fails: generic descriptor, no rationale, memorability unsupported, no style differentiation, trademark claim unsupported.

## Process
1. **Gather context** — clarify product value, audience, tone, and differentiation goals.
2. **Generate candidates across styles** — create 8–12 names spanning descriptive, invented, metaphorical, compound, and abbreviation.
3. **Score each candidate** — memorability (1–10), pronounceability, distinctiveness, and availability flags.
4. **Organize by style** — group and present with rationale for each.
5. **Recommend top names** — highlight top 2–3 based on scoring and fit to positioning.
6. **Flag legal requirements** — note that trademark search and domain registration checks are required before final commitment.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] **8–12 candidates generated** across at least three distinct naming styles (descriptive, invented, metaphorical, compound, abbreviation).
- [ ] **Each candidate has rationale** explaining how it reflects the product's value, appeals to the target audience, and aligns with brand tone.
- [ ] **Memorability and pronounceability are scored and reasoned** — no bare assertions.
- [ ] **Distinctiveness is explained** — how each name differs from named competitors (if provided).
- [ ] **.com domain availability is flagged** (checked or noted as not verified); alternatives suggested if primary unavailable.
- [ ] **Trademark risk is noted as subjective** and a legal search reminder is included.
- [ ] **Top 2–3 recommendations are highlighted** with reasoning tied to the criteria.
- [ ] **Naming criteria section is present** at the start, grounding all candidates in positioning.
- [ ] If the output is written to a file, it follows `template.md` — all 4 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `product-name-happy` (happy path) — clear product/audience/tone; skill generates well-differentiated, memorable names.
- `product-name-edge` (edge) — vague or over-constrained input (e.g., "name my AI thing" or many conflicting constraints); skill probes and generates reasonable options.
- `product-name-adversarial` (adversarial) — user asks for names without context or with impossible requirements; skill declines gracefully and asks for missing info.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `value-proposition` — clarifies the core value the name must communicate; feeds naming rationale.
- `competitor-analysis` — competitive names feed into distinctiveness evaluation and differentiation goals.
- `positioning` — brand voice and tone inform candidate generation and relevance scoring.

### External Frameworks
- Brandroot, *The Science of Naming* — memorability, phonetic appeal, and emotional resonance principles this skill applies.
- Marty Neumeier, *The Brand Gap* (2003) — brand architecture and naming strategy alignment.
- David Aaker, *Building Strong Brands* — the relationship between naming, brand positioning, and target audience psychology.
