# DeepSeek Native API

## Summary

DeepSeek's official API is intentionally close to the OpenAI chat-completions style, but it is still a provider-native integration because the base URL, model catalog, operational behavior, and roadmap come from DeepSeek's own platform. Treat it as "officially OpenAI-compatible," not "identical to OpenAI in every edge case."

## Auth and Base URL

- Base URL: `https://api.deepseek.com`
- Auth header: `Authorization: Bearer $DEEPSEEK_API_KEY`
- Content type: `application/json`

## Primary text-generation endpoint

- `POST /chat/completions`

DeepSeek also documents a `/v1` path prefix for compatibility, but the provider notes that `v1` is a path convention rather than a model-version boundary.

## Minimal request

```bash
curl https://api.deepseek.com/chat/completions \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      { "role": "user", "content": "Write a one-line hello in Python." }
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

This is close to the OpenAI chat-completions shape.

## Streaming notes

- Enable with `"stream": true`
- DeepSeek streams in an OpenAI-like SSE pattern
- Partial text normally arrives in `choices[*].delta`

Even when the shape looks familiar, keep provider-specific retry, model, and rate-limit handling separate from OpenAI assumptions.

## Tool-calling notes

DeepSeek documents function calling in an OpenAI-compatible style. If you already have a chat-completions tool layer, the payload shape will feel familiar.

Still verify:

- which models support function calling
- whether strict schema behavior matches your expectations

Minimal function-calling request:

```bash
curl https://api.deepseek.com/chat/completions \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      { "role": "user", "content": "What is the weather in Shanghai?" }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "lookup_weather",
          "description": "Get the weather for a city",
          "parameters": {
            "type": "object",
            "properties": {
              "city": { "type": "string" }
            },
            "required": ["city"]
          }
        }
      }
    ]
  }'
```

Typical continuation flow:

1. inspect `choices[0].message.tool_calls`
2. execute the requested function locally
3. append the tool result message in the next request using the OpenAI-compatible chat pattern

Minimal follow-up request after executing the tool:

```json
{
  "model": "deepseek-chat",
  "messages": [
    { "role": "user", "content": "What is the weather in Shanghai?" },
    {
      "role": "assistant",
      "content": null,
      "tool_calls": [
        {
          "id": "call_123",
          "type": "function",
          "function": {
            "name": "lookup_weather",
            "arguments": "{\"city\":\"Shanghai\"}"
          }
        }
      ]
    },
    {
      "role": "tool",
      "tool_call_id": "call_123",
      "content": "{\"temperature_c\":22,\"condition\":\"Cloudy\"}"
    }
  ]
}
```

Minimal TypeScript chat-client flow:

```ts
type ChatMessage =
  | { role: "user"; content: string }
  | { role: "assistant"; content: string | null; tool_calls?: unknown[] }
  | { role: "tool"; tool_call_id: string; content: string };

async function complete(messages: ChatMessage[]) {
  const response = await fetch("https://api.deepseek.com/chat/completions", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.DEEPSEEK_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "deepseek-chat",
      messages,
      tools: [
        {
          type: "function",
          function: {
            name: "lookup_weather",
            description: "Get the weather for a city",
            parameters: {
              type: "object",
              properties: {
                city: { type: "string" },
              },
              required: ["city"],
            },
          },
        },
      ],
    }),
  });

  if (!response.ok) {
    throw new Error(`DeepSeek request failed: ${response.status} ${response.statusText}`);
  }

  return response.json();
}
```

Practical parsing rule:

- read `choices[0].message.tool_calls`
- parse `tool_calls[*].function.arguments` as JSON
- execute your local function
- append a `role: "tool"` message with the matching `tool_call_id`
- send the full conversation back for the final answer

## Structured-output notes

DeepSeek documents JSON output behavior. Use the provider's documented JSON mode or structured-output pattern instead of relying only on prompt wording when downstream code expects valid JSON.

## Multimodal notes

Do not assume every DeepSeek model accepts image input. Check the current model-specific docs before wiring a multimodal request path.

## Embeddings notes

Embeddings are not the core focus of the pilot reference. Verify current DeepSeek embeddings support against official docs before implementation.

## Common pitfalls

- Assuming DeepSeek supports every modern OpenAI Responses feature just because chat completions look similar
- Treating `/v1` as a distinct API generation rather than a compatibility path
- Reusing OpenAI model ids instead of DeepSeek model ids
- Assuming multimodal or schema features are universally available across DeepSeek models
- Sending only the tool result without preserving the assistant tool-call message in the follow-up request

## Sources

- DeepSeek quick start: <https://api-docs.deepseek.com/>
- DeepSeek chat completions: <https://api-docs.deepseek.com/api/create-chat-completion>
- DeepSeek function calling: <https://api-docs.deepseek.com/guides/function_calling>
- DeepSeek JSON output: <https://api-docs.deepseek.com/guides/json_mode>
