---
id: shipping-artifacts-happy
skill: shipping-artifacts
input:
  prompt: "Document this app for handoff."
  context: "Node.js + Express backend, React frontend, PostgreSQL with RLS. Three roles (admin, member, viewer) derived from JWT claims. Email notifications via SendGrid. Scheduled jobs via node-cron. Public marketing site with SEO. Embedded AI agent (Stripe webhook parsing)."
expected:
  - "Produces all five core documents: architecture.md, flows.md, permissions.md, variables.md, tests.md"
  - "architecture.md identifies tech stack (Node+Express+Postgres+React), trust boundaries (browser→server, server→SendGrid, app→cron, webhook→agent), and known risks tied to code evidence"
  - "flows.md describes at least three flows (e.g., member creates invoice, admin approves, system sends email notification) with actor, trigger, authz checks at each step, and trust-boundary crossings"
  - "permissions.md includes role/claim inventory and a resource × operation × role matrix (at least invoices/users, read/write/delete/approve)"
  - "variables.md lists all secrets (database password, SendGrid API key, JWT secret, webhook token) with scope (server/client), source, rotation, and risk; confirms no secrets in client bundle"
  - "tests.md separates existing, proposed, and gap sections and ties at least three documented rules (e.g., 'viewer cannot approve invoice') to tests or gaps"
  - "Conditional docs included: emails.md (SendGrid flow), cron.md (scheduled jobs), seo.md (public site), automation.md (Stripe webhook agent)"
  - "All docs cross-reference architecture.md in a 'Related Documents' section"
rubric:
  completeness: 0.35
  trust_boundaries: 0.25
  code_evidence: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: complete app with auth, flows, jobs, email, SEO, and automation.
Guards against missing any core document or conditional, and ensures trust
boundaries and risk evidence are explicit and tied to code, not vague.
