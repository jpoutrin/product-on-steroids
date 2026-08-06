---
id: stakeholder-engagement-advisor-adversarial
skill: stakeholder-engagement-advisor
input:
  prompt: "Give me a generic stakeholder engagement template I can reuse across all projects."
  context: "No initiative, no stakeholder list, and no stance or influence information provided."
expected:
  - "Does NOT return a generic, fill-in-the-blank engagement template"
  - "Explains why a generic template is not useful: engagement tactics must be grounded in each stakeholder's actual motivations and stance"
  - "Asks for the minimum required inputs: a brief initiative description and at least a rough stakeholder list with influence and stance"
  - "If the user insists on a generic output, produces at most a lightweight illustrative example while clearly labeling it as a placeholder that must be personalized"
  - "Does not lecture the user at length — one clear, actionable ask for the missing inputs is sufficient"
rubric:
  scoping_discipline: 0.40
  correctness: 0.25
  assumptions_explicit: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: a request for a reusable generic template with no initiative context
or stakeholder data. Guards against the most common failure mode — producing a
generic stakeholder communication grid that looks complete but provides no
actionable guidance for any real situation.
