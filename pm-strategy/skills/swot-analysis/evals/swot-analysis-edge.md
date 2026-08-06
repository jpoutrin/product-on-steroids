---
id: swot-analysis-edge
skill: swot-analysis
input:
  prompt: "Here are factors for our SWOT: a new competitor just raised $50M; our churn is 9%; regulators may cap our pricing next year; our founder is well-known in the space; customers love our API. Sort these and finish the analysis."
  context: "The user has dumped a mixed list without labeling internal vs external, and some items are easy to misfile."
expected:
  - "Correctly classifies each factor: churn and API love and founder reputation as internal (W/S/S); competitor raise and pricing regulation as external (T/T)"
  - "Explicitly applies the internal-vs-external test (do we control it?) rather than accepting the user's implied placement"
  - "Fills out the remaining quadrants where the dump is thin, flagging added items as assumptions when evidence is absent"
  - "Cross-references into TOWS pairs, e.g. using API love (S) against the funded competitor (T)"
  - "Names the pricing-cap regulation as a top uncertainty with a way to validate its likelihood"
rubric:
  classification_discipline: 0.40
  correctness: 0.25
  tows_synthesis: 0.20
  assumptions_explicit: 0.15
weight: 1.0
---

Edge: a mixed, partly-misfileable factor dump. Guards against passively echoing the
user's placement instead of enforcing the internal/external axis that makes SWOT useful.
