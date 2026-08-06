---
id: identify-assumptions-existing-happy
skill: identify-assumptions-existing
input:
  prompt: >
    Our product is a B2B e-signature SaaS (Docusign competitor) for SMBs in Europe.
    We're considering adding a new feature: real-time collaboration on documents
    during signing (multiple users can comment and negotiate terms in-app before signing).
    Target users: legal teams and finance teams at mid-market companies (50–500 employees).
    Can you surface the risky assumptions we should validate before building this?
  context: >
    Product context: We've been operating for 3 years, have ~2,000 SMB customers,
    $1.5M ARR, 70% customer retention. Current feature set: basic e-signing,
    audit trails, compliance (GDPR, eIDAS). No collaboration or commenting features yet.
expected:
  - "Desirability assumptions identified: at least 2–3 covering user adoption, pain-point fit, and workflow displacement."
  - "Viability assumptions identified: at least 2–3 covering revenue impact, GTM, and support complexity."
  - "Feasibility assumptions identified: at least 2–3 covering integration with existing signing flow, infrastructure, and performance."
  - "Each assumption has a confidence level (High/Medium/Low) and a falsifiable validation step."
  - "Top 3–5 risks ranked by uncertainty × impact with mitigation suggestions."
  - "Summary statement on go/no-go readiness."
rubric:
  accuracy: "All assumptions are grounded in existing-product reality (not zero-to-one). Confidence levels are calibrated to the context (e.g., revenue impact unknown = low confidence in viability). Tests are concrete and falsifiable."
  completeness: "All three categories (Desirability, Viability, Feasibility) are covered. At least 2–3 assumptions per category. Risk ranking includes top 3–5 with mitigation. Summary present."
  actionability: "Each assumption has a concrete next step (interview users, pricing test, technical spike, etc.). Mitigation suggestions are specific enough to guide next actions."
weight: 1.0
---

Happy-path scenario: straightforward feature request for an existing product with clear context.
This guards against the skill failing to surface domain-specific risks (e.g., integration complexity,
user-workflow disruption, pricing model tension). Also ensures the skill tightly couples assumptions
to the existing-product context (not treating it as a greenfield launch).
