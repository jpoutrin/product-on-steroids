---
name: release-notes
description: >
  Transform technical tickets, changelogs, or PRDs into polished, user-facing
  release notes organized by category (new features, improvements, fixes). Use
  when writing release notes, creating changelogs, announcing product updates, or
  summarizing what shipped.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/release-notes/template.md
---

# Transform Technical Changes into User-Facing Release Notes

## Purpose
Convert technical tickets, PRDs, changelogs, or Git logs into clear, engaging release notes that **lead with user benefit** rather than technical detail. Every entry is organized by category (new features, improvements, fixes, breaking changes, deprecations), written in plain language for your product's audience, and explains *why it matters*.

**When NOT to use:** technical changelogs for developers only (no translation needed), internal sprint summaries for your team, or release notes you've already written that just need editing — for that, use a general editor or `product-copyediting`. This skill transforms *raw material* into *marketing copy*.

## Inputs
- **Required:** raw material — one or more tickets (JIRA, Linear, GitHub), PRDs, Git logs, internal changelogs, or product descriptions. If you provide files, the skill reads them. If you mention a product URL, the skill may use web search to understand the audience.
- **Optional:** tone anchor (professional/friendly/technical), specific audience (founders, technical users, end users), version number or release date, screenshots or visuals to include, categories to emphasize or de-emphasize (e.g., no deprecations this cycle).

## Output Contract
The deliverable is a **release-notes document** with these sections (see `template.md`):

1. **New Features** — entirely new capabilities, each with a 1–3 sentence description of what it does and why it matters.
2. **Improvements** — enhancements to existing features, each with the area and how it helps users.
3. **Bug Fixes** — issues resolved, phrased in user terms (not technical terminology).
4. **Breaking Changes** (if any) — features or APIs that require user action, with clear migration or upgrade instructions.
5. **Deprecations** (if any) — features being sunset, timelines, and recommended alternatives.

The document opens with a title line (product name, version, date) in the style `# [Product Name] — [Version / Date]`.

Format: markdown or the requested format (HTML, plain text, etc.). Length: adaptable to scope; typically 0.5–2 pages.

**GOOD (excerpt):**
> **Dashboards now load up to 3× faster** — we've optimized backend queries and added smart caching, so your insights are ready when you are.
>
> **New: Bulk actions for reports** — select multiple reports and export, share, or archive them in one go. Saves time on repetitive tasks.

**BAD (excerpt):**
> "Implemented Redis caching layer for dashboard API endpoints." — tells *what* not *why*; uses internal jargon; ignores the user benefit.
>
> "Fixed race condition in concurrent checkout flow." — technical terminology; doesn't explain impact to the user.

## Process
1. **Read all raw material** — gather tickets, PRDs, logs, or changelogs. Extract what changed, who it affects, and why it matters.
2. **Map each change to a category**:
   - **New Features** — entirely new capabilities.
   - **Improvements** — enhancements to existing features (speed, UX, scope).
   - **Bug Fixes** — issues resolved.
   - **Breaking Changes** — changes requiring user action (migrations, API changes, config updates).
   - **Deprecations** — features being sunset.
3. **Rewrite each entry** for the user, not the developer:
   - Lead with benefit ("now 3× faster") not mechanism ("added Redis caching").
   - Use plain language; avoid jargon, internal codenames, or ticket numbers.
   - Keep to 1–3 sentences per entry.
   - Include visuals if available.
4. **Structure the document** — follow `template.md`; adjust tone to match product voice (professional for B2B, friendly for consumer, technical depth for developer APIs).
5. **Run the Quality Bar** — confirm all entries meet the bar; revise if any fail; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every change is categorized (new feature, improvement, fix, breaking change, or deprecation).
- [ ] Each entry **leads with user benefit**, not technical implementation.
- [ ] Entries use **plain language** — no jargon, internal codenames, ticket numbers, or unexplained acronyms.
- [ ] Each entry is **1–3 sentences** and actionable (user understands what it is and why it matters).
- [ ] Breaking changes and deprecations include **clear migration or upgrade steps**.
- [ ] Tone **matches the product's voice** (professional for B2B, friendly for consumer, technical for developer audiences).
- [ ] If visuals are available, they are included and captioned.
- [ ] The release notes follow `template.md` structure — all relevant sections present, in order, headings matching.

## Validation & Eval
Scenario cards in `evals/`:
- `release-notes-happy` (happy path) — straightforward B2B SaaS multi-feature release with clear feature/fix/improvement split and user benefit focus.
- `release-notes-edge` (edge) — sparse raw material (1–2 brief tickets) that requires inference and expansion to polish; edge case is breaking change requiring clear steps.
- `release-notes-adversarial` (adversarial) — highly technical raw material (Git commit messages, code diffs) that must be abstracted and humanized; must refuse to ship if audience is unclear.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `product-copyediting` — for polishing release notes you've already written (vs. generating from raw material).
- `prd` — if you need to document the rationale *behind* a release, use PRD structure instead.

### External Frameworks
- Inspired by [Intercom's release notes best practices](https://www.intercom.com/blog/product-updates/) — user benefit first, clear language, organized categories.
- Stripe's [changelog](https://stripe.com/docs/changelog) — example of professional, benefit-driven release notes for a developer audience.
