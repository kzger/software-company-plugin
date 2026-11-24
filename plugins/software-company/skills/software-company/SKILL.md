---
name: software-company
description: Plan or deliver a software project in the current Codex App workspace. Use when the user invokes Software Company, requests its plan documents, or asks to implement and review an existing Software Company plan.
---

# Software Company

Use the current local Codex App chat and its selected workspace for every stage. Use the signed-in App model and its built-in file, terminal, and review capabilities. Execute the roles as stages in this chat, carrying decisions forward through workspace files.

- **Plan** applies when the user asks for planning or leaves implementation scope unspecified. Read [Planning](references/plan.md), write the PRD, system design and task list, then stop after verifying them.
- **Generate** applies when the user explicitly asks to implement. Read [Delivery](references/delivery.md) and continue from the agreed plan in this workspace. If a plan is missing and the user authorized the full workflow, complete Planning first.
- **Review** applies when the user asks to review existing work. Read the review guidance in [Delivery](references/delivery.md) and inspect the requested implementation against its plan.

Keep the user's brief, approvals, and destination in this chat. Follow the project's applicable `AGENTS.md` files. If the active workspace is the wrong project, ask the user to select the intended local workspace in Codex before writing files.

Tell the user which files were written or examined, what was verified, and any open decisions or failed checks. A `plan` request authorizes planning files only.
