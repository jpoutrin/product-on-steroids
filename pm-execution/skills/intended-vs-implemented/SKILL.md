---
name: intended-vs-implemented
description: >
  Audit the gap between what a system is supposed to do and what the code
  actually does — find bugs that generic scanners miss because they lack a model
  of intent. Use when auditing AI-built code, reviewing access control against
  documented permissions, checking whether a codebase matches its documentation,
  or hunting for scope drift before shipping.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/intended-vs-implemented/template.md
---

# Intended vs. Implemented: Auditing the Gap

## Purpose

A linter scans code in a vacuum — it can tell you the code is *internally* consistent, but it cannot tell you the code does what you *meant*, because it has no model of your intent. The highest-value security and correctness bugs live in that gap: a permission documented but never enforced, a "cron-only" endpoint anyone can call, a field marked public-only that leaks private data, a feature spec turned into half-implemented code.

This skill is the method for finding that gap. It requires documented intent (permissions.md, architecture.md, feature specifications, etc.); without that paper trail, you cannot audit what was promised vs. what was built. That is exactly why commodity linters cannot replicate it.

**When NOT to use:** when documented intent does not exist or is radically out of date (in that case, the absence is itself the first finding — recommend documenting intent first, then auditing). This skill does not replace linters, security scanners, or performance profilers; it adds the *intent axis* they lack.

## Inputs

- **Required:** documented intent — a spec, design doc, permissions list, architecture doc, feature requirements, or shipping checklist that describes what the system *should* do. Treat the docs as claims to verify, not as proof.
- **Required:** code to audit — the implementation under review.
- **Optional:** specific boundary or feature to focus on (access control, data flows, payment logic, etc.) or a previous audit report to track drift over time.

## Output Contract

The deliverable is an **audit memo** with these sections (see `template.md`):

1. **Audit Scope** — what was audited (subsystem, feature, boundary), what documents were the source of truth, what code was reviewed, date range.
2. **Methodology** — how intent was established, how implementation evidence was gathered and validated, any limitations or blind spots.
3. **Findings** — for each documented rule or boundary, a summary of whether the code enforces it. Organized by boundary/feature, not by severity.
4. **Detailed Gaps** — each mismatch that matters, with:
   - **Documented intent** (quote the doc + cite location)
   - **Implemented reality** (cite the code + file/line)
   - **Impact** (who can exploit the gap, what do they access, what boundary is crossed?)
   - **Concrete fix** (what must change in code, docs, or both)
5. **Undocumented-but-enforced** — rules the code enforces that docs are silent on (flags stale docs).
6. **Sign-off** — summary: "N findings, M of which cross a boundary; N' require doc-only fixes; N'' are cosmetic."

Format: prose + tables where appropriate. Length: ~1–4 pages depending on scope. Every finding is cited on both sides (intent + code).

**GOOD (excerpt):**
> **Documented intent** (from permissions.md, line 24): *"Only admins may modify user roles."*
>
> **Implemented reality** (file: `app/routes/admin.py`, lines 156–168): The role-change endpoint checks `if user.is_admin()`, but this check is only applied server-side. The role POST handler is also exposed to the unauthenticated REST API at `/api/v1/users/{id}/role` (lines 289–295) with no guard.
>
> **Impact:** Any unauthenticated attacker can change any user's role to admin, violating the documented boundary and crossing tenant isolation.
>
> **Fix:** Remove `/api/v1/users/{id}/role` from the public API surface, or add the same `is_admin()` guard to both endpoints and test both paths.

**BAD (excerpt):**
> "The code looks OK; permissions are enforced in most places."
> — fails: vague, no citation of specific doc or code, "most places" hides which boundary-crossing gaps exist.

## Process

1. **Establish intent.** Read the documentation set (permissions.md, architecture.md, feature spec, shipping checklist) as claims to verify, not as proof. If docs are missing or patchy, note that — the absence is a finding.
2. **List boundaries and rules.** Extract each documented claim about scope, access, data, or behavior. Number them.
3. **Gather implementation evidence.** For each claim, read the code that enforces it (or fails to). Evidence is a cited file, line, and code path — not a comment, not "it's probably handled upstream," but the actual enforcement or its absence.
4. **Verify the code path.** Follow the entire flow: unauthenticated request → endpoint → guard → enforcement. If a claim relies on downstream enforcement, verify it actually happens downstream.
5. **Classify mismatches by impact.** A mismatch matters when crossing it lets a real actor reach data, money, infrastructure, or another tenant they shouldn't reach. Mismatches that only affect a single actor on their own data (cosmetic drift, internal inconsistencies) are lower priority; ignore them if time is tight.
6. **Avoid hand-wavy findings.** Every finding names: the documented intent (quote the doc), the implemented reality (cite the code), the attacker and victim, and the concrete fix. If you cannot cite both sides, it is a question to investigate, not a finding to report.
7. **Flag undocumented-but-enforced rules.** If the code enforces a rule the docs are silent on, call that out — the docs are now stale.
8. **Run the Quality Bar; revise if any item fails; then return.**

## Quality Bar

Before returning, confirm:
- [ ] Audit scope and source documents are clearly named (what was audited, what docs were used as ground truth).
- [ ] Methodology is transparent (how intent was extracted, how code was verified, any blind spots).
- [ ] Every finding that *crosses a boundary* (access, data, tenant, cost) is cited on **both** sides — documented intent and implemented code.
- [ ] No claim is made without evidence; comments like "it's probably handled upstream" or "internal only" are not evidence.
- [ ] Mismatches are classified by impact (boundary-crossing vs. cosmetic); cosmetic gaps are either dropped or grouped.
- [ ] Each detailed gap includes: quoted intent, cited code, named attacker/victim, and a concrete fix.
- [ ] Undocumented-but-enforced rules are flagged to alert to doc staleness.
- [ ] Sign-off summarizes: how many findings, how many cross a boundary, how many are doc-only vs. code-only vs. both.
- [ ] If gaps are left unresolved, they are labeled as "flagged for follow-up" with a priority or severity.

## Validation & Eval

Scenario cards in `evals/`:
- `intended-vs-implemented-happy` (happy path) — well-documented feature with a clear intent/code mismatch (scope drift).
- `intended-vs-implemented-edge` (edge) — partial documentation and a subtle boundary-crossing gap that requires code reading to spot.
- `intended-vs-implemented-adversarial` (adversarial) — vague or absent documentation; the auditor must scope the audit or flag the absence.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `shipping-artifacts` — documents the intent that this skill audits against. Run this first to ensure intent is written down.
- `scope-and-prioritize` — prioritizes findings by impact; consumes the gap list this skill produces.

### External Frameworks
- Gall's Law (John Gall, *Systemantics*, 1975) — complex systems that work are invariably found to have evolved from simple systems that worked; a complex system designed from scratch will not work. Auditing intent-vs-implemented helps catch designs that were too ambitious and shipped partial.
- Threat modeling (Microsoft STRIDE, OWASP) — systematically enumerates trust boundaries, data flows, and actors; this skill validates that documented boundaries are actually enforced in code.
- The Practice of System and Network Administration (Limoncelli et al., 2007) — covers configuration auditing and the importance of written specifications before implementation.
