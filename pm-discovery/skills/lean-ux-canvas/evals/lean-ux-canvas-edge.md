---
id: lean-ux-canvas-edge
skill: lean-ux-canvas
input:
  prompt: >
    I'm a solo backend engineer and I want to build a feature that lets users
    export reports as PDF. Can you help me fill in the Lean UX Canvas? I'm
    working alone and haven't talked to any users or stakeholders yet.
  context: >
    Solo engineer, no user research, no business-outcome data, no stakeholder
    input. The stated request is solution-first ("build PDF export"), not
    problem-first.
expected:
  - The skill reframes Block 1 around the underlying business problem (why PDF export might matter), not the feature itself
  - The skill flags explicitly that the canvas is best filled collaboratively and that some blocks contain assumptions that must be validated with stakeholders or users
  - Block 3 proposes plausible user types as assumptions (not stated as facts) and invites the user to confirm or correct them
  - Block 6 hypotheses are clearly marked as unvalidated starting-point assumptions, not established facts
  - Block 7 highlights that the riskiest assumption is whether PDF export actually solves a real user problem (discovery risk)
  - Block 8 recommends a lightweight discovery experiment (e.g., 3 user interviews) before any engineering work, given the solo / no-research context
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge scenario: a solo engineer with no stakeholder alignment, no user research,
and a solution-first framing. Guards against the skill blindly accepting the
feature request and producing a canvas that looks complete but is built entirely
on unvalidated assumptions. The skill should still produce a full canvas (don't
refuse), but must surface the discovery risks explicitly and steer toward
lightweight validation before building.
