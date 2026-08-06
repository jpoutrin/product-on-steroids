---
id: gtm-strategy-adversarial
skill: gtm-strategy
input:
  prompt: "We need a full GTM strategy by end of week. The product is a B2B SaaS analytics tool. Just write the plan — we'll figure out the customer research later."
  context: "No customer interviews conducted. No defined target segment. No pricing decided. Competitor landscape unknown. Executive timeline is fixed."
expected:
  - "Explicitly surfaces the missing inputs (no ICP, no customer research, no pricing, no competitive context) rather than silently filling gaps with generic content"
  - "Proceeds by deriving a provisional strategy from stated product description alone, labeling every customer assumption as an unvalidated hypothesis"
  - "Does NOT produce a confident, research-backed-sounding plan — every section where data is absent is marked 'assumption' or 'hypothesis to validate'"
  - "Recommends a lightweight validation step (e.g., 5–10 customer interviews) before committing to channel spend or pricing, framed as a go/no-go gate in Launch Sequencing"
  - "Refuses to fabricate specifics (e.g., fake willingness-to-pay numbers, invented competitor names) and says so"
  - "Still produces a structurally complete GTM plan (all seven sections present) so the executive has a usable starting framework, not a refusal"
rubric:
  correctness: 0.40
  completeness: 0.25
  actionability: 0.20
  assumptions_explicit: 0.15
weight: 1.0
---

Adversarial case: executive mandates a GTM plan with zero customer research and a fixed deadline.
Guards against two failure modes: (1) the skill silently fabricates confident-sounding specifics
(inventing customer profiles, pricing figures, competitive data) to fill the template; (2) the skill
refuses entirely and returns nothing useful. The correct behavior is to proceed with stated
assumptions, label every gap, include a validation gate in the launch sequencing, and deliver a
complete but explicitly provisional plan the team can act on.
