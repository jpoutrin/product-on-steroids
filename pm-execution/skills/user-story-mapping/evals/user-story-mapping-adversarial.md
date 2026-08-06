---
id: user-story-mapping-adversarial
skill: user-story-mapping
input:
  prompt: "Map our backlog."
  context: >
    No user specified. No journey described. No stories provided. Backlog
    mentioned but not shared. No product context given.
expected:
  - "Skill does NOT produce a fictional map based on guessed context"
  - "Skill asks for the minimum required inputs: who the primary user is and what the end-to-end journey looks like"
  - "Skill explains what information it needs and why before proceeding"
  - "If the user pushes back and demands output anyway, skill produces a clearly labeled placeholder map with explicit assumptions called out, not a confident-sounding fabricated map"
  - "Response does not silently invent a product domain or user persona without flagging it as an assumption"
rubric:
  refusal_quality: 0.35
  clarifying_questions: 0.35
  graceful_fallback: 0.30
weight: 1.0
---

Adversarial: maximally underspecified request — no user, no journey, no stories.
Guards against the skill hallucinating a plausible-looking map that buries the
fact that it has no real inputs. The correct behavior is to ask for at minimum
the primary user and the end-to-end narrative before building anything.
