---
id: user-stories-happy
skill: user-stories
input:
  prompt: "Write user stories for a 'Recently Viewed Products' section on our e-commerce product page."
  context: "Product: ShopFlow (B2C e-commerce platform). Users: Online Shoppers and Guest Visitors. Design: https://figma.com/shopflow/recently-viewed. Constraint: section must be WCAG 2.1 AA accessible. Stories should be sprint-sized."
expected:
  - "Each story uses exact 'As a [persona], I want [action], so that [outcome]' format"
  - "Every story has 4–6 numbered, observable acceptance criteria"
  - "Stories are independent and can be developed in any order"
  - "Each story includes a Design field referencing the Figma link"
  - "At least one acceptance criterion per story covers an edge case or exclusion condition"
  - "At least one criterion addresses accessibility (WCAG 2.1 AA)"
rubric:
  correctness: 0.35
  completeness: 0.30
  invest_compliance: 0.20
  actionability: 0.15
weight: 1.0
---

Happy-path scenario: a well-specified feature with a design link, clear user roles, and an explicit constraint (accessibility). Guards against the skill skipping the design field, producing fewer than 4 acceptance criteria, or writing non-specific acceptance criteria such as "it should work correctly."
