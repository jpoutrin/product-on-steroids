---
id: identify-assumptions-existing-edge
skill: identify-assumptions-existing
input:
  prompt: >
    We run a consumer social app (think Instagram for pet lovers, ~100k MAU).
    We want to explore monetization. One idea is a "premium" tier: $2.99/month
    unlocks filters, badges, ad-free feed, early access to new features.
    Can you help us think through the risky assumptions before we build it?
  context: >
    Currently: 100% free, no revenue. Ad network rejected us (audience too young).
    Funding: $200k pre-seed, 8 months runway. Product engagement: DAU/MAU = 0.4.
    No existing community research or payment infrastructure.
expected:
  - "Skill asks clarifying questions if needed (e.g., churn risk, support load) and proceeds with reasonable assumptions stated."
  - "Desirability assumptions cover willingness-to-pay, feature desirability, and cannibalization risk (free users downgrading)."
  - "Viability assumptions cover payment-provider risk, revenue per user, and user-support complexity for a new revenue model."
  - "Feasibility assumptions cover payment integration complexity, A/B testing framework, and metrics tracking."
  - "Skill explicitly flags the constraint that this is a revenue experiment, not a feature experiment — assumptions should reflect that."
  - "Risk ranking surfaces the highest-uncertainty / highest-impact items (e.g., willingness-to-pay unknown = high uncertainty, high impact if wrong)."
rubric:
  accuracy: "Assumptions correctly reflect monetization-specific risks (payment, churn, LTV) not just feature risks. Confidence levels are honest (revenue model = low confidence). Does NOT treat this as a standard feature launch."
  completeness: "All three categories covered, with explicit monetization angles in Viability. Risk ranking surfaces top 3–5. Clarifying questions asked and answered (or assumptions stated). Summary addresses go/no-go for monetization readiness."
  actionability: "Suggested tests are revenue-specific (cohort pricing test, survey willingness-to-pay, etc.). Mitigation steps are concrete (e.g., 'run 2-week cohort A/B test on 10% of users')."
weight: 1.0
---

Edge scenario: vague or complex feature request; skill must ask clarifying questions and
state assumptions explicitly. This guards against the skill over-committing to assumptions
the user hasn't stated, and ensures it surfaces monetization-specific risks (not just feature risks).
Also tests whether the skill distinguishes between feature experiments and revenue experiments.
