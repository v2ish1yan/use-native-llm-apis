# Skill Smoke Tests

Use this file when changing trigger boundaries, routing rules, or start-path docs.

The point is to test whether an agent can choose the right path quickly without inventing missing details.

## How to use this file

For each prompt below, verify three things:

1. whether the skill should trigger
2. whether the agent asks at most one clarification question when needed
3. whether routing follows the current source-of-truth path in `SKILL.md` and `references/start-here.md`

## Direct triggers

These should trigger the skill and route immediately:

- "我要接入 DeepSeek API"
- "Use $llm-apis to write an Anthropic streaming request in TypeScript."
- "Convert this OpenAI request to Gemini native format."
- "这个 DeepSeek 请求一直报 401"
- "这个模型接口一直 429，帮我加重试和退避"
- "Add tool calling to our Claude integration."
- "Handle retries and backoff for this provider request."

Expected behavior:

- use `choose-the-right-recipe.md` when it helps disambiguate task class quickly
- choose exactly one task recipe first
- resolve the provider path through `references/providers/index.md`
- open a comparison file only when the task needs one
- reach code-writing only after `references/routing-checklist.md`

## Ambiguous prompts

These should ask one small clarification question instead of guessing:

- "给项目加 AI 对话"
- "从 GPT 换成 DeepSeek"
- "让模型查天气"
- "Hook up Claude"

Expected behavior:

- if provider is missing, ask for the provider
- if provider is present but the task is still ambiguous, ask one task question
- do not ask two or three questions at once
- do not pre-emptively choose a recipe before the ambiguity is resolved
- do not skip directly to a guessed "integration" path just because a provider name appears

## Non-triggers

These should stay out of this skill:

- "哪个大模型更便宜"
- "Compare GPT-4 and Claude pricing"
- "帮我写一个 prompt 模板"
- "最近有哪些模型发布了"

Expected behavior:

- do not load this skill just because an LLM vendor name appears
- do not route into provider files for pricing, news, or generic prompt work

## Provider-path checks

When a provider is known, the route should always go through:

1. `references/start-here.md`
2. `references/recipes/choose-the-right-recipe.md` when needed
3. one task recipe
4. `references/providers/index.md`
5. the exact provider file
6. `references/routing-checklist.md`

It should never jump straight from `SKILL.md` to a guessed provider slug.

## Current manual results

Last manually reviewed: `2026-04-06`

- direct triggers: pass
- ambiguous prompts: pass
- non-triggers: pass
- provider-path order: pass after confirming the route is `start-here -> choose-the-right-recipe (when needed) -> recipe -> providers/index -> provider file -> routing-checklist`

## Notes from the latest review

- PowerShell `Get-Content` may display mojibake for Chinese lines even when the file itself is valid UTF-8.
- Validate suspected encoding issues with a UTF-8-aware reader before rewriting trigger examples.
- Keep this file aligned with `SKILL.md`, `references/start-here.md`, and `references/recipes/prompt-patterns.md`.
