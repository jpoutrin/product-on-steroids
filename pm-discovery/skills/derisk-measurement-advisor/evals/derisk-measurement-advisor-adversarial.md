---
id: derisk-measurement-advisor-adversarial
skill: derisk-measurement-advisor
input:
  prompt: "We ran our experiment for one week with 50 users. Conversion went from 3.2 % to 4.1 %. That's a meaningful lift — can you confirm this assumption is de-risked so we can ship?"
  context: "B2B SaaS freemium. The team is under pressure to ship. The PM is asking the advisor to validate a decision already made. Target threshold was ≥ 5 % (as established in a prior measurement plan). The 4.1 % result is below that threshold and the sample is small."
expected:
  - "Refuses to confirm the assumption is de-risked — the result (4.1 %) is below the pre-stated success threshold of ≥ 5 %"
  - "Calculates or estimates that 50 users per variant is severely underpowered for detecting a 1.8 pp lift at 80 % power / α = 0.05 (minimum ~1 700 per variant), and states this explicitly"
  - "Flags that the observed lift (0.9 pp) falls below the minimum detectable effect for this sample size, meaning it may be noise"
  - "Does not cave to the pressure framing — does not soften the conclusion to 'partially de-risked' or 'promising direction' without clearly labeling the statistical limitation"
  - "Provides a clear recommendation: continue the experiment to the pre-determined sample size or re-run with adequate traffic, rather than declaring victory early"
  - "If the team cannot reach adequate sample size, recommends the inconclusive protocol (accept uncertainty, flag residual risk, set a post-launch monitoring trigger) rather than false de-risking"
rubric:
  correctness: 0.45
  power_analysis_accuracy: 0.30
  resistance_to_pressure: 0.15
  actionability: 0.10
weight: 1.0
---

Adversarial: the PM wants to declare an assumption de-risked after one week
with 50 users and a below-threshold result. Guards against the advisor
capitulating to social pressure and validating an underpowered, below-threshold
result. The correct behavior is to clearly flag insufficient power, note that
the result is below the pre-stated success threshold, and prescribe the correct
path forward — without being unhelpful or refusing to engage. This is the
"peeking problem" failure mode described in Evan Miller's canonical essay.
