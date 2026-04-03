# OpenAI Native API

## Summary

Use OpenAI's native API when the user is integrating OpenAI directly or when a provider explicitly exposes the OpenAI Responses wire format. For new projects, prefer the Responses API over older Chat Completions flows unless the existing codebase is already built around chat completions.

## Auth and Base URL

- Base URL: `https://api.openai.com/v1`
- Auth header: `Authorization: Bearer $OPENAI_API_KEY`
- Content type: `application/json`

## Primary text-generation endpoint

- Preferred: `POST /responses`
- Legacy but still common: `POST /chat/completions`

## Minimal request

```bash
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.4",
    "input": [
      {
        "role": "user",
        "content": [
          { "type": "input_text", "text": "Write a one-line hello in Python." }
        ]
      }
    ]
  }'
```

## Response shape

Common fields to read:

- `id`
- `model`
- `output`
- `output_text`

In raw structured output, the generated text typically lives inside `output[*].content[*]` blocks. `output_text` is the convenient flattened form when available.

## Streaming notes

- Enable with `"stream": true`
- The Responses API streams server-sent events
- Expect incremental text events and a final completion event
- Your parser should treat the stream as event frames, not newline-delimited JSON blobs

## Tool-calling notes

Declare tools at the top level with a `tools` array.

Minimal function tool shape:

```json
{
  "type": "function",
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
```

Handle tool calls as structured model output, then execute the tool and continue the conversation with the tool result in the next request.

## Structured-output notes

For schema-constrained output, prefer a JSON schema format instead of prompt-only "return JSON" instructions.

Typical pattern:

- set `text.format.type` to `json_schema`
- provide the schema under `text.format.schema`

This is stronger than best-effort JSON prompting and is the right default for machine-consumed output.

## Multimodal notes

OpenAI Responses supports multimodal input blocks. For image input, send content items such as:

```json
{
  "type": "input_image",
  "image_url": "https://example.com/image.png"
}
```

or the corresponding inline image form when needed.

## Embeddings notes

- Endpoint: `POST /embeddings`
- Pattern: send `model` plus `input`
- Use this separately from Responses

## Common pitfalls

- Treating Responses like Chat Completions and looking only for `choices[0].message.content`
- Parsing streaming output as plain JSON instead of SSE
- Using prompt-only JSON instructions instead of schema-based structured output where reliability matters
- Forgetting that some OpenAI-compatible gateways do not fully implement the current Responses API

## Sources

- OpenAI Responses migration guide: <https://platform.openai.com/docs/guides/migrate-to-responses>
- OpenAI API docs root: <https://platform.openai.com/docs/api-reference>
