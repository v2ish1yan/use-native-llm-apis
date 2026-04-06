# Novita AI API

## Summary

Use Novita AI when integrating through Novita's official hosted platform. For LLM APIs, Novita explicitly documents OpenAI compatibility as the primary development path, while also exposing broader platform APIs for billing, account management, images, video, reranking, and compute.

Treat Novita's LLM surface as an official OpenAI-compatible provider layer, not as a fully native non-OpenAI schema.

## Auth and Base URL

Base URLs documented by Novita:

- general API base: `https://api.novita.ai`
- OpenAI-compatible base: `https://api.novita.ai/openai`

Auth header:

- `Authorization: Bearer $NOVITA_API_KEY`

## Primary LLM access pattern

Novita's official docs say its LLM APIs follow the OpenAI API standard. That means:

- OpenAI SDKs can be reused
- the main runtime route should be treated as OpenAI-compatible
- the platform's LLM docs are organized around chat completions, completions, embeddings, rerank, model listing, and batch/file operations

## Minimal chat-completions request

```bash
curl https://api.novita.ai/openai/v1/chat/completions \
  -H "Authorization: Bearer $NOVITA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek/deepseek-r1",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

Typical response field for text:

- `choices[0].message.content`

## Streaming notes

Novita's LLM guide explicitly says chat completions support:

- non-streaming mode
- streaming mode

The chat-completions API reference also documents:

- `stream`
- `stream_options.include_usage`

Practical rule:

- on the LLM surface, treat streaming as OpenAI-style chat-completions streaming
- still verify model-specific support before promising streaming for every upstream model

## Tool-calling notes

Novita's public guides include a dedicated Function Calling guide and route users back to the chat-completions reference for the exact schema.

That means function calling is part of the officially documented LLM surface, not just an inferred compatibility claim.

Practical rule:

- keep OpenAI-style tools expectations
- verify model support, because Novita fronts many upstream models

## Structured-output notes

Because Novita's LLM surface is OpenAI-compatible, the safest assumption is:

- start from OpenAI-compatible response-format expectations
- verify strict structured-output behavior per model family when the task is high-stakes

Do not assume every hosted upstream model behaves identically just because the outer API is uniform.

## Embeddings and rerank notes

Novita's LLM API reference also documents:

- embeddings
- rerank
- model listing and retrieval
- batch operations and files

This makes Novita stronger than a minimal chat-only wrapper. It is a broader official hosted LLM platform.

## Development guidance

When integrating Novita AI:

1. use the OpenAI-compatible base URL for LLM work
2. send one minimal chat-completions request
3. verify the exact model id
4. add streaming, tools, or structured-output behavior only after the base request works

## Common pitfalls

- Treating Novita as a native non-OpenAI schema instead of an official OpenAI-compatible surface
- Assuming all upstream models behave identically just because the surface is OpenAI-compatible
- Mixing the general platform base URL and the OpenAI-compatible base without noticing which one your client expects
- Forgetting that model-specific capability still matters for streaming or function calling

## Sources

- Novita API reference overview: <https://novita.ai/docs/api-reference>
- Novita authentication: <https://novita.ai/docs/api-reference/basic-authentication>
- Novita model APIs introduction: <https://novita.ai/docs/api-reference/model-apis-introduction>
- Novita create chat completion: <https://novita.ai/docs/api-reference/model-apis-llm-create-chat-completion>
- Novita LLM API guide: <https://novita.ai/docs/guides/llm-api>
- Novita function calling guide: <https://novita.ai/docs/guides/llm-function-calling>
