# OpenRouter API

## Summary

Use OpenRouter when the goal is to route one API surface across many upstream model providers. Unlike the native vendor docs in this skill, OpenRouter is explicitly a normalization layer. Its value is consistency, model breadth, and extra platform features such as plugins and generation-level metadata.

## Auth and Base URL

- Base URL: `https://openrouter.ai/api/v1`
- Auth header: `Authorization: Bearer $OPENROUTER_API_KEY`
- Optional attribution headers:
  - `HTTP-Referer`
  - `X-OpenRouter-Title`
  - `X-OpenRouter-Categories`

## Primary text-generation endpoint

- `POST /chat/completions`

## Minimal request

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-5.2",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

OpenRouter normalizes responses to an OpenAI-chat-completions-like schema:

- `id`
- `choices`
- `model`
- `object`
- `usage`

For streaming, the final chunk may include usage data with an empty `choices` array before `[DONE]`.

## Structured-output notes

OpenRouter supports:

- `response_format: { "type": "json_object" }`
- `response_format: { "type": "json_schema", "json_schema": { ... } }`

This is one of the strongest reasons to treat OpenRouter as its own provider doc instead of lumping it into generic gateways.

## Tool and plugin notes

OpenRouter supports:

- model tools via normalized request formats
- plugins such as web search, file parsing, and response healing

These are OpenRouter platform features, not guaranteed upstream-native features.

## Common pitfalls

- Assuming every upstream provider behaves identically even after normalization
- Treating OpenRouter as if it preserves all native vendor semantics
- Forgetting that plugins are OpenRouter-specific extensions

## Sources

- OpenRouter API overview: <https://openrouter.ai/docs/api/reference/overview/>
- OpenRouter OpenAPI YAML: <https://openrouter.ai/openapi.yaml>
- OpenRouter embeddings docs: <https://openrouter.ai/docs/api-reference/embeddings>
