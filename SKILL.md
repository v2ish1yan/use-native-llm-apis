---
name: use-native-llm-apis
description: >
  Trigger when a user wants to implement, integrate, connect, migrate, or debug a
  large-model / LLM / AI API in code. Covers provider-native request and response
  shapes, auth, base URLs, streaming, tool calling, structured output, multimodal
  inputs, and migration between vendors.

  Chinese triggers: 接入/对接/集成/调用/切换/迁移/加上 大模型/模型/LLM/AI API,
  接入 DeepSeek API, 对接 Anthropic/Claude API, 调用 OpenAI API,
  把 OpenAI 改成 Gemini, 切换到 DeepSeek, 迁移到 Claude, 加流式输出,
  加工具调用/函数调用, 返回结构化 JSON, 排查/调试 模型接口 400/401/403,
  智谱 GLM API, 阿里百炼/通义千问 API, 豆包/火山引擎 API, Kimi/Moonshot API,
  MiniMax API, 阶跃星辰/StepFun API, 小米 MiMo API, 硅基流动/SiliconFlow API,
  火山方舟, 魔搭 ModelScope.

  English triggers: integrate/connect/call/use/switch/migrate/port/wire/hook up
  DeepSeek/Anthropic/Claude/OpenAI/Gemini/Zhipu/Bailian/Doubao/Kimi/MiniMax/StepFun/
  MiMo/SiliconFlow/OpenRouter/AWS Bedrock/Azure OpenAI/NVIDIA/ModelScope API,
  add streaming/tool calling/function calling/structured output/JSON mode,
  convert/migrate OpenAI to Gemini, debug model API request 400/401/403/422,
  LLM API integration, large model API, AI model API request.

  Do NOT trigger for market comparison, pricing research, or model benchmarking.
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

Common Chinese trigger phrases:

- "我要接入 DeepSeek 大模型 API"
- "帮我对接 Anthropic/Claude API"
- "这个项目要调用 OpenAI API"
- "把 OpenAI 改成 Gemini 原生格式"
- "给这个项目加上流式输出"
- "帮我加工具调用/函数调用"
- "让模型返回结构化 JSON"
- "排查这个模型接口为什么 400/401"
- "接入智谱 GLM API"
- "对接阿里百炼/通义千问 API"
- "调用豆包/火山引擎 API"
- "把 LLM 接口从 OpenAI 切到 DeepSeek"
- "接入 Kimi/Moonshot API"
- "调用 MiniMax/阶跃星辰/小米 MiMo/硅基流动 API"

Common English trigger phrases:

- "I need to integrate the DeepSeek API"
- "Hook up Anthropic/Claude in this project"
- "Convert this OpenAI request to Gemini native format"
- "Add streaming to our LLM client"
- "Wire tool calling into this model request"
- "Make the model return structured JSON"
- "Debug why this provider request is returning 400"
- "Switch this project from OpenAI to DeepSeek"
- "Port this to Zhipu/Bailian/Doubao/Kimi/MiniMax/StepFun/MiMo"
- "Connect to SiliconFlow/OpenRouter/AWS Bedrock/Azure OpenAI"

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

31 provider reference files across four categories:

**Native LLM Providers (11):** OpenAI, Anthropic, Gemini, DeepSeek, Zhipu GLM, Alibaba Bailian/DashScope, Kimi/Moonshot, Doubao/Volcengine Ark, MiniMax, StepFun, Xiaomi MiMo

**Cloud & Managed Platforms (5):** Azure OpenAI, AWS Bedrock, NVIDIA NIM, ModelScope, GitHub Copilot

**Gateway & Aggregation Layers (5):** OpenRouter, SiliconFlow, AiHubMix, Novita AI, NewAPI

**Relay / Proxy Services (10):** PackyCode, Cubence, CrazyRouter, Compshare, CTok.ai, Right Code, X-Code API, Ai Go Code, AICodeMirror, DMXAPI

**Cross-Provider Comparisons (4):** request shape, streaming, tool calling, structured output

See [references/research/coverage-status.md](references/research/coverage-status.md) for live status and [references/research/cc-switch-provider-notes.md](references/research/cc-switch-provider-notes.md) for expansion planning.

## Guardrails

- Treat model names as unstable. Use examples, but do not assume a specific model is permanently available.
- Prefer official provider docs over community blog posts when bundled references are insufficient.
- If a detail is time-sensitive and not covered here, verify it against official docs before coding.
- For OpenAI-compatible providers, do not assume full behavioral compatibility. Check the provider-specific notes and the comparison docs first.
- Do not add new provider claims from memory alone. Save the official source URLs before expanding coverage.
