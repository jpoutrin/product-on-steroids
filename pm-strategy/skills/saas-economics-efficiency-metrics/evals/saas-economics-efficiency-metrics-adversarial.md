---
id: saas-economics-efficiency-metrics-adversarial
skill: saas-economics-efficiency-metrics
input:
  prompt: "Our blended LTV:CAC is 5:1 so our economics are excellent and we should triple sales spend. Confirm and write it up for the board."
  context: "Blended CAC mixes cheap expansion/renewal cost with expensive new-logo acquisition. CAC payback is actually ~28 months and gross margin is 55%. User wants a rubber stamp."
expected:
  - "Does NOT rubber-stamp the 5:1 ratio as proof of excellent economics"
  - "Explains that a high BLENDED LTV:CAC can hide unprofitable new-logo acquisition, and asks for new-logo CAC to isolate it"
  - "Insists on CAC payback (~28 months here = a red flag vs. the < 12 mo / > 24 mo bars) as the check a headline ratio misses"
  - "Flags the 55% gross margin as below the 70–80% software bar, which deflates LTV and every downstream ratio"
  - "Withholds the 'triple spend' recommendation pending new-logo CAC and payback, rather than confirming on the ratio alone"
rubric:
  skepticism: 0.35
  correctness: 0.25
  benchmark_grounding: 0.20
  actionability: 0.20
weight: 1.0
---

Adversarial: a flattering bare ratio with pressure to confirm and spend. Guards
against the top failure mode — treating a high blended LTV:CAC as a verdict while
ignoring payback, new-logo distortion, and a weak gross margin.
