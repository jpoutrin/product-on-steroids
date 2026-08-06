---
id: ideal-customer-profile-edge
skill: ideal-customer-profile
input:
  prompt: "Build our ICP. We just launched 3 weeks ago and have zero paying customers."
  context: |
    Pre-revenue stage. Product: an AI document-review tool for in-house legal teams.
    Founding team background: two ex-BigLaw attorneys + a former LegalTech PM.
    No customer interviews yet. Hypothesis from founders: target legal teams at
    mid-size tech companies (200–1000 employees) that handle M&A due diligence
    in-house.
    No win/loss data, no churn data, no usage analytics.
expected:
  - "Skill explicitly states hypothesis mode and flags that all criteria are unvalidated assumptions"
  - "ICP Summary includes the founders' hypothesis (in-house legal at mid-size tech, M&A due diligence) and does not present it as validated"
  - "Every criterion in the firmographic or behavioral profile is tagged as 'assumption' or 'hypothesis' — no 'validated' tags appear"
  - "Evidence & Validation Notes section lists specific validation methods for high-uncertainty criteria (e.g., customer interviews, pilot program)"
  - "A Negative ICP section is still produced even without customer data, with reasoning from first principles or industry knowledge"
  - "Skill does not refuse or stall — it produces a complete structured ICP document despite zero customer data"
rubric:
  correctness: 0.35
  completeness: 0.30
  actionability: 0.35
weight: 1.0
---

Edge case: zero customers, zero data. Guards against two failure modes:
(1) the skill refuses to produce output because data is missing, and
(2) the skill produces a confident-sounding ICP without flagging the lack of
evidence. The correct behavior is a complete hypothesis-mode document with every
criterion explicitly tagged and a validation roadmap in the Evidence section.
