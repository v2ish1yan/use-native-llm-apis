# Zhipu GLM Native API

## Summary

Use Zhipu GLM's official API when integrating directly with BigModel. Its primary chat API is OpenAI-chat-completions-like, but it uses Zhipu's own base URL, model catalog, and platform semantics. Treat it as provider-native, not as a generic OpenAI clone.

## Auth and Base URL

- Base URL: `https://open.bigmodel.cn/api/paas/v4`
- Auth header: `Authorization: Bearer $ZHIPU_API_KEY`
- Content type: `application/json`

For coding-plan scenarios, Zhipu documents a separate coding endpoint:

- `https://open.bigmodel.cn/api/coding/paas/v4`

Use the coding endpoint only for coding-plan integrations, not as the default general API base URL.

## Primary text-generation endpoint

- `POST /chat/completions`

Combined URL:

- `https://open.bigmodel.cn/api/paas/v4/chat/completions`

## Minimal request

```bash
curl https://open.bigmodel.cn/api/paas/v4/chat/completions \
  -H "Authorization: Bearer $ZHIPU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-4.7",
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
- `model`
- `choices`
- `choices[0].message`
- `usage`

This is close to an OpenAI chat-completions response shape.

## Streaming notes

- Enable with `"stream": true`
- Expect an OpenAI-like server-sent event stream
- Incremental text commonly arrives in `choices[*].delta`

Do not assume that every GLM model has identical streaming behavior or feature support. Check model-specific capability notes if a request behaves strangely.

## Tool-calling notes

Zhipu documents function-calling support for GLM family models. The wire shape is close to OpenAI-compatible tool calling.

Typical pattern:

- declare `tools`
- inspect `choices[0].message.tool_calls`
- execute the local function
- send a follow-up request with the assistant tool-call message plus a `role: "tool"` result message

## Structured-output notes

Zhipu documents support for structured output and JSON-oriented machine-readable generation on supported models. Prefer the provider's documented structured-output controls instead of prompt-only "return JSON" wording when the output is consumed by code.

## Multimodal notes

Do not assume every GLM text model accepts images. Use model-specific docs for multimodal variants and keep modality assumptions out of generic chat integrations.

## Embeddings notes

Zhipu's platform supports multiple API categories. Verify the current embeddings endpoint and model support against the official docs before implementation instead of assuming they share the chat endpoint shape.

## Common pitfalls

- Using the coding-plan endpoint for normal chat integrations
- Assuming every OpenAI-style client option maps perfectly onto Zhipu
- Reusing OpenAI model names instead of GLM model names
- Assuming tool-calling and structured-output behavior are identical across all GLM variants

## Sources

- Zhipu API introduction: <https://docs.bigmodel.cn/cn/api/introduction>
- Zhipu chat completions reference: <https://docs.bigmodel.cn/api-reference>
- Zhipu GLM model guide: <https://docs.bigmodel.cn/cn/guide/models/text/glm-4>
