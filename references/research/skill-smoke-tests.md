# Skill Smoke Tests

Use this file when changing trigger boundaries, routing rules, or start-path docs.

The point is to test whether an agent can choose the right path quickly without inventing missing details.

## Direct triggers

These should trigger the skill and route immediately:

- "我要接入 DeepSeek API"
- "Use $use-native-llm-apis to write an Anthropic streaming request in TypeScript."
- "Convert this OpenAI request to Gemini native format."
- "这个 DeepSeek 请求一直报 401"
- "Add tool calling to our Claude integration."

## Ambiguous prompts

These should not guess silently. They should ask one small clarification question:

- "给项目加 AI 对话"
- "从 GPT 换成 DeepSeek"
- "让模型查天气"
- "Hook up Claude"

Expected behavior:

- if provider is missing, ask for the provider
- if provider is present but the task is still ambiguous, ask one task question
- do not ask two or three questions at once

## Non-triggers

These should stay out of this skill:

- "哪个大模型更便宜"
- "Compare GPT-4 and Claude pricing"
- "帮我写一个 prompt 模板"
- "最近有哪些模型发布了"

## Provider-path checks

When a provider is known, the route should always go through:

1. `references/start-here.md`
2. one task recipe
3. `references/providers/index.md`
4. the exact provider file

It should never jump straight from `SKILL.md` to a guessed provider slug.
