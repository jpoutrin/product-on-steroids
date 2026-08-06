---
id: competitive-battlecard-adversarial
skill: competitive-battlecard
input:
  prompt: "Create a battlecard for Dominant Competitor Z. They have features we don't, they're cheaper, and they're winning 70% of our head-to-head deals."
  context: "This is a difficult competitive scenario. They're objectively strong in several areas. Our sales team is demoralized. We need a realistic battlecard that doesn't sugarcoat but finds real wins."
expected:
  - "Acknowledges competitor's genuine strengths honestly (not spin); 'Where They Win' section is substantial and credible"
  - "Where We Win section is specific, grounded, and believable even if fewer than ideal (e.g., specific niches, customer segments, implementation speed, support quality)"
  - "Avoids false parity (does not claim we win on features we objectively don't have); respects sales team's intelligence"
  - "Objection responses reframe value rather than deny competitor strength (e.g., 'Yes, they have feature X; for your use case here's why you don't need it, and here's where we excel.')"
  - "Landmine questions expose real product gaps in competitor, not nitpicks"
  - "Win/Loss Patterns honestly names conditions where they win (e.g., 'They win when customers need feature X or lowest total cost') and where we win (e.g., 'We win when customer values ease-of-use and fast onboarding')"
  - "Closing positioning offers a narrow but defensible strategy (e.g., 'Focus on SMB segment where their enterprise pricing fails' or 'Target buyers who prioritize speed over feature breadth')"
rubric:
  correctness: 0.35
  honesty_and_realism: 0.30
  defensibility_of_wins: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial case: competitor is objectively strong. Skill must resist the urge to oversell, must find genuine wins (however narrow), and must help sales team fight smart from a position of realistic weakness. Guards against delusional battlecards that lose trust when sales reps use them in calls.
