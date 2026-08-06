---
name: prioritization-frameworks
description: >
  Recommend which prioritization framework fits a given decision — RICE, ICE,
  MoSCoW, Kano, WSJF, Value-vs-Effort, or Opportunity Scoring — with the inputs,
  tradeoffs, and failure modes of each. Use when choosing a prioritization
  method, comparing frameworks like RICE vs ICE, deciding how to rank a roadmap,
  or learning how different prioritization approaches work.
version: 0.1.0
type: component
source: import:phuryn/pm-skills@18468a9
hooks:
  PostToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: python3
          args:
            - ${CLAUDE_PLUGIN_ROOT}/scripts/check_output_conformance.py
            - ${CLAUDE_PLUGIN_ROOT}/skills/prioritization-frameworks/template.md
---

# Choose a Prioritization Framework

## Purpose
Recommend **which** prioritization framework fits a specific decision, and explain
how each candidate works, what it needs as input, and where it breaks. Produces a
selection recommendation (a primary framework, when to pair or fall back to another)
so a team stops arguing about *method* and can start scoring. Covers RICE, ICE,
MoSCoW, Kano, WSJF, Value-vs-Effort, and Opportunity (Importance-vs-Satisfaction)
Scoring.

**When NOT to use:** actually **running** a scoring pass on a concrete backlog and
returning a ranked list — that is `prioritize-features`. This skill selects and
teaches the method; it does not rank the user's items. Also not for sequencing an
already-prioritized set into a release plan (that is roadmap/release planning), nor
for OKR/goal-setting. If the user already knows their framework and just wants the
numbers run, hand off to `prioritize-features`.

## Inputs
- **Required:** the **decision being made** and what is being prioritized —
  features/ideas, customer problems, requirements, or personal tasks; plus the
  **granularity/scale** (a handful of bets vs. a large backlog) and **who must buy
  in** (solo PM, squad, or exec stakeholders). If missing, ask which of these
  applies before recommending — the answer changes the recommendation.
- **Optional:** available data (do they have reach numbers, effort estimates,
  customer survey data on importance/satisfaction?), time budget for the exercise,
  whether the goal is *ranking* vs. *understanding expectations*, and any framework
  the team already uses. Absent data, default to the lightest framework the inputs
  can support and name the data that would justify a heavier one.

## Output Contract
The deliverable is a **framework-selection brief** with these sections (see
`template.md`):

1. **Decision framing** — one line: what is being prioritized, at what scale, for whom.
2. **Recommendation** — the **primary** framework, one-sentence why it fits, and a named **fallback/pairing** (e.g. Kano to understand, then RICE to rank).
3. **Candidate comparison table** — the relevant frameworks with columns: *best for*, *inputs needed*, *formula/mechanic*, *key tradeoff / failure mode*.
4. **How to apply the pick** — the formula or mechanic spelled out, the inputs to gather, and the scale to use.
5. **Watch-outs** — the specific ways the recommended framework misleads (false precision, effort gaming, ignoring problems vs. solutions) and how to guard against them.

Format: prose framing + one comparison table. Length: ~1 page. Always name a
concrete pick and a fallback — never "it depends" without a decision. Prioritize
**problems/opportunities over solutions** where the input allows.

**GOOD (excerpt):**
> **Recommendation:** Use **RICE** as the primary. You have ~40 backlog items, reach data from analytics, and exec stakeholders who need auditable math — RICE's `(Reach × Impact × Confidence) / Effort` gives defensible, comparable scores at that scale. **Fallback:** for the ~5 items with no reach data, drop to **ICE** rather than fabricate a Reach number.
> *Watch-out: Effort is a denominator, so tiny-effort items inflate; sanity-check the top of the list against strategy before committing.*

**BAD (excerpt):**
> "Use RICE, it's the industry standard."
> — fails: no decision framing, ignores that the team has no reach/effort data (so RICE is unsupported), no fallback, no tradeoff, treats a framework as a default instead of a fit.

## Process
1. **Frame the decision** — pin down what is being prioritized, the scale, and who must buy in.
2. **Screen by object** — prioritizing *customer problems* → Opportunity Scoring; *requirements* → MoSCoW; *flow/cost-of-delay* → WSJF; *ideas/features* → ICE/RICE/Value-vs-Effort; *understanding expectations* → Kano (understanding, not ranking).
3. **Screen by data & rigor** — light data or a quick triage → Value-vs-Effort or ICE; reach data + need for auditable rigor at scale → RICE; survey data on importance/satisfaction → Opportunity Scoring.
4. **Pick a primary and a fallback** — commit to one framework, and name the framework to pair with or fall back to when its inputs are missing.
5. **Spell out application** — give the formula/mechanic, the inputs to gather, and the scale.
6. **Name the watch-outs** — the specific failure mode of the pick and the guardrail.
7. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] A **single primary framework is named** (not "it depends") with a one-line fit rationale tied to the stated decision, scale, and audience.
- [ ] A **fallback or pairing** is named for when the primary's inputs are missing or a second lens is needed.
- [ ] The comparison table lists, for each candidate, its **inputs needed** and **key tradeoff/failure mode** — not just its formula.
- [ ] The recommendation is **justified by the available data**, and any framework requiring data the user lacks is either excluded or flagged as "needs X first".
- [ ] The **formula/mechanic and scale** for the pick are spelled out so the user could run it next.
- [ ] At least one **watch-out** specific to the chosen framework (false precision, effort gaming, problem-vs-solution) is stated with a guardrail.
- [ ] Where the object of prioritization is customer needs, the brief steers toward prioritizing **problems/opportunities over solutions**.
- [ ] If the output is written to a file, it follows `template.md` — all 5 sections present, in order, headings matching (a skill-scoped hook re-checks this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `prioritization-frameworks-happy` (happy path) — a squad with reach + effort data on a sizeable backlog; expects a RICE recommendation with an ICE fallback and watch-outs.
- `prioritization-frameworks-edge` (edge) — sparse data and a customer-problem object; must steer to Value-vs-Effort or Opportunity Scoring rather than force RICE, and flag missing data.
- `prioritization-frameworks-adversarial` (adversarial) — user demands "just tell me RICE is best" as a universal answer; the skill must resist the one-framework-fits-all framing and select by fit.

Pass bar: baseline overall ≥ 0.8; a change dropping overall > 0.05 fails.

## References

### Related Skills
- `prioritize-features` — the execution counterpart: runs the chosen framework's scoring pass on a real backlog and returns a ranked list. This skill picks the method; that one applies it.
- `market-sizing` — Opportunity/Impact inputs (reach, value per customer) are grounded by the SAM/SOM boundaries market sizing sets.

### External Frameworks
- Dan Olsen, *The Lean Product Playbook* — Opportunity (Importance-vs-Satisfaction) Scoring; the "prioritize problems, not solutions" principle this skill carries.
- Intercom / Sean McBride — **RICE** `(Reach × Impact × Confidence) / Effort`, the auditable-at-scale framework.
- Sean Ellis — **ICE** (Impact × Confidence × Ease) for lightweight, fast prioritization.
- Noriaki Kano — the **Kano Model** (Must-be / Performance / Attractive / Indifferent / Reverse) for understanding, not ranking, expectations.
- Dean Leffingwell (SAFe) — **WSJF** (Weighted Shortest Job First = Cost of Delay ÷ Job Size) for flow and cost-of-delay sequencing.
- **MoSCoW** (Must / Should / Could / Won't) — DSDM requirements prioritization; useful for scope negotiation, weak as a ranking system.
