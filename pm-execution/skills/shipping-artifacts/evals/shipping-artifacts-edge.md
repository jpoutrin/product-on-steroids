---
id: shipping-artifacts-edge
skill: shipping-artifacts
input:
  prompt: "Document this app for review."
  context: "Simple Python Flask API. Single role (authenticated user). No email, no background jobs, no SEO, no embedded agents. Only one secret (API key). No RLS; all permissions enforced in code."
expected:
  - "Produces all five core documents (architecture.md, flows.md, permissions.md, variables.md, tests.md)"
  - "architecture.md is minimal but complete: Flask + database, no external services, one trust boundary (browser→server), one secret, no agents or scheduled work"
  - "flows.md includes at least one flow (e.g., 'User fetches their profile') with authz check (token validation)"
  - "permissions.md is a simple one-role matrix (authenticated vs. unauthenticated) with a note 'All permissions enforced in code; no RLS'"
  - "variables.md lists only the API key with scope (server), source (env var), rotation policy, and risk level"
  - "tests.md notes which auth checks exist and which are unverified"
  - "Conditional docs are omitted (no emails.md, cron.md, seo.md, automation.md); architecture.md includes one-line stubs (e.g., 'No email — no emails.md')"
  - "No empty or generic sections; honest about what the app does and does not have"
rubric:
  honesty: 0.35
  appropriate_scope: 0.35
  conditional_handling: 0.3
weight: 1.0
---

Edge case: minimal app with no complex capabilities. Guards against inventing
empty conditional documents or missing one-line stubs, and ensures the skill
documents what actually exists rather than a checklist.
