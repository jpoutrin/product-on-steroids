---
id: voice-of-customer-miner-happy
skill: voice-of-customer-miner
input:
  prompt: "Mine the voice of the customer from these 50 app store reviews and 20 support tickets for our project management app. Surface the top themes with verbatim quotes."
  context: "Sources: 50 App Store reviews (mixed ratings, past 90 days) + 20 Zendesk support tickets (past 60 days). No segment filter. Default 5 top themes. Reviews and tickets both mention onboarding, notification overload, and mobile performance."
expected:
  - "Reports at least 5 themes, each with a sentiment tag (Positive/Negative/Mixed) and a volume count or estimate"
  - "Every exemplar quote in Theme Breakdown is verbatim from the input — no paraphrased summaries substituted for quotes"
  - "Themes are derived from patterns across both sources (App Store + support tickets), not from a single source only"
  - "Notable Gaps section names at least two topics absent from the corpus with a hypothesis for each"
  - "JTBD Signals section contains at least one job statement per major theme, each supported by a verbatim quote"
  - "Recommended Actions are explicitly tied back to named themes or gaps"
rubric:
  correctness: 0.35
  verbatim_fidelity: 0.30
  completeness: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: two distinct source types with overlapping pain themes, enough signal
to produce a full five-theme synthesis. Guards against paraphrasing customer
language, single-source theme elevation, and recommendations that float free
of the evidence.
