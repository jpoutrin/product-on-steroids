---
id: epic-hypothesis-edge
skill: epic-hypothesis
input:
  prompt: "Help us write an epic hypothesis for a mobile offline mode."
  context: "Consumer mobile app (expense tracking). No current metric for the problem: we don't know how many users actually experience connectivity issues, and we have no baseline for any relevant metric. The team suspects offline usage is important because support tickets mention it. No OKR tied to this yet."
expected:
  - "Does NOT refuse to produce a hypothesis because baselines are missing"
  - "Flags that the baseline is 'unknown' in the success criteria table, rather than inventing a number"
  - "Proposes the most direct metric for offline mode value (e.g., sessions completed while offline, expense entries submitted post-reconnect) and explains why"
  - "Rates baseline-dependent assumptions as low confidence and names concrete validation steps (e.g., instrument offline session events before building)"
  - "Notes in open questions that the OKR connection is unresolved and prompts the team to anchor the epic to a business outcome"
  - "Produces a grammatically complete canonical statement even with unknowns — using estimated or directional targets clearly labeled as assumptions"
rubric:
  correctness: 0.35
  completeness: 0.25
  assumptions_explicit: 0.30
  actionability: 0.10
weight: 1.0
---

Edge case: no baseline data and no OKR. Guards against refusing to produce a
hypothesis (unhelpful) and against inventing baselines without flagging them
(misleading). The skill must navigate uncertainty honestly while still delivering
a usable artifact.
