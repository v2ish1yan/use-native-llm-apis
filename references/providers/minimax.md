# MiniMax API

## Summary

Use MiniMax's official API when integrating MiniMax text models directly. MiniMax's docs are unusually explicit that text generation can be accessed in three ways:

- HTTP requests
- Anthropic-compatible API
- OpenAI-compatible API

For many development tasks, MiniMax officially recommends the Anthropic-compatible API. That means the compatible layer is not merely a third-party convenience; it is part of MiniMax's own supported surface.

## Auth and Base URLs

International base URLs:

- Anthropic-compatible: `https://api.minimax.io/anthropic`
- OpenAI-compatible: `https://api.minimax.io/v1`

China base URLs:

- Anthropic-compatible: `https://api.minimaxi.com/anthropic`
- OpenAI-compatible: `https://api.minimaxi.com/v1`

Auth:

- `Authorization: Bearer $MINIMAX_API_KEY` for HTTP-style calls
- or the equivalent API-key handling in the chosen compatible SDK

## Primary access patterns

MiniMax's text-generation docs currently emphasize these official patterns:

- Compatible Anthropic API: recommended
- Compatible OpenAI API
- direct HTTP requests for text generation

This skill treats MiniMax as an official provider with multiple first-party access styles.

## Minimal OpenAI-compatible request

```bash
curl https://api.minimax.io/v1/chat/completions \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.5",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Minimal Anthropic-compatible request

```bash
curl https://api.minimax.io/anthropic/v1/messages \
  -H "x-api-key: $MINIMAX_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "MiniMax-M2.5",
    "max_tokens": 512,
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

Response shape depends on the official access mode:

- OpenAI-compatible access returns an OpenAI-like envelope
- Anthropic-compatible access returns Anthropic-like content blocks
- direct HTTP text-generation calls use MiniMax's own HTTP request and response shape

Pick one style per integration and keep your client consistent with it.

## Streaming notes

MiniMax officially supports streaming in its compatible APIs.

- Anthropic-compatible streaming supports text and tool calls, plus interleaved thinking for supported models
- OpenAI-compatible streaming supports chunked streaming responses similar to OpenAI SDK expectations

Important implementation note from MiniMax docs:

- preserve the full assistant response when doing multi-turn tool use
- for some models, `<think>` content or separate reasoning fields must be preserved completely

## Tool-calling notes

MiniMax provides official docs for tool use and interleaved thinking. The key maintenance rule is stronger than in many vendor docs:

- append the full assistant response to history, including tool calls and reasoning fields

That is especially important when using:

- OpenAI-compatible access with `reasoning_details`
- Anthropic-compatible access with content blocks that include thinking and `tool_use`

## Structured-output notes

Structured output depends on the access style you choose:

- OpenAI-compatible flows can follow OpenAI-style JSON-oriented controls where supported
- Anthropic-compatible flows should follow Anthropic-style content and tool semantics

Do not mix the two request styles in one client just because the underlying model is the same.

## Prompt caching notes

MiniMax explicitly documents prompt caching in both:

- text/OpenAI-style flows
- Anthropic-compatible flows

That makes MiniMax more operationally sophisticated than a simple chat-completions-only provider and is worth preserving in future updates.

## Model and coding notes

MiniMax's docs also include a dedicated guide for AI coding tools. This matters because `cc-switch` includes MiniMax coding-oriented presets, and the official docs confirm that MiniMax expects developers to use these models inside agent and coding-tool scenarios.

## Common pitfalls

- Assuming only one official wire format exists
- Losing reasoning or thinking content when appending assistant messages in tool-use flows
- Mixing Anthropic-compatible and OpenAI-compatible assumptions in the same integration
- Hard-coding one region-specific base URL for all deployments
- Treating compatible APIs as unofficial when MiniMax itself documents and recommends them

## Sources

- MiniMax API overview: <https://platform.minimax.io/docs/api-reference/api-overview>
- MiniMax text generation overview: <https://platform.minimax.io/docs/api-reference/text-intro>
- MiniMax text generation guide: <https://platform.minimax.io/docs/guides/text-generation>
- MiniMax compatible Anthropic API: <https://platform.minimax.io/docs/api-reference/text-anthropic-api>
- MiniMax compatible OpenAI API: <https://platform.minimax.io/docs/api-reference/text-openai-api>
- MiniMax tool use and interleaved thinking: <https://platform.minimax.io/docs/api-reference/text-m2-function-call-refer>
- MiniMax AI coding tools guide: <https://platform.minimax.io/docs/api-reference/text-ai-coding-refer>
