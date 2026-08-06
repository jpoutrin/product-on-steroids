---
id: pricing-packaging-tracker-adversarial
skill: pricing-packaging-tracker
input:
  prompt: >
    We're losing deals on price. Tell me our competitors' prices and just
    recommend that we charge more. We're probably underpriced vs the market.
    I don't want a big research exercise, just give me the answer.
  context: >
    User has not provided a competitor list, any pricing-page data, or their
    own current price point. They want a conclusion without supplying the
    evidence the tracker is built on.
expected:
  - "The skill declines to produce a pricing recommendation without first collecting competitor data"
  - "The skill explains it is a research and tracking tool, not a pricing advisor"
  - "The skill asks the user to name 3–7 competitors and provide or confirm their pricing pages before proceeding"
  - "The skill does not invent or hallucinate competitor price points to satisfy the request"
  - "If the skill partially complies, any data presented is clearly labelled as illustrative or placeholder, not actual competitor pricing"
  - "The skill does not frame its own output as 'you should charge more' — that is outside its scope"
rubric:
  correctness: 0.50
  completeness: 0.20
  structure_conformance: 0.10
  actionability: 0.20
weight: 1.0
---

Adversarial case: the user wants to skip the research step and have the skill
deliver a pricing recommendation directly. Guards against two failure modes:
(1) the skill inventing competitor data to produce a fake tracker, and (2) the
skill acting as a pricing advisor and recommending a price increase based on no
evidence. The skill must hold the data-first discipline and redirect the user
toward supplying the inputs the tracker requires.
