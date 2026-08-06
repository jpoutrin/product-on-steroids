---
name: shipping-artifacts
description: >
  Define the durable documentation set that makes AI-built code reviewable
  before shipping. Use when documenting a codebase for handoff, mapping user
  journeys and trust-boundary crossings, planning test coverage, or preparing
  for a security or performance audit.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/shipping-artifacts/template.md
---

# Shipping Artifacts: The Docs That Make AI-Built Code Reviewable

## Purpose

AI agents write code fast but leave no durable record of intent — what the
system is supposed to do, who is allowed to do what, where secrets live, which
rules are verified. This skill defines the documentation set that restores
reviewability by capturing architecture, permissions, data flows, secrets, and
test coverage. Supports code reviews, security audits, performance reviews, and
handoffs to new teams.

**When NOT to use:** detailed feature specs (use `create-prd`), release
communication (use `release-notes`), or product roadmapping (use roadmap skills).
This skill is infrastructure documentation, not user-facing narrative.

## Inputs

- **Required:** the codebase (or description) to document — what it does, what
  tech stack it uses, what external services it calls, and what user roles
  exist. If missing, ask the user to describe the app before proceeding.
- **Optional:** which documentation surfaces are already in place (so the skill
  can advise what's missing), known risks or audit focuses (security,
  performance, operational safety), and time horizon (generate all docs or
  produce only core).

## Output Contract

The deliverable is a **shipping-artifacts kit** — a set of markdown files in
`documentation/` at the repo root, consisting of:

**Core documents (always produce):**

1. **`architecture.md`** — product overview, tech stack, how auth/sessions/claims
   flow end-to-end, trust boundaries, and a "Known risks / assumptions" list
   backed by code evidence. Serves as the root document cross-referencing all
   others. ~0.5–1 page.

2. **`flows.md`** — each load-bearing user journey as actor → precondition →
   outcome, step-by-step from UI through server, data, jobs, external services,
   and agents. Explicitly notes authorization checks at each protected step and
   trust-boundary crossings. Omits flows that touch only business logic without
   permissions, data integrity, external side effects, or operational safety.
   ~1–2 pages.

3. **`permissions.md`** — roles, claims, scopes, and a resource × operation ×
   role matrix. Notes which tables have row-level security and which rely on
   code-enforced checks. Serves as the static baseline for access-control
   audits. ~0.5–1 page.

4. **`variables.md`** — configuration and secrets in a Name · used-by · scope ·
   source · rotation · risk table. Confirms no secret is bundled client-side.
   Includes a pre-go-live checklist. ~0.5 page.

5. **`tests.md`** — the verification map: which documented rules are actually
   tested (existing coverage), which are only proposed, and which have no
   verification (gaps). Each row: use-case → rule → expected behavior → evidence
   source → status. Tied to `architecture.md`, `flows.md`, and `permissions.md`.
   ~1–2 pages.

**Conditional documents (include only if capability exists):**

6. **`emails.md`** — transactional and automated email queues, templates, retry
   behavior. Only if the app sends email.

7. **`cron.md`** — scheduled and background jobs, schedule, idempotency, and
   retry strategy. Only if background jobs exist.

8. **`seo.md`** — SEO and social-preview routing for public/indexable routes.
   Only if the app is publicly indexable.

9. **`automation.md`** — embedded agents, LLM workflows, tool-calling, webhooks.
   Documents triggers, tool surfaces, approval gates, and output contracts. Only
   if automation exists.

Each file is short, table-and-bullet heavy, skips generic theory, and is honest
about current state.

See `template.md` for the fill-in structure.

**GOOD (excerpt from flows.md):**
> **Flow: User approves an invoice** — Actor: member with approve-scope · Trigger:
> POST /approve with invoice_id · Authz check: `member.scopes.includes("invoice:approve")`
> on the invoice's organization_id (not user-scoped) · Side effect: workflow
> triggered to notify vendor. Trust-boundary crossing: server→webhook provider
> (OAuth token in header).

**BAD (excerpt):**
> "The system has flows." — fails: vague, no actor/precondition, no authz
> checks, no side effects or trust boundaries, no evidence of what actually
> happens.

## Process

1. **Gather context** — ask for app description, tech stack, user roles, and
   which docs are already in place.
2. **Reverse-engineer architecture** — map tech stack, auth/session flow, trust
   boundaries, known risks tied to code.
3. **Extract flows** — list each load-bearing user journey: actor, trigger,
   authz checks at each step, side effects, trust-boundary crossings.
4. **Map permissions** — roles, claims, scopes, and resource × operation × role
   matrix; note RLS vs. code-enforced checks.
5. **Inventory secrets** — all configuration and secrets: where used, scope
   (server/client), source, rotation, risk.
6. **Verify tests** — map existing tests to rules from architecture/flows/permissions;
   call out proposed and unverified rules.
7. **Write conditionals** — add emails.md, cron.md, seo.md, automation.md only
   if the capability exists; one-line stubs otherwise in architecture.md.
8. **Cross-reference** — all docs link back to architecture.md in a "Related
   Documents" index.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar

Before returning, confirm:

- [ ] **Core five documents are present:** architecture.md, flows.md,
  permissions.md, variables.md, and tests.md all exist.
- [ ] **architecture.md includes a "Known risks / assumptions" section** with
  each entry backed by a file path or function name (not generic checklists).
- [ ] **flows.md captures at least three load-bearing user journeys** with actor,
  precondition, outcome, step-by-step sequence, and explicit authorization
  checks and trust-boundary crossings at each step.
- [ ] **permissions.md includes a resource × operation × role matrix** with clear
  notes on RLS vs. code-enforced checks.
- [ ] **variables.md has a complete Name · used-by · scope · source · rotation ·
  risk table** and explicitly states "No secrets bundled client-side."
- [ ] **tests.md separates existing, proposed, and gap sections** — none read
  falsely green.
- [ ] **Conditional docs are included only where the capability exists;** one-line
  stubs elsewhere in architecture.md (e.g., "No scheduled work — no cron.md").
- [ ] **All docs link back to architecture.md** in a "Related Documents" index.
- [ ] **No generic theory, examples, or templates — only this system's state.**
- [ ] If the output is written to files, all are in `documentation/` at the repo
  root and follow `template.md` (a skill-scoped hook re-checks on write).

## Validation & Eval

Scenario cards in `evals/`:

- `shipping-artifacts-happy` — complete app with auth, flows, jobs, secrets;
  guards against missing any core doc or conditional.
- `shipping-artifacts-edge` — minimal app (no email, no jobs, no automation);
  guards against inventing empty docs or missing one-line stubs.
- `shipping-artifacts-adversarial` — vague or contradictory brief ("document
  the app") with hidden complexity; guards against missing risks or treating
  unverified assumptions as facts.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills

- `create-prd` — the feature spec that documents product intent; shipping
  artifacts document technical intent.
- `release-notes` — external communication; shipping artifacts are internal
  documentation.
- `pre-mortem` — risk assessment by team; shipping artifacts document risks with
  code evidence.

### External Frameworks

- [OWASP — Threat Modeling](https://owasp.org/www-community/Threat_Model) —
  trust boundaries and threat surfaces in `flows.md`.
- [NSA — Secure Software Development Framework](https://csrc.nist.gov/projects/secure-software-development-framework) —
  documentation expectations for security reviews.
- [Google Cloud — Application Hardening Patterns](https://cloud.google.com/architecture/application-hardening) —
  secrets and configuration management discipline.
