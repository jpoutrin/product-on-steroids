---
id: user-personas-edge
skill: user-personas
input:
  prompt: "Create user personas for our habit-tracking mobile app."
  context: |
    We have notes from 5 user interviews conducted last week (no recording, no
    transcript — just the researcher's handwritten summary). No survey data, no
    analytics access yet. Interviewees were recruited via a Reddit post so they
    skew toward early adopters. Three mentioned wanting to track workouts, two
    mentioned managing medication schedules. No demographic data collected.
expected:
  - "Flags the thin data situation upfront (5 interviews, no demographics, convenience sample) rather than proceeding as if data were complete"
  - "Derives at most 2 personas from the limited data rather than inventing additional segments not visible in the notes"
  - "Labels every claim as low-confidence and names a concrete validation method (e.g., 'run a 50-person survey to test this split')"
  - "Does NOT invent demographic anchors not present in the data; uses 'unknown / not collected' where absent"
  - "Explicitly calls out the convenience-sample bias (Reddit early adopters) as a data quality risk"
  - "Provides actionable next steps for data collection to strengthen persona confidence"
rubric:
  data_grounding: 0.35
  gap_flagging: 0.35
  completeness: 0.20
  actionability: 0.10
weight: 1.0
---

Edge case: thin, low-quality data from a convenience sample with no demographics.
Guards against two failure modes: (1) producing confident-sounding personas from
insufficient data, and (2) refusing to proceed at all. The skill should deliver
what the data supports, flag everything uncertain, and prescribe next research
steps rather than papering over gaps.
