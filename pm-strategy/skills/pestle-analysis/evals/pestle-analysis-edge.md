---
id: pestle-analysis-edge
skill: pestle-analysis
input:
  prompt: "Do a PESTLE analysis for our fintech app."
  context: "No geography or sub-sector given. Consumer fintech, but neither the target market nor the regulatory regime is specified."
expected:
  - "Elicits the missing required inputs (target market/geography and sector/sub-sector) before producing a full scan"
  - "Explains that PESTLE factors are geography- and sector-dependent and cannot be rated without them"
  - "If it proceeds on stated assumptions, labels the chosen geography/sector as an assumption and flags affected factors as low-confidence"
  - "Still delivers ratings and 'so what' implications rather than a bare factor list once scope is fixed"
  - "Numbers its assumptions with confidence levels"
rubric:
  correctness: 0.35
  input_elicitation: 0.3
  assumptions_explicit: 0.2
  actionability: 0.15
weight: 1.0
---

Edge case: sparse context missing the required geography and sector. Guards
against the skill fabricating ratings for an unspecified market instead of
eliciting scope or clearly labeling its assumptions and lowering confidence.
