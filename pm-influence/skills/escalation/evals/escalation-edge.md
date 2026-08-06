---
id: escalation-edge
skill: escalation
input:
  prompt: "I need to escalate. Legal hasn't reviewed our privacy policy update and we're supposed to launch next month. I sent them a Slack message last week and they haven't replied. Can you write an escalation to my CPO?"
  context: "Only one prior attempt (a Slack message last week). No specific launch date stated beyond 'next month'. No consequence named. No prior formal meeting or written request. CPO is the proposed recipient — possibly over-escalating."
expected:
  - "Does NOT immediately draft a full escalation memo from this thin brief"
  - "Flags that only one prior attempt (a Slack message) is insufficient evidence that normal channels have failed"
  - "Asks the user to try at minimum one more formal channel before escalating (e.g., a calendar request, an email to Legal's manager, a structured written request)"
  - "If the user confirms genuine urgency that overrides the normal sequence, explains what information is still needed: specific launch date, concrete consequence if Legal misses the review, and whether CPO is the right level or Legal's direct manager would suffice"
  - "If ultimately asked to draft despite the gaps, produces a memo that clearly labels missing information as assumptions and suggests the user verify them"
rubric:
  premature_escalation_detection: 0.35
  appropriate_pushback: 0.30
  escalation_calibration: 0.20
  actionability: 0.15
weight: 1.0
---

Edge case: the escalation is premature — only one informal prior attempt exists,
no concrete consequence is named, and the recipient level may be too high. Guards
against the skill rubber-stamping every escalation request without checking
whether normal channels have genuinely been exhausted, which would erode the
PM's credibility with leadership over time.
