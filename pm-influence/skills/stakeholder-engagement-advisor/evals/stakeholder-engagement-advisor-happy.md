---
id: stakeholder-engagement-advisor-happy
skill: stakeholder-engagement-advisor
input:
  prompt: "Build a stakeholder engagement plan for our checkout redesign initiative."
  context: |
    Initiative: redesign the checkout flow to reduce cart abandonment by 20%.
    Timeline: 10 weeks to executive sign-off and engineering kick-off.
    Stakeholders:
    - Sarah Kim, VP Product (sponsor, high influence, supporter)
    - Tom Reyes, VP Engineering (high influence, neutral — worried about sprint capacity)
    - Dana Park, Head of UX (medium influence, supporter — already on the design)
    - Marcus Webb, CFO (high influence, neutral — wants ROI evidence before approving budget)
    - Priya Nair, Customer Success Lead (medium influence, blocker — fears increased support tickets)
expected:
  - "Produces a Stakeholder Roster table with all five stakeholders, their influence, stance, and priority"
  - "Engagement Playbook addresses each stakeholder individually with a named channel, frequency, and motivation-grounded message framing"
  - "Sequencing Map places Sarah Kim (champion) before Marcus Webb (neutral governor) and explains why"
  - "Priya Nair's blocker stance is addressed with a root-cause hypothesis and a concrete de-escalation tactic"
  - "Cadence Snapshot covers at least 4 weeks and shows planned touchpoints for each stakeholder"
  - "Success Indicators are specific and observable, not generic"
rubric:
  correctness: 0.35
  completeness: 0.25
  motivation_grounding: 0.25
  actionability: 0.15
weight: 1.0
---

Happy path: a realistic B2B product initiative with a mixed stakeholder set —
two champions, two neutrals, one blocker — and enough context to produce a
fully populated plan. Guards against generic advice and channel-less playbooks.
