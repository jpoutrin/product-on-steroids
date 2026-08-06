---
id: competitive-research-snapshot-edge
skill: competitive-research-snapshot
input:
  prompt: >
    We are building VoiceOps, an AI call-summarization tool for B2B sales reps.
    The category is brand-new — there are no established direct competitors yet.
    Please build a competitive research snapshot so we can understand the
    landscape before our launch.
  context: >
    VoiceOps integrates with CRMs and records + summarizes sales calls. It
    launched in private beta last month. No competitors have been named by the
    user; the PM is asking the skill to discover them.
expected:
  - Skill surfaces at least 3 indirect competitors or substitutes (e.g. Gong, Chorus, manual note-taking, CRM built-ins, generic transcription tools)
  - Each indirect competitor is clearly flagged as "indirect" in the table
  - Landscape Overview explicitly acknowledges the absence of direct competitors and explains the category-creation context
  - "Where to Win" section addresses category-creation opportunity rather than defaulting to "we are better than X" framing
  - "Gaps & Risks" flags the risk of a large player (e.g. Salesforce, HubSpot) entering the space
rubric:
  correctness: 0.4
  completeness: 0.3
  actionability: 0.3
weight: 1.0
---

Edge case: the market has no established direct competitors, so the skill must
identify and classify indirect substitutes rather than refusing or producing a
skeleton table. Guards against the skill failing silently (empty table) or
treating the absence of direct competition as a reason to skip the snapshot.
The Where to Win section must reframe around category creation, not head-to-head
comparison.
