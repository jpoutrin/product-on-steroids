---
id: pol-probe-edge
skill: pol-probe
input:
  prompt: >
    I just joined Nova Health (a 200-person health-tech startup) three weeks
    ago as a PM. My manager asked me to drive a new patient-onboarding flow
    redesign that will require sign-off from product, clinical operations, and
    legal. I barely know anyone yet. Can you help me do a POL probe so I know
    how to start engaging stakeholders?
  context: >
    PM is new (3 weeks in). Knows their manager (Head of Product, Priya Shah)
    and one engineer (Dmitri Volkov) from onboarding. Aware that clinical ops
    has historically been skeptical of product-driven redesigns. No budget
    figure provided. No names for legal or clinical ops leadership. No
    knowledge of decision cycles. Regulatory context: health-tech, so HIPAA
    compliance review is likely required.
expected:
  - Skill produces a POL Brief rather than refusing due to thin context
  - Every inferred element (e.g. assumed clinical ops stance, assumed veto
    holders) is flagged with [Low confidence — validate with: <source>]
  - Organizational Levers section identifies legal/HIPAA review as a likely
    veto point even without named individuals
  - Risk Register includes a risk about the PM's credibility gap as a newcomer
    and suggests a concrete mitigation (e.g. brief through manager first)
  - Engagement Strategy recommends Priya Shah as first conversation to map
    the org before any direct stakeholder outreach
  - Brief explicitly tells the PM which gaps to close in the first two weeks
    of relationship-building
rubric:
  correctness: 0.35
  completeness: 0.3
  actionability: 0.35
weight: 0.8
---

Edge case: PM has almost no organizational context — a common real-world
situation when someone is new. Guards against two failure modes — (1) refusing
to produce anything useful because context is thin, and (2) producing a brief
that presents inferences as facts without confidence flags.

The right behavior is a best-effort brief that is transparent about what it
knows vs. infers, prioritizes closing information gaps over false precision,
and makes Priya Shah the first engagement step (since she is the one person
who can unlock org intelligence quickly). The HIPAA regulatory angle should be
surfaced even without explicit mention by the PM, because the health-tech
context makes it a structural veto point.
