---
id: shipping-artifacts-adversarial
skill: shipping-artifacts
input:
  prompt: "Document the app."
  context: "Vague brief with hidden complexity. User provides: 'It's a multi-tenant SaaS. Uses Node, database, some external services. Has users and admins.' Actually uses: OAuth (third-party login), Stripe webhooks (payment processing), delayed job queue (async notifications), internal CLI tools (batch operations), and customer data stored in a data warehouse (ETL pipeline)."
expected:
  - "Skill asks clarifying questions (architecture, tech stack, user roles, which capabilities exist) rather than guessing"
  - "Once clarified, produces all five core documents"
  - "architecture.md captures all trust boundaries actually present (OAuth provider, Stripe, job queue, data warehouse) with code evidence, not just the 'obvious' ones"
  - "flows.md includes at least one flow touching the hidden complexity (e.g., 'Customer pays → Stripe webhook → notification queued → admin notified') with authz checks and side effects at each step"
  - "permissions.md distinguishes tenant-level from admin-level permissions and notes where RLS is missing (data warehouse ETL) as a risk"
  - "tests.md identifies gaps where documented flows or permissions lack verification"
  - "Conditional docs included: automation.md (Stripe webhook parsing), cron.md (delayed job queue), and emails.md (async notifications)"
  - "Known risks section in architecture.md is honest about ETL data exposure and webhook signing validation rather than claiming full security"
rubric:
  clarifying_questions: 0.25
  hidden_complexity: 0.35
  risk_honesty: 0.25
  completeness: 0.15
weight: 1.0
---

Adversarial case: vague or contradictory brief with hidden complexity. Guards
against the skill treating unsupported assumptions as facts, missing
important trust boundaries or integrations, and documenting what the user
claims rather than what actually exists.
