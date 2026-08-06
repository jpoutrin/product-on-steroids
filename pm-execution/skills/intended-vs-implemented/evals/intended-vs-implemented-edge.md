---
id: intended-vs-implemented-edge
skill: intended-vs-implemented
input:
  prompt: "Audit the user-role assignment feature. Architecture.md says: 'Role changes are admin-only and validated server-side.' The code (file: `app/routes.py`, lines 205–220) checks `if current_user.is_admin()` before allowing a role POST. But there's also a separate bulk-upload endpoint at `/api/admin/upload-roles` (lines 356–370) that processes CSV files. The bulk endpoint calls a different role-update function that re-uses the same enforcement logic but it's not immediately obvious from the code."
  context: "Partial documentation; guards are present but distributed across multiple code paths. Auditor must verify that documented intent is enforced on *every* path, not just the obvious one."
expected:
  - "Identifies the documented intent (admin-only, server-side validation) and both code paths (POST endpoint and bulk-upload endpoint)"
  - "Verifies that enforcement applies to both paths or flags if enforcement is inconsistent between them"
  - "Cites the bulk-upload endpoint (lines 356–370) as a second path that needs verification, not just the first one"
  - "If enforcement is delegated across functions, verifies the delegation by citing both the delegation point and the actual enforcement in the called function"
  - "Flags if the enforcement is truly applied everywhere, or reports if there's a gap (e.g., bulk endpoint bypasses the guard)"
rubric:
  path_coverage: 0.35
  delegation_verification: 0.25
  gap_detection: 0.25
  doc_staleness_flag: 0.15
weight: 1.0
---

Edge case: multiple code paths that implement the same documented rule. Guards against missing gaps because the auditor only checked the obvious endpoint, or incorrectly flagging enforcement that's actually present but delegated across functions. Tests whether the auditor follows *every* path to verify intent, not just the first one.
