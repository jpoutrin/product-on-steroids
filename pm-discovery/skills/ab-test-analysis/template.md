# A/B Test Results: <Test Name>

## Experiment Overview
- **Hypothesis:** <What we expected to happen and why>
- **What Changed:** <Description of the variant>
- **Primary Metric:** <KPI being tested>
- **Guardrail Metrics:** <Secondary metrics that should not degrade>
- **Duration:** <X days> | **Traffic Split:** <% control / % variant>
- **Sample Sizes:** <N control> / <N variant>

## Test Validation
- **Power Analysis:** <Sample size adequate for effect size? Flag if underpowered (<80% power)>
- **Test Duration:** <Did it run ≥ 1–2 business cycles? Any novelty/primacy effect window?>
- **Randomization Health:** <SRM check — any sample ratio mismatch?>
- **Status:** <All clear / Flag noted (explain)>

## Statistical Results

| Metric | Control | Variant | Lift | 95% CI | p-value | Significant? |
|--------|---------|---------|------|--------|---------|--------------|
| <Primary Metric> | <X%> | <Y%> | <+Z%> | [<lower>, <upper>] | <0.0X> | Yes/No |
| <Guardrail 1> | <X%> | <Y%> | <+Z%> | [<lower>, <upper>] | <0.0X> | — |
| <Guardrail 2> | <X%> | <Y%> | <+Z%> | [<lower>, <upper>] | <0.0X> | — |

**Relative Lift:** <(variant − control) / control × 100>%  
**Confidence Interval:** <95% CI interpretation — does zero fall within it?>  
**Statistical Significance:** <p-value < 0.05 → yes; explain in context>

## Guardrail Check
- **Revenue/Engagement:** <No change / degraded by <X%> — investigate>
- **Page Load / Performance:** <No change / improved / degraded>
- **Churn / Retention:** <No change / flagged>
- **Conclusion:** <All guardrails green / Trade-off analysis / Showstopper>

## Segment Breakdown (if applicable)
| Segment | Control | Variant | Lift | Direction |
|---------|---------|---------|------|-----------|
| <e.g., New Users> | <X%> | <Y%> | <+Z%> | ↑ or ↓ or — |
| <e.g., Mobile> | <X%> | <Y%> | <+Z%> | ↑ or ↓ or — |

**Inversions:** <Note if metric direction differs by segment>

## Recommendation
**Decision:** Ship / Extend / Stop / Investigate

**Reasoning:** <Tie the recommendation to quantitative thresholds: statistical significance, practical significance (business lift bar), guardrail status, power, novelty effect timing>

**Business Impact:** <If shipping: expected lift in absolute terms over 30 days, revenue impact, etc.>

## Next Steps
- **If Shipping:** <Rollout plan, monitoring guardrails post-launch, segment-specific rollout strategy if needed>
- **If Extending:** <Additional data needed, revised sample size, suggested duration>
- **If Stopping:** <Why the result doesn't justify continuation, alternative hypotheses to test>
- **If Investigating:** <Which trade-offs or caveats need resolution before shipping, suggested deep-dive activities>
