# pm-influence — Plugin Proposal

*The Influencing People quadrant: Managing Up · Team Leadership · Stakeholder Management. Almost entirely original (only `stakeholder-map` imports), and the highest-value plugin because these skills produce the documents you actually send — so the Output Contract is the whole game.*

Date: 2026-08-05 · Owner: Jeremie

## Shape: 10 core skills + 1 situational

| # | Skill | Sub-competency | Source | Artifact it produces |
|---|---|---|---|---|
| 1 | stakeholder-map | Stakeholder Mgmt | IMPORT (phuryn) + elevate | Roster + 2 grids + per-quadrant plan |
| 2 | stakeholder-engagement-plan | Stakeholder Mgmt | GENERATE | 1-page brief for ONE critical stakeholder |
| 3 | alignment-narrative | Stakeholder Mgmt | GENERATE | 1–2 page narrative to align cross-functional teams |
| 4 | raci-decision-rights | Stakeholder Mgmt | GENERATE | RACI + decision-rule table |
| 5 | exec-update | Managing Up | GENERATE | Recurring leadership status |
| 6 | decision-memo | Managing Up | GENERATE | 1-page decision doc for sign-off |
| 7 | incoming-request-advisor | Managing Up | GENERATE (dean idea) | Decode of an incoming ask + suggested reply |
| 8 | managing-up-brief | Managing Up | GENERATE | Pre-1:1 / skip-level prep |
| 9 | escalation | Team Leadership | GENERATE | Tight escalation message |
| 10 | feedback-note | Team Leadership | GENERATE | SBI feedback/recognition note |
| +1 | executive-onboarding-playbook | Team Leadership | GENERATE (dean idea) | 30-60-90 diagnostic *(situational, P3)* |

Note the balance: Stakeholder Mgmt 4 · Managing Up 4 · Team Leadership 2 (+1). Team Leadership is deliberately lean — it's the most org-specific, so I'd rather define fewer, well-tailored ones (see "What I need from you").

---

## Each skill, to the standard (Output Contract + Quality Bar + a sample eval)

### 1. stakeholder-map  *(IMPORT + elevate)*
**When:** launching an initiative; before an engagement plan.
**Output Contract:** (a) roster table — *name · role · power H/M/L · interest H/M/L · current stance (Blocker/Skeptic/Neutral/Supporter/Champion) · what they want · what you need from them*; (b) two grids — Power×Interest and Support×Influence; (c) engagement strategy per quadrant (Manage closely / Keep satisfied / Keep informed / Monitor).
**Quality Bar:** every stakeholder has a stance *and* a "what they want"; each quadrant strategy is specific, not generic. **Absorbs** dean `stakeholder-identification`.
**Eval scenario:** initiative + 8 named stakeholders → correct quadrant placement and a *differentiated* strategy per quadrant (fails if strategies are interchangeable).

### 2. stakeholder-engagement-plan  *(GENERATE)*
**When:** one critical or resistant stakeholder needs winning over before a decision.
**Output Contract:** their goals & fears · your specific ask · 2–3 likely objections *with* a concrete response each · channel & timing · a one-line opening message.
**Quality Bar:** at least one *real* objection (not a strawman) with a specific counter; a concrete channel + timing, not "set up a meeting."
**Eval:** resistant CFO stakeholder → surfaces a budget/risk objection and a specific, evidence-based counter.

### 3. alignment-narrative  *(GENERATE — net-new)*
**When:** cross-functional teams disagree or drift; you need one shared version of the direction. (Amazon 6-pager, lite.)
**Output Contract:** *prose narrative, 1–2 pages, deliberately no bullets* — Situation → Why now → The decision → Why this over the alternatives → What it means for each team → What we need.
**Quality Bar:** states one clear decision; names the rejected alternatives and why; spells out per-team implications.
**Eval:** two competing roadmap visions → narrative that commits to one, explains the trade, and says what each of eng/design/sales must do.

### 4. raci-decision-rights  *(GENERATE — net-new)*
**When:** ownership is fuzzy; decisions stall or get re-litigated.
**Output Contract:** RACI matrix (rows = key decisions/deliverables; cols = roles) + an explicit "decision rule" line per row (who decides, who's consulted, escalation path).
**Quality Bar:** exactly **one** Accountable per row; no row that is all-Consulted; an escalation path exists.
**Eval:** a launch with 5 decisions → valid RACI (single A per row) + a usable escalation path.

### 5. exec-update  *(GENERATE — net-new)*
**When:** recurring status to leadership (weekly/monthly).
**Output Contract:** TL;DR (≤1 sentence + status color) · Progress vs goals · Metrics moved · Risks/blockers *each with an owner and an ask* · Decisions needed · Next. Length ≤ one screen.
**Quality Bar:** TL;DR is one sentence; ≥1 quantified metric; every risk carries an owner *and* a specific ask; no wall of prose.
**Eval:** messy status dump → scannable update where each risk has an owner+ask and the TL;DR reads in 3 seconds.

### 6. decision-memo  *(GENERATE — net-new)*
**When:** you need an exec/steering decision.
**Output Contract:** The decision being asked · Context (why now) · Options (2–4, each with pros/cons/cost) · Recommendation + rationale · Risks · The ask + who approves + by when.
**Quality Bar:** ≥2 genuine options with trade-offs; a single clear recommendation; an explicit approver and deadline.
**Eval:** build-vs-buy question → memo with 2–3 real options and one decisive recommendation + a dated ask.

### 7. incoming-request-advisor  *(GENERATE — dean idea)*
**When:** before replying to a loaded ask from an exec/stakeholder.
**Output Contract:** the literal ask · the job-to-be-done behind it · what's *really* being evaluated · urgency read · what to clarify first · a suggested reply.
**Quality Bar:** separates literal ask from JTBD; flags the missing info you'd need before committing.
**Eval:** "Can you get feature X done by Friday?" → decodes the real driver (a customer/exec commitment) and proposes a clarifying reply, not a yes/no.

### 8. managing-up-brief  *(GENERATE — net-new)*
**When:** prepping a 1:1 or skip-level with your manager/exec.
**Output Contract:** what to surface (wins + risks) · decisions to extract · calibrated questions to ask them · support/resources to request · framing for each.
**Quality Bar:** ≥1 explicit ask and ≥1 genuine question (not a status recital).
**Eval:** a stalled initiative → brief that turns the 1:1 into getting a decision + unblocking resource, not a progress readout.

### 9. escalation  *(GENERATE — net-new)*
**When:** blocked and you need someone senior to act.
**Output Contract:** what's blocked + quantified impact ($ / date / users) · what you've already tried · options · the specific decision/help needed · from whom · by when.
**Quality Bar:** impact is quantified; a named owner and a deadline; calm, non-blaming tone.
**Eval:** a dependency slipping → escalation with dollarized/dated impact and a specific named ask, no finger-pointing.

### 10. feedback-note  *(GENERATE — net-new)*
**When:** giving a team member/peer feedback or recognition.
**Output Contract:** SBI structure — Situation · Behavior (observable) · Impact · then one clear forward ask/encouragement.
**Quality Bar:** concrete situation + observable behavior (no vague adjectives like "great job"); one specific ask.
**Eval:** raw "they did well in the review" → an SBI note a manager could send verbatim.

### +1. executive-onboarding-playbook  *(GENERATE — situational, P3)*
30-60-90 diagnostic for entering a new product role/team. Output: phased plan (listen → diagnose → first bets) with per-phase goals and anti-patterns (don't reorg in week 2).

---

## Cross-cutting reuse
All the interactive ones (stakeholder-map, engagement-plan, managing-up-brief) import the shared **`workshop-facilitation`** protocol so the guided Q&A feels consistent across the marketplace.

## Integration angle (you have Notion + Slack connected)
`exec-update`, `decision-memo`, and `alignment-narrative` are natural **Notion** outputs (create the page in the right database) and **Slack**-shareable summaries. Worth wiring once the skills exist so the artifact lands where your stakeholders already look.

## What I need from you to tailor this (this plugin lives or dies on fit)
1. **exec-update** — cadence (weekly/bi-weekly/monthly), channel (Notion page / Slack / email / deck), and any status-color or section conventions your orgs use.
2. **Decision model** — RACI, or DACI/other? Any standing "decision doc" template your clients expect?
3. **Team Leadership scope** — is it leading the *cross-functional squad* (rituals, decisions) or also *people management* (growth, performance)? That decides whether we add e.g. a `1:1-cadence` or `team-operating-principles` skill.
4. Anything from the deanpeters career-transition set (director/VP-CPO readiness) you actually want — otherwise it stays deferred.
