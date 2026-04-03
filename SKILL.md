---
name: use-native-llm-apis
description: Use when an agent needs provider-native LLM API details during implementation or migration work. Covers native API request and response formats, auth, base URLs, streaming, tool calling, structured output, multimodal inputs, and embeddings for mainstream providers. Especially useful when integrating OpenAI, Anthropic, Gemini, DeepSeek, or when adapting code between providers without re-searching vendor docs.
---

# Use Native LLM APIs

## Overview

Use this skill when the task is active implementation work, not general market research. The bundled references are designed to answer "what request do I actually send?" and "what changes when I switch providers?" fast enough that you do not need to go back to web search for common protocol questions.

Keep the work provider-native. Do not flatten different providers into a fake universal schema unless the user explicitly wants an abstraction layer.

## Quick Start

Start with [references/index.md](references/index.md).

Use the references in this order:

1. Open the provider file in `references/providers/` when implementing against one specific vendor.
2. Open the topic file in `references/comparisons/` when migrating code, building an adapter, or debugging portability assumptions.
3. Open [references/research/cc-switch-provider-notes.md](references/research/cc-switch-provider-notes.md) when you need the broader `cc-switch` coverage map for Stage 2 expansion.

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
