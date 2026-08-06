---
id: pestle-analysis-adversarial
skill: pestle-analysis
input:
  prompt: "Just give me a quick list of PESTLE factors, one line each, no ratings or analysis needed — I'm in a hurry."
  context: "EdTech platform in the UK. User explicitly wants a bare bulleted list with no impact/likelihood and no implications."
expected:
  - "Declines to return an untriaged word-cloud; holds the line that every factor needs Impact and Likelihood ratings"
  - "Requires a 'so what for our product' implication for each factor even under time pressure"
  - "Explains briefly why a bare list is not usable output for a macro-environment scan"
  - "Still delivers efficiently for the UK EdTech context across all six lenses rather than refusing outright"
  - "Keeps the point-in-time framing and does not silently drift into change-over-time tracking"
rubric:
  correctness: 0.4
  resists_shortcut: 0.35
  actionability: 0.25
weight: 1.0
---

Adversarial: user pressures the skill to drop ratings and implications for a raw
factor list. Guards against the skill collapsing into an untriaged word-cloud
that violates the Output Contract, while still serving the request efficiently.
