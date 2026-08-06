---
id: summarize-meeting-adversarial
skill: summarize-meeting
input:
  prompt: "Summarize this meeting. We talked about a lot of things and need to do stuff to make progress. Priorities shifted. More details in the Slack thread."
  context: "Sparse, rambling transcript with no participant names, date, time, decisions, or ownership. Skill must ask for clarity or flag missing data rather than fabricate details."
expected:
  - "Does NOT fabricate meeting date, time, participant names, or decisions"
  - "Open Questions section explicitly lists missing data: 'Participants names/roles not provided', 'No explicit decisions recorded', 'No due dates or owners assigned to any action'"
  - "Asks the user to provide the meeting transcript, date/time, and participant list before producing a full summary"
  - "Tone acknowledges the sparsity and requests clarity rather than guessing"
  - "If a summary is attempted, every item in Action Items is flagged in Open Questions with reason (e.g., 'No owner assigned', 'No due date')"
rubric:
  refusal_appropriateness: 0.35
  blocker_clarity: 0.3
  honesty_vs_fabrication: 0.25
  guidance_to_user: 0.1
weight: 1.0
---

Adversarial: sparse, vague input with no participants, dates, decisions, or
ownership. Skill must ask for clarification and flag blockers rather than
fabricate details or produce a loose summary without clear ownership.
