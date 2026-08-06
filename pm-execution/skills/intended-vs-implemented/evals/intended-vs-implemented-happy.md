---
id: intended-vs-implemented-happy
skill: intended-vs-implemented
input:
  prompt: "Audit this payment-processing subsystem against its documented spec. Here's the permissions.md: 'Only admins may refund orders. Refunds must reduce the customer balance by the exact refund amount.' And here's a sketch of the code (file: `app/payments.py`): admin check at line 156 is `if not user.is_admin(): return error`. Refund logic at lines 158–170 subtracts the refund amount from balance, logs it, and updates the database."
  context: "Well-documented feature with clear spec; code path is straightforward. Goal: find any mismatch between the documented intent and implementation."
expected:
  - "Identifies both the documented intent (only admins may refund, refunds must reduce balance by exact amount) and the implementation evidence (admin guard at line 156, balance update at lines 158–170)"
  - "Cites both the docs and code with line numbers or specific references"
  - "Confirms that no boundary-crossing gap exists (the code enforces what the docs require)"
  - "If the docs and code align, reports that clearly rather than fabricating gaps"
  - "Includes an Audit Scope section that names what was audited and what documents were used as ground truth"
rubric:
  citation_precision: 0.35
  boundary_identification: 0.25
  gap_accuracy: 0.25
  avoidance_of_fabrication: 0.15
weight: 1.0
---

Happy path: well-documented feature with clear intent and straightforward code path. Guards against fabricating gaps when intent and code align, and ensures the auditor cites specific lines and rules rather than hand-waving ("looks right to me").
