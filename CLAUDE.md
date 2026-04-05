# use-native-llm-apis for Claude Code

This file provides Claude Code-specific guidance for using the `use-native-llm-apis` skill.

## What this skill is for

Use this skill for **provider-native API implementation work**:

- integrating a provider API
- migrating between providers
- adding streaming, tool calling, or structured output
- debugging auth, endpoint, or request-shape failures

Do not load it for:

- pure model comparison
- pricing research
- prompt engineering only
- generic AI product design without provider API implementation

## Quick route

When a user asks to implement or debug an LLM API:

1. Check [references/recipes/prompt-patterns.md](references/recipes/prompt-patterns.md).
2. Pick the right task recipe from `references/recipes/`.
3. Load the target provider file from `references/providers/`.
4. Load a comparison file from `references/comparisons/` only when needed.

## Trigger boundary

Trigger immediately when the request includes:

- a provider name
- an API implementation action

Examples:

- "我要接入 DeepSeek 大模型 API"
- "帮我对接 Anthropic API"
- "把 OpenAI 改成 Gemini 原生格式"
- "排查这个模型接口为什么 400/401"

If the request only mentions:

- a provider with no API action
- an API action with no provider
- a broad AI feature like chatbot, RAG, or assistant

confirm intent first instead of auto-routing.

## Claude Code usage guidance

### File reading

Use targeted reads instead of loading everything:

```text
Read: references/recipes/integrate-one-provider.md
Read: references/providers/deepseek.md
Read: references/comparisons/streaming-differences.md
```

### Code generation

When generating code:

- prefer raw HTTP shape over abstraction-heavy wrappers
- prefer native `fetch` examples unless the user asks for an SDK
- make streaming examples runnable, not just descriptive
- keep provider-specific fields visible until the request path is proven correct

### Coverage claims

Before claiming a provider is covered, verify against:

- [references/research/coverage-status.md](references/research/coverage-status.md)

Before claiming a detail is current, verify against:

- [references/research/source-registry.md](references/research/source-registry.md)

## Task completion bar

A provider integration task is complete when:

1. One non-stream request path works.
2. Auth header and base URL are correct.
3. Request shape matches the provider reference.
4. Response parsing reads the expected output fields.
5. Provider-specific caveats are reflected in the delivered code or explanation.

## Maintenance notes

- Keep trigger rules aligned with `SKILL.md`.
- Keep routing examples aligned with `references/recipes/prompt-patterns.md`.
- Prefer narrowing ambiguous routes over broadening triggers.
