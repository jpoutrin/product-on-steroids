---
id: summarize-meeting-happy
skill: summarize-meeting
input:
  prompt: "Summarize this product planning meeting: We discussed shipping the new dashboard feature, deferred the mobile redesign to Q3 (budget constraints), and assigned Sarah to run a competitive analysis by June 15. Tom (Engineering Lead) will prototype the dashboard by June 8. We also flagged a blocker: API rate limits need engineering review—Dave to investigate by June 10."
  context: "Meeting held 2024-06-01, 10:00-10:45. Participants: Sarah (PM), Tom (Engineering Lead), Dave (Backend Engineer), Maya (Designer). Clear decisions and ownership assigned."
expected:
  - "Reports meeting date, time range, and all four participant names with roles"
  - "Topic is a short, clear title (not a list of decisions)"
  - "Captures 3–5 key points in plain language (no jargon)"
  - "Lists at least two decisions explicitly with ownership"
  - "Action Items table has three columns (Due Date, Owner, Action); every row has both owner and date"
  - "Sorts action items by due date"
  - "Open Questions section is present and lists the API rate limit blocker"
  - "Tone is objective and uses 'we' language"
rubric:
  ownership_clarity: 0.35
  completeness: 0.3
  actionability: 0.2
  tone_and_structure: 0.15
weight: 1.0
---

Happy path: clear transcript with explicit decisions, action items, and owners.
Guards against vague or unstructured summaries and ensures every action item
has a date and owner.
