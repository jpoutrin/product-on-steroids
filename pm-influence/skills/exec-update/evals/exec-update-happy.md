---
id: exec-update-happy
skill: exec-update
input:
  prompt: "Write an executive status update for the Payments Revamp initiative."
  context: |
    Audience: VP Product and CFO.
    Period: Week of 28 Jul – 1 Aug 2026.
    Completed: New checkout flow launched on 30 Jul; A/B test running with
    10% traffic split; conversion rate up 2.1 pp vs. control.
    In progress: Back-end payment processor migration (65% complete).
    Slipped: PCI-DSS audit scheduled for 5 Aug is now pushed to 19 Aug due
    to auditor availability.
    Risks: Processor migration may surface edge-case failures in multi-currency
    transactions during load testing (owner: Elena R., Engineering).
    Asks: Approve the revised audit timeline with legal by 8 Aug so vendor
    contracts stay in force.
    Next milestone: Full traffic rollout of new checkout flow, target 15 Aug.
expected:
  - "BLUF is the first section and contains a clear GREEN / AMBER / RED signal"
  - "BLUF is self-contained — an executive reading only BLUF understands status and next action"
  - "Status section uses bullet points with completed, in-progress, and slipped items"
  - "Key Risks names the multi-currency edge-case risk with impact and owner (Elena R.)"
  - "Asks includes the legal approval request phrased with an action verb and a deadline (8 Aug)"
  - "Next Milestone states the 15 Aug full-rollout checkpoint"
  - "Body is ≤ 350 words and contains no unexplained acronyms"
rubric:
  bluf_signal_clarity: 0.30
  completeness: 0.25
  asks_actionability: 0.25
  plain_language: 0.20
weight: 1.0
---

Happy path: all five required inputs are provided with concrete detail.
Guards against padding, jargon, and omitting the status signal from the
BLUF. Also verifies the skill correctly identifies AMBER (audit slip + risk)
rather than defaulting to GREEN.
