---
id: problem-framing-canvas-happy
skill: problem-framing-canvas
input:
  prompt: >
    We're kicking off a sprint on mobile checkout abandonment. Here's what we
    know: 34% of mobile sessions drop at the address step (analytics, Q1 2025,
    45k sessions). Support tickets for "can't complete order on phone" are 210/
    month (Zendesk, Feb–Apr 2025), up 40% YoY. In usability sessions, users
    said the on-screen keyboard covers the address field. Most users switch to
    desktop to finish. Can you produce a Problem Framing Canvas so the team
    is aligned before we start designing?
  context: >
    B2C e-commerce platform, mobile web (not app). Team of 6: 1 PM, 2 engineers,
    1 designer, 1 QA, 1 data analyst. Two-week sprint. No budget constraint.
expected:
  - All nine canvas blocks (Problem, Who Is Affected, Context, Evidence, Current Workarounds, Business Impact, Success Metrics, Constraints, Open Questions) are present and substantively filled.
  - Evidence block cites both the 34% abandonment stat and the 210 tickets/month figure with sources and dates.
  - Current Workarounds lists the desktop switch-over as a confirmed workaround (observed in usability sessions).
  - Success Metrics express outcome-based measures (e.g., mobile checkout completion rate) — not feature descriptions.
  - The Problem block describes a symptom, not a solution (does not say "redesign the address field").
  - Open Questions each have a suggested research activity.
rubric:
  correctness: 0.4
  completeness: 0.35
  actionability: 0.25
weight: 1.0
---

Happy-path guard. Validates that the skill correctly populates a well-evidenced
canvas when the team provides good research input. Ensures evidence is cited
with sources, workarounds are surfaced from the provided usability data, and
success metrics are outcome-oriented rather than solution-descriptive. Prevents
the skill from producing a vague or incomplete canvas when solid inputs exist.
