# use-native-llm-apis for Claude Code

This file provides Claude Code-specific guidance for using the `use-native-llm-apis` skill.

## Quick Start

When a user asks to integrate, migrate, or debug an LLM API:

1. **Check if this skill applies** - See [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md)
2. **Route to the right recipe** - Pick one:
   - `references/recipes/integrate-one-provider.md`
   - `references/recipes/migrate-between-providers.md`
   - `references/recipes/add-streaming.md`
   - `references/recipes/add-tool-calling.md`
   - `references/recipes/add-structured-output.md`
   - `references/recipes/debug-failed-request.md`
3. **Load provider reference** - From `references/providers/`
4. **Load comparison if needed** - From `references/comparisons/`

## Claude Code Specific Behaviors

### File Reading

Use `Read` tool to load reference files. Prefer targeted reads over full directory listings:

```
Read: references/providers/deepseek.md
Read: references/recipes/add-streaming.md
```

### Code Generation

When generating code for the user:

- Prefer native `fetch` examples over SDK wrappers
- Keep code close to the provider's raw wire format
- Include complete working examples, not fragments
- For streaming, provide full `ReadableStream` or SSE parsing examples

### Provider Status Check

Before claiming a provider is covered, verify in [references/research/coverage-status.md](references/research/coverage-status.md).

### Source Documentation

When bundled references are insufficient, check [references/research/source-registry.md](references/research/source-registry.md) for official doc URLs before web search.

## Trigger Phrases (Chinese)

Common user phrases that should activate this skill:

- "我要接入 DeepSeek 大模型 API"
- "帮我对接 Anthropic API"
- "把 OpenAI 改成 Gemini 原生格式"
- "给这个项目加上流式输出"
- "帮我加工具调用"
- "让模型返回结构化 JSON"
- "排查这个模型接口为什么 400/401"

## Exit Criteria for Tasks

A task is complete when:

1. One verified request path works (non-streaming base case)
2. Auth headers and base URL are correct
3. Request body shape matches provider's documented format
4. Response parsing extracts the expected fields
5. Provider-specific caveats are noted in comments

## Maintenance Notes

- Update `references/research/source-registry.md` when adding new official doc URLs
- Update `references/research/coverage-status.md` when provider status changes
- Prefer official provider docs over community blog posts
