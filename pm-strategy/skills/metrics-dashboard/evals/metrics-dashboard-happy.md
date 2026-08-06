---
id: metrics-dashboard-happy
skill: metrics-dashboard
input:
  prompt: "Design a metrics dashboard for our B2B team collaboration tool. Core value moment is a team publishing a shared doc."
  context: "Subscription B2B SaaS. ~940 weekly active teams today. Tooling: Amplitude + Metabase. No existing NSM."
expected:
  - "Defines exactly one North Star Metric as a rate/ratio over a time window tied to the publish value moment, not a cumulative signup or pageview count"
  - "Decomposes the NSM into 3-5 input metrics each mapped to a funnel/lifecycle stage with the input-to-NSM link stated"
  - "Includes at least 2 health guardrails (e.g. latency, error rate, complaint/NPS) with thresholds"
  - "Includes a business-metrics layer (e.g. MRR, CAC, LTV, churn) linked to the tree"
  - "Every metric row has a formula, cadence, owner, target, and alert threshold with no blank cells"
  - "Each alert names a threshold, audience, channel, and response time; review cadence spans daily/weekly/monthly/quarterly"
rubric:
  correctness: 0.35
  completeness: 0.3
  actionability: 0.2
  no_vanity_metrics: 0.15
weight: 1.0
---

Happy path: a clear value moment and enough context to build a full NSM → inputs
→ health → business tree with every cell defined. Guards against unstructured
metric lists and undefined rows.
