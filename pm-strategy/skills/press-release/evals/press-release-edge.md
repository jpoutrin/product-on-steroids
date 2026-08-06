---
id: press-release-edge
skill: press-release
input:
  prompt: "Draft a Working Backwards PR/FAQ for an idea I'm still shaping: a browser extension that summarizes long Slack threads for busy managers. I don't have pricing, a launch date, or a name yet."
  context: "Early-stage idea. Customer: managers on teams with heavy Slack usage who miss context. No pricing model, availability, or product name decided."
expected:
  - "Still produces a full release plus both FAQ sections despite missing details"
  - "Uses clearly labeled [placeholder] / [assumption] values for the missing name, price, launch date, and availability rather than fabricating them as fact"
  - "Keeps the release future-dated, customer-framed, and hype-free at roughly one page"
  - "Internal FAQ flags the biggest risk and calls out how customer demand would be validated"
  - "Go / refine / no-go read acknowledges the idea is thin and names the top unknown to test first"
rubric:
  correctness: 0.3
  completeness: 0.25
  assumptions_explicit: 0.3
  actionability: 0.15
weight: 1.0
---

Edge: a thin, early idea with several unknowns. Guards against the skill either
refusing to draft or, worse, inventing pricing/dates/names as if they were decided
instead of marking them as assumptions to confirm.
