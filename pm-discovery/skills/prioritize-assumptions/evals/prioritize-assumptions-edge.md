---
id: prioritize-assumptions-edge
skill: prioritize-assumptions
input:
  prompt: "Rank these 3 assumptions for a consumer mobile app (habit-tracking)."
  context: |
    Assumptions:
    1. Users will open the app 5+ times per week (no confidence level given)
    2. Freemium model (conversion at 10% after 2 weeks free trial) is viable
    3. Push notifications increase engagement by 2x
    
    User note: "We have data from 50 beta users on engagement (#1), but pricing (#2) is completely unknown. #3 is from competitor benchmarks (Habitica), not our data."
expected:
  - "Scores assumption #1 low-uncertainty (beta data exists)"
  - "Scores assumption #2 high-uncertainty (no validation, go/no-go gate)"
  - "Scores assumption #3 medium-uncertainty (borrowed from competitor, not direct validation)"
  - "Identifies willingness-to-pay as high-impact (determines business model viability)"
  - "Does not ignore low-uncertainty assumptions; places them in lower-priority quadrant appropriately"
rubric:
  correctness: 0.35
  completeness: 0.25
  actionability: 0.25
  context_sensitivity: 0.15
weight: 1.0
---

Edge case: sparse assumptions, mixed evidence quality (beta data, competitor benchmarks, pure guesses). Skill should score uncertainty based on evidence provided, not assume all assumptions are equally uncertain. Guards against: ignoring context clues about data quality, treating all assumptions uniformly, or failing to identify what needs testing vs. what's already validated.
