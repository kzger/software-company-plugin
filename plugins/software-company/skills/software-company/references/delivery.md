# Delivery

## Generate

Use the plan directory specified by the user or unambiguously established in this chat. Before editing source, read the existing `prd.md`, `system-design.md`, and `task-list.md` in the current workspace. If the plan is missing or incomplete, report which files are needed and stop. The user can run Plan to prepare those files or Boss to start from a brief. Resolve ambiguity about which plan to continue before editing source.

When implementation is authorized, check the workspace state and project instructions. Work through applicable task dependencies in order with the App's built-in tools, then perform Testing and Review. Preserve the plan's requirement IDs for traceability. Record completed and blocked tasks in `task-list.md`. If a newly discovered constraint requires a product or interface change, resolve the decision and update the affected planning files before marking the task complete.

## Testing

Use the project's tests and the acceptance checks from the plan. Add or update tests when the task list calls for them or a relevant behavior otherwise lacks coverage. Run the relevant commands in the current workspace with the App's terminal. Write `test-report.md` next to the plan with executed commands, observed outcomes, coverage by requirement, and any checks skipped or blocked.

## Review

Inspect the requested implementation and test evidence against the available PRD, design, and task list. If there is no plan, use the user's review scope and the project's documented behavior, and report the resulting coverage gaps. Give findings by severity with file and line references, the affected requirement when known, and an actionable correction. When implementation is authorized, fix in-scope issues and rerun the affected checks. Record remaining findings and verification gaps in `review.md` next to the plan, or in the chat if there is no plan or the user asked for chat-only feedback. For a review-only request, leave the implementation untouched.

Keep each stage in the same Codex App workspace. Use commands only for the project work within its scope and its normal approval rules.
