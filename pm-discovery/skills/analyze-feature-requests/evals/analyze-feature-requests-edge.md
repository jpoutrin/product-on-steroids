---
id: analyze-feature-requests-edge
skill: analyze-feature-requests
input:
  prompt: "I've dumped all the requests in this spreadsheet. Some are vague ('make it faster', 'better UX'). Others are from a single vocal customer. Not sure what to prioritize."
  context: "Product: a developer-facing API analytics platform. ~45 requests. No explicit product strategy statement. Requests range from fully formed user stories to single-word complaints. One customer accounts for 8+ requests."
expected:
  - "Acknowledges the mixed quality of input and clarifies which requests are too vague to score (asking for translation or better definition as needed)"
  - "Handles duplicate/overlapping requests (e.g., 'make it faster' grouped into Performance theme) without losing signal"
  - "De-weights or flags the single vocal customer's requests so their frequency doesn't dominate prioritization"
  - "Makes reasonable assumptions about impact/effort when context is thin, and labels them as assumptions"
  - "Still produces a usable prioritization (at least 3–5 clusters and scores) even under incomplete data, rather than refusing to proceed"
  - "Notes in the output what additional data would improve confidence (e.g., 'Recommendation: survey top 10 customers on roadmap priorities')"
rubric:
  graceful_degradation: 0.30
  assumption_labeling: 0.25
  debiasing: 0.25
  completeness_under_constraint: 0.20
weight: 1.0
---

Edge case: mixed data quality, no explicit strategy, vocal-customer bias. Guards against both refusing to analyze sparse data and over-interpreting vague feedback.
