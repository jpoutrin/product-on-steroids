---
id: strategy-red-team-adversarial
skill: strategy-red-team
input:
  prompt: "Red-team our strategy: we're going to win by being the AI-native option. Go."
  context: >
    No written strategy, canvas, PRD, or roadmap is provided — only a one-line
    slogan. No target customer, wedge, mechanism, or bets are stated. The user
    wants the attack now.
expected:
  - "Does NOT invent a plausible strategy and then attack that fabrication"
  - "Recognizes there is no load-bearing strategy to attack — a slogan is not a strategy — and says so"
  - "Elicits the actual written strategy or its 3–5 core claims (target customer, wedge, mechanism, bets) before red-teaming"
  - "Points the user to product-strategy-canvas to author the strategy first, since this skill critiques rather than writes one"
  - "Refuses to produce a full ranked kill-assumption list against an undefined direction"
rubric:
  refuses_to_attack_a_fabrication: 0.45
  elicits_real_strategy: 0.30
  correct_handoff: 0.15
  no_generic_output: 0.10
weight: 1.0
---

Adversarial: pressure to red-team a slogan with no underlying strategy. Guards
the skill's boundary — it critiques an existing strategy and must not attack a
strategy it had to invent; it should elicit the real one or hand off to
product-strategy-canvas.
