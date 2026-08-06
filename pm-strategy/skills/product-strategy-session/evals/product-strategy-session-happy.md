---
id: product-strategy-session-happy
skill: product-strategy-session
input:
  prompt: "I'm facilitating a half-day (3.5-hour) product strategy offsite next week. We need to decide between two growth motions: doubling down on our sales-led enterprise motion vs. launching a self-serve SMB tier. Eight people: our VP Product (the decision owner), two PMs, eng lead, design lead, head of sales, head of marketing, and a data analyst. Give me a run-of-show and the readout structure."
  context: "Decision, Decider (VP Product), participants/roles, and timebox are all provided. A prior market-sizing memo and a draft product-strategy-canvas exist as pre-reads."
expected:
  - "Produces a Session Frame naming the exact decision, the VP Product as Decider, participant roles (decide/advise/input), and the 3.5-hour timebox"
  - "Gives a timeboxed agenda whose durations sum to ~3.5 hours, each stage carrying a facilitation technique and specific question(s), arced context -> diverge -> converge -> decide -> commit"
  - "Includes a convergence plan with a concrete closing mechanism per divergent stage and a stall/escalation path"
  - "Provides a readout structure where each decision names an accepted trade-off and every next step has a named owner and due date"
  - "Treats the existing product-strategy-canvas as a pre-read/output, not something the session itself authors"
rubric:
  correctness: 0.35
  completeness: 0.3
  actionability: 0.35
weight: 1.0
---

Happy path: a fully-specified session with a clear binary decision, a named Decider, defined roles, and a fixed timebox. Guards that the skill produces a complete, timeboxed, technique-attached run-of-show plus a decisions/open-questions/next-steps readout, and that it stays a facilitation pack rather than drifting into authoring the strategy canvas.
