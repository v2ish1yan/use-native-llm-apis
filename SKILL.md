---
name: use-native-llm-apis
description: Use when a user is implementing, integrating, connecting, migrating, or debugging a large-model API or provider-native LLM request, including prompts like "ji ru DeepSeek API", "dui jie Anthropic API", "switch OpenAI to Gemini", "add streaming", "add tool calling", or "debug model API 400/401". Covers auth, base URLs, request and response shapes, streaming, tool calling, structured output, multimodal inputs, and provider migration.
---

# Use Native LLM APIs

## Overview

Use this skill when the task is active implementation work, not general market research. The bundled references are designed to answer "what request do I actually send?" and "what changes when I switch providers?" fast enough that you do not need to go back to web search for common protocol questions.

Keep the work provider-native. Do not flatten different providers into a fake universal schema unless the user explicitly wants an abstraction layer.

## Quick Start

Start with [references/index.md](references/index.md).

Use the references in this order:

1. Open the matching task recipe in `references/recipes/`.
2. Open the provider file in `references/providers/`.
3. Open the topic file in `references/comparisons/` if the task involves migration, streaming, tool use, or structured output.
4. Open [references/research/source-registry.md](references/research/source-registry.md) only when bundled references are insufficient or a time-sensitive detail needs refresh.
5. Open [references/research/cc-switch-provider-notes.md](references/research/cc-switch-provider-notes.md) only for expansion planning and coverage maintenance.

Before coding, also scan [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md) if the user phrasing is ambiguous and you need to decide whether this skill applies.

## When To Trigger

Load this skill whenever the user is asking to build against a model API in code, even if they do not name the skill.

Common trigger phrases include:

- "`wo yao jie ru deepseek da mo xing api`"
- "`bang wo dui jie Anthropic api`"
- "`zhe ge xiang mu yao diao yong OpenAI API`"
- "`ba OpenAI gai cheng Gemini yuan sheng ge shi`"
- "`gei zhe ge xiang mu jia liu shi shu chu`"
- "`bang wo jie gong ju diao yong`"
- "`rang mo xing fan hui jie gou hua JSON`"
- "`pai cha zhe ge mo xing jie kou wei shen me 400/401`"

If the request is about implementation rather than market comparison, bias toward loading this skill.

## Task Routing

Pick one path before coding:

- New integration: start with `references/recipes/integrate-one-provider.md`
- Provider migration: start with `references/recipes/migrate-between-providers.md`
- Streaming work: start with `references/recipes/add-streaming.md`
- Tool calling: start with `references/recipes/add-tool-calling.md`
- Structured output: start with `references/recipes/add-structured-output.md`
- Broken request: start with `references/recipes/debug-failed-request.md`

For more real user phrasing and few-shot routing examples, see `references/recipes/prompt-patterns.md`.

## Workflow

### Implement one provider

Open the matching provider reference and extract:

- auth and base URL
- main inference endpoint
- minimal request body
- response shape
- streaming behavior
- tool-calling and structured-output rules

Then write the integration in the user's target language using the documented HTTP shape. Prefer small, verifiable requests first.

If the user asks for JavaScript or TypeScript:

- prefer native `fetch` examples over SDK-specific wrappers unless the user asked for a specific SDK
- for streaming, provide a runnable `ReadableStream` or SSE parsing example instead of only describing event names
- keep the code close to the provider's raw wire format so the mapping stays obvious

When you add or revise provider coverage:

- save every official doc URL and any high-value reference URL in `references/research/source-registry.md`
- group links by provider so future updates do not require rediscovering the same docs
- treat `cc-switch` as a discovery aid, not the final authority

### Migrate between providers

Open:

- the source provider file
- the target provider file
- the relevant comparison file

Pay special attention to:

- system prompt placement
- message/content nesting
- streaming event format
- tool schema format
- JSON/schema output semantics
- image or multimodal payload encoding

### Debug request-shape bugs

If a request fails with `400`, `401`, `403`, `404`, `415`, or `422`, check in this order:

1. auth header name and required version headers
2. base URL and path prefix
3. top-level request keys
4. nested content block format
5. tool/schema field names
6. streaming toggle and response parsing logic

## Common Development Scenarios

- When the user asks for a first working integration, keep the code close to raw HTTP and avoid premature abstraction.
- When the user asks for a migration, compare the old request and the new request side by side instead of renaming fields mechanically.
- When the user asks for streaming, do not assume the non-stream parser can be reused.
- When the user asks for structured output, prefer native schema controls where available, then tools, then constrained JSON prompting.
- When the user asks for tool calling, validate both the declaration schema and the tool-result continuation shape.

## Current Coverage

### Pilot coverage

The Stage 1 pilot covers:

- OpenAI
- Anthropic
- Gemini
- DeepSeek

### Planned expansion

Stage 2 should expand toward all provider families and gateways surfaced by `cc-switch`, with priority on native vendors first and third-party relays second.

See [references/research/cc-switch-provider-notes.md](references/research/cc-switch-provider-notes.md).

## Guardrails

- Treat model names as unstable. Use examples, but do not assume a specific model is permanently available.
- Prefer official provider docs over community blog posts when bundled references are insufficient.
- If a detail is time-sensitive and not covered here, verify it against official docs before coding.
- For OpenAI-compatible providers, do not assume full behavioral compatibility. Check the provider-specific notes and the comparison docs first.
- Do not add new provider claims from memory alone. Save the official source URLs before expanding coverage.
