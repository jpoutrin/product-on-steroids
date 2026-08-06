---
id: feedback-note-adversarial
skill: feedback-note
input:
  prompt: "Write a feedback note for Jordan that covers both some really good
    work she did on the roadmap presentation AND the fact that she keeps
    interrupting people in meetings. I want to do it all in one note."
  context: "Jordan is a senior PM and a peer. The roadmap presentation was last
    month. The interrupting behavior has happened in three consecutive weekly
    syncs."
expected:
  - "The skill declines to produce a single note combining positive and constructive feedback"
  - "The skill explains why mixing directions in one note undermines both messages"
  - "The skill offers to produce two separate notes instead"
  - "If the user agrees, the two notes are each properly SBI-structured with the right direction (positive / constructive) independently"
  - "Neither note contains judgment labels about Jordan's character"
rubric:
  refuses_mixed_note: 0.40
  explains_rationale: 0.25
  offers_two_notes: 0.20
  sbi_structure_if_drafted: 0.15
weight: 1.0
---

Adversarial case: the user explicitly requests a combined positive-and-constructive
note. The skill must refuse this combination — mixing directions dilutes both
messages and makes it harder for the recipient to act on either. Guards against
the skill blindly complying with a structurally harmful request. The correct
response is to decline, explain briefly, and offer two clean notes.
