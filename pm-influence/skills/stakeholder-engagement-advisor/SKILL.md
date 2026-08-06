---
name: stakeholder-engagement-advisor
description: >
  Use when you have a stakeholder map (or a list of stakeholders) and need a
  concrete engagement plan — who to communicate with, how, how often, and in
  what order — to build support, reduce resistance, or maintain alignment for a
  product initiative.
version: 0.1.0
type: workflow
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/stakeholder-engagement-advisor/template.md
---

# Stakeholder Engagement Advisor

## Purpose
Given a stakeholder map or a roster of key stakeholders for a product initiative,
produce a **Stakeholder Engagement Plan** — a structured, actionable playbook
that specifies *how* to engage each stakeholder: the right channel, message
framing, frequency, and sequencing to build support and reduce friction over the
life of the initiative.

The plan goes beyond the map: it prioritises stakeholders by influence and
stance, selects engagement tactics tailored to each person's motivations and
communication preferences, and sequences outreach so that wins with early
champions unlock harder conversations later.

**When NOT to use:**
- You need to *discover* who the stakeholders are — use `stakeholder-identification`.
- You need to *map* influence, interest, and stance — use `stakeholder-map`.
- You need to *draft* a specific narrative or announcement — use `alignment-narrative`.
- The initiative is already approved and you just need a recurring status-update
  cadence — use `exec-update` or `managing-up-brief`.

## Inputs
- **Required:** a stakeholder list or map — at minimum: name/role, their stance
  (supporter, neutral, blocker), and their estimated influence on the initiative.
  If not provided, ask for these three attributes per stakeholder before proceeding.
- **Required:** a brief description of the initiative — what it is, what decision
  or outcome you need from stakeholders, and the rough timeline.
- **Optional:** known communication preferences (channel, meeting frequency, preferred
  format) per stakeholder — incorporate when supplied; infer sensible defaults otherwise.
- **Optional:** existing relationships or prior friction points — use to calibrate tone
  and sequencing.
- **Optional:** explicit constraints (e.g., "the CTO must not hear about this before
  the VP of Product") — honour as hard sequencing rules.

## Output Contract
The deliverable is a **Stakeholder Engagement Plan** structured as (see `template.md`):

1. **Initiative Summary** — one-paragraph recap of the initiative, the desired
   stakeholder outcomes, and the plan's time horizon.
2. **Stakeholder Roster** — a table with columns: Name/Role · Influence · Stance ·
   Primary Goal / Concern · Engagement Priority (H/M/L).
3. **Engagement Playbook** — one subsection per stakeholder (or per stakeholder
   cluster when stance and influence are similar), each covering:
   - **Channel & format** — e.g., 1:1 Slack, steering-committee slide, async doc, coffee chat
   - **Frequency & timing** — e.g., biweekly check-in; brief before each key milestone
   - **Message framing** — the core "what's in it for them" angle and any framing to avoid
   - **Ask / call to action** — what you specifically need from them at each touchpoint
4. **Sequencing Map** — a numbered engagement sequence (who first, who second, …) with
   the rationale for the order — i.e., which early supporters unlock later hard conversations.
5. **Resistance & De-risking** — for each blocker or likely resister: root-cause hypothesis,
   de-escalation tactic, and escalation path if the tactic fails.
6. **Cadence Snapshot** — a compact calendar view (weekly or monthly grid) showing
   planned touchpoints across all stakeholders for the next 4–8 weeks.
7. **Success Indicators** — two or three observable signals that engagement is working
   (e.g., "VP Engineering stops raising scope concerns in steering meetings").

Format: structured prose + tables. Length: 2–4 pages. Every engagement tactic must
be grounded in the stakeholder's stated or inferred motivation — not generic advice.

**GOOD (excerpt):**
> **Maria Chen — VP Engineering (Blocker, High Influence)**
> *Channel:* Biweekly 30-min 1:1 (her preference); avoid large group settings until aligned.
> *Framing:* Lead with technical debt reduction — her primary concern. Show how the initiative
> retires two legacy integrations she flagged in Q3 planning. Avoid "velocity" language (she
> associates it with cutting corners).
> *Ask (first 2 weeks):* One working-session to walk her through the technical approach and
> capture her objections. Goal: surface blockers early, not lobby for approval.

**BAD (excerpt):**
> "Engage Maria regularly and keep her updated on progress."
> — fails: no channel, no framing tied to her concerns, no concrete ask, no frequency,
> and does not reflect that she is a blocker requiring active de-escalation.

## Process
1. **Intake** — confirm the initiative description, timeline, and stakeholder list.
   If stance or influence is missing for any stakeholder, ask or propose a working
   assumption explicitly.
2. **Segment stakeholders** — group by influence × stance into four zones:
   - *Champions* (high influence, supporter) — leverage for social proof and sequencing.
   - *Governors* (high influence, neutral/blocker) — highest priority; must be addressed early.
   - *Allies* (lower influence, supporter) — activate for grassroots momentum.
   - *Monitors* (lower influence, neutral/blocker) — address last or via broadcast.
3. **Determine engagement mode per stakeholder** — choose 1:1 depth vs. group setting,
   synchronous vs. async, and the appropriate artifact (slide, doc, data pull, demo, coffee).
4. **Frame messages per motivation** — identify each stakeholder's primary goal or concern
   and anchor every message to it. Note any language or framing to avoid.
5. **Design the sequence** — order outreach so champions are aligned before you approach
   governors; use their endorsement to reduce governor resistance. Honour any explicit
   ordering constraints.
6. **Plan resistance responses** — for each blocker, hypothesize the root cause (fear of
   workload, loss of control, strategic disagreement, etc.) and match a targeted tactic.
7. **Build the cadence** — map all touchpoints onto a 4–8 week calendar, ensuring no
   stakeholder gap exceeds what their influence level warrants.
8. **Define success signals** — name two or three observable indicators that the engagement
   is shifting stance in the right direction.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every stakeholder in the input appears in the Stakeholder Roster with influence,
  stance, and engagement priority assessed.
- [ ] Each stakeholder (or cluster) in the Playbook has a named channel, a concrete
  frequency/timing, a motivation-grounded message framing, and a specific ask.
- [ ] Blockers each have a root-cause hypothesis and a de-escalation tactic — not just
  "keep them informed."
- [ ] The Sequencing Map includes an explicit rationale for the order (who unlocks whom).
- [ ] Success Indicators are observable and specific, not vague ("stakeholders feel
  engaged" is not acceptable).
- [ ] No engagement tactic is purely generic — each must reference the stakeholder's
  stated or inferred concern or preference.
- [ ] If the output is written to a file, it follows `template.md` — all 7 sections
  present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `stakeholder-engagement-advisor-happy` (happy path) — a product initiative with a
  clear stakeholder map including champions, neutrals, and one blocker.
- `stakeholder-engagement-advisor-edge` (edge) — sparse input: stakeholder list with
  minimal context; skill must surface working assumptions and still produce a usable plan.
- `stakeholder-engagement-advisor-adversarial` (adversarial) — user provides only the
  initiative name and asks for a generic "stakeholder engagement template"; skill must
  decline to produce a generic plan and ask for the minimum required inputs.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `stakeholder-identification` — discovers who the stakeholders are; this skill engages them.
- `stakeholder-map` — produces the influence/stance map this skill consumes as input.
- `alignment-narrative` — drafts the specific narrative or announcement; this skill decides
  when and how to deliver it.
- `exec-update` — handles recurring executive status updates once engagement is established.
- `managing-up-brief` — frames upward communication; pairs with this skill's "managing up"
  touchpoints for senior stakeholders.

### External Frameworks
- Mendelow's Power–Interest Matrix (1991) — the canonical 2×2 for segmenting stakeholders
  by influence and interest; underpins the four-zone segmentation in the Process above.
- Roger Fisher & William Ury, *Getting to Yes* (1981) — principled negotiation and
  interests-over-positions framing that informs the motivation-grounded message framing step.
- John Kotter, *Leading Change* (1996) — the "guiding coalition" model, which motivates
  the sequencing logic: win champions first to create social proof for governors.
- PMI, *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)*, Chapter 13:
  Stakeholder Engagement — industry-standard taxonomy of engagement levels
  (unaware → resistant → neutral → supportive → leading) used to assess stance progression.
