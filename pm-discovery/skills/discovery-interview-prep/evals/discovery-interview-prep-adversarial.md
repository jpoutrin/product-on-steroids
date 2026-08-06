---
id: discovery-interview-prep-adversarial
skill: discovery-interview-prep
input:
  prompt: >
    I have a discovery interview with a potential customer next week. I want to
    use the session to test our solution concept — we've built a prototype of an
    automated invoice-matching dashboard and I'd like to walk them through it
    and see if they'd buy it. Can you help me prep questions to validate whether
    they like the solution?
  context: >
    PM is in early discovery but has jumped to a solution concept. They are
    framing the interview as a solution-validation or sales call, not a learning
    session. No problem-space hypotheses stated.
expected:
  - Skill explicitly reframes the PM's intent — names the risk that showing a
    solution concept in early discovery will bias the participant's responses
    and foreclose learning about the actual problem.
  - Skill does NOT produce questions designed to pitch or walk through the
    prototype.
  - "Solution-pitching" and "showing the prototype" appear in the Forbidden
    Frames section of the final prep sheet.
  - Skill redirects to a learning-first objective: helps the PM articulate what
    problem or behaviour they want to understand *before* any concept is shown.
  - If the PM accepts the reframe, skill produces a valid prep sheet with
    hypotheses and open-ended behavioural questions aligned to the underlying
    problem (invoice reconciliation), not to the solution concept.
  - Skill may optionally note that concept testing belongs in a later evaluative
    phase, with a different session design (e.g. prototype walkthrough with
    think-aloud), not in generative discovery.
rubric:
  correctness: 0.5
  completeness: 0.25
  actionability: 0.25
weight: 1.0
---

Adversarial scenario: PM wants to use a discovery session to pitch their solution
concept and collect purchase intent, conflating discovery with sales or concept
testing. This is one of the most common and damaging mistakes in product
discovery — it produces confirmation bias, not learning. Guards against the skill
complying with solution-pitching framing. Validates that the skill actively
reframes toward learning-first and encodes "solution-pitching" as a Forbidden
Frame in the output, while remaining constructive and producing a usable prep
sheet once the PM accepts the reframe.
