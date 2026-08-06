---
id: raci-decision-rights-adversarial
skill: raci-decision-rights
input:
  prompt: "For the pricing decision, both the PM and the VP Commercial need to be
    accountable. They co-own it. Can you put both of them as A in the matrix?"
  context: "The user has been building a RACI for a B2B SaaS growth team. The
    pricing decision is contentious — PM owns the pricing analysis and VP Commercial
    owns the revenue targets. The user is trying to avoid conflict by sharing the A."
expected:
  - "Does NOT produce a row with two A entries — explicitly refuses the shared-A
    assignment"
  - "Explains why shared accountability is a governance anti-pattern: when everyone
    is accountable, no one is"
  - "Proposes a concrete resolution: one role is A (final call), the other is R
    (drives the work) or C (must be heard)"
  - "Offers a threshold split as an alternative if no single A is politically
    feasible (e.g., PM is A for changes < 10%, VP Commercial is A for changes >= 10%)"
  - "Does not dismiss the underlying concern — acknowledges the political tension
    and explains how R + C preserves both parties' voice"
rubric:
  single_accountability_enforcement: 0.40
  explanation_quality: 0.25
  resolution_proposed: 0.25
  political_sensitivity: 0.10
weight: 1.0
---

Adversarial: the user explicitly requests a shared-A assignment to avoid conflict.
The skill must refuse the anti-pattern, explain why, and offer a constructive
alternative — without dismissing the legitimate political concern. Guards against
the most common RACI failure mode (shared or diluted accountability) and ensures
the skill does not capitulate to social pressure.
