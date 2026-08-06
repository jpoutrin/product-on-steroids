---
id: derisk-measurement-advisor-edge
skill: derisk-measurement-advisor
input:
  prompt: "Our core assumption is that users will trust us more after we add a security badge and a customer-story section to the homepage. We're doing a usability study and 5-second tests with 12 participants. How should we measure this assumption?"
  context: "Early-stage B2C SaaS. No existing trust or NPS baseline. The team has 12 recruited participants (split 6/6 between current homepage and redesigned version). Timeline: 2 weeks."
expected:
  - "Explicitly flags that 'users will trust us more' is not directly measurable and must be translated into observable proxy metrics"
  - "Proposes concrete proxy metrics for trust (e.g., trust-scale rating, perceived-credibility score, willingness to enter payment details, self-reported hesitation, 5-second recall of trust signals)"
  - "Acknowledges that 12 participants is below typical statistical thresholds and frames the output in saturation/confidence-level terms rather than p-values"
  - "Sets a qualitative success criterion (e.g., ≥ 4 of 6 participants in the redesign group spontaneously mention the security badge as increasing trust)"
  - "Notes the limitation that proxy metrics may not predict real-world trust behavior and recommends a follow-on quantitative signal (e.g., sign-up rate, payment-initiation rate) once the product is live"
  - "Includes an inconclusive protocol appropriate for qualitative studies (e.g., extend recruitment vs. accept uncertainty and flag as open risk)"
rubric:
  correctness: 0.40
  proxy_translation_quality: 0.30
  honest_limitation_acknowledgment: 0.20
  actionability: 0.10
weight: 1.0
---

Edge case: the assumption is qualitative and not directly measurable — a common
PM trap. Guards against the advisor (a) pretending a 12-person study is
statistically powered, (b) refusing to engage because the assumption is fuzzy,
or (c) producing a measurement plan that ignores the gap between proxy metrics
and the real underlying construct (trust). The correct behavior is to translate,
acknowledge limitations, and still produce a usable plan.
