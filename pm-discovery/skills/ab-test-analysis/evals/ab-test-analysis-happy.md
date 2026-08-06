---
id: ab-test-analysis-happy
skill: ab-test-analysis
scenario: Straightforward positive test result with strong statistical significance, adequate power, no guardrail concerns. Skill should recommend shipping with confidence.
input:
  prompt: "We ran a test increasing the checkout discount from 10% to 15%. Analyze the results."
  context: |
    Test ran for 14 days across all traffic.
    Control (10% discount): 8,432 conversions from 68,250 sessions (12.35% conv rate)
    Variant (15% discount): 9,187 conversions from 68,180 sessions (13.48% conv rate)
    Relative lift: +9.2%
    Two-tailed z-test p-value: 0.008
    95% CI: [+0.3pp, +1.9pp]
    Guardrail metrics: Average Order Value flat (−0.8%), Revenue per session +8.3%, Page load time +2ms (negligible)
    Novelty effect: Test ran across 2 full weeks; discount effect is not time-isolated.
expected:
  - Correctly identifies statistical significance (p = 0.008 < 0.05)
  - Confirms practical significance (9.2% relative lift exceeds typical business bar)
  - Validates test power and duration (14 days, ~68k samples per arm)
  - Clears guardrail metrics and contextualizes AOV flat vs RPS up trade-off
  - Recommends shipping with rationale tied to quantitative thresholds
  - Includes next steps (monitor guardrails post-launch, segment performance)
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy path: positive lift, clean statistical case, no trade-offs. Skill should confidently recommend ship and provide monitoring guidance. Guards against: recommendations made without statistical rigor, missed guardrail review, vague next steps.
