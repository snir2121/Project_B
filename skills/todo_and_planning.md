# TODO and Planning Skill

Use this skill to manage project tasks consistently across collaborators and coding agents.

## Main sections

Every task list must contain exactly two main sections:

1. `TODO` — tasks that are pending, active, blocked, or otherwise unfinished.
2. `Done` — tasks that have been completed.

## Task fields

Every task in either section must include:

- **Status:** The current task state, such as `pending`, `in progress`, `blocked`, or `completed`.
- **Notes:** Useful context, requirements, decisions, blockers, or completion details.
- **Priority:** One of `high`, `medium`, or `low`.

## Template

```markdown
# TODO

## Task name

- **Status:** pending
- **Notes:** Describe the work and any relevant context.
- **Priority:** medium

# Done

## Completed task name

- **Status:** completed
- **Notes:** Summarize what was completed and where.
- **Priority:** medium
```

When a task is completed, move it from `TODO` to `Done` and change its status to `completed`. Keep notes specific enough that another collaborator or coding agent can understand the result without relying on chat history.
