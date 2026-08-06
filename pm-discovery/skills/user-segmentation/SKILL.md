---
name: user-segmentation
description: >
  Divide a user base into distinct behavioral, needs-based, or contextual segments
  with size estimates, characteristics, and strategic implications per segment.
  Use when segmenting a user base, analyzing diverse user feedback, building a
  segmentation model, or designing targeted product strategies.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/user-segmentation/template.md
---

# Segment a User Base by Behavior & Needs

## Purpose
Divide a user base into distinct, actionable segments based on behavioral patterns,
jobs-to-be-done, and needs — not demographics alone — and define each segment's
characteristics, size, strategic importance, and targeted value propositions. Supports
product strategy, feature prioritization, GTM planning, and roadmap decisions.

**When NOT to use:** building individual user archetypes (use `user-personas`, which
create representative personas *within* segments); rapid pre-research hypothesis
segmentation (use `proto-persona` for quick assumptions); or competitive positioning
(use `competitor-analysis`). This skill delivers the *segmentation framework itself*;
personas add detail *within* segments.

## Inputs
- **Required:** user feedback data (interviews, support tickets, product usage logs,
  surveys, NPS comments, feature requests). If none provided, ask for at least one
  source before proceeding; segmentation without grounding data is speculation.
- **Optional:** product focus (what product or feature area to segment around), known
  segment hypotheses to test against, target customer type (B2B/B2C, buyer vs. user),
  minimum segment size threshold (e.g., "only count segments > 10% of base").

## Output Contract
The deliverable is a **segmentation model** with these sections (see `template.md`):

1. **Executive Summary** — the segmentation thesis (how many segments, on what dimensions).
2. **Segment Profiles** — one profile per segment, containing:
   - **Segment name & overview** — descriptor, estimated size/%, one-sentence characterization.
   - **Behavioral characteristics** — how this segment uses the product, primary use cases,
     frequency, technical proficiency, integration with workflows.
   - **Jobs-to-be-done & motivations** — core job(s), underlying motivations, desired outcomes,
     what success means for this segment.
   - **Needs & pain points** — unmet needs, obstacles, current workarounds, severity.
   - **Product fit** — how well the current product serves this segment, valued features,
     gaps, churn risk.
   - **Value proposition** — unique value to unlock, feature/experience improvements that
     maximize fit, resonant messaging.
3. **Segment prioritization matrix** — strategic importance (growth / revenue / alignment)
   vs. implementation difficulty, with recommendation (invest / maintain / de-prioritize).
4. **Validation notes** — data sources, confidence levels per segment, gaps in feedback
   coverage, next steps to validate.

Format: prose + one prioritization table. Length: ~2–4 pages. Every segment is grounded
in representative quotes or behavioral patterns from actual data — never hypothetical.

**GOOD (excerpt):**
> **Segment: "Compliance-First Teams" (~25% of base)**
> — In-house legal/compliance teams using our workflow tool to audit and certify processes.
> Job: "Ensure 100% audit trail and compliance with SOC2/GDPR/ISO standards."
> Motivation: Risk mitigation; avoiding fines and reputation damage.
> Product fit: They value export/audit features highly; frustrated by lack of real-time
> alert on non-compliant actions. Workaround: spreadsheet log. Pain: manual, error-prone.
> Value unlock: Build real-time compliance dashboard, automated alert rules → eliminate
> workaround, reduce audit prep time by 60%. Messaging: "Certify with confidence."

**BAD (excerpt):**
> "We have three customer types: small, medium, and large" — fails because: no behavioral
> data, demographics-only (size ≠ needs), no jobs or pain points, no product-fit assessment,
> no data source cited.

## Process
1. **Organize the data** — read all provided feedback sources (interviews, tickets, logs,
   surveys); extract and tag behavioral patterns, jobs, motivations, pain points, product
   usage modes.
2. **Cluster by behavior & needs** — group users who share similar jobs, motivations,
   pain points, and product usage. Avoid demographic clustering; prioritize behavioral
   and motivational similarity. Aim for 3–5 segments; more than 5 is usually fragmentation.
3. **Name each segment** — use descriptive labels that capture the job or motivation
   (e.g., "Compliance-First Teams", "Growth-Hacking Explorers", "Efficiency Optimizers"),
   not demographics.
4. **Estimate segment size** — count feedback points per segment as a % of total feedback
   (e.g., "40 interview mentions ÷ 160 total = 25%"); note confidence.
5. **Define segment profiles** — for each segment, document: behavioral characteristics,
   core job(s), motivations, needs/pain points, product fit, and targeted value proposition.
6. **Assess strategic importance** — rank each by growth potential, revenue impact, and
   strategic alignment with product vision.
7. **Create prioritization matrix** — plot strategic importance vs. implementation
   difficulty; recommend invest / maintain / de-prioritize.
8. **Call out validation gaps** — which segments have thin data? What follow-up research
   would tighten confidence?
9. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] **≥ 3 distinct segments** identified, each with a descriptive name and estimated size (%).
- [ ] **Every segment is grounded** in behavioral patterns or representative quotes from actual
  feedback data — no hypotheticals.
- [ ] **No segment is purely demographic** (size, geography, role title alone); each defines
  behavioral or motivational differences.
- [ ] **Jobs-to-be-done are explicit** for each segment — what outcome is this group trying to achieve?
- [ ] **Product fit is assessed** per segment — what do they value, where are the gaps, what's the churn risk?
- [ ] **Unique value propositions are segment-specific** — not generic; they address each group's
  unmet needs.
- [ ] **Prioritization is justified** — strategic importance and difficulty have stated rationale.
- [ ] **Data sources are cited** — interviews (# and type), support tickets (count), usage logs (date range),
  surveys (sample size).
- [ ] **Confidence levels or gaps are flagged** — which segments have light data? What follow-up validates?
- [ ] If the output is written to a file, it follows `template.md` — all sections present, in order,
  headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `user-segmentation-happy` (happy path) — rich multi-source feedback (interviews, usage logs, surveys) with clear behavioral clusters.
- `user-segmentation-edge` (edge) — sparse or skewed feedback (mostly support tickets, limited interviews) requiring inference and confidence flagging.
- `user-segmentation-adversarial` (adversarial) — vague ask ("segment our users") with no data provided; skill must ask for sources before proceeding.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `user-personas` — defines representative archetypes *within* each segment; consumes the segmentation framework this skill produces.
- `proto-persona` — rapid hypothesis segmentation for early-stage research; less rigorous than this skill.
- `market-sizing` — sizes market opportunities; can consume segment definitions from this skill.

### External Frameworks
- Tony Ulwick, *Jobs to Be Done: Theory to Practice* — the jobs-based segmentation lens and motivation mapping this skill centers.
- Clayton Christensen, *The Innovator's Dilemma* — competing consumption chains and job-based customer segmentation.
- Georgiana Laudi, *Segmentation for Product Managers* — behavioral and needs-based segmentation models, avoiding demographic traps.
