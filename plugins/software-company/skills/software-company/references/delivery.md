# Delivery

## Implementation

Read `prd.md`, `system-design.md`, and `task-list.md` from the plan directory in the current workspace. Resolve any ambiguity about the plan before editing source. Check the workspace state, project instructions, and the requested implementation scope.

Work through applicable task dependencies in order with the App's built-in tools. Preserve the plan's requirement IDs for traceability. Record completed and blocked tasks in `task-list.md`. If a newly discovered constraint requires a product or interface change, resolve the decision and update the affected planning files before marking the task complete.

## Testing

Use the project's tests and the acceptance checks from the plan. Add or update tests when the task list calls for them or a relevant behavior otherwise lacks coverage. Run the relevant commands in the current workspace with the App's terminal. Write `test-report.md` next to the plan with executed commands, observed outcomes, coverage by requirement, and any checks skipped or blocked.

## Review

Inspect the implementation and test evidence against the PRD, design, and task list. Give findings by severity with file and line references, the affected requirement, and an actionable correction. When implementation is authorized, fix in-scope issues and rerun the affected checks. Record remaining findings and verification gaps in `review.md` next to the plan. For a review-only request, avoid editing the implementation.

Keep each stage in the same Codex App workspace. Use commands only for the project work within its scope and its normal approval rules.
