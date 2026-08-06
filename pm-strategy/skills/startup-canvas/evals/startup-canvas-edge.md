---
id: startup-canvas-edge
skill: startup-canvas
input:
  prompt: "Here's my idea: a mobile app that helps people find local hiking buddies. Make me a startup canvas."
  context: "Consumer idea, pre-launch, no data, no competitors named, no pricing thought through. Founder is one person coding nights/weekends."
expected:
  - "Still produces all 11 sections, filling gaps with clearly labeled hypotheses rather than inventing facts"
  - "Marks unknown market-size, cost, and revenue figures as hypotheses/estimates, never as unsupported numbers"
  - "Proposes at least one plausible first segment defined by a problem/JTBD and justifies why it's first"
  - "Chooses a defensible cost positioning and a pricing approach even with thin input, flagging it as tentative"
  - "Ends with a Hypotheses & Experiments list pairing each riskiest assumption with a low-effort test"
rubric:
  correctness: 0.3
  completeness: 0.25
  assumptions_explicit: 0.3
  actionability: 0.15
weight: 1.0
---

Edge: sparse consumer input with no competitors, data, or pricing. Guards
against the skill either refusing or fabricating figures — it must fill the
canvas with explicit hypotheses and cheap validation experiments.
