---
name: use-native-llm-apis
description: Use when implementing, integrating, migrating, or debugging provider-native LLM APIs in code, especially auth, request shapes, streaming, tool calling, structured output, or provider switching. Covers 31 providers across native LLM, cloud/managed, gateway, and relay categories.
---

# Use Native LLM APIs

## Overview

Use this skill for **provider-native API implementation work**, not market research. The references answer "what request do I actually send?" and "what changes when I switch providers?" without web search.

Keep the work provider-native. Do not flatten different providers into a fake universal schema unless the user explicitly wants an abstraction layer.

## When To Trigger

Load this skill when the user's request is about **provider-native API implementation work**: integrating, calling, migrating between, or debugging an LLM provider's wire-format API in code.

Trigger actions: 接入, 对接, 调用, 迁移, 切换, 加流式输出, 加工具调用, 结构化 JSON, 排查 400/401/422.

Do NOT trigger for: building agents/chatbots/RAG without naming a provider API, prompt engineering, model tuning, pricing comparison.

For trigger phrase examples and routing, see [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md).

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

Then load:
1. The matching provider file from `references/providers/`
2. The matching comparison file from `references/comparisons/` if migrating or adding streaming/tools/schema

## Code Generation Defaults

- Prefer native `fetch` over SDK wrappers unless the user asked for a specific SDK
- For streaming, provide a runnable SSE parser, not just event-name descriptions
- Keep provider-specific field names visible until the request path is proven correct
- For JavaScript/TypeScript, keep code close to the raw wire format

## Guardrails

- Treat model names as unstable — use examples, do not hardcode availability assumptions
- Prefer official provider docs over community blog posts when bundled references are insufficient
- For OpenAI-compatible providers, do not assume full behavioral compatibility
- Do not add new provider claims from memory alone — save official source URLs first
