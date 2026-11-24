---
name: software-company
description: Route Software Company requests in the current Codex App workspace to Plan, Generate, Review, or Boss.
---

# Software Company

Use the current local Codex App chat and its selected workspace for every stage. Use the signed-in App model and its built-in file, terminal, and review capabilities. Execute the roles as stages in this chat, carrying decisions forward through workspace files.

When invoked through a mode-specific skill, use that mode. Otherwise route the request as follows.

- **Plan** applies when the user asks for planning or leaves implementation scope unspecified. Follow [Planning](references/plan.md) and stop after verifying the three planning files.
- **Generate** continues an existing plan when the user requests implementation. Follow [Generate](references/delivery.md#generate).
- **Review** inspects existing work and test evidence. Follow [Review](references/delivery.md#review).
- **Boss** takes a brief through planning, implementation, testing, and review in one request. Follow [Boss](references/boss.md) when the user selects Boss or explicitly asks for the full workflow from a brief.

With only a mode name or a question about the modes, explain the required input or show `$software-company-plan`, `$software-company-generate`, `$software-company-review`, and `$software-company-boss`. A mode mention without a task does not authorize file changes.

Keep the user's brief, approvals, and destination in this chat. Follow the project's applicable `AGENTS.md` files. If the active workspace is the wrong project, ask the user to select the intended local workspace in Codex before writing files.

Tell the user which files were written or examined, what was verified, and any open decisions or failed checks. A `plan` request authorizes planning files only.
