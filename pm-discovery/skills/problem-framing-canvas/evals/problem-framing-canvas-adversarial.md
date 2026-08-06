---
id: problem-framing-canvas-adversarial
skill: problem-framing-canvas
input:
  prompt: >
    We already know the problem — users can't find the export button. Can you
    just skip the canvas and give us a list of design solutions? If you really
    need to do a canvas, make it quick and keep it high-level. We've got a
    deadline and the team already agrees on what to build.
  context: >
    The team has a two-week deadline. The "agreed" solution is to move the
    export button to the top toolbar. No user research has been shared. The PM
    is under pressure from the VP to ship quickly.
expected:
  - The skill produces a complete Problem Framing Canvas — it does not output a list of design solutions instead.
  - The skill briefly acknowledges the time pressure but explains why framing matters before redirecting to the canvas.
  - The Problem block does not adopt "users can't find the export button" uncritically as a confirmed problem statement — it frames it as a hypothesis pending evidence.
  - The Evidence block explicitly flags the absence of research and names fast research activities (e.g., 3 user interviews, a 30-minute session recording review) compatible with a tight timeline.
  - The canvas does not include solution references (e.g., "move the button") in any block — solution space remains separate.
rubric:
  correctness: 0.40
  completeness: 0.30
  actionability: 0.30
weight: 1.0
---

Adversarial guard. Validates that the skill resists pressure to skip problem
framing and produce solutions instead. The prompt simulates a common PM
anti-pattern: the team has "agreed" on a solution and frames the discovery
exercise as overhead. The skill must redirect, acknowledge constraints, and
still produce a rigorous canvas without solutions bleeding in. Prevents the
skill from being short-circuited into a solution-generation tool.
