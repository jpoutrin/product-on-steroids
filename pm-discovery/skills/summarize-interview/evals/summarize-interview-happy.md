---
id: summarize-interview-happy
skill: summarize-interview
input:
  prompt: "Summarize this customer interview for our expense-reporting product discovery."
  context: |
    Transcript excerpt:
    Date: 2025-03-12. Participants: Maria Lopes, Finance Manager, Acme GmbH.
    "We currently use Expensify. What I like is that receipt scanning works — I
    snap a photo and the amount is there. But reconciliation with our SAP is a
    nightmare. Every month I spend two to three hours fixing duplicates and
    re-categorising expenses the tool gets wrong. I'd love it if reconciliation
    just happened automatically. It's blocking us from closing the books on time.
    Follow-up: our CFO wants a demo of whatever you build."
expected:
  - "Header includes date (2025-03-12), participant name (Maria Lopes), role (Finance Manager), and company (Acme GmbH)"
  - "Current Solution identifies Expensify as the tool in use today"
  - "What They Like includes receipt scanning with satisfaction level of at least satisfied"
  - "Problems section includes reconciliation with SAP, rated critical or high importance, with frustrated satisfaction"
  - "Key Insights contains at least one item beyond the JTBD rows (e.g., the shadow-spreadsheet inference or the CFO demo signal)"
  - "Action Items includes the CFO demo follow-up with an owner or date placeholder"
  - "No field is invented — uses only details from the provided transcript"
rubric:
  accuracy: "All extracted facts match the transcript; no invented details"
  completeness: "All six template sections present and non-empty"
  jtbd_structure: "Every JTBD row has job + desired outcome + satisfaction level"
  actionability: "Action items are concrete and traceable to the transcript"
weight: 1.0
---

Happy path: a rich transcript with clear JTBD signals, full metadata, and an
explicit action item. Guards against missing JTBD structure fields, invented
details, and vague action items that aren't traceable to what the customer said.
