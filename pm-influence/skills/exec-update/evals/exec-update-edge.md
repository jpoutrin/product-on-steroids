---
id: exec-update-edge
skill: exec-update
input:
  prompt: "Write the monthly exec update for the Onboarding Redesign project."
  context: |
    Audience: CEO and Head of Customer Success.
    Period: July 2026.
    Status: All July milestones hit. New onboarding flow is live for 100%
    of new signups. Time-to-first-value dropped from 8 days to 3.2 days.
    No risks or blockers identified.
    No asks from leadership at this time.
    Next milestone: August retention cohort analysis, target 31 Aug.
expected:
  - "BLUF is present and signals GREEN clearly given all milestones hit"
  - "Status correctly reflects the time-to-first-value improvement as a concrete metric"
  - "Key Risks section explicitly states no risks rather than being omitted or left blank"
  - "Asks section explicitly states 'No asks this period' rather than being omitted or left blank"
  - "Next Milestone names the retention cohort analysis with the 31 Aug date"
  - "Output does not fabricate risks or asks not present in the input"
  - "Body remains concise (≤ 350 words) despite the light content"
rubric:
  bluf_signal_clarity: 0.25
  graceful_empty_handling: 0.35
  completeness: 0.25
  conciseness: 0.15
weight: 1.0
---

Edge case: all milestones hit, no risks, no asks. Guards against two
failure modes: (1) the skill omitting Risks or Asks sections entirely,
which breaks template conformance; (2) the skill fabricating risks or
asks to fill the sections. The correct behavior is to include both
sections with explicit "none" language.
