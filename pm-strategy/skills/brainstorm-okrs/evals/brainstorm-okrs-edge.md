---
id: brainstorm-okrs-edge
skill: brainstorm-okrs
input:
  prompt: "Draft OKRs for the mobile team."
  context: "We want the app to do better. No analytics instrumented yet; no baselines. No stated company objective."
expected:
  - "Elicits the missing company objective / North Star before drafting rather than inventing one"
  - "Still produces three distinct outcome-based OKR sets once an anchor is assumed or requested"
  - "Flags every Key Result target as an assumption because no baseline exists"
  - "Adds data-availability notes for metrics not currently instrumented"
  - "Does not fabricate baseline numbers or present unsupported targets as fact"
rubric:
  correctness: 0.30
  assumptions_explicit: 0.30
  alignment: 0.25
  actionability: 0.15
weight: 1.0
---

Edge: vague goal and zero baselines/instrumentation. Guards against inventing a
company objective, fabricating baselines, and stating targets as fact when they
are unvalidated assumptions.
