---
id: proto-persona-edge
skill: proto-persona
input:
  prompt: >
    I'm the only one who's thought about this at all. We're building a tool for
    freelance graphic designers to manage client feedback on design deliverables.
    My assumption is that they're drowning in revision requests over email and
    Slack and lose track of what's approved. Build me a proto-persona.
  context: >
    Single stakeholder (the PM) providing all assumptions. No kickoff notes,
    no other team input, no market research references. The PM has not spoken
    to any freelance designers directly.
expected:
  - "Output explicitly flags that inputs came from a single stakeholder, warning about the thin basis"
  - "Artifact is still useful — produces a named persona with all 6 sections populated"
  - "Validation Plan is particularly emphasized as critical given the thin input basis"
  - "Output carries a [HYPOTHESIS — NOT VALIDATED] banner"
  - "All assumption sections are labeled [ASSUMED] and quote labeled [INVENTED]"
  - "At least one red-flag result is stated that would invalidate the core frustration assumption"
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge case: inputs come from a single stakeholder with no corroboration. Guards two
failure modes in tension with each other — (1) producing a proto-persona so hedged
it is useless, and (2) producing a confident-looking artifact without flagging the
particularly thin basis. The skill must thread this: produce a genuinely useful
provisional artifact while making the single-source limitation unmistakably visible
and weighting the Validation Plan accordingly.
