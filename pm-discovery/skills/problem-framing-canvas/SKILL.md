---
name: problem-framing-canvas
description: >
  Use when a team needs to deeply explore a problem space before committing to
  solutions — sprint kickoffs, discovery workshops, alignment sessions where
  stakeholders disagree on what the problem actually is, or when a team is
  jumping to solutions without shared understanding of the problem.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/problem-framing-canvas/template.md
---

# Problem Framing Canvas

## Purpose
Produce a nine-block Problem Framing Canvas — a structured workshop artifact
that maps the full problem space (who is affected, the evidence, current
workarounds, business impact, success metrics, constraints, and open questions)
before any solution is considered. Supports sprint kickoffs, discovery
workshops, and alignment sessions where the team needs shared understanding of
*what problem we are actually solving* before discussing *how*.

**When NOT to use:** writing a concise, ready-to-ship problem statement for a
doc (use `problem-statement`); planning the overall arc of a discovery sprint
(use `discovery-process`); exploring the solution space or framing hypotheses
(use `lean-ux-canvas`); or when the team already has a well-understood problem
and only needs to validate a specific solution direction.

## Inputs
- **Required:** a rough description of the problem area — even "we think
  checkout is broken for mobile users" is enough to start. If the team cannot
  articulate even this, run the `discovery-process` skill first to scope the
  arc.
- **Optional:**
  - Existing research artifacts (user interviews, support tickets, analytics)
    — surface them in the Evidence block rather than inventing data.
  - Stakeholder perspectives or team disagreements — especially useful; record
    them as Open Questions if not yet resolved.
  - Scope boundaries (time, platform, user segment) — pre-populate Constraints.
  - Desired success metrics — pre-populate the Success Metrics block if the
    team already has hypotheses.

## Output Contract
The deliverable is a **Problem Framing Canvas** — a nine-block multi-section
artifact (see `template.md`):

1. **Problem** — one to three sentences on what is going wrong, in user/system
   terms. Not a solution, not a cause — the observable symptom.
2. **Who Is Affected** — the user segments or stakeholders experiencing the
   problem, with distinguishing characteristics. At least one primary segment.
3. **Context** — the when, where, and why the problem occurs. Workflow step,
   trigger conditions, platform, frequency.
4. **Evidence** — quantitative data, qualitative quotes, and direct observations
   that confirm the problem is real and significant. Must include at least one
   data point; flag gaps explicitly.
5. **Current Workarounds** — how users cope today. Each workaround is a clue
   about JTBD and unmet needs. "None" is a valid answer only if confirmed by
   research.
6. **Business Impact** — why this problem matters to the company: revenue risk,
   retention, support cost, strategic positioning, regulatory exposure.
7. **Success Metrics** — what "problem solved" looks like in measurable terms.
   Lead and lag indicators. Do not conflate with solution features.
8. **Constraints** — what the team cannot change: technical, legal, budget,
   timeline, organizational. Be honest — false constraints waste discovery.
9. **Open Questions** — what the team still does not know. Each question should
   be answerable by a specific research activity. Prioritize by impact on the
   problem frame.

Format: markdown with nine `##` sections. Length: approximately one to two
pages. Evidence and Workarounds may use bullet lists; narrative blocks should
be prose. Every data point in Evidence is cited or flagged as an assumption.

**GOOD (excerpt):**
> **Evidence**
> - 34% of mobile checkout sessions abandoned at the address step (analytics,
>   Q1 2025 — 90-day window, 45k sessions).
> - "I always give up when it asks for my address — the keyboard covers the
>   field and I can't see what I'm typing." — User interview P7, March 2025.
> - Support ticket volume for "can't complete order on phone": 210 tickets/month
>   (Zendesk, Feb–Apr 2025), up 40% YoY.
>
> **Current Workarounds**
> - Switch to desktop to complete the purchase (observed in 12/20 usability
>   sessions).
> - Use the mobile app instead of the web (CS team estimate: ~15% of affected
>   users).

**BAD (excerpt):**
> **Evidence**
> "Users seem frustrated with checkout."
> — fails: no data, no quotes, no source — unverifiable and unactionable.
>
> **Success Metrics**
> "Build a better checkout flow."
> — fails: this is a solution direction, not a measurable outcome. A metric
> answers "how will we know the problem is solved?", not "what will we build?".

## Process
1. **Anchor the problem** — ask for the rough problem description if not
   provided; do not invent scope. Write a first draft of the Problem block.
2. **Map who is affected** — identify primary and secondary segments from the
   context. If the user has research artifacts, extract segments from them.
3. **Set the context** — pin the trigger conditions, workflow step, platform,
   and frequency. Note anything the user is uncertain about as an Open Question.
4. **Surface the evidence** — pull in every data point the user provides.
   Explicitly flag any block that has no evidence yet; do not fill gaps with
   plausible-sounding numbers.
5. **Enumerate workarounds** — ask what users do today when they hit this
   problem. If unknown, flag as an Open Question and note the research activity
   (e.g., "5 usability sessions with segment A").
6. **Quantify business impact** — express impact in terms the company tracks:
   revenue, retention, cost, NPS, strategic. If data is unavailable, estimate
   the order of magnitude and label it an estimate.
7. **Define success metrics** — write outcome-based metrics (rate, volume,
   time) not feature descriptions. Include at least one lead indicator.
8. **State real constraints** — surface technical, legal, budget, and timeline
   constraints the team is working within. Challenge constraints that seem
   assumed rather than confirmed.
9. **Capture open questions** — list every unresolved question that would
   materially change the problem frame. For each, suggest the fastest research
   method to answer it.
10. Run the Quality Bar below; revise any block that fails; then return the
    completed canvas.

## Quality Bar
Before returning, confirm:
- [ ] All nine blocks are present and non-empty (a block may say "None confirmed
  by research" but never left as a placeholder).
- [ ] The **Problem** block describes an observable symptom — it is not a
  solution, a root cause, or a solution-disguised-as-a-problem (e.g., "we need
  to redesign checkout" is a solution, not a problem).
- [ ] **Evidence** contains at least one cited data point (or explicitly flags
  the gap and names the research needed to fill it).
- [ ] **Success Metrics** are outcome-based and measurable — no feature
  descriptions or solution references.
- [ ] **Current Workarounds** are actual observed or reported behaviors — not
  invented, and "None" is backed by research if used.
- [ ] **Open Questions** each have a suggested research activity to answer them.
- [ ] The canvas does not prescribe a solution in any block.
- [ ] If the canvas is written to a file, it follows `template.md` — all nine
  `##` sections present, in order, headings matching (a skill-scoped hook
  re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `problem-framing-canvas-happy` — sprint kickoff for a well-evidenced mobile
  checkout abandonment problem.
- `problem-framing-canvas-edge` — team disagrees on whether the problem is real;
  canvas must surface the disagreement as Open Questions without fabricating
  resolution.
- `problem-framing-canvas-adversarial` — team wants to skip framing and jump to
  solutions; skill must redirect and produce the canvas rather than comply.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `problem-statement` — consumes the Problem block of this canvas and distils
  it into a concise 1–3 sentence written artifact for docs and briefs.
- `discovery-process` — plans the research arc; the canvas is one deliverable
  within that arc, typically produced at the kickoff workshop.
- `lean-ux-canvas` — solution-space counterpart (Jeff Gothelf); use *after* the
  problem frame is locked.

### External Frameworks
- Teresa Torres, *Continuous Discovery Habits* (2021) — opportunity-solution
  tree; problem framing precedes opportunity mapping.
- Marty Cagan, *Inspired* (2017) — the distinction between problem space and
  solution space; the canvas lives entirely in the problem space.
- IDEO / Design Thinking "How Might We" — the framing exercise that follows
  once this canvas is locked; open questions feed directly into HMW generation.
- Jake Knapp, *Sprint* (2016) — Monday mapping exercise; the canvas is a
  pre-sprint artifact that accelerates the Monday map.
