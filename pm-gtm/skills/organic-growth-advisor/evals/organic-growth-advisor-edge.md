---
id: organic-growth-advisor-edge
skill: organic-growth-advisor
input:
  prompt: >
    We have a consumer habit-tracking app (iOS/Android). We launched 3 months ago,
    have about 800 downloads total, no community, no social presence, and the app
    has no sharing feature or invite flow. We want to go viral organically. What
    should we do?
  context: >
    Consumer mobile app, pre-PMF (very early traction — 800 downloads in 3 months),
    no community, no product viral hooks (no share/invite), no social presence.
    User says "go viral" with no organic infrastructure in place.
expected:
  - "Skill diagnoses the absence of product viral hooks (no share/invite flow) and flags this as a prerequisite before recommending PLG virality"
  - "Skill does not promise 'going viral' — explicitly states virality requires product hooks and an existing audience to amplify"
  - "Playbook recommends building foundations first (product hook instrumentation, one community seed channel) before any amplification tactic"
  - "Time-to-impact for community and content tactics is stated as 3–12 months — not weeks"
  - "Skill asks about or acknowledges the ICP (who the habit-tracker is for) since consumer is broad"
  - "At least one tactic addresses the missing product viral surface (recommend adding a share or invite feature as a prerequisite)"
  - "Sequencing reflects the cold-start reality: Phase 1 is infrastructure, not growth"
rubric:
  correctness: 0.45
  completeness: 0.25
  actionability: 0.3
weight: 1.0
---

Edge case: a consumer app at pre-PMF with no organic growth infrastructure who asks to
"go viral." The failure mode is recommending TikTok/influencer/referral tactics without
acknowledging that the product has no share hooks and the user base is too small to
amplify anything. The skill must diagnose the missing infrastructure, set realistic
expectations about virality, and sequence foundations before amplification. It must
also surface that consumer is a broad ICP and may need narrowing.
