---
name: summarize-interview
description: >
  Transform a customer interview transcript into a structured summary capturing
  Jobs to Be Done, satisfaction signals, pain points, and action items.
  Use when processing interview recordings or transcripts, synthesizing discovery
  interviews, preparing interview readouts, or building an evidence base across
  multiple customer conversations.
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
            - ${CLAUDE_PLUGIN_ROOT}/skills/summarize-interview/template.md
---

# Summarize Customer Interview

## Purpose
Produce a structured, decision-ready summary of a customer discovery interview.
The output makes JTBD signals, satisfaction levels, and pain points immediately
scannable — so a PM or researcher can file the interview, brief stakeholders, or
feed findings into a synthesis without re-reading the raw transcript.

**When NOT to use:** cross-interview synthesis or affinity mapping across multiple
sessions (use `synthesize-discovery`), quantitative survey analysis (use a data
analytics skill), or competitive intelligence gathering (use `competitor-analysis`).
This skill processes **one interview at a time**.

## Inputs
- **Required:** the interview transcript — pasted inline, or as an attached file
  (text, PDF, audio transcription). If neither is provided, ask before proceeding;
  do not fabricate content.
- **Required:** the product or discovery topic being researched (e.g., "expense
  reporting for SMBs"). If absent, ask — the context shapes which signals matter.
- **Optional:** participant metadata (name, role, company, date) — use "-" for any
  field the transcript does not supply; never invent.
- **Optional:** a list of specific hypotheses or research questions to pay
  attention to — default is to surface the most prominent JTBD and pain signals.

## Output Contract
The deliverable is a **customer interview summary** with these sections (see
`template.md`):

1. **Header** — date, participants (name, role, company), and background context
   (one sentence on who the customer is and what they do day-to-day).
2. **Current Solution** — the product, workflow, or workaround the customer uses
   today to address the problem space.
3. **What They Like** — JTBD signals for what is working well: job, desired
   outcome, and satisfaction level (delighted / satisfied / neutral / frustrated).
4. **Problems With Current Solution** — JTBD signals for pain: job, desired
   outcome, importance to the customer, and satisfaction level.
5. **Key Insights** — 2–5 unexpected findings, notable patterns, or verbatim
   quotes that would not be obvious from the section headers.
6. **Action Items** — concrete next steps: date · owner · action (one row per item).

Format: structured prose with short bullets per section. Total length: one page
(roughly 300–500 words). Use plain language — a non-technical stakeholder must
be able to read it without the transcript.

**GOOD (excerpt):**
> **Problems With Current Solution**
> - *Job:* reconcile travel expenses at month-end · *Desired outcome:* zero manual
>   re-entry into the ERP · *Importance:* critical (blocks invoice closure)
>   · *Satisfaction:* frustrated — "I spend three hours every month fixing
>   duplicates the tool creates."
>
> **Key Insights**
> - Customer manually maintains a shadow spreadsheet alongside the tool — a strong
>   signal that automated categorisation is table-stakes, not a differentiator.

**BAD (excerpt):**
> "The customer was happy with some things and unhappy with others. They said the
> tool was okay but could be better."
> — fails: no JTBD structure, no satisfaction level, no verbatim signal, not
> actionable for a follow-up or synthesis session.

## Process
1. **Read the full transcript** before writing anything. Do not skim.
2. **Extract metadata** — date, participants, background. Mark "-" for any missing
   field; do not invent details.
3. **Identify the current solution** — the actual workflow or tool today, not what
   they wish they had.
4. **Map JTBD signals** — for each identified job, note: the job itself, the
   desired outcome, and whether the signal is a like (working) or a pain (broken).
   Rate satisfaction on the four-point scale.
5. **Surface key insights** — flag anything unexpected, contradictory, or quotable
   that a reader skimming only the JTBD rows would miss.
6. **Draft action items** — only include items explicitly mentioned or clearly
   implied in the interview; do not invent follow-ups.
7. **Write using plain language** — aim for primary-school readability; avoid
   jargon unless the customer used it themselves.
8. Run the Quality Bar below; revise if any item fails; then return.

## Quality Bar
Before returning, confirm:
- [ ] Every JTBD signal includes **job, desired outcome, and satisfaction level** —
  no row is missing any of the three fields.
- [ ] No participant name, role, date, or company is **invented** — "-" is used for
  genuinely missing fields.
- [ ] **Key Insights** contains at least two items that are not already captured in
  the JTBD rows (they must add information, not restate it).
- [ ] **Action Items** reference only next steps that are traceable to the
  transcript — nothing fabricated.
- [ ] The summary is **one page or shorter** and written in plain, jargon-free
  language.
- [ ] If the summary is written to a file, it follows `template.md` — all six
  sections present, in order, headings matching (a skill-scoped hook re-checks
  this on write).

## Validation & Eval
Scenario cards in `evals/`:
- `summarize-interview-happy` — rich transcript with clear JTBD signals and full
  participant metadata.
- `summarize-interview-edge` — sparse transcript with minimal metadata and only
  one clear job signal.
- `summarize-interview-adversarial` — user requests a summary without providing a
  transcript; skill must ask before proceeding, not fabricate.

Pass bar: baseline overall ≥ 0.8; a change that drops overall > 0.05 fails.

## References

### Related Skills
- `synthesize-discovery` — aggregates multiple interview summaries into themes,
  patterns, and opportunity areas; consumes the structured output this skill
  produces.
- `create-persona` — uses JTBD signals and pain patterns from interview summaries
  to build or refine customer personas.

### External Frameworks
- Paweł Huryn, ["User Interviews: The Ultimate Guide to Research Interviews"](https://www.productcompass.pm/p/interviewing-customers-the-ultimate) — covers interview structure, probing techniques, and the JTBD lens this skill applies.
- Tony Ulwick, *Outcome-Driven Innovation* (2005) — the JTBD/desired-outcome/satisfaction model that anchors the "What They Like" and "Problems" sections.
- Teresa Torres, *Continuous Discovery Habits* (2021) — interview cadence and synthesis practices; the interview summary is the atomic input to Torres's opportunity solution tree.
