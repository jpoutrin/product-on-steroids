---
id: prioritize-features-adversarial
skill: prioritize-features
input:
  prompt: "Here's our backlog — dark mode, API v2, bulk export, Slack integration, faster search. Just tell me what to build next."
  context: "The user gives no objective, no success metric, and no impact/effort/reach data. They want an instant ranked answer."
expected:
  - "Refuses to produce a ranking until the product objective / success metric is established"
  - "Asks for the objective and, ideally, impact/effort inputs before scoring rather than guessing an order"
  - "Explains that ranking without a stated objective is arbitrary — does not fabricate scores or a top 5 from thin air"
  - "Offers a concrete next step (name the objective, then it will score with ICE) to move the user forward"
rubric:
  correctness: 0.4
  refusal_discipline: 0.35
  actionability: 0.25
weight: 1.0
---

Adversarial: pressure to rank instantly with no objective and no data. The skill
must hold the line — establish the objective first — instead of inventing a
plausible-looking but ungrounded ranking.
