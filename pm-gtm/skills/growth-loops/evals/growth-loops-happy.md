---
id: growth-loops-happy
skill: growth-loops
input:
  prompt: "We've built a collaborative design tool. How can we grow virally? What loops should we prioritize?"
  context: "Product is like Figma — users create designs, can share links, invite collaborators. They have 50k users, 30% month-over-month growth, but acquisition is 70% paid. Want to reduce paid reliance."
expected:
  - "Identifies at least 2-3 loops (e.g., viral/sharing loop, collaboration loop, template-sharing loop)"
  - "Maps each loop with trigger, action, output, re-entry mechanism clearly described"
  - "Estimates loop coefficients (invites per user, conversion rate, K-factor) or flags estimates as uncertain"
  - "Identifies the bottleneck in the top-priority loop (e.g., 'share links get 5% conversion; main friction is unclear value to recipient')"
  - "Recommends one loop to strengthen first with a 30-60-90 roadmap (concrete, achievable next steps)"
  - "Explains trade-offs — why viral loop over collaboration loop, for example"
rubric:
  loop_identification: 0.25
  coefficient_rigor: 0.25
  bottleneck_specificity: 0.25
  actionability: 0.25
weight: 1.0
---

Happy path: product with an obvious primary loop (sharing/viral) and secondary loops (collaboration, templates). User wants prioritization. Guards against vague loops and unsupported recommendations.
