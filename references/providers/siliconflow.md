# SiliconFlow API

## Summary

Use SiliconFlow when integrating many hosted models through SiliconFlow's official platform. SiliconFlow is a hosted aggregation layer with a broad model catalog and strong OpenAI-style HTTP support, but it also exposes extra platform-specific fields such as `reasoning_content`, `enable_thinking`, and model-specific controls.

## Auth and Base URL

- Base URL: `https://api.siliconflow.com/v1`
- Auth header: `Authorization: Bearer $SILICONFLOW_API_KEY`
- Content type: `application/json`

## Primary text-generation endpoint

- `POST /chat/completions`

Additional documented endpoints include:

- `POST /messages`
- `POST /completions`
- `POST /embeddings`

## Minimal request

```bash
curl https://api.siliconflow.com/v1/chat/completions \
  -H "Authorization: Bearer $SILICONFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/QwQ-32B",
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

## Response shape

SiliconFlow's chat API is OpenAI-chat-completions-like but includes platform-specific enrichments such as:

- `choices[0].message.reasoning_content`
- `choices[0].message.tool_calls`

That means client code should not discard unknown fields if reasoning metadata matters for the workflow.

## Streaming notes

- Enable with `"stream": true`
- Stream terminates with `data: [DONE]`
- Incremental output follows OpenAI-style delta chunks

## Tool-calling notes

SiliconFlow supports `tools` on the chat-completions endpoint. The public reference uses OpenAI-style tool declarations and returns `tool_calls` in the assistant message.

One important platform-specific note:

- for some reasoning-capable models, function calling may require `enable_thinking: false`

## Structured-output notes

SiliconFlow supports `response_format`, which makes it practical for machine-readable JSON outputs. Because it fronts many model families, verify structured-output behavior per model if the task is strict or high-stakes.

## Embeddings notes

SiliconFlow also documents:

- `POST /v1/embeddings`

This is useful when the project wants both generation and vector search from the same hosted platform.

## Common pitfalls

- Treating SiliconFlow as a plain OpenAI clone and ignoring extra response fields
- Assuming all hosted models support the same features
- Forgetting that model-specific controls such as `enable_thinking` can affect tool-calling behavior

## Sources

- SiliconFlow chat completions reference: <https://docs.siliconflow.com/en/api-reference/chat-completions/chat-completions>
- SiliconFlow alternate text conversation page: <https://docs.siliconflow.com/en/api-reference/chat-completions/chat-completions_copy>
- SiliconFlow messages endpoint: <https://docs.siliconflow.com/en/api-reference/chat-completions/messages>
- SiliconFlow embeddings reference: <https://docs.siliconflow.com/en/api-reference/embeddings/create-embeddings>
