---
id: outcome-roadmap-edge
skill: outcome-roadmap
input:
  prompt: "Rewrite our roadmap as outcomes. H1: SSO login, audit log export, mobile app. H2: role-based permissions, SCIM provisioning."
  context: "B2B security/compliance SaaS moving upmarket to enterprise. No metric baselines are available yet and no OKRs were shared."
expected:
  - "Still produces an outcome statement per output in the Enable ... to ... so that ... form"
  - "Names a plausible success metric for each outcome but marks it 'baseline TBD' rather than fabricating a number"
  - "Does not silently drop the metric column just because baselines are missing"
  - "Flags the absence of stated objectives/OKRs as an assumption to confirm, and infers the enterprise-move intent"
  - "Keeps H1/H2 phase windows as ranges, not invented calendar dates"
rubric:
  correctness: 0.3
  measurability: 0.3
  handles_missing_data: 0.25
  actionability: 0.15
weight: 1.0
---

Edge: no baselines and no OKRs. Guards against fabricating metrics and against
skipping measurability when data is thin — must use "baseline TBD" and flag
the missing strategic context instead of guessing hard numbers.
