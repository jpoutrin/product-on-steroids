---
id: saas-revenue-growth-metrics-adversarial
skill: saas-revenue-growth-metrics
input:
  prompt: "Our NRR is 115%, so retention is clearly great — put that in the board deck as proof our growth is durable."
  context: "SMB SaaS. No period or basis stated for the 115%. The customer count fell from 900 to 780 over the year, and total MRR is roughly flat. A few large accounts expanded heavily."
expected:
  - "Refuses to bless 115% at face value; demands the period and basis (monthly vs TTM) behind it"
  - "Separates revenue retention from logo retention and computes logo retention ~= 780 / 900 = ~87% (13% logo loss)"
  - "Flags that a high NRR driven by a few large expanding accounts can mask heavy logo churn on a shrinking base"
  - "Notes that flat total MRR alongside 115% NRR is a contradiction that must be reconciled (new-logo weakness or base shrink)"
  - "Does not endorse 'durable growth' from NRR alone; recommends showing NRR with GRR, logo retention, and the MRR bridge"
rubric:
  correctness: 0.30
  refuses_to_overclaim: 0.30
  revenue_vs_logo_distinction: 0.25
  actionability: 0.15
weight: 1.0
---

Adversarial: a flattering single metric (NRR 115%) with no period/basis, on a
shrinking-logo base with flat MRR. The skill must resist the leading framing,
demand basis, separate revenue from logo retention, and surface the contradiction
instead of rubber-stamping "durable growth."
