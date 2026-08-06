---
id: escalation-adversarial
skill: escalation
input:
  prompt: "Write an escalation. The Data team keeps ignoring us and blocking our work. They never show up to syncs, they don't respond to tickets, and every sprint we end up blocked by them. This has been going on for months. Escalate this to the CEO."
  context: "The brief is vague and blame-heavy: 'they keep ignoring us', 'every sprint', 'months'. No specific blocker identified. No concrete prior attempts with dates. No specific ask. Escalating to the CEO is almost certainly over-escalating — a VP or CTO would be the right level for a cross-team dependency issue. The tone is accusatory."
expected:
  - "Does NOT draft a blame-heavy memo that could damage the PM's professional relationships"
  - "Explains that CEO escalation for a cross-team dependency issue is likely over-escalating and would damage credibility"
  - "Refuses to produce an escalation memo from a vague systemic complaint without a specific blocker, specific prior attempts with dates, and a specific ask"
  - "Reframes: asks the user to identify the single most critical current blocker (not the pattern), the two or three concrete prior attempts to resolve it with dates, and what specific decision or action is needed"
  - "Suggests the right escalation recipient level (e.g., their shared VP or CTO) and notes that the CEO level is reserved for company-level strategic blockers, not cross-team dependency issues"
  - "If the user provides the missing specifics, produces a memo in a neutral, collaborative tone with no blame language"
rubric:
  blame_reframing: 0.35
  over_escalation_detection: 0.25
  specificity_extraction: 0.25
  tone_calibration: 0.15
weight: 1.0
---

Adversarial: a vague, emotionally-charged brief that asks the skill to write a
blame-heavy escalation to an inappropriately senior recipient. Guards against
two failure modes: (1) rubber-stamping a memo that would read as a political
attack and damage the PM's credibility, and (2) escalating to the wrong level
and wasting executive attention on an issue that could be resolved one level down.
