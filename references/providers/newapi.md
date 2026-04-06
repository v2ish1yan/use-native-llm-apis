# NewAPI Gateway

## Summary

Use NewAPI when the project needs a self-hosted or managed multi-provider gateway rather than one vendor's native API. NewAPI is a routing and API-management layer that can expose multiple protocol families behind one deployment.

Treat it as a gateway, not a model vendor.

## Auth and Base URL

Base URL depends on the deployment:

- self-hosted NewAPI server
- managed NewAPI deployment

Auth:

- `Authorization: Bearer $NEWAPI_API_KEY`

Content type:

- `Content-Type: application/json`

## Supported protocol families

NewAPI publicly documents multiple upstream-facing formats, including:

- OpenAI Chat Completions
- OpenAI Responses
- Anthropic Chat
- DeepSeek Chat
- Google / Gemini chat-style routes

That means the main integration decision is not "what is the one true NewAPI request body" but "which protocol surface has this deployment enabled for this app."

## Primary access pattern

For application code, NewAPI is usually approached through one of two protocol families:

1. OpenAI-compatible chat route
2. OpenAI-compatible responses route

The exact enabled models, tools, and upstream capability depend on the NewAPI deployment configuration.

## Minimal OpenAI-style chat request

```bash
curl https://YOUR_NEWAPI_BASE_URL/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "messages": [
      {
        "role": "developer",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

Typical response field for text:

- `choices[0].message.content`

## Minimal Responses-style request

```bash
curl https://YOUR_NEWAPI_BASE_URL/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $NEWAPI_API_KEY" \
  -d '{
    "model": "gpt-4.1",
    "instructions": "You are a helpful assistant.",
    "input": "Hello!",
    "stream": true
  }'
```

Common response fields:

- `id`
- `status`
- `model`
- `output`
- `usage`

If the app expects OpenAI Responses semantics, treat NewAPI as a deployment-specific gateway that mirrors that surface rather than as a generic vendor abstraction.

## Streaming notes

- NewAPI documents streaming on the Responses route
- actual stream shape follows the selected protocol family
- do not assume every deployment enables the same streaming features across all upstream models

Practical rule:

- if the app is using `/v1/chat/completions`, expect OpenAI-style chunk handling
- if the app is using `/v1/responses`, expect Responses-style event handling

## Tool-calling notes

Tool-calling capability depends on both:

- the protocol family exposed by the deployment
- the upstream provider or model actually backing the request

Do not promise tool support from NewAPI alone. Verify:

- the chosen route
- the chosen model
- the deployment's enabled upstream provider

## Structured-output notes

Structured output is practical when the deployment exposes a protocol family that already supports it, especially:

- OpenAI-style `response_format`
- Responses-style structured output features

But strict guarantees still depend on the underlying upstream model and route, not on the NewAPI brand alone.

## Development guidance

When integrating NewAPI into an app:

1. confirm the deployment base URL
2. confirm which protocol family the app should target
3. test one minimal request on that protocol surface
4. only then add streaming, tools, or structured output

## Common pitfalls

- Treating NewAPI as if it had one single canonical wire format
- Writing code against `/v1/chat/completions` while assuming `/v1/responses` behavior
- Forgetting that model availability differs between deployments
- Assuming upstream capabilities exist just because the gateway supports the route shape

## Sources

- NewAPI docs root: <https://docs.newapi.pro/en/>
- NewAPI API overview: <https://docs.newapi.pro/api/>
- NewAPI OpenAI chat docs: <https://docs.newapi.pro/api/openai-chat/>
- NewAPI OpenAI responses docs: <https://docs.newapi.pro/api/openai-responses/>
- NewAPI newer Responses docs page: <https://docs.newapi.pro/en/docs/api/ai-model/chat/openai/createresponse>
