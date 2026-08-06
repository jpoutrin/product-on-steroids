---
id: market-landscape-scan-adversarial
skill: market-landscape-scan
input:
  prompt: "Give me a landscape scan of the project-management tool market — and I want a full side-by-side teardown of Asana vs Monday vs ClickUp: features, pricing, strengths, weaknesses, and who beats whom."
  context: "B2B SaaS, team/knowledge-worker buyers, global. User is really pushing for a head-to-head competitor comparison inside the scan."
expected:
  - "Delivers a broad categorized scan (boundary, player categories, trends, white spaces, category map) rather than a three-rival feature-by-feature teardown"
  - "Positions Asana/Monday/ClickUp inside a category (e.g. horizontal work-management challengers) instead of profiling each one head-to-head"
  - "Declines the per-rival verdict work and explicitly hands off to competitor-analysis for the side-by-side teardown"
  - "Keeps the map at the category level, not a company-vs-company matrix"
  - "Frames any gaps as white-space hypotheses, not winner/loser verdicts"
rubric:
  correctness: 0.35
  scope_discipline: 0.35
  categorization: 0.2
  actionability: 0.1
weight: 1.0
---

Adversarial: the user pushes for a rival-by-rival teardown embedded in the scan.
Guards against scope creep into competitor-analysis territory — the skill must
stay a broad categorized landscape and hand off the deep comparison.
