# Assumption Prioritization Matrix

<!-- Fill in each section below. This template structures the output of prioritize-assumptions.
Remove this comment block in your final output. -->

## Priority Matrix

<!-- Paste the 2×2 matrix or ranked-table version. Use one of these formats:

**2×2 Grid Format** (text representation):
```
            Low Uncertainty  |  High Uncertainty
High Impact  • Assumption A  |  • Assumption B
             • Assumption C  |  • Assumption D
Low Impact   • Assumption E  |  • Assumption F
```

Or **Ranked Table Format** (recommended if >6 assumptions):
-->

| Rank | Assumption | Impact | Uncertainty | Validation Method | Timeline |
|------|-----------|--------|-------------|-----------------|----------|
| 1    | <assumption statement> | High | High | <experiment type, e.g., pre-order test> | <e.g., 1 week> |
| 2    | <assumption statement> | High | Medium | <method> | <timeline> |
| 3    | <assumption statement> | <High/Medium/Low> | <High/Medium/Low> | <method> | <timeline> |
| ... | ... | ... | ... | ... | ... |

## Quadrant Actions

### High Impact, High Uncertainty
**Action:** Test immediately.
- <list top-priority assumptions>
- <rationale: why these are critical>

### High Impact, Low Uncertainty
**Action:** Proceed or defer (low risk, lower learning value).
- <assumptions in this quadrant>
- <note: if confidence is high, consider whether testing adds value or if you should move to implementation>

### Low Impact, High Uncertainty
**Action:** Test only if time permits.
- <assumptions in this quadrant>
- <note: learning value is moderate but impact is lower; deprioritize if time is constrained>

### Low Impact, Low Uncertainty
**Action:** Deprioritize.
- <assumptions in this quadrant>
- <note: these are low-risk and low-learning; address after critical assumptions are validated>

## Key Scoring Rationale

<!-- Explain your impact and uncertainty scoring. Include:
- The decision or go/no-go gate that each high-impact assumption affects.
- Why key assumptions are scored high uncertainty (e.g., "no customer validation yet", "conflicting data").
- Any market or competitive context that influenced scoring.
-->

**Critical Assumption:** <top assumption and why it's ranked highest>

**Impact Scoring:** <brief explanation of how impact was determined, e.g., "based on whether assumption affects pricing/market sizing/feature roadmap">

**Uncertainty Scoring:** <brief explanation of confidence levels, e.g., "high because no customer feedback yet; medium because we have 5 customer interviews; low because we have 50+ customer data points">

**Tie-Breaker:** If impact and uncertainty are tied, which assumptions move up in the queue? <e.g., "assumptions affecting go/no-go gate first, then feature/channel decisions">
