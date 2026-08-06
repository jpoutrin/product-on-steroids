---
name: summarize-meeting
description: >
  Extract and structure meeting outcomes into decisions, action items, and open
  questions with clear ownership and deadlines. Use when processing meeting
  transcripts, creating meeting notes, writing meeting minutes, or recapping
  discussions to keep teams aligned and accountable.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a95b427e70e258b51389796367c6f684e7d
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/summarize-meeting/template.md
---

# Summarize Meeting

## Purpose
Transform raw meeting transcripts, recordings, or notes into a structured summary
that captures decisions, key discussion points, action items with clear ownership,
and open questions — keeping teams aligned and accountable across meetings.

**When NOT to use:** structured team retrospectives (use `retrospective-prep`),
customer interview synthesis (use `summarize-interview`), or post-mortems (use
`pre-mortem` for pre-planning or a custom reflection for post-incident analysis).
Meeting summaries are for internal product/org meetings where decisions ripple
across the team; this skill handles that, not customer discovery or incident
reflection.

## Inputs
- **Required:** meeting transcript, recording notes, or raw discussion text.
  If only a meeting title is given, ask for the actual content before
  summarizing; do not fabricate discussion points.
- **Optional:** list of participants (names + roles), meeting date/time, agenda
  items, or known decisions/concerns to highlight. If not provided, infer from
  transcript; flag any you are uncertain about.

## Output Contract
The deliverable is a **meeting summary memo** with these sections (see
`template.md`):

1. **Date & Time** — meeting date, start and end time (if available).
2. **Participants** — attendee names and roles (inferred from transcript or
   provided).
3. **Topic** — short title of what the meeting was about.
4. **Summary** — 3–5 key discussion points or decisions (bullet points, prose).
5. **Decisions Made** — list of decisions, each actionable and linked to who
   owns follow-up.
6. **Action Items** — table with Due Date, Owner, and Action; sorted by due
   date; every action has an owner and date or a clear blocklist reason.
7. **Open Questions** — unresolved topics, blockers, or needs for follow-up
   meetings.

Format: markdown. Length: ~1–2 pages. Tone: objective, collaborative ("we"),
clear ownership. Every action item must name an owner; if no owner was assigned
in the meeting, note that as a blocker in Open Questions.

**GOOD (excerpt):**
> **Decision:** Pause feature X until Q3 to focus engineering on performance.
> Owned by: CTO. Triggers: retrospective on Q1 launch learnings (due June 15).
>
> **Action Item:**
> | Due Date | Owner | Action |
> |----------|-------|--------|
> | June 15 | Sarah (PM) | Run retrospective session; share 3-point learnings doc to team Slack. |
> | June 20 | Engineering Lead | Review learnings and propose Q2 sprint focus. |
>
> **Open Question:** Do we pause customer onboarding requests during the pause,
> or continue light intake? Marketing to revisit next meeting.

**BAD (excerpt):**
> "We talked about X, Y, and Z and decided to do some stuff. People should work
> on things."
> — fails: no specific decisions, no clear action items, no owner, no date, no
> followthrough.

## Process
1. **Gather content** — read the transcript, recording notes, or text provided.
   If sparse, ask for more context before proceeding.
2. **Identify participants and their roles** — infer from transcript or use any
   names provided. Flag if a role is unclear.
3. **Extract key discussion points** — scan for: main topic, sub-topics, areas
   of agreement/tension, alternatives discussed.
4. **Identify decisions** — list what was decided, who owns the follow-up, and
   any conditional logic ("If X, then Y").
5. **Extract action items** — capture: action, owner, due date. If no date or
   owner was named, flag it as blocker in Open Questions.
6. **Capture open questions** — what remains unresolved, needs revisiting, or
   was deferred to a later meeting.
7. **Run the Quality Bar** — confirm every action has an owner and date (or a
   note why not), decisions are explicit, tone is objective. Revise if any
   item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Meeting date, time (if available), and participant names and roles are
      recorded.
- [ ] Topic is a short, clear title (not a list or vague phrase).
- [ ] Summary captures 3–5 key points in accessible language; no jargon without
      explanation.
- [ ] Every decision is explicit and tied to a follow-up action or ownership.
- [ ] Action items table has three columns (Due Date, Owner, Action); every row
      has an owner and date OR a note in Open Questions explaining why.
- [ ] Open Questions lists unresolved topics, blockers, or deferred items; if
      an action item has no owner/date, it is listed here.
- [ ] Tone is objective and collaborative (no personal opinions; use "we"
      language).
- [ ] If written to a file, it follows `template.md` — all 7 sections present,
      in order, headings matching (skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `summarize-meeting-happy` (happy path) — transcript with clear decisions,
  action items, and owners; guards against loose summaries.
- `summarize-meeting-edge` (edge) — meeting with conflicting viewpoints or
  deferred decisions; skill must surface tensions and open questions.
- `summarize-meeting-adversarial` (adversarial) — sparse or rambling transcript;
  skill must ask for clarity or flag blockers rather than fabricate ownership.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `retrospective-prep` — structured team reflection on process/outcomes; distinct
  from meeting summaries (which capture what was decided in the moment).
- `summarize-interview` — customer interview synthesis; distinct from internal
  meeting summaries (which focus on decisions and action items, not customer
  insights).
- `pre-mortem` — prospective risk analysis; meeting summaries document what was
  decided, pre-mortems explore what could go wrong before building.

### External Frameworks
- Google re:Work, "Manager's Guide to Effective Meetings" — decision ownership and
  action-item clarity as guardrails for meeting efficacy.
- Radical Candor (Kim Scott) — actionable feedback and clear ownership in team
  meetings.
- The Eisenhower Matrix (Urgent/Important) — prioritizing action items by
  deadline and impact.
