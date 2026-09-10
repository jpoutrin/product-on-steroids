---
id: market-sizing-fr-project
skill: market-sizing
input:
  prompt: "Dimensionne le marché d'un outil de signature électronique pour PME."
  context: "The project declares `language: fr` in .config/pm-skills.yaml. Bottom-up preferred. ~24M EU SMBs. Anchor pricing €15/mo. B2B SaaS, EU-only."
expected:
  - "The whole deliverable — headings, prose, table labels — is written in French"
  - "Keeps TAM, SAM and SOM untranslated as the section labels for the three figures"
  - "Preserves the template's section structure: same sections, same order, same heading levels"
  - "Still reports TAM, SAM and SOM as three distinct numbers with a top-down and a bottom-up TAM reconciled"
  - "States every key assumption explicitly with a source or a caveat and a confidence level"
rubric:
  language_fidelity: 0.30
  structure_preserved: 0.25
  correctness: 0.25
  assumptions_explicit: 0.20
weight: 1.0
---

Language card: the project declares French, so the memo is French but its
structure is unchanged. Guards against the two failure modes that matter — an
English memo in a French project, and a French memo that reorganises or drops
sections (or translates TAM/SAM/SOM) and so no longer matches the template.

This is the pattern to copy for any skill whose output language is load-bearing;
see docs/output-language.md.
