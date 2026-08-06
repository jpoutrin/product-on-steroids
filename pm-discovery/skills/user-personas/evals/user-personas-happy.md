---
id: user-personas-happy
skill: user-personas
input:
  prompt: "Build user personas for our B2B e-signature tool."
  context: |
    We ran 24 structured interviews (15 contract managers, 9 legal ops leads) and
    a 180-response survey. Key findings: 72% cite version confusion across email
    threads as their top pain; 18/24 interviewees pay for personal Acrobat Pro
    subscriptions out-of-pocket because IT procurement takes 6+ weeks; contract
    managers complete 3-5 signature cycles per week while legal ops leads handle
    batch runs of 20+ documents monthly. NPS verbatims highlight "just get me the
    countersigned PDF fast" as the dominant desired outcome.
expected:
  - "Produces 2–3 distinct personas behaviorally differentiated (contract manager vs legal ops lead at minimum)"
  - "Each persona has a named JTBD tied to the frequency data provided (e.g., 3-5 cycles/week vs monthly batch)"
  - "Pain points cite evidence from the provided data (e.g., '72%', '18/24 interviewees')"
  - "Includes the out-of-pocket Acrobat Pro finding as an Unexpected Insight with a product implication"
  - "Every quote is labeled verbatim or synthesized"
  - "Personas are behaviorally distinct, not just demographic splits (age/title alone is insufficient)"
rubric:
  data_grounding: 0.40
  completeness: 0.30
  distinctness: 0.20
  actionability: 0.10
weight: 1.0
---

Happy path: rich interview + survey data with clear behavioral segments. Guards
against demographic-only segmentation, unsupported claims, and missing the
counterintuitive willingness-to-pay insight. Also validates that evidence
frequency counts (e.g., "18/24") are surfaced rather than smoothed into vague
language.
