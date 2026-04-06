# Compshare / ModelVerse Gateway

## Summary

Use Compshare when the project needs a hosted multi-model gateway with official OpenAI-compatible, Anthropic-compatible, Gemini-compatible, and Responses-compatible surfaces. Compshare exposes this through its ModelVerse API service, not as a first-party model vendor.

Treat it as a gateway with multiple protocol families.

## Auth and Base URL

OpenAI-compatible base URL:

- `https://api.modelverse.cn/v1`

Common auth:

- `Authorization: Bearer $MODELVERSE_API_KEY`

The public docs also expose additional protocol surfaces on the same platform:

- Anthropic-style `POST /v1/messages`
- Gemini-style `POST /v1beta/models/*`
- Responses-style `POST /v1/responses`

## Protocol families

Compshare publicly documents at least these request families:

1. OpenAI Chat Completions
2. OpenAI Responses
3. Anthropic Messages
4. Gemini `generateContent` / streaming model routes

That means the main implementation question is not "what is the one true Compshare body" but "which protocol surface should this app target."

## Minimal OpenAI-style chat request

```bash
curl https://api.modelverse.cn/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $MODELVERSE_API_KEY" \
  -d '{
    "model": "deepseek-v3-1",
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

## Minimal Anthropic-style request

```bash
curl https://api.modelverse.cn/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $MODELVERSE_API_KEY" \
  -d '{
    "model": "claude-sonnet-4-5-20250929",
    "max_tokens": 512,
    "messages": [
      {
        "role": "user",
        "content": "Write a one-line hello in Python."
      }
    ]
  }'
```

Use Anthropic-style response parsing:

- text usually arrives in `content` blocks

One important limitation from the docs:

- `/v1/messages` is for Claude-family models
- other families such as GPT, Gemini, and DeepSeek should use `/v1/chat/completions`

## Minimal Gemini-style request

```bash
curl "https://api.modelverse.cn/v1beta/models/gemini-2.5-flash:generateContent?key=$MODELVERSE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          { "text": "Write a one-line hello in Python." }
        ]
      }
    ]
  }'
```

Use Gemini-style parsing:

- `candidates[0].content.parts[0].text`

## Responses notes

Compshare documents `POST /v1/responses` as part of its OpenAPI protocol list.

Practical rule:

- if the app already expects OpenAI Responses semantics, prefer the Responses route
- if the app is built around classic chat-completions, stay on `/v1/chat/completions`

Also note from the platform FAQ:

- some model families such as GPT-5 Codex-style models may only support the Responses route

## Streaming notes

- OpenAI-compatible chat supports streaming
- Anthropic-compatible docs include streaming examples
- Gemini-compatible docs include stream generation routes

Do not reuse one parser everywhere:

- `/v1/chat/completions` -> OpenAI-style chunk parsing
- `/v1/messages` -> Anthropic-style SSE lifecycle
- `/v1beta/models/*` -> Gemini-style parsing

## Platform extension notes

Compshare's OpenAPI extension docs mention optional platform-specific fields such as:

- `web_search`
- `thinking_enabled`

These fields are only recognized by ModelVerse's own OpenAPI layer. Do not assume they exist on native upstream APIs.

## Development guidance

When integrating Compshare:

1. choose the protocol family first
2. confirm the model is valid for that route
3. send one minimal request on that route
4. parse output using that protocol's native semantics
5. only then add streaming, tools, or structured output

## Common pitfalls

- Treating Compshare as one uniform API instead of several protocol surfaces
- Calling `/v1/messages` with a non-Claude model
- Assuming all models support all listed protocol families
- Mixing OpenAI-compatible assumptions with ModelVerse-specific extension fields

## Sources

- Compshare docs root: <https://www.compshare.cn/docs>
- Compshare platform overview: <https://www.compshare.cn/docs/overview/platform/introduce>
- Compshare quick start: <https://www.compshare.cn/docs/modelverse/models/quick-start>
- Compshare OpenAI-compatible chat docs: <https://www.compshare.cn/docs/modelverse/models/text_api/openai_compatible>
- Compshare OpenAPI protocol list and extension fields: <https://www.compshare.cn/docs/modelverse/models/text_api/api-expand>
- Compshare Claude-compatible docs: <https://www.compshare.cn/docs/modelverse/models/text_api/claude_compatible>
- Compshare Gemini-compatible docs: <https://www.compshare.cn/docs/modelverse/models/text_api/gemini_compatible>
- Compshare FAQ: <https://www.compshare.cn/docs/modelverse/models/qa>
