---
id: jobs-to-be-done-adversarial
skill: jobs-to-be-done
input:
  prompt: "Map the JTBD for our customers — they want a faster dashboard with real-time data and a mobile app."
  context: >
    Segment: small business owners using an accounting SaaS. The user has framed
    the entire ask as a feature list: faster dashboard, real-time data, mobile
    app. No situation or outcome language is present in the input.
expected:
  - "Refuses to embed solution terms (faster dashboard, real-time data, mobile app) inside any job statement"
  - "Reframes the input from features to underlying motivation — identifies what progress the customer is trying to make that those features are proxies for"
  - "Produces at least one canonical job statement in When/I want to/so I can format that is free of solution language"
  - "Explains to the user why feature-framed input must be translated to job language before a valid JTBD analysis can be produced"
  - "Flags that the reframed job statements are hypotheses requiring validation, since no interview data was provided"
rubric:
  correctness: 0.40
  reframing_quality: 0.30
  format_conformance: 0.20
  actionability: 0.10
weight: 1.0
---

Adversarial case: the user smuggles solutions into what should be a motivation
mapping exercise. Guards against the skill laundering feature requests into
pseudo-JTBD statements. The skill must actively reframe — not refuse outright —
explaining the JTBD lens and producing valid job statements that strip out the
solution layer while preserving (and making explicit) the underlying progress
the customer is seeking.
