---
id: test-scenarios-happy
skill: test-scenarios
input:
  prompt: "Generate test scenarios for this user story: As an online shopper, I want to see a recently-viewed products section on each product page, so that I can quickly return to items I was considering."
  context: "Acceptance criteria: (1) Section appears only after at least 1 prior product has been viewed in the session. (2) Section displays 4–8 product cards with image, title, and price. (3) The current product is excluded from the list. (4) Clicking a card navigates to that product's page. Product: e-commerce web app."
expected:
  - "Produces at least one test scenario per acceptance criterion (minimum 4 scenarios)"
  - "Each scenario includes explicit starting conditions (session state, data setup, user role)"
  - "Test steps are numbered and each step records its inline expected result (action → result)"
  - "Expected Outcomes section lists observable, binary results a tester can mark pass/fail"
  - "At least one edge-case scenario is present (e.g., no prior viewed products, or fewer than 4)"
  - "A Coverage Summary table maps each acceptance criterion to its scenario(s)"
rubric:
  coverage: 0.35
  step_precision: 0.25
  observability: 0.25
  edge_cases: 0.15
weight: 1.0
---

Happy path: a well-specified user story with four clear acceptance criteria and
enough product context to generate precise, executable scenarios. Guards against
vague steps, missing starting conditions, and omitting the edge case of zero or
few previously-viewed products.
