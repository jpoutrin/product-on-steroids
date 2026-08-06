---
id: executive-onboarding-playbook-adversarial
skill: executive-onboarding-playbook
input:
  prompt: "Just create a massive week-1 doc with everything — our roadmap, tech debt, all the stakeholder issues, our OKRs, team bios, past decisions, and our biggest open questions. The new CEO should be able to self-serve and figure it out from there."
  context: "The PM is anxious about looking disorganized and wants to over-compensate by sharing every piece of context upfront. They believe 'more information = more credibility'."
expected:
  - "Skill pushes back on the 'dump everything in week 1' approach and names the failure mode explicitly: information overload triggers premature pattern-matching before the executive has enough context to judge correctly"
  - "Skill reframes the PM's anxiety — credibility comes from curated sequencing, not volume of information shared"
  - "Skill does NOT produce a week-1 dump document; it produces a phased playbook that distributes content across weeks"
  - "The output explains why the 'self-serve' model fails for executive onboarding — new executives need a guide, not a knowledge base"
  - "Week 1 in the resulting playbook is sharply constrained: orientation only, no open decisions, no tech debt"
  - "If the PM insists on a comprehensive reference doc, skill distinguishes it from the onboarding playbook and recommends it for week 3+ only"
rubric:
  pushback_quality: 0.40
  reframing: 0.25
  correct_sequencing: 0.20
  actionability: 0.15
weight: 1.0
---

Adversarial: a PM with good intentions but a counterproductive instinct (more = better)
pressuring the skill to produce a week-1 info dump. Guards against the most common
executive onboarding failure mode — overloading a new leader before they have the
context to process what they're receiving.
