---
id: cohort-analysis-happy
skill: cohort-analysis
input:
  prompt: "Analyze our monthly user cohorts from Jan–Apr 2025. We want to understand retention trends and why Q1 cohorts underperform Q4 2024."
  context: "Monthly acquisition cohorts; data includes cohort size, retention %, DAU, and feature adoption. Jan 1: onboarding flow redesigned. Mar 15: new feature X launched."
expected:
  - "Quantified retention curves for each cohort (not round numbers; actual % values)"
  - "Cohort-to-cohort comparison showing Q1 vs. Q4 performance delta with magnitudes"
  - "At least 2 inflection points identified (e.g., Week 1 churn spike, adoption jump post-feature launch)"
  - "Churn drivers tied to data or flagged as hypotheses requiring follow-up"
  - "2–4 specific, testable product recommendations grounded in findings"
  - "Qualitative and quantitative follow-up research outlined (who, what, when)"
  - "Report structured per template.md with all 7 sections (Data Summary, Retention Curves, Inflection Points, Churn Drivers, Recommendations, Follow-Ups, Limitations)"
rubric:
  correctness: 0.3
  completeness: 0.35
  actionability: 0.35
weight: 1.0
---

Happy path: clean, multi-cohort monthly data with clear product context and
a feature launch to correlate. Guards against single-metric analysis, round
guesses, and vague recommendations. Tests the skill's ability to compare cohorts
quantitatively and tie findings to product events.
