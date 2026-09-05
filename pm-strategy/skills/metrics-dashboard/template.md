# Metrics Dashboard Spec: <Product>

## North Star Metric <!--#north-star-metric-->
- **NSM:** <metric name>
- **Formula:** <numerator / denominator + time window>
- **Why it captures value:** <the value moment it measures; why it leads business success>
- **Target:** <goal value> (from <current baseline>)

## Metric Tree <!--#metric-tree-->
```
NORTH STAR: <NSM> = <current> → <target>
   ├── Input 1: <metric> (<lifecycle stage>)   → drives NSM via <link>
   ├── Input 2: <metric> (<lifecycle stage>)   → drives NSM via <link>
   ├── Input 3: <metric> (<lifecycle stage>)   → drives NSM via <link>
   └── Input 4: <metric> (<lifecycle stage>)   → drives NSM via <link>
```
- **Link:** <the arithmetic or causal path from inputs up to the NSM>

## Metric Definitions <!--#metric-definitions-->
| Metric | Layer | Formula (numerator/denominator + window) | Cadence | Owner | Target | Alert Threshold |
|--------|-------|------------------------------------------|---------|-------|--------|-----------------|
| <NSM>   | North Star | <...> | <...> | <...> | <...> | <...> |
| <input> | Input      | <...> | <...> | <...> | <...> | <...> |
| <guard> | Health     | <...> | <...> | <...> | <...> | <...> |
| <biz>   | Business   | <...> | <...> | <...> | <...> | <...> |

## Health Guardrails <!--#health-guardrails-->
- **<metric>** — <what gaming/degradation it catches> — threshold: <value>
- **<metric>** — <...> — threshold: <value>

## Business Metrics <!--#business-metrics-->
- **<metric>** — <formula> — links the tree to <revenue/cost/unit economics>
- **<metric>** — <...>

## Review Cadence & Alerts <!--#review-cadence-alerts-->
- **Daily:** <operational health metrics>
- **Weekly:** <input metrics & engagement>
- **Monthly:** <NSM, business metrics, OKR progress>
- **Quarterly:** <strategic review & metric recalibration>

| Alert | Threshold | Notified | Channel | Response time |
|-------|-----------|----------|---------|---------------|
| <...> | <...>     | <...>    | <...>   | <...>         |
