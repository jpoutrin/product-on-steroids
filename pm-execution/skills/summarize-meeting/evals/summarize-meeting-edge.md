---
id: summarize-meeting-edge
skill: summarize-meeting
input:
  prompt: "Summarize this strategy meeting: We debated whether to pivot to enterprise or stay consumer. Sarah argues enterprise has higher CAC but better retention; Tom thinks consumer is faster to revenue but saturated. No decision was made. We'll revisit next week with competitive data. Also discussed: customer churn is up 5%, but unclear if it's seasonal or product-related. Engineering thinks it's support load; Sales thinks it's feature gap. We need more data."
  context: "Meeting held 2024-06-01, 14:00-15:15. Participants: Sarah (PM), Tom (Engineering Lead), Alex (Sales). Conflicting viewpoints, deferred decision, open questions."
expected:
  - "Reports meeting date, time, and participant names with roles"
  - "Topic is clear but captures the tension (e.g., 'Enterprise vs. Consumer Pivot Discussion')"
  - "Summary surfaces the two competing viewpoints without resolving them"
  - "Decisions Made section is present; if no decision was made, states 'No decision made this meeting' or lists the deferred decision with revisit date"
  - "Action Items table includes: revisit pivot decision with competitive data (owner, date); identify churn root cause (ownership or flagged as blocker in Open Questions)"
  - "Open Questions clearly lists the unresolved churn cause and notes the need for data before re-deciding"
  - "Tone remains objective and collaborative even when capturing disagreement"
rubric:
  tension_capture: 0.35
  deferred_clarity: 0.3
  blocker_flagging: 0.2
  structure_consistency: 0.15
weight: 1.0
---

Edge case: meeting with competing viewpoints, deferred decisions, and unresolved
blockers. Guards against false consensus and ensures skill surfaces tensions and
open questions rather than papering over them.
