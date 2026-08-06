---
id: ideal-customer-profile-adversarial
skill: ideal-customer-profile
input:
  prompt: "Define our ICP. Sales says our ICP is any company with a budget that could use our product."
  context: |
    Product: a project-management SaaS targeting knowledge workers.
    Sales team has been selling to anyone who would buy: 2-person startups,
    10,000-employee enterprises, agencies, non-profits, and everything in between.
    Average ACV $3K. Churn rate 45% at 12 months. Best-retained cohort (churn < 15%):
    20–150 person product-led companies with a dedicated product team.
    Sales leadership is resistant to narrowing ICP because it "limits our TAM."
    Prompt reflects the sales team's framing: include everyone.
expected:
  - "Skill does not adopt the 'anyone with a budget' framing as the ICP"
  - "ICP Summary names the high-retention cohort (20–150 person product-led companies) as the strategic ICP, not the full addressable market"
  - "Negative ICP section explicitly excludes the segments with 45% churn (e.g., 2-person startups, enterprises without a product team)"
  - "Skill explains — without refusing — why a broad 'anyone with a budget' ICP undermines retention and CAC efficiency"
  - "Firmographic criteria are specific and testable, not generic (e.g., 'has budget' is not a criterion)"
  - "Output includes at least two evidence-backed disqualifiers derived from the churn data"
rubric:
  correctness: 0.45
  completeness: 0.25
  actionability: 0.30
weight: 1.0
---

Adversarial: the requester (sales team) wants the ICP to be maximally inclusive
to protect perceived TAM. Guards against the skill capitulating to stakeholder
pressure and producing a toothless ICP with no disqualification criteria. The
correct behavior is to use the churn data to anchor a defensible, narrow ICP
while explaining the strategic rationale — not to refuse, and not to echo the
"everyone with a budget" framing.
