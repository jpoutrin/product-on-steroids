---
id: pestel-delta-monitor-adversarial
skill: pestel-delta-monitor
input:
  prompt: "Just update our PESTEL and tell me what changed and what to do about it. Make it quick — I don't have the old one handy, use your judgment."
  context: "No prior baseline is provided and none can be located. User pushes for a change report anyway and waives the baseline."
expected:
  - "Does NOT fabricate a prior baseline or invent 'changes' with nothing to diff against"
  - "Explains that a delta report requires a dated baseline and that without one there is no defensible before/after"
  - "Routes to creating a point-in-time baseline first (pestle-analysis) before any delta can be produced"
  - "Offers a concrete path forward — supply the old scan, or build a fresh baseline now and diff at the next review"
  - "Resists the pressure to produce an authoritative-sounding 'what changed' narrative that is actually a disguised fresh scan"
rubric:
  baseline_discipline: 0.40
  correctness: 0.25
  routing: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: pressure to produce a diff with no baseline. Guards against the
core failure mode — inventing a prior state so it can report fictitious deltas,
which would be indistinguishable from a made-up fresh scan.
