---
name: incoming-request-advisor
description: >
  Helps a PM handle an incoming stakeholder request diplomatically — deciding
  whether to accept, defer, redirect, or decline it, and how to communicate
  that decision without damaging the relationship. Use when a stakeholder asks
  you to add a feature, reprioritize the roadmap, take on extra scope, or
  requests something you suspect is off-strategy.
version: 0.1.0
type: interactive
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/incoming-request-advisor/template.md
---

# Incoming Request Advisor

## Purpose
Produce a **response plan** for a specific incoming stakeholder request — covering
the PM's recommended disposition (accept / conditionally accept / defer / redirect /
decline), the rationale grounded in strategy and data, and the exact language to
use in the reply so the relationship stays intact regardless of the answer.

This skill is reactive: it handles the moment a request lands. It focuses on
triage, interpersonal navigation, and communication drafting, not on ongoing
relationship management or proactive outreach.

**When NOT to use:**
- Planning proactive stakeholder outreach → use `stakeholder-engagement-advisor`.
- Driving a binary strategic decision that requires exec sign-off → use `decision-memo`.
- Building a shared narrative across a stakeholder group before a big initiative →
  use `alignment-narrative`.
- The request is clearly in-scope and you just need to say yes — no advisor needed;
  a simple acknowledgement suffices.

## Inputs
- **Required:** a description of the incoming request — who is asking, what they
  want, and by when. If any of these three are missing, ask before continuing.
- **Required:** the current product strategy or priorities (even a one-sentence
  summary). Without this, the skill cannot ground the disposition in strategy.
- **Optional:** the stakeholder's seniority and relationship context (peer, skip
  manager, key customer, external partner). Affects tone and escalation risk.
- **Optional:** any prior commitments or history with this stakeholder. Affects
  how much latitude exists in the response.
- **Optional:** urgency or hard deadline on the request. If absent, assume
  standard planning cadence.

If required inputs are missing, ask for them one at a time — start with "Who is
making this request and what exactly are they asking for?" before surfacing the
strategy question.

## Output Contract
The deliverable is an **incoming-request response plan** (see `template.md`):

1. **Request Summary** — a neutral one-paragraph restatement of the request, the
   stakeholder, and any stated urgency. Surfaces hidden assumptions in the ask.
2. **Disposition** — one of: Accept / Conditionally Accept / Defer / Redirect /
   Decline. Includes a single-sentence rationale for why this disposition fits.
3. **Strategic Rationale** — two to four bullet points connecting the disposition
   to strategy, roadmap priorities, capacity, or customer data. Each bullet is a
   falsifiable claim, not a vague assertion.
4. **Investigation Checklist** — the three to five questions the PM should answer
   before finalizing the response (e.g., data to pull, stakeholders to consult).
   Only included if more information is needed; omit if disposition is clear.
5. **Draft Reply** — the actual message to send, in the PM's voice. Empathetic
   opener, clear disposition, brief rationale, next step. No jargon. Length: 80–
   150 words for async messages; shorter for in-person talking points.
6. **Bridge-Preservation Notes** — one or two specific actions the PM can take to
   maintain goodwill even when declining or deferring (e.g., offer a 15-min call,
   loop them into a future planning cycle, acknowledge their team's pain).

Format: prose + one draft reply block. Total length: one page or less.

**GOOD (excerpt):**
> **Disposition:** Defer — the request is legitimate but competes with a committed
> Q3 milestone; scheduling it now would slip the existing delivery.
>
> **Draft Reply:**
> "Thanks for flagging this, [Name] — I can see why it feels urgent given the
> complaints you're hearing. We're locked into delivering [X] by end of Q3; I'd
> like to propose we revisit this in our Q4 planning session, which starts
> [date]. I'll add it to the agenda myself and send you a calendar invite so you
> know it won't fall through the cracks. Does that work for you?"

**BAD (excerpt):**
> "We can't do that right now because of the roadmap."
> — fails: no empathy, no rationale, no next step, and it burns the relationship
> without preserving a bridge.

## Process
1. **Clarify** — if required inputs are missing, ask for them before proceeding.
2. **Restate the request** — write the Request Summary neutrally; surface any
   hidden assumptions or unstated urgency in the ask.
3. **Assess fit** — compare the request against stated strategy and current
   priorities. Is it in-scope, adjacent, or clearly off-strategy?
4. **Check capacity and commitments** — would accepting slip an existing
   commitment? Is there a more appropriate owner?
5. **Choose a disposition** — pick the single best disposition and make the
   rationale explicit. If the fit is genuinely ambiguous, name that; do not
   default to Defer to avoid conflict.
6. **Build the investigation checklist** — only if decision uncertainty remains;
   name the minimum facts needed before committing.
7. **Draft the reply** — open with acknowledgement, state the disposition and
   why, name the concrete next step, close warmly. Keep it short.
8. **Add bridge-preservation notes** — identify the one or two specific actions
   that turn a disappointing answer into a relationship investment.
9. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] A disposition is explicitly named (Accept / Conditionally Accept / Defer /
      Redirect / Decline) — not hedged or left open.
- [ ] The strategic rationale contains falsifiable claims, not just vague alignment
      language ("this doesn't fit our strategy" is not enough).
- [ ] The draft reply opens with genuine acknowledgement of the stakeholder's
      perspective before stating the decision.
- [ ] The draft reply names a concrete next step — not just "let's revisit."
- [ ] Bridge-Preservation Notes are specific and actionable, not generic advice
      like "be empathetic."
- [ ] The tone of the draft reply matches the stated relationship and seniority of
      the stakeholder (a skip-manager gets a different tone than a peer).
- [ ] If the output is written to a file, it follows `template.md` (a skill-scoped
      hook re-checks this on write).

## Validation & Eval
Scenario cards live in `evals/`:
- `incoming-request-advisor-happy` (happy path) — a clear, off-roadmap request
  from a respected peer with enough context to produce a Defer disposition and
  a full draft reply.
- `incoming-request-advisor-edge` (edge) — a request from a senior executive with
  political risk; tests whether the skill handles seniority gradient without
  capitulating on strategy.
- `incoming-request-advisor-adversarial` (adversarial) — an under-specified ask
  where the PM is also suspected of avoiding the conversation; the skill must
  elicit missing inputs and name the avoidance risk.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `stakeholder-engagement-advisor` — for proactive outreach planning; the
  bridge-preservation actions from this skill often feed the next engagement plan.
- `alignment-narrative` — builds shared understanding across a group before a big
  initiative; complements this skill when a recurring request reveals a narrative gap.
- `decision-memo` — when the incoming request escalates to a formal go/no-go that
  needs exec sign-off; this skill produces the response plan, not the decision doc.
- `stakeholder-map` — use to understand the stakeholder's influence and interest
  level before choosing tone and disposition.

### External Frameworks
- Roger Fisher & William Ury, *Getting to Yes* (1981) — principled negotiation;
  the "separate people from the problem" principle underpins the empathetic-opener
  pattern in the draft reply.
- Chris Voss, *Never Split the Difference* (2016) — tactical empathy and labeling;
  informs the acknowledgement-first structure of the draft reply.
- David Maister, Charles Green & Robert Galford, *The Trusted Advisor* (2000) —
  the trust equation (credibility + reliability + intimacy / self-orientation)
  grounds the bridge-preservation discipline.
