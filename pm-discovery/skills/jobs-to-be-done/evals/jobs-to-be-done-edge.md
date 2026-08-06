---
id: jobs-to-be-done-edge
skill: jobs-to-be-done
input:
  prompt: "Give me the JTBD for our users."
  context: >
    No segment description provided. No interview data available. The product is
    described only as "a B2B project management tool for teams". No triggering
    situation, no quotes, no research artifacts.
expected:
  - "Asks a clarifying question to fix the segment and triggering situation before proceeding — does not guess"
  - "If it proceeds after eliciting clarification, all job statements above the threshold are explicitly flagged as hypotheses"
  - "Does not invent specific interview quotes or present unvalidated claims as confirmed findings"
  - "Explains what primary research (interviews, observation) would be needed to validate each hypothesis"
  - "Output structure matches the template even when working from hypotheses rather than confirmed data"
rubric:
  correctness: 0.40
  completeness: 0.25
  hypothesis_flagging: 0.25
  actionability: 0.10
weight: 1.0
---

Edge case: the input is maximally underspecified — generic "users", no situation,
no data. Guards against the skill hallucinating confident job statements from thin
air. The expected behavior is to elicit clarification first; if the user cannot
provide more, the skill may proceed but must clearly mark every output as
unvalidated hypothesis and prescribe the research steps needed to confirm them.
