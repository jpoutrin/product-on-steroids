---
id: user-segmentation-adversarial
skill: user-segmentation
scenario: >
  Vague request with no data provided ("just segment our users"). Skill must refuse to
  hallucinate and ask for data sources before proceeding. Tests boundary behavior.
input:
  prompt: >
    Can you segment our users?
  context: >
    No supporting information. No feedback data, no product description, no user base size,
    no behavioral insights provided.
expected:
  - Skill asks for required inputs before proceeding; does not guess or assume.
  - Specific data sources requested (interviews, usage logs, support tickets, surveys, NPS feedback, or similar).
  - Skill explains why segmentation without data is not actionable.
  - Skill offers to segment once data is provided; does not refuse the ask outright.
  - Skill does not return a generic 3–5 segment framework applied to an imaginary product.
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

**Why this scenario exists:**
This guards against hallucination and false authority. Segmentation without grounding data
is speculation, and returning invented segments under the guise of analysis is worse than
refusing the task. The skill must be honest about prerequisites. Measures whether the skill
prioritizes data integrity over apparent productivity and knows when to ask for help.
