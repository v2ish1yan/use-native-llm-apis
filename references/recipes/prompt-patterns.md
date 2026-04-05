# Prompt Patterns and Few-Shot Triggers

Use this file to decide whether a user's request should trigger the `use-native-llm-apis` skill.

## Trigger rule

Trigger when the user wants to **implement, integrate, call, migrate, or debug** a provider-native LLM API in code.

Do NOT trigger for: market comparison, pricing research, model benchmarking, prompt engineering, general AI architecture advice — unless the user also asks to implement code against a specific provider API.

## Chinese trigger phrases

- "我要接入 DeepSeek 大模型 API"
- "帮我对接 Anthropic/Claude API"
- "这个项目要用 OpenAI API"
- "把现在的 OpenAI 请求改成 Gemini 原生格式"
- "给这个项目加大模型流式输出"
- "帮我把工具调用接上"
- "我要让模型返回结构化 JSON"
- "这个模型接口为什么一直 400"
- "帮我排查 401，是不是鉴权格式错了"
- "我要把 LLM 接口从 OpenAI 切到 DeepSeek"
- "项目里需要接大模型接口"
- "这里需要调用模型 API"
- "接入智谱 GLM / 阿里百炼 / 豆包 / Kimi / MiniMax / 阶跃星辰 / 小米 MiMo / 硅基流动 API"

## English trigger phrases

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
- "How do I authenticate against the Anthropic API"
- "What's the correct request body for Gemini"
- "The streaming is broken, help me fix it"

## Ambiguous phrasing — confirm before routing

These phrases may or may not involve provider-native API work. Check whether the user is asking about a specific provider's API before loading the skill. If unclear, ask:

- "项目里需要 AI 对话功能" → may need provider integration, confirm which provider
- "从 GPT 换成 DeepSeek" → likely a migration, confirm whether they need the request body changed
- "Add AI chat to this app" → confirm which provider before routing

If the user names a specific provider and an API action, trigger immediately.

## Non-trigger examples

These should NOT trigger the skill:

- "哪个大模型更便宜"
- "帮我比较一下 OpenAI 和 Gemini 哪个更强"
- "最近有哪些大模型发布了"
- "帮我写个 prompt 模板"
- "模型参数 temperature 怎么调"
- "Which LLM is the best"
- "Compare GPT-4 vs Claude pricing"

## Few-shot routing examples

### Example 1 — direct integration

User:

> 我要接入 DeepSeek 大模型 API

Route: `integrate-one-provider.md` → `providers/deepseek.md`

### Example 2 — provider migration

User:

> 把现在的 OpenAI 接口改成 Gemini 原生格式

Route: `migrate-between-providers.md` → `providers/openai.md` + `providers/gemini.md` + `comparisons/request-shape-differences.md`

### Example 3 — add streaming

User:

> 给这个项目加 Claude 流式输出

Route: `add-streaming.md` → `providers/anthropic.md` + `comparisons/streaming-differences.md`

### Example 4 — tool calling

User:

> 让模型调用本地函数查天气

This is not enough to trigger provider-native routing by itself because no provider is named.

Confirm first: "你要接哪个模型或 provider 的 API？"

If the user names a provider, then route to `add-tool-calling.md` → target provider file + `comparisons/tool-calling-differences.md`.

### Example 5 — debug request

User:

> 这个 DeepSeek 请求一直报 401

Route: `debug-failed-request.md` → `providers/deepseek.md`

### Example 6 — English direct

User:

> I need to hook up Zhipu GLM in this project

Route: `integrate-one-provider.md` → `providers/zhipu-glm.md`

### Example 7 — ambiguous

User:

> 帮我搭一个聊天机器人，底层用 DeepSeek

This mentions a specific provider (DeepSeek) and implies API integration. Confirm: "你要接入 DeepSeek 的 API 对吗？" If yes, route to `integrate-one-provider.md` → `providers/deepseek.md`.

## Detection heuristic

Trigger if the request contains:

1. A provider name: OpenAI, Anthropic, Claude, Gemini, DeepSeek, 智谱, GLM, 阿里百炼, 通义千问, 豆包, 火山引擎, Kimi, Moonshot, MiniMax, 阶跃星辰, StepFun, 小米 MiMo, 硅基流动, SiliconFlow, etc.
2. An API implementation verb: 接入, 对接, 调用, 集成, 迁移, 切换, 排查, integrate, connect, call, switch, migrate, debug, hook up, wire

If only one of the two is present, check context before triggering.

Safe default:

- provider + API action → trigger immediately
- provider only → confirm whether the user needs implementation work
- API action only → confirm which provider
