---
id: acquisition-channel-advisor-happy
skill: acquisition-channel-advisor
input:
  prompt: "We're a two-person B2B SaaS team building a contract-review tool for in-house legal teams at mid-market companies (50–500 employees). We have $0 acquisition budget — completely bootstrapped. We're pre-PMF; we've had 5 pilot customers through warm intros but no repeatable channel yet. Our ICP is the Head of Legal or General Counsel at a 100–400 person company in the US. Help us figure out which acquisition channels to focus on."
  context: "No paid budget. Founder-led sales only. US market. No existing content or SEO footprint. LinkedIn profile exists but unused for outreach."
expected:
  - "At least 8 of the Traction 19 channels are considered and either included in the scoring table or explicitly eliminated with a one-line reason"
  - "Paid channels (SEM, Facebook Ads, etc.) are flagged as budget-incompatible and either excluded or marked as future/post-funding"
  - "The Top 3 recommendation focuses on zero/low-cost channels appropriate for pre-PMF B2B — e.g., cold outbound, community/niche events, content/SEO, or strategic partnerships"
  - "The Test Protocol for Channel 1 includes a falsifiable hypothesis, a specific leading metric, a $0 or near-$0 budget line, a success threshold, and a named failure signal"
  - "ICP Fit scores are justified by reference to Head of Legal / GC persona — not generic B2B reasoning"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy-path scenario: a bootstrapped pre-PMF B2B SaaS team with a clearly defined ICP
but no budget. Guards against the skill recommending paid channels when budget is zero,
and verifies that the output is actionable for a founder doing everything themselves.
The scenario also checks that the ICP (Head of Legal at mid-market) meaningfully shapes
the ICP Fit column — not a one-size-fits-all answer.
