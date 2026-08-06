---
id: opportunity-solution-tree-edge
skill: opportunity-solution-tree
input:
  prompt: "Build an OST for our B2B project management SaaS. We want to reduce churn. We haven't done formal user research yet — only have a few anecdotal observations from the sales team."
  context: "Sales team observations: 'customers complain the reporting is confusing', 'a few accounts said onboarding was hard', 'one customer churned because they couldn't integrate with Slack'. No interview data, no survey data, no analytics breakdown of churn cohorts. Desired outcome is vague: 'reduce churn'."
expected:
  - "Asks for or proposes a specific measurable desired outcome (e.g., reduce monthly churn rate from X% to Y%) rather than proceeding with the vague 'reduce churn' framing"
  - "Acknowledges the research gap explicitly and labels opportunities as hypotheses, not validated findings"
  - "Still produces a usable skeleton OST with clearly marked hypothesis placeholders rather than refusing entirely"
  - "Recommends discovery activities (e.g., churn interviews, cohort analysis) to validate the hypothetical opportunities before committing to solutions"
  - "Does not fabricate evidence anchors — each opportunity is labeled as a hypothesis or anecdotal signal, not a validated pain"
  - "Experiment suggestions prioritize fast discovery methods (e.g., churn exit interviews, prototype tests) over premature A/B tests on an unvalidated tree"
rubric:
  scoping_discipline: 0.35
  completeness: 0.30
  correctness: 0.20
  actionability: 0.15
weight: 1.0
---

Edge case: sparse and anecdotal research signal combined with a vague desired
outcome. Guards against two failure modes: (1) fabricating confident opportunities
from thin evidence, and (2) refusing to produce anything useful. The skill must
thread the needle — deliver a useful skeleton while being honest about what is
hypothesis vs. validated. Also guards against skipping the outcome-clarification
step when "reduce churn" is given without a baseline or target.
