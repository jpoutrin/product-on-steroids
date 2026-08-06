---
id: ab-test-analysis-adversarial
skill: ab-test-analysis
scenario: Incomplete or ambiguous data where test results hinge on unstated business context (e.g., what is the business lift bar? is this metric actually important?). Skill must ask clarifying questions and gracefully handle missing information rather than make unfounded recommendations.
input:
  prompt: "Our test results show a 3% increase. Is that good? Should we ship?"
  context: |
    We tested personalized email subject lines.
    Sample sizes not provided.
    Open rate increased from 18% to 18.55% (0.55pp, 3% relative lift).
    No p-value or confidence interval provided.
    No guardrail metrics mentioned.
    Test duration: unknown.
    No segment breakdown.
expected:
  - Asks for missing critical data (sample sizes, test duration, p-value/significance test, guardrail metrics)
  - Explains why each data point matters (e.g., "3% relative lift could be noise if sample size is small")
  - Acknowledges positive direction but refuses to recommend ship without rigor
  - Does not assume p < 0.05 or make up confidence intervals
  - Suggests a path forward: "Provide sample sizes and I can run a significance test" or "What business lift bar did you set for email open rate?"
  - Handles gracefully; offers to re-analyze once data is complete
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Adversarial case: vague, incomplete data with no clear business context. Skill must refuse to make recommendations without rigor, ask clarifying questions, and explain why each missing data point matters. Guards against: rubber-stamping results without statistical evidence, shipping based on hunches, failing to tie recommendations to business thresholds, making up missing data.
