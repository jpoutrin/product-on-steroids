---
id: user-story-splitting-edge
skill: user-story-splitting
input:
  prompt: "Split this story: As a finance manager I want to export transaction reports so that I can reconcile accounts."
  context: "B2B SaaS. Story is estimated at 18 points. Supported export formats: CSV (simple), Excel with pivot tables, and PDF with branding. All three formats are requested by different customer segments and all must ship. The workflow to export is a single click — there is no multi-step process to split on."
expected:
  - "Recognizes that a workflow-step (Path) split is a poor fit because the export action is a single step — not a multi-phase flow"
  - "Selects a Data or Interface split (by output format/complexity tier: CSV vs Excel vs PDF) as the primary pattern instead"
  - "Justifies why the chosen pattern fits better than workflow-step in this context"
  - "Each child story (one per format or logical grouping) is independently deliverable and valuable"
  - "Acceptance criteria for each child are format-specific and testable"
  - "Includes a Quality Check table verifying INVEST for each child"
rubric:
  pattern_selection: 0.35
  correctness: 0.30
  invest_compliance: 0.20
  completeness: 0.15
weight: 1.0
---

Edge case: the obvious first-instinct split pattern (workflow/Path) does not fit
because the user action is a single click. The skill must recognize this and pivot
to a data-variation or interface split by format complexity tier. Guards against
mechanically applying workflow-step splits when the story does not have a
sequential user flow.
