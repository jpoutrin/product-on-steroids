---
id: ab-test-analysis-edge
skill: ab-test-analysis
scenario: Positive lift present, but guardrail metric degrades and test is underpowered. Skill must surface the trade-off and recommend investigation or extension, not a confident ship decision.
input:
  prompt: "We tested a new onboarding flow. Should we ship it?"
  context: |
    Test ran for 7 days (one week, half a business cycle).
    Control (old flow): 1,240 completions from 12,150 starts (10.20% completion)
    Variant (new flow): 1,380 completions from 12,220 starts (11.29% completion)
    Relative lift: +10.7%
    Two-tailed z-test p-value: 0.052
    95% CI: [−0.01pp, +2.38pp]
    Guardrail metrics: Time-to-upgrade +45 minutes (6.2% increase), Support tickets +8.3%, User satisfaction (NPS) −3 points
    Novelty effect: Test ran only 1 week; new-flow users may be exploring, not yet habituated. Risk of novelty wear-off.
expected:
  - Flags p-value (0.052) as marginally not significant (just above 0.05 threshold)
  - Flags guardrail degradations (time-to-upgrade +6%, support tickets, NPS drop)
  - Identifies test power concerns and novelty/primacy effect window (1 week insufficient)
  - Acknowledges positive trend (10.7% lift) but recommends caution
  - Recommends "Investigate" or "Extend" — not ship
  - Suggests: extend test 2+ more weeks to confirm habituation and significance, root-cause guardrail concern (e.g., why support tickets up?), define business lift bar for trade-off acceptance
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge case: positive signal with caveats (marginal significance, guardrail concern, short duration). Skill must resist premature shipping and surface the trade-off clearly. Guards against: ignoring guardrail red flags, shipping underpowered tests, treating marginal p-values as green lights, skipping novelty effect assessment.
