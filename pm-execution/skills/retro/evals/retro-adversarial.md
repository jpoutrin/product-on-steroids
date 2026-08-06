---
id: retro-adversarial
skill: retro
input:
  prompt: "Sprint 40 was a disaster. We committed 60 points, finished 18. Key person quit mid-sprint. Database crashed during launch. Team morale is low. Do a retro."
  context: "Emotional, high-stakes situation. Team is demoralized and likely to blame individuals (the person who quit, the on-call engineer). No structured feedback; you have raw sentiment. High risk of retro reinforcing blame instead of driving systems improvement. Previous sprint's action: 'hire more QA' — not completed."
expected:
  - "Reframes high-emotion, blame-prone feedback into systems-focused themes (e.g., 'understaffing + lack of oncall rotation' not 'person X failed')"
  - "Surfaces structural root causes without ignoring individual frustration (e.g., 'database scaling not tested; oncall unprepared for incident')"
  - "Generates 2–3 action items that address systemic gaps, not individual blame (e.g., 'load-testing protocol before launch', 'oncall runbook for DB issues', 'staffing review')"
  - "Acknowledges the tough sprint constructively without dismissing frustration, and steers toward recovery"
  - "Prioritizes immediate stabilization actions (oncall, monitoring) over nice-to-haves"
rubric:
  systems_focus: 0.35
  root_cause_depth: 0.25
  tone_management: 0.25
  recovery_urgency: 0.15
weight: 1.0
---

Adversarial case: high-emotion, blame-prone sprint with personnel and infrastructure crises, low morale, and incomplete prior actions. Skill must surface root causes without personalizing blame, reframe toward systems improvement, and maintain constructive forward momentum despite justified frustration.
