---
id: discovery-process-happy
skill: discovery-process
scenario: >
  Standard sprint-scoped discovery kick-off for a B2B SaaS team. Clear trigger,
  moderate user access, 4-week runway.
input:
  prompt: >
    We're a 4-person PM/UXR team at a B2B HR-tech company. Our "onboarding
    completion" metric dropped 18% last quarter. Eng thinks it's a UX issue;
    sales thinks we're selling to the wrong segment. We've never done structured
    discovery on this flow — just a handful of support tickets. We have 4 weeks
    and access to ~20 recent churned customers who might take a call. Help me
    plan the discovery.
  context: >
    Team has moderate research experience. No prior interview data. Metric drop
    is the primary business trigger. Stakeholders are misaligned on root cause.
expected:
  - Discovery Goal is phrased as "We need to understand …" and includes a done
    criterion tied to a number of confirming data points or a specific artifact
    (e.g., problem statement or OST branch).
  - All three phases (Explore, Validate, Synthesize) are present with realistic
    durations summing to ~4 weeks, and Explore precedes Validate.
  - Methods table names at least 3 specific methods with rationale; each method
    is mapped to a pm-discovery skill by name.
  - Artifacts Checklist lists at least 4 concrete deliverables, each with a phase
    and a skill.
  - Risks & Mitigations addresses the stakeholder misalignment (confirmation bias
    or pre-committed solution risk) explicitly.
  - The plan does not prescribe a solution — it stays in problem space.
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

This is the canonical happy-path scenario: a PM with a clear trigger (metric
drop), a concrete time box (4 weeks), and a real access constraint (20 churned
customers). It guards against the skill producing a generic "do some interviews"
non-plan. The stakeholder misalignment angle tests whether the Risks section is
substantive rather than boilerplate. A good output gives this team something they
can hand to their UXR on Monday morning.
