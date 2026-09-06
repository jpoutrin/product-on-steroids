# Pricing Finance Memo: <Product / Unit / Plan>

## Inputs & Assumptions
- **Variable cost per unit/seat/mo:** <€X> — *given / assumed (default)*
- **Gross-margin floor:** <Y%> — *given / assumed (default 70–80% SaaS)*
- **CAC:** <€X> — *given / assumed / N/A*
- **Customer lifetime:** <N months> (or churn <Z%/mo>) — *given / assumed / N/A*
- **Proposed price:** <€X/unit/mo> — *given / N/A*
- **Targets:** LTV:CAC ≥ <3:1>, payback ≤ <12/18 mo> — *default unless overridden*

## Price Floor
- **Formula:** variable_cost ÷ (1 − margin_floor)
- **Arithmetic:** <€X> ÷ (1 − <Y%>) = **<€floor>/unit/mo**
- Nothing below **<€floor>** holds the <Y%> margin.

## Finance-Justified Target Price
- **Target:** **<€target>/unit/mo**
- **Reasoning:** starts at the floor <€floor>; raised to clear LTV:CAC ≥ <3:1> and
  payback ≤ <N mo>. Headroom rationale: <...>

## Guardrail Check @ <proposed / target €X>
| Guardrail    | Computation                            | Value  | Target   | Verdict       |
|--------------|----------------------------------------|--------|----------|---------------|
| Gross margin | (price − cost) / price                  | <Y%>   | ≥ <Y%>   | PASS/FAIL     |
| LTV:CAC      | (price × margin × lifetime_mo) / CAC    | <R:1>  | ≥ 3:1    | PASS/FAIL/N/A |
| CAC payback  | CAC / (price × margin per month)        | <N mo> | ≤ <N mo> | PASS/FAIL/N/A |

## Where It Breaks
- **Binding constraint:** <which guardrail fails first>
- **Flips to PASS at:** price <€X> (holding CAC) — or CAC <€X> / cost <€X> / lifetime <N mo>

| Lever | Current | Needed to PASS |
|-------|---------|----------------|
| Price | <€X>    | <€X>           |
| CAC   | <€X>    | <€X>           |

## Verdict
**<PROCEED / PROCEED WITH FIX / DO NOT PROCEED>** — <single most important number and the one action>.
