---
id: storyboard-edge
skill: storyboard
input:
  prompt: >
    Storyboard how a senior software engineer uses our AI-assisted code review
    feature. The feature analyzes a pull request and flags potential bugs,
    style violations, and security issues before human reviewers see it.
  context: >
    The feature is brand new — no prototype exists. The PM has no user research
    data yet. The AI runs in the background and posts inline comments on the PR
    within 30–90 seconds. The engineer has not used the feature before. The
    team wants the storyboard to communicate the concept to designers before
    wireframes are built.
expected:
  - "Translates the abstract AI capability into concrete human moments (e.g., what the engineer actually sees, clicks, reads) — does not describe the AI's internal behavior as a frame"
  - "Produces 5–8 frames; does not collapse the scenario into 2–3 vague frames because the feature is abstract"
  - "Every frame has Scene, Action, Emotion, Annotation — none omitted"
  - "Annotations flag assumptions explicitly (e.g., 'We are assuming the AI comment arrives before the engineer pings a human reviewer — needs timing data')"
  - "Does not invent specific metrics or performance claims for the AI that were not provided"
  - "Takeaways surface at least one open design question for the design team to resolve"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge-case guard: tests the skill's ability to handle an abstract, capability-first
feature description and produce a concrete, human-centered narrative without
inventing facts or collapsing the arc. A weak output either anthropomorphizes
the AI (making it a character rather than showing what the human experiences)
or stays so abstract that frames describe system behavior rather than user
experience. This scenario also checks that the skill surfaces assumption flags
when the PM has no research data to ground the storyboard.
