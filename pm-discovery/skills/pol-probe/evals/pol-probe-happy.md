---
id: pol-probe-happy
skill: pol-probe
input:
  prompt: >
    I'm launching a cross-functional internal data platform initiative at
    Acme Corp. The goal is to consolidate four siloed data warehouses into one
    shared platform so product, sales, and finance teams can self-serve
    analytics. I need engineering, sales ops, and finance to align by end of Q3
    or we miss the annual planning window. Help me run a POL probe so I can
    prepare my stakeholder engagement.
  context: >
    PM is senior at Acme Corp (Series C, 600 people). Known stakeholders:
    CTO (Ana Ruiz) is supportive of infra consolidation; VP Sales (Ben Park)
    worries about engineering capacity being pulled from pipeline features; CFO
    (Dana Cho) controls the budget for tooling; Data Engineering Lead (Carla
    Menz) has championed a unified platform internally for 18 months.
    Engineering is in a quarterly planning cycle; next sprint kick-off is in 3
    weeks. No regulatory constraints known.
expected:
  - Political Map names at least Ana Ruiz, Ben Park, Dana Cho, and Carla Menz
    with individual power levels and stances
  - Ben Park is identified as Skeptic or Blocker with a rationale tied to
    engineering capacity, not a generic "may resist" note
  - Organizational Levers names Dana Cho as budget owner and the Q3 annual
    planning window as the critical decision gate
  - Risk Register includes a risk specifically about engineering capacity
    perception by Sales, with a concrete mitigation
  - Engagement Strategy sequences Carla Menz or Ana Ruiz before Ben Park,
    with a rationale about building visible air cover first
  - No element is labeled Low confidence given the rich context provided
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy path: PM has rich org context and a concrete initiative. Guards against
two failure modes — (1) producing a generic stakeholder list without meaningful
power/stance differentiation, and (2) a vague engagement strategy that says
"build buy-in" without sequencing logic anchored to the Political Map.

The scenario deliberately includes a sympathetic champion (Carla Menz) who has
organizational credibility, and a high-power skeptic (Ben Park) whose concern
is legitimate. A good brief must acknowledge Ben's concern as a real risk rather
than dismissing it, while showing how to use Carla and Ana as coalition anchors
before the group conversation.
