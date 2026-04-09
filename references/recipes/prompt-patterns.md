# Prompt Patterns and Few-Shot Triggers

Use this file to decide whether a user's request should trigger the `llm-apis` skill.

## Core trigger rule

Trigger when both are true:

1. the user names a provider or clearly implies a provider-native API
2. the user asks for implementation work in code

Implementation work includes:

- integrate
- connect
- call
- migrate
- switch
- debug
- stream
- tool calling
- structured output
- 接入
- 对接
- 调用
- 迁移
- 切换
- 排查

Do not trigger for comparison, pricing, prompt writing, or general AI planning unless the request also asks to implement against a specific provider API.

## Fast decision rules

- provider + API action -> trigger immediately
- provider only -> confirm whether the user needs implementation work
- API action only -> confirm which provider
- neither -> do not trigger

Ask at most one clarification question before routing.

## Task-router hints

- "接入 / 对接 / 调用 / integrate / hook up" -> usually `integrate-one-provider.md`
- "迁移 / 改成 / switch / convert" -> usually `migrate-between-providers.md`
- "流式 / streaming / SSE" -> usually `add-streaming.md`
- "工具调用 / function call / tool use" -> usually `add-tool-calling.md`
- "结构化 JSON / schema / structured output" -> usually `add-structured-output.md`
- "`400` / `401` / `422` / request invalid" -> usually `debug-failed-request.md`
- "`429` / `5xx` / retry / backoff / Retry-After" -> usually `handle-rate-limits-and-errors.md`

## Chinese trigger examples

- "我要接入 DeepSeek 大模型 API"
- "帮我对接 Anthropic / Claude API"
- "这个项目要用 OpenAI API"
- "把现在的 OpenAI 请求改成 Gemini 原生格式"
- "给这个项目加大模型流式输出"
- "帮我把工具调用接进去"
- "我要让模型返回结构化 JSON"
- "这个模型接口为什么一直 400"
- "帮我排查 401，是不是鉴权格式错了"
- "我要把 LLM 接口从 OpenAI 切到 DeepSeek"

## English trigger examples

- "I need to integrate the DeepSeek API"
- "Hook up Anthropic/Claude in this project"
- "Convert this OpenAI request to Gemini native format"
- "Add streaming to our LLM client"
- "Wire tool calling into this model request"
- "Make the model return structured JSON"
- "Debug why this provider request is returning 400"
- "Handle retries and backoff for this provider request"
- "This model API keeps returning 429"
- "Switch this project from OpenAI to DeepSeek"

## Ambiguous prompts

These should ask one clarification question instead of guessing:

- "给项目加 AI 对话"
- "从 GPT 换成 DeepSeek"
- "让模型查天气"
- "Add AI chat to this app"
- "Hook up Claude"
- "把 Claude 接进去"
- "接个 DeepSeek"

## Non-trigger examples

These should not trigger the skill:

- "哪个大模型更便宜"
- "帮我比较一下 OpenAI 和 Gemini 哪个更强"
- "最近有哪些大模型发布了"
- "帮我写个 prompt 模板"
- "模型参数 temperature 怎么调"
- "Which LLM is the best"
- "Compare GPT-4 vs Claude pricing"

## Few-shot routing examples

### Example 1 - direct integration

User:

> 我要接入 DeepSeek 大模型 API

Route:

1. `references/start-here.md`
2. `choose-the-right-recipe.md`
3. `integrate-one-provider.md`
4. `providers/index.md`
5. `providers/deepseek.md`

### Example 2 - provider migration

User:

> 把现在的 OpenAI 接口改成 Gemini 原生格式

Route:

1. `references/start-here.md`
2. `choose-the-right-recipe.md`
3. `migrate-between-providers.md`
4. `providers/index.md`
5. `providers/openai.md`
6. `providers/gemini.md`
7. `comparisons/request-shape-differences.md`

### Example 3 - add streaming

User:

> 给这个项目加 Claude 流式输出

Route:

1. `references/start-here.md`
2. `choose-the-right-recipe.md`
3. `add-streaming.md`
4. `providers/index.md`
5. `providers/anthropic.md`
6. `comparisons/streaming-differences.md`

### Example 4 - tool calling with missing provider

User:

> 让模型调用本地函数查天气

Behavior:

- do not route yet
- ask one question: "你要接哪个 provider 的 API？"

### Example 5 - debug request

User:

> 这个 DeepSeek 请求一直报 401

Route:

1. `references/start-here.md`
2. `choose-the-right-recipe.md`
3. `debug-failed-request.md`
4. `providers/index.md`
5. `providers/deepseek.md`

### Example 6 - rate limit and retry

User:

> 这个 LLM 接口一直 429，帮我加重试和退避

Route:

1. `references/start-here.md`
2. `choose-the-right-recipe.md`
3. `handle-rate-limits-and-errors.md`
4. `providers/index.md`
5. the exact provider file

### Example 7 - English direct retry work

User:

> Handle retries and backoff for this Anthropic request

Route:

1. `references/start-here.md`
2. `choose-the-right-recipe.md`
3. `handle-rate-limits-and-errors.md`
4. `providers/index.md`
5. `providers/anthropic.md`

### Example 8 - English direct

User:

> I need to hook up Zhipu GLM in this project

Route:

1. `references/start-here.md`
2. `choose-the-right-recipe.md`
3. `integrate-one-provider.md`
4. `providers/index.md`
5. `providers/zhipu-glm.md`

### Example 9 - ambiguous but likely integration

User:

> 帮我搭一个聊天机器人，底层用 DeepSeek

Behavior:

- ask one question: "你要接入 DeepSeek 的原生 API，对吗？"
- if yes, route through `references/start-here.md` -> `choose-the-right-recipe.md` -> `integrate-one-provider.md` -> `providers/index.md` -> `providers/deepseek.md`
