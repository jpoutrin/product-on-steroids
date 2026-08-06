---
id: discovery-process-edge
skill: discovery-process
scenario: >
  Continuous discovery cadence request with a vague trigger, severely constrained
  user access (enterprise, legal-gated), and an opinionated senior stakeholder
  who has already briefed the board on a solution direction.
input:
  prompt: >
    We're a PM at an enterprise legal-tech company. Our CPO wants us to "do
    discovery" on our contract-review product but hasn't given us a specific
    question — just "figure out what lawyers really need." We only have access to
    3 internal legal teams (external customers require sales approval that takes
    6+ weeks). Our CPO has also already told the board we'll launch AI-powered
    clause flagging by Q3. Can you help us plan continuous discovery that fits
    this reality?
  context: >
    Enterprise environment. Legal-gated customer access. CPO pre-committed to a
    solution. No prior research. Vague brief. Continuous cadence requested.
expected:
  - The skill surfaces the vague trigger problem and proposes a sharpened
    Discovery Goal before building the plan, or asks the user to confirm a
    drafted goal.
  - The plan explicitly acknowledges the stakeholder pre-commitment risk and
    offers a concrete mitigation (e.g., separate problem-space interviews from
    solution feedback sessions; frame early findings as "informing" not
    "blocking").
  - The plan adapts to the access constraint: proposes proxy methods (internal
    users, diary studies, session recordings, support tickets) rather than
    assuming normal external participant recruitment.
  - A continuous cadence structure is provided (e.g., weekly interview rhythm
    aligned to Teresa Torres' model) rather than a sprint-scoped plan, since
    the user requested it.
  - The plan does not simply capitulate to the CPO's solution frame — at least
    one Explore-phase activity keeps the problem space genuinely open.
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

This edge case tests three hard scenarios simultaneously: a vague discovery
brief (the skill must sharpen it rather than bulldoze through), a pre-committed
stakeholder (the canonical discovery anti-pattern), and a severely constrained
access environment (enterprise legal). A weak output ignores the CPO risk and
recommends 10 customer interviews as if they were trivially available. A strong
output reconfigures the plan around proxy access, uses the continuous cadence
the PM asked for, and provides a diplomatic framing for keeping problem space
open alongside the Q3 commitment.
