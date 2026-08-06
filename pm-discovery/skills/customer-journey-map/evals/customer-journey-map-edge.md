---
id: customer-journey-map-edge
skill: customer-journey-map
scenario: >
  Sparse-data B2B enterprise product where the PM has no customer interviews
  and only a rough product description. Most stages must be inferred from
  domain knowledge. Tests correct labeling of evidence vs. inference and
  appropriate scope narrowing when data is thin.
input:
  prompt: >
    Map the customer journey for Procura, a B2B procurement automation platform
    sold to mid-market CFOs and their procurement teams. We have no interview
    data yet. Persona: CFO at a 200–1000 person company who wants to reduce
    maverick spend and get visibility into vendor contracts. Map all stages.
  context: >
    No research materials available. Product is a SaaS platform that integrates
    with ERP systems (SAP, NetSuite), surfaces spend analytics, and automates
    PO approval workflows. Typical deal size: $40K–$120K ARR. Sales-led motion
    with a 3–6 month enterprise sales cycle. Implementation requires IT involvement.
expected:
  - Every pain point and opportunity is explicitly labeled [inference] since no research was provided.
  - The Acquisition stage accounts for the 3–6 month enterprise sales cycle and procurement committee dynamics.
  - The Onboarding stage flags IT involvement and ERP integration as likely friction points (labeled [inference]).
  - At least one Moment of Truth reflects the B2B evaluation/procurement committee dynamic (not a B2C-style decision).
  - The skill does not fabricate specific statistics or quote non-existent interviews.
  - Prioritized Improvements recommend discovery steps before scoping (noted as "Needs discovery first" for high-uncertainty items).
rubric:
  accuracy: No invented research data; all claims are flagged as [inference] and plausibly grounded in B2B procurement domain knowledge.
  completeness: All required sections present; enterprise-specific dynamics (multi-stakeholder buying, IT dependency, ERP integration) are represented.
  actionability: At least two opportunities name the mechanism and stage clearly enough to prioritize discovery sprints around them.
weight: 1.0
---

Guards behavior under sparse data conditions common in early-stage or enterprise
products. The risk being guarded: the skill hallucinates interview evidence, uses
B2C journey patterns for a complex B2B buying cycle, or presents inferences as
facts. The correct response is a fully structured map where every finding is
honestly labeled [inference], the enterprise sales cycle complexity is surfaced
in Acquisition/Consideration, and high-uncertainty improvements are flagged as
requiring discovery before scoping.
