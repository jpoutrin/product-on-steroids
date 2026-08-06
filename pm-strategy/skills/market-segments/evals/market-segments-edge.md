---
id: market-segments-edge
skill: market-segments
input:
  prompt: "We're launching a consumer habit-tracking app. Segment the market for us."
  context: "No customer research yet. Only signal is app-store reviews of competitors: some users want streaks/gamification, some want gentle non-judgmental reminders, some are recovering from burnout and want minimalism."
expected:
  - "Infers segments from the behavioral signals available (motivation style) rather than fabricating demographic data"
  - "Anchors each segment on a job-to-be-done and desired outcome despite sparse data"
  - "Explicitly flags low confidence and marks scores as estimates where evidence is thin"
  - "Holds segments distinct and non-overlapping, or explains where overlap risk is highest"
  - "Still produces a Size/Attractiveness/Reachability matrix and a single beachhead pick"
  - "Lists the riskiest assumptions and concrete research to validate them before committing"
rubric:
  correctness: 0.30
  assumptions_explicit: 0.30
  completeness: 0.20
  actionability: 0.20
weight: 1.0
---

Edge: near-zero first-party data. The skill must infer JTBD segments from behavioral
proxies, keep them distinct, and be honest about confidence instead of inventing
firmographics. Guards against false precision and against refusing to segment at all.
