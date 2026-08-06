---
id: retro-happy
skill: retro
input:
  prompt: "Facilitate a retrospective for Sprint 42, which ended Aug 20. We committed to 45 story points and completed 42. Goal was 'stabilize the API'; we achieved it."
  context: "Team of 5 (2 backend, 2 frontend, 1 QA). Async survey results provided covering what went well (strong pair programming, good async docs), what didn't (time-zone sync was hard, acceptance criteria unclear before dev), and what to keep (daily standups). Previous sprint's action: 'schedule weekly sync' — completed and working."
expected:
  - "Reports sprint goal outcome clearly (achieved, partial, or missed) with velocity data (committed vs completed points)"
  - "Organizes feedback into 3–5 distinct themes (not a flat list of comments)"
  - "Generates 2–3 action items with specific owners, realistic deadlines within 1–2 sprints, and measurable success metrics"
  - "Tracks carry-over from last sprint, showing completion status of prior action items"
  - "Tone is constructive and systems-focused, not blame-seeking"
  - "Avoids vague improvements ('communicate better') in favor of concrete steps ('Friday 3pm sync for US/EU overlap')"
rubric:
  correctness: 0.35
  completeness: 0.25
  actionability: 0.25
  tone: 0.15
weight: 1.0
---

Happy path: strong data (velocity, clear feedback, prior action tracking), straightforward synthesis into themes, and actionable next steps with owners. Guards against low-signal retros (vague, blame-focused, or missing action items).
