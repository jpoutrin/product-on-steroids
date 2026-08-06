---
id: beachhead-segment-happy
skill: beachhead-segment
input:
  prompt: "Help me pick a beachhead segment for our product."
  context: |
    Product: AI-powered contract review tool for legal teams. Automatically flags
    risky clauses, suggests standard alternatives, and tracks redline history.
    Candidate segments the founders are considering: (A) in-house legal teams at
    Series-B/C SaaS companies (20-200 employees, France/Benelux), (B) mid-market
    law firms (50-200 lawyers, France), (C) procurement teams at large enterprises
    (1000+ employees). Pricing anchor: €400/seat/month. We have 3 pilot customers
    in segment A and zero in B or C.
expected:
  - "Recommends segment A (in-house legal at Series-B/C SaaS) as the beachhead and
    justifies it against at least three of the four criteria (pain, advantage,
    winnability, referral)"
  - "Notes the 3 existing pilot customers in segment A as a winnability and
    reachability signal"
  - "States the 10x advantage over the status quo (manual review or generic
    tools) specifically for this segment"
  - "Defines at least 3 measurable win criteria with numbers and time horizons"
  - "Identifies the next bowling-pin segment (e.g., law firms or segment B/C) and
    the mechanism that connects it to the beachhead"
  - "Flags at least one risk with an early-warning indicator"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy path: the founder has a clear product and three candidate segments, including
one with existing pilots. The skill should pick the strongest segment (A, supported
by traction evidence), score all three at least briefly, and produce a complete
brief with measurable win criteria and a bowling-pin next move. Guards against
picking segment A without justifying it against the others and against vague win
criteria like "strong adoption."
