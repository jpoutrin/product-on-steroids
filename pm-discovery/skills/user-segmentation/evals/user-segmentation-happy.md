---
id: user-segmentation-happy
skill: user-segmentation
scenario: >
  Rich, multi-source feedback (interviews, usage logs, support tickets) with clear
  behavioral clusters and distinct jobs-to-be-done. Skill should identify 3–4 segments
  with confidence and produce actionable profiles with strategic recommendations.
input:
  prompt: >
    Segment our user base. I've attached 20 customer interviews (B2B SaaS workflow tool),
    6 months of support tickets (500+ messages), and usage telemetry for 1,200 active users.
  context: >
    Product: workflow automation platform for teams. Interviews cover designers, developers,
    ops managers, and compliance specialists. Support tickets span feature requests, bug reports,
    onboarding struggles. Usage logs show distinct patterns: power users (10+ automations),
    casual users (1–2), and heavy API integrators.
expected:
  - Output identifies ≥ 3 behavioral segments with distinct jobs and pain points (not demographic buckets).
  - Each segment is grounded in specific quotes, behavior counts, or usage patterns from provided data.
  - Segment sizes are estimated as % of user base with data source cited (e.g., "40% from interviews", "20% from support tickets").
  - Product fit is assessed per segment; gaps and churn risks are specific, not generic.
  - Value propositions are segment-tailored, addressing unique unmet needs; not one-size-fits-all messaging.
  - Prioritization matrix recommends invest / maintain / de-prioritize with clear rationale tied to strategic importance and difficulty.
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

**Why this scenario exists:**
This guards against surface-level segmentation. With rich data, the skill should produce deep,
grounded segment profiles that reveal distinct behavioral and motivational clusters, not just
demographic divisions. The skill must synthesize multiple data types and avoid generic segments.
Measures whether the skill actually uncovers *why* users behave differently, not just *that*
they do.
