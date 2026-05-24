---
name: clickup-task-creator
description: Create, split, update, delete, and analyze ClickUp tasks and subtasks through the connected ClickUp integration. Use when the user wants to add one or more tasks, turn a checklist into subtasks, reorganize an existing task into multiple tasks, continue a partially completed batch, inspect tasks in a space or list, or decide what to work on next from the ClickUp backlog. If the destination list is not explicit and not clearly implied by recent context, always ask which list to publish to before creating or moving anything.
---

# ClickUp Task Creator

## Overview

Use the connected ClickUp tools to manage the user's task backlog quickly and with low token overhead.
Prioritize clear execution over long explanations.

## Core Workflow

1. Parse the request into concrete operations.
2. Resolve the destination list before creating or moving tasks.
3. Normalize the task structure.
4. Execute efficiently.
5. Return a concise summary of what was done and what remains.

## Resolve The Destination List

Treat the destination list as required context.

- If the user explicitly names the space or list, use it.
- If the user says "no mesmo lugar", "na mesma lista", or equivalent, reuse the most recent unambiguous destination from the current thread.
- If the destination is ambiguous, ask one concise question before creating anything:
  `Em qual lista devo publicar?`
- Never invent list IDs, assignee IDs, or space names.
- Prefer existing thread context for known IDs; otherwise discover them through the ClickUp integration.

## Normalize The Request

Convert the user's message into one of these patterns:

### 1. Single Simple Task

Use for reminders or isolated actions.

- Create one task with a short title.
- Skip long descriptions unless the user asked for detail.
- Add subtasks only if the user explicitly requested them.

### 2. Parent Task With Subtasks

Use when the user gives a checklist, phases, or ordered execution.

- Create the parent task first.
- Create subtasks in the same order the user gave them.
- Preserve sequence when the order matters.
- Keep subtask names action-oriented and specific.

### 3. Task Split Or Restructure

Use when the user wants to delete one task and replace it with two or more better-scoped tasks.

- Confirm the target task identity if there is any ambiguity.
- Remove or replace only the task the user clearly referenced.
- Recreate the new structure in a logical dependency order.
- Call out the new dependency flow in the summary when helpful.

### 4. Bulk Task Intake

Use when the user sends several tasks at once.

- Group related items under one parent only when the user clearly implies a grouped checklist.
- Otherwise create independent tasks.
- Prefer parallel tool calls when the tasks are independent.
- Keep titles short and consistent.

### 5. Backlog Analysis

Use when the user asks what to do now, what matters most, or what has the highest leverage.

- Fetch the relevant open tasks from the requested list, space, or workspace.
- Rank by blocker impact, revenue leverage, dependency unlocks, urgency, and owner coordination needs.
- Recommend a short ordered list of next actions.
- Explain the ranking briefly and concretely.

## Execution Rules

- Default to minimal task descriptions to reduce token usage.
- Only add rich structure when the user asked for a detailed plan, checklist, or phased execution.
- If the request references an external site, brief, or profile and the subtasks depend on that context, inspect the material first, then create the task breakdown.
- When creating many subtasks, proceed in batches if needed and keep track of what has already been created.
- If the tool session hits a limit or is interrupted, summarize what was completed and wait for `continuar` to resume the remaining items.
- When the user says `continuar`, continue only the pending remainder instead of redoing completed work.
- If recurring configuration is requested but the ClickUp tool cannot set recurrence, create the task and state clearly that recurrence must be configured manually.

## Response Style

Use concise operational summaries.

- After creation, report the parent task name and the number of subtasks created.
- If useful, list the created subtasks in order.
- For simple reminders, a one-line confirmation is enough.
- For backlog analysis, present the recommendation first and the reasoning second.

## Safety And Accuracy

- Never claim a task, subtask, deletion, or move succeeded unless the tool confirmed it.
- Never assume a list, assignee, or task exists without verifying.
- If multiple tasks have similar names, identify the correct one before deleting or editing.
- If the user's request is incomplete but still executable, make the smallest safe assumption and say so briefly.
- If the missing information changes where the task should be created, ask the list question first.

## Useful Reference

For common request shapes and handling patterns, see `references/request-patterns.md`.
