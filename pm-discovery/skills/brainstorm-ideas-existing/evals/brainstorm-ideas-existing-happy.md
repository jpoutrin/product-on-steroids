---
id: brainstorm-ideas-existing-happy
skill: brainstorm-ideas-existing
scenario: >
  Clear product opportunity with research context: a SaaS team collaboration tool
  (Slack-like) wants to reduce message overwhelm for large teams. User provides
  the product, objective, segment, and some research data (user interviews
  mentioning notification fatigue).
input:
  prompt: >
    We run a team chat product for enterprise teams (50–500 people). We're seeing
    churn in large teams (200+) due to message overwhelm — users report they miss
    important conversations in the noise, and notifications keep interrupting them.
    We want to improve how people stay in the loop without being overwhelmed. Help
    me brainstorm feature ideas from PM, Designer, and Engineer perspectives.
  context: >
    Recent user interviews (10 large-team leads) flagged: (1) muting channels
    leaves them out of the loop, (2) keyword notifications are too blunt, (3)
    they spend 20+ min/day scrolling to find what matters. Product has 2M users,
    $40 CAC, $500 ARR per customer. Tech stack: React frontend, Node backend,
    PostgreSQL, Elasticsearch for full-text search.
expected:
  - "All three perspectives (PM, Designer, Engineer) are represented with distinct ideas."
  - "Top 5 ideas are specific, grounded in product context, and address message overwhelm."
  - "Each prioritized idea includes name, 1-sentence description, selection reasoning, ≥2 assumptions, and feasibility/impact tags."
  - "Ideas span at least two perspectives (not PM-only or Designer-only dominance)."
  - "Assumptions are testable (e.g., 'reduce time-to-important-msg by 3+ min') and not generic."
rubric:
  correctness: >
    All top 5 ideas are directly responsive to the stated opportunity (message
    overwhelm in large teams). Ideas do not contradict the product context
    (e.g., no suggestions to remove notifications entirely). Ideas distinguish
    between perspectives meaningfully.
  completeness: >
    All three perspectives are represented with 5 ideas each. Each prioritized
    idea has all required elements: name, description, reasoning, ≥2 assumptions,
    feasibility tags, impact tags. No placeholder text remains.
  actionability: >
    Ideas are specific enough to act on (e.g., "smart digest at 9am" not "improve
    notifications"). Assumptions are concrete and measurable. Feasibility tags
    include effort/scope (e.g., "3 weeks, ML-based ranking"). Ideas reference the
    product's actual stack (Elasticsearch, React, Node) or segment reality
    (200+ person teams).
weight: 1.0
---

This scenario tests the skill's ability to ideate from multiple perspectives when
given a clear product opportunity with some research context. It guards against:
generic ideas, skipped perspectives, missing detail in prioritized ideas, and
assumptions that are too vague to test. A strong output shows the skill can
integrate domain knowledge (SaaS, chat products), prioritize across perspectives,
and ground ideas in the product's current state and technical constraints.
