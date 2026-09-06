# Revenue-Metrics Readout — <company / cohort>, <period>

## Inputs & Period
- Starting MRR/ARR: <start figure>
- Movements this period — new: <n>, expansion: <n>, contraction: <n>, churned: <n>
- Ending MRR/ARR: <end figure>
- Customers: start <n>, end <n>, logos lost <n> (if provided)
- Period length: <monthly / quarterly> | Retention basis: <monthly / trailing-12-month>
- Assumptions made to fill gaps: <none | list>

## MRR Bridge
Start MRR <start>
  + New          <new>
  + Expansion    <expansion>
  − Contraction  <contraction>
  − Churned      <churned>
  = End MRR      <end>   (reconciles to reported ending MRR: yes/no)

## Metrics Table

| Metric | Value | Formula (numbers substituted) | Benchmark (good / median / weak) | Read |
|--------|-------|-------------------------------|----------------------------------|------|
| NRR (<basis>) | <value> | (start + expansion − contraction − churned) ÷ start | <band for stage/segment> | <one line> |
| GRR (<basis>) | <value> | (start − contraction − churned) ÷ start | <band> | <one line> |
| ARR growth (<basis>) | <value> | (end − start) ÷ start | <band> | <one line> |
| SaaS quick ratio | <value> | (new + expansion) ÷ (contraction + churned) | <band> | <one line> |
| Logo retention | <value or "insufficient data — need customer counts"> | retained customers ÷ starting customers | <band> | <one line> |
| ARPA | <value or "insufficient data — need customer count"> | MRR ÷ customers | <band> | <one line> |

## Interpretation
<2–4 sentences: is growth durable (NRR vs 100%, quick ratio vs 4)? where is the
leak — contraction vs churn, revenue vs logo? what the metrics together say that
no single one does.>

## Pitfalls & Caveats
- <specific distortion in play, e.g. annual-prepay lumpiness inflating a month>
- <cohort mixing / small-N noise / shrinking base flattering a ratio>
- <what to validate or re-cut before trusting the numbers>
