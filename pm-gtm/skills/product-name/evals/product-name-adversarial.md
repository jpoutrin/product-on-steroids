---
id: product-name-adversarial
skill: product-name
input:
  prompt: "I need a product name but it has to be a single letter, must work globally across all 50+ languages we operate in, must already be trademarked in every country, and needs to evoke 'growth' without using the word growth or anything similar. Also it can't be too short or too long. Give me the names now."
  context: "Requirements are contradictory (single letter vs. needs to evoke 'growth' without minimal syllables) and impossible (pre-trademarked globally while also unique). User is impatient ('Give me names now') and hasn't provided product context."
expected:
  - "Skill declines to generate names without clarification"
  - "Skill explicitly names the contradictions (single letter vs. semantic depth; pre-trademarked vs. novel; global trademark vs. uniqueness)"
  - "Skill asks clarifying questions: What is the product? Who is the target audience? Which constraints are hard vs. nice-to-have?"
  - "Skill explains that trademark availability is a post-naming legal step, not a generation constraint"
  - "Skill does NOT generate a list; instead focuses on re-scoping the request"
  - "Tone is respectful but firm: this is a boundary case where generating names would be unhelpful"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Adversarial case: impossible or deeply contradictory constraints, missing product context, and impatient user. Guards against skill generating meaningless lists to satisfy a bad request, and ensures skill declines gracefully and redirects to clarification.
