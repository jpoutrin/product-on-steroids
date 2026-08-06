---
id: value-prop-statements-edge
skill: value-prop-statements
input:
  prompt: "I need value propositions for our B2B API platform. We help engineers integrate payment processing. What should we say?"
  context: "No explicit segments named. Only one persona implied: engineers. No alternatives or proof points provided. Limited feature information."
expected:
  - "Does NOT assume segments — actively asks or proposes 2–3 distinct segments (not just 'engineers'). For example: startup founders vs. enterprise architects vs. DevOps teams, each with different concerns"
  - "For each segment, articulates a distinct outcome and alternative. Startup founders might compare against manual payment handling; enterprise architects might compare against other payment APIs"
  - "Identifies and uses features from the API context (fast integration, low latency, scalable, good documentation) and maps them to segment-specific benefits"
  - "Includes a caveat or asks for proof points (latency benchmarks, integration time, cost savings) if the user hasn't provided them, rather than inventing metrics"
  - "Produces at least 2–3 value propositions reflecting the distinct segments proposed or elicited"
rubric:
  segment_elicitation: 0.35
  alternative_articulation: 0.25
  feature_inference: 0.20
  appropriately_cautious: 0.20
weight: 1.0
---

Edge case: sparse inputs (single implied persona, no explicit alternatives or metrics).
Guards against over-generalizing to one segment and ensures the skill elicits or proposes
segments actively rather than defaulting to a catch-all persona.

