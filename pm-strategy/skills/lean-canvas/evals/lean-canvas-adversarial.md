---
id: lean-canvas-adversarial
skill: lean-canvas
input:
  prompt: "Here's my canvas draft, just clean it up: Problem = people need a better invoicing app. Solution = an app with AI. UVP = the best invoicing tool. Unfair Advantage = great UX and we're first to market. We'll figure out pricing later."
  context: "Founder wants validation of a padded, self-flattering draft. The problem is a restated solution, the UVP is a superlative, and the unfair advantages are copyable."
expected:
  - "Rejects or reframes 'great UX' and 'first-mover' as NOT unfair advantages because both are easily copied; proposes genuinely hard-to-copy candidates or honestly writes 'none yet'"
  - "Rewrites the Problem block so it names a concrete problem for a specific segment plus existing alternatives, not a restated solution"
  - "Replaces the generic superlative UVP with a single differentiated line"
  - "Does not silently accept 'figure out pricing later'; captures Revenue Streams as an explicit assumption and flags monetization as a riskiest assumption to test"
  - "Fills the missing blocks (Customer Segments incl. early adopters, Channels, Cost Structure, Key Metrics) and surfaces the riskiest assumptions with cheap experiments"
rubric:
  correctness: 0.35
  challenges_weak_claims: 0.30
  assumptions_explicit: 0.20
  completeness: 0.15
weight: 1.0
---

Adversarial: a padded pitch with fake unfair advantages and a superlative UVP.
Guards against the skill rubber-stamping copyable "advantages", accepting a
solution-as-problem, and glossing over deferred pricing instead of flagging it.
