# Prompt Patterns and Few-Shot Triggers

Use this file when the goal is to recognize that a user is asking for provider-native LLM API integration work — even if they never mention "API" or name this skill.

## Trigger rule

Load this skill when the user is building something that talks to a model in code. This covers:

- explicit API work: integrate, connect, call, switch, migrate, debug a model API
- **implicit intent**: building an AI agent/chatbot/assistant/RAG/copilot that needs a model backend
- **feature work**: adding streaming, tool calling, multimodal, structured output to an existing model call
- **debugging**: model response errors, slow responses, wrong format, auth failures

Bias toward loading. Only skip if the request is purely market comparison or pricing research with zero code intent.

## Direct Chinese triggers (mentions API/provider)

- "我要接入 DeepSeek 大模型 API"
- "帮我对接一下 Anthropic/Claude API"
- "这个项目要用 OpenAI API"
- "把现在的 OpenAI 请求改成 Gemini 原生格式"
- "给这个项目加大模型流式输出"
- "帮我把工具调用接上"
- "我要让模型返回结构化 JSON"
- "这个模型接口为什么一直 400"
- "帮我排查 401，是不是鉴权格式错了"
- "接入智谱 GLM / 阿里百炼 / 豆包 / Kimi / MiniMax / 阶跃星辰 / 小米 MiMo / 硅基流动 API"

## Natural-language Chinese triggers (no "API" in the sentence)

These users describe WHAT they build, not the API call. They still need this skill.

- "我要写一个 AI agent，用 MiniMax 的大模型"
- "帮我搭一个聊天机器人，底层用 DeepSeek"
- "做一个知识库问答系统，模型用智谱"
- "项目里需要 AI 对话功能"
- "帮我写个智能客服，接大模型"
- "我要搭一个 RAG，用 Claude 做后端"
- "这个 agent 要能调用工具/搜索/查数据库"
- "帮我建一个 AI 助手/copilot"
- "用大模型做文本摘要/翻译/情感分析/代码生成"
- "帮我调一下模型参数 temperature/top_p"
- "从 GPT 换成 DeepSeek/Claude/Gemini"
- "模型回复太慢了帮我优化一下"
- "我的 AI 应用需要加多轮对话记忆"
- "给这个页面加一个 AI 对话窗口"
- "写个 prompt 模板让模型"
- "这个 bot 用的是 Claude 吧"（暗示要接入/切换）
- "用 MiniMax 的模型做这个"
- "后端接哪个模型好"（后续必涉及接入代码）

## Direct English triggers

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

## Natural-language English triggers

- "Build an AI agent that uses MiniMax as the model"
- "I want to create a chatbot powered by DeepSeek"
- "Add AI chat functionality to this app"
- "My agent needs to call tools and search the web"
- "Build a RAG pipeline with Claude as the backend"
- "Create an AI copilot/assistant for this project"
- "The model response is slow, help me optimize"
- "Switch the model from GPT to Gemini"
- "I need multi-turn conversation memory for my AI app"
- "Use an LLM for text summarization/translation/coding"
- "This bot uses Claude right?"（implies integration/switch）

## Few-shot routing examples

### Example 1 — direct integration

User:

> 我要接入 DeepSeek 大模型 API

Route: `integrate-one-provider.md` → `providers/deepseek.md`

### Example 2 — natural language (build an agent)

User:

> 我要写一个 AI agent，用 MiniMax 的大模型

Correct interpretation: This is a new integration disguised as "build an agent." The user needs MiniMax API wired in.

Route: `integrate-one-provider.md` → `providers/minimax.md`

### Example 3 — provider migration

User:

> 把现在的 OpenAI 接口改成 Gemini 原生格式

Route: `migrate-between-providers.md` → `providers/openai.md` + `providers/gemini.md` + `comparisons/request-shape-differences.md`

### Example 4 — add streaming

User:

> 给这个项目加 Claude 流式输出

Route: `add-streaming.md` → `providers/anthropic.md` + `comparisons/streaming-differences.md`

### Example 5 — tool calling

User:

> 让模型调用本地函数查天气

Route: `add-tool-calling.md` → target provider file + `comparisons/tool-calling-differences.md`

### Example 6 — debug request

User:

> 这个 DeepSeek 请求一直报 401

Route: `debug-failed-request.md` → `providers/deepseek.md`

### Example 7 — natural language (build a chatbot)

User:

> 帮我搭一个聊天机器人，底层用 DeepSeek

Correct interpretation: Building a chatbot = needs streaming chat API. Provider is DeepSeek.

Route: `integrate-one-provider.md` → `add-streaming.md` → `providers/deepseek.md`

### Example 8 — natural language (RAG)

User:

> 做一个知识库问答系统，模型用智谱

Correct interpretation: RAG system = needs embedding + chat API. Provider is Zhipu GLM.

Route: `integrate-one-provider.md` → `providers/zhipu-glm.md`

### Example 9 — English natural language (agent)

User:

> Build an AI agent that uses MiniMax as the model

Correct interpretation: Agent = needs chat + tool calling API. Provider is MiniMax.

Route: `integrate-one-provider.md` → `add-tool-calling.md` → `providers/minimax.md`

### Example 10 — performance optimization

User:

> 模型回复太慢了帮我优化一下

Correct interpretation: Optimization likely involves streaming, async, or switching provider.

Route: Check current provider → `add-streaming.md` → relevant provider file

## Non-trigger examples

- "哪个大模型更便宜" — pricing only
- "帮我比较一下 OpenAI 和 Gemini 哪个更强" — benchmark only
- "最近有哪些大模型发布了" — news only
- "Which LLM is the best" — opinion only
- "Compare GPT-4 vs Claude pricing" — market research only

Exception: if the user adds ANY implementation intent ("比较一下...然后帮我接进来"), trigger immediately.

## Detection heuristic

Trigger if the request contains ANY of these patterns:

**Pattern A — explicit (provider + verb):**
1. A provider name: OpenAI, Anthropic, Claude, Gemini, DeepSeek, 智谱, GLM, 阿里百炼, 通义千问, 豆包, 火山引擎, Kimi, Moonshot, MiniMax, 阶跃星辰, StepFun, 小米 MiMo, 硅基流动, SiliconFlow, etc.
2. An API verb: 接入, 对接, 调用, 集成, 迁移, 切换, 排查, integrate, connect, call, switch, migrate, debug, hook up, wire

**Pattern B — implicit (build + model):**
1. A build intent: 写, 搭建, 做, 创建, build, create, make, develop, write
2. An AI concept: AI agent, chatbot, 助手, 机器人, copilot, RAG, 智能客服, 对话, assistant
3. A model reference (optional but strengthens signal): 用大模型, 用 XX 模型, 底层用, powered by, uses model

**Pattern C — feature (existing model code + enhancement):**
1. A model reference in existing code context
2. A feature request: 流式, 工具调用, 结构化, streaming, tool calling, structured output, JSON mode
