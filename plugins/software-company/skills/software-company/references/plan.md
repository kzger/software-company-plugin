# Planning

1. Use the user's destination inside the active workspace. If none is given, use `docs/software-company/<project-slug>/` and report the path. For a new plan, choose an unused directory or confirm the intended update before replacing an unrelated plan. Read the applicable project guidance before writing.
2. Write the following UTF-8 Markdown files in order. Read each earlier file before drafting the next. Match the language of the brief and keep file and requirement identifiers stable.

| Stage | File | Content |
| --- | --- | --- |
| Product | `prd.md` | State the user outcome, scope and exclusions. Give each requirement a stable ID, a priority, and observable acceptance criteria. Mark assumptions and open decisions. |
| Architecture | `system-design.md` | Explain the implementation approach, file responsibilities, interfaces and failure handling. Map design decisions to requirement IDs and identify how the acceptance criteria can be checked. |
| Project management | `task-list.md` | List ordered tasks with affected files, dependencies, requirement IDs, and acceptance checks. Assign tests and review as explicit tasks. |

Before completing `plan`, reopen all three files. Check that every requirement has a design decision and at least one task with a verifiable outcome. Check examples, interfaces, outputs, and error behavior for agreement. Correct inconsistencies in the planning files and report any decision still needed for implementation. The task list is the handoff for a later turn in this chat.
