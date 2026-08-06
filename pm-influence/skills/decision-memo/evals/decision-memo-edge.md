---
id: decision-memo-edge
skill: decision-memo
input:
  prompt: "I need a decision memo for the leadership team — we have to decide by end of day today whether to delay the v2 launch by 2 weeks or ship with the known accessibility issues."
  context: >
    The v2 launch is tomorrow. QA flagged 4 WCAG 2.1 AA failures this morning
    affecting screen-reader users. Legal has not assessed litigation risk. The
    engineering estimate for the fix is 10–12 days. There is no single decision
    owner — the call will be made jointly by the CPO (Maria Fonseca) and the CTO
    (David Kim). We have no data on what percentage of our users rely on assistive
    technology; our last accessibility audit was 18 months ago.
expected:
  - "Acknowledges the joint decision ownership (Maria Fonseca and David Kim) and does not invent a single owner"
  - "Presents both options (ship now vs. delay) with their specific benefits and costs, including the legal risk gap"
  - "Explicitly flags that the percentage of AT-dependent users is unknown and names this as a key missing data point"
  - "Does not fabricate a litigation-risk estimate or an AT-user percentage; labels those as gaps"
  - "Still makes a recommendation despite the missing data, or explicitly states what information would be needed to make one"
  - "Sets the response deadline as end of day (same day) and names the consequence of missing it"
  - "Keeps the memo to approximately one page given the urgency"
rubric:
  correctness: 0.30
  assumptions_explicit: 0.35
  actionability: 0.25
  completeness: 0.10
weight: 1.0
---

Edge case: a group decision owner, extreme time pressure (same-day deadline), and
critical missing data (AT-user percentage, legal risk). Guards against fabricating
numbers under pressure, inventing a single owner when authority is shared, and
refusing to produce a memo because the data is incomplete. The skill must flag
gaps honestly while still being useful.
