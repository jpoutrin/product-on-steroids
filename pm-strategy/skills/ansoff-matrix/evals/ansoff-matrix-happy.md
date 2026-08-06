---
id: ansoff-matrix-happy
skill: ansoff-matrix
input:
  prompt: "Build an Ansoff growth matrix for our EU SMB e-signature SaaS and recommend where to grow next."
  context: "Current product: e-signature web app. Current market: EU SMBs, English-first. Traction: 8k paying SMBs, ~15% annual churn. Team of 25, ~€4M ARR, limited capital for one big bet. Growth target: 2x ARR in 24 months."
expected:
  - "States the current product and current market explicitly before mapping quadrants"
  - "Renders a 2x2 matrix labeling all four quadrants (penetration, market development, product development, diversification)"
  - "Gives 2-3 concrete, product-specific growth options for each of the four quadrants (not a generic checklist)"
  - "Assigns an explicit risk level per quadrant with penetration lowest and diversification highest, each with a one-line rationale"
  - "Recommends a sequenced 1-2-3 growth path with an advance trigger per step, tied to the stated team/capital constraints"
  - "Warns against pursuing all four quadrants simultaneously"
  - "Numbers key assumptions with confidence levels and validation steps"
rubric:
  correctness: 0.30
  completeness: 0.25
  sequencing_quality: 0.25
  actionability: 0.20
weight: 1.0
---

Happy path: a well-anchored product with real traction and stated constraints,
enough to fill all four quadrants and defend a sequence. Guards against generic
option lists, flat (undifferentiated) risk, and a missing growth path.
