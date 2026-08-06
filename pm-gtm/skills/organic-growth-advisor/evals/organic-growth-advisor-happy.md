---
id: organic-growth-advisor-happy
skill: organic-growth-advisor
input:
  prompt: >
    We run a B2B SaaS HR onboarding tool targeting People Ops managers at
    companies with 50–500 employees. We have early traction (120 paying customers,
    NPS 52). We want an organic growth playbook for the next 12 months. We have
    a 2-person marketing team and a $3K/month content budget. We're already doing
    occasional LinkedIn posts but have no SEO programme, no community, and no
    referral mechanism.
  context: >
    B2B SaaS, HR/People Ops ICP, early traction stage, 12-month horizon,
    2-person team, $3K/month content budget, LinkedIn ad hoc only, no SEO/community/referral.
expected:
  - "Playbook explicitly states ICP (People Ops managers, 50–500 employee companies) in the Context block"
  - "SEO/content is recommended with a time-to-impact of at least 6 months — not labelled a quick win"
  - "Recommended tactics have effort ratings (S/M/L) and time-to-impact ranges for every row"
  - "Sequencing has three distinct phases (months 1–3, 4–6, 7–12) with dependency logic"
  - "Measurement plan includes at least one leading and one lagging indicator per tactic"
  - "Referral or word-of-mouth tactic is recommended given NPS 52 (strong advocate signal)"
  - "Quick Wins vs Long-Term Bets section clearly separates 90-day signal from 6–18-month compounders"
  - "Playbook does not recommend paid channels (organic-only scope respected)"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy path: a well-specified B2B SaaS with a clear ICP, real traction (NPS 52 is a
referral signal), a content budget, and a 12-month horizon. Guards against the failure
mode of recommending all channels without prioritisation, mislabelling SEO as fast, or
ignoring the referral surface that high NPS unlocks. The skill must produce a sequenced,
opinionated playbook — not a generic channel list.
