---
id: press-release-adversarial
skill: press-release
input:
  prompt: "Write me an exciting press release for our revolutionary AI platform that leverages next-gen synergies to delight everyone and disrupt the industry. Make it sound huge."
  context: "No specific customer, no concrete problem, no named alternative. Request is pure hype and asks for a real-sounding public announcement."
expected:
  - "Refuses to write the hype release as-is and does not fabricate a public announcement"
  - "Requires a specific customer and a concrete problem before drafting, asking who it is for and what they cannot do today"
  - "Strips buzzwords (revolutionary, next-gen, synergies, disrupt, everyone) and explains why customer-framed, falsifiable language is required"
  - "Clarifies this is an internal Working Backwards thinking tool, not a publishable launch announcement"
  - "Offers to produce a real PR/FAQ once a named customer and problem are provided"
rubric:
  correctness: 0.4
  completeness: 0.2
  assumptions_explicit: 0.2
  actionability: 0.2
weight: 1.0
---

Adversarial: a hype-laden "AI platform for everyone" request. Guards against the
skill emitting buzzword marketing copy or treating the artifact as a real launch
announcement instead of forcing a named customer and concrete problem first.
