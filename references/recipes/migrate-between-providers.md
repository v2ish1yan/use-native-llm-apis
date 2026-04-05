# Migrate Between Providers

Use this recipe when existing code already works for one provider and must be ported to another.

## Goal

Preserve behavior while changing the wire format as little as necessary.

## What to open first

1. `references/index.md`
2. `references/providers/index.md`
3. the source provider file linked from `references/providers/index.md`
4. the target provider file linked from `references/providers/index.md`
5. `references/comparisons/request-shape-differences.md`
6. one of the other comparison files if the task also involves streaming, tools, or structured output

If either provider file is unclear, return to `references/providers/index.md` instead of guessing.

## Migration order

1. Move auth and base URL first.
2. Remap the top-level request shape.
3. Remap system prompt placement.
4. Remap user content nesting.
5. Remap response parsing.
6. Remap advanced features such as streaming, tools, or schemas.

## Side-by-side migration map

Before renaming fields, lay out source and target:

```text
Source (OpenAI Chat Completions)     Target (Anthropic Messages)
─────────────────────────────────    ──────────────────────────────
POST /v1/chat/completions            POST /v1/messages
Authorization: Bearer $KEY           x-api-key: $KEY
(no version header)                  anthropic-version: 2023-06-01

Body:                                Body:
{                                    {
  "model": "gpt-4o",                  "model": "claude-sonnet-4-5",
  "messages": [                       "max_tokens": 1024,
    {"role": "system",                "system": "You are helpful.",
     "content": "You are helpful."},  "messages": [
    {"role": "user",                    {"role": "user",
     "content": "Hello"}                 "content": "Hello"}
  ]                                    ]
}                                    }

Response text:                       Response text:
choices[0].message.content           content.find(b => b.type === "text").text
```

## High-risk mapping table

| Concern | OpenAI | Anthropic | Gemini |
|---------|--------|-----------|--------|
| System prompt | `messages[0].role: "system"` | top-level `system` field | `systemInstruction` or first turn |
| User content | `messages[].content` (string or array) | `messages[].content` (block array) | `contents[].parts[].text` |
| Tool schema field | `tools[].parameters` | `tools[].input_schema` | `tools[].functionDeclarations[]` |
| Tool result | `role: "tool"` message | `tool_result` content block | `functionResponse` part |
| Stream events | `data: {"choices":[{"delta":...}]}` | named SSE events | chunked JSON or SSE |
| JSON mode | `response_format.type` | tool-mediated or constrained | `responseMimeType` |

## Safe migration pattern

- Keep the old request next to the new one while porting.
- Change one concern at a time.
- Compare raw requests and raw responses, not only post-processed app objects.
- If the old code used an abstraction layer, temporarily peel it back until the new wire format is correct.

## Exit criteria

This recipe is complete when:

- the target provider returns a successful response
- the app reads the correct output field
- advanced features are re-validated instead of assumed
