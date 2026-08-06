---
id: lean-canvas-happy
skill: lean-canvas
input:
  prompt: "Draft a Lean Canvas for a tool that helps solo B2B freelancers get paid on time."
  context: "Early-stage, pre-launch. Segment: EU freelance designers billing >€3k/mo. Problem believed: chasing late invoices wastes ~4 hrs/week."
expected:
  - "Fills all nine Lean Canvas blocks (Problem, Customer Segments, UVP, Solution, Channels, Revenue Streams, Cost Structure, Key Metrics, Unfair Advantage)"
  - "Problem block lists concrete problems AND the existing alternatives freelancers use today (manual reminders, spreadsheets, generic tools)"
  - "Customer Segments separately calls out early adopters distinct from the broad segment"
  - "UVP is a single differentiated line, not a generic superlative"
  - "Solution is a thin feature set of roughly one feature per top problem"
  - "Includes a ranked list of 3-5 riskiest assumptions, each paired with a cheap validation experiment and a success threshold"
rubric:
  correctness: 0.35
  completeness: 0.30
  assumptions_and_risk: 0.20
  actionability: 0.15
weight: 1.0
---

Happy path: a concrete early-stage B2B idea with a clear segment and problem
hypothesis. Guards against skipping blocks, omitting existing alternatives or
early adopters, and failing to rank riskiest assumptions with cheap tests.
