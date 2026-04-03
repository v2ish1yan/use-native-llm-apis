# Kimi / Moonshot API

## Summary

Use Moonshot's official API when integrating Kimi directly. Moonshot's public API is intentionally OpenAI-chat-completions-compatible, but the platform also provides official guides for streaming, tool calls, JSON mode, token counting, and model-specific usage. Treat it as an official provider API with an OpenAI-like wire shape.

## Auth and Base URL

- Base URL: `https://api.moonshot.cn/v1`
- Auth header: `Authorization: Bearer $MOONSHOT_API_KEY`
- Content type: `application/json`

## Primary text-generation endpoint

- `POST /chat/completions`

Combined URL:

- `https://api.moonshot.cn/v1/chat/completions`

## Minimal request

```bash
curl https://api.moonshot.cn/v1/chat/completions \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k2.5",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

Common fields to read:

- `id`
- `object`
- `model`
- `choices`
- `choices[0].message`
- `usage`

This is close to an OpenAI chat-completions response shape.

## Streaming notes

- Enable with `"stream": true`
- Streaming response content type is `text/event-stream`
- Incremental chunks arrive as SSE frames prefixed with `data:`
- The stream ends with `data: [DONE]`

Moonshot's official streaming guide shows delta-style chunks such as:

- `choices[0].delta.content`
- final chunk with `finish_reason`
- usage information in the last chunk

This means a simple OpenAI-style SSE parser is a good starting point for Kimi.

## Tool-calling notes

Moonshot provides an official tool-calls guide. The tool declaration shape follows the familiar OpenAI-style pattern:

- top-level `tools`
- each tool has `type: "function"`
- function definition under `function`

Typical continuation flow:

1. inspect `choices[0].message.tool_calls`
2. parse the function arguments
3. execute the local tool
4. append the assistant tool-call turn and a `role: "tool"` message
5. send the updated conversation back to `/chat/completions`

For streaming tool calls, Moonshot's guide also shows that `tool_calls` can arrive incrementally inside streaming deltas. If you stream tool-calling responses, assemble the tool call pieces carefully before execution.

## Structured-output notes

Moonshot documents `JSON Mode` through:

- `response_format: { "type": "json_object" }`

Important platform-specific notes:

- JSON Mode is for JSON objects, not arbitrary JSON arrays
- the prompt should still explicitly describe the expected JSON shape
- if output is truncated, check `finish_reason == "length"` and increase `max_tokens`

## Multimodal notes

Moonshot's current docs distinguish text-generation and multimodal model families. Do not assume every Kimi model accepts images or files; check the model-specific guide before wiring multimodal inputs.

## Embeddings and token notes

Moonshot's docs explicitly reference token counting through:

- `POST /tokenizers/estimate-token-count`

This is especially useful for streaming flows where the final usage chunk might be missing due to interruption.

## Common pitfalls

- Treating Kimi as a generic OpenAI relay and ignoring Moonshot-specific docs
- Forgetting that streaming is SSE with `data:` frames and a final `[DONE]`
- Assuming tool calls only arrive in non-stream mode
- Using JSON Mode without clearly describing the target object schema in the prompt
- Forgetting that Kimi's newer model lineup changes over time, so hard-coded model names may age quickly

## Sources

- Moonshot docs introduction: <https://platform.moonshot.cn/docs/introduction>
- Moonshot quick start guide: <https://platform.moonshot.cn/blog/posts/kimi-api-quick-start-guide>
- Moonshot streaming guide: <https://platform.moonshot.cn/docs/guide/utilize-the-streaming-output-feature-of-kimi-api>
- Moonshot tool calls guide: <https://platform.moonshot.cn/docs/guide/use-kimi-api-to-complete-tool-calls>
- Moonshot JSON mode guide: <https://platform.moonshot.cn/docs/guide/use-json-mode-feature-of-kimi-api>
