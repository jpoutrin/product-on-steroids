---
id: summarize-interview-edge
skill: summarize-interview
input:
  prompt: "Summarize this customer interview for our project management tool discovery."
  context: |
    Transcript excerpt (sparse — interviewer notes only, no full dialogue):
    "Spoke with someone from a mid-size agency. Didn't catch their name.
    They use Trello. Main complaint: no time-tracking built in. Everything else
    seems okay. No clear asks for follow-up."
expected:
  - "Header uses '-' for participant name and company rather than inventing them"
  - "Current Solution identifies Trello"
  - "Problems section captures the missing time-tracking pain even though satisfaction level was not stated explicitly — uses 'frustrated' or notes the signal is inferred"
  - "Key Insights flags the sparse metadata as a research quality risk or notes the lack of JTBD depth"
  - "Action Items section is either empty or contains only a single inferred follow-up; no invented next steps"
  - "Summary does not fabricate any participant details, importance ratings, or quotes not present in the notes"
rubric:
  accuracy: "'-' used for genuinely unknown fields; no detail invented"
  completeness: "All six template sections present even when some are minimal"
  sparse_handling: "Skill gracefully handles missing metadata and shallow signals without hallucinating"
  actionability: "Does not create fictitious action items to fill the section"
weight: 1.0
---

Edge case: sparse interviewer notes with missing participant metadata, no verbatim
quotes, and no explicit action items. Guards against hallucination of names, roles,
satisfaction levels, and follow-ups when the source material is thin. The skill
must use '-' and flag the limitation rather than invent content to fill the template.
