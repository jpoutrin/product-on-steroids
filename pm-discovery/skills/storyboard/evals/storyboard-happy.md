---
id: storyboard-happy
skill: storyboard
input:
  prompt: >
    Storyboard the onboarding experience for Marcus, a 34-year-old Operations
    Manager at a 50-person logistics company, using our B2B SaaS task-management
    tool for the first time after his IT admin set up his account. Focus on his
    first login through completing his first task assignment.
  context: >
    Product: a B2B project management SaaS. Target user: operations managers
    who are not highly technical. Onboarding is self-serve after admin account
    creation. Key flows: login → dashboard → create project → assign task →
    invite teammate. Known friction point: the teammate invitation step requires
    email lookup, which confuses non-admin users.
expected:
  - "Produces 5–8 numbered frames covering the full arc from login to task assignment completion"
  - "Every frame has all four sub-sections: Scene, Action, Emotion, Annotation"
  - "At least one frame captures a negative or mixed emotion (e.g., confusion, frustration)"
  - "Each Emotion sub-section uses a named label (e.g., anticipation, confusion, relief) plus an explanatory sentence"
  - "Annotations surface PM-level insights or design questions — not paraphrases of the scene"
  - "Takeaways section contains 3–5 bullets grounded in specific frames"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Happy-path guard: verifies the skill produces a well-formed, emotionally honest
storyboard for a realistic B2B SaaS onboarding scenario with a named persona
and a known friction point. Guards against outputs that are structurally
incomplete (missing sub-sections), emotionally flat (all positive), or
annotated with scene paraphrases rather than PM insights.
