---
id: competitive-battlecard-edge
skill: competitive-battlecard
input:
  prompt: "Create a battlecard for Upstart Competitor Y. They're newer, less well-known, and we don't have much sales data on them yet."
  context: "Limited public information. No G2 reviews yet. Product is 2 years old. One sales rep reported seeing them in a deal. Help us understand how to position against them."
expected:
  - "Acknowledges limited information where data is sparse; uses best available public sources (website, LinkedIn, demo, Reddit, ProductHunt)"
  - "Company Overview is present but honest about what is unknown (e.g., 'Funding not publicly disclosed')"
  - "Comparison table exists with rows for known capabilities; marks unclear areas as 'TBD' or 'needs verification' where public info is thin"
  - "Where We Win section is concrete and actionable based on available info, even if competitor comparison is incomplete"
  - "Includes a note or section flagging assumptions and suggesting sales team verify claims with prospects during calls"
  - "Landmine questions are crafted to help sales reps discover competitor positioning during prospect conversations"
  - "Win/Loss Patterns section is informed by limited data but avoids speculation; notes 'to be validated with more deal data'"
rubric:
  correctness: 0.30
  completeness: 0.25
  honesty_about_gaps: 0.25
  actionability: 0.20
weight: 1.0
---

Edge case: sparse public information on a newer competitor. Skill must avoid hallucinating missing facts, flag assumptions, and still deliver actionable sales guidance. Guards against overconfident comparisons and ensures sales team knows what to validate in the field.
