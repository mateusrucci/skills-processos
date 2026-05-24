# ClickUp Request Patterns

Use these patterns to quickly classify the user's request before acting.

## Simple Reminder

Example:
- `Crie uma tarefa para conversar com o Emanuel sobre o notebook`

Handling:
- Create one task.
- Keep the title concise.
- Do not add subtasks unless requested.

## Task With Ordered Subtasks

Example:
- `Crie uma tarefa para resolver a caixa de padrinhos do Jean. Subtarefas: escrever a carta, escolher o livro.`

Handling:
- Create the parent task first.
- Create the subtasks in the same order.

## Large Checklist

Example:
- The user sends a long optimization checklist or a multi-phase project.

Handling:
- Create one parent task when the checklist belongs to a single initiative.
- Group execution by section if the list is long.
- If the tool limit is reached, report completed sections and wait for `continuar`.

## Restructure Existing Work

Example:
- The user wants to delete one task and split the work into two new tasks.

Handling:
- Verify the old task.
- Delete or replace only the confirmed item.
- Create the new tasks and explain the new structure briefly.

## Analyze The Backlog

Example:
- `Analise a minha lista do ClickUp completa e me diga o que faz mais sentido eu fazer agora`

Handling:
- Fetch open tasks from the relevant scope.
- Rank by leverage, blockers, urgency, and monetization impact.
- Return a short prioritized recommendation.

## Ambiguous Destination

Example:
- The user says `coloque no ClickUp` but does not specify the list.

Handling:
- If recent context does not make the target list obvious, ask:
  `Em qual lista devo publicar?`
