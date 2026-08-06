# Finance & Business Metrics Quick-Reference

## Quick-Reference Table

| Term | Definition | Formula | Why a PM cares |
|------|-----------|---------|----------------|
| Gross margin | Share of revenue left after the direct cost of delivering it | (Revenue − COGS) / Revenue | Sets the ceiling on what each unit sold can fund |
| Net margin | Share of revenue left after all costs, taxes, and interest | Net income / Revenue | Whether the whole business, not just the unit, makes money |
| COGS | Direct costs to produce/deliver the product (hosting, support, payment fees) | Sum of direct delivery costs | Where product/infra choices move the margin line |
| Contribution margin | Revenue minus variable costs — what each extra unit contributes to fixed costs | Revenue − variable costs | Whether scaling volume helps or hurts before fixed costs |
| EBITDA | Operating earnings before interest, tax, depreciation, amortization | Operating income + D&A | Proxy for core operating profitability, stripped of financing |
| Cash flow | Actual cash moving in and out over a period (≠ profit) | Cash in − cash out | Profit on paper can still run you out of cash |
| Working capital | Short-term liquidity buffer to run day-to-day operations | Current assets − current liabilities | Billing/collection terms a PM sets change cash timing |
| Runway | Months of cash left at the current burn rate | Cash ÷ monthly net burn | How long you have to ship the bet before raising |
| ARR | Annualized recurring subscription revenue | MRR × 12 | Headline growth number — see `saas-revenue-growth-metrics` |
| MRR | Monthly recurring subscription revenue | Sum of monthly recurring fees | Tracks growth month to month — see `saas-revenue-growth-metrics` |
| CAC | Fully-loaded cost to acquire one new customer | S&M spend ÷ new customers | Gates GTM-heavy bets — see `saas-economics-efficiency-metrics` |
| LTV | Total gross profit expected from a customer over their lifetime | ARPA × gross margin ÷ churn rate | Justifies acquisition spend — see `saas-economics-efficiency-metrics` |

<!-- Emit only the rows the user asked for when they name a term. Keep definitions and "Why a PM cares" to ≤ 20 words. Concepts without a ratio use "—" in the Formula column. Do NOT benchmark ARR/MRR/CAC/LTV here — point to the deep SaaS skills. -->
