# Prompt Patterns and Few-Shot Triggers

Use this file when the goal is to recognize that a user is asking for provider-native LLM API integration work, even if they do not explicitly mention this skill.

## Trigger rule

This skill should be loaded when the user is clearly asking to:

- access a large-model API
- integrate or connect a provider API
- switch one model provider to another
- add streaming, tool calling, multimodal input, or structured output to an LLM request
- debug a broken model API request

If the user's request is about using a model API in code, assume this skill is relevant unless the task is clearly only product comparison or pricing research.

## Chinese trigger phrases

- "我要接入 DeepSeek 大模型 API"
- "帮我对接一下 Anthropic/Claude API"
- "这个项目要用 OpenAI API"
- "把现在的 OpenAI 请求改成 Gemini 原生格式"
- "我要在插件里接入 Claude API"
- "给这个项目加大模型流式输出"
- "帮我把工具调用接上"
- "我要让模型返回结构化 JSON"
- "这个模型接口为什么一直 400"
- "帮我排查 401，是不是鉴权格式错了"
- "我要把现在的 LLM 接口从 OpenAI 切到 DeepSeek"
- "项目里需要接大模型接口"
- "这里需要调用模型 API"
- "接入多模态模型接口"
- "写一个 DeepSeek 的 fetch 请求"
- "接入智谱 GLM API"
- "对接阿里百炼/通义千问 API"
- "调用豆包/火山引擎 API"
- "把接口改成 Kimi/Moonshot"
- "接入 MiniMax API"
- "对接阶跃星辰/StepFun API"
- "调用小米 MiMo API"
- "接入硅基流动/SiliconFlow API"
- "通过火山方舟调用模型"
- "用魔搭 ModelScope 推理 API"

## English trigger phrases

- "I need to integrate the DeepSeek API"
- "Hook up Anthropic/Claude in this project"
- "Convert this OpenAI request to Gemini native format"
- "Add streaming to our LLM client"
- "Wire tool calling into this model request"
- "Make the model return structured JSON"
- "Debug why this provider request is returning 400"
- "Switch this project from OpenAI to DeepSeek"
- "Port this from OpenAI to Zhipu GLM"
- "Connect to Alibaba Bailian / DashScope API"
- "Call the Doubao / Volcengine Ark API"
- "Integrate Kimi / Moonshot API"
- "Use MiniMax API in this project"
- "Add StepFun as a provider"
- "Wire up Xiaomi MiMo API"
- "Connect via SiliconFlow"
- "Migrate to OpenRouter"
- "Use AWS Bedrock for Claude"
- "Set up Azure OpenAI endpoint"
- "Call model through NVIDIA NIM"
- "Use ModelScope inference API"
- "Write a fetch request for DeepSeek"
- "How do I authenticate against the Anthropic API"
- "What's the correct request body for Gemini"
- "The streaming is broken, help me fix it"
- "Add function calling to this LLM request"

## Few-shot routing examples

### Example 1 — new integration

User:

> 我要接入 DeepSeek 大模型 API

Correct interpretation:

- This is a provider-native integration task.
- Start with `references/recipes/integrate-one-provider.md`.
- Then open `references/providers/deepseek.md`.

### Example 2 — provider migration

User:

> 把现在的 OpenAI 接口改成 Gemini 原生格式

Correct interpretation:

- This is a provider migration task.
- Start with `references/recipes/migrate-between-providers.md`.
- Then open `references/providers/openai.md`, `references/providers/gemini.md`, and `references/comparisons/request-shape-differences.md`.

### Example 3 — add streaming

User:

> 给这个项目加 Claude 流式输出

Correct interpretation:

- This is a streaming task for one provider.
- Start with `references/recipes/add-streaming.md`.
- Then open `references/providers/anthropic.md` and `references/comparisons/streaming-differences.md`.

### Example 4 — tool calling

User:

> 让模型调用本地函数查天气

Correct interpretation:

- This is a tool-calling task.
- Start with `references/recipes/add-tool-calling.md`.
- Then open the target provider file and `references/comparisons/tool-calling-differences.md`.

### Example 5 — debug request

User:

> 这个 DeepSeek 请求一直报 401

Correct interpretation:

- This is a request-debugging task.
- Start with `references/recipes/debug-failed-request.md`.
- Then open `references/providers/deepseek.md`.

### Example 6 — English integration

User:

> I need to hook up Zhipu GLM in this project

Correct interpretation:

- This is a provider-native integration task.
- Start with `references/recipes/integrate-one-provider.md`.
- Then open `references/providers/zhipu-glm.md`.

## Non-trigger examples

These requests do not automatically require this skill:

- "哪个大模型更便宜"
- "帮我比较一下 OpenAI 和 Gemini 哪个更强"
- "最近有哪些大模型发布了"
- "Which LLM is the best"
- "Compare GPT-4 vs Claude pricing"

Those are research or recommendation tasks unless the user also asks to implement code against the API.

## Simple detection heuristic

If the request contains both:

1. a provider or model API name: OpenAI, Anthropic, Claude, Gemini, DeepSeek, 智谱, GLM, 阿里百炼, 通义千问, 豆包, 火山引擎, Kimi, Moonshot, MiniMax, 阶跃星辰, StepFun, 小米 MiMo, 硅基流动, SiliconFlow, LLM API, 大模型 API, 模型 API, AI API
2. an implementation verb: 接入, 对接, 调用, 集成, 迁移, 切换, 改成, 加上, 排查, 调试, integrate, connect, call, use, switch, migrate, port, wire, hook up, add, debug

then this skill should usually be loaded.
