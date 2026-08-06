---
id: pestle-analysis-happy
skill: pestle-analysis
input:
  prompt: "Run a PESTLE scan for launching our B2B HR-tech SaaS into the German market next year."
  context: "Cloud payroll/HR product, EU-headquartered, entering Germany. Sector: HR software. Question: market-entry go/no-go."
expected:
  - "Covers all six lenses (Political, Economic, Social, Technological, Legal, Environmental) with 3-5 factors each"
  - "Rates every factor on both Impact (H/M/L) and Likelihood (H/M/L)"
  - "Gives each factor a 'so what for our product' implication specific to a German HR-tech launch"
  - "Grounds factors in German/EU context (e.g. GDPR, works-council/co-determination law, DATEV integration) rather than generic statements"
  - "Extracts priority factors tagged Opportunity/Threat/Compliance with a strategic response"
  - "Frames the output as a point-in-time snapshot with an as-of date and a watch-list handed to pestel-delta-monitor"
rubric:
  correctness: 0.35
  completeness: 0.25
  actionability: 0.25
  point_in_time_framing: 0.15
weight: 1.0
---

Happy path: enough geography and sector context to rate all six lenses concretely
and extract priorities. Guards against generic word-cloud factors, missing
impact/likelihood ratings, and losing the point-in-time framing.
