---
name: decision-memo
description: >
  Use when you need async sign-off on a specific decision without scheduling a
  meeting, when you are escalating a choice to a stakeholder who needs context
  fast, or when you want to pre-align a team around a recommendation before it
  is ratified.
version: 0.1.0
type: component
source: original
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/decision-memo/template.md
---

# Decision Memo

## Purpose
Produce a concise, self-contained memo that drives a single, well-scoped decision
asynchronously. The memo frames the question being posed, presents two to four
options with explicit trade-offs, makes a clear recommendation, and states exactly
who must decide, what they are approving, and by when. The reader should be able
to act — approve, counter, or request more information — without attending a meeting.

**When NOT to use:**
- Status updates or progress reporting — use `exec-update` instead.
- Prep material for a live conversation — use `managing-up-brief`.
- Building shared understanding over time without forcing a choice — use `alignment-narrative`.
- Clarifying who owns which class of decisions in general — use `raci-decision-rights`.
- Exploratory decisions that require discovery before framing options — gather
  data first, then use this skill once the option set is known.

## Inputs
- **Required:** the specific decision to be made — what question is being put to
  the reader. If the user states a vague topic rather than a crisp question (e.g.,
  "pricing strategy" vs. "Should we move to usage-based pricing for the growth tier
  by Q3?"), ask them to sharpen it before continuing.
- **Required:** the two to four options under consideration — at minimum their
  labels and the key trade-off each represents. If the user has not thought these
  through, prompt them to articulate options before drafting.
- **Required:** the recommended option and the one-sentence rationale.
- **Required:** the decision owner(s) — name or role — and the deadline for a
  response.
- **Optional:** relevant context (background, constraints, prior decisions that
  narrow the space). Default: derive from the options and recommendation.
- **Optional:** risks if the deadline is missed or the decision is deferred. Default:
  flag deferral cost only if it is obvious from context.
- **Optional:** supporting data, metrics, or quotes. Default: do not fabricate;
  note what data is missing and how it could be collected.

## Output Contract
The deliverable is a **decision memo** (see `template.md`), structured as:

1. **Header block** — memo date, subject (the decision question, one sentence),
   author, decision owner(s), and response deadline.
2. **Situation** — two to four sentences of context: what has changed or what
   pressure is creating the need for this decision now. No background lecture;
   only what is load-bearing for the options.
3. **Complication** — one to two sentences: the tension, constraint, or trade-off
   that makes this a real decision rather than an obvious call.
4. **Options** — two to four labeled options. For each: a one-line description,
   the key benefit, the key cost or risk, and a confidence rating (high/med/low)
   in the data supporting that assessment.
5. **Recommendation** — the preferred option, stated unambiguously, with the
   primary reasoning in two to four sentences. Flag the one assumption that, if
   wrong, would change the recommendation.
6. **Decision requested** — a crisp call-to-action: what the reader is being
   asked to approve, counter, or decide; who else (if anyone) is cc'd and why;
   and the response-by date.
7. **If deferred** — one sentence on what happens to scope, cost, or timeline if
   no decision is made by the deadline (omit if the cost of deferral is zero).

Format: plain prose with a header table and an options comparison. Length: half
a page to one page. No jargon. Every claim is either cited or labeled an
assumption.

**GOOD (excerpt):**
> **Recommendation:** Adopt Option B — a 14-day grace period before hard paywall.
> This balances conversion (our 30-day cohort data shows 68% of paid converts
> engage on days 8–14) against the revenue risk of extending free access. The
> critical assumption is that the grace period does not materially suppress urgency;
> if day-14 conversion drops below 4%, revert within 30 days.
>
> **Decision requested:** Approve Option B for the July 1 rollout. Response needed
> by June 20. No response by June 20 = we default to Option A (status quo).

**BAD (excerpt):**
> "We have several options and should discuss them at the next team meeting to
> decide what makes the most sense for the business."
> — fails: defers the decision rather than driving it, names no owner, states no
> deadline, and contains no recommendation.

See `template.md` for the fill-in structure.

## Process
1. **Sharpen the question** — confirm the decision is specific and bounded (one
   choice, one scope, one time horizon). If the user gives a broad topic, reframe
   it as a yes/no or option-A/B/C question before proceeding.
2. **Frame the Situation and Complication** — apply McKinsey SCQA: Situation
   (what is true now), Complication (what has changed or what tension exists),
   Question (the decision), Answer (the recommendation). Write sections 2 and 3
   from S and C.
3. **Build the options table** — for each option: label, one-line description,
   primary benefit, primary cost or risk, confidence in the supporting data. Do
   not stack the options unfairly; present each on its best terms.
4. **State the recommendation** — pick one option. If you genuinely cannot
   recommend one, say so and explain what information would break the tie — but
   do not present a memo without a recommendation unless the user explicitly wants
   an options-only brief.
5. **Write the decision request** — name the owner, state what approval looks like
   (a reply? a calendar invite? a Jira ticket?), and set the deadline.
6. **Add the deferral cost** — if missing the deadline has a real cost (a sprint
   starts, a contract lapses, a competitor ships), name it in one sentence.
7. Run the Quality Bar; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] The subject line states the decision as a question or choice, not a topic.
- [ ] There are two to four distinct options; none is a strawman inserted only to be rejected.
- [ ] Each option has an explicit benefit AND an explicit cost or risk.
- [ ] A single option is recommended, stated unambiguously.
- [ ] The recommendation names the one assumption whose failure would change it.
- [ ] A specific decision owner (name or role) and response deadline are stated.
- [ ] No unsupported factual claims — every number is cited or labeled an assumption.
- [ ] Length is half a page to one page; no jargon; no meeting-scheduling language.
- [ ] If the output is written to a file, it follows `template.md` — all 7 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `decision-memo-happy` — well-specified pricing decision with clear options and data.
- `decision-memo-edge` — decision owner is a group, deadline pressure is extreme,
  and the right answer requires flagging missing data rather than fabricating a
  recommendation.
- `decision-memo-adversarial` — user asks for a "decision memo" but the input is
  a vague topic with no options and no owner; the skill must scope it down before
  drafting.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `exec-update` — status reporting to leadership; does not drive a choice.
- `managing-up-brief` — synchronous conversation prep; use when a meeting is
  unavoidable and the memo alone is insufficient.
- `alignment-narrative` — builds shared understanding over time; use when the
  goal is belief change, not a single ratified choice.
- `raci-decision-rights` — clarifies who owns which category of decisions;
  upstream to this skill when decision authority is genuinely unclear.

### External Frameworks
- Barbara Minto, *The Pyramid Principle* (1987) — SCQA structure (Situation,
  Complication, Question, Answer) that drives sections 2–3 and ensures the memo
  leads with the answer rather than burying it.
- Amazon 6-pager / Working Backwards — narrative-first, data-backed memo culture
  that rejects slide decks; the decision memo is the single-decision variant of
  this discipline.
- Roger Martin, *The Opposable Mind* (2007) — integrative thinking and option
  framing: options should be genuinely distinct, each argued on its best terms,
  before a recommendation collapses them.
