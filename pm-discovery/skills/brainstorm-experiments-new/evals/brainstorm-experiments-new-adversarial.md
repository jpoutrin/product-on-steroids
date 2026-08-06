---
id: brainstorm-experiments-new-adversarial
skill: brainstorm-experiments-new
input:
  prompt: "Design experiments for an app that gamifies habit formation with AI coaching, blockchain rewards, and social accountability."
  context: "No customer interviews. CEO is bullish on the concept. Asking to validate the product idea ASAP."
expected:
  - "Skill declines to design experiments without first anchoring a testable hypothesis (problem, customer, core behavior)"
  - "Skill asks clarifying questions: Who is the target user? What specific habit are we testing (fitness, learning, sleep)? What is the core value prop (habit tracking vs. social vs. rewards)?"
  - "Skill warns that 'gamification + AI + blockchain + social' is too broad; requests focus on one problem assumption first"
  - "If the user insists, skill reframes: proposes 1–2 experiments testing the single riskiest assumption (e.g., 'Do users commit time to habit tracking?' via landing page + concierge)"
  - "Skill avoids the trap of feature-driven design; experiments are hypothesis-driven, not feature-list driven"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

This adversarial scenario tests whether the skill can push back on feature-led, opinion-driven, or over-scoped briefs.
The skill should refuse to design experiments for a nebulous "all the things" product and insist on hypothesis clarity first.
Guards against producing theater (experiments that sound good but test nothing in particular) and against enabling premature building.
