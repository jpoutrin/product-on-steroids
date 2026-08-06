---
id: prioritize-assumptions-happy
skill: prioritize-assumptions
input:
  prompt: "Prioritize these 6 assumptions for a B2B SaaS product (AI-powered document summarization for legal teams)."
  context: |
    Assumptions from user interviews (10 in-house counsel at mid-market firms):
    1. In-house counsel needs faster document review (confidence: high)
    2. They'll pay €200+/mo for this tool (confidence: low)
    3. AI accuracy on legal documents must be >95% (confidence: medium)
    4. Implementation/setup is faster than current manual review (confidence: medium)
    5. Compliance and data privacy concerns are blocking adoption (confidence: medium)
    6. Most legal teams use Microsoft Word/Google Docs (confidence: high)
expected:
  - "Ranks assumptions by impact × uncertainty (high/high first)"
  - "High-uncertainty assumptions (e.g., willingness to pay, compliance fears) surface as top priorities"
  - "Includes specific validation methods (pre-order test, compliance audit, etc.) for top-3 assumptions"
  - "Provides rationale explaining why willingness-to-pay or compliance is scored as high-impact"
  - "Distinguishes between low-uncertainty (e.g., tool adoption) and high-uncertainty (price, compliance)"
rubric:
  correctness: 0.35
  completeness: 0.25
  actionability: 0.25
  rationale_clarity: 0.15
weight: 1.0
---

Happy path: well-formed assumption list with mixed confidence levels. Skill should surface pricing and compliance as top priorities (high impact, high uncertainty) and defer lower-impact assumptions (e.g., Word/Docs compatibility). This scenario guards against flat prioritization (treating all assumptions equally) and ensures the skill correctly inverts confidence into uncertainty scoring.
