---
id: incoming-request-advisor-happy
skill: incoming-request-advisor
input:
  prompt: "My head of sales just asked me to add a bulk CSV export feature before
    the end of this quarter. He says two enterprise prospects are blocking on it.
    We're four weeks from our Q3 mobile performance milestone. What should I do?"
  context: "Current strategy: double down on mobile retention before adding
    enterprise features. The sales lead is a respected peer, no prior friction.
    Team has no slack capacity this quarter."
expected:
  - "Names an explicit disposition — Defer is appropriate given the capacity conflict"
  - "Strategic rationale references the Q3 mobile milestone and capacity constraint"
  - "Draft reply opens with acknowledgement of the sales team's pressure before stating the decision"
  - "Draft reply names a specific next step (e.g., Q4 planning session, follow-up meeting date)"
  - "Bridge-Preservation Notes include at least one specific action (e.g., log the prospect names, loop into Q4 planning)"
  - "Tone is peer-level and collegial, not bureaucratic"
rubric:
  correctness: 0.35
  completeness: 0.25
  tone_and_empathy: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: enough context to produce a clear Defer disposition, a well-grounded
strategic rationale, and a warm peer-level draft reply. Guards against dispositions
that capitulate without rationale or replies that are technically correct but
relationship-damaging.
