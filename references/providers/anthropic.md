# Anthropic Native API

## Summary

Use Anthropic's native Messages API when integrating Claude directly. Anthropic's request and streaming semantics differ meaningfully from both OpenAI Responses and Gemini `contents`, especially around headers, content blocks, and tool-use responses.

## Auth and Base URL

- Base URL: `https://api.anthropic.com`
- Main endpoint: `POST /v1/messages`
- Required headers:
  - `x-api-key: $ANTHROPIC_API_KEY`
  - `anthropic-version: 2023-06-01`
  - `content-type: application/json`

## Primary text-generation endpoint

- `POST /v1/messages`

## Minimal request

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-5",
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

Common fields to read:

- `id`
- `type`
- `role`
- `model`
- `content`
- `stop_reason`
- `usage`

Text usually arrives in `content` blocks with `type: "text"`.

## Streaming notes

- Enable with `"stream": true`
- Anthropic streams server-sent events with named event types
- Common events include:
  - `message_start`
  - `content_block_start`
  - `content_block_delta`
  - `message_delta`
  - `message_stop`

Your stream parser should be event-aware. Do not assume OpenAI-style delta payloads.

Minimal streaming request:

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 512,
    "stream": true,
    "messages": [
      {
        "role": "user",
        "content": "Stream a short Python hello."
      }
    ]
  }'
```

Typical parser strategy:

1. read SSE events, not raw JSON lines
2. append text only from `content_block_delta`
3. stop on `message_stop`

Minimal TypeScript example for Node 18+:

```ts
type AnthropicStreamEvent =
  | { type: "message_start" }
  | { type: "content_block_start" }
  | { type: "content_block_delta"; delta?: { type?: string; text?: string } }
  | { type: "message_delta" }
  | { type: "message_stop" }
  | { type: string; [key: string]: unknown };

export async function streamAnthropicMessage() {
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    throw new Error("Missing ANTHROPIC_API_KEY");
  }

  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "x-api-key": apiKey,
      "anthropic-version": "2023-06-01",
      "content-type": "application/json",
    },
    body: JSON.stringify({
      model: "claude-sonnet-4-5",
      max_tokens: 512,
      stream: true,
      messages: [
        {
          role: "user",
          content: "Stream a short TypeScript hello world example.",
        },
      ],
    }),
  });

  if (!response.ok || !response.body) {
    throw new Error(`Anthropic request failed: ${response.status} ${response.statusText}`);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";
  let fullText = "";

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });

    while (buffer.includes("\n\n")) {
      const boundary = buffer.indexOf("\n\n");
      const rawEvent = buffer.slice(0, boundary);
      buffer = buffer.slice(boundary + 2);

      const lines = rawEvent.split("\n");
      let eventName = "";
      const dataLines: string[] = [];

      for (const line of lines) {
        if (line.startsWith("event:")) {
          eventName = line.slice(6).trim();
        } else if (line.startsWith("data:")) {
          dataLines.push(line.slice(5).trim());
        }
      }

      if (!dataLines.length) continue;

      const dataText = dataLines.join("\n");
      let parsed: AnthropicStreamEvent;

      try {
        parsed = JSON.parse(dataText);
      } catch {
        continue;
      }

      if (eventName === "content_block_delta" && parsed.type === "content_block_delta") {
        const chunk = parsed.delta?.text ?? "";
        if (chunk) {
          fullText += chunk;
          process.stdout.write(chunk);
        }
      }

      if (eventName === "message_stop") {
        process.stdout.write("\n");
        return fullText;
      }
    }
  }

  return fullText;
}
```

## Tool-calling notes

Declare tools with a top-level `tools` array. Each tool uses `input_schema`.

Minimal tool shape:

```json
{
  "name": "lookup_weather",
  "description": "Get the weather for a city",
  "input_schema": {
    "type": "object",
    "properties": {
      "city": { "type": "string" }
    },
    "required": ["city"]
  }
}
```

When Claude calls a tool, the response contains a `tool_use` content block. Return the tool result in the next user message as a `tool_result` block tied to the tool-use id.

Minimal tool result follow-up:

```json
{
  "model": "claude-sonnet-4-5",
  "max_tokens": 512,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_123",
          "content": "{\"temperature_c\":22}"
        }
      ]
    }
  ]
}
```

## Structured-output notes

Anthropic supports structured workflows, but the most stable portable pattern is still tool-based schema enforcement or carefully constrained JSON output. Do not assume OpenAI-style `json_schema` request fields exist with identical semantics.

If strict machine-readable output is required, tools are usually the safest baseline.

## Multimodal notes

Anthropic supports content blocks beyond plain text. Keep multimodal payloads in the `content` array instead of inventing separate top-level keys.

## Embeddings notes

Anthropic's core public Messages API references are centered on generation and tool use. Do not assume a separate embeddings API in the same shape without checking current official docs.

## Common pitfalls

- Omitting the required `anthropic-version` header
- Sending OpenAI-style `tools[].parameters` instead of `input_schema`
- Parsing stream chunks like OpenAI deltas
- Treating `content` as always a plain string instead of a block array

## Sources

- Anthropic Messages API examples: <https://docs.anthropic.com/en/api/messages-examples>
- Anthropic streaming docs: <https://docs.anthropic.com/en/docs/build-with-claude/streaming>
- Anthropic tool use overview: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview>
