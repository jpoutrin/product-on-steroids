---
id: retro-edge
skill: retro
input:
  prompt: "Run a retro for Sprint 41. We committed 50 points, completed 28. Goal was 'ship checkout flow' but we got stuck on payment integration."
  context: "Team feedback is mixed and sparse: 'blockers were rough', 'pair programming helped', 'we need better planning', 'payment API docs were terrible'. No velocity history provided. No prior action items to track. Conflicting sentiment: some team members frustrated, others optimistic about progress."
expected:
  - "Synthesizes sparse/conflicting feedback into coherent themes despite missing data (e.g., infers root cause 'external dependency uncertainty' from payment API blocker)"
  - "Asks clarifying questions or makes reasonable assumptions explicit (e.g., 'Assuming the payment API docs are from the vendor, not ours—validate this')"
  - "Generates action items that address root causes, not just symptoms (e.g., instead of 'better planning', suggests 'pre-identify external dependencies in backlog refinement')"
  - "Maintains constructive framing of a tough sprint (systems-focused; acknowledges frustration without blame)"
  - "Prioritizes actions within realistic scope for a 2-week sprint"
rubric:
  synthesis: 0.35
  assumption_clarity: 0.25
  actionability: 0.25
  tone: 0.15
weight: 1.0
---

Edge case: sparse, conflicting feedback; missing context (velocity history, prior actions); external blockers dominating the sprint. Skill must synthesize signal from noise, clarify what's missing, and surface root causes without data to hide behind.
