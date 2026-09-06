# documentation/

This directory contains the durable documentation set that makes this codebase
reviewable before shipping. Five core documents describe architecture,
permissions, flows, secrets, and test coverage. Additional conditional documents
(emails, cron, SEO, automation) are added only if the capability exists.

## architecture.md

**Root document.** Product overview, tech stack, auth/session flow end-to-end,
trust boundaries, known risks with code evidence, and a "Related Documents"
index.

### Key sections:
- **Product overview:** what the system does, who uses it, key constraints.
- **Tech stack:** language, framework, database, external services.
- **Auth/session flow:** how claims/roles/scopes flow from login to protected
  endpoints, end-to-end.
- **Trust boundaries:** browser ↔ server, server ↔ external providers, app ↔
  jobs, agent ↔ tool surfaces.
- **Known risks & assumptions:** each entry tied to a file path or function name,
  not generic checklists.
- **Related Documents:** index linking to all other docs.

## flows.md

**Runtime view.** Each load-bearing user journey as actor → trigger →
precondition → outcome, with step-by-step flow, authorization checks, side
effects, and trust-boundary crossings at each step.

### Key sections:
- **Flow name:** (e.g., "User approves invoice")
- **Actor:** which role/scope.
- **Precondition:** entry state.
- **Success outcome:** final state and side effects (emails queued, jobs
  triggered, external calls).
- **Step-by-step:** UI → server → DB/jobs → external providers → webhooks →
  agents.
- **Authz checks:** which claim/role/scope is checked at each protected step;
  expected deny case.
- **Trust-boundary crossings:** where credentials are passed, how (headers/body).

Omit flows that touch only business logic without permissions, data integrity,
external side effects, or operational safety.

## permissions.md

**Access-control matrix.** Roles, claims, scopes, and resource × operation ×
role table. Notes which tables have row-level security (RLS) and which rely on
code-enforced checks.

### Key sections:
- **Roles & claims:** list of all roles (e.g., admin, member, viewer) and how
  they are derived (JWT claims, DB lookups, API keys).
- **Scopes:** what fine-grained permissions exist (e.g., invoice:read,
  invoice:approve) and how they are scoped (user-level, organization-level).
- **Resource × operation × role matrix:** rows are resources (invoices, users,
  reports), columns are operations (read, write, delete), cells show which
  roles/scopes are allowed.
- **RLS vs. code-enforced:** which tables enforce permissions via database
  policies, which via application code.

## variables.md

**Secrets and configuration.** All environment variables, API keys, database
credentials, and feature flags in a Name · used-by · scope · source · rotation
· risk table. Confirms no secret is bundled client-side. Includes pre-go-live
checklist.

### Key sections:
- **Configuration & secrets table:** Name · what uses it · scope (server/client)
  · where it comes from (env var, .env.local, secrets manager) · rotation
  frequency · risk level (low/medium/high).
- **Client-side audit:** explicit confirmation: "No secrets bundled
  client-side."
- **Pre-go-live checklist:** (e.g., all production secrets in the right
  secrets manager, rotation schedules set, backups configured).

## tests.md

**Verification map.** Which documented rules (from architecture, flows,
permissions) are actually tested, which are proposed, and which are unverified.
Derived from other docs and the existing test suite, not reverse-engineered
from code.

### Key sections (clearly separated so the map cannot read falsely green):

- **Existing coverage:** tests in the repo today, each tied to the rule it pins.
- **Proposed tests:** recommended cases not yet written, marked by type
  (unit/integration/guarded live/manual review).
- **Gaps:** documented rules with no verification, ranked by risk.

Each row: use-case → rule → expected behavior (including deny/negative case) →
evidence source (doc + code file) → status (existing / proposed / none).

## emails.md (conditional)

**Include only if the app sends email.** Queue → processor → provider path,
templates and variables, retry/backoff, and troubleshooting.

## cron.md (conditional)

**Include only if scheduled/background jobs exist.** Inventory table (job →
schedule → function → secrets → limits → retry), idempotency, internal
authentication, and monitoring.

## seo.md (conditional)

**Include only if there are public/indexable or bot-facing routes.** Preview
approach (static meta, prerender, edge HTML), route → needs-SEO table, metadata
sanitization, bot-vs-human routing.

## automation.md (conditional)

**Include only if the app embeds agents, LLM workflows, webhooks, or external
automation.** Per automation: trigger · owner · approval gate · inputs · exact
tools/APIs callable · steering (prompt) vs. guardrails · output contract · app
vs. agent responsibilities · rate limits and kill switch.
