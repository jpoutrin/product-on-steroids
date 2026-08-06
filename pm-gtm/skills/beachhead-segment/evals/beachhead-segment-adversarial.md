---
id: beachhead-segment-adversarial
skill: beachhead-segment
input:
  prompt: "We want to target all SMBs in Europe from day 1. Help us plan the GTM."
  context: |
    Product: expense management SaaS, €15/user/month. Pre-launch, 2-person founding
    team, €500k pre-seed raised. Founder insists the product is horizontal and
    applicable to every SMB (1-200 employees) across Europe. They believe narrowing
    down is "leaving money on the table." No customer interviews yet.
expected:
  - "Pushes back on the go-broad-from-day-1 request with a clear explanation of
    why it is a beachhead anti-pattern (resource dilution, slow feedback loops,
    inability to dominate any segment)"
  - "Does NOT simply comply and produce a broad GTM plan as requested"
  - "Explains that a narrow beachhead increases the probability of dominance and
    makes references credible, which is what enables later expansion"
  - "Proposes a path: pick a beachhead first, then expand — and offers to run the
    segment-scoring exercise"
  - "Flags the absence of customer interviews as a risk and recommends discovery
    before finalizing the beachhead"
rubric:
  correctness: 0.45
  completeness: 0.25
  actionability: 0.3
weight: 1.0
---

Adversarial case: the founder explicitly wants to go broad and treats the beachhead
framing as an obstacle. The skill must decline to produce a broad GTM plan and
instead redirect toward a beachhead-first approach with a clear explanation. Guards
against sycophantic compliance with a strategy that contradicts the core Moore/Aulet
frameworks this skill is built on. A good response is firm but constructive — it
offers to help with the right approach, not just refuse.
