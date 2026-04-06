# DMXAPI Relay

## Summary

Use DMXAPI when the project needs a hosted aggregation layer that exposes multiple provider-style protocols behind one platform. DMXAPI is not a native model vendor. It is a relay service with OpenAI-style, Responses-style, Claude-style, and Gemini-style entry points.

Treat it as a compatibility gateway, not as a first-party provider.

## Auth and Base URL

DMXAPI docs describe several public bases:

- `https://www.dmxapi.cn/v1`
- `https://www.dmxapi.com/v1/`
- `https://www.dmxapi.cn`

Common auth:

- `Authorization: Bearer $DMXAPI_API_KEY`

For Gemini-native routes, the docs also show API key usage on the URL query string:

- `?key=$DMXAPI_API_KEY`

## Protocol families

DMXAPI publicly documents at least these request families:

1. OpenAI chat-completions style
2. OpenAI Responses
3. Claude-native compatibility
4. Gemini-native `generateContent`

So the main decision is which protocol family your app should target, not "what is the one DMXAPI schema."

## Minimal OpenAI-style chat request

```bash
curl https://www.dmxapi.cn/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DMXAPI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
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

## Responses notes

DMXAPI explicitly documents a Responses-compatible format.

Practical rule:

- if the app expects modern OpenAI Responses semantics, use the Responses route
- if the app is built around classic chat completions, use `/v1/chat/completions`

Do not assume these two routes are interchangeable just because the same relay exposes both.

## Claude-compatible notes

The public docs explicitly say Claude original format is supported on the DMXAPI domain.

That means for Anthropic-style integrations you should expect:

- `/v1/messages`
- `x-api-key` or auth style compatible with Claude-family tooling
- Anthropic-style content blocks and SSE lifecycle semantics

Parse Claude responses like Anthropic, not like OpenAI deltas.

## Gemini-native notes

DMXAPI also documents Gemini-native routes such as:

- `POST /v1beta/models/{model}:generateContent`

Example pattern from the docs:

```bash
curl "https://www.dmxapi.cn/v1beta/models/gemini-2.5-flash:generateContent?key=$DMXAPI_API_KEY" \
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

## Embeddings notes

DMXAPI documents an embeddings route:

- `POST /v1/embeddings`

That is useful when the app wants both generation and retrieval features through the same relay.

## Streaming notes

Streaming behavior depends on the chosen route family:

- chat-completions route -> OpenAI-style streaming
- Claude route -> Anthropic-style SSE lifecycle
- Gemini route -> Gemini-style content stream
- Responses route -> Responses-style event model

Do not reuse one parser across all four.

## Development guidance

When integrating DMXAPI:

1. choose the route family first
2. replace the official upstream base URL with the DMXAPI base
3. send one minimal request on that route
4. parse output using that protocol family's native semantics
5. only then add streaming, tools, or structured output

## Common pitfalls

- Assuming DMXAPI only supports OpenAI-compatible requests
- Forgetting to replace the base URL when reusing official client code
- Treating the relay as if it guarantees full upstream-native behavior
- Using Gemini-native docs but trying to parse the result like OpenAI chat

## Sources

- DMXAPI docs home: <https://doc.dmxapi.com/>
- DMXAPI Chinese docs home: <https://doc.dmxapi.com/zh/>
- DMXAPI quick start: <https://doc.dmxapi.com/jichu.html>
- DMXAPI common endpoints: <https://doc.dmxapi.com/jiekou.html>
- DMXAPI Responses API note: <https://doc.dmxapi.com/responses.html>
- DMXAPI Gemini-native docs: <https://doc.dmxapi.com/gemini-chat.html>
- DMXAPI Gemini JSON docs: <https://doc.dmxapi.com/gemini-json.html>
- DMXAPI embeddings docs: <https://doc.dmxapi.com/embedding.html>
