---
id: escalation-happy
skill: escalation
input:
  prompt: "Write an escalation memo for me. Our Q3 mobile checkout feature is blocked because the Payments team hasn't approved our API spec. I've emailed twice (June 3 and June 10) and requested a review in last week's sync — no response. Without their sign-off by June 17, we miss our July 1 beta launch, which is committed to our top 3 enterprise customers. I need VP Engineering (Sarah Chen) to instruct the Payments team to respond within 48 hours."
  context: "The PM has three prior attempts documented. The consequence is a committed beta date with named enterprise customers. The ask is specific: VP Eng instructs Payments team to respond within 48 hours. Deadline June 17."
expected:
  - "Subject line begins with 'Escalation:' and names the blocker in one sentence"
  - "Situation section is four sentences or fewer and states how long the issue has been stuck (since June 3)"
  - "What Has Been Tried lists all three prior attempts with dates (June 3, June 10, and the weekly sync) and their outcomes"
  - "What Is Needed is a single crisp ask: VP Eng instructs Payments team to respond within 48 hours"
  - "Consequence is concrete: July 1 beta miss and named enterprise customer commitments at risk"
  - "Deadline is June 17 with a rationale (July 1 beta requires sign-off by June 17)"
  - "Tone is collaborative and direct — no blame language toward the Payments team"
  - "Memo is half a page or fewer"
rubric:
  structure_completeness: 0.30
  ask_specificity: 0.25
  consequence_concreteness: 0.25
  tone_calibration: 0.20
weight: 1.0
---

Happy path: a well-specified escalation with three documented prior attempts, a
specific ask, a concrete deadline tied to a real customer commitment, and a
clear recipient. Guards against verbose memos that bury the ask, blame language
toward the blocked party, and missing the deadline rationale.
