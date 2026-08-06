---
id: pre-mortem-happy
skill: pre-mortem
input:
  prompt: "Run a pre-mortem on our new B2B SaaS product launch (Notion-style collaboration tool for mid-market). PRD attached. Launch is 6 weeks away."
  context: "Product is feature-complete but go-to-market strategy not fully defined. Sales team hasn't been trained. Competitor recently launched similar feature set."
expected:
  - "Identifies ≥3 Tigers (real risks) with specific failure modes, not generic worries"
  - "Separates Tigers into launch-blocking, fast-follow, and track categories"
  - "Includes ≥1 Paper Tiger with reasoning for why it's overblown"
  - "Includes ≥1 Elephant (unspoken assumption) with suggested investigation method"
  - "Every launch-blocking Tiger has a named owner and a concrete mitigation action"
  - "Risks are anchored to evidence (e.g., untested at enterprise scale, dependency on key hire) or logic"
rubric:
  risk_specificity: 0.3
  categorization: 0.25
  actionability: 0.25
  evidence_based: 0.2
weight: 1.0
---

Happy path: clear PRD, defined timeline, cross-functional context. Skill should surface real risks (onboarding UX at scale, enterprise sales friction, competitive differentiation) while filtering overblown concerns. Guards against vague risk lists and round-number guesses.
