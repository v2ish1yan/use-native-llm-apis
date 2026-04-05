---
name: use-native-llm-apis
description: Use when implementing, integrating, migrating, or debugging provider-native LLM APIs in code, especially auth, request shapes, streaming, tool calling, structured output, or provider switching.
---

# Use Native LLM APIs

## Overview

Use this skill for provider-native API implementation work. The goal is not to compare vendors or design an AI product in the abstract. The goal is to help an agent send the right request, parse the right response, and avoid mixing one provider's wire format with another's.

Keep the work provider-native unless the user explicitly asks for an abstraction layer.

## Trigger Boundary

Load this skill when the user's request is about implementing, integrating, calling, migrating, or debugging a named provider's native LLM API in code.

Typical trigger verbs:

- 接入
- 对接
- 调用
- 集成
- 迁移
- 切换
- 排查
- integrate
- connect
- call
- migrate
- switch
- debug
- hook up
- wire

Typical trigger topics:

- auth headers
- base URLs
- request body shape
- response parsing
- streaming
- tool calling
- structured JSON output
- 400 / 401 / 422 request failures

Do not trigger for:

- pricing comparison
- model benchmarking
- prompt engineering
- generic chatbot or RAG planning without provider-native API work
- broad product design questions without a provider integration task

For examples, see [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md).

## Start Protocol

Always use this order:

1. Open [references/start-here.md](references/start-here.md).
2. Choose exactly one task recipe.
3. Resolve the exact provider file through [references/providers/index.md](references/providers/index.md).
4. Open one comparison file only if the task involves migration, streaming, tool calling, or structured output.
5. Only then write or patch code.

Do not skip directly from `SKILL.md` to a guessed provider file.

## Missing-Info Protocol

When the request is incomplete, use the smallest possible clarification:

- Provider missing: ask which provider API they want to use.
- Task missing but provider is present: infer the most likely task from the request; if still ambiguous, ask one question about the task.
- Provider and task both missing: do not load this skill yet.

Ask at most one clarification question before routing.

Examples:

- "给项目加 AI 对话" -> do not trigger yet
- "给项目接 Claude" -> trigger, but confirm whether they need integration, streaming, migration, or debugging only if the task is not inferable
- "把 OpenAI 改成 Gemini" -> trigger immediately as migration

## Task Routing

Pick one recipe before coding:

| Task | Start here |
|------|-----------|
| Integrate one provider | [integrate-one-provider.md](references/recipes/integrate-one-provider.md) |
| Migrate between providers | [migrate-between-providers.md](references/recipes/migrate-between-providers.md) |
| Add streaming | [add-streaming.md](references/recipes/add-streaming.md) |
| Add tool calling | [add-tool-calling.md](references/recipes/add-tool-calling.md) |
| Add structured JSON output | [add-structured-output.md](references/recipes/add-structured-output.md) |
| Debug a failed request | [debug-failed-request.md](references/recipes/debug-failed-request.md) |

## Execution Rules

- Open one recipe first, not multiple.
- Resolve provider paths through `references/providers/index.md`, not from memory.
- Keep provider-specific field names visible until the request path is verified.
- Prefer raw HTTP examples over abstraction-heavy wrappers.
- Prefer native `fetch` examples unless the user asked for a specific SDK.
- For streaming, provide a runnable parser instead of only naming event types.

## Stop Rules

Stop and clarify before coding if:

- the provider is still unknown
- the task could mean two materially different routes
- the user is asking for research or comparison rather than implementation
- the request is framed as "OpenAI-compatible" but the exact provider behavior matters

## Guardrails

- Treat model names as unstable examples, not guarantees.
- Prefer official docs over memory when bundled references are insufficient.
- Do not assume OpenAI-compatible means fully behavior-compatible.
- Do not add new provider claims from memory alone; save official source URLs first.
