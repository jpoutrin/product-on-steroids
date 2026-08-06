---
id: prioritize-features-edge
skill: prioritize-features
input:
  prompt: "Rank these ideas for our goal of reducing churn: better error messages, self-serve cancellation flow, health-score alerts, mobile app, annual billing."
  context: "Objective is clear (reduce churn) but there are NO effort estimates and no reach numbers — early-stage team, sparse data."
expected:
  - "Recognizes reach/effort data is missing and switches to ICE (or elicits/T-shirt-sizes effort) rather than forcing RICE"
  - "Scores each candidate on Impact, Confidence, Ease with a stated 1–10 scale applied consistently"
  - "Explicitly flags the low-confidence scores caused by sparse data and names a way to validate the most uncertain ones"
  - "Still produces a ranked table and a top recommendation set traceable to the churn objective"
  - "Does not invent precise reach numbers or present guesses as facts"
rubric:
  correctness: 0.3
  completeness: 0.25
  assumptions_explicit: 0.3
  actionability: 0.15
weight: 1.0
---

Edge case: right objective but missing effort/reach data. The skill must degrade
gracefully to ICE, size effort, and be honest about low confidence rather than
fabricating RICE inputs.
