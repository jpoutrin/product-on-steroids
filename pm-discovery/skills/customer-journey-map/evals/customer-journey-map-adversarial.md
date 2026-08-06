---
id: customer-journey-map-adversarial
skill: customer-journey-map
scenario: >
  Vague ask with no persona provided. The user says "map the user journey for
  my app" without identifying who the user is, what the app does, or what
  JTBD is being served. Tests that the skill elicits the persona before
  proceeding rather than producing a useless generic map.
input:
  prompt: >
    Map the user journey for my app.
  context: >
    No additional context provided. The user has not named a persona, described
    the product, shared a URL, or supplied any research materials.
expected:
  - The skill does NOT produce a generic journey map without a persona.
  - The skill asks at minimum for the persona (role/segment + JTBD) and a brief product description before proceeding.
  - The clarifying questions are specific and purposeful — not a laundry list of every possible input.
  - If the user provides only a product name with no persona in a follow-up, the skill asks for the persona again rather than inventing one.
rubric:
  accuracy: The skill correctly identifies that the request is underspecified and refuses to map a generic "user" journey.
  completeness: The clarifying ask covers at minimum persona identity and product/JTBD; it may also ask about scope (stages) and research materials.
  actionability: The questions are concise (2–3 targeted asks, not a paragraph of demands) and would unblock the skill if answered.
weight: 1.0
---

Guards against the most common failure mode for journey mapping: producing a
hollow, generic map that fills in placeholder personas and vague emotions
("users feel frustrated") when the input is underspecified. A generic CJM is
worse than no CJM — it creates false alignment in the team around an artifact
that has no grounding. The correct behavior is to surface the gap immediately
and ask for the minimum viable input (persona + product context) before
producing any output. This adversarial card also guards against the skill
asking too many questions at once, which stalls the workflow.
